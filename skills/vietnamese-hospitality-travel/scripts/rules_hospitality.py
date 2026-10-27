# -*- coding: utf-8 -*-
"""Rules for Vietnamese hospitality and travel copy that a calque table cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and regulatory compliance across Vietnamese hospitality,
resort accommodation (Luật Du lịch 2017 Điều 50), civil aviation notices and passenger
rights during flight delays or cancellations (Thông tư 14/2015/TT-BGTVT & Thông tư 19/2023/TT-BGTVT),
pricing transparency and Net vs ++ disclosures (Luật Giá & Nghị định 109/2013/NĐ-CP),
Fine Dining / F&B culinary disclosures (tax, service charge, and allergen notifications),
and guest-courtesy standards.
"""
from __future__ import annotations

import pathlib
import re

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

RULE_DOCS = {
    "HOS001": "unexplained '++' pricing shorthand ('1.500.000++', 'giá 500.000 ₫++', 'chưa gồm ++') without explicitly stating service charge (phí phục vụ) and VAT (thuế GTGT)",
    "HOS002": "unrecognized/illegal star rating claim ('khách sạn 6 sao', 'resort 7 sao', 'tiêu chuẩn 6 sao') — under Article 50 of Luật Du lịch 2017, accommodation ratings in Vietnam span 1 to 5 stars only",
    "HOS003": "when doctype == 'hotel-booking', missing check-in/check-out schedule ('nhận phòng' / 'trả phòng') or missing cancellation/surcharge policy ('hoàn hủy' / 'phụ thu')",
    "HOS004": "when doctype == 'flight-notice', announcing flight disruption (delay/cancellation) without courteous apology ('xin lỗi' / 'mong Quý khách thông cảm' / 'lấy làm tiếc') or passenger support rights under TT 14/2015 & TT 19/2023/TT-BGTVT",
    "HOS005": "when doctype == 'fnb-menu', missing allergen disclosure ('dị ứng') or tax/service charge status ('thuế GTGT' / 'phí phục vụ')",
    "HOS006": "hostile or bureaucratic imperative phrasing toward guests ('Cấm mang đồ ăn', 'Khách tự chịu trách nhiệm nếu mất đồ', 'Phạt ngay 100%')",
}

DOCTYPES = {
    "hotel-booking": "Xác nhận đặt phòng khách sạn / Resort / Chính sách nhận - trả phòng",
    "flight-notice": "Thông báo chuyến bay / Thay đổi giờ khởi hành / Chính sách hành lý & hoàn đổi vé",
    "fnb-menu": "Thực đơn nhà hàng Fine Dining / F&B / Tiệc cưới & Hội nghị",
    "tour-itinerary": "Lịch trình tour du lịch lữ hành nội địa & quốc tế",
}

PLUS_PLUS_RE = re.compile(
    r"(?<![A-Za-z])(?:\d{1,3}(?:\.\d{3})*|\d+)\s*(?:₫|VND|đ|USD)?\s*\+\+|chưa\s+(?:bao\s+)?gồm\s*\+\+|giá\s+(?:từ\s+)?\S+\s*\+\+|\+\+(?![A-Za-z+])",
    re.IGNORECASE,
)

ILLEGAL_STAR_RE = re.compile(
    r"(?<!\w)(?:(?:khách\s+sạn|resort|khu\s+nghỉ\s+dưỡng|tiêu\s+chuẩn|đẳng\s+cấp|chất\s+lượng|dịch\s+vụ)\s+)?(?:[6-9]|\d{2,})\s*sao(?!\w)",
    re.IGNORECASE,
)

HOSTILE_GUEST_RE = re.compile(
    r"(?<!\w)(?:cấm\s+mang\s+(?:đồ\s+ăn|thức\s+ăn|nước\s+uống|thực\s+phẩm)|"
    r"cấm\s+hút\s+thuốc\s+phạt|"
    r"khách\s+tự\s+chịu\s+trách\s+nhiệm(?:\s+nếu\s+(?:mất|thất\s+lạc))?|"
    r"không\s+chịu\s+trách\s+nhiệm\s+về\s+mọi\s+mất\s+mát|"
    r"phạt\s+(?:ngay\s+)?(?:tiền|\d+%\s*|nặng)|"
    r"tuyệt\s+đối\s+cấm|"
    r"bắt\s+buộc\s+phải\s+bồi\s+thường|"
    r"tự\s+bảo\s+quản\s+mất\s+ráng\s+chịu)(?!\w)",
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
    """Line-by-line checks for illegal star ratings and hostile imperative tone."""
    # HOS002: Unrecognized / illegal star ratings (6-star, 7-star)
    for m in ILLEGAL_STAR_RE.finditer(masked_line):
        yield (
            "HOS002",
            ERROR,
            m.start() + 1,
            m.group(0),
            f"unrecognized/illegal star rating claim “{m.group(0)}”",
            "Luật Du lịch 2017 Điều 50 quy định cơ sở lưu trú du lịch tại Việt Nam chỉ xếp hạng từ 1 đến 5 sao do Cục Du lịch Quốc gia Việt Nam hoặc Sở Du lịch công nhận; không tồn tại hạng sao 6 sao hoặc 7 sao.",
        )

    # HOS006: Hostile or bureaucratic imperative phrasing toward guests
    for m in HOSTILE_GUEST_RE.finditer(masked_line):
        yield (
            "HOS006",
            WARN,
            m.start() + 1,
            m.group(0),
            f"hostile or bureaucratic imperative phrasing toward guests “{m.group(0)}”",
            "Chuyển sang văn phong hiếu khách lịch thiệp: dùng 'Quý khách vui lòng...', 'Để đảm bảo an toàn vệ sinh thực phẩm, khu nghỉ dưỡng xin phép không phục vụ thức ăn mang từ ngoài vào...', 'Để bảo vệ an toàn tài sản, Quý khách vui lòng gửi tư trang tại két sắt phòng ngủ...'.",
        )


def check_document(ctx):
    """Document-level checks for pricing transparency, booking terms, flight notices, and menus."""
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    first = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # HOS001: Unexplained '++' pricing shorthand
    match_pp = PLUS_PLUS_RE.search(body)
    if match_pp:
        has_svc = bool(re.search(r"(?:phí\s+phục\s+vụ|phí\s+dịch\s+vụ|service\s+charge)", body, re.IGNORECASE))
        has_vat = bool(re.search(r"(?:thuế\s+GTGT|giá\s+trị\s+gia\s+tăng|thuế\s+vat|\bvat\b)", body, re.IGNORECASE))
        if not (has_svc and has_vat):
            lineno = body[:match_pp.start()].count("\n") + 1
            col = match_pp.start() - body.rfind("\n", 0, match_pp.start())
            yield (
                "HOS001",
                ERROR,
                lineno,
                col,
                match_pp.group(0),
                f"unexplained '++' pricing shorthand “{match_pp.group(0)}” without disclosing service charge and VAT",
                "Nghị định 109/2013/NĐ-CP & Luật Giá quy định niêm yết giá minh bạch; ghi rõ giá Net hoặc ghi chú chi tiết 'chưa bao gồm 5% phí phục vụ và 8% (hoặc 10%) thuế GTGT'.",
            )

    # HOS003: Hotel booking confirmation missing check-in/out or cancellation/surcharge policy
    if doctype == "hotel-booking" and body.strip():
        has_checkin = bool(re.search(r"(?:nhận\s+phòng|check-?in)", body, re.IGNORECASE))
        has_checkout = bool(re.search(r"(?:trả\s+phòng|check-?out)", body, re.IGNORECASE))
        has_policy = bool(re.search(r"(?:hoàn\s+hủy|hủy\s+phòng|chính\s+sách\s+hủy|phụ\s+thu|phí\s+hủy)", body, re.IGNORECASE))

        missing = []
        if not (has_checkin and has_checkout):
            missing.append("giờ nhận phòng/trả phòng")
        if not has_policy:
            missing.append("chính sách hoàn hủy/phụ thu")

        if missing:
            yield (
                "HOS003",
                ERROR,
                first,
                1,
                "",
                f"hotel booking confirmation missing mandatory disclosures: {'; '.join(missing)}",
                "Xác nhận đặt phòng khách sạn/resort yêu cầu minh bạch thời gian nhận phòng (Check-in), trả phòng (Check-out) và chính sách hoàn hủy hoặc phụ thu theo quy chuẩn lưu trú du lịch.",
            )

    # HOS004: Flight disruption notice missing apology or passenger support rights
    if doctype == "flight-notice" and body.strip():
        flight_disruption = bool(re.search(
            r"(?:chậm\s+chuyến|hoãn\s+chuyến|hủy\s+chuyến|thay\s+đổi\s+(?:giờ|lịch)\s+bay|khởi\s+hành\s+muộn|trì\s+hoãn)",
            body,
            re.IGNORECASE,
        ))
        if flight_disruption:
            has_apology = bool(re.search(
                r"(?:xin\s+lỗi|mong\s+Quý\s+khách\s+thông\s+cảm|lấy\s+làm\s+tiếc|chân\s+thành\s+cáo\s+lỗi)",
                body,
                re.IGNORECASE,
            ))
            has_rights = bool(re.search(
                r"(?:đổi\s+chuyến|chuyển\s+chuyến|hoàn\s+vé|bồi\s+thường|phục\s+vụ\s+ăn\s+uống|hỗ\s+trợ|quyền\s+lợi|chăm\s+sóc)",
                body,
                re.IGNORECASE,
            ))

            missing = []
            if not has_apology:
                missing.append("lời xin lỗi / cáo lỗi chân thành")
            if not has_rights:
                missing.append("quyền lợi hành khách (đổi chuyến, hoàn vé, bồi thường theo quy định)")

            if missing:
                yield (
                    "HOS004",
                    ERROR,
                    first,
                    1,
                    "",
                    f"flight disruption notice missing: {'; '.join(missing)}",
                    "Thông tư 14/2015/TT-BGTVT và Thông tư 19/2023/TT-BGTVT quy định hãng hàng không phải xin lỗi chân thành và thông báo rõ quyền lợi chuyển chuyến, hoàn vé, phục vụ ăn uống hoặc bồi thường ứng trước không hoàn lại khi chậm/hủy chuyến.",
                )

    # HOS005: F&B menu missing allergen or tax/service charge disclosures
    if doctype == "fnb-menu" and body.strip():
        has_allergen = bool(re.search(r"(?:dị\s+ứng|thành\s+phần\s+gây\s+dị\s+ứng|allergen)", body, re.IGNORECASE))
        has_tax_svc = bool(re.search(r"(?:thuế\s+GTGT|giá\s+trị\s+gia\s+tăng|phí\s+phục\s+vụ|phí\s+dịch\s+vụ|VAT|đã\s+bao\s+gồm\s+thuế)", body, re.IGNORECASE))

        missing = []
        if not has_allergen:
            missing.append("lưu ý dị ứng thực phẩm")
        if not has_tax_svc:
            missing.append("thông tin thuế GTGT / phí phục vụ")

        if missing:
            yield (
                "HOS005",
                WARN,
                first,
                1,
                "",
                f"F&B menu missing culinary disclosures: {'; '.join(missing)}",
                "Thực đơn F&B / Fine Dining chuyên nghiệp cần có ghi chú lưu ý dị ứng thực phẩm và tình trạng thuế GTGT / phí phục vụ (giá Net hay ++).",
            )
