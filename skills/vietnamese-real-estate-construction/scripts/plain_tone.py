# -*- coding: utf-8 -*-
# synced from shared/scripts/plain_tone.py (2866527c5d4c2eed) — edit shared/ source, not this copy
"""Plain-tone rules PLAIN001-PLAIN007 for ``validate_copy.py``.

Pure Python 3.9+ standard library. Sibling module of ``validate_copy.py``, loaded by
file path (like ``writing_context.py``), not a ``rules_*.py`` domain module.

The rules catch prose that passes every mechanical check yet reads as long-winded
and machine-written. Data lives in ``references/plain-vietnamese.md`` (the phrase
table) and is parsed here; this file holds the checks. Findings are reported
through ``emit(rule, severity, lineno, col, snippet, message, hint)``.
"""
from __future__ import annotations

import bisect
import re
from typing import Callable, Dict, List, Optional, Sequence, Tuple

DEFAULT_MAX_SENTENCE_WORDS = 30
MAX_PARENTHESES = 2

RULE_DOCS: Dict[str, str] = {
    "PLAIN001": "sentence is too long to read in one pass (default > 30 words); split it",
    "PLAIN002": "audit label (FACT / INFERENCE / ASSUMPTION / UNKNOWN) left in prose",
    "PLAIN003": "meta opener that announces the text instead of saying the point",
    "PLAIN004": "filler phrase that adds length and no meaning",
    "PLAIN005": "“không chỉ … mà còn” in one sentence; give each fact its own sentence",
    "PLAIN006": "spaced dash used as an aside inside a sentence; use a full stop or a comma",
    "PLAIN007": "more than two parentheses in one sentence; move the detail to its own sentence",
}

Emit = Callable[[str, str, int, int, str, str, str], None]
TableParser = Callable[[str, str], Tuple[List[str], List[List[str]]]]
Unwrap = Callable[[str], str]

PHRASE_MARKER = "<!-- machine-readable: plain-phrases -->"


class PlainPhrases:
    """Phrase list from ``plain-vietnamese.md``: ``(phrase, rewrite hint)`` pairs per kind."""

    def __init__(self) -> None:
        self.labels: List[Tuple[str, str]] = []
        self.openers: List[Tuple[str, str]] = []
        self.fillers: List[Tuple[str, str]] = []
        self._compiled: Optional[tuple] = None

    def compiled(self) -> tuple:
        """``(labels, openers, fillers)``: lists of ``(regex, phrase, hint)``, built once."""
        if self._compiled is None:
            self._compiled = (
                [(re.compile(rf"(?<![\w-]){re.escape(p)}(?![\w-])"), p, h) for p, h in self.labels],
                [(re.compile(rf"^[\s*_>\"“‘'(\[]*{_phrase_body(p)}(?!\w)", re.IGNORECASE), p, h)
                 for p, h in self.openers],
                [(re.compile(rf"(?<!\w){_phrase_body(p)}(?!\w)", re.IGNORECASE), p, h)
                 for p, h in self.fillers],
            )
        return self._compiled


def _phrase_body(phrase: str) -> str:
    return r"[\s ]+".join(re.escape(word) for word in phrase.split())


def parse_phrases(text: str, table_with_header: TableParser, unwrap: Unwrap) -> PlainPhrases:
    """Build :class:`PlainPhrases` from the markdown text of ``plain-vietnamese.md``."""
    phrases = PlainPhrases()
    _header, rows = table_with_header(text, PHRASE_MARKER)
    targets = {"label": phrases.labels, "opener": phrases.openers, "filler": phrases.fillers}
    for row in rows:
        if len(row) < 2:
            continue
        phrase, kind = unwrap(row[0]), unwrap(row[1]).lower()
        hint = row[2].strip() if len(row) > 2 else ""
        if phrase and phrase != "—" and kind in targets:
            targets[kind].append((phrase, hint))
    return phrases


# --------------------------------------------------------------------------- #
# Prose blocks and sentences
# --------------------------------------------------------------------------- #
_HEADING_RE = re.compile(r"^\s{0,3}#{1,6}(?:\s|$)")
_TABLE_RE = re.compile(r"^\s*\|")
_RULER_RE = re.compile(r"^\s*(?:-{3,}|\*{3,}|_{3,})\s*$")
_LIST_RE = re.compile(r"^\s*(?:[-*+]|\d{1,3}[.)])\s+")
_QUOTE_RE = re.compile(r"^\s*>")
_COMMENT_RE = re.compile(r"<!--.*?-->")
_SENTENCE_END_RE = re.compile(r"[.!?…]+(?=\s|$)")
# (joined start offset, line number, column of the part's first character)
_Part = Tuple[int, int, int]


class _Block:
    """Consecutive prose lines joined with single spaces, with a map back to line/column."""

    def __init__(self) -> None:
        self.text = ""
        self._starts: List[int] = []
        self._parts: List[_Part] = []

    def add(self, lineno: int, col: int, text: str) -> None:
        if self.text:
            self.text += " "
        self._starts.append(len(self.text))
        self._parts.append((len(self.text), lineno, col))
        self.text += text

    def locate(self, offset: int) -> Tuple[int, int]:
        index = max(0, bisect.bisect_right(self._starts, offset) - 1)
        start, lineno, col = self._parts[index]
        return lineno, col + (offset - start) + 1


def _front_matter_end(lines: Sequence[str]) -> int:
    if lines and lines[0].strip() == "---":
        for index in range(1, len(lines)):
            if lines[index].strip() in ("---", "..."):
                return index + 1
    return 0


def prose_blocks(lines: Sequence[str]) -> List[_Block]:
    """Group Markdown-ish lines into prose blocks.

    Blank lines, headings, table rows, rulers, quoted lines (``>``) and the start of a list
    item end a block. Headings, tables, rulers, quotes and front matter are not the
    writer's prose and are dropped; list markers are stripped so a block starts with its
    first word.
    """
    blocks: List[_Block] = []
    current: Optional[_Block] = None
    for index in range(_front_matter_end(lines), len(lines)):
        raw = _COMMENT_RE.sub(lambda m: " " * len(m.group(0)), lines[index])
        if (not raw.strip() or _HEADING_RE.match(raw) or _TABLE_RE.match(raw)
                or _RULER_RE.match(raw) or _QUOTE_RE.match(raw)):
            current = None
            continue
        col = 0
        item = _LIST_RE.match(raw)
        if item:
            current = None
            col = item.end()
        col += len(raw[col:]) - len(raw[col:].lstrip())
        if current is None:
            current = _Block()
            blocks.append(current)
        current.add(index + 1, col, raw[col:].rstrip())
    return blocks


def sentences(block: _Block) -> List[Tuple[int, str]]:
    """``(offset in block.text, sentence)`` for each non-empty sentence of a block."""
    out: List[Tuple[int, str]] = []
    pos = 0
    for match in list(_SENTENCE_END_RE.finditer(block.text)) + [None]:
        end = match.end() if match else len(block.text)
        chunk = block.text[pos:end]
        stripped = chunk.lstrip()
        if stripped.strip():
            out.append((pos + len(chunk) - len(stripped), stripped.rstrip()))
        pos = end
    return out


def count_words(sentence: str) -> int:
    """Space-separated tokens that contain a letter or digit (one Vietnamese syllable each)."""
    return sum(1 for token in sentence.split() if re.search(r"\w", token))


# --------------------------------------------------------------------------- #
# Rules
# --------------------------------------------------------------------------- #
# A sentence with none of these letters is not Vietnamese prose (an English paragraph, a
# part number): the plain-tone rules leave it alone.
_VI_LETTER_RE = re.compile(
    "[ăâđêôơưàáạảãằắặẳẵầấậẩẫèéẹẻẽềếệểễìíịỉĩòóọỏõồốộổỗờớợởỡùúụủũừứựửữỳýỵỷỹ]", re.IGNORECASE
)
_NOT_ONLY_RE = re.compile(r"(?<!\w)không\s+(?:chỉ|những)(?!\w).*?(?<!\w)mà\s+còn(?!\w)", re.IGNORECASE)
_DASH_RE = re.compile(r"(?<=\S)\s[—–]\s(?=\S)")


def _clip(text: str, limit: int = 60) -> str:
    text = text.strip()
    return text if len(text) <= limit else text[: limit - 1] + "…"


def _check_sentence(block: _Block, offset: int, sentence: str, phrases: Optional[PlainPhrases],
                    max_words: int, severity: str, emit: Emit) -> None:
    if not _VI_LETTER_RE.search(sentence):
        return

    def at(position: int) -> Tuple[int, int]:
        return block.locate(offset + position)

    words = count_words(sentence)
    if words > max_words:
        line, col = at(0)
        emit("PLAIN001", severity, line, col, _clip(sentence),
             f"sentence has {words} words (limit {max_words})",
             "split it at the connectors (và, nhưng, nên, vì, mà); one idea per sentence")

    if phrases is not None:
        labels, openers, fillers = phrases.compiled()
        for regex, phrase, hint in labels:
            for m in regex.finditer(sentence):
                line, col = at(m.start())
                emit("PLAIN002", severity, line, col, m.group(0),
                     f"audit label “{phrase}” left in prose", hint)
        for regex, phrase, hint in openers:
            m = regex.match(sentence)
            if m:
                line, col = at(m.start())
                emit("PLAIN003", severity, line, col, _clip(m.group(0)),
                     f"meta opener “{phrase}” announces the text instead of saying the point", hint)
                break
        for regex, phrase, hint in fillers:
            for m in regex.finditer(sentence):
                line, col = at(m.start())
                emit("PLAIN004", severity, line, col, m.group(0),
                     f"filler “{m.group(0)}”", hint)

    m = _NOT_ONLY_RE.search(sentence)
    if m:
        line, col = at(m.start())
        emit("PLAIN005", severity, line, col, _clip(m.group(0)),
             "“không chỉ … mà còn” in one sentence",
             "give each fact its own sentence, or join them with “và”")

    dashes = [
        d for d in _DASH_RE.finditer(sentence)
        if not (sentence[: d.start()][-1:].isdigit() and sentence[d.end():][:1].isdigit())
    ]
    if dashes:
        line, col = at(dashes[0].start() + 1)
        emit("PLAIN006", severity, line, col, dashes[0].group(0).strip(),
             f"dash used as an aside ({len(dashes)} in this sentence)",
             "end the sentence with a full stop, or set the aside off with commas")

    parens = sentence.count("(")
    if parens > MAX_PARENTHESES:
        line, col = at(sentence.index("("))
        emit("PLAIN007", severity, line, col, _clip(sentence),
             f"{parens} parentheses in one sentence (limit {MAX_PARENTHESES})",
             "move each aside into its own sentence")


def check(lines: Sequence[str], emit: Emit, severity: str,
          phrases: Optional[PlainPhrases] = None,
          max_words: int = DEFAULT_MAX_SENTENCE_WORDS) -> None:
    """Run PLAIN001-PLAIN007 over NFC lines with code and URLs already blanked.

    ``phrases`` is the parsed phrase table; without it only the structural rules run
    (PLAIN001, PLAIN005, PLAIN006, PLAIN007).
    """
    for block in prose_blocks(lines):
        for offset, sentence in sentences(block):
            _check_sentence(block, offset, sentence, phrases, max_words, severity, emit)
