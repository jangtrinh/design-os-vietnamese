# -*- coding: utf-8 -*-
"""Business communications domain rules for Vietnamese copy validation.

Covers Zalo OA (ZNS/ZBS), marketplace listings, B2B sales outreach,
commercial quotations (báo giá), dunning sequences, administrative
correspondence (công văn), bulk messaging, and influencer advertising disclosures.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Dict, Iterator, List, Optional, Sequence, Tuple

ERROR = "error"
WARN = "warning"

DOCTYPES: Dict[str, str] = {
    "zns": "Zalo Notification Service message (transactional or customer service, 400-char NFC limit)",
    "zns-transactional": "Strict transactional Zalo ZNS template (zero promotional copy, 400-char NFC limit)",
    "marketplace-title": "Shopee, Lazada, TikTok Shop product title (no ALL-CAPS spam, no spam emoji)",
    "cold-outreach": "B2B outbound sales email or message (courteous salutation, professional tone)",
    "bao-gia": "B2B sales quotation / commercial proposal (requires VAT treatment and validity date)",
    "dunning": "Accounts receivable / payment reminder sequence (escalating formal tone)",
    "bulk-message": "Bulk marketing SMS, email, or ZBS broadcast (requires statutory opt-out per NĐ 91/2020)",
    "promo": "Promotional campaign copy or flash sale (statutory discount ceiling <= 50% per NĐ 81/2018)",
    "influencer-post": "KOL/KOC sponsored social post (mandatory disclosure per Luật 75/2025/QH15)",
    "cong-van": "Official administrative document / dispatch (statutory layout per Nghị định 30/2020/NĐ-CP)",
}

RULE_DOCS: Dict[str, str] = {
    "ZNS001": "marketing/promotional wording inside a transactional Zalo ZNS template",
    "ZNS002": "Zalo ZNS/ZBS body exceeds the 400-character NFC limit",
    "MKT001": "ALL-CAPS word (4+ letters, excluding whitelisted brand acronyms like HDMI/USB/OLED/WIFI/UNIQ/APPLE/SONY/ANKER/SAMSUNG) or spam emoji in a marketplace listing title",
    "MKT002": "promotional discount > 50% without a <!-- khuyen-mai-tap-trung: ... --> annotation (NĐ 81/2018 & NĐ 128/2024)",
    "MKT003": "sponsored KOL/KOC post missing explicit sponsorship disclosure ('#QuảngCáo', '#Ad', 'Tài trợ bởi', 'Hợp tác cùng' — Luật 75/2025/QH15)",
    "SALES001": "casual pronoun ('bạn', 'mình', 'bọn mình', 'cậu') in B2B outreach, quotation, dunning, or công văn",
    "SALES003": "cold outreach missing a courteous opening salutation ('Kính gửi', 'Kính chào', 'Chào anh/chị')",
    "SALES004": "quotation (báo giá) missing VAT treatment ('thuế GTGT' / 'VAT') or validity date ('hiệu lực' / 'có giá trị đến')",
    "SPAM001": "bulk marketing message missing an explicit opt-out mechanism (NĐ 91/2020 Điều 13)",
    "ADMIN001": "official administrative document (công văn) missing statutory Quốc hiệu ('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM') or Tiêu ngữ ('Độc lập - Tự do - Hạnh phúc') per Nghị định 30/2020/NĐ-CP",
}

# --------------------------------------------------------------------------- #
# Regex Patterns
# --------------------------------------------------------------------------- #

# ZNS Transactional Promotional Keywords (Zalo strictly bans promotional words in transactional templates)
ZNS_PROMO_KEYWORDS_RE = re.compile(
    r"(?i)\b(?:"
    r"giảm\s+(?:giá|sâu|ngay|sốc)|"
    r"khuyến\s+m[aạ]i|khuyến\s+mãi|"
    r"ưu\s+đãi|"
    r"chiết\s+khấu|"
    r"voucher|"
    r"săn\s+deal|deal\s+hời|"
    r"quà\s+tặng|"
    r"flash\s*sale|"
    r"giá\s+sốc|"
    r"mua\s+ngay|đặt\s+mua\s+ngay"
    r")\b"
)

# Marketplace spam emoji (Shopee, Lazada, TikTok Shop strictly penalize emoji in listing titles)
SPAM_EMOJI_RE = re.compile(
    r"[\U0001F300-\U0001FAFF"  # Miscellaneous Symbols, Pictographs, Supplemental Symbols
    r"\u2600-\u26FF"          # Misc Symbols (⚡, ⚠️, etc.)
    r"\u2700-\u27BF"          # Dingbats (✨, ❌, etc.)
    r"]"
)

# Marketplace ALL-CAPS words (4+ letters, Vietnamese & ASCII)
ALL_CAPS_WORD_RE = re.compile(
    r"\b([A-ZÀÁẢÃẠĂẮẰẲẴẶÂẤẦẨẪẬĐÈÉẺẼẸÊẾỀỂỄỆÌÍỈĨỊÒÓỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÙÚỦŨỤƯỨỪỬỮỰỲÝỶỸỴ]{4,})\b"
)

# Whitelisted uppercase technical abbreviations and global brands permitted in marketplace titles
WHITELISTED_ACRONYMS = frozenset({
    "HDMI", "USB", "OLED", "WIFI", "UNIQ", "APPLE", "SONY", "ANKER", "SAMSUNG",
    "TYPE-C", "BLUETOOTH", "RAM", "ROM", "SSD", "HDD", "NVME", "BASEUS", "UGREEN",
    "LOGITECH", "XIAOMI", "ASUS", "DELL", "LENOVO", "INTEL", "RYZEN", "NVIDIA",
    "PD", "QC", "RGB", "DPI", "VESA", "ANSI", "ISO", "IP68", "IP67", "GPS",
})

# Promotional discount > 50%
DISCOUNT_OVER_50_RE = re.compile(
    r"(?i)(?:"
    r"(?:giảm|sale|ưu\s+đãi|chiết\s+khấu|off)\s*(?:giá|sốc|ngay|tới|lên\s+đến|lên\s+tới)?\s*([5-9][1-9]|[6-9]\d|100)\s*%|"
    r"([5-9][1-9]|[6-9]\d|100)\s*%\s*(?:giảm|off|chiết\s+khấu)"
    r")"
)

KHUYEN_MAI_TAP_TRUNG_RE = re.compile(
    r"khuyen-mai-tap-trung\s*:",
    re.IGNORECASE,
)

# KOL / KOC Sponsorship disclosure tokens (Luật 75/2025/QH15)
INFLUENCER_DISCLOSURE_RE = re.compile(
    r"(?i)(?:"
    r"#quảngcáo|#quangcao|#ad|#sponsored|#commercial|"
    r"tài\s+trợ\s+bởi|hợp\s+tác\s+cùng|hợp\s+tác\s+với|nội\s+dung\s+được\s+tài\s+trợ|"
    r"quảng\s+cáo\s+bởi|sản\s+phẩm\s+do\s+.*?\s+tài\s+trợ"
    r")"
)

# Casual pronouns forbidden in B2B / Administrative contexts
CASUAL_B2B_PRONOUNS_RE = re.compile(
    r"(?i)\b(bạn|mình|bọn\s+mình|cậu|chúng\s+mình)\b"
)

# Non-pronoun compounds containing "bạn" that are valid vocabulary
PRONOUN_COMPOUND_EXEMPT_RE = re.compile(
    r"(?<!\w)(?:"
    r"bạn\s+(?:bè|đọc|hàng|đời|học|đồng\s+hành|hữu|nhỏ|trai|gái|diễn|tình|thân|đường)|"
    r"(?:kết|tình|nhóm|hội|cùng)\s+bạn"
    r")(?!\w)",
    re.IGNORECASE,
)

# Cold outreach opening salutations
COURTEOUS_SALUTATION_RE = re.compile(
    r"(?i)\b(?:"
    r"kính\s+gửi|"
    r"kính\s+chào|"
    r"chào\s+(?:anh/chị|anh|chị|quý\s+anh/chị|quý\s+khách|quý\s+đối\s+tác|ông|bà)|"
    r"thưa\s+(?:anh/chị|quý\s+khách|ông|bà)"
    r")\b"
)

# Báo giá VAT treatment
BAO_GIA_VAT_RE = re.compile(
    r"(?i)\b(?:"
    r"thuế\s+gtgt|thuế\s+giá\s+trị\s+gia\s+tăng|vat|"
    r"(?:đã|chưa)\s+(?:bao\s+)?gồm\s+(?:thuế\s+gtgt|vat)"
    r")\b"
)

# Báo giá validity period
BAO_GIA_VALIDITY_RE = re.compile(
    r"(?i)\b(?:"
    r"hiệu\s+lực|"
    r"có\s+giá\s+trị\s+(?:đến|trong)|"
    r"thời\s+hạn\s+hiệu\s+lực|"
    r"ngày\s+hết\s+hạn|"
    r"báo\s+giá\s+có\s+giá\s+trị"
    r")\b"
)

# Anti-Spam statutory opt-out mechanism (Nghị định 91/2020 Điều 13)
OPT_OUT_RE = re.compile(
    r"(?i)\b(?:"
    r"từ\s+chối|"
    r"hủy\s+nhận\s+tin|"
    r"soạn\s+tc|"
    r"opt-out|"
    r"unsubscribe|"
    r"dừng\s+nhận\s+tin|"
    r"ngừng\s+nhận\s+tin|"
    r"hủy\s+đăng\s+ký"
    r")\b"
)

# Công văn statutory Quốc hiệu & Tiêu ngữ (Nghị định 30/2020/NĐ-CP)
QUOC_HIEU_RE = re.compile(
    r"CỘNG\s+HÒA\s+XÃ\s+HỘI\s+CHỦ\s+NGHĨA\s+VIỆT\s+NAM",
    re.IGNORECASE,
)
TIEU_NGU_RE = re.compile(
    r"Độc\s+lập\s*[-–—]\s*Tự\s+do\s*[-–—]\s*Hạnh\s+phúc",
    re.IGNORECASE,
)


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


# --------------------------------------------------------------------------- #
# Line-Level Checker
# --------------------------------------------------------------------------- #
def check_line(ctx: Any, lineno: int, raw_line: str, line: str) -> Iterator[Tuple[str, str, int, str, str, str]]:
    """Inspect a single line of copy against business communications rules.

    Yields (rule, severity, col, snippet, message, hint).
    """
    doctype = ctx.doctype or ""
    register = ctx.register or ""

    # 1. ZNS001: Promotional wording inside transactional Zalo ZNS
    if doctype == "zns-transactional":
        for m in ZNS_PROMO_KEYWORDS_RE.finditer(line):
            yield (
                "ZNS001",
                ERROR,
                m.start() + 1,
                m.group(0),
                f"promotional wording “{m.group(0)}” forbidden in transactional Zalo ZNS template",
                "transactional ZNS must contain only order, payment, or account updates; promotional copy belongs in ZBS",
            )

    # 2. MKT001: ALL-CAPS words or spam emoji in marketplace listing titles
    if doctype == "marketplace-title":
        # Check spam emoji
        for m in SPAM_EMOJI_RE.finditer(raw_line):
            yield (
                "MKT001",
                ERROR,
                m.start() + 1,
                m.group(0),
                f"spam emoji “{m.group(0)}” forbidden in marketplace listing title",
                "remove emojis from product title to comply with Shopee, Lazada, and TikTok Shop listing algorithms",
            )
        # Check ALL-CAPS words (4+ letters)
        for m in ALL_CAPS_WORD_RE.finditer(raw_line):
            word = m.group(1)
            if word not in WHITELISTED_ACRONYMS:
                yield (
                    "MKT001",
                    ERROR,
                    m.start() + 1,
                    word,
                    f"ALL-CAPS word “{word}” violates marketplace title casing policy",
                    "use Title Case or standard brand casing; only technical standards (HDMI, USB, OLED) and whitelisted brand acronyms may be ALL-CAPS",
                )

    # 3. MKT002: Promotional discount > 50% without centralized promotion annotation
    has_tap_trung = bool(KHUYEN_MAI_TAP_TRUNG_RE.search(ctx.text))
    if not has_tap_trung:
        for m in DISCOUNT_OVER_50_RE.finditer(line):
            yield (
                "MKT002",
                ERROR,
                m.start() + 1,
                m.group(0),
                f"promotional discount “{m.group(0)}” exceeds statutory 50% ceiling without concentrated promotion annotation",
                "attach <!-- khuyen-mai-tap-trung: [Quyết định số/Chương trình] --> per NĐ 81/2018 & NĐ 128/2024, or cap discount at 50%",
            )

    # 4. SALES001: Casual pronoun in B2B outreach, quotation, dunning, or công văn
    if doctype in ("cold-outreach", "bao-gia", "dunning", "cong-van") or register in ("b2b", "gov-admin"):
        # Find non-pronoun compound spans to exempt
        exempt_spans = [
            (m.start(), m.end())
            for m in PRONOUN_COMPOUND_EXEMPT_RE.finditer(line)
        ]
        for m in CASUAL_B2B_PRONOUNS_RE.finditer(line):
            start, end = m.start(), m.end()
            if any(s <= start and end <= e for s, e in exempt_spans):
                continue
            matched = m.group(0)
            yield (
                "SALES001",
                ERROR,
                start + 1,
                matched,
                f"casual pronoun “{matched}” forbidden in B2B commercial/administrative communications",
                "use professional kinship address 'anh/chị' (B2B) or formal institutional address (công văn)",
            )


# --------------------------------------------------------------------------- #
# Document-Level Checker
# --------------------------------------------------------------------------- #
def check_document(ctx: Any) -> Iterator[Tuple[str, str, int, int, str, str, str]]:
    """Inspect whole document for structural and compliance constraints.

    Yields (rule, severity, lineno, col, snippet, message, hint).
    """
    doctype = ctx.doctype or ""
    register = ctx.register or ""
    text = ctx.text

    # 1. ZNS002: Zalo ZNS/ZBS 400-character NFC limit
    if doctype in ("zns", "zns-transactional"):
        # Strip comments such as <!-- ... --> for actual payload character calculation
        body_text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL).strip()
        nfc_len = len(unicodedata.normalize("NFC", body_text))
        if nfc_len > 400:
            yield (
                "ZNS002",
                ERROR,
                1,
                1,
                body_text[:40].replace("\n", " "),
                f"Zalo ZNS template body ({nfc_len} NFC characters) exceeds 400-character ceiling",
                "condense parameters and body text to strictly stay within the 400 NFC character quota",
            )

    # 2. MKT003: Sponsored KOL/KOC post missing explicit sponsorship disclosure
    if doctype == "influencer-post":
        if not INFLUENCER_DISCLOSURE_RE.search(text):
            first_line = ctx.lines[0] if ctx.lines else text[:40]
            yield (
                "MKT003",
                ERROR,
                1,
                1,
                first_line[:40].strip(),
                "sponsored KOL/KOC post missing explicit sponsorship disclosure",
                "add '#QuảngCáo', '#Ad', 'Tài trợ bởi [Thương hiệu]', or 'Hợp tác cùng [Thương hiệu]' per Luật 75/2025/QH15",
            )

    # 3. SALES003: Cold outreach missing courteous opening salutation
    if doctype == "cold-outreach":
        if not COURTEOUS_SALUTATION_RE.search(text):
            first_line = ctx.lines[0] if ctx.lines else text[:40]
            yield (
                "SALES003",
                ERROR,
                1,
                1,
                first_line[:40].strip(),
                "cold outreach missing courteous opening salutation",
                "open cold outreach with 'Kính gửi [Tên/Quý Doanh nghiệp]', 'Kính chào Anh/Chị', or 'Chào Anh/Chị [Tên]'",
            )

    # 4. SALES004: Quotation (báo giá) missing VAT treatment or validity date
    if doctype == "bao-gia":
        has_vat = bool(BAO_GIA_VAT_RE.search(text))
        has_validity = bool(BAO_GIA_VALIDITY_RE.search(text))
        if not (has_vat and has_validity):
            missing: List[str] = []
            if not has_vat:
                missing.append("VAT treatment ('thuế GTGT' / 'VAT')")
            if not has_validity:
                missing.append("validity date ('hiệu lực' / 'có giá trị đến')")
            first_line = ctx.lines[0] if ctx.lines else text[:40]
            yield (
                "SALES004",
                ERROR,
                1,
                1,
                first_line[:40].strip(),
                f"quotation (báo giá) missing commercial terms: {', '.join(missing)}",
                "B2B quotations must explicitly state VAT treatment ('Đã bao gồm VAT' / 'Chưa bao gồm thuế GTGT') and quotation validity period",
            )

    # 5. SPAM001: Bulk marketing message missing statutory opt-out mechanism
    if doctype == "bulk-message":
        if not OPT_OUT_RE.search(text):
            first_line = ctx.lines[0] if ctx.lines else text[:40]
            yield (
                "SPAM001",
                ERROR,
                1,
                1,
                first_line[:40].strip(),
                "bulk marketing message missing statutory opt-out instruction",
                "include an explicit refusal instruction (e.g., 'Soạn TC gửi 1324' or 'Nhấp vào đây để hủy nhận tin') per NĐ 91/2020 Điều 13",
            )

    # 6. ADMIN001: Official administrative document missing Quốc hiệu or Tiêu ngữ
    if doctype == "cong-van" or register == "gov-admin":
        has_quoc_hieu = bool(QUOC_HIEU_RE.search(text))
        has_tieu_ngu = bool(TIEU_NGU_RE.search(text))
        if not (has_quoc_hieu and has_tieu_ngu):
            missing_admin: List[str] = []
            if not has_quoc_hieu:
                missing_admin.append("Quốc hiệu ('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM')")
            if not has_tieu_ngu:
                missing_admin.append("Tiêu ngữ ('Độc lập - Tự do - Hạnh phúc')")
            first_line = ctx.lines[0] if ctx.lines else text[:40]
            yield (
                "ADMIN001",
                ERROR,
                1,
                1,
                first_line[:40].strip(),
                f"official administrative document missing statutory header: {', '.join(missing_admin)}",
                "add statutory Quốc hiệu ('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM') and Tiêu ngữ ('Độc lập - Tự do - Hạnh phúc') per Nghị định 30/2020/NĐ-CP",
            )
