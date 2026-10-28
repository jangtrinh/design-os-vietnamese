# -*- coding: utf-8 -*-
"""Writing-context rules CTX001-CTX005 for ``validate_copy.py --context``.

Pure Python 3.9+ standard library. This is a sibling module, not a ``rules_*.py``
domain module: ``validate_copy.py`` loads it by file path and calls it only when a
context is declared. The stderr suggestion lives in ``context_suggestion.py``.

Data lives in ``references/context-matrix.md`` and is parsed by the sibling
``context_matrix.py``; this file holds the checks. The rule contract matches the
domain engines: findings are reported through
``emit(rule, severity, lineno, col, snippet, message, hint)``.
"""
from __future__ import annotations

import re
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple

ERROR = "error"
WARN = "warning"

RULE_DOCS: Dict[str, str] = {
    "CTX001": "address or self term does not fit the declared writing context (--context)",
    "CTX002": "message to a superior addresses the reader but has no politeness particle (ạ / dạ / vâng)",
    "CTX003": "chat abbreviation / teencode in a context that is not a close chat",
    "CTX004": "email has no greeting line or no sign-off",
    "CTX005": "executive document has no summary or conclusion near the top",
}

# How far into a message the structural rules look. Conventions, not statute.
SUMMARY_WINDOW_LINES = 15
SIGNOFF_WINDOW_LINES = 6
SIGNATURE_SCAN_LINES = 12

# Compounds, idioms and third-person uses whose letters spell a forbidden term.
_COMPOUND_EXEMPT_RE = re.compile(
    r"(?<!\w)(?:"
    r"tao\s+(?:nhã|khang|đàn|loạn|phùng|tác|ngộ)|"
    r"mày\s+(?:mò|đay|râu)|"
    r"(?:một|tự|chính|bản\s+thân|thân|riêng|nửa|hết)\s+mình|mình\s+(?:mẩy|đồng)|về\s+phần\s+mình|"
    r"cậu\s+(?:bé|ấm|út|mợ|chủ)|"
    r"các\s+bạn\s+(?:thực\s+tập|sinh\s+viên|trẻ|ứng\s+viên|nhân\s+viên|học\s+sinh|đồng\s+nghiệp|"
    r"trong|ở|mới|nữ|nam|cùng)"
    r")(?!\w)",
    re.IGNORECASE,
)
# "bạn Lan": a capitalised name after bạn is a third person (case-sensitive on purpose).
_NAMED_THIRD_PERSON_RE = re.compile(r"(?<!\w)[Bb]ạn\s+[A-ZĐ][^\W\d_]*")
_FIRST_PERSON_RE = re.compile(r"(?<!\w)(?:tôi|em|con|cháu|chúng\s+tôi|chúng\s+em)(?!\w)", re.IGNORECASE)
_SENTENCE_RE = re.compile(r"[^.!?;]+")
_REFLEXIVE_RE = re.compile(r"(?<=của )mình(?!\w)", re.IGNORECASE)
# Third-person or non-pronoun uses of the words that mark direct address.
_NOT_DIRECT_ADDRESS = r"(?!\s+(?:ấy|ta|kia|đó|hùng|em|chàng|trai|gái|dâu|giáo|ruột)(?!\w))"
_HEADER_FIELD_RE = re.compile(
    r"^\s*(?:#+\s|(?:subject|chủ\s+đề|tiêu\s+đề|v\s*/\s*v|to|đến|từ|from|cc|bcc|re|fwd|fw)\s*:)",
    re.IGNORECASE,
)
_PARTICLE_FALLBACK = ("ạ", "dạ", "vâng")
_ADDRESS_RE = re.compile(r"[^\s@]+@[^\s@]+")
_QUOTE_MARKERS = (
    re.compile(r"^\s*>"),
    re.compile(r"^\s*(?:vào|trên|on)\b.{0,120}?(?:đã\s+viết|wrote)\s*:?\s*$", re.IGNORECASE),
    re.compile(r"^\s*-{2,}\s*(?:original\s+message|thư\s+gốc|tin\s+nhắn\s+gốc)\s*-{2,}\s*$", re.IGNORECASE),
)
_CONTACT_LINE_RE = re.compile(
    r"@|https?://|www\.|(?<!\d)(?:\+?84|0)[\d .-]{8,}\d"
    r"|^\s*(?:điện\s+thoại|đt|tel|phone|mobile|hotline|email|e-mail|website|web|địa\s+chỉ|address|fax|zalo|skype)\s*[:：]",
    re.IGNORECASE,
)

Emit = Callable[[str, str, int, int, str, str, str], None]
# Duck-typed views of context_matrix.ContextProfile / ContextMatrix (this module is
# loaded by path, so it cannot import its sibling by name).
Profile = Any
Matrix = Any


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _blank(match: "re.Match[str]") -> str:
    return " " * len(match.group(0))


def _word_re(term: str) -> "re.Pattern[str]":
    body = r"\s+".join(re.escape(w) for w in term.split())
    return re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)


def _any_word_re(terms: Sequence[str], lead: str = "", tail: str = "") -> "re.Pattern[str]":
    alts = "|".join(
        r"\s+".join(re.escape(w) for w in t.split())
        for t in sorted(terms, key=len, reverse=True)
    )
    return re.compile(rf"{lead}(?:{alts})(?!\w){tail}", re.IGNORECASE)


def _blank_compounds(lines: Sequence[str]) -> List[str]:
    """Blank idioms, third-person uses and first-person reflexives (``hết mình``, ``của mình``)."""
    def reflexive(sentence: "re.Match[str]") -> str:
        text = sentence.group(0)
        return _REFLEXIVE_RE.sub(_blank, text) if _FIRST_PERSON_RE.search(text) else text

    out = []
    for line in lines:
        line = _COMPOUND_EXEMPT_RE.sub(_blank, line)
        line = _NAMED_THIRD_PERSON_RE.sub(_blank, line)
        out.append(_SENTENCE_RE.sub(reflexive, line))
    return out


def _quote_start(lines: Sequence[str]) -> int:
    """Index of the first quoted-reply line, or ``len(lines)`` when there is none."""
    for index, line in enumerate(lines):
        if any(marker.match(line) for marker in _QUOTE_MARKERS):
            return index
    return len(lines)


def _body_lines(lines: Sequence[str]) -> List[Tuple[int, str]]:
    """Non-empty ``(lineno, text)`` pairs without leading header fields (Subject:, V/v:, ...)."""
    body = [(i, line) for i, line in enumerate(lines, 1) if line.strip()]
    while body and _HEADER_FIELD_RE.match(body[0][1]):
        body.pop(0)
    return body


def _quoted(terms: Sequence[str]) -> str:
    return ", ".join(f"“{t}”" for t in terms)


# --------------------------------------------------------------------------- #
# Rules
# --------------------------------------------------------------------------- #
def _check_forbidden_terms(profile: Profile, cleaned: Sequence[str], emit: Emit) -> None:
    severity = ERROR if profile.relation == "up" else WARN
    if profile.address_terms:
        hint = "this context addresses the reader as " + _quoted(profile.address_terms)
        if profile.self_terms:
            hint += " and refers to the writer as " + _quoted(profile.self_terms)
    else:
        hint = "this context is impersonal; avoid direct address"
    cleaned = _blank_compounds(cleaned)
    for term in profile.forbids:
        regex = _word_re(term)
        for i, line in enumerate(cleaned, 1):
            m = regex.search(line)
            if m:
                emit("CTX001", severity, i, m.start() + 1, m.group(0),
                     f"“{m.group(0)}” does not fit the {profile.id} context ({profile.label})", hint)
                break


def _check_politeness(profile: Profile, matrix: Matrix,
                      lines: Sequence[str], emit: Emit) -> None:
    alternatives = [a.strip() for term in profile.address_terms for a in term.split("/") if a.strip()]
    if not alternatives:
        return
    body = _body_lines(lines)
    if body and matrix.formal_openers and _any_word_re(
        matrix.formal_openers, lead=r"^[\s>*_\-]*"
    ).match(body[0][1]):
        return  # a formal opener already carries the respect
    address_re = re.compile(
        r"(?<!nước\s)(?<!tiếng\s)(?<!người\s)(?<!\w)(?:"
        + "|".join(re.escape(a) for a in alternatives)
        + r")(?!\w)" + _NOT_DIRECT_ADDRESS,
        re.IGNORECASE,
    )
    particle_re = _any_word_re(matrix.particles or _PARTICLE_FALLBACK, lead=r"(?<!\w)")
    first = None
    for i, line in enumerate(lines, 1):
        if particle_re.search(line):
            return
        m = address_re.search(line)
        if m and first is None:
            first = (i, m.start() + 1, m.group(0))
    if first:
        emit("CTX002", WARN, first[0], first[1], first[2],
             f"the {profile.id} context addresses a superior but the message has no politeness particle",
             "add “ạ”, “dạ” or “vâng” where the message asks or answers, e.g. “Em gửi anh báo cáo ạ.”")


def _check_abbreviations(profile: Profile, matrix: Matrix,
                         lines: Sequence[str], emit: Emit) -> None:
    skip_ambiguous = profile.reader == "technical" or profile.channel == "document"
    meanings: Dict[str, str] = {}
    spellings: List[str] = []
    for token, meaning, ambiguous, caps in matrix.abbreviations:
        if ambiguous and skip_ambiguous:
            continue
        forms = {token}
        if len(token) > 1:
            forms |= {token.capitalize()} | ({token.upper()} if caps else set())
        for form in forms:
            meanings[form] = meaning
            spellings.append(form)
    if not spellings:
        return
    alts = "|".join(re.escape(s) for s in sorted(spellings, key=len, reverse=True))
    regex = re.compile(rf"(?<![\w./@_-])(?:{alts})(?![\w/_@-]|\.\w)")
    severity = ERROR if profile.relation == "up" and profile.channel in ("email", "document") else WARN
    for i, line in enumerate(lines, 1):
        for m in regex.finditer(line):
            if re.search(r"\d\s*$", line[:m.start()]):
                continue  # 5k, 5 ns: a unit, not teencode
            word = m.group(0)
            full = meanings.get(word, "")
            alternatives = [part.strip() for part in full.split(" / ") if part.strip()]
            emit("CTX003", severity, i, m.start() + 1, word,
                 f"chat abbreviation “{word}” ({full}) in the {profile.id} context",
                 "write it out in full: " + " or ".join(f"“{a}”" for a in alternatives) if alternatives else "")


def _signoff_candidates(body: Sequence[Tuple[int, str]]) -> List[str]:
    """Lines that may hold the sign-off: the tail, plus the lines above the signature block."""
    tail = [line for _n, line in body[-SIGNOFF_WINDOW_LINES:]]
    scan_from = max(0, len(body) - SIGNATURE_SCAN_LINES)
    for index in range(scan_from, len(body)):
        if _CONTACT_LINE_RE.search(body[index][1]):
            above = [line for _n, line in body[max(0, index - SIGNOFF_WINDOW_LINES):index]]
            return tail + above
    return tail


def _check_email_frame(matrix: Matrix, lines: Sequence[str], emit: Emit) -> None:
    body = _body_lines(lines)
    if not body:
        return
    lead = r"^[\s>*_\-]*"
    greeting_re = _any_word_re(matrix.greetings, lead=lead) if matrix.greetings else None
    ending_re = (
        re.compile(rf"^[^\n]{{0,40}}?(?<!\w)(?:{'|'.join(re.escape(e) for e in matrix.greeting_endings)})(?!\w)",
                   re.IGNORECASE)
        if matrix.greeting_endings else None
    )
    signoff_re = _any_word_re(matrix.signoffs, lead=lead) if matrix.signoffs else None
    first_no, first_line = body[0]
    if greeting_re and not greeting_re.match(first_line) and not (ending_re and ending_re.match(first_line)):
        emit("CTX004", WARN, first_no, 1, first_line.strip()[:60],
             "email has no greeting line",
             "open with a greeting, e.g. “Kính gửi anh/chị,” or “Chào An,”")
    if signoff_re and not any(signoff_re.match(line) for line in _signoff_candidates(body)):
        last_no, last_line = body[-1]
        emit("CTX004", WARN, last_no, 1, last_line.strip()[:60],
             "email has no sign-off",
             "close with a sign-off before your name, e.g. “Trân trọng,” or “Thân,”")


def _check_executive_summary(matrix: Matrix, lines: Sequence[str], emit: Emit) -> None:
    if not matrix.summary_markers:
        return
    window = [(i, line) for i, line in enumerate(lines, 1) if line.strip()][:SUMMARY_WINDOW_LINES]
    if not window:
        return
    marker_re = _any_word_re(matrix.summary_markers, lead=r"(?<!\w)")
    if any(marker_re.search(line) for _n, line in window):
        return
    first_no, first_line = window[0]
    emit("CTX005", WARN, first_no, 1, first_line.strip()[:60],
         f"no summary or conclusion within the first {SUMMARY_WINDOW_LINES} non-empty lines",
         "open with “Tóm tắt” or “Đề xuất”: the decision first, the background after")


def check(profile: Profile, matrix: Matrix,
          lines: Sequence[str], cleaned: Sequence[str], emit: Emit) -> None:
    """Run every CTX rule the profile enables.

    ``lines`` are NFC lines with code and URLs blanked; ``cleaned`` are the same lines
    with pronoun compounds (``bạn bè``, ``quý giá``) blanked as well. For ``chat`` and
    ``email`` channels everything from the first quoted-reply marker on is ignored.
    """
    if profile.channel in ("chat", "email"):
        cut = _quote_start(lines)
        lines, cleaned = lines[:cut], cleaned[:cut]
    plain = [_ADDRESS_RE.sub(_blank, line) for line in lines]
    cleaned = [_ADDRESS_RE.sub(_blank, line) for line in cleaned]
    enabled = profile.enables
    if "CTX001" in enabled:
        _check_forbidden_terms(profile, cleaned, emit)
    if "CTX002" in enabled:
        _check_politeness(profile, matrix, cleaned, emit)
    if "CTX003" in enabled:
        _check_abbreviations(profile, matrix, plain, emit)
    if "CTX004" in enabled and profile.channel == "email":
        _check_email_frame(matrix, lines, emit)
    if "CTX005" in enabled:
        _check_executive_summary(matrix, lines, emit)
