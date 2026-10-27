# -*- coding: utf-8 -*-
"""Rules for Vietnamese real estate, property development, and construction compliance.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only. Zero external dependencies.

Enforces:
- Law on Real Estate Business 2023 (Luật Kinh doanh bất động sản số 29/2023/QH15)
  Article 23 Clause 5 (deposit cap 5%) and Article 25 (payment schedule limits).
- Land Law 2024 (Luật Đất đai số 31/2024/QH15) & Housing Law 2023 (Luật Nhà ở số 27/2023/QH15)
  Article 134 Land Law 2024 (land tenure accuracy for commercial properties),
  Article 141 Housing Law 2023 (carpet vs. wall-center area),
  Article 152 Housing Law 2023 (2% mandatory maintenance fund).
- Decree 37/2015/NĐ-CP & construction BOQ translationese and calques.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "off-plan-contract": "Hợp đồng mua bán / đặt cọc nhà ở, công trình xây dựng hình thành trong tương lai (Luật Kinh doanh BĐS 2023)",
    "project-brochure": "Tài liệu giới thiệu dự án bất động sản / Condotel / Officetel / Căn hộ (Luật Đất đai 2024 & Luật Nhà ở 2023)",
    "construction-boq": "Hợp đồng thi công xây dựng / Bảng tiên lượng mời thầu BOQ & Hồ sơ nghiệm thu (Luật Xây dựng & NĐ 37/2015/NĐ-CP)",
}

RULE_DOCS = {
    "REA001": "off-plan real estate deposit exceeding 5% statutory cap under Article 23 Clause 5 of Law on Real Estate Business 2023 (Luật Kinh doanh bất động sản 2023 Điều 23 Khoản 5) or disguised capital mobilization",
    "REA002": "off-plan payment schedule violating Article 25 of Law on Real Estate Business 2023 (first installment > 30%, pre-handover > 70% or > 50% for FDI developers, or pre-certificate > 95%)",
    "REA003": "misleading land tenure claims promising permanent residential title ('sổ đỏ lâu dài', 'sổ hồng vĩnh viễn', 'sở hữu lâu dài') for commercial-service properties (condotel, officetel, shophouse thương mại dịch vụ) under Land Law 2024 (Luật Đất đai 2024)",
    "REA004": "apartment area stated without specifying carpet area ('diện tích thông thủy') vs wall-center area ('diện tích tim tường') or ambiguous 'diện tích phủ bì' under Article 141 Housing Law 2023 (Luật Nhà ở 2023)",
    "REA005": "apartment sales contract missing mandatory 2% maintenance fund ('kinh phí bảo trì'), unlawfully charging > 2%, or demanding maintenance fund before handover under Article 152 Housing Law 2023 (Luật Nhà ở 2023)",
    "REA006": "literal English calques in real estate & construction BOQ copy ('vùng xanh lá cây', 'tài sản thực', 'danh sách số lượng', 'căn hộ trên kế hoạch', 'bàn giao thô ráp', 'chứng chỉ hoàn thành thực chất')",
}

# REA001: Deposit rate exceeding 5%
DEPOSIT_RATE_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:đặt\s+cọc|tiền\s+cọc|tiền\s+đặt\s+cọc|đặt\s+cọc\s+giữ\s+chỗ|tiền\s+giữ\s+chỗ|giữ\s+chỗ\s+thiện\s+chí)[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%|"
    r"(\d+(?:[.,]\d+)?)\s*%\s*(?:giá\s+bán|giá\s+trị\s+hợp\s+đồng|tổng\s+giá\s+trị)[^\n.,;:]*?(?:đặt\s+cọc|tiền\s+cọc|tiền\s+đặt\s+cọc)|"
    r"thu\s+(\d+(?:[.,]\d+)?)\s*%\s*(?:giá\s+bán|giá\s+trị\s+hợp\s+đồng)[^\n.,;:]*?đặt\s+cọc"
    r")(?!\w)",
    re.IGNORECASE,
)

# REA001: Disguised capital mobilization
DISGUISED_MOBILIZATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:huy\s+động\s+vốn|hợp\s+đồng\s+góp\s+vốn|thỏa\s+thuận\s+giữ\s+chỗ|đặt\s+cọc\s+giữ\s+chỗ|giữ\s+chỗ\s+thiện\s+chí)[^\n.,;:]*?"
    r"(?:khi\s+chưa\s+đủ\s+điều\s+kiện|chưa\s+có\s+văn\s+bản\s+đủ\s+điều\s+kiện|chưa\s+được\s+phép\s+mở\s+bán|chưa\s+đủ\s+điều\s+kiện\s+bán|khi\s+chưa\s+xong\s+móng)"
    r")(?!\w)",
    re.IGNORECASE,
)

# REA002: Installment 1 > 30%
INSTALLMENT_PAYMENT_KW_RE = re.compile(
    r"(?<!\w)(?:thanh\s+toán|đóng|(?<!doanh\s)thu|nộp|giá\s+trị\s+hợp\s+đồng|giá\s+bán|tiền)(?!\w)",
    re.IGNORECASE,
)

INSTALLMENT_1_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:thanh\s+toán\s+đợt\s+1|thanh\s+toán\s+lần\s+đầu|(?:thanh\s+toán|đóng|(?<!doanh\s)thu|nộp)[^\n.,;:]*?(?:đợt\s+1|đợt\s+đầu)|(?:đợt\s+1|đợt\s+đầu)[^\n.,;:]*?(?:thanh\s+toán|đóng|(?<!doanh\s)thu|nộp|giá\s+trị\s+hợp\s+đồng|giá\s+bán|tiền))[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%|"
    r"(\d+(?:[.,]\d+)?)\s*%\s*(?:giá\s+trị\s+hợp\s+đồng|tổng\s+giá\s+trị|tiền)[^\n.,;:]*?(?:ở\s+đợt\s+1|trong\s+đợt\s+1|đợt\s+đầu|ngay\s+đợt\s+1)"
    r")(?!\w)",
    re.IGNORECASE,
)

# REA002: Pre-handover > 70% (or > 50% for FDI)
PRE_HANDOVER_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:trước\s+khi\s+bàn\s+giao(?!\s+(?:sổ|giấy\s+chứng\s+nhận))|trước\s+thời\s+điểm\s+bàn\s+giao(?!\s+(?:sổ|giấy\s+chứng\s+nhận))|trước\s+khi\s+nhận\s+nhà)[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%|"
    r"(\d+(?:[.,]\d+)?)\s*%\s*[^\n.,;:]*?(?:trước\s+khi\s+bàn\s+giao(?!\s+(?:sổ|giấy\s+chứng\s+nhận))|trước\s+thời\s+điểm\s+bàn\s+giao(?!\s+(?:sổ|giấy\s+chứng\s+nhận))|trước\s+khi\s+nhận\s+nhà)|"
    r"thanh\s+toán\s+(\d+(?:[.,]\d+)?)\s*%\s*giá\s+trị\s+hợp\s+đồng\s+đến\s+khi\s+bàn\s+giao"
    r")(?!\w)",
    re.IGNORECASE,
)

# REA002: Pre-certificate > 95%
PRE_CERT_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:trước\s+khi\s+(?:cấp|nhận|bàn\s+giao)\s+(?:Giấy\s+chứng\s+nhận|sổ\s+hồng|sổ\s+đỏ))[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%|"
    r"(\d+(?:[.,]\d+)?)\s*%\s*[^\n.,;:]*?(?:trước\s+khi\s+(?:cấp|nhận|bàn\s+giao)\s+(?:Giấy\s+chứng\s+nhận|sổ\s+hồng|sổ\s+đỏ))|"
    r"thu\s+100%\s+giá\s+trị\s+hợp\s+đồng\s+trước\s+khi\s+bàn\s+giao\s+sổ\s+hồng"
    r")(?!\w)",
    re.IGNORECASE,
)

# REA003: Commercial properties with misleading permanent tenure
COMMERCIAL_PROPERTY_RE = re.compile(
    r"(?<!\w)(?:condotel|officetel|căn\s+hộ\s+du\s+lịch|biệt\s+thự\s+nghỉ\s+dưỡng|biệt\s+thự\s+du\s+lịch|shophouse\s+thương\s+mại\s+dịch\s+vụ|căn\s+hộ\s+văn\s+phòng|đất\s+thương\s+mại\s+dịch\s+vụ)(?!\w)",
    re.IGNORECASE,
)
PERMANENT_TENURE_RE = re.compile(
    r"(?<!\w)(?:sổ\s+đỏ\s+lâu\s+dài|sổ\s+hồng\s+vĩnh\s+viễn|sở\s+hữu\s+lâu\s+dài\s+vĩnh\s+viễn|sở\s+hữu\s+vĩnh\s+viễn|sở\s+hữu\s+lâu\s+dài)(?!\w)",
    re.IGNORECASE,
)

# REA004: Ambiguous apartment area
AREA_AMBIGUOUS_RE = re.compile(
    r"(?<!\w)(?:diện\s+tích\s+căn\s+hộ|diện\s+tích\s+phủ\s+bì)(?!\w)",
    re.IGNORECASE,
)
AREA_CARPET_RE = re.compile(r"(?<!\w)thông\s+thủy(?!\w)", re.IGNORECASE)
AREA_WALL_CENTER_RE = re.compile(r"(?<!\w)tim\s+tường(?!\w)", re.IGNORECASE)

# REA005: Maintenance fund overcharge or premature collection
MAINTENANCE_FEE_OVERCHARGE_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:kinh\s+phí\s+bảo\s+trì|phí\s+bảo\s+trì)[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%|"
    r"(\d+(?:[.,]\d+)?)\s*%\s*(?:kinh\s+phí\s+bảo\s+trì|phí\s+bảo\s+trì)"
    r")(?!\w)",
    re.IGNORECASE,
)
MAINTENANCE_PREMATURE_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:nộp|đóng|thu|thanh\s+toán)\s+(?:2%\s+)?(?:kinh\s+phí|phí)\s+bảo\s+trì[^\n.,;:]*?(?:ngay\s+khi\s+(?:ký|đặt\s+cọc|đặt\s+chỗ)|ở\s+đợt\s+1|trong\s+đợt\s+1|đợt\s+đầu)|"
    r"(?:ngay\s+khi\s+(?:ký\s+thỏa\s+thuận\s+đặt\s+cọc|đặt\s+cọc))[^\n.,;:]*?(?:nộp|đóng|thu)\s+2%\s+(?:kinh\s+phí|phí)\s+bảo\s+trì"
    r")(?!\w)",
    re.IGNORECASE,
)

# REA006: Calques in real estate & construction BOQ
CALQUES_MAP = {
    "vùng xanh lá cây": "mảng xanh / công viên cây xanh / diện tích cây xanh",
    "tài sản thực": "bất động sản",
    "danh sách số lượng": "bảng tiên lượng mời thầu / bảng khối lượng mời thầu (BOQ)",
    "căn hộ trên kế hoạch": "nhà ở hình thành trong tương lai / bất động sản hình thành trong tương lai",
    "tài sản ngoài kế hoạch": "nhà ở hình thành trong tương lai / bất động sản hình thành trong tương lai",
    "bàn giao thô ráp": "bàn giao thô",
    "chứng chỉ hoàn thành thực chất": "biên bản nghiệm thu hoàn thành công trình đưa vào sử dụng",
}

CALQUES_RE = re.compile(
    r"(?<!\w)(" + "|".join(re.escape(k) for k in CALQUES_MAP) + r")(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


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


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # REA001: Off-plan deposit exceeding 5%
    for match in DEPOSIT_RATE_RE.finditer(masked):
        if _is_negated_or_meta(raw, match.start()):
            continue
        matched_str = match.group(0).lower()
        if "bao gồm" in matched_str or "đã gồm" in matched_str or "(gồm" in matched_str:
            continue
        start = match.start()
        prefix = masked[max(0, start - 25) : start].lower()
        if "bao gồm" in prefix or "đã gồm" in prefix:
            continue
        captured_rate = next((g for g in match.groups() if g is not None), None)
        if captured_rate:
            try:
                rate_val = float(captured_rate.replace(",", "."))
            except ValueError:
                continue
            if rate_val > 5.0:
                yield (
                    "REA001",
                    ERROR,
                    match.start() + 1,
                    match.group(0),
                    f"off-plan real estate deposit rate ({captured_rate}%) exceeds the 5% statutory cap under Article 23 Clause 5 of Law on Real Estate Business 2023",
                    "Article 23 Clause 5 of Law on Real Estate Business 2023 (Luật Kinh doanh bất động sản 2023) limits deposit for off-plan property to maximum 5% of selling price; cap deposit at 5% and verify statutory commercialization conditions",
                )

    # REA001: Disguised capital mobilization
    for match in DISGUISED_MOBILIZATION_RE.finditer(masked):
        if _is_negated_or_meta(raw, match.start()):
            continue
        yield (
            "REA001",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"unlawful capital mobilization disguised as deposit/booking “{match.group(0)}” prior to satisfying statutory sale conditions",
            "Article 23 Clause 5 Law on Real Estate Business 2023 prohibits disguised capital mobilization; deposits may only be collected after the project meets all statutory conditions for commercialization",
        )

    # REA002: Payment schedule violating Article 25
    # First installment > 30%
    if INSTALLMENT_PAYMENT_KW_RE.search(raw):
        for match in INSTALLMENT_1_RE.finditer(masked):
            captured_rate = next((g for g in match.groups() if g is not None), None)
            if captured_rate:
                try:
                    rate_val = float(captured_rate.replace(",", "."))
                except ValueError:
                    continue
                if rate_val > 30.0:
                    yield (
                        "REA002",
                        ERROR,
                        match.start() + 1,
                        match.group(0),
                        f"first installment payment ({captured_rate}%) exceeds the 30% statutory limit under Article 25 of Law on Real Estate Business 2023",
                        "first installment payment for off-plan real estate cannot exceed 30% of contract value (inclusive of deposit)",
                    )

    # Pre-handover > 70% (or > 50% for FDI)
    for match in PRE_HANDOVER_RE.finditer(masked):
        captured_rate = next((g for g in match.groups() if g is not None), None)
        if captured_rate:
            try:
                rate_val = float(captured_rate.replace(",", "."))
            except ValueError:
                continue
            is_fdi = bool(re.search(r"vốn\s+đầu\s+tư\s+nước\s+ngoài|fdi", ctx.text, re.IGNORECASE))
            cap = 50.0 if is_fdi else 70.0
            if rate_val > cap:
                yield (
                    "REA002",
                    ERROR,
                    match.start() + 1,
                    match.group(0),
                    f"pre-handover payment ({captured_rate}%) exceeds the statutory {int(cap)}% cap under Article 25 Law on Real Estate Business 2023",
                    f"cumulative payments prior to handover cannot exceed {int(cap)}% of contract value under Article 25",
                )

    # Pre-certificate > 95%
    for match in PRE_CERT_RE.finditer(masked):
        captured_rate = next((g for g in match.groups() if g is not None), None)
        if captured_rate:
            try:
                rate_val = float(captured_rate.replace(",", "."))
            except ValueError:
                continue
            if rate_val > 95.0:
                yield (
                    "REA002",
                    ERROR,
                    match.start() + 1,
                    match.group(0),
                    f"pre-certificate payment ({captured_rate}%) exceeds 95% statutory cap under Article 25 Law on Real Estate Business 2023",
                    "remaining 5% of contract value can only be collected after the Certificate of Land Use Rights and Assets Attached to Land is issued",
                )
        elif "100%" in match.group(0):
            yield (
                "REA002",
                ERROR,
                match.start() + 1,
                match.group(0),
                "collecting 100% contract value prior to certificate issuance violates Article 25 Law on Real Estate Business 2023",
                "Article 25 caps payments prior to certificate issuance at 95%; retain 5% until the Certificate is granted to the buyer",
            )

    # REA003: Commercial-service properties claiming permanent tenure
    if COMMERCIAL_PROPERTY_RE.search(masked) and PERMANENT_TENURE_RE.search(masked):
        comm_match = COMMERCIAL_PROPERTY_RE.search(masked)
        tenure_match = PERMANENT_TENURE_RE.search(masked)
        assert comm_match and tenure_match
        if not (_is_negated_or_meta(raw, tenure_match.start()) or _is_negated_or_meta(raw, comm_match.start())):
            yield (
                "REA003",
                ERROR,
                tenure_match.start() + 1,
                tenure_match.group(0),
                f"misleading permanent tenure claim “{tenure_match.group(0)}” for commercial-service property “{comm_match.group(0)}” on leasehold land",
                "commercial-service properties (condotels, officetels, resort villas, shophouses on commercial land) have limited 50/70-year leasehold tenure under Land Law 2024; never promise 'sổ đỏ lâu dài' or 'sở hữu vĩnh viễn'",
            )

    # REA004: Ambiguous apartment area
    for match in AREA_AMBIGUOUS_RE.finditer(masked):
        term = match.group(0)
        if "phủ bì" in term.lower():
            yield (
                "REA004",
                WARN,
                match.start() + 1,
                term,
                f"ambiguous area descriptor “{term}” without carpet area breakdown",
                "Article 141 Housing Law 2023 requires specifying usable carpet area ('diện tích thông thủy') and wall-center area ('diện tích tim tường'); avoid ambiguous 'diện tích phủ bì'",
            )
        elif "căn hộ" in term.lower():
            has_carpet = bool(AREA_CARPET_RE.search(masked) or AREA_CARPET_RE.search(ctx.text))
            has_wall_center = bool(AREA_WALL_CENTER_RE.search(masked) or AREA_WALL_CENTER_RE.search(ctx.text))
            if not (has_carpet or has_wall_center):
                yield (
                    "REA004",
                    WARN,
                    match.start() + 1,
                    term,
                    f"apartment area stated without specifying carpet area ('diện tích thông thủy') vs wall-center area ('diện tích tim tường')",
                    "under Article 141 Housing Law 2023, apartment sales contracts and specifications must clearly distinguish 'diện tích thông thủy' from 'diện tích tim tường'",
                )

    # REA005: Maintenance fund overcharge or premature collection
    for match in MAINTENANCE_FEE_OVERCHARGE_RE.finditer(masked):
        captured_rate = next((g for g in match.groups() if g is not None), None)
        if captured_rate:
            try:
                rate_val = float(captured_rate.replace(",", "."))
            except ValueError:
                continue
            if rate_val > 2.0:
                yield (
                    "REA005",
                    ERROR,
                    match.start() + 1,
                    match.group(0),
                    f"apartment maintenance fund rate ({captured_rate}%) exceeds the 2% statutory requirement under Article 152 Housing Law 2023",
                    "Article 152 of Housing Law 2023 (Luật Nhà ở 2023) sets the apartment common maintenance fund strictly at 2% of the apartment value before VAT",
                )

    for match in MAINTENANCE_PREMATURE_RE.finditer(masked):
        yield (
            "REA005",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"demanding 2% apartment maintenance fund at deposit/early stage “{match.group(0)}” prior to handover",
            "Article 152 Housing Law 2023 stipulates that the 2% apartment maintenance fund is paid upon receiving apartment handover, not at deposit or initial installment",
        )

    # REA006: Calques in real estate & construction BOQ
    for match in CALQUES_RE.finditer(masked):
        term_lower = match.group(1).lower()
        replacement = CALQUES_MAP.get(term_lower, "thuật ngữ chuẩn")
        yield (
            "REA006",
            WARN,
            match.start() + 1,
            match.group(1),
            f"literal English calque in real estate / construction “{match.group(1)}”",
            f"replace with conventional Vietnamese industry phrasing: '{replacement}'",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # REA005: Missing 2% maintenance fund in off-plan sales contracts
    if doctype == "off-plan-contract":
        has_maintenance = bool(re.search(r"kinh\s+phí\s+bảo\s+trì|phí\s+bảo\s+trì", body, re.IGNORECASE))
        if not has_maintenance:
            yield (
                "REA005",
                ERROR,
                first_line,
                1,
                "",
                "off-plan-contract missing mandatory 2% apartment maintenance fund disclosure ('kinh phí bảo trì phần sở hữu chung nhà chung cư 2%')",
                "Article 152 Housing Law 2023 mandates explicit disclosure of the 2% apartment maintenance fund in apartment sales contracts",
            )
