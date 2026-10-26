# -*- coding: utf-8 -*-
"""Rules for Vietnamese e-commerce, retail promotions, product labeling, and consumer protection.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only. Zero external dependencies.

Enforces:
- Decree 52/2013/NĐ-CP & Decree 85/2021/NĐ-CP on E-Commerce (MoIT blue vs. red badge accuracy).
- Decree 81/2018/NĐ-CP & Decree 128/2024/NĐ-CP on commercial promotion discount caps (50%).
- Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng số 19/2023/QH15)
  Article 25 (void unconscionable clauses, no-return prohibitions) & Article 10 (dark patterns).
- Decree 43/2017/NĐ-CP & Decree 111/2021/NĐ-CP on mandatory Vietnamese product labeling (PDP).
- E-commerce logistics translationese and calques.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "product-pdp": "Trang chi tiết sản phẩm TMĐT / PDP & Nhãn hàng hóa điện tử (Nghị định 52/2013, 85/2021, 43/2017 & 111/2021/NĐ-CP)",
    "flash-sale-promo": "Chương trình Khuyến mại / Flash Sale / Voucher (Nghị định 81/2018 & 128/2024/NĐ-CP)",
    "return-policy": "Chính sách đổi trả, bảo hành & vận chuyển COD (Luật Bảo vệ quyền lợi người tiêu dùng 2023)",
}

RULE_DOCS = {
    "ECOM001": "conflating 'Đã thông báo Bộ Công Thương' with 'Đã đăng ký Bộ Công Thương' or falsely claiming Ministry of Industry and Trade notification guarantees product quality or authenticity (Nghị định 52/2013/NĐ-CP & 85/2021/NĐ-CP)",
    "ECOM002": "promotional discount exceeding 50% statutory cap under Decree 81/2018/NĐ-CP & 128/2024/NĐ-CP without citing state concentrated promotion program, or fake anchor pricing",
    "ECOM003": "unlawful blanket no-return policy ('hàng mua rồi miễn đổi trả trong mọi trường hợp') violating Article 25 Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng 2023)",
    "ECOM004": "e-commerce product listing (PDP) missing mandatory Vietnamese product labeling disclosures ('Xuất xứ' and responsible business entity) under Decree 43/2017/NĐ-CP & Decree 111/2021/NĐ-CP",
    "ECOM005": "awkward machine-translated e-commerce & logistics calques ('Ra ngoài để giao hàng', 'Sự hoàn thành đơn hàng', 'Thêm vào xe đẩy', 'Tiền mặt trên giao hàng', 'Chính sách trở lại', 'Người vận chuyển cuối cùng')",
    "ECOM006": "manipulative dark-pattern urgency, courier salary deduction coercion, or unauthorized recurring enrollment prohibited under Law on Protection of Consumers' Rights 2023",
}

# ECOM001: Badge conflation & fake MoIT quality endorsements
BADGE_CONFLATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"sàn\s+(?:giao\s+dịch\s+)?(?:thương\s+mại\s+điện\s+tử|TMĐT)[^\n.,;:]*?(?:chỉ\s+cần\s+(?:gắn\s+logo|thông\s+báo)?\s*(?:logo\s+)?Đã\s+thông\s+báo\s+Bộ\s+Công\s+Thương)|"
    r"sàn\s+(?:thương\s+mại\s+điện\s+tử|TMĐT)[^\n.,;:]*?gắn\s+logo\s+Đã\s+thông\s+báo\s+Bộ\s+Công\s+Thương"
    r")(?!\w)",
    re.IGNORECASE,
)

MOIT_QUALITY_CLAIM_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:được\s+)?Bộ\s+Công\s+Thương\s+bảo\s+chứng\s+chất\s+lượng(?:\s+100%)?|"
    r"logo\s+Bộ\s+Công\s+Thương\s+chứng\s+nhận(?:\s+hàng\s+chính\s+hãng(?:\s+tuyệt\s+đối)?)?|"
    r"Bộ\s+Công\s+Thương\s+chứng\s+nhận\s+hàng\s+chính\s+hãng|"
    r"chứng\s+nhận\s+hàng\s+chính\s+hãng\s+bởi\s+Bộ\s+Công\s+Thương|"
    r"Bộ\s+Công\s+Thương\s+cam\s+kết\s+chất\s+lượng"
    r")(?!\w)",
    re.IGNORECASE,
)

# ECOM002: Discount exceeding 50%
DISCOUNT_RATE_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:giảm\s+giá|sale|khuyến\s+mại|ưu\s+đãi|chiết\s+khấu)[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%|"
    r"(\d+(?:[.,]\d+)?)\s*%\s*[^\n.,;:]*?(?:giảm\s+giá|sale|khuyến\s+mại|ưu\s+đãi)|"
    r"sale\s+sập\s+sàn\s+(\d+(?:[.,]\d+)?)\s*%"
    r")(?!\w)",
    re.IGNORECASE,
)

CONCENTRATED_PROMO_RE = re.compile(
    r"(?<!\w)(?:khuyến\s+mại\s+tập\s+trung|tháng\s+khuyến\s+mại|hàng\s+thanh\s+lý|thanh\s+lý\s+hàng\s+tồn)(?!\w)",
    re.IGNORECASE,
)

FAKE_ANCHOR_PRICE_RE = re.compile(
    r"(?<!\w)(?:"
    r"nâng\s+khống\s+giá\s+gốc(?:\s+để\s+giảm\s+giá\s+ảo)?|"
    r"tăng\s+giá\s+gốc\s+(?:để|rồi)\s+giảm\s+giá\s+ảo"
    r")(?!\w)",
    re.IGNORECASE,
)

# ECOM003: Unlawful no-return policies
NO_RETURN_POLICY_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:hàng\s+mua\s+rồi\s+)?miễn\s+đổi\s+trả(?:\s+trong\s+mọi\s+trường\s+hợp)?|"
    r"không\s+(?:áp\s+dụng|chấp\s+nhận)\s+đổi\s+trả(?:\s+với\s+bất\s+kỳ\s+lý\s+do\s+gì|\s+trong\s+mọi\s+trường\s+hợp)?(?:\s+kể\s+cả\s+lỗi\s+nhà\s+sản\s+xuất)?|"
    r"từ\s+chối\s+đổi\s+trả(?:\s+với\s+bất\s+kỳ\s+lý\s+do\s+gì|\s+kể\s+cả\s+hàng\s+lỗi)?|"
    r"cấm\s+đồng\s+kiểm\s+và\s+từ\s+chối\s+hoàn\s+tiền\s+dưới\s+mọi\s+hình\s+thức|"
    r"từ\s+chối\s+hoàn\s+tiền\s+dưới\s+mọi\s+hình\s+thức"
    r")(?!\w)",
    re.IGNORECASE,
)

# ECOM005: E-commerce logistics calques
LOGISTICS_CALQUES_MAP = {
    "ra ngoài để giao hàng": "đang giao hàng",
    "sự hoàn thành đơn hàng": "hoàn tất đơn hàng / xử lý đơn hàng",
    "thêm vào xe đẩy": "thêm vào giỏ hàng",
    "bỏ vào giỏ xe": "thêm vào giỏ hàng",
    "tiền mặt trên giao hàng": "thanh toán khi nhận hàng (COD)",
    "chính sách trở lại": "chính sách đổi trả",
    "người vận chuyển cuối cùng": "đơn vị vận chuyển chặng cuối",
}

LOGISTICS_CALQUES_RE = re.compile(
    r"(?<!\w)(" + "|".join(re.escape(k) for k in LOGISTICS_CALQUES_MAP) + r")(?!\w)",
    re.IGNORECASE,
)

# ECOM006: Dark pattern urgency & manipulation
DARK_PATTERN_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:nhân\s+viên|shipper|người\s+giao\s+hàng)\s+(?:sẽ\s+)?bị\s+trừ\s+lương\s+nếu\s+(?:quý\s+khách|khách\s+hàng|bạn)?\s*hủy\s+đơn|"
    r"bị\s+trừ\s+lương\s+nếu\s+hủy\s+đơn|"
    r"(?:hệ\s+thống\s+tự\s+động\s+)?khóa\s+tài\s+khoản\s+vĩnh\s+viễn\s+nếu\s+không\s+thanh\s+toán(?:\s+trong\s+\d+\s+phút|\s+ngay)?|"
    r"tự\s+động\s+(?:đăng\s+ký|gia\s+hạn)\s+(?:gói\s+)?(?:hội\s+viên|dịch\s+vụ)\s+trả\s+phí\s+gia\s+hạn\s+ngầm\s+không\s+cần\s+đồng\s+ý|"
    r"tự\s+động\s+đăng\s+ký\s+gói\s+hội\s+viên\s+trả\s+phí[^\n.,;:]*?không\s+cần\s+đồng\s+ý"
    r")(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # ECOM001: Badge conflation
    for match in BADGE_CONFLATION_RE.finditer(masked):
        yield (
            "ECOM001",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"conflating e-commerce platform registration with sales notification badge “{match.group(0)}”",
            "e-commerce marketplaces/service platforms must register with MoIT and use the red 'Đã đăng ký Bộ Công Thương' badge under Decree 52/2013/NĐ-CP & Decree 85/2021/NĐ-CP",
        )

    # ECOM001: Misrepresenting MoIT badge as product quality certification
    for match in MOIT_QUALITY_CLAIM_RE.finditer(masked):
        yield (
            "ECOM001",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"falsely claiming Ministry of Industry and Trade certification guarantees quality “{match.group(0)}”",
            "MoIT notification/registration is an administrative operation filing; it does not certify product quality or authenticity under Decree 52/2013/NĐ-CP & Decree 85/2021/NĐ-CP",
        )

    # ECOM002: Promotional discount exceeding 50%
    for match in DISCOUNT_RATE_RE.finditer(masked):
        captured_rate = next((g for g in match.groups() if g is not None), None)
        if captured_rate:
            try:
                rate_val = float(captured_rate.replace(",", "."))
            except ValueError:
                continue
            if rate_val > 50.0:
                is_concentrated = bool(
                    CONCENTRATED_PROMO_RE.search(masked) or CONCENTRATED_PROMO_RE.search(ctx.text)
                )
                if not is_concentrated:
                    yield (
                        "ECOM002",
                        ERROR,
                        match.start() + 1,
                        match.group(0),
                        f"promotional discount rate ({captured_rate}%) exceeds 50% statutory ceiling without state concentrated promotion authorization",
                        "under Decree 81/2018/NĐ-CP & Decree 128/2024/NĐ-CP, commercial discount rates cannot exceed 50% unless part of an authorized state concentrated promotion program",
                    )

    # ECOM002: Fake anchor pricing
    for match in FAKE_ANCHOR_PRICE_RE.finditer(masked):
        yield (
            "ECOM002",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"fake anchor pricing / deceptive price inflation “{match.group(0)}”",
            "inflating pre-discount prices to display artificial discount percentages is deceptive pricing prohibited under Decree 81/2018/NĐ-CP and Consumer Protection Law 2023",
        )

    # ECOM003: Unlawful blanket no-return policies
    for match in NO_RETURN_POLICY_RE.finditer(masked):
        yield (
            "ECOM003",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"unlawful blanket no-return clause “{match.group(0)}”",
            "blanket return exclusions and denying inspection/refunds for defective goods violate Article 25 Law on Protection of Consumers' Rights 2023 and are null and void (vô hiệu)",
        )

    # ECOM005: E-commerce logistics calques
    for match in LOGISTICS_CALQUES_RE.finditer(masked):
        term_lower = match.group(1).lower()
        replacement = LOGISTICS_CALQUES_MAP.get(term_lower, "thuật ngữ chuẩn")
        yield (
            "ECOM005",
            WARN,
            match.start() + 1,
            match.group(1),
            f"awkward machine-translated e-commerce / logistics calque “{match.group(1)}”",
            f"replace with conventional Vietnamese e-commerce phrasing: '{replacement}'",
        )

    # ECOM006: Dark pattern urgency, coercion, sneaky billing
    for match in DARK_PATTERN_RE.finditer(masked):
        yield (
            "ECOM006",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"manipulative dark pattern / coercive urgency claim “{match.group(0)}”",
            "threatening staff penalties, immediate account termination, or enrolling in hidden paid subscriptions without affirmative consent violates Consumer Protection Law 2023",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # ECOM004: Missing mandatory Vietnamese product labeling in PDP
    if doctype == "product-pdp":
        has_origin = bool(re.search(r"xuất\s+xứ|nơi\s+sản\s+xuất|sản\s+xuất\s+tại|nguồn\s+gốc", body, re.IGNORECASE))
        has_responsible = bool(
            re.search(
                r"thương\s+nhân\s+chịu\s+trách\s+nhiệm|nhà\s+sản\s+xuất|đơn\s+vị\s+nhập\s+khẩu|nhà\s+phân\s+phối|nhập\s+khẩu\s+bởi",
                body,
                re.IGNORECASE,
            )
        )
        if not (has_origin and has_responsible):
            missing_items = []
            if not has_origin:
                missing_items.append("thông tin xuất xứ hàng hóa ('Xuất xứ' / 'Sản xuất tại')")
            if not has_responsible:
                missing_items.append("thương nhân chịu trách nhiệm ('Nhà sản xuất' / 'Đơn vị nhập khẩu')")
            yield (
                "ECOM004",
                WARN,
                first_line,
                1,
                "",
                f"product-pdp missing mandatory Vietnamese product labeling disclosures: {'; '.join(missing_items)}",
                "Decree 43/2017/NĐ-CP & Decree 111/2021/NĐ-CP mandate explicit display of product name, origin, and responsible entity on e-commerce product detail pages",
            )
