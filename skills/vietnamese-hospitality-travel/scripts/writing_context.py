# -*- coding: utf-8 -*-
# synced from shared/scripts/writing_context.py (42f36598d1a352bb) — edit shared/ source, not this copy
"""Writing-context rules CTX001-CTX005 and the stderr suggestion for ``validate_copy.py --context``.

Pure Python 3.9+ standard library. This is a sibling module, not a ``rules_*.py``
domain module: ``validate_copy.py`` loads it by file path and calls it only when a
context is declared (plus a stderr-only suggestion when none is).

Data lives in ``references/context-matrix.md`` and is parsed by the sibling
``context_matrix.py``; this file holds the checks. The rule contract matches the
domain engines: findings are reported through
``emit(rule, severity, lineno, col, snippet, message, hint)``.
"""
from __future__ import annotations

import re
from typing import Any, Callable, Dict, List, Optional, Sequence

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

# Compounds whose letters spell a forbidden address term but are not pronouns.
_COMPOUND_EXEMPT_RE = re.compile(
    r"(?<!\w)(?:"
    r"tao\s+(?:nhã|khang|đàn|loạn|phùng|tác|ngộ)|"
    r"mày\s+(?:mò|đay|râu)|"
    r"(?:một|tự|chính|bản\s+thân|thân|riêng|nửa)\s+mình|mình\s+(?:mẩy|đồng)|"
    r"cậu\s+(?:bé|ấm|út|mợ|chủ)"
    r")(?!\w)",
    re.IGNORECASE,
)
# Third-person or non-pronoun uses of the words that mark direct address.
_NOT_DIRECT_ADDRESS = r"(?!\s+(?:ấy|ta|kia|đó|hùng|em|chàng|trai|gái|dâu|giáo|ruột)(?!\w))"
_HEADER_FIELD_RE = re.compile(
    r"^\s*(?:#+\s|(?:subject|chủ\s+đề|tiêu\s+đề|to|đến|từ|from|cc|bcc|re|fwd|fw)\s*:)",
    re.IGNORECASE,
)
_PARTICLE_FALLBACK = ("ạ", "dạ", "vâng")

Emit = Callable[[str, str, int, int, str, str, str], None]
# Duck-typed views of context_matrix.ContextProfile / ContextMatrix (this module is
# loaded by path, so it cannot import its sibling by name).
Profile = Any
Matrix = Any


# --------------------------------------------------------------------------- #
# Rules
# --------------------------------------------------------------------------- #
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
    return [_COMPOUND_EXEMPT_RE.sub(lambda m: " " * len(m.group(0)), line) for line in lines]


def _quoted(terms: Sequence[str]) -> str:
    return ", ".join(f"“{t}”" for t in terms)


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
    technical = profile.reader == "technical"
    meanings: Dict[str, str] = {}
    spellings: List[str] = []
    for token, meaning, ambiguous in matrix.abbreviations:
        if ambiguous and technical:
            continue
        for form in {token, token.capitalize()} if len(token) > 1 else {token}:
            meanings[form] = meaning
            spellings.append(form)
    if not spellings:
        return
    alts = "|".join(re.escape(s) for s in sorted(spellings, key=len, reverse=True))
    regex = re.compile(rf"(?<![\w./@_-])(?:{alts})(?![\w/_@-])")
    severity = ERROR if profile.relation == "up" and profile.channel in ("email", "document") else WARN
    for i, line in enumerate(lines, 1):
        for m in regex.finditer(line):
            if re.search(r"\d\s*$", line[:m.start()]):
                continue  # 5k, 5 ns: a unit, not teencode
            word = m.group(0)
            full = meanings.get(word, "")
            emit("CTX003", severity, i, m.start() + 1, word,
                 f"chat abbreviation “{word}” ({full}) in the {profile.id} context",
                 f"write the full word “{full.split(' / ')[0]}”" if full else "")


def _check_email_frame(matrix: Matrix, lines: Sequence[str], emit: Emit) -> None:
    body = [(i, line) for i, line in enumerate(lines, 1) if line.strip()]
    while body and _HEADER_FIELD_RE.match(body[0][1]):
        body.pop(0)
    if not body:
        return
    lead = r"^[\s>*_\-]*"
    greeting_re = _any_word_re(matrix.greetings, lead=lead) if matrix.greetings else None
    signoff_re = _any_word_re(matrix.signoffs, lead=lead) if matrix.signoffs else None
    first_no, first_line = body[0]
    if greeting_re and not greeting_re.match(first_line):
        emit("CTX004", WARN, first_no, 1, first_line.strip()[:60],
             "email has no greeting line",
             "open with a greeting, e.g. “Kính gửi anh/chị,” or “Chào An,”")
    tail = body[-SIGNOFF_WINDOW_LINES:]
    if signoff_re and not any(signoff_re.match(line) for _n, line in tail):
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
    with pronoun compounds (``bạn bè``, ``quý giá``) blanked as well.
    """
    enabled = profile.enables
    if "CTX001" in enabled:
        _check_forbidden_terms(profile, cleaned, emit)
    if "CTX002" in enabled:
        _check_politeness(profile, matrix, cleaned, emit)
    if "CTX003" in enabled:
        _check_abbreviations(profile, matrix, lines, emit)
    if "CTX004" in enabled and profile.channel == "email":
        _check_email_frame(matrix, lines, emit)
    if "CTX005" in enabled:
        _check_executive_summary(matrix, lines, emit)


# --------------------------------------------------------------------------- #
# Suggestion (stderr hint only; never a finding)
# --------------------------------------------------------------------------- #
_LETTER_OPENER_RE = re.compile(r"(?:^|\n)[ \t>*_-]*(?:kính\s+gửi|dear)(?!\w)", re.IGNORECASE)
_MANAGER_OPENER_RE = re.compile(
    r"(?:^|\n)[ \t>*_-]*kính\s+gửi\s+(?:anh|chị|sếp)(?!\w)", re.IGNORECASE
)
_SELF_EM_RE = re.compile(
    r"(?<!\w)em\s+(?:xin|gửi|là|rất|đã|sẽ|muốn|cảm\s+ơn|kính|mong|báo\s+cáo|nhờ)(?!\w)",
    re.IGNORECASE,
)
_APPLICATION_RE = re.compile(
    r"(?<!\w)(?:ứng\s+tuyển|xin\s+việc|thư\s+xin\s+việc|hồ\s+sơ\s+ứng\s+tuyển)(?!\w)"
    r"|(?<!\w)(?:đính\s+kèm|gửi\s+kèm|kèm\s+theo)\s+CV(?!\w)",
    re.IGNORECASE,
)
_FRIEND_MAY_RE = re.compile(r"(?<!\w)mày(?!\w)", re.IGNORECASE)
_FRIEND_TAO_RE = re.compile(r"(?<!\w)tao(?!\w)", re.IGNORECASE)


def suggest_context(text: str) -> Optional[str]:
    """Return a preset id when strong signals appear, else ``None``. Pure and conservative."""
    if _LETTER_OPENER_RE.search(text) and _APPLICATION_RE.search(text):
        return "job-application"
    if _MANAGER_OPENER_RE.search(text) and _SELF_EM_RE.search(text):
        return "email-to-manager"
    blanked = _COMPOUND_EXEMPT_RE.sub(" ", text)
    if _FRIEND_MAY_RE.search(blanked) and _FRIEND_TAO_RE.search(blanked):
        return "chat-close-friend"
    return None
