# -*- coding: utf-8 -*-
"""Rules for Vietnamese school, academic, and EdTech writing that a calque table cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory educational terminology and pedagogical standards in Vietnam across
the 7-tier pedagogy continuum (Mầm non -> Tiểu học -> THCS/THPT -> GDNN -> Đại học -> Thạc sĩ -> Tiến sĩ & GS/PGS):
- VBHN 01/VBHN-BGDĐT: early childhood education developmental milestones across 5 domains
  (Thể chất, Nhận thức, Ngôn ngữ, Tình cảm - Kỹ năng xã hội, Thẩm mỹ); forbids numeric scores and K-12 grades.
- Thông tư 27/2020/TT-BGDĐT: primary school qualitative assessment ('cần cố gắng' instead of 'cần cải thiện').
- Thông tư 22/2021/TT-BGDĐT: secondary/high school overall grading scale (Tốt / Khá / Đạt / Chưa đạt)
  and abolition of 'học sinh tiên tiến'.
- Luật Giáo dục nghề nghiệp & Thông tư 04/2022/TT-BLĐTBXH: TVET modules, vocational credits, national skill standards.
- Thông tư 08/2021/TT-BGDĐT: higher education credit ('tín chỉ' vs 'tín dụng'), GPA decimal commas,
  and graduation works (khóa luận tốt nghiệp / đồ án tốt nghiệp).
- Thông tư 23/2021/TT-BGDĐT: Master's degree graduation works (luận văn thạc sĩ / đề án thạc sĩ).
- Thông tư 18/2021/TT-BGDĐT & QĐ 37/2018/QĐ-TTg: Doctoral dissertations (luận án tiến sĩ), academic degrees
  (Tiến sĩ, Thạc sĩ, Cử nhân) vs academic ranks / titles (Giáo sư, Phó Giáo sư), and scholarly register discipline.
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
    "EDU004": "misuse of Vietnamese academic rank (học hàm / chức danh) vs academic degree (học vị) (Luật Giáo dục & Quyết định 37/2018/QĐ-TTg)",
    "EDU005": "“tín dụng” for academic credit instead of “tín chỉ” (Thông tư 08/2021)",
    "EDU006": "GPA written with a dot decimal instead of the Vietnamese comma",
    "EDU007": "literal empty-state phrase on EdTech UI without an actionable CTA",
    "EDU008": "mismatched graduation work nomenclature across degree tiers (TT 08/2021, TT 23/2021, TT 18/2021)",
    "EDU009": "unpedagogical or harsh pronunciation feedback violating the Sandwich model",
    "EDU010": "children's EdTech onboarding/consent collecting minor data without mentioning parent/guardian consent ('phụ huynh' / 'người giám hộ' under Nghị định 13/2023/NĐ-CP Điều 20)",
    "EDU011": "numeric grading or K-12 academic classification applied to preschool children (VBHN 01/VBHN-BGDĐT)",
    "EDU012": "casual pronouns, teacher-student address, or unscientific claim inflation in postgraduate research (TT 23/2021, TT 18/2021)",
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
    "preschool-report": "Sổ theo dõi sức khỏe và đánh giá sự phát triển của trẻ mầm non (Nhà trẻ 3–36 tháng & Mẫu giáo 3–6 tuổi, VBHN 01/VBHN-BGDĐT)",
    "tvet-syllabus": "Chương trình / Mô-đun Giáo dục nghề nghiệp (Trung cấp / Cao đẳng, TT 04/2022/TT-BLĐTBXH)",
    "master-thesis": "Đề cương / Tóm tắt Luận văn Thạc sĩ hoặc Đề án Thạc sĩ (TT 23/2021/TT-BGDĐT, VQF Bậc 7)",
    "doctoral-dissertation": "Đề cương / Tóm tắt Luận án Tiến sĩ hoặc Chuyên đề Tiến sĩ (TT 18/2021/TT-BGDĐT, VQF Bậc 8)",
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

# EDU004: Academic rank (học hàm / chức danh: Giáo sư, Phó Giáo sư) vs academic degree (học vị / văn bằng: Tiến sĩ, Thạc sĩ, Cử nhân, Kỹ sư, Bác sĩ, Dược sĩ)
RANK_DEGREE_CONFUSION_RE = re.compile(
    r"(?<!\w)(?:"
    r"học\s+hàm(?:\s*[:–-]\s*|\s+)(?:tiến\s+sĩ|thạc\s+sĩ|cử\s+nhân|kỹ\s+sư|bác\s+sĩ|dược\s+sĩ)|"
    r"chức\s+danh(?:\s*[:–-]\s*|\s+)(?:tiến\s+sĩ|thạc\s+sĩ|cử\s+nhân|kỹ\s+sư|bác\s+sĩ|dược\s+sĩ)|"
    r"học\s+vị(?:\s*[:–-]\s*|\s+)(?:giáo\s+sư|phó\s+giáo\s+sư)|"
    r"(?:văn\s+bằng|bằng(?:\s+cấp)?)(?:\s*[:–-]\s*|\s+)(?:giáo\s+sư|phó\s+giáo\s+sư)"
    r")(?!\w)",
    re.IGNORECASE,
)

# EDU008: Mismatched graduation work nomenclature across degree tiers
GRAD_WORK_MISMATCH_RE = re.compile(
    r"(?<!\w)(?:"
    r"luận\s+án\s+(?:cử\s+nhân|đại\s+học|tốt\s+nghiệp\s+đại\s+học|tốt\s+nghiệp\s+cử\s+nhân|thạc\s+sĩ)|"
    r"khóa\s+luận\s+(?:thạc\s+sĩ|tiến\s+sĩ|cao\s+học)|"
    r"đồ\s+án\s+(?:thạc\s+sĩ|tiến\s+sĩ|cao\s+học)|"
    r"luận\s+văn\s+tiến\s+sĩ"
    r")(?!\w)",
    re.IGNORECASE,
)

# EDU011: Preschool assessment under VBHN 01/VBHN-BGDĐT forbids numeric scores and K-12 academic performance tiers
PRESCHOOL_NUMERIC_GRADE_RE = re.compile(
    r"(?<!\w)(?:"
    r"điểm\s+\d+(?:[.,]\d+)?(?:\s*/\s*10)?|"
    r"\d+(?:[.,]\d+)?\s*(?:/\s*10\s*điểm|/\s*10\b|\s*điểm(?!\s+danh))|"
    r"xếp\s+loại\s+(?:học\s+lực\s+)?[ABCDEF]\b|"
    r"(?:xếp\s+loại\s+học\s+lực|học\s+lực|xếp\s+loại)\s+(?:xuất\s+sắc|giỏi|khá|trung\s+bình|yếu|kém)"
    r")(?!\w)",
    re.IGNORECASE,
)

# EDU012: In postgrad theses/dissertations or edu-postgrad register: casual/K-12 pronouns or unscientific claim inflation
POSTGRAD_CASUAL_PRONOUNS_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:cô|thầy)\s+(?:khen|nhắc|bảo)\s+(?:con|các\s+em|em)|"
    r"(?:thầy|cô)\s+nhắc\s+các\s+em|"
    r"(?:các\s+em|các\s+con)\s+(?:hãy|chú\s+ý|cần)|"
    r"bạn\s+hãy|"
    r"(?:mình|chúng\s+mình)\s+sẽ"
    r")(?!\w)",
    re.IGNORECASE,
)

POSTGRAD_CLAIM_INFLATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"chứng\s+minh\s+tuyệt\s+đối|"
    r"(?:chính\s+xác|chuẩn\s+xác)\s+tuyệt\s+đối\s+100%|"
    r"(?:tuyệt\s+đối\s+)?100%\s+không\s+có\s+sai\s+số|"
    r"không\s+(?:hề\s+)?có\s+sai\s+số(?:\s+nào)?|"
    r"kết\s+quả\s+hoàn\s+hảo\s+100%|"
    r"tuyệt\s+đối\s+không\s+(?:bao\s+giờ\s+)?sai\s+lệch"
    r")(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str):
    doctype = ctx.doctype
    register = getattr(ctx, "register", None)

    # EDU004: Academic rank vs degree confusion (always checked in academic copy)
    for match in RANK_DEGREE_CONFUSION_RE.finditer(masked):
        yield (
            "EDU004",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"misuse of academic rank/degree “{match.group(0)}”",
            "Giáo sư (GS) and Phó Giáo sư (PGS) are academic ranks / titles (học hàm / chức danh), "
            "whereas Tiến sĩ (TS), Thạc sĩ (ThS), Cử nhân, and Kỹ sư are academic degrees (học vị / văn bằng) "
            "— see references/preschool-to-postgrad-continuum.md.",
        )

    # EDU008: Graduation work nomenclature mismatch across degree tiers
    for match in GRAD_WORK_MISMATCH_RE.finditer(masked):
        yield (
            "EDU008",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"mismatched graduation work nomenclature “{match.group(0)}”",
            "statutory graduation work nomenclature: undergraduate (Đại học) uses “khóa luận tốt nghiệp” "
            "or “đồ án tốt nghiệp” (TT 08/2021); Master's (Thạc sĩ) uses “luận văn thạc sĩ” or “đề án thạc sĩ” "
            "(TT 23/2021); Doctorate (Tiến sĩ) exclusively uses “luận án tiến sĩ” (TT 18/2021).",
        )

    # EDU011: Preschool assessment under VBHN 01/VBHN-BGDĐT
    is_preschool = (doctype == "preschool-report") or (
        not doctype and bool(re.search(r"(?<!\w)(?:mầm\s+non|mẫu\s+giáo|nhà\s+trẻ)(?!\w)", ctx.text or "", re.IGNORECASE))
    )
    if is_preschool:
        for match in PRESCHOOL_NUMERIC_GRADE_RE.finditer(masked):
            yield (
                "EDU011",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"numeric grading / K-12 classification “{match.group(0)}” in preschool context",
                "under VBHN 01/VBHN-BGDĐT, early childhood education does not use numeric scores "
                "or K-12 academic classifications (Giỏi/Khá/Trung bình/Yếu/Kém); assessment evaluates "
                "developmental milestones across 5 domains using qualitative observation and Đạt / Chưa đạt.",
            )

    # EDU012: In postgrad theses/dissertations or edu-postgrad register
    is_postgrad = (doctype in ("master-thesis", "doctoral-dissertation")) or (register == "edu-postgrad")
    if is_postgrad:
        for match in POSTGRAD_CASUAL_PRONOUNS_RE.finditer(masked):
            yield (
                "EDU012",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"casual/K-12 pronoun “{match.group(0)}” in postgraduate research",
                "Master's theses and Doctoral dissertations require formal academic register (TT 23/2021, "
                "TT 18/2021). Third-person address (nghiên cứu sinh, học viên, tác giả) is mandatory; "
                "never use casual pronouns or K-12 teacher-student address.",
            )
        for match in POSTGRAD_CLAIM_INFLATION_RE.finditer(masked):
            yield (
                "EDU012",
                ERROR,
                match.start() + 1,
                match.group(0),
                f"unscientific claim inflation “{match.group(0)}”",
                "scholarly dissertations forbid absolute unsubstantiated claims; specify statistical "
                "significance, confidence intervals, and empirical margins of error.",
            )

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
