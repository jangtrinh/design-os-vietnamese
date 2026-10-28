# -*- coding: utf-8 -*-
"""Domain-specific validation rules for Vietnamese landing pages and conversion copy.

Loaded automatically by validate_copy.py via the `rules_*.py` pattern.
Standard library only, plain tuples contract:
(rule_id, severity, lineno_or_col, snippet, message, hint)
"""
from __future__ import annotations

import re

ERROR = "error"
WARN = "warning"

RULE_DOCS = {
    "LND001": "passive English construction ('được thiết kế bởi', 'được xây dựng bởi', 'được phát triển bởi') in hero/headline copy",
    "LND002": "lead-form collecting personal data without explicit purpose statement and privacy policy reference ('Chính sách bảo mật' / 'dữ liệu cá nhân', Luật 91/2025/QH15 Điều 9; NĐ 356/2025/NĐ-CP Điều 6)",
    "LND003": "e-commerce footer missing mandatory statutory fields ('MST' / 'Mã số doanh nghiệp' or 'Bộ Công Thương', NĐ 52/2013 & NĐ 85/2021)",
    "LND004": "pricing table mixing colloquial 'tỷ/triệu' and full grouped digits in the same table, or using '/month' instead of '/tháng'",
}

DOCTYPES = {
    "hero": "landing page hero section or headline",
    "lead-form": "lead capture form or consultation form",
    "ecommerce-footer": "e-commerce footer containing statutory disclosures",
    "pricing-table": "pricing plan table or subscription tier breakdown",
    "real-estate-project": "real estate project landing page or masterplan overview",
}

# LND001: Passive English constructions in hero/headline copy
PASSIVE_HERO_RE = re.compile(
    r"(?<!\w)được\s+(?:thiết\s+kế|xây\s+dựng|phát\s+triển|tạo\s+ra|chế\s+tác|thực\s+hiện|sản\s+xuất|vận\s+hành)\s+bởi(?!\w)",
    re.IGNORECASE,
)

# LND004: English billing intervals in pricing tables
BILLING_PERIOD_RE = re.compile(r"/(?:month|mo|yr|year)\b", re.IGNORECASE)

# LND004: Pricing scales (colloquial words vs full grouped digits)
WORD_SCALE_RE = re.compile(r"\b\d+[\s\u00A0]*(?:tỷ|triệu|nghìn|tr|k)\b", re.IGNORECASE)
GROUPED_NUM_RE = re.compile(r"\b\d{1,3}(?:\.\d{3})+\b")

# LND002: PDPD (Luật 91/2025/QH15 Điều 9; NĐ 356/2025/NĐ-CP Điều 6) required markers in lead forms
PURPOSE_RE = re.compile(r"(?:nhằm\s+mục\s+đích|mục\s+đích|để|phục\s+vụ\s+cho)", re.IGNORECASE)
PRIVACY_RE = re.compile(r"(?:chính\s+sách\s+bảo\s+mật|dữ\s+liệu\s+cá\s+nhân|bảo\s+vệ\s+dữ\s+liệu)", re.IGNORECASE)

# LND003: E-commerce footer statutory requirements (NĐ 52/2013/NĐ-CP & NĐ 85/2021/NĐ-CP)
TAX_ID_RE = re.compile(r"(?:mã\s+số\s+thuế|mã\s+số\s+doanh\s+nghiệp|mst|msdn)\b", re.IGNORECASE)
MOIT_RE = re.compile(r"(?:bộ\s+công\s+thương|đã\s+thông\s+báo\s+bộ\s+công\s+thương|đã\s+đăng\s+ký\s+bộ\s+công\s+thương)", re.IGNORECASE)


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


def check_line(ctx, lineno, raw, masked):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype == "hero":
        for m in PASSIVE_HERO_RE.finditer(masked):
            yield (
                "LND001",
                WARN,
                m.start() + 1,
                m.group(0),
                f"passive English construction “{m.group(0)}” in hero copy",
                "front the actor: write “Do [đối tượng] thiết kế/xây dựng” instead of the passive English calque “được ... bởi”",
            )

    if doctype == "pricing-table":
        for m in BILLING_PERIOD_RE.finditer(masked):
            yield (
                "LND004",
                WARN,
                m.start() + 1,
                m.group(0),
                f"English billing period “{m.group(0)}” in pricing table",
                "use Vietnamese billing periods: “/tháng”, “/năm”, or “/người dùng/tháng”",
            )


def check_document(ctx):
    doctype = ctx.doctype
    if not doctype:
        return

    if doctype == "lead-form":
        text = "\n".join(ctx.masked)
        has_purpose = bool(PURPOSE_RE.search(text))
        has_privacy = bool(PRIVACY_RE.search(text))
        if not (has_purpose and has_privacy):
            first_line = next((l.strip() for l in ctx.lines if not _is_comment_or_blank(l)), "")[:40]
            yield (
                "LND002",
                WARN,
                1,
                1,
                first_line,
                "lead-form collecting personal data without explicit purpose statement and privacy policy reference",
                "Luật 91/2025/QH15 Điều 9; NĐ 356/2025/NĐ-CP Điều 6 require an explicit purpose statement (e.g. “nhằm mục đích tư vấn”) and reference to “Chính sách bảo mật” / “dữ liệu cá nhân”",
            )

    if doctype == "ecommerce-footer":
        text = "\n".join(ctx.masked)
        has_tax = bool(TAX_ID_RE.search(text))
        has_moit = bool(MOIT_RE.search(text))
        if not (has_tax and has_moit):
            first_line = next((l.strip() for l in ctx.lines if not _is_comment_or_blank(l)), "")[:40]
            yield (
                "LND003",
                WARN,
                1,
                1,
                first_line,
                "e-commerce footer missing mandatory statutory fields ('MST' / 'Mã số doanh nghiệp' or 'Bộ Công Thương')",
                "Nghị định 52/2013/NĐ-CP & 85/2021/NĐ-CP require Tax ID (MST/Mã số doanh nghiệp) and registration notification with Bộ Công Thương",
            )

    if doctype == "pricing-table":
        text = "\n".join(ctx.masked)
        if WORD_SCALE_RE.search(text) and GROUPED_NUM_RE.search(text):
            first_line = next((l.strip() for l in ctx.lines if not _is_comment_or_blank(l)), "")[:40]
            yield (
                "LND004",
                WARN,
                1,
                1,
                first_line,
                "pricing table mixing colloquial 'tỷ/triệu' and full grouped digits in the same table",
                "standardize pricing notation: either use full period-grouped figures (e.g. 500.000 ₫) or word scale (500 nghìn ₫), not both in one table",
            )
