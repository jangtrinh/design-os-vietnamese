# -*- coding: utf-8 -*-
"""Rules for Vietnamese insurance, InsurTech, and Bancassurance compliance.

Loaded automatically by validate_copy.py because the filename starts with `rules_`.
Pure Python standard library only.

This module enforces statutory and regulatory compliance across Vietnamese insurance
illustrations, certificates, and claim guides under the Law on Insurance Business 2022
(Luật Kinh doanh bảo hiểm số 08/2022/QH15) and Ministry of Finance Circular 67/2023/TT-BTC.
"""
from __future__ import annotations

import pathlib
import re
from typing import Iterator, Tuple

ERROR = "error"
WARN = "warning"

REF_DIR = pathlib.Path(__file__).resolve().parent.parent / "references"

DOCTYPES = {
    "policy-illustration": "Tài liệu minh họa bán hàng & Giới thiệu sản phẩm bảo hiểm nhân thọ / liên kết đầu tư (Luật KDBH 2022 & TT 67/2023/TT-BTC)",
    "insurance-certificate": "Giấy chứng nhận bảo hiểm & Tóm tắt quy tắc, điều khoản bảo hiểm (Luật Kinh doanh bảo hiểm 2022)",
    "claim-guide": "Hướng dẫn giải quyết quyền lợi bảo hiểm / Thông báo bồi thường (Điều 31 Luật KDBH 2022)",
}

RULE_DOCS = {
    "INS001": "disguising investment-linked life insurance ('bảo hiểm liên kết đầu tư/chung/đơn vị') as a fixed-interest bank savings deposit ('tiết kiệm ngân hàng cam kết lãi suất', 'lợi nhuận cố định 100% không rủi ro') prohibited under Law on Insurance Business 2022 & Circular 67/2023/TT-BTC",
    "INS002": "life insurance illustration or welcome kit omitting the mandatory 21-day free-look period ('thời gian cân nhắc tham gia bảo hiểm 21 ngày') or stating a shorter free-look period violating Article 35 of Law on Insurance Business 2022",
    "INS003": "hiding or waiving disclosure of liability exclusion clauses ('không cần đọc điều khoản loại trừ', 'chi trả mọi rủi ro không loại trừ', or certificate missing exclusion section) violating Article 19 of Law on Insurance Business 2022",
    "INS004": "confusing or machine-translating Vietnamese statutory insurance terminology ('chính sách bảo hiểm' for contract, 'người giữ chính sách' for policyholder, 'tiền thưởng bảo hiểm' for premium, 'câu chuyện bảo hiểm' for coverage, 'sự kiện thiên Chúa' for force majeure)",
    "INS005": "unlawful claim settlement timeline exceeding statutory limits (e.g. 60 or 90 days) violating Article 31 of Law on Insurance Business 2022 (statutory maximum 15 days, or up to 30 days when verification is required)",
    "INS006": "coercive bancassurance tying ('bắt buộc mua bảo hiểm nhân thọ mới được giải ngân khoản vay') prohibited under Circular 67/2023/TT-BTC and Law on Credit Institutions 2024",
}

# INS001: Disguising investment-linked insurance as fixed-yield bank savings deposit
SAVINGS_DISGUISE_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:sản\s+phẩm\s+)?tiết\s+kiệm\s+ngân\s+hàng\s+lãi\s+suất\s+cam\s+kết|"
    r"gửi\s+tiết\s+kiệm(?:\s+đầu\s+tư)?\s+cam\s+kết\s+lợi\s+nhuận(?:\s+cố\s+định)?|"
    r"tiết\s+kiệm\s+đầu\s+tư\s+cam\s+kết\s+(?:lãi\s+suất|lợi\s+nhuận)|"
    r"(?:tiết\s+kiệm\s+ngân\s+hàng|gửi\s+tiết\s+kiệm)[^\n.,;:]*?(?:lãi\s+suất\s+cam\s+kết\s+\d+|cam\s+kết\s+lợi\s+nhuận|không\s+rủi\s+ro)|"
    r"(?:bảo\s+hiểm\s+liên\s+kết\s+(?:đầu\s+tư|chung|đơn\s+vị))[^\n.,;:]*?(?:như\s+gửi\s+tiết\s+kiệm|lãi\s+suất\s+cam\s+kết|lợi\s+nhuận\s+cố\s+định|không\s+rủi\s+ro)"
    r")(?!\w)",
    re.IGNORECASE,
)

# INS002: Free-look period misstated, shortened, or waived
FREE_LOOK_MISSTATED_RE = re.compile(
    r"(?<!\w)(?:"
    r"thời\s+gian\s+cân\s+nhắc(?:\s+tham\s+gia\s+bảo\s+hiểm)?\s+(?:là\s+)?(?:[1-9]|1[0-9]|20)\s+ngày|"
    r"thời\s+gian\s+cân\s+nhắc\s+(?:7|10|14)\s+ngày|"
    r"không\s+(?:được\s+)?hủy\s+hợp\s+đồng\s+(?:sau\s+khi\s+ký|trong\s+mọi\s+trường\s+hợp)|"
    r"không\s+có\s+thời\s+gian\s+cân\s+nhắc"
    r")(?!\w)",
    re.IGNORECASE,
)

# INS003: Concealing or waiving liability exclusions
EXCLUSION_WAIVER_RE = re.compile(
    r"(?<!\w)(?:"
    r"không\s+cần\s+(?:đọc|xem|quan\s+tâm)\s+điều\s+khoản\s+loại\s+trừ(?:\s+trách\s+nhiệm)?|"
    r"(?:bảo\s+hiểm\s+)?chi\s+trả\s+mọi\s+rủi\s+ro\s+không\s+(?:có\s+)?(?:bất\s+kỳ\s+)?(?:điều\s+khoản\s+)?loại\s+trừ(?:\s+nào)?|"
    r"cam\s+kết\s+chi\s+trả\s+100%\s+không\s+loại\s+trừ(?:\s+bất\s+kỳ\s+trường\s+hợp\s+nào)?|"
    r"chi\s+trả\s+mọi\s+rủi\s+ro\s+không\s+loại\s+trừ"
    r")(?!\w)",
    re.IGNORECASE,
)

# INS004: Translationese and non-statutory insurance terms
INSURANCE_CALQUES_RE = re.compile(
    r"(?<!\w)(?:"
    r"chính\s+sách\s+bảo\s+hiểm(?:\s+nhân\s+thọ)?|"
    r"người\s+giữ\s+chính\s+sách|"
    r"câu\s+chuyện\s+bảo\s+hiểm|"
    r"sự\s+kiện\s+thiên\s+chúa|"
    r"tiền\s+thưởng\s+bảo\s+hiểm(?:\s+hàng\s+năm)?|"
    r"phí\s+bảo\s+hiểm\s+thưởng"
    r")(?!\w)",
    re.IGNORECASE,
)

# INS005: Unlawful claim settlement timeline exceeding statutory limits
EXCESSIVE_CLAIM_TIMELINE_RE = re.compile(
    r"(?<!\w)(?:"
    r"(?:thời\s+hạn\s+)?(?:giải\s+quyết\s+bồi\s+thường|chi\s+trả\s+quyền\s+lợi(?:\s+bảo\s+hiểm)?|bồi\s+thường)\s+(?:là\s+|trong\s+vòng\s+|lên\s+đến\s+)(?:[3-9]\d|\d{3,})\s+ngày(?:\s+làm\s+việc)?|"
    r"(?:giải\s+quyết\s+bồi\s+thường|chi\s+trả\s+quyền\s+lợi(?:\s+bảo\s+hiểm)?)\s+trong\s+vòng\s+(?:45|60|90)\s+ngày(?:\s+làm\s+việc)?|"
    r"thời\s+hạn\s+(?:giải\s+quyết\s+bồi\s+thường|chi\s+trả\s+quyền\s+lợi(?:\s+bảo\s+hiểm)?)\s+là\s+(?:45|60|90)\s+ngày(?:\s+làm\s+việc)?"
    r")(?!\w)",
    re.IGNORECASE,
)

# INS006: Coercive Bancassurance tying
BANCASSURANCE_COERCION_RE = re.compile(
    r"(?<!\w)(?:"
    r"bắt\s+buộc\s+(?:phải\s+)?mua\s+bảo\s+hiểm(?:\s+nhân\s+thọ)?\s+(?:mới\s+được|để\s+được)\s+giải\s+ngân|"
    r"từ\s+chối\s+phê\s+duyệt\s+hồ\s+sơ\s+vay(?:\s+vốn)?\s+nếu\s+(?:khách\s+hàng\s+)?không\s+tham\s+gia(?:\s+gói)?\s+bảo\s+hiểm(?:\s+liên\s+kết\s+đầu\s+tư)?|"
    r"điều\s+kiện\s+bắt\s+buộc\s+để\s+giải\s+ngân\s+là\s+phải\s+mua\s+bảo\s+hiểm|"
    r"ép\s+buộc\s+mua\s+bảo\s+hiểm(?:\s+nhân\s+thọ)?\s+để\s+được\s+vay|"
    r"không\s+mua\s+bảo\s+hiểm\s+thì\s+không\s+được\s+giải\s+ngân"
    r")(?!\w)",
    re.IGNORECASE,
)

# Structural markers
FREE_LOOK_21_DAYS_RE = re.compile(
    r"(?<!\w)(?:thời\s+gian\s+cân\s+nhắc(?:\s+tham\s+gia\s+bảo\s+hiểm)?\s+(?:là\s+)?21\s+ngày|21\s+ngày\s+cân\s+nhắc)(?!\w)",
    re.IGNORECASE,
)
EXCLUSION_SECTION_RE = re.compile(
    r"(?<!\w)(?:loại\s+trừ\s+trách\s+nhiệm(?:\s+bảo\s+hiểm)?|điều\s+khoản\s+loại\s+trừ|các\s+trường\s+hợp\s+loại\s+trừ)(?!\w)",
    re.IGNORECASE,
)


def _is_comment_or_blank(line: str) -> bool:
    stripped = line.strip()
    return not stripped or stripped.startswith(("#", "<!--", "//"))


def _is_negated(text: str, start: int) -> bool:
    prefix = text[max(0, start - 60):start].lower()
    return any(neg in prefix for neg in (
        "nghiêm cấm", "không được phép", "cấm", "không bắt buộc", "bãi bỏ", "không được ép", "xử phạt hành vi",
    ))


def check_line(ctx, lineno: int, raw: str, masked: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    if _is_comment_or_blank(raw):
        return

    # INS001: Disguising investment-linked insurance as fixed-rate bank savings
    for match in SAVINGS_DISGUISE_RE.finditer(masked):
        if _is_negated(masked, match.start()):
            continue
        yield (
            "INS001",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"misrepresenting investment-linked insurance as guaranteed bank savings “{match.group(0)}”",
            "under Law on Insurance Business 2022 and Circular 67/2023/TT-BTC, investment-linked insurance must never be promoted as fixed-rate savings deposits; include investment risk disclaimers and fluctuating yield scenarios",
        )

    # INS002: Truncated or waived free-look period
    for match in FREE_LOOK_MISSTATED_RE.finditer(masked):
        yield (
            "INS002",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"misstated or shortened free-look period “{match.group(0)}”",
            "Article 35 Law on Insurance Business 2022 mandates a 21-day free-look period ('thời gian cân nhắc tham gia bảo hiểm 21 ngày') for life insurance contracts with terms exceeding 1 year",
        )

    # INS003: Waiving or concealing liability exclusion clauses
    for match in EXCLUSION_WAIVER_RE.finditer(masked):
        yield (
            "INS003",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"unlawful waiver or concealment of liability exclusions “{match.group(0)}”",
            "Article 19 Law on Insurance Business 2022 mandates explicit disclosure and explanation of liability exclusion clauses ('điều khoản loại trừ trách nhiệm bảo hiểm') to prevent invalidity",
        )

    # INS004: Translationese and machine-translated insurance calques
    for match in INSURANCE_CALQUES_RE.finditer(masked):
        yield (
            "INS004",
            WARN,
            match.start() + 1,
            match.group(0),
            f"machine-translated insurance terminology “{match.group(0)}”",
            "use statutory Vietnamese insurance terms under Article 4 Law on Insurance Business 2022: 'hợp đồng bảo hiểm' (not chính sách), 'bên mua bảo hiểm' (not người giữ chính sách), 'phí bảo hiểm' (not tiền thưởng bảo hiểm)",
        )

    # INS005: Unlawful claim settlement timeline exceeding statutory limits
    for match in EXCESSIVE_CLAIM_TIMELINE_RE.finditer(masked):
        yield (
            "INS005",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"excessive claim settlement timeline “{match.group(0)}” exceeding statutory limits",
            "under Article 31 Law on Insurance Business 2022, claim payouts must be made within 15 days of receiving complete valid dossier (or maximum 30 days if verification is required)",
        )

    # INS006: Bancassurance coercive tying
    for match in BANCASSURANCE_COERCION_RE.finditer(masked):
        if _is_negated(masked, match.start()):
            continue
        yield (
            "INS006",
            ERROR,
            match.start() + 1,
            match.group(0),
            f"coercive bancassurance tying “{match.group(0)}”",
            "Circular 67/2023/TT-BTC and Law on Credit Institutions 2024 strictly prohibit coercing borrowers into buying life insurance as a mandatory condition for loan disbursement",
        )


def check_document(ctx) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    doctype = ctx.doctype
    body = "\n".join(ctx.masked)
    if not body.strip():
        return

    first_line = next((i for i, raw in enumerate(ctx.lines, 1) if not _is_comment_or_blank(raw)), 1)

    # INS002: Missing 21-day free-look in policy-illustration
    if doctype == "policy-illustration":
        if not FREE_LOOK_21_DAYS_RE.search(body):
            yield (
                "INS002",
                ERROR,
                first_line,
                1,
                "",
                "policy-illustration missing mandatory 21-day free-look period notice ('thời gian cân nhắc tham gia bảo hiểm 21 ngày')",
                "life insurance sales illustrations under Article 35 Law on Insurance Business 2022 must explicitly advise customers of the 21-day free-look period",
            )

    # INS003: Missing exclusion clause in insurance-certificate
    if doctype == "insurance-certificate":
        if not EXCLUSION_SECTION_RE.search(body):
            yield (
                "INS003",
                ERROR,
                first_line,
                1,
                "",
                "insurance-certificate missing mandatory liability exclusion clause section ('loại trừ trách nhiệm bảo hiểm')",
                "insurance certificates and policy summaries under Article 19 Law on Insurance Business 2022 must explicitly state liability exclusion clauses",
            )
