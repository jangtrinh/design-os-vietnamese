# -*- coding: utf-8 -*-
"""Rules for Vietnamese HR, recruitment, and labor compliance copy.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory compliance with Bộ luật Lao động 2019:
- Anti-discrimination in recruitment (Điều 8 khoản 1: giới tính, hôn nhân, thai sản, ngoại hình, tuổi tác)
- Probation duration and salary floor (Điều 25 tối đa 60 ngày, Điều 26 lương thử việc >= 85%)
- Transparency of Gross vs Net compensation in Offer Letters
- Strict prohibition of withholding original personal documents or unlawful salary deduction/fines (Điều 17 & Điều 128)
- Elimination of exploitative, toxic JD clichés
- Professional behavior-based SBI performance appraisal vs subjective personal attacks
"""
from __future__ import annotations

import pathlib
import re

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

RULE_DOCS = {
    "HR001": "discriminatory hiring criteria in recruitment copy based on gender, marital status, pregnancy, appearance, or arbitrary age caps (Bộ luật Lao động 2019 Điều 8 khoản 1)",
    "HR002": "probation salary below 85% statutory floor or duration exceeding 60-day cap for skilled roles (Bộ luật Lao động 2019 Điều 25 & 26)",
    "HR003": "when doctype == 'offer-letter', stating salary figure without specifying Gross (trước thuế & bảo hiểm) or Net (thực lĩnh)",
    "HR004": "illegal original document retention or wage deduction / punitive fine threats (Bộ luật Lao động 2019 Điều 17 & Điều 128)",
    "HR005": "vague or toxic JD clichés ('lương hấp dẫn theo năng lực', 'chịu được áp lực cực cao không giới hạn giờ giấc', 'coi công ty là nhà 24/7')",
    "HR006": "when doctype == 'performance-review', subjective personal attacks ('thái độ kém cỏi', 'lười biếng', 'thiếu năng lực bẩm sinh') instead of behavior- and metric-based SBI feedback",
}

DOCTYPES = {
    "job-description": "Tin tuyển dụng / Mô tả công việc (JD)",
    "offer-letter": "Thư mời nhận việc (Offer Letter — Bộ luật Lao động 2019)",
    "performance-review": "Đánh giá hiệu suất nhân sự định kỳ (OKR / KPI / 360 Feedback)",
    "internal-policy": "Nội quy lao động / Thông báo nhân sự nội bộ",
}

DISCRIMINATION_RE = re.compile(
    r"(?<!\w)(?:chỉ\s+tuyển\s+(?:nam|nữ)|"
    r"yêu\s+cầu\s+giới\s+tính\s+(?:nam|nữ)|"
    r"ưu\s+tiên\s+(?:nam|nữ)\s+(?:độc\s+thân)?|"
    r"chưa\s+kết\s+hôn|"
    r"yêu\s+cầu\s+chưa\s+kết\s+hôn|"
    r"không\s+vướng\s+bận\s+gia\s+đình|"
    r"cam\s+kết\s+không\s+(?:kết\s+hôn|mang\s+thai|sinh\s+con)(?:\s+trong\s+\d+\s+năm)?|"
    r"ngoại\s+hình\s+(?:ưa\s+nhìn|sáng|chuẩn)|"
    r"tuổi\s+(?:từ\s+\d+\s+đến\s+(?:2\d|3\d|4\d)|dưới\s+(?:2\d|3\d|4\d)|không\s+quá\s+(?:2\d|3\d|4\d)))(?!\w)",
    re.IGNORECASE,
)

PROBATION_SUB85_RE = re.compile(
    r"(?<!\w)(?:lương\s+thử\s+việc\s+(?:bằng\s+)?(?:[1-7]\d|8[0-4])\s*%|"
    r"hưởng\s+(?:[1-7]\d|8[0-4])\s*%\s*(?:mức\s+)?(?:lương|thu\s+nhập)(?:\s+chính\s+thức)?(?:\s+trong\s+thời\s+gian\s+thử\s+việc)?|"
    r"(?:nhận|trả)\s+(?:[1-7]\d|8[0-4])\s*%\s*lương\s+thử\s+việc)(?!\w)",
    re.IGNORECASE,
)

PROBATION_EXCESS_DURATION_RE = re.compile(
    r"(?<!\w)thử\s+việc\s+(?:trong\s+)?(?:([3-9]|\d{2,})\s+tháng|([7-9]\d|\d{3,})\s+ngày)(?!\w)",
    re.IGNORECASE,
)

ILLEGAL_RETENTION_DEDUCTION_RE = re.compile(
    r"(?<!\w)(?:giữ\s+(?:bản\s+chính|bản\s+gốc)\s+(?:bằng\s+đại\s+học|bằng\s+tốt\s+nghiệp|giấy\s+tờ|CCCD|căn\s+cước|CMND|hộ\s+chiếu)|"
    r"giữ\s+(?:bằng\s+đại\s+học|CCCD|căn\s+cước(?:\s+công\s+dân)?|hộ\s+chiếu)\s+gốc|"
    r"thu\s+giữ\s+(?:bằng\s+đại\s+học|bằng\s+tốt\s+nghiệp|giấy\s+tờ\s+tùy\s+thân)|"
    r"phạt\s+(?:trừ\s+)?lương|"
    r"trừ\s+lương\s+phạt|"
    r"tịch\s+thu\s+(?:tiền\s+)?(?:đặt\s+)?cọc|"
    r"nộp\s+tiền\s+cọc\s+(?:để\s+được\s+)?(?:đi\s+làm|nhận\s+việc)|"
    r"khấu\s+trừ\s+lương\s+(?:trái\s+pháp\s+luật|\d+%\s*do\s+vi\s+phạm))(?!\w)",
    re.IGNORECASE,
)

TOXIC_JD_RE = re.compile(
    r"(?<!\w)(?:lương\s+hấp\s+dẫn\s+theo\s+năng\s+lực|"
    r"lương\s+thỏa\s+thuận\s+theo\s+năng\s+lực|"
    r"chịu\s+(?:được\s+)?áp\s+lực\s+công\s+việc\s+cực\s+cao|"
    r"không\s+giới\s+hạn\s+giờ\s+giấc|"
    r"coi\s+công\s+ty\s+(?:là|như)\s+nhà|"
    r"làm\s+việc\s+24/7|"
    r"sẵn\s+sàng\s+(?:OT|tăng\s+ca)\s+không\s+(?:cần\s+)?tính\s+lương|"
    r"tinh\s+thần\s+chiến\s+binh\s+bất\s+kể\s+ngày\s+đêm)(?!\w)",
    re.IGNORECASE,
)

PERSONAL_ATTACK_RE = re.compile(
    r"(?<!\w)(?:thái\s+độ\s+(?:kém\s+cỏi|tồi\s+tệ|chống\s+đối|yếu\s+kém)|"
    r"lười\s+biếng|"
    r"thiếu\s+năng\s+lực(?:\s+bẩm\s+sinh)?|"
    r"năng\s+lực\s+yếu\s+kém|"
    r"bản\s+tính\s+chậm\s+chạp|"
    r"không\s+có\s+tương\s+lai\s+phát\s+triển|"
    r"ý\s+thức\s+tồi)(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith("<!--") or stripped.startswith("#")


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


def check_line(ctx, lineno: int, raw_line: str, masked_line: str):
    """Line-by-line checks for recruitment discrimination, probation terms, document retention, and toxic clichés."""
    doctype = ctx.doctype

    # HR001: Discriminatory hiring criteria (gender, marital status, pregnancy, appearance, age caps)
    for m in DISCRIMINATION_RE.finditer(masked_line):
        yield (
            "HR001",
            ERROR,
            m.start() + 1,
            m.group(0),
            f"discriminatory hiring criteria in recruitment copy “{m.group(0)}”",
            "Bộ luật Lao động 2019 Điều 8 khoản 1 nghiêm cấm phân biệt đối xử trong lao động dựa trên giới tính, độ tuổi, tình trạng hôn nhân, thai sản hoặc ngoại hình.",
        )

    # HR002: Probation salary below 85% or excessive probation duration
    for m in PROBATION_SUB85_RE.finditer(masked_line):
        yield (
            "HR002",
            ERROR,
            m.start() + 1,
            m.group(0),
            f"probation salary below 85% statutory floor “{m.group(0)}”",
            "Bộ luật Lao động 2019 Điều 26 quy định tiền lương của người lao động trong thời gian thử việc do hai bên thỏa thuận nhưng ít nhất phải bằng 85% mức lương của công việc đó.",
        )

    for m in PROBATION_EXCESS_DURATION_RE.finditer(masked_line):
        # Exemption: người quản lý doanh nghiệp under Điều 25 khoản 1 allows up to 180 days
        is_executive = "người quản lý doanh nghiệp" in masked_line.lower() or "quản lý doanh nghiệp" in masked_line.lower()
        if not is_executive:
            yield (
                "HR002",
                ERROR,
                m.start() + 1,
                m.group(0),
                f"probation duration exceeding statutory cap “{m.group(0)}”",
                "Bộ luật Lao động 2019 Điều 25 quy định thời gian thử việc tối đa không quá 60 ngày đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn kỹ thuật từ cao đẳng trở lên (chỉ người quản lý doanh nghiệp mới được tối đa 180 ngày).",
            )

    # HR004: Illegal document retention or wage deduction / fine threats
    for m in ILLEGAL_RETENTION_DEDUCTION_RE.finditer(masked_line):
        yield (
            "HR004",
            ERROR,
            m.start() + 1,
            m.group(0),
            f"illegal document retention or wage deduction threat “{m.group(0)}”",
            "Bộ luật Lao động 2019 Điều 17 nghiêm cấm người sử dụng lao động giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động; Điều 128 nghiêm cấm dùng hình thức phạt tiền, cắt lương thay việc xử lý kỷ luật lao động.",
        )

    # HR005: Vague or toxic JD clichés
    for m in TOXIC_JD_RE.finditer(masked_line):
        yield (
            "HR005",
            WARN,
            m.start() + 1,
            m.group(0),
            f"vague or toxic JD cliché “{m.group(0)}”",
            "Tin tuyển dụng hiện đại cần nêu rõ dải thu nhập (salary range), thời gian làm việc chuẩn và kỳ vọng công việc theo kết quả đầu ra, tránh khẩu hiệu sáo rỗng hoặc bóc lột.",
        )

    # HR006: Subjective personal attack in performance review
    if doctype == "performance-review":
        for m in PERSONAL_ATTACK_RE.finditer(masked_line):
            yield (
                "HR006",
                WARN,
                m.start() + 1,
                m.group(0),
                f"subjective personal attack in performance review “{m.group(0)}”",
                "Đánh giá hiệu suất nhân sự cần tuân thủ mô hình SBI (Situation - Behavior - Impact), nhận xét dựa trên hành vi cụ thể và số liệu đo lường OKR/KPI, tránh công kích cá nhân hoặc định kiến chủ quan.",
            )


def check_document(ctx):
    """Document-level checks for Offer Letter salary transparency (Gross vs Net)."""
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    first = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # HR003: Offer letter states salary without specifying Gross or Net
    if doctype == "offer-letter" and body.strip():
        has_salary_mention = bool(re.search(
            r"(?:mức\s+)?(?:lương|thu\s+nhập|chế\s+độ\s+lương|\b\d{1,3}(?:\.\d{3})+\s*(?:₫|VND|đồng))",
            body,
            re.IGNORECASE,
        ))
        if has_salary_mention:
            has_gross_net = bool(re.search(r"(?:Gross|Net|trước\s+thuế|thực\s+lĩnh)", body, re.IGNORECASE))
            if not has_gross_net:
                yield (
                    "HR003",
                    WARN,
                    first,
                    1,
                    "",
                    "offer letter states salary figure without specifying Gross or Net",
                    "Thư mời nhận việc (Offer Letter) chuyên nghiệp và minh bạch pháp lý yêu cầu ghi rõ mức lương là Gross (trước thuế TNCN và các khoản bảo hiểm bắt buộc) hoặc Net (thực lĩnh).",
                )
