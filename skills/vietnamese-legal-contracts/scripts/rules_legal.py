# -*- coding: utf-8 -*-
"""Rules for Vietnamese legal contracts, ToS, labor, IP, and PDPD compliance.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and regulatory compliance across Vietnamese civil
and commercial agreements (Bộ luật Dân sự 2015 & Luật Thương mại 2005), labor
contracts (Bộ luật Lao động 2019), consumer terms of service (Luật Bảo vệ quyền
lợi người tiêu dùng 2023), personal data protection agreements (Nghị định 13/2023/NĐ-CP
& Luật Dữ liệu 2024), and intellectual property licensing/assignments (Luật Sở hữu
trí tuệ sửa đổi 2022).
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "commercial-contract": "Hợp đồng thương mại / Hợp đồng cung ứng dịch vụ B2B (Luật Thương mại 2005 & Bộ luật Dân sự 2015)",
    "civil-contract": "Hợp đồng dân sự / Hợp đồng thuê tài sản / Hợp đồng vay tài sản (Bộ luật Dân sự 2015)",
    "labor-contract": "Hợp đồng lao động (Bộ luật Lao động 2019 — Số 45/2019/QH14)",
    "terms-of-service": "Điều khoản sử dụng dịch vụ (ToS) / Hợp đồng theo mẫu & Điều kiện giao dịch chung (Luật Bảo vệ quyền lợi người tiêu dùng 2023)",
    "pdpd-policy": "Chính sách bảo mật & Thỏa thuận xử lý dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP & Luật Dữ liệu 2024)",
}

RULE_DOCS = {
    "LEG001": "penalty for breach ('phạt vi phạm') exceeding 8% statutory cap of breached obligation under Article 301 of Commercial Law 2005 (Luật Thương mại 2005 Điều 301)",
    "LEG002": "obsolete seasonal labor contract ('hợp đồng lao động mùa vụ' / 'theo mùa vụ') abolished by Article 20 of Labor Code 2019 (Bộ luật Lao động 2019)",
    "LEG003": "foreign statutory citation hierarchy ('Điều 15 Khoản 2' / 'Điều 15.2(a)'); standard Vietnamese order is 'Khoản 2 Điều 15' or 'Điểm a Khoản 2 Điều 15' (Luật Ban hành văn bản QPPL)",
    "LEG004": "unconscionable blanket liability waiver in consumer terms ('miễn trừ hoàn toàn mọi trách nhiệm', 'chúng tôi không chịu bất kỳ trách nhiệm nào trong mọi trường hợp') prohibited under Article 25 of Consumer Protection Law 2023 (Luật Bảo vệ quyền lợi người tiêu dùng 2023)",
    "LEG005": "obsolete statute name ('Bộ luật Dân sự 2005', 'Bộ luật Lao động 2012', 'Luật Doanh nghiệp 2014', 'Luật Sở hữu trí tuệ 2005 chưa sửa đổi') used without historical context",
    "LEG006": "commercial or civil contract missing mandatory dispute resolution clause ('Giải quyết tranh chấp' / 'Tòa án' / 'Trọng tài') or force majeure clause ('Bất khả kháng')",
    "LEG007": "PDPD policy / DPA missing mandatory data subject rights under Article 9 of Decree 13/2023/NĐ-CP ('Quyền của chủ thể dữ liệu' / 'rút lại sự đồng ý' / 'yêu cầu xóa dữ liệu')",
}

# LEG001: Commercial penalty rate > 8%
PENALTY_RATE_RE = re.compile(
    r"(?<!\w)(?:"
    r"phạt\s+vi\s+phạm(?:\s+hợp\s+đồng)?(?:\s+là|\s+ở\s+mức|\s+mức)?\s*:?\s*(\d+(?:[.,]\d+)?)\s*%|"
    r"mức\s+phạt(?:\s+vi\s+phạm)?(?:\s+hợp\s+đồng)?(?:\s+là|\s*:|\s+ở\s+mức|\s+mức)?\s*(\d+(?:[.,]\d+)?)\s*%|"
    r"tiền\s+phạt\s+vi\s+phạm(?:\s+hợp\s+đồng)?(?:\s+là)?\s*(\d+(?:[.,]\d+)?)\s*%|"
    r"(?:bị\s+)?phạt\s+(\d+(?:[.,]\d+)?)\s*%\s*(?:giá\s+trị|tổng\s+giá\s+trị|phần\s+nghĩa\s+vụ)|"
    r"phạt\s+vi\s+phạm\s+[^\n.,;:]*?(\d+(?:[.,]\d+)?)\s*%"
    r")(?!\w)",
    re.IGNORECASE,
)

# LEG002: Obsolete seasonal labor contracts
OBSOLETE_LABOR_RE = re.compile(
    r"(?<!\w)(?:"
    r"hợp\s+đồng\s+(?:lao\s+động\s+)?(?:theo\s+)?mùa\s+vụ|"
    r"lao\s+động\s+mùa\s+vụ|"
    r"hợp\s+đồng\s+mùa\s+vụ(?:\s+hoặc\s+theo\s+một\s+công\s+việc\s+nhất\s+định)?"
    r")(?!\w)",
    re.IGNORECASE,
)

# LEG003: Foreign citation hierarchy (Điều -> Khoản -> Điểm)
FOREIGN_CITATION_RE = re.compile(
    r"(?<!\w)(?:"
    r"Điều\s+\d+[\s,]+(?:Khoản\s+\d+|\.\d+|\(\d+\))(?:\s*(?:Điểm\s+[a-zđ]|\([a-zđ]\)))?|"
    r"Điều\s+\d+\.\d+(?:\([a-zđ0-9]+\))?|"
    r"Điều\s+\d+\s*\(\d+\)(?:\([a-zđ0-9]+\))?"
    r")(?!\w)",
    re.IGNORECASE,
)

# LEG004: Unconscionable blanket liability waiver in consumer terms
BLANKET_WAIVER_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:chúng\s+tôi|công\s+ty|bên\s+cung\s+cấp|nhà\s+cung\s+cấp)\s+(?:hoàn\s+toàn\s+)?không\s+chịu\s+(?:bất\s+kỳ\s+)?trách\s+nhiệm\s+(?:nào\s+)?trong\s+mọi\s+trường\s+hợp|"
    r"trong\s+mọi\s+trường\s+hợp[^\n.,;]*không\s+chịu\s+(?:bất\s+kỳ\s+)?trách\s+nhiệm|"
    r"miễn\s+trừ\s+hoàn\s+toàn\s+mọi\s+trách\s+nhiệm(?:\s+pháp\s+lý)?|"
    r"miễn\s+trừ\s+toàn\s+bộ\s+trách\s+nhiệm(?:\s+pháp\s+lý|\s+bồi\s+thường)?(?:\s+trong\s+mọi\s+trường\s+hợp)?|"
    r"khách\s+hàng\s+(?:tự\s+chịu\s+mọi\s+rủi\s+ro\s+và\s+)?từ\s+bỏ\s+(?:mọi\s+)?quyền\s+khiếu\s+nại(?:,\s*khiếu\s+kiện)?|"
    r"từ\s+bỏ\s+(?:mọi\s+)?quyền\s+khiếu\s+nại(?:,\s*khiếu\s+kiện)?|"
    r"loại\s+trừ\s+hoàn\s+toàn\s+trách\s+nhiệm\s+bồi\s+thường|"
    r"khách\s+hàng\s+tự\s+chịu\s+mọi\s+rủi\s+ro"
    r")(?!\w)",
    re.IGNORECASE,
)

# LEG005: Obsolete legal document names
OBSOLETE_STATUTE_RE = re.compile(
    r"(?<!\w)(?:"
    r"Bộ\s+luật\s+Dân\s+sự\s+2005|"
    r"Bộ\s+luật\s+Lao\s+động\s+2012|"
    r"Luật\s+Doanh\s+nghiệp\s+2014|"
    r"Luật\s+Doanh\s+nghiệp\s+2005|"
    r"Luật\s+Sở\s+hữu\s+trí\s+tuệ\s+2005\s+chưa\s+sửa\s+đổi|"
    r"Luật\s+Bảo\s+vệ\s+quyền\s+lợi\s+người\s+tiêu\s+dùng\s+2010|"
    r"Luật\s+Thương\s+mại\s+1997"
    r")(?!\w)",
    re.IGNORECASE,
)

# LEG006: Dispute resolution and force majeure markers for contracts
DISPUTE_RE = re.compile(
    r"(?<!\w)(?:giải\s+quyết\s+tranh\s+chấp|luật\s+áp\s+dụng|cơ\s+quan\s+tài\s+phán|tòa\s+án|trọng\s+tài|viac)(?!\w)",
    re.IGNORECASE,
)
FORCE_MAJEURE_RE = re.compile(
    r"(?<!\w)(?:bất\s+khả\s+kháng|sự\s+kiện\s+bất\s+khả\s+kháng)(?!\w)",
    re.IGNORECASE,
)

# LEG007: Mandatory PDPD data subject rights markers
PDPD_RIGHTS_RE = re.compile(r"(?<!\w)quyền\s+của\s+chủ\s+thể\s+dữ\s+liệu(?!\w)", re.IGNORECASE)
PDPD_WITHDRAW_RE = re.compile(r"(?<!\w)rút\s+lại\s+sự\s+đồng\s+ý(?!\w)", re.IGNORECASE)
PDPD_ERASURE_RE = re.compile(r"(?<!\w)(?:xóa\s+dữ\s+liệu|yêu\s+cầu\s+xóa\s+dữ\s+liệu)(?!\w)", re.IGNORECASE)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # LEG001: Commercial contract breach penalty > 8%
    # Gated to commercial-contract or untyped contract context (sparing explicit civil contracts)
    if ctx.doctype == "commercial-contract" or (
        ctx.doctype is None and not re.search(r"hợp\s+đồng\s+dân\s+sự", ctx.text, re.IGNORECASE)
    ):
        for match in PENALTY_RATE_RE.finditer(masked):
            captured_rate = next((g for g in match.groups() if g is not None), None)
            if captured_rate:
                try:
                    rate_val = float(captured_rate.replace(",", "."))
                except ValueError:
                    continue
                if rate_val > 8.0:
                    yield (
                        "LEG001",
                        ERROR,
                        match.start() + 1,
                        match.group(0),
                        f"penalty for breach ({captured_rate}%) exceeds the 8% statutory cap under Article 301 of Commercial Law 2005 (Luật Thương mại 2005 Điều 301)",
                        "cap penalty for breach at maximum 8% of the breached contract obligation value ('không quá 8% giá trị phần nghĩa vụ hợp đồng bị vi phạm'); damages ('bồi thường thiệt hại') may be claimed separately",
                    )

    # LEG002: Obsolete seasonal labor contract
    for match in OBSOLETE_LABOR_RE.finditer(masked):
        yield (
            "LEG002",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"obsolete labor contract type “{match.group(0)}” abolished under Article 20 of Labor Code 2019",
            "Bộ luật Lao động 2019 recognizes only indefinite-term ('không xác định thời hạn') and fixed-term up to 36 months ('xác định thời hạn không quá 36 tháng'); replace seasonal contract with fixed-term labor contract",
        )

    # LEG003: Foreign citation ordering
    for match in FOREIGN_CITATION_RE.finditer(masked):
        yield (
            "LEG003",
            WARN,
            match.start() + 1,
            match.group(0),
            f"foreign statutory citation hierarchy “{match.group(0)}”",
            "recast into standard Vietnamese legislative hierarchy: 'Khoản ... Điều ...' or 'Điểm ... Khoản ... Điều ...' (Luật Ban hành văn bản quy phạm pháp luật)",
        )

    # LEG004: Unconscionable blanket liability waiver in consumer terms
    for match in BLANKET_WAIVER_RE.finditer(masked):
        yield (
            "LEG004",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"unconscionable blanket liability waiver / consumer rights exclusion “{match.group(0)}”",
            "clauses totally waiving vendor liability or excluding consumer complaint/litigation rights are null and void (vô hiệu) under Article 25 of Luật Bảo vệ quyền lợi người tiêu dùng 2023; define proportionate liability boundaries and lawful statutory exemptions instead",
        )

    # LEG005: Obsolete legal document names
    for match in OBSOLETE_STATUTE_RE.finditer(masked):
        yield (
            "LEG005",
            WARN,
            match.start() + 1,
            match.group(0),
            f"obsolete legal document name “{match.group(0)}”",
            "update to current effective statute (Bộ luật Dân sự 2015, Bộ luật Lao động 2019, Luật Doanh nghiệp 2020, Luật Sở hữu trí tuệ sửa đổi 2022, Luật Bảo vệ quyền lợi người tiêu dùng 2023)",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # LEG006: Missing dispute resolution or force majeure clause in contracts
    if doctype in ("commercial-contract", "civil-contract"):
        has_dispute = bool(DISPUTE_RE.search(body))
        has_force_majeure = bool(FORCE_MAJEURE_RE.search(body))

        if not has_dispute:
            yield (
                "LEG006",
                ERROR,
                first_line,
                1,
                "",
                f"{doctype} missing mandatory dispute resolution clause ('Giải quyết tranh chấp' / 'Tòa án' / 'Trọng tài')",
                "contracts under BLDS 2015 & Luật Thương mại 2005 must include a governing law and dispute resolution mechanism ('Giải quyết tranh chấp', 'Tòa án có thẩm quyền', or 'Trọng tài thương mại')",
            )
        if not has_force_majeure:
            yield (
                "LEG006",
                ERROR,
                first_line,
                1,
                "",
                f"{doctype} missing mandatory force majeure clause ('Bất khả kháng')",
                "contracts under BLDS 2015 Điều 156 must define force majeure events ('Sự kiện bất khả kháng') and notification procedures",
            )

    # LEG007: Missing PDPD data subject rights
    if doctype == "pdpd-policy":
        has_rights = bool(PDPD_RIGHTS_RE.search(body))
        has_withdraw = bool(PDPD_WITHDRAW_RE.search(body))
        has_erasure = bool(PDPD_ERASURE_RE.search(body))

        if not (has_rights and has_withdraw and has_erasure):
            missing_items = []
            if not has_rights:
                missing_items.append("quy định về quyền của chủ thể dữ liệu")
            if not has_withdraw:
                missing_items.append("quyền rút lại sự đồng ý")
            if not has_erasure:
                missing_items.append("quyền yêu cầu xóa dữ liệu")
            yield (
                "LEG007",
                ERROR,
                first_line,
                1,
                "",
                f"pdpd-policy missing mandatory data subject rights under Article 9 of Decree 13/2023/NĐ-CP: {'; '.join(missing_items)}",
                "Article 9 Decree 13/2023/NĐ-CP mandates explicit enumeration of data subject rights including the right to withdraw consent ('rút lại sự đồng ý') and right to erasure ('xóa dữ liệu cá nhân')",
            )
