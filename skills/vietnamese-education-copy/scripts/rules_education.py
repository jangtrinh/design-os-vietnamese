# -*- coding: utf-8 -*-
"""Rules for Vietnamese school, academic, and EdTech writing that a calque table cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory educational terminology and pedagogical standards in Vietnam:
- Thông tư 22/2021/TT-BGDĐT: secondary/high school overall grading scale (Tốt / Khá / Đạt / Chưa đạt)
  and abolition of 'học sinh tiên tiến'.
- Thông tư 27/2020/TT-BGDĐT: primary school qualitative assessment ('cần cố gắng' instead of 'cần cải thiện').
- Thông tư 08/2021/TT-BGDĐT: higher education credit ('tín chỉ' vs 'tín dụng') and GPA decimal commas.
- Thông tư 21/2019/TT-BGDĐT: diploma reissuance regulations ('cấp bản sao từ sổ gốc').
- Nghị định 13/2023/NĐ-CP Điều 20: double consent for children's personal data ('phụ huynh' / 'người giám hộ').
- Learning science & EdTech UX: Sandwich pronunciation feedback and actionable empty states.
"""
from __future__ import annotations

import re

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "EDU001": "abolished secondary (THCS/THPT) overall grading term (Thông tư 22/2021)",
    "EDU002": "“bạn” addressing a student in a teacher's voice",
    "EDU003": "“cần cải thiện” on a primary report card instead of “cần cố gắng” (Thông tư 27/2020)",
    "EDU005": "“tín dụng” for academic credit instead of “tín chỉ” (Thông tư 08/2021)",
    "EDU006": "GPA written with a dot decimal instead of the Vietnamese comma",
    "EDU007": "literal empty-state phrase on EdTech UI without an actionable CTA",
    "EDU009": "unpedagogical or harsh pronunciation feedback violating the Sandwich model",
    "EDU010": "children's EdTech onboarding/consent collecting minor data without mentioning parent/guardian consent ('phụ huynh' / 'người giám hộ' under Nghị định 13/2023/NĐ-CP Điều 20)",
}

DOCTYPES = {
    "primary-report-card": "a primary-school (tiểu học) report card or sổ liên lạc entry",
    "secondary-report-card": "a secondary/high-school (THCS/THPT) report card or học bạ entry",
    "teacher-to-student": "a teacher addressing a student directly",
    "transcript": "a university transcript or GPA statement",
    "diploma": "diploma issuance or reissuance copy",
    "higher-ed": "university administrative prose — syllabi, course descriptions, registration",
    "pronunciation-feedback": "AI / teacher pronunciation diagnostic feedback",
    "edtech-microcopy": "EdTech product UI strings, empty states, and notifications",
    "pedagogical-nudge": "pedagogical reminder and habit-loop notifications",
    "parental-analytics": "learning analytics and progress reports for parents",
    "child-consent": "child personal data collection, onboarding, or consent flow under NĐ 13/2023 Điều 20",
}

# The overall scale for THCS/THPT under TT 22/2021 is Tốt / Khá / Đạt / Chưa đạt.
LEGACY_OVERALL_RE = re.compile(
    r"(?:xếp\s+loại|đạt\s+loại|đạt\s+mức|xếp\s+loại\s+học\s+lực|học\s+lực)\s+(giỏi|trung\s+bình|yếu|kém)(?!\w)",
    re.IGNORECASE,
)
LEGACY_TITLE_RE = re.compile(r"(?<!\w)học\s+sinh\s+tiên\s+tiến(?!\w)", re.IGNORECASE)

# In teacher-to-student address, "bạn" is forbidden unless inside established compound nouns.
ADDRESS_BAN_RE = re.compile(
    r"(?<!\w)bạn(?!\s+(?:bè|học|đọc|hàng|đời|thân|đồng\s+hành))(?!\w)",
    re.IGNORECASE,
)

NEEDS_IMPROVEMENT_CALQUE_RE = re.compile(r"(?<!\w)cần\s+cải\s+thiện(?!\w)", re.IGNORECASE)

CREDIT_CALQUE_RE = re.compile(r"(?<!\w)tín\s+dụng(?!\w)", re.IGNORECASE)

GPA_DOT_RE = re.compile(r"(?<!\d)\d\.\d{1,2}\s*/\s*\d(?:\.\d{1,2})?(?!\d)")

EMPTY_STATE_CALQUE_RE = re.compile(
    r"(?<!\w)(?:trạng\s+thái\s+trống|không\s+có\s+dữ\s+liệu)(?!\w)",
    re.IGNORECASE,
)

HARSH_FEEDBACK_RE = re.compile(
    r"(?<!\w)(?:sai\s+rồi|bạn\s+(?:đã\s+)?phát\s+âm\s+sai|phát\s+âm\s+rất\s+tệ|điểm\s+(?:phát\s+âm\s+)?của\s+bạn\s+là\s*\d)(?!\w)",
    re.IGNORECASE,
)

CHILD_DATA_RE = re.compile(
    r"(?<!\w)(?:thu\s+thập\s+dữ\s+liệu\s+(?:của\s+)?(?:trẻ\s+em|học\s+sinh\s+tiểu\s+học|trẻ\s+dưới\s+16\s+tuổi|bé)|đăng\s+ký\s+tài\s+khoản\s+cho\s+(?:trẻ\s+em|bé|học\s+sinh\s+tiểu\s+học)|dữ\s+liệu\s+cá\s+nhân\s+của\s+trẻ|thu\s+thập\s+thông\s+tin\s+của\s+bé|xử\s+lý\s+dữ\s+liệu\s+trẻ\s+em|lưu\s+trữ\s+dữ\s+liệu\s+của\s+học\s+sinh\s+nhỏ)(?!\w)",
    re.IGNORECASE,
)
PARENT_CONSENT_RE = re.compile(
    r"(?<!\w)(?:phụ\s+huynh|người\s+giám\s+hộ|cha\s+mẹ)(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype == "secondary-report-card":
        for match in LEGACY_TITLE_RE.finditer(masked):
            yield (
                "EDU001",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"abolished title “{match.group(0)}”",
                "Thông tư 22/2021/TT-BGDĐT abolished “Học sinh Tiên tiến” as an overall "
                "classification title — use Tốt / Khá / Đạt / Chưa đạt.",
            )
        for match in LEGACY_OVERALL_RE.finditer(masked):
            yield (
                "EDU001",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"abolished overall classification “{match.group(0)}”",
                "the overall secondary grading scale under Thông tư 22/2021/TT-BGDĐT Điều 9 is "
                "Tốt / Khá / Đạt / Chưa đạt (“Khá” itself is unchanged).",
            )

    if doctype == "teacher-to-student":
        for match in ADDRESS_BAN_RE.finditer(masked):
            yield (
                "EDU002",
                WARN,
                match.start() + 1,
                match.group(0),
                f"“{match.group(0)}” addressing a student",
                "a teacher addresses a student as 'em' (secondary) or 'con' (primary), never "
                "'bạn' — see references/doc-registers.md.",
            )

    if doctype == "primary-report-card":
        for match in NEEDS_IMPROVEMENT_CALQUE_RE.finditer(masked):
            yield (
                "EDU003",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"“{match.group(0)}” instead of the statutory term",
                "Thông tư 27/2020/TT-BGDĐT Điều 7 mandates “cần cố gắng” for primary "
                "routine assessment, not the calque “cần cải thiện”.",
            )

    if doctype in ("higher-ed", "transcript"):
        for match in CREDIT_CALQUE_RE.finditer(masked):
            yield (
                "EDU005",
                WARN,
                match.start() + 1,
                match.group(0),
                f"“{match.group(0)}” for academic credit",
                "academic credit is “tín chỉ” (Thông tư 08/2021/TT-BGDĐT); “tín dụng” refers "
                "to financial credit. Reserve it for financial contexts like “tín dụng sinh viên”.",
            )

    if doctype == "transcript":
        for match in GPA_DOT_RE.finditer(masked):
            yield (
                "EDU006",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"GPA written with a dot decimal “{match.group(0)}”",
                "Vietnamese transcripts use a decimal comma — write "
                f"“{match.group(0).replace('.', ',')}”.",
            )

    if doctype == "edtech-microcopy":
        for match in EMPTY_STATE_CALQUE_RE.finditer(masked):
            yield (
                "EDU007",
                WARN,
                match.start() + 1,
                match.group(0),
                f"literal empty-state phrase “{match.group(0)}”",
                "never display raw “Trạng thái trống” / “Không có dữ liệu” — provide an "
                "encouraging, actionable Call to Action (see references/edtech-pedagogy.md).",
            )

    if doctype == "pronunciation-feedback":
        for match in HARSH_FEEDBACK_RE.finditer(masked):
            yield (
                "EDU009",
                WARN,
                match.start() + 1,
                match.group(0),
                f"unpedagogical negative feedback “{match.group(0)}”",
                "apply the Sandwich Feedback model (praise effort, provide constructive "
                "phoneme/tone tip, encourage growth mindset — see references/edtech-pedagogy.md).",
            )


def check_document(ctx):
    doctype = ctx.doctype
    if not doctype:
        return

    body = "\n".join(ctx.masked)

    # EDU010: Minor personal data processing without parent/guardian consent under NĐ 13/2023 Điều 20
    if doctype in ("child-consent", "edtech-microcopy"):
        match_cd = CHILD_DATA_RE.search(body)
        if match_cd and not PARENT_CONSENT_RE.search(body):
            line = body[:match_cd.start()].count("\n") + 1
            yield (
                "EDU010",
                WARN,
                line,
                1,
                match_cd.group(0),
                f"child data collection “{match_cd.group(0)}” missing parent/guardian consent",
                "Nghị định 13/2023/NĐ-CP Điều 20 requires verified consent from parent or legal guardian "
                "('phụ huynh' / 'người giám hộ') for collecting or processing personal data of children.",
            )
