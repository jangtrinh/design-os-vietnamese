# -*- coding: utf-8 -*-
"""Domain-specific validation rules for Vietnamese engineering and product writing.

Loaded automatically by validate_copy.py via the `rules_*.py` pattern.
Standard library only, plain tuples contract:
(rule_id, severity, lineno_or_col, snippet, message, hint)
"""
from __future__ import annotations

import re
import unicodedata

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "ENG001": "diacritics in a commit subject, branch name, or identifier",
    "ENG003": "direct address in a document whose register is impersonal",
    "ENG007": "hedged instruction in a runbook; steps take the imperative",
    "ENG008": "blaming the user in an error message; state the condition objectively",
    "PROD002": "agree/disagree scale in a survey — inflates scores via acquiescence bias",
    "PROD003": "app-store metadata over the platform character limit",
    "PROD004": "consent copy without an explicit purpose (Nghị định 13/2023/NĐ-CP)",
}

DOCTYPES = {
    "commit": "a git commit subject line — ASCII only",
    "branch": "a git branch name — ASCII only",
    "identifier": "code identifiers, i18n keys, filenames — ASCII only",
    "rfc": "an RFC or technical design doc — impersonal register",
    "postmortem": "a postmortem or incident report — impersonal register, no named individuals",
    "adr": "an architectural decision record — impersonal register",
    "runbook": "an operational runbook or disaster recovery procedure — imperative steps",
    "error-message": "UI error message or validation alert — objective, non-blaming",
    "survey": "a user research survey or questionnaire",
    "app-store-title": "an app-store title (30 characters)",
    "app-store-subtitle": "an app-store subtitle (30 characters)",
    "app-store-promo": "an App Store promotional text (170 characters)",
    "app-store-short-description": "a Play Store short description (80 characters)",
    "consent": "consent or permission copy collecting personal data",
}

ASCII_ONLY = ("commit", "branch", "identifier")
IMPERSONAL = ("rfc", "postmortem", "adr")

CHAR_LIMITS = {
    "app-store-title": 30,
    "app-store-subtitle": 30,
    "app-store-promo": 170,
    "app-store-short-description": 80,
}

# Direct address in impersonal documents
ADDRESS_RE = re.compile(r"(?<!\w)(bạn|quý khách|quý vị)(?!\w)", re.IGNORECASE)

# Hedged instructions in runbooks
HEDGE_RE = re.compile(r"(?<!\w)bạn\s+(nên|có thể|hãy)(?!\w)", re.IGNORECASE)

# Blaming the user in error messages
USER_BLAME_RE = re.compile(
    r"(?<!\w)(?:bạn\s+đã\s+nhập\s+sai|lỗi\s+của\s+bạn|do\s+bạn\s+nhập\s+sai|bạn\s+làm\s+sai|bạn\s+nhập\s+sai)(?!\w)",
    re.IGNORECASE,
)

# Survey agree/disagree bias
AGREE_SCALE_RE = re.compile(r"(?<!\w)(?:rất\s+)?(?:không\s+)?đồng\s*ý(?!\w)", re.IGNORECASE)
AGREE_QUESTION_RE = re.compile(r"(?<!\w)(?:có\s+)?đồng\s*ý\s+(?:rằng|với)(?!\w)", re.IGNORECASE)

# Consent copy purpose markers
PURPOSE_RE = re.compile(r"(?<!\w)(?:nhằm\s+mục\s+đích|để|mục\s+đích|phục\s+vụ)(?!\w)", re.IGNORECASE)
CONSENT_RE = re.compile(r"(?<!\w)(?:đồng\s+ý|cho\s+phép|chấp\s+thuận)(?!\w)", re.IGNORECASE)

# Non-ASCII regex
NON_ASCII_RE = re.compile(r"[^\x00-\x7F]+")

# JSON key extractor for identifier validation
JSON_KEY_RE = re.compile(r'"([^"\\]*)"\s*:')


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith("#") or stripped.startswith("<!--")


META_NEGATION_RE = re.compile(
    r"(?:đã\s+bãi\s+bỏ|bãi\s+bỏ\s+quy\s+định|bãi\s+bỏ\s+loại\s+hình|thay\s+thế\s+cho|"
    r"không\s+được(?:\s+phép)?\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết|ghi|viết|dùng|sử\s+dụng)|"
    r"nghiêm\s+cấm\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết|ghi|viết|dùng|sử\s+dụng)|"
    r"cấm\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết)\s+|"
    r"tránh\s+(?:viết|dùng|sử\s+dụng))\s*[^\n.;:]{0,25}$",
    re.IGNORECASE,
)


def _is_negated_or_meta(raw_line: str, match_start: int) -> bool:
    prefix = raw_line[max(0, match_start - 60):match_start]
    return bool(META_NEGATION_RE.search(prefix))


def _ascii_spans(doctype: str, raw: str):
    if doctype != "identifier":
        yield raw, 0
        return
    keys = list(JSON_KEY_RE.finditer(raw))
    if keys:
        for match in keys:
            yield match.group(1), match.start(1)
        return
    yield raw, 0


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype in ASCII_ONLY and not _is_comment_or_blank(raw):
        if doctype == "commit" and lineno > 1:
            return
        for text, offset in _ascii_spans(doctype, raw):
            for match in NON_ASCII_RE.finditer(text):
                yield (
                    "ENG001",
                    ERROR,
                    offset + match.start() + 1,
                    match.group(0),
                    f"non-ASCII in a {doctype}: “{match.group(0)}”",
                    "commit subjects, branch names and identifiers must be ASCII. In a resource file the key is ASCII and the value is Vietnamese; in a commit the subject is ASCII and the body may be Vietnamese",
                )

    if doctype in IMPERSONAL:
        for match in ADDRESS_RE.finditer(masked):
            yield (
                "ENG003",
                WARN,
                match.start() + 1,
                match.group(0),
                f"“{match.group(0)}” in a {doctype}",
                "this document describes a system, not a reader — write “Hệ thống sẽ…”, “Cần cấu hình…”, or drop the subject entirely",
            )

    if doctype == "runbook":
        for match in HEDGE_RE.finditer(masked):
            yield (
                "ENG007",
                WARN,
                match.start() + 1,
                match.group(0),
                f"hedged instruction “{match.group(0)}” in a runbook",
                "use the bare imperative — “Chạy migration trước”, not “Bạn nên chạy migration trước”",
            )

    if doctype == "error-message":
        for match in USER_BLAME_RE.finditer(masked):
            yield (
                "ENG008",
                WARN,
                match.start() + 1,
                match.group(0),
                f"blaming the user “{match.group(0)}” in an error message",
                "state the error condition and resolution objectively without blaming the user — e.g. “Email không đúng định dạng. Vui lòng kiểm tra lại.”",
            )

    if doctype == "survey":
        for match in AGREE_QUESTION_RE.finditer(masked):
            yield (
                "PROD002",
                WARN,
                match.start() + 1,
                match.group(0),
                "agree/disagree question wording",
                "ask about the property itself — “Mức độ dễ sử dụng của ứng dụng?” with endpoints “Rất khó – Rất dễ”",
            )
        for match in AGREE_SCALE_RE.finditer(masked):
            yield (
                "PROD002",
                WARN,
                match.start() + 1,
                match.group(0),
                f"agree/disagree scale point “{match.group(0)}”",
                "acquiescence bias inflates agreement by ~10 points; use an item-specific scale instead — see references/survey-design.md",
            )


def check_document(ctx):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype in CHAR_LIMITS:
        limit = CHAR_LIMITS[doctype]
        for lineno, raw in enumerate(ctx.lines, 1):
            text = raw.strip()
            if _is_comment_or_blank(raw):
                continue
            length = len(unicodedata.normalize("NFC", text))
            if length > limit:
                yield (
                    "PROD003",
                    WARN,
                    lineno,
                    1,
                    text[:40],
                    f"{length} characters, over the {limit}-character {doctype} limit",
                    "Vietnamese runs 25–30% longer than English — shorten rather than relying on the platform to truncate",
                )

    if doctype == "consent":
        text = "\n".join(ctx.masked)
        if CONSENT_RE.search(text) and not PURPOSE_RE.search(text):
            first_line = next((l.strip() for l in ctx.lines if not _is_comment_or_blank(l)), "")[:40]
            yield (
                "PROD004",
                WARN,
                1,
                1,
                first_line,
                "consent copy does not state an explicit purpose",
                "Nghị định 13/2023/NĐ-CP requires express, informed consent naming the purpose — “… nhằm mục đích [X]”",
            )
