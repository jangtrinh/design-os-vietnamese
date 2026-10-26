# -*- coding: utf-8 -*-
"""Rules for Vietnamese cybersecurity, incident response, ATTT Levels 1–5, and PDPD breach compliance.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and regulatory compliance across Vietnamese cybersecurity
operations (Luật An toàn thông tin mạng 2015, Luật An ninh mạng 2018), 72-hour personal data
breach notifications to A05 Ministry of Public Security (Nghị định 13/2023/NĐ-CP Điều 23),
strict 5-tier information system security classification (Nghị định 85/2016/NĐ-CP & Thông tư
12/2022/TT-BTTTT), standard InfoSec/SOC terminology, credential security, and CVE advisory completeness.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "breach-notification": "Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân gửi Cục A05 Bộ Công an (Điều 23 Nghị định 13/2023/NĐ-CP)",
    "security-advisory": "Cảnh báo an toàn thông tin / Khuyến nghị bản vá lỗ hổng bảo mật CVE (VNCERT/CC & NCSC)",
    "pentest-report": "Báo cáo kiểm thử xâm nhập (Pentest) & Đánh giá An toàn hệ thống thông tin theo cấp độ 1–5 (NĐ 85/2016 & TT 12/2022/TT-BTTTT)",
}

RULE_DOCS = {
    "SEC001": "personal data breach notification deadline exceeding 72 hours or omitting notification to A05 Ministry of Public Security under Article 23 Decree 13/2023/NĐ-CP (Nghị định 13/2023/NĐ-CP Điều 23 thời hạn 72 giờ gửi Cục A05 Bộ Công an)",
    "SEC002": "fabricated information system security level above level 5 ('cấp độ 6', 'cấp độ 7', 'ATTT cấp 6'); Decree 85/2016/NĐ-CP & Circular 12/2022/TT-BTTTT define strictly Levels 1 to 5",
    "SEC003": "awkward machine-translated cybersecurity terminology ('cuộc tấn công câu cá', 'phần mềm đòi tiền chuộc', 'kỹ thuật xã hội', 'bề mặt cuộc tấn công', 'tường lửa thế hệ tiếp theo', 'kiểm toán cây bút')",
    "SEC004": "phishing-like or insecure credential solicitation asking users to send passwords, PINs, OTPs, or CVV codes via email, message, or forms",
    "SEC005": "security advisory missing mandatory vulnerability severity rating ('Mức độ nghiêm trọng' / 'CVSS') or remediation guidance ('Biện pháp khắc phục' / 'Khuyến nghị cập nhật bản vá')",
    "SEC006": "misclassifying health, financial/banking, biometric, or location data as basic personal data instead of sensitive personal data under Article 2 Clause 4 Decree 13/2023/NĐ-CP",
}

# SEC001: Breach reporting deadline exceeding 72 hours / 3 days
BREACH_DEADLINE_DAYS_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:báo\s+cáo|thông\s+báo)(?:\s+[^\n.,;]*?)?\s+(?:sau|trong\s+vòng|trong\s+thời\s+hạn)\s+(\d+)\s+ngày|"
    r"(?:thời\s+hạn|thời\s+gian)\s+(?:báo\s+cáo|thông\s+báo)(?:\s+sự\s+cố|\s+vi\s+phạm)?(?:\s+là)?\s+(\d+)\s+ngày"
    r")(?!\w)",
    re.IGNORECASE,
)
BREACH_DEADLINE_HOURS_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:báo\s+cáo|thông\s+báo)(?:\s+[^\n.,;]*?)?\s+(?:sau|trong\s+vòng|trong\s+thời\s+hạn)\s+(\d+)\s+giờ|"
    r"(?:thời\s+hạn|thời\s+gian)\s+(?:báo\s+cáo|thông\s+báo)(?:\s+sự\s+cố|\s+vi\s+phạm)?(?:\s+là)?\s+(\d+)\s+giờ"
    r")(?!\w)",
    re.IGNORECASE,
)

# SEC002: Fabricated security levels above 5
FABRICATED_LEVEL_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:an\s+toàn\s+hệ\s+thống\s+thông\s+tin|an\s+toàn\s+thông\s+tin|attt|tiêu\s+chuẩn\s+bảo\s+mật|hệ\s+thống\s+thông\s+tin)(?:\s+[^\n.,;]*?)?\s+cấp\s+độ\s+([6-9]|10)|"
    r"(?:an\s+toàn\s+hệ\s+thống\s+thông\s+tin|an\s+toàn\s+thông\s+tin|attt|tiêu\s+chuẩn\s+bảo\s+mật|hệ\s+thống\s+thông\s+tin)(?:\s+[^\n.,;]*?)?\s+cấp\s+([6-9]|10)|"
    r"\battt\s+cấp\s+([6-9]|10)\b|"
    r"cấp\s+độ\s+([6-9]|10)\s+(?:theo\s+)?(?:Nghị\s+định\s+85|NĐ\s+85|Thông\s+tư\s+12|TT\s+12|Bộ\s+TT&TT|Bộ\s+Thông\s+tin)|"
    r"cấp\s+độ\s+([6-9]|10)\s+(?:về\s+)?(?:an\s+toàn|bảo\s+mật)"
    r")(?!\w)",
    re.IGNORECASE,
)

# SEC003: Awkward machine-translated cybersecurity terminology
INFOSEC_CALQUES: Tuple[Tuple[re.Pattern, str, str], ...] = (
    (
        re.compile(r"(?<!\w)(?:cuộc\s+tấn\s+công\s+câu\s+cá|tấn\s+công\s+câu\s+cá)(?!\w)", re.IGNORECASE),
        "cuộc tấn công câu cá",
        "tấn công giả mạo / lừa đảo trực tuyến (phishing)",
    ),
    (
        re.compile(r"(?<!\w)(?:phần\s+mềm\s+đòi\s+tiền\s+chuộc|mã\s+độc\s+chuộc\s+lỗi|phần\s+mềm\s+chuộc\s+lỗi)(?!\w)", re.IGNORECASE),
        "phần mềm đòi tiền chuộc / mã độc chuộc lỗi",
        "mã độc tống tiền (ransomware)",
    ),
    (
        re.compile(r"(?<!\w)kỹ\s+thuật\s+xã\s+hội(?!\w)", re.IGNORECASE),
        "kỹ thuật xã hội",
        "tấn công phi kỹ thuật / thao túng tâm lý (social engineering)",
    ),
    (
        re.compile(r"(?<!\w)bề\s+mặt\s+cuộc\s+tấn\s+công(?!\w)", re.IGNORECASE),
        "bề mặt cuộc tấn công",
        "bề mặt tấn công (attack surface)",
    ),
    (
        re.compile(r"(?<!\w)tường\s+lửa\s+thế\s+hệ\s+tiếp\s+theo(?!\w)", re.IGNORECASE),
        "tường lửa thế hệ tiếp theo",
        "tường lửa thế hệ mới (NGFW)",
    ),
    (
        re.compile(r"(?<!\w)(?:kiểm\s+toán\s+cây\s+bút|kiểm\s+toán\s+bút)(?!\w)", re.IGNORECASE),
        "kiểm toán cây bút",
        "kiểm thử xâm nhập (pentest)",
    ),
)

# SEC004: Insecure credential solicitation
CREDENTIAL_SOLICITATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:vui\s+lòng\s+|hãy\s+)?(?:gửi\s+(?:lại\s+)?|cung\s+cấp\s+|nhập\s+|chia\s+sẻ\s+)(?:lại\s+)?(?:mật\s+khẩu|mã\s+otp|mã\s+pin|số\s+cvv|mật\s+khẩu\s+gốc)(?:\s+[^\n.,;]*?)?(?:qua\s+email|qua\s+tin\s+nhắn|cho\s+nhân\s+viên|vào\s+biểu\s+mẫu|để\s+xác\s+minh|để\s+mở\s+khóa)|"
    r"(?:gửi\s+lại\s+mật\s+khẩu|cung\s+cấp\s+mã\s+pin|nhập\s+mật\s+khẩu\s+gốc)|"
    r"(?:mã\s+pin\s+và\s+số\s+cvv|mật\s+khẩu\s+hiện\s+tại\s+và\s+mã\s+otp)\s+(?:cho\s+nhân\s+viên|qua\s+email|qua\s+tin\s+nhắn)"
    r")(?!\w)",
    re.IGNORECASE,
)
CREDENTIAL_NEGATION_RE = re.compile(
    r"(?:không\s+bao\s+giờ\s+(?:yêu\s+cầu\s+)?|tuyệt\s+đối\s+không\s+|không\s+(?:được\s+)?yêu\s+cầu\s+|cảnh\s+báo\s+không\s+)(?:\S+\s+){0,4}$",
    re.IGNORECASE,
)

# SEC006: Misclassifying sensitive personal data as basic personal data
SENSITIVE_AS_BASIC_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:dữ\s+liệu\s+sức\s+khỏe|sinh\s+trắc\s+học|tài\s+khoản\s+ngân\s+hàng|số\s+dư\s+tài\s+khoản|vị\s+trí\s+địa\s+lý|dữ\s+liệu\s+vị\s+trí)[^\n.,;]*?(?:là|thuộc\s+nhóm|thuộc\s+loại|được\s+phân\s+loại\s+là)\s+dữ\s+liệu\s+cá\s+nhân\s+cơ\s+bản|"
    r"dữ\s+liệu\s+cá\s+nhân\s+cơ\s+bản\s+bao\s+gồm\s+[^\n.,;]*?(?:sức\s+khỏe|sinh\s+trắc\s+học|ngân\s+hàng|vị\s+trí)"
    r")(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # SEC001: Personal data breach notification deadline exceeding 72h / 3 days
    for match in BREACH_DEADLINE_DAYS_RE.finditer(masked):
        days_str = next((g for g in match.groups() if g is not None), None)
        if days_str:
            try:
                days_val = int(days_str)
            except ValueError:
                continue
            if days_val > 3:
                yield (
                    "SEC001",
                    ERROR,
                    match.start() + 1,
                    match.group(0),
                    f"breach notification deadline ({days_val} days) exceeds the 72-hour statutory deadline under Article 23 Decree 13/2023/NĐ-CP",
                    "Article 23 of Decree 13/2023/NĐ-CP mandates notifying the Department of Cybersecurity and High-Tech Crime Prevention (Cục A05, Bộ Công an) within 72 hours of detecting a personal data breach",
                )

    for match in BREACH_DEADLINE_HOURS_RE.finditer(masked):
        hrs_str = next((g for g in match.groups() if g is not None), None)
        if hrs_str:
            try:
                hrs_val = int(hrs_str)
            except ValueError:
                continue
            if hrs_val > 72:
                yield (
                    "SEC001",
                    ERROR,
                    match.start() + 1,
                    match.group(0),
                    f"breach notification deadline ({hrs_val} hours) exceeds the 72-hour statutory deadline under Article 23 Decree 13/2023/NĐ-CP",
                    "Article 23 of Decree 13/2023/NĐ-CP mandates notifying the Department of Cybersecurity and High-Tech Crime Prevention (Cục A05, Bộ Công an) within 72 hours of detecting a personal data breach",
                )

    # SEC002: Fabricated system security levels above 5
    for match in FABRICATED_LEVEL_RE.finditer(masked):
        yield (
            "SEC002",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"fabricated information system security level “{match.group(0)}”",
            "Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT classify information system security strictly from Level 1 to Level 5 ('Cấp độ 1' to 'Cấp độ 5'); Levels 6+ do not exist in Vietnamese law",
        )

    # SEC003: Awkward machine-translated InfoSec terminology
    for regex, term, hint in INFOSEC_CALQUES:
        for match in regex.finditer(masked):
            yield (
                "SEC003",
                WARN,
                match.start() + 1,
                match.group(0),
                f"machine-translated cybersecurity calque “{match.group(0)}”",
                f"use standard Vietnamese InfoSec terminology: “{hint}”",
            )

    # SEC004: Insecure credential solicitation
    for match in CREDENTIAL_SOLICITATION_RE.finditer(masked):
        prefix = masked[max(0, match.start() - 40):match.start()]
        if CREDENTIAL_NEGATION_RE.search(prefix):
            continue
        yield (
            "SEC004",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"insecure credential solicitation “{match.group(0)}”",
            "security advisories and operational communications must never ask users or staff to provide passwords, OTPs, PINs, or CVVs; emphasize that security staff never request credentials",
        )

    # SEC006: Misclassifying sensitive personal data as basic personal data
    for match in SENSITIVE_AS_BASIC_RE.finditer(masked):
        yield (
            "SEC006",
            WARN,
            match.start() + 1,
            match.group(0),
            f"misclassifying sensitive personal data as basic personal data: “{match.group(0)}”",
            "Article 2 Clause 4 of Decree 13/2023/NĐ-CP classifies health records, banking/financial data, biometrics, and location data as 'dữ liệu cá nhân nhạy cảm' requiring enhanced security safeguards",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # SEC001: Personal data breach notification missing A05 or 72-hour requirement
    if doctype == "breach-notification":
        has_a05 = bool(re.search(
            r"(?<!\w)(?:Cục\s+A05|A05|Cục\s+An\s+ninh\s+mạng\s+và\s+phòng,\s*chống\s+tội\s+phạm\s+sử\s+dụng\s+công\s+nghệ\s+cao|Bộ\s+Công\s+an)(?!\w)",
            body,
            re.IGNORECASE,
        ))
        has_72h = bool(re.search(r"(?<!\w)(?:72\s+giờ|72h|03\s+ngày|3\s+ngày)(?!\w)", body, re.IGNORECASE))

        if not (has_a05 and has_72h):
            missing_items = []
            if not has_a05:
                missing_items.append("thông báo gửi Cục A05 Bộ Công an")
            if not has_72h:
                missing_items.append("thời hạn thông báo trong vòng 72 giờ")
            yield (
                "SEC001",
                ERROR,
                first_line,
                1,
                "",
                f"breach-notification missing mandatory statutory requirements under Article 23 Decree 13/2023/NĐ-CP: {'; '.join(missing_items)}",
                "Article 23 Decree 13/2023/NĐ-CP mandates notifying Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) - Bộ Công an trong thời hạn 72 giờ kể từ khi phát hiện vi phạm",
            )

    # SEC005: Security advisory missing CVSS / severity rating or remediation guidance
    if doctype == "security-advisory":
        has_severity = bool(re.search(
            r"(?<!\w)(?:mức\s+độ\s+nghiêm\s+trọng|độ\s+nghiêm\s+trọng|điểm\s+cvss|cvss)(?!\w)",
            body,
            re.IGNORECASE,
        ))
        has_remediation = bool(re.search(
            r"(?<!\w)(?:biện\s+pháp\s+khắc\s+phục|khuyến\s+nghị\s+cập\s+nhật\s+bản\s+vá|biện\s+pháp\s+giảm\s+thiểu|hướng\s+dẫn\s+xử\s+lý|bản\s+vá|cập\s+nhật\s+bản\s+vá)(?!\w)",
            body,
            re.IGNORECASE,
        ))

        if not (has_severity and has_remediation):
            missing_items = []
            if not has_severity:
                missing_items.append("Mức độ nghiêm trọng / Điểm CVSS")
            if not has_remediation:
                missing_items.append("Biện pháp khắc phục / Khuyến nghị cập nhật bản vá")
            yield (
                "SEC005",
                ERROR,
                first_line,
                1,
                "",
                f"security-advisory missing mandatory security disclosure sections: {'; '.join(missing_items)}",
                "vulnerability advisories must explicitly include CVSS/severity ratings ('Mức độ nghiêm trọng') and actionable patching/mitigation instructions ('Biện pháp khắc phục')",
            )
