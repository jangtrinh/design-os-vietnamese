#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DESIGN:OS Vietnamese UI/UX & Design System Rules Plugin.

Pure Python 3.9+ standard library. Zero external pip dependencies.
Loaded by validate_copy.py to enforce:
  - UX001: Component character caps (button <= 24, tab <= 18, badge <= 16, toast <= 90)
  - UX002: Pronouns ('bạn', 'tôi', 'chúng tôi') or 'vui lòng' padding in compact labels
  - UX003: Raw empty-state placeholders without actionable recovery/creation CTA
  - UX004: Dead-end error states without actionable recovery steps
  - UX005: Destructive confirmation modal with vague button or omitted permanent consequence
  - UX006: CSS line-height < 1.18 on heading or < 1.35 on body clipping diacritics
  - UX007: next/font/google declaration specifying subsets: ['latin'] without 'vietnamese'
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any, Dict, List, Optional, Sequence, Tuple

ERROR = "error"
WARN = "warning"

RULE_DOCS: Dict[str, str] = {
    "UX001": "UI control copy exceeds component character cap (button <= 24, tab <= 18, badge <= 16, toast <= 90)",
    "UX002": "pronoun ('bạn', 'tôi', 'chúng tôi') or 'vui lòng' padding inside a compact button/tab/badge label",
    "UX003": "raw empty-state placeholder ('Trạng thái trống', 'Không có dữ liệu', 'Trống') without an actionable recovery or creation CTA",
    "UX004": "dead-end error state ('Đã xảy ra lỗi', 'Lỗi hệ thống', 'Không thành công') without an actionable recovery step (e.g., 'Thử lại', 'Kiểm tra...', 'Liên hệ...')",
    "UX005": "destructive confirmation modal uses vague 'OK' / 'Đồng ý' / 'Có' button or omits permanent consequence ('Không thể hoàn tác' / 'vĩnh viễn')",
    "UX006": "CSS line-height < 1.18 on heading or < 1.35 on body clips Vietnamese stacked diacritics (Ẫ, Ễ, Ộ, Ữ)",
    "UX007": "next/font/google declaration specifies subsets: ['latin'] without 'vietnamese'",
}

DOCTYPES: Dict[str, str] = {
    "ui-button": "Primary/secondary button or CTA label (cap <= 24)",
    "ui-tab": "Navigation tab or segmented control item (cap <= 18)",
    "ui-badge": "Status badge, tag, or pill (cap <= 16)",
    "ui-toast": "Toast or snackbar transient notification (cap <= 90)",
    "ui-empty": "Empty state screen or card with recovery CTA",
    "ui-error": "Form, screen, or network error state with recovery",
    "ui-destructive-modal": "Destructive confirmation dialog / modal",
    "css-tokens": "CSS typography rules, tokens, or style declarations",
    "nextjs-font": "Next.js Google Fonts font loader configuration",
}

CAPS: Dict[str, Tuple[str, int]] = {
    "ui-button": ("button", 24),
    "ui-tab": ("tab", 18),
    "ui-badge": ("badge", 16),
    "ui-toast": ("toast", 90),
}

UX002_RE = re.compile(
    r"(?i)(?<!\w)(bạn|tôi|chúng\s+tôi|vui\s+lòng|xin\s+vui\s+lòng|quý\s+khách|mình)(?!\w)"
)

RAW_EMPTY_RE = re.compile(
    r"(?i)(?<!\w)(trạng\s+thái\s+trống|không\s+có\s+dữ\s+liệu|chưa\s+có\s+dữ\s+liệu|danh\s+sách\s+trống|trống|chưa\s+có\s+mục\s+nào|không\s+có\s+mục\s+nào)(?!\w)"
)

EMPTY_CTA_RE = re.compile(
    r"(?i)(?<!\w)(tạo|thêm|bắt\s+đầu|khám\s+phá|tải\s+lên|nhập|thiết\s+lập|kết\s+nối|thử\s+lại|tìm\s+kiếm|xem\s+dự\s+án|create|add|upload|new|start)(?!\w)"
)

DEAD_END_ERROR_RE = re.compile(
    r"(?i)(?<!\w)(đã\s+xảy\s+ra\s+lỗi|lỗi\s+hệ\s+thống|không\s+thành\s+công|thao\s+tác\s+thất\s+bại|lỗi\s+không\s+xác\s+định|có\s+lỗi\s+xảy\s+ra|lỗi\s+mạng)(?!\w)"
)

ERROR_RECOVERY_RE = re.compile(
    r"(?i)(?<!\w)(thử\s+lại|kiểm\s+tra|liên\s+hệ|tải\s+lại|quay\s+lại|gửi\s+lại|xem\s+hướng\s+dẫn|hỗ\s+trợ|retry|reload|contact)(?!\w)"
)

VAGUE_BTN_RE = re.compile(
    r"(?i)(?<!\w)(ok|đồng\s+ý|có|xác\s+nhận|yes|tiếp\s+tục)(?!\w)"
)

CONSEQUENCE_RE = re.compile(
    r"(?i)(?<!\w)(không\s+thể\s+hoàn\s+tác|vĩnh\s+viễn|không\s+thể\s+khôi\s+phục|mất\s+hoàn\s+toàn)(?!\w)"
)

LH_RE = re.compile(
    r"(?i)(?:line-height|lineHeight|--lh-[\w-]*)\s*[:=]\s*['\"]?([0-9.]+)(px|rem|em|%)?['\"]?"
)


def _extract_text_for_cap(raw: str) -> Optional[str]:
    stripped = raw.strip()
    if not stripped:
        return None
    if stripped.startswith(("//", "/*", "*", "#", "<!--")):
        return None
    # JSON key-value: "key": "value"
    m_json = re.search(r':\s*"([^"]+)"', raw)
    if m_json:
        return m_json.group(1).strip()
    # Quoted string
    if (stripped.startswith('"') and stripped.endswith('"')) or (stripped.startswith("'") and stripped.endswith("'")):
        if len(stripped) >= 2:
            return stripped[1:-1].strip()
    return stripped


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


def check_line(ctx: Any, lineno: int, raw: str, masked: str) -> List[Tuple[str, str, int, str, str, str]]:
    findings: List[Tuple[str, str, int, str, str, str]] = []

    # UX001: Character caps
    if ctx.doctype in CAPS:
        role_label, cap = CAPS[ctx.doctype]
        target = _extract_text_for_cap(raw)
        if target:
            target_nfc = unicodedata.normalize("NFC", target)
            char_count = len(target_nfc)
            if char_count > cap:
                snippet = target[:40]
                col = raw.find(target[:10]) + 1 if target[:10] in raw else 1
                findings.append((
                    "UX001",
                    WARN,
                    max(1, col),
                    snippet,
                    f"UI control copy exceeds component character cap ({char_count} > {cap} chars)",
                    f"shorten {role_label} label to <= {cap} characters (currently {char_count})",
                ))

    # UX002: Pronouns / padding in compact controls
    if ctx.doctype in ("ui-button", "ui-tab", "ui-badge"):
        for m in UX002_RE.finditer(raw):
            findings.append((
                "UX002",
                WARN,
                m.start() + 1,
                m.group(0),
                f"pronoun or padding phrase '{m.group(0)}' inside a compact UI label",
                "remove pronoun or 'vui lòng' padding in compact UI controls (keep action verb-first)",
            ))

    # UX006: CSS line-height (single-line or direct property check)
    if ctx.doctype == "css-tokens" or (ctx.path and getattr(ctx.path, "suffix", "").lower() == ".css"):
        m_lh = LH_RE.search(raw)
        if m_lh:
            try:
                val = float(m_lh.group(1))
                unit = m_lh.group(2) or ""
                if unit == "%":
                    val = val / 100.0
                is_heading = bool(re.search(r"(?i)\b(h[1-6]|heading|display|title|hero)\b", raw))
                is_body = bool(re.search(r"(?i)\b(body|prose|text|p|paragraph)\b", raw))
                if val < 1.18:
                    findings.append((
                        "UX006",
                        WARN,
                        m_lh.start() + 1,
                        m_lh.group(0),
                        f"CSS line-height {val} < 1.18 clips Vietnamese stacked diacritics (Ẫ, Ễ, Ộ, Ữ)",
                        "use line-height >= 1.18 for headings or >= 1.35 for body prose",
                    ))
                elif is_body and val < 1.35:
                    findings.append((
                        "UX006",
                        WARN,
                        m_lh.start() + 1,
                        m_lh.group(0),
                        f"CSS line-height {val} < 1.35 on body prose clips Vietnamese diacritics",
                        "use line-height >= 1.35 (recommended 1.5–1.6) for Vietnamese body prose",
                    ))
            except ValueError:
                pass

    return findings


def check_document(ctx: Any) -> List[Tuple[str, str, int, int, str, str, str]]:
    findings: List[Tuple[str, str, int, int, str, str, str]] = []

    # UX003: Empty states
    if ctx.doctype == "ui-empty":
        m_empty = RAW_EMPTY_RE.search(ctx.text)
        has_cta = bool(EMPTY_CTA_RE.search(ctx.text))
        if m_empty and not has_cta:
            abs_pos = m_empty.start()
            lineno = ctx.text[:abs_pos].count("\n") + 1
            line_start = ctx.text.rfind("\n", 0, abs_pos) + 1
            col = abs_pos - line_start + 1
            findings.append((
                "UX003",
                WARN,
                lineno,
                col,
                m_empty.group(0),
                "raw empty-state placeholder without an actionable recovery or creation CTA",
                "explain why the state is empty and provide a clear recovery or creation CTA (e.g. 'Tạo dự án mới')",
            ))

    # UX004: Error states
    if ctx.doctype == "ui-error":
        m_err = DEAD_END_ERROR_RE.search(ctx.text)
        has_recovery = bool(ERROR_RECOVERY_RE.search(ctx.text))
        if m_err and not has_recovery:
            abs_pos = m_err.start()
            lineno = ctx.text[:abs_pos].count("\n") + 1
            line_start = ctx.text.rfind("\n", 0, abs_pos) + 1
            col = abs_pos - line_start + 1
            findings.append((
                "UX004",
                WARN,
                lineno,
                col,
                m_err.group(0),
                "dead-end error state without an actionable recovery step",
                "explain what went wrong and provide an actionable recovery step (e.g., 'Kiểm tra mạng và thử lại')",
            ))

    # UX005: Destructive confirmation modal
    if ctx.doctype == "ui-destructive-modal":
        m_vague = VAGUE_BTN_RE.search(ctx.text)
        has_consequence = bool(CONSEQUENCE_RE.search(ctx.text))
        if m_vague:
            abs_pos = m_vague.start()
            lineno = ctx.text[:abs_pos].count("\n") + 1
            line_start = ctx.text.rfind("\n", 0, abs_pos) + 1
            col = abs_pos - line_start + 1
            findings.append((
                "UX005",
                WARN,
                lineno,
                col,
                m_vague.group(0),
                "destructive confirmation modal uses vague button copy or omits permanent consequence",
                "use specific verb-first action button (e.g. 'Xóa vĩnh viễn') and explicitly state 'Không thể hoàn tác'",
            ))
        elif not has_consequence:
            findings.append((
                "UX005",
                WARN,
                1,
                1,
                ctx.lines[0][:40] if ctx.lines else "",
                "destructive confirmation modal omits permanent consequence warning",
                "explicitly state permanent consequences (e.g. 'Hành động này không thể hoàn tác' / 'bị xóa vĩnh viễn')",
            ))

    # UX006: CSS line-height block check across multiple lines
    if ctx.doctype == "css-tokens" or (ctx.path and getattr(ctx.path, "suffix", "").lower() == ".css"):
        # Multi-line selector tracking
        current_selector = ""
        for i, line in enumerate(ctx.lines, 1):
            if "{" in line:
                current_selector = line.split("{")[0].strip()
            m_lh = LH_RE.search(line)
            if m_lh:
                try:
                    val = float(m_lh.group(1))
                    unit = m_lh.group(2) or ""
                    if unit == "%":
                        val = val / 100.0
                    is_body = bool(re.search(r"(?i)\b(body|prose|text|p|paragraph)\b", current_selector or line))
                    if 1.18 <= val < 1.35 and is_body:
                        # Check if already emitted by check_line
                        if not bool(re.search(r"(?i)\b(body|prose|text|p|paragraph)\b", line)):
                            findings.append((
                                "UX006",
                                WARN,
                                i,
                                m_lh.start() + 1,
                                m_lh.group(0),
                                f"CSS line-height {val} < 1.35 on body prose clips Vietnamese diacritics",
                                "use line-height >= 1.35 (recommended 1.5–1.6) for Vietnamese body prose",
                            ))
                except ValueError:
                    pass
            if "}" in line:
                current_selector = ""

    # UX007: Next.js Google Fonts subsets
    if ctx.doctype == "nextjs-font" or "next/font" in ctx.text:
        m_subset = re.search(r"subsets:\s*\[([^\]]*)\]", ctx.text)
        if m_subset:
            subsets_str = m_subset.group(1)
            has_latin = "'latin'" in subsets_str or '"latin"' in subsets_str
            has_vietnamese = "'vietnamese'" in subsets_str or '"vietnamese"' in subsets_str
            if has_latin and not has_vietnamese:
                abs_pos = m_subset.start()
                lineno = ctx.text[:abs_pos].count("\n") + 1
                line_start = ctx.text.rfind("\n", 0, abs_pos) + 1
                col = abs_pos - line_start + 1
                findings.append((
                    "UX007",
                    ERROR,
                    lineno,
                    col,
                    m_subset.group(0),
                    "next/font/google declaration specifies subsets: ['latin'] without 'vietnamese'",
                    "add 'vietnamese' to subsets: ['latin', 'vietnamese'] to ensure full diacritic coverage",
                ))

    return findings
