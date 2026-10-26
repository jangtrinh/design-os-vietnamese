# -*- coding: utf-8 -*-
"""Rules for Vietnamese finance copy that a calque table cannot express.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and regulatory compliance across Vietnamese financial
documents, financial statements (BCTC under Thông tư 99/2025/TT-BTC), electronic
invoices (hóa đơn điện tử under Nghị định 123/2020/NĐ-CP & Nghị định 70/2025/NĐ-CP),
consumer lending and BNPL transparency (Thông tư 43/2016/TT-NHNN & Thông tư 18/2019/TT-NHNN),
securities and fund marketing (Luật Chứng khoán 2019 & Nghị định 38/2018/NĐ-CP),
investment-linked insurance disclaimers (Thông tư 67/2023/TT-BTC Điều 53),
and FinTech transfer / biometric security thresholds (Quyết định 2345/QĐ-NHNN).

FIN001 is the exception to the doctype gating: guaranteed-return language is prohibited
in investment solicitation regardless of document type, so it fires unconditionally.
All other rules evaluate within their relevant doctype contexts.
"""
from __future__ import annotations

import pathlib
import re

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

RULE_DOCS = {
    "FIN001": "guaranteed-return language ('cam kết lợi nhuận', 'đảm bảo sinh lời', 'bảo toàn vốn', 'đầu tư không rủi ro') — prohibited in solicitation (Luật CK Đ12; NĐ 38/2018)",
    "FIN002": "promotional 0% rate ('lãi suất 0%', 'trả góp 0%') with no explicit fee or total-cost disclosure ('phí chuyển đổi', 'tổng chi phí', 'lãi suất thực tế', 'tổng số tiền phải trả' — TT 43/2016)",
    "FIN005": "financial statement table missing 'Đơn vị tính' header",
    "FIN006": "negative number written with a minus sign (-1.234) in a financial statement; use parentheses (1.234)",
    "FIN007": "e-invoice missing mandatory statutory fields ('MST' or 'thuế GTGT', NĐ 123/2020 & NĐ 70/2025)",
    "FIN008": "investment-linked insurance copy ('bảo hiểm liên kết đầu tư', 'ILP', 'UL') missing explicit disclaimer that it is an insurance product, not a bank deposit, and policyholder bears investment risk (TT 67/2023/TT-BTC Điều 53)",
    "FIN009": "high-value bank transfer UI (> 10 triệu đồng per transaction or > 20 triệu đồng/day) omitting biometric authentication requirement ('sinh trắc học' / 'khuôn mặt' / 'CCCD gắn chip', QĐ 2345/QĐ-NHNN)",
}

DOCTYPES = {
    "statement": "a financial statement or reporting table",
    "e-invoice": "an electronic invoice (hóa đơn điện tử)",
    "financial-promotion": "marketing for a financial, banking, or insurance product",
    "disclosure": "a regulatory disclosure document",
    "loan": "loan, credit, or installment product copy",
    "insurance": "insurance product copy, policy wording, or solicitation",
    "fintech-transfer": "instant payment, VietQR, NAPAS, or money transfer UI",
}

GUARANTEED_MARKER = "<!-- machine-readable: guaranteed-return -->"

FALLBACK_GUARANTEED = (
    r"cam\s+kết\s+(?:lợi\s+nhuận|lãi\s+suất|sinh\s+lời|hoàn\s+vốn)",
    r"đảm\s+bảo\s+(?:sinh\s+lời|lợi\s+nhuận|có\s+lãi)",
    r"đầu\s+tư\s+không\s+(?:có\s+)?rủi\s+ro",
    r"bảo\s+toàn\s+vốn",
    r"chắc\s+chắn\s+có\s+lãi",
    r"sinh\s+lời\s+chắc\s+chắn",
    r"không\s+bao\s+giờ\s+lỗ",
    r"an\s+toàn\s+100\s*%\s+vốn",
)

RATE_ZERO_RE = re.compile(
    r"(?<!\w)(?:lãi\s+suất\s*0\s*%|0\s*%\s*lãi\s+suất|trả\s+góp\s*0\s*%|0\s*%\s*trả\s+góp|0\s*đ(?!\w))",
    re.IGNORECASE,
)
COST_DISCLOSURE_RE = re.compile(
    r"(?<!\w)(?:phí\s+chuyển\s+đổi|tổng\s+chi\s+phí|lãi\s+suất\s+thực\s+tế|tổng\s+số\s+tiền\s+phải\s+trả|chi\s+phí\s+chuyển\s+đổi)(?!\w)",
    re.IGNORECASE,
)

UNIT_HEADER_RE = re.compile(r"đơn\s+vị\s+tính", re.IGNORECASE)
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")

# Grouped or bare negative number carrying leading minus: -1.234 or -1.234.000. Spares year ranges like 2020-2026.
MINUS_NUMBER_RE = re.compile(r"(?<![\w\d.,])[-−–]\s?\d{1,3}(?:\.\d{3})*(?:,\d+)?(?![\w])")

MST_RE = re.compile(r"(?<!\w)MST(?!\w)", re.IGNORECASE)
VAT_RE = re.compile(r"(?<!\w)(thuế\s*GTGT|giá\s+trị\s+gia\s+tăng)(?!\w)", re.IGNORECASE)

# Investment-linked insurance triggers under TT 67/2023/TT-BTC
ILP_TRIGGER_RE = re.compile(
    r"(?<!\w)(?:bảo\s+hiểm\s+liên\s+kết\s+(?:đầu\s+tư|chung|đơn\s+vị)|sản\s+phẩm\s+ILP|hợp\s+đồng\s+ILP|\bILP\b|\bUL\b)(?!\w)",
    re.IGNORECASE,
)
NOT_DEPOSIT_RE = re.compile(
    r"(?<!\w)(?:không\s+phải\s+(?:là\s+)?(?:sản\s+phẩm\s+)?tiết\s+kiệm|không\s+phải\s+(?:là\s+)?tiền\s+gửi(?: ngân hàng)?|đây\s+là\s+sản\s+phẩm\s+bảo\s+hiểm,\s+không\s+phải)",
    re.IGNORECASE,
)
BEARS_RISK_RE = re.compile(
    r"(?<!\w)(?:(?:bên\s+mua\s+bảo\s+hiểm|khách\s+hàng|người\s+tham\s+gia)\s+chịu\s+(?:mọi\s+)?rủi\s+ro|kết\s+quả\s+đầu\s+tư\s+không\s+được\s+đảm\s+bảo|không\s+được\s+bảo\s+đảm\s+lợi\s+nhuận)(?!\w)",
    re.IGNORECASE,
)

# High-value transfer trigger under QĐ 2345/QĐ-NHNN (> 10 triệu/giao dịch hoặc > 20 triệu/ngày)
HIGH_VALUE_TRANSFER_RE = re.compile(
    r"(?<!\w)(?:(?:chuyển\s+(?:khoản|tiền)|giao\s+dịch|thanh\s+toán|hạn\s+mức)\s*(?:[^\n.]{0,25}?)\s*(?:trên|>|vượt|từ)\s*(?:10|20)\s*(?:triệu|tr|trđ)|(?:trên|>|vượt)\s*10\.000\.000\s*(?:₫|đ|vnd)?|10\.000\.00[1-9]\s*(?:₫|đ|vnd)?|(?:[1-9]\d|[1-9]\d{2,})\.000\.000\s*(?:₫|đ|vnd)?|trên\s*20\s*triệu\s*(?:đồng)?\s*/\s*ngày)(?!\w)",
    re.IGNORECASE,
)
BIOMETRIC_AUTH_RE = re.compile(
    r"(?<!\w)(?:sinh\s+trắc\s+học|khuôn\s+mặt|cccd\s+gắn\s+chip|nhận\s+diện\s+khuôn\s+mặt|vneid\s+mức\s*2|xác\s+thực\s+(?:bằng\s+)?khuôn\s+mặt)(?!\w)",
    re.IGNORECASE,
)


def _load_guaranteed_patterns():
    """Parse the guaranteed-return table out of references/glossary.md."""
    path = REF_DIR / "glossary.md"
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        text = ""
    index = text.find(GUARANTEED_MARKER)
    raw = []
    if index != -1:
        started = False
        for line in text[index + len(GUARANTEED_MARKER):].splitlines():
            line = line.strip()
            if not line.startswith("|"):
                if started:
                    break
                continue
            started = True
            if set(line) <= set("|-: "):
                continue
            cells = [c.replace(r"\|", "|").strip() for c in re.split(r"(?<!\\)\|", line)[1:-1]]
            if cells:
                raw.append(cells[0].strip().strip("`").strip())
        raw = raw[1:]  # drop header row
    compiled = []
    for pattern in raw or FALLBACK_GUARANTEED:
        try:
            compiled.append(re.compile(pattern, re.IGNORECASE))
        except re.error:
            continue
    return compiled or [re.compile(p, re.IGNORECASE) for p in FALLBACK_GUARANTEED]


GUARANTEED = _load_guaranteed_patterns()


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str):
    # FIN001 is never gated: guaranteed-return phrasing is prohibited wherever it appears
    for regex in GUARANTEED:
        for match in regex.finditer(masked):
            yield (
                "FIN001",
                WARN,
                match.start() + 1,
                match.group(0),
                f"guaranteed-return language “{match.group(0)}”",
                "prohibited in investment solicitation (Luật Chứng khoán 2019 Đ12; "
                "NĐ 38/2018 Đ2 kh.4). Write “lợi nhuận kỳ vọng” with a risk disclaimer, "
                "and route to legal review.",
            )

    if ctx.doctype == "statement":
        if _is_comment_or_blank(raw):
            return
        for match in MINUS_NUMBER_RE.finditer(masked):
            yield (
                "FIN006",
                WARN,
                match.start() + 1,
                match.group(0).strip(),
                f"negative written as “{match.group(0).strip()}”",
                "financial statements write negatives in parentheses — (1.234), not -1.234",
            )


def check_document(ctx):
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    first = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # FIN002: Promotional 0% rate without fee or total-cost disclosure
    if doctype in ("financial-promotion", "loan", "statement", "e-invoice", "disclosure", "insurance", "fintech-transfer"):
        match = RATE_ZERO_RE.search(body)
        if match and not COST_DISCLOSURE_RE.search(body):
            line = body[:match.start()].count("\n") + 1
            yield (
                "FIN002",
                WARN,
                line,
                1,
                match.group(0),
                f"promotional 0% rate “{match.group(0)}” with no fee or total-cost disclosure",
                "Thông tư 43/2016/TT-NHNN (amended by TT 18/2019/TT-NHNN) requires publishing "
                "the fee schedule ('phí chuyển đổi'), total cost ('tổng chi phí'), or total repayment "
                "amount ('tổng số tiền phải trả') beside any promotional 0% rate claim.",
            )

    # FIN005: Financial statement table missing "Đơn vị tính" header
    if doctype == "statement":
        has_table = any(TABLE_ROW_RE.match(raw) for raw in ctx.lines)
        if has_table and not UNIT_HEADER_RE.search(body):
            yield (
                "FIN005",
                WARN,
                first,
                1,
                "",
                "financial statement table missing “Đơn vị tính” header",
                "add “Đơn vị tính: triệu đồng” (hoặc tỷ đồng / VND) — without it readers "
                "cannot distinguish units of magnitude.",
            )

    # FIN007: E-invoice missing mandatory statutory fields
    if doctype == "e-invoice" and body.strip():
        if not MST_RE.search(body):
            yield (
                "FIN007",
                WARN,
                first,
                1,
                "",
                "invoice does not name a tax code (MST)",
                "Mã số thuế (MST) is a mandatory e-invoice field under Nghị định 123/2020/NĐ-CP "
                "and Nghị định 70/2025/NĐ-CP.",
            )
        if not VAT_RE.search(body):
            yield (
                "FIN007",
                WARN,
                first,
                1,
                "",
                "invoice does not name the VAT treatment (thuế GTGT)",
                "thuế GTGT is a mandatory e-invoice field under Nghị định 123/2020/NĐ-CP "
                "and Nghị định 70/2025/NĐ-CP.",
            )

    # FIN008: Investment-linked insurance missing disclaimers under TT 67/2023/TT-BTC Điều 53
    if doctype in ("insurance", "financial-promotion", "disclosure"):
        match_ilp = ILP_TRIGGER_RE.search(body)
        if match_ilp:
            has_not_deposit = bool(NOT_DEPOSIT_RE.search(body))
            has_bears_risk = bool(BEARS_RISK_RE.search(body))
            if not (has_not_deposit and has_bears_risk):
                line = body[:match_ilp.start()].count("\n") + 1
                missing = []
                if not has_not_deposit:
                    missing.append("sản phẩm không phải là tiền gửi ngân hàng/tiết kiệm")
                if not has_bears_risk:
                    missing.append("bên mua bảo hiểm chịu mọi rủi ro đầu tư")
                yield (
                    "FIN008",
                    WARN,
                    line,
                    1,
                    match_ilp.group(0),
                    f"investment-linked insurance copy “{match_ilp.group(0)}” missing statutory disclaimers",
                    "Thông tư 67/2023/TT-BTC Điều 53 mandates explicit disclaimers: "
                    + "; ".join(missing),
                )

    # FIN009: High-value transfer omitting biometric authentication under QĐ 2345/QĐ-NHNN
    if doctype in ("fintech-transfer", "financial-promotion", "disclosure"):
        match_hv = HIGH_VALUE_TRANSFER_RE.search(body)
        if match_hv and not BIOMETRIC_AUTH_RE.search(body):
            line = body[:match_hv.start()].count("\n") + 1
            yield (
                "FIN009",
                WARN,
                line,
                1,
                match_hv.group(0),
                f"high-value bank transfer UI “{match_hv.group(0)}” omitting biometric authentication requirement",
                "Quyết định 2345/QĐ-NHNN mandates biometric authentication ('sinh trắc học' / "
                "'khuôn mặt' / 'CCCD gắn chip') for transfers > 10.000.000 ₫ per transaction "
                "or aggregate transfers > 20.000.000 ₫/day.",
            )
