#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DESIGN:OS Vietnamese Copy, Typography, & Compliance Validator (vi-VN).

Pure Python 3.9+ standard library. Zero external pip dependencies.

Usage:
    python3 validate_copy.py copy.md
    python3 validate_copy.py src/messages/ --register ux-microcopy --strict
    python3 validate_copy.py copy.md --doctype commit
    python3 validate_copy.py copy.md --json
    python3 validate_copy.py copy.md --fix             # repairs NFC violations in place
    python3 validate_copy.py copy.md --fix-tone new    # normalizes oa/oe/uy to kiểu mới (or old)

Exit codes:
    0 = clean (or warnings only without --strict)
    1 = errors present (or any warning when --strict is set)
    2 = invalid CLI arguments or missing target files
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys
import unicodedata
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

ERROR = "error"
WARN = "warning"

EXCLUDED_DIRS = frozenset({
    ".git", ".hg", ".svn", "node_modules", ".next", ".nuxt", "dist", "build", "out",
    "target", "vendor", ".venv", "venv", "__pycache__", ".cache", ".turbo", ".yarn",
    "coverage", ".pytest_cache", ".mypy_cache", ".tox", "_evidence",
})

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
REF_DIR = SKILL_DIR / "references"

DEFAULT_EXTENSIONS = (
    ".md", ".mdx", ".markdown", ".txt", ".json", ".html", ".htm",
    ".yaml", ".yml", ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte", ".css",
)

DEFAULT_REGISTERS: Dict[str, dict] = {
    "ux-microcopy":    {"expects": "bạn",           "forbids": ("quý khách", "quý vị", "mày", "cậu")},
    "saas":            {"expects": "bạn",           "forbids": ("quý khách", "quý vị")},
    "re":              {"expects": "quý khách",     "forbids": ("bạn", "mình", "cả nhà")},
    "formal":          {"expects": "quý vị",        "forbids": ("bạn", "mình", "cả nhà")},
    "consult":         {"expects": "anh/chị",       "forbids": ("bạn", "quý vị")},
    "b2b":             {"expects": "anh/chị",       "forbids": ("bạn", "quý vị", "cả nhà")},
    "zns":             {"expects": "quý khách",     "forbids": ("bạn", "mình", "cả nhà")},
    "press":           {"expects": "quý vị",        "forbids": ("bạn", "mình", "bọn mình", "cả nhà")},
    "livestream":      {"expects": "cả nhà",        "forbids": ("quý vị", "quý khách")},
    "eng-impersonal":  {"expects": "",              "forbids": ("bạn", "quý khách", "quý vị", "anh/chị", "em", "con")},
    "eng-readme":      {"expects": "bạn",           "forbids": ("quý khách", "quý vị")},
    "finance-formal":  {"expects": "quý khách",     "forbids": ("bạn", "mình", "cả nhà")},
    "edu-k12":            {"expects": "em",            "forbids": ("bạn", "quý khách", "quý vị")},
    "edu-k12-primary":    {"expects": "con",           "forbids": ("bạn", "quý khách", "quý vị", "em")},
    "edu-preschool":      {"expects": "con",           "forbids": ("bạn", "quý khách", "quý vị", "em")},
    "edu-parent":         {"expects": "quý phụ huynh", "forbids": ("bạn", "mình", "quý khách", "em", "con")},
    "edu-uni":            {"expects": "",              "forbids": ("bạn", "con", "em", "quý khách")},
    "edu-postgrad":       {"expects": "",              "forbids": ("bạn", "con", "em", "quý khách", "mình", "cả nhà")},
    "gov-admin":          {"expects": "",              "forbids": ("bạn", "mình", "em", "con", "cả nhà")},
    "healthcare":         {"expects": "quý khách",     "forbids": ("bạn", "mình", "cả nhà")},
    "healthcare-clinical":{"expects": "",              "forbids": ("bạn", "mình", "cả nhà", "cậu", "mày")},
    "legal-contract":     {"expects": "",              "forbids": ("bạn", "mình", "cả nhà", "em", "con", "cậu")},
    "hospitality-luxury": {"expects": "quý khách",     "forbids": ("bạn", "mình", "cả nhà", "cậu", "mày")},
    "hr-candidate":       {"expects": "anh/chị",       "forbids": ("mày", "cậu", "con", "cả nhà")},
    "realestate-luxury":  {"expects": "quý khách",     "forbids": ("bạn", "mình", "cả nhà", "cậu", "mày")},
    "construction-b2b":   {"expects": "",              "forbids": ("bạn", "mình", "cả nhà", "em", "con", "cậu", "mày")},
    "ecommerce-shopper":  {"expects": "bạn",           "forbids": ("quý vị", "mày", "cậu")},
    "public-citizen":     {"expects": "ông/bà",        "forbids": ("bạn", "mình", "cả nhà", "cậu", "mày")},
    "insurance-policyholder": {"expects": "quý khách", "forbids": ("bạn", "mình", "cả nhà", "cậu", "mày")},
    "infosec-advisory":   {"expects": "",              "forbids": ("mình", "cả nhà", "cậu", "mày", "em", "con")},
    "crisis-comms":       {"expects": "quý vị",        "forbids": ("bạn", "mình", "cả nhà", "cậu", "mày")},
}

FORMAL_PRONOUNS = ("quý khách", "quý vị", "quý phụ huynh")
CASUAL_PRONOUNS = ("bạn",)

# Non-pronoun compound words containing "bạn" or "quý" that must never trigger PRO001/PRO002.
PRONOUN_COMPOUND_EXEMPT_RE = re.compile(
    r"(?<!\w)(?:"
    r"bạn\s+(?:bè|đọc|hàng|đời|học|đồng\s+hành|hữu|nhỏ|trai|gái|diễn|tình|thân|đường|cùng\s+phòng|cùng\s+lớp|tri\s+kỷ)|"
    r"(?:kết|tình|nhóm|hội|cùng|người|những\s+người|một\s+người|các\s+người)\s+bạn|"
    r"quý\s+(?:giá|hiếm|báu|trọng|mến|nhân|tộc|danh|tính|I|II|III|IV|1|2|3|4|đầu|cuối|này|trước|sau|tới|vừa\s+qua|cơ\s+quan|công\s+ty|doanh\s+nghiệp|đối\s+tác|đơn\s+vị)"
    r")(?!\w)",
    re.IGNORECASE,
)


class Finding:
    __slots__ = ("rule", "severity", "path", "line", "col", "text", "message", "hint")

    def __init__(self, rule: str, severity: str, path: pathlib.Path, line: int,
                 col: int, text: str, message: str, hint: str = ""):
        self.rule = rule
        self.severity = severity
        self.path = path
        self.line = line
        self.col = col
        self.text = text
        self.message = message
        self.hint = hint

    def as_dict(self) -> dict:
        return {
            "rule": self.rule,
            "severity": self.severity,
            "file": str(self.path),
            "line": self.line,
            "column": self.col,
            "text": self.text,
            "message": self.message,
            "hint": self.hint,
        }

    def render(self) -> str:
        tag = "error" if self.severity == ERROR else "warn "
        head = f"{self.path}:{self.line}:{self.col}: {tag} {self.rule}  {self.message}"
        if self.hint:
            head += f"\n      → {self.hint}"
        return head


# --------------------------------------------------------------------------- #
# Markdown Table Parsing
# --------------------------------------------------------------------------- #
def _table_with_header(text: str, marker: str) -> Tuple[List[str], List[List[str]]]:
    idx = text.find(marker)
    if idx == -1:
        return [], []
    rows: List[List[str]] = []
    started = False
    for raw in text[idx + len(marker):].splitlines():
        line = raw.strip()
        if not line.startswith("|"):
            if started:
                break
            continue
        started = True
        if set(line) <= set("|-: "):
            continue
        cells = [
            c.replace(r"\|", "|").strip()
            for c in re.split(r"(?<!\\)\|", line)[1:-1]
        ]
        if cells:
            rows.append(cells)
    if not rows:
        return [], []
    return [c.strip().lower() for c in rows[0]], rows[1:]


def _table_after_marker(text: str, marker: str) -> List[List[str]]:
    return _table_with_header(text, marker)[1]


def _severity_column(header: Sequence[str]) -> int:
    for i, cell in enumerate(header):
        if cell in ("severity", "mức độ"):
            return i
    return -1


def _parse_severity(cell: str) -> Optional[str]:
    value = _unwrap(cell).lower()
    if value in ("error", "lỗi"):
        return ERROR
    if value in ("warn", "warning", "cảnh báo"):
        return WARN
    return None


def _unwrap(cell: str) -> str:
    return cell.strip().strip("`").strip()


def _split_alternatives(cell: str) -> List[str]:
    return [
        _unwrap(part)
        for part in cell.split("/")
        if _unwrap(part) and _unwrap(part) != "—"
    ]


BUILTIN_CALQUES: Tuple[Tuple[str, str, str, str], ...] = (
    ("làm ơn nhập của bạn mật khẩu", "Vui lòng nhập mật khẩu của bạn", "builtin", ERROR),
    ("của bạn mật khẩu", "mật khẩu của bạn", "builtin", ERROR),
    ("của bạn tài khoản", "tài khoản của bạn", "builtin", ERROR),
    ("làm ơn nhập", "Vui lòng nhập", "builtin", ERROR),
)

DOMAIN_SKILL_MAP: Dict[str, str] = {
    "ux": "vn-design-system-ux",
    "vn-design-system-ux": "vn-design-system-ux",
    "landing": "vietnamese-landing-copy",
    "vietnamese-landing-copy": "vietnamese-landing-copy",
    "tech": "vietnamese-tech-writing",
    "vietnamese-tech-writing": "vietnamese-tech-writing",
    "biz": "vietnamese-business-comms",
    "business": "vietnamese-business-comms",
    "vietnamese-business-comms": "vietnamese-business-comms",
    "finance": "vietnamese-finance-copy",
    "vietnamese-finance-copy": "vietnamese-finance-copy",
    "edu": "vietnamese-education-copy",
    "education": "vietnamese-education-copy",
    "vietnamese-education-copy": "vietnamese-education-copy",
    "healthcare": "vietnamese-healthcare-copy",
    "medical": "vietnamese-healthcare-copy",
    "vietnamese-healthcare-copy": "vietnamese-healthcare-copy",
    "legal": "vietnamese-legal-contracts",
    "contracts": "vietnamese-legal-contracts",
    "vietnamese-legal-contracts": "vietnamese-legal-contracts",
    "hospitality": "vietnamese-hospitality-travel",
    "travel": "vietnamese-hospitality-travel",
    "vietnamese-hospitality-travel": "vietnamese-hospitality-travel",
    "hr": "vietnamese-hr-recruitment",
    "recruitment": "vietnamese-hr-recruitment",
    "vietnamese-hr-recruitment": "vietnamese-hr-recruitment",
    "realestate": "vietnamese-real-estate-construction",
    "construction": "vietnamese-real-estate-construction",
    "vietnamese-real-estate-construction": "vietnamese-real-estate-construction",
    "ecommerce": "vietnamese-ecommerce-retail",
    "retail": "vietnamese-ecommerce-retail",
    "vietnamese-ecommerce-retail": "vietnamese-ecommerce-retail",
    "gov": "vietnamese-government-public-service",
    "public-service": "vietnamese-government-public-service",
    "vietnamese-government-public-service": "vietnamese-government-public-service",
    "insurance": "vietnamese-insurance-insurtech",
    "insurtech": "vietnamese-insurance-insurtech",
    "vietnamese-insurance-insurtech": "vietnamese-insurance-insurtech",
    "cybersecurity": "vietnamese-cybersecurity-infosec",
    "infosec": "vietnamese-cybersecurity-infosec",
    "vietnamese-cybersecurity-infosec": "vietnamese-cybersecurity-infosec",
    "media": "vietnamese-media-journalism-pr",
    "journalism": "vietnamese-media-journalism-pr",
    "pr": "vietnamese-media-journalism-pr",
    "vietnamese-media-journalism-pr": "vietnamese-media-journalism-pr",
}


class Blocklists:
    """Calques, superlative patterns, and register profiles loaded from Markdown."""

    def __init__(self, ref_dir: "pathlib.Path | Sequence[pathlib.Path]" = REF_DIR):
        self.calques: List[tuple] = list(BUILTIN_CALQUES)
        self.superlatives: List[tuple] = []
        self.registers: Dict[str, dict] = dict(DEFAULT_REGISTERS)
        self.missing: List[str] = []
        ref_dirs = [ref_dir] if isinstance(ref_dir, pathlib.Path) else list(ref_dir)
        resolved_targets = {d.resolve() for d in ref_dirs if d.exists()}
        shared_loaded = False
        for candidate_shared in (
            SKILL_DIR / "references" if SKILL_DIR.name == "shared" else None,
            SKILL_DIR.parent / "shared" / "references",
            SKILL_DIR.parent.parent / "shared" / "references",
        ):
            if candidate_shared is not None and candidate_shared.is_dir():
                if candidate_shared.resolve() not in resolved_targets:
                    self._load_glossary(candidate_shared / "glossary.md")
                    self._load_banned(candidate_shared / "banned-phrases.md")
                    shared_loaded = True
                break
        for rdir in ref_dirs:
            self._load_glossary(rdir / "glossary.md", optional=shared_loaded)
            self._load_banned(rdir / "banned-phrases.md", optional=shared_loaded)
            self._load_registers(rdir / "register-matrix.md", optional=True)
        # Deduplicate calques while preserving order
        deduped_calques: List[tuple] = []
        seen_calques: set = set()
        for phrase, suggestion, source, severity in self.calques:
            key = (phrase.lower(), suggestion.lower(), severity)
            if key not in seen_calques:
                seen_calques.add(key)
                deduped_calques.append((phrase, suggestion, source, severity))
        self.calques = deduped_calques

    def _read(self, path: pathlib.Path, optional: bool = False) -> Optional[str]:
        try:
            return path.read_text(encoding="utf-8")
        except OSError:
            if not optional:
                self.missing.append(str(path))
            return None

    def _load_glossary(self, path: pathlib.Path, optional: bool = False) -> None:
        text = self._read(path, optional=optional)
        if text is None:
            return
        header, rows = _table_with_header(text, "<!-- machine-readable: glossary -->")
        sev_col = _severity_column(header)
        for row in rows:
            if len(row) < 3:
                continue
            bad, good = _unwrap(row[1]), row[2]
            alternatives = _split_alternatives(good)
            if not bad or bad == "—":
                continue
            if bad in alternatives:
                continue
            severity = _parse_severity(row[sev_col]) if 0 <= sev_col < len(row) else None
            self.calques.append((bad, " / ".join(alternatives), "glossary.md", severity))

    def _load_banned(self, path: pathlib.Path, optional: bool = False) -> None:
        text = self._read(path, optional=optional)
        if text is None:
            return
        header, rows = _table_with_header(text, "<!-- machine-readable: calques -->")
        sev_col = _severity_column(header)
        for row in rows:
            if len(row) < 2:
                continue
            bad, good = _unwrap(row[0]), _unwrap(row[1])
            severity = _parse_severity(row[sev_col]) if 0 <= sev_col < len(row) else None
            if bad and bad != "—":
                self.calques.append((bad, good, "banned-phrases.md", severity))
        for row in _table_after_marker(text, "<!-- machine-readable: superlatives -->"):
            if not row:
                continue
            pattern = _unwrap(row[0])
            note = row[2] if len(row) > 2 else ""
            try:
                self.superlatives.append((re.compile(pattern, re.IGNORECASE), note))
            except re.error as exc:
                print(
                    f"warning: bad superlative regex {pattern!r} in banned-phrases.md: {exc}",
                    file=sys.stderr,
                )

    def _load_registers(self, path: pathlib.Path, optional: bool = False) -> None:
        text = self._read(path, optional=optional)
        if text is None:
            return
        loaded = {}
        for row in _table_after_marker(text, "<!-- machine-readable: registers -->"):
            if len(row) < 3:
                continue
            name = _unwrap(row[0])
            if not name:
                continue
            forbids = tuple(
                _unwrap(part)
                for part in row[2].split(",")
                if _unwrap(part) and _unwrap(part) != "—"
            )
            loaded[name] = {"expects": _unwrap(row[1]), "forbids": forbids}
        if loaded:
            self.registers.update(loaded)

    def compiled_calques(self):
        for phrase, suggestion, source, severity in self.calques:
            body = r"[\s\u00A0]+".join(re.escape(w) for w in phrase.split())
            yield (
                re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE),
                phrase,
                suggestion,
                source,
                severity,
            )


# --------------------------------------------------------------------------- #
# Code, JSON Key & URL Masking
# --------------------------------------------------------------------------- #
FENCE_RE = re.compile(r"^\s*(```|~~~)")
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")
URL_RE = re.compile(r"(?:https?://|www\.)\S+")
JSON_KEY_RE = re.compile(r'(?:^|[{,])(\s*"(?:\\.|[^"\\])*"\s*:)')


def mask_code(lines: Sequence[str], is_markdown: bool, is_json: bool = False) -> List[str]:
    masked: List[str] = []
    in_fence = False
    for line in lines:
        if is_markdown and FENCE_RE.match(line):
            in_fence = not in_fence
            masked.append(" " * len(line))
            continue
        if in_fence:
            masked.append(" " * len(line))
            continue
        out = line
        if is_json:
            out = JSON_KEY_RE.sub(
                lambda m: m.group(0)[: m.start(1) - m.start(0)] + (" " * len(m.group(1))),
                out,
            )
        if is_markdown:
            out = INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), out)
        out = URL_RE.sub(lambda m: " " * len(m.group(0)), out)
        masked.append(out)
    return masked


# --------------------------------------------------------------------------- #
# Suppression Directives
# --------------------------------------------------------------------------- #
_END = r'[^>*"\n]*'
FILE_DISABLE_RE = re.compile(
    rf"(?:vlc|vncopy)-(?:disable|ignore):\s*({_END}?)(?:-->|\*/|\"|$)",
    re.IGNORECASE,
)
LINE_DISABLE_RE = re.compile(
    rf"(?:vlc|vncopy)-(?:disable|ignore)-line(?:\s*:?\s*({_END}?))?(?:-->|\*/|\"|$)",
    re.IGNORECASE,
)
PROOF_RE = re.compile(r"(?:<!--|//|/\*|#)\s*proof\s*:", re.IGNORECASE)
NEGATION_PREFIX_RE = re.compile(
    r"(?:không\s+phải\s+(?:là\s+)?|chưa\s+phải\s+(?:là\s+)?|đừng\s+tin\s+vào\s+|không\s+cam\s+kết\s+|"
    r"không\s+được(?:\s+phép)?\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết|dùng|sử\s+dụng)?\s*|"
    r"nghiêm\s+cấm\s+(?:quảng\s+cáo|tuyên\s+bố|cam\s+kết|dùng|sử\s+dụng)?\s*|"
    r"tránh\s+(?:viết|dùng|sử\s+dụng|quảng\s+cáo)\s+)(?:\S+\s+){0,4}$",
    re.IGNORECASE,
)
ORDINAL_SO_1_PREFIX_RE = re.compile(
    r"(?:bước|trang|điều|khoản|mục|phần|phụ\s+lục|bảng|hình|phương\s+án|kênh|cổng|lần|câu|bài|quyển|tập|"
    r"mẫu|cửa|quầy|tầng|phòng|nhóm|đội|ca|loại|cấp|mức|hạng\s+mục|giai\s+đoạn|đợt|ưu\s+tiên|nguyên\s+tắc|"
    r"quy\s+tắc|thứ\s+tự|vị\s+trí)\s+$",
    re.IGNORECASE,
)
BENIGN_DUY_NHAT_PREFIX_RE = re.compile(
    r"(?:một\s+lần|1\s+lần|mã\s+xác\s+thực|mã\s+otp|định\s+danh|khóa\s+chính|cửa\s+sổ|phiên)\s+$",
    re.IGNORECASE,
)
BENIGN_TOT_NHAT_PREFIX_RE = re.compile(
    r"(?:để\s+có\s+trải\s+nghiệm|trải\s+nghiệm|cố\s+gắng|nỗ\s+lực|chuẩn\s+bị)\s+$",
    re.IGNORECASE,
)


def _is_benign_superlative(line: str, start: int, matched: str) -> bool:
    prefix = line[max(0, start - 35):start]
    low = re.sub(r"\s+", " ", matched.strip().lower())
    if low in ("số 1", "số một") and ORDINAL_SO_1_PREFIX_RE.search(prefix):
        return True
    if low == "duy nhất" and BENIGN_DUY_NHAT_PREFIX_RE.search(prefix):
        return True
    if low == "tốt nhất" and BENIGN_TOT_NHAT_PREFIX_RE.search(prefix):
        return True
    return False


def file_disabled_rules(text: str) -> set:
    rules = set()
    for match in FILE_DISABLE_RE.finditer(text):
        tokens = [t.strip().upper() for t in re.split(r"[,\s]+", match.group(1) or "") if t.strip()]
        if not tokens:
            rules.add("ALL")
        else:
            rules.update(tokens)
    return rules


def line_disabled_rules(line: str) -> set:
    rules = set()
    for match in LINE_DISABLE_RE.finditer(line):
        tokens = [t.strip().upper() for t in re.split(r"[,\s]+", match.group(1) or "") if t.strip()]
        if not tokens:
            rules.add("ALL")
        else:
            rules.update(tokens)
    return rules


# --------------------------------------------------------------------------- #
# Universal Rule Patterns (v5.1 DESIGN:OS Engine)
# --------------------------------------------------------------------------- #
# Multi-domain high-confidence unaccented Vietnamese phrase detector (120+ phrases across UI, SaaS, Tech, Finance, Edu, Real Estate)
DIACRITIC_PHRASES = (
    # UI / UX / Auth / Controls
    "dang ky", "dang nhap", "dang xuat", "mat khau", "quen mat khau", "tai khoan",
    "cai dat", "thiet lap", "thong bao", "xac nhan", "huy bo", "luu thay doi",
    "khong the", "vui long", "he thong", "du lieu", "ung dung", "trang chu",
    "tim kiem", "tim hieu", "tim hieu them", "xem chi tiet", "xem them",
    "lien he", "ho va ten", "so dien thoai", "dia chi", "cam on", "gioi thieu",
    "san pham", "dich vu", "gio hang", "thanh toan", "mien phi", "bat dau ngay",
    "dung thu", "tai xuong", "tai len", "chia se", "sao chep", "xoa tai khoan",
    "trang thai", "ket qua", "danh sach", "cap nhat", "thanh cong", "that bai",
    # Business / E-commerce / Marketing
    "khach hang", "quy khach", "uu dai", "bao gia", "nhan bao gia", "so luong co han",
    "dat lich", "tu van", "chinh sach", "dieu khoan", "bao mat", "doi tra",
    "van chuyen", "giao hang", "don hang", "ma giam gia", "khuyen mai",
    # Real Estate & Architecture
    "can ho", "du an", "tien ich", "bat dong san", "mat bang", "phap ly",
    "chu dau tu", "tong quan", "nha mau", "tien do", "thiet ke", "vi tri",
    "lien ket vung",
    # Finance & Banking
    "chuyen khoan", "so du", "lai suat", "hoa don", "bao cao tai chinh",
    "thue gia tri gia tang", "nguoi thu huong", "sao ke", "tin dung", "khoan vay",
    # Education & EdTech (7-Tier: Mầm non -> Tiến sĩ)
    "hoc sinh", "sinh vien", "phu huynh", "giao vien", "bai tap", "kiem tra",
    "bang diem", "hoc ba", "ket qua hoc tap", "mam non", "mau giao", "luan van",
    "luan an", "nghien cuu sinh", "khoa luan tot nghiep",
    # Healthcare, Legal, Hospitality & HR
    "kham chua benh", "benh nhan", "nguoi benh", "don thuoc", "thuc pham chuc nang",
    "hop dong", "boi thuong thiet hai", "bat kha khang", "giai quyet tranh chap",
    "khach san", "dat phong", "nhan phong", "tra phong", "chuyen bay", "hanh ly",
    "tuyen dung", "ung vien", "thu viec", "bao hiem xa hoi", "hop dong lao dong",
    # Real Estate, E-Commerce, Gov DVC, Insurance, Cybersecurity & Media PR
    "giay chung nhan", "dien tich thong thuy", "kinh phi bao tri", "ban giao can ho",
    "da thong bao bo cong thuong", "da dang ky bo cong thuong", "mien phi van chuyen",
    "dich vu cong truc tuyen", "the can cuoc", "dinh danh dien tu", "so ho khau",
    "hop dong bao hiem", "phi bao hiem", "loai tru trach nhiem", "gia tri hoan lai",
    "an toan thong tin", "lo hong bao mat", "du lieu ca nhan nhay cam", "tan cong mang",
    "thong cao bao chi", "cai chinh xin loi", "co quan bao chi",
)
DIACRITIC_RE = re.compile(
    r"(?<![\w/-])(" + "|".join(re.escape(p) for p in DIACRITIC_PHRASES) + r")(?![\w/-])",
    re.IGNORECASE,
)

# Mojibake (UTF-8 bytes decoded as Latin-1 / Windows-1252)
MOJIBAKE_RE = re.compile(
    r"(?:Ã¡|Ã |áº¡|áº£|Ã£|Ã¢|áº¥|áº§|áº©|áº«|áº­|Äƒ|áº¯|áº±|áº³|áºµ|áº·|"
    r"Ã©|Ã¨|áº¹|áº»|áº½|Ãª|áº¿|á» |á»ƒ|á»…|á»‡|Ä‘|Ä |Æ°|á»©|á»«|á»­|á»¯|á»±|"
    r"Æ¡|á»›|á» |á»Ÿ|á»¡|á»£|Ã´|á»‘|á»“|á»•|á»—|á»™)"
)

# Syntactic translationese patterns (structural English word-order calques)
SYNTACTIC_CALQUES: Tuple[Tuple[re.Pattern, str, str], ...] = (
    (
        re.compile(r"(?<!\w)như\s+một\s+([^,\n]{2,60}?),?\s+tôi\s+muốn(?!\w)", re.IGNORECASE),
        "English user-story calque “Như một ..., tôi muốn”",
        "write “Là [vai trò], tôi muốn…”",
    ),
    (
        re.compile(r"(?<!\w)nó\s+là\s+(?:rất\s+)?(?:quan\s+trọng|cần\s+thiết)\s+để(?!\w)", re.IGNORECASE),
        "dummy-subject calque “Nó là quan trọng/cần thiết để”",
        "recast with a direct clause: “Cần…” or “Việc … rất quan trọng”",
    ),
    (
        re.compile(r"(?<!\w)(?:làm|thực\s+hiện)\s+một\s+quyết\s+định(?!\w)", re.IGNORECASE),
        "light-verb calque “làm/thực hiện một quyết định” (make a decision)",
        "write “đưa ra quyết định” or simply “quyết định”",
    ),
    (
        re.compile(r"(?<!\w)lấy\s+một\s+hành\s+động(?!\w)", re.IGNORECASE),
        "calque “lấy một hành động” (take an action)",
        "write “thực hiện hành động” or name the exact verb",
    ),
)

# Case-aware Open-Syllable Tone Placement (oa / oe / uy)
VN_CHAR = (
    r"a-zA-ZăâđêôơưĂÂĐÊÔƠƯ"
    r"áàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩị"
    r"óòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    r"ÁÀẢÃẠẤẦẨẪẬẮẰẲẴẶÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊ"
    r"ÓÒỎÕỌỐỒỔỖỘỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ"
)
TONE_OLD_RE = re.compile(rf"(?<![{VN_CHAR}])[{VN_CHAR}]*[òóỏõọÒÓỎÕỌ][aeAE](?![{VN_CHAR}])")
TONE_OLD_UY_RE = re.compile(rf"(?<![{VN_CHAR}])[{VN_CHAR}]*(?<![qQ])[ùúủũụÙÚỦŨỤ][yY](?![{VN_CHAR}])")
TONE_NEW_RE = re.compile(rf"(?<![{VN_CHAR}])[{VN_CHAR}]*[oO][àáảãạèéẻẽẹÀÁẢÃẠÈÉẺẼẸ](?![{VN_CHAR}])")
TONE_NEW_UY_RE = re.compile(rf"(?<![{VN_CHAR}])[{VN_CHAR}]*(?<![qQ])[uU][ỳýỷỹỵỲÝỶỸỴ](?![{VN_CHAR}])")

# Mapping tables for --fix-tone=new and --fix-tone=old
_OLD_TO_NEW_PAIRS = {
    # oa
    "òa": "oà", "óa": "oá", "ỏa": "oả", "õa": "oã", "ọa": "oạ",
    "Òa": "Oà", "Óa": "Oá", "Ỏa": "Oả", "Õa": "Oã", "Ọa": "Oạ",
    "ÒA": "OÀ", "ÓA": "OÁ", "ỎA": "OẢ", "ÕA": "OÃ", "ỌA": "OẠ",
    # oe
    "òe": "oè", "óe": "oé", "ỏe": "oẻ", "õe": "oẽ", "ọe": "oẹ",
    "Òe": "Oè", "Óe": "Oé", "Ỏe": "Oẻ", "Õe": "Oẽ", "Ọe": "Oẹ",
    "ÒE": "OÈ", "ÓE": "OÉ", "ỎE": "OẺ", "ÕE": "OẼ", "ỌE": "OẸ",
    # uy
    "ùy": "uỳ", "úy": "uý", "ủy": "uỷ", "ũy": "uỹ", "ụy": "uỵ",
    "Ùy": "Uỳ", "Úy": "Uý", "Ủy": "Uỷ", "Ũy": "Uỹ", "Ụy": "Uỵ",
    "ÙY": "UỲ", "ÚY": "UÝ", "ỦY": "UỶ", "ŨY": "UỸ", "ỤY": "UỴ",
}
_NEW_TO_OLD_PAIRS = {v: k for k, v in _OLD_TO_NEW_PAIRS.items()}

# Locale & Number Patterns
NUM_COMMA_GROUP_RE = re.compile(r"(?<![\d.,])\d{1,3}(?:,\d{3})+(?![\d,])")
NUM_UNGROUPED_RE = re.compile(r"(?<![\d.,])(\d{4,})(?![\d.,])\s*(VND|vnd|₫|đồng|đ(?![\w]))")
# Only flag period as decimal separator when followed by 1-2 digits (e.g. 4.5%, 12.75 m²) or 0.xxx (never 5.000 tỷ thousands separator)
NUM_DOT_DECIMAL_RE = re.compile(
    r"(?<![\d.,vV])(?:0\.\d{1,3}|[1-9]\d*\.\d{1,2})(?![\d.])\s*(?:tỷ|tỉ|triệu|nghìn|ngàn|%|m²|m³|cm²|km²|kg|km|lít|điểm|g/dL|mmol/L)"
)
# Area/Volume ASCII superscript check with Hardware Chip Guard (matches both '50 m2' and '50m2', never flags Apple M2/M3, SSD M2, BMW M2/M3)
SQM_RE = re.compile(r"(?<![a-zA-Z_])(cm2|km2|m2|m3)(?![\w])", re.IGNORECASE)
HARDWARE_M2_CONTEXT_RE = re.compile(
    r"(?:"
    r"(?:apple|chip|macbook(?:\s+(?:air|pro))?|mac\s+mini|mac\s+studio|ipad(?:\s+(?:air|pro))?|imac|vi\s+xử\s+lý|bộ\s+xử\s+lý|ổ\s+cứng|ssd|nvme|pcie|khe|chuẩn|bmw)\s+$|"
    r"^\s*(?:pro|max|ultra|air|ssd|nvme|pcie|sata|\d+gb|\d+tb)"
    r")",
    re.IGNORECASE,
)

DATE_RE = re.compile(r"(?<![\d/])(\d{1,2})/(\d{1,2})/(\d{4})(?![\d/])")
PHONE_RE = re.compile(r"\+84[\s.-]*\(?0\)?")

# Multi-line & Single-line ICU MessageFormat Checks
ICU_PLURAL_BLOCK_RE = re.compile(r"\{\s*[\w.]+\s*,\s*plural\s*,", re.IGNORECASE)
ICU_NON_OTHER_RE = re.compile(r"(?<!\w)(zero|one|two|few|many)\s*\{")
# Placeholder variable containing Vietnamese diacritics (e.g. {tên}, {{số_lượng}})
TRANSLATED_PLACEHOLDER_RE = re.compile(
    r"\{\{?\s*([a-zA-Z0-9_]*[ăâđêôơưĂÂĐÊÔƠƯáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ][a-zA-Z0-9_\s]*)\s*\}?\}"
)

RULE_DOCS: Dict[str, str] = {
    "NFC001": "Unicode is decomposed (NFD); emit precomposed NFC",
    "ENC001": "corrupted UTF-8 mojibake or legacy Vietnamese encoding detected",
    "CAL001": "English calque — use the conventional Vietnamese wording",
    "SYN001": "English syntactic translationese — recast with natural Vietnamese clause order",
    "LAW001": "regulated superlative — needs documented proof (Luật Quảng cáo Đ8 K11 & Luật 75/2025)",
    "DIA001": "Vietnamese text written without diacritics",
    "TONE001": "both tone-mark conventions (kiểu mới & kiểu cũ) mixed in one document",
    "NUM001": "comma used as a thousands separator; Vietnamese uses a period",
    "NUM002": "ungrouped currency amount; use periods every three digits",
    "NUM003": "period used as a decimal separator; Vietnamese uses a comma",
    "NUM004": "ASCII unit exponent (m2/m3/cm2/km2); use superscript m²/m³/cm²/km²",
    "DATE001": "date appears to be MM/dd/yyyy; Vietnamese uses dd/MM/yyyy",
    "PHONE001": "trunk zero kept after the +84 country code",
    "ICU001": "ICU non-'other' plural branch (one/zero/two/few/many); Vietnamese uses 'other' only",
    "ICU002": "translated/accented placeholder variable name; keep placeholder identifiers ASCII",
    "PRO001": "formal and casual pronouns mixed in one document",
    "PRO002": "pronoun does not match the declared register",
}

BASE_RULE_DOCS: Dict[str, str] = dict(RULE_DOCS)
DOMAIN_MODULES: List = []
DOCTYPES: Dict[str, str] = {}


class Context:
    __slots__ = ("path", "lines", "masked", "text", "register", "doctype", "is_markdown")

    def __init__(self, path, lines, masked, text, register, doctype, is_markdown):
        self.path = path
        self.lines = lines
        self.masked = masked
        self.text = text
        self.register = register
        self.doctype = doctype
        self.is_markdown = is_markdown


def _resolve_domain_skill_dir(domain: str) -> Optional[pathlib.Path]:
    skill_slug = DOMAIN_SKILL_MAP.get(domain, domain)
    candidates = (
        SKILL_DIR if SKILL_DIR.name == skill_slug else None,
        SKILL_DIR.parent / "skills" / skill_slug,
        SKILL_DIR.parent / skill_slug,
        SKILL_DIR.parent.parent / "skills" / skill_slug,
    )
    for cand in candidates:
        if cand is not None and cand.is_dir():
            return cand
    return None


def load_domain_rules_multi(directories: Sequence[pathlib.Path]) -> List:
    import importlib.util

    RULE_DOCS.clear()
    RULE_DOCS.update(BASE_RULE_DOCS)
    DOCTYPES.clear()
    modules = []
    seen_paths: set = set()
    for directory in directories:
        for path in sorted(directory.glob("rules_*.py")):
            resolved = path.resolve()
            if resolved in seen_paths:
                continue
            seen_paths.add(resolved)
            spec = importlib.util.spec_from_file_location(path.stem, path)
            if spec is None or spec.loader is None:
                continue
            module = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(module)
            except Exception as exc:
                print(f"warning: cannot load {path.name}: {exc}", file=sys.stderr)
                continue
            RULE_DOCS.update(getattr(module, "RULE_DOCS", {}))
            DOCTYPES.update(getattr(module, "DOCTYPES", {}))
            modules.append(module)
    DOMAIN_MODULES[:] = modules
    return modules


def load_domain_rules(directory: Optional[pathlib.Path] = None) -> List:
    return load_domain_rules_multi([directory or SCRIPT_DIR])


load_domain_rules()


class Validator:
    def __init__(self, blocklists: Blocklists, register: Optional[str] = None,
                 doctype: Optional[str] = None):
        self.bl = blocklists
        self.calques = list(blocklists.compiled_calques())
        self.register = register
        self.doctype = doctype

    def check_file(self, path: pathlib.Path) -> List[Finding]:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            return [Finding("IO001", ERROR, path, 1, 1, "", f"cannot read UTF-8 file: {exc}")]
        return self.check_text(text, path)

    def check_text(self, text: str, path: pathlib.Path = pathlib.Path("<stdin>")) -> List[Finding]:
        disabled = file_disabled_rules(text)
        if "ALL" in disabled:
            return []

        raw_lines = text.splitlines()
        # Normalize to NFC in memory so decomposed NFD input cannot bypass linguistic & domain rules
        text_nfc = unicodedata.normalize("NFC", text)
        lines = text_nfc.splitlines()
        suffix = path.suffix.lower()
        is_markdown = suffix in (".md", ".mdx", ".markdown") or str(path) == "<stdin>"
        is_json = suffix in (".json", ".xcstrings")
        masked = mask_code(lines, is_markdown, is_json=is_json)
        findings: List[Finding] = []

        def emit(rule: str, severity: str, lineno: int, col: int,
                 snippet: str, message: str, hint: str = "") -> None:
            if rule in disabled:
                return
            if 1 <= lineno <= len(lines):
                line_disabled = line_disabled_rules(lines[lineno - 1])
                if "ALL" in line_disabled or rule in line_disabled:
                    return
            findings.append(Finding(rule, severity, path, lineno, col, snippet, message, hint))

        self._check_nfc_and_encoding(raw_lines, path, emit)
        self._check_text_rules(lines, masked, path, emit)
        self._check_multiline_icu(lines, "\n".join(masked), emit)
        self._check_tone_consistency(masked, path, emit)
        self._check_pronouns(masked, path, emit)
        self._check_domain_rules(lines, masked, text_nfc, path, is_markdown, emit)

        findings.sort(key=lambda f: (f.line, f.col, f.rule))
        return findings

    def _check_nfc_and_encoding(self, lines: Sequence[str], path: pathlib.Path, emit) -> None:
        for i, line in enumerate(lines, 1):
            if unicodedata.normalize("NFC", line) != line:
                col = 1
                for j, ch in enumerate(line):
                    if unicodedata.combining(ch):
                        col = max(1, j)
                        break
                emit(
                    "NFC001", ERROR, i, col, line.strip()[:60],
                    "text is not NFC-normalized (decomposed NFD diacritics)",
                    "run with --fix, or call unicodedata.normalize('NFC', text)",
                )
            m_moji = MOJIBAKE_RE.search(line)
            if m_moji:
                emit(
                    "ENC001", ERROR, i, m_moji.start() + 1, m_moji.group(0),
                    f"UTF-8 mojibake / legacy encoding artifact “{m_moji.group(0)}”",
                    "file was decoded as Latin-1/CP1252 before saving as UTF-8; re-decode from raw bytes",
                )

    def _check_text_rules(self, lines: Sequence[str], masked: Sequence[str],
                          path: pathlib.Path, emit) -> None:
        for i, line in enumerate(masked, 1):
            # 1. Calque blocklist (longest span wins, one finding per winning span)
            hits = [
                (m.start(), m.end(), phrase, suggestion, source, declared)
                for regex, phrase, suggestion, source, declared in self.calques
                for m in regex.finditer(line)
            ]
            winning_spans: Dict[Tuple[int, int], List[Tuple[str, str, str, Optional[str]]]] = {}
            for start, end, phrase, suggestion, source, declared in hits:
                if any(
                    other_start <= start and end <= other_end
                    and (other_end - other_start) > (end - start)
                    for other_start, other_end, *_ in hits
                ):
                    continue
                winning_spans.setdefault((start, end), []).append(
                    (phrase, suggestion, source, declared)
                )
            for (start, end), group in sorted(winning_spans.items()):
                matched = line[start:end]
                severities = [
                    d or (WARN if " " not in p else ERROR)
                    for p, _s, _src, d in group
                ]
                severity = ERROR if ERROR in severities else WARN
                merged_suggestions: List[str] = []
                seen_lower: set = set()
                has_glossary = False
                for _p, sugg, src, _d in group:
                    if src == "glossary.md":
                        has_glossary = True
                    for part in (x.strip() for x in sugg.split("/") if x.strip()):
                        key = part.lower()
                        if key not in seen_lower:
                            seen_lower.add(key)
                            merged_suggestions.append(part)
                merged_str = " / ".join(merged_suggestions)
                hint = f"use “{merged_str}”" if merged_str else ""
                if has_glossary:
                    hint += " (glossary.md)" if hint else "see glossary.md"
                emit("CAL001", severity, i, start + 1, matched, f"calque “{matched}”", hint)

            # 2. Syntactic translationese
            for syn_re, msg, hint in SYNTACTIC_CALQUES:
                for m in syn_re.finditer(line):
                    emit("SYN001", WARN, i, m.start() + 1, m.group(0), msg, hint)

            # 3. Advertising superlatives with multi-line proof window, negation & ordinal guard
            proof_window = any(
                bool(PROOF_RE.search(lines[idx]))
                for idx in range(max(0, i - 3), i)
            )
            if not proof_window:
                sup_hits: List[Tuple[int, int, str]] = []
                for regex, _note in self.bl.superlatives:
                    for m in regex.finditer(line):
                        prefix = line[max(0, m.start() - 40):m.start()]
                        if NEGATION_PREFIX_RE.search(prefix):
                            continue
                        if _is_benign_superlative(line, m.start(), m.group(0)):
                            continue
                        sup_hits.append((m.start(), m.end(), m.group(0)))
                seen_sup_spans: set = set()
                for s_start, s_end, s_text in sorted(sup_hits, key=lambda x: (x[0], -(x[1] - x[0]))):
                    if any(os <= s_start and s_end <= oe for os, oe in seen_sup_spans):
                        continue
                    seen_sup_spans.add((s_start, s_end))
                    emit(
                        "LAW001", WARN, i, s_start + 1, s_text,
                        f"regulated superlative “{s_text}”",
                        "needs a licensed market survey or award certificate; annotate "
                        "with <!-- proof: ... --> or rewrite as a countable fact",
                    )

            # 4. Unaccented Vietnamese phrases
            for m in DIACRITIC_RE.finditer(line):
                emit(
                    "DIA001", WARN, i, m.start() + 1, m.group(0),
                    f"Vietnamese written without diacritics: “{m.group(0)}”",
                    "restore the tone marks; unaccented forms belong in slugs and search indexes only",
                )

            # 5. Numbers & Currency
            for m in NUM_COMMA_GROUP_RE.finditer(line):
                fixed = m.group(0).replace(",", ".")
                emit("NUM001", ERROR, i, m.start() + 1, m.group(0),
                     f"comma-grouped number “{m.group(0)}”", f"write “{fixed}”")

            for m in NUM_UNGROUPED_RE.finditer(line):
                emit("NUM002", WARN, i, m.start() + 1, m.group(0),
                     f"ungrouped currency amount “{m.group(0)}”",
                     "group thousands with periods (e.g. 50.000 ₫), or use tỷ/triệu scale in prose")

            for m in NUM_DOT_DECIMAL_RE.finditer(line):
                fixed = m.group(0).replace(".", ",", 1)
                emit("NUM003", ERROR, i, m.start() + 1, m.group(0),
                     f"period used as a decimal separator in “{m.group(0)}”", f"write “{fixed}”")

            for m in SQM_RE.finditer(line):
                unit_raw = m.group(1)
                before = line[max(0, m.start() - 25):m.start()]
                after = line[m.end():min(len(line), m.end() + 20)]
                # Guard Apple M2/M3, SSD M2, BMW M2/M3 when capitalized M2/M3 or in hardware context
                if unit_raw in ("M2", "M3") and (
                    HARDWARE_M2_CONTEXT_RE.search(before) or HARDWARE_M2_CONTEXT_RE.search(after)
                ):
                    continue
                if unit_raw.lower() in ("m2", "m3") and (
                    HARDWARE_M2_CONTEXT_RE.search(before) or HARDWARE_M2_CONTEXT_RE.search(after)
                ):
                    continue
                sup_map = {"m2": "m²", "m3": "m³", "cm2": "cm²", "km2": "km²"}
                target = sup_map.get(unit_raw.lower(), "m²")
                emit("NUM004", WARN, i, m.start() + 1, m.group(0),
                     f"ASCII “{m.group(0)}”", f"use the superscript “{target}”")

            # 6. Dates & Phones
            for m in DATE_RE.finditer(line):
                first, second = int(m.group(1)), int(m.group(2))
                if second > 12 and first <= 12:
                    emit("DATE001", ERROR, i, m.start() + 1, m.group(0),
                         f"date “{m.group(0)}” looks like MM/dd/yyyy",
                         f"write “{m.group(2)}/{m.group(1)}/{m.group(3)}” (dd/MM/yyyy)")

            for m in PHONE_RE.finditer(line):
                emit("PHONE001", ERROR, i, m.start() + 1, m.group(0),
                     "trunk zero kept after +84", "drop the leading 0: +84 912 345 678")

            # 7. Translated Placeholder Variables (evaluated on masked line so code blocks are ignored)
            for m in TRANSLATED_PLACEHOLDER_RE.finditer(line):
                var_name = m.group(1).strip()
                emit("ICU002", ERROR, i, m.start() + 1, m.group(0),
                     f"placeholder variable “{var_name}” contains Vietnamese diacritics",
                     "keep interpolation variable identifiers ASCII (e.g. {name}, {{count}})")

    def _check_multiline_icu(self, lines: Sequence[str], text: str, emit) -> None:
        """Scan both single-line and multi-line ICU plural blocks for forbidden branches."""
        for m_block in ICU_PLURAL_BLOCK_RE.finditer(text):
            # Find the closing brace of this ICU plural block using balanced brace counting
            start_idx = m_block.start()
            depth = 0
            end_idx = len(text)
            for pos in range(start_idx, len(text)):
                ch = text[pos]
                if ch == "{":
                    depth += 1
                elif ch == "}":
                    depth -= 1
                    if depth == 0:
                        end_idx = pos + 1
                        break
            block_str = text[start_idx:end_idx]
            for m_branch in ICU_NON_OTHER_RE.finditer(block_str):
                abs_pos = start_idx + m_branch.start()
                lineno = text[:abs_pos].count("\n") + 1
                line_start = text.rfind("\n", 0, abs_pos) + 1
                col = abs_pos - line_start + 1
                category = m_branch.group(1)
                emit(
                    "ICU001", ERROR, lineno, col, m_branch.group(0),
                    f"ICU plural has a “{category}” branch",
                    f"Vietnamese has only the 'other' plural category (plus optional '=0') — delete '{category}'",
                )

    def _check_tone_consistency(self, masked: Sequence[str], path: pathlib.Path, emit) -> None:
        old_hits: List[Tuple[int, int, str]] = []
        new_hits: List[Tuple[int, int, str]] = []
        for i, line in enumerate(masked, 1):
            for regex in (TONE_OLD_RE, TONE_OLD_UY_RE):
                for m in regex.finditer(line):
                    old_hits.append((i, m.start() + 1, m.group(0)))
            for regex in (TONE_NEW_RE, TONE_NEW_UY_RE):
                for m in regex.finditer(line):
                    new_hits.append((i, m.start() + 1, m.group(0)))
        if old_hits and new_hits:
            # Dominant convention is whichever has more occurrences; if tied, the earlier one wins
            if len(new_hits) > len(old_hits) or (len(new_hits) == len(old_hits) and new_hits[0] < old_hits[0]):
                minority_hits = old_hits
                dominant_sample = new_hits[0][2]
            else:
                minority_hits = new_hits
                dominant_sample = old_hits[0][2]
            for lineno, col, word in minority_hits:
                emit(
                    "TONE001", WARN, lineno, col, word,
                    f"mixed tone-mark conventions: “{dominant_sample}” and “{word}”",
                    "pick kiểu mới (hoà, thuỷ) or kiểu cũ (hòa, thủy) consistently, or run --fix-tone new|old",
                )

    def _check_pronouns(self, masked: Sequence[str], path: pathlib.Path, emit) -> None:
        # Strip compound words containing bạn/quý so they never trigger pronoun rules
        cleaned_lines = [
            PRONOUN_COMPOUND_EXEMPT_RE.sub(lambda m: " " * len(m.group(0)), line)
            for line in masked
        ]

        def find_first(term: str) -> Optional[Tuple[int, int, str]]:
            body = r"\s+".join(re.escape(w) for w in term.split())
            regex = re.compile(rf"(?<!\w){body}(?!\w)", re.IGNORECASE)
            for i, line in enumerate(cleaned_lines, 1):
                m = regex.search(line)
                if m:
                    return (i, m.start() + 1, m.group(0))
            return None

        formal = next((h for h in (find_first(p) for p in FORMAL_PRONOUNS) if h), None)
        casual = next((h for h in (find_first(p) for p in CASUAL_PRONOUNS) if h), None)

        if formal and casual:
            later = max(formal, casual, key=lambda h: (h[0], h[1]))
            other = formal if later is casual else casual
            emit(
                "PRO001", WARN, later[0], later[1], later[2],
                f"mixed register: “{other[2]}” and “{later[2]}” in one document",
                "maintain one consistent register per document — see references/register-matrix.md",
            )

        if self.register:
            profile = self.bl.registers.get(self.register)
            if profile is None:
                return
            for forbidden in profile["forbids"]:
                hit = find_first(forbidden)
                if hit:
                    emit(
                        "PRO002", WARN, hit[0], hit[1], hit[2],
                        f"“{hit[2]}” does not fit the {self.register} register",
                        (
                            f"this register addresses the reader as “{profile['expects']}”"
                            if profile["expects"]
                            else "this register is impersonal and uses no direct second-person address"
                        ),
                    )

    def _check_domain_rules(self, lines, masked, text, path, is_markdown, emit) -> None:
        if not DOMAIN_MODULES:
            return
        ctx = Context(path, lines, masked, text, self.register, self.doctype, is_markdown)
        for module in DOMAIN_MODULES:
            per_line = getattr(module, "check_line", None)
            if per_line is not None:
                for i, line in enumerate(masked, 1):
                    for found in per_line(ctx, i, lines[i - 1], line) or ():
                        rule, severity, col, snippet, message, hint = found
                        emit(rule, severity, i, col, snippet, message, hint)
            whole = getattr(module, "check_document", None)
            if whole is not None:
                for found in whole(ctx) or ():
                    rule, severity, lineno, col, snippet, message, hint = found
                    emit(rule, severity, lineno, col, snippet, message, hint)


# --------------------------------------------------------------------------- #
# Deterministic Auto-Fixers (NFC & Tone Placement)
# --------------------------------------------------------------------------- #
def collect(paths: Iterable[str], extensions: Sequence[str]) -> List[pathlib.Path]:
    out: List[pathlib.Path] = []
    for raw in paths:
        p = pathlib.Path(raw)
        if p.is_dir():
            found: List[pathlib.Path] = []
            for dirpath, dirnames, filenames in os.walk(p):
                dirnames[:] = [d for d in dirnames if d not in EXCLUDED_DIRS]
                for name in filenames:
                    if pathlib.Path(name).suffix.lower() not in extensions:
                        continue
                    candidate = pathlib.Path(dirpath) / name
                    if candidate.is_file():
                        found.append(candidate)
            out.extend(sorted(found))
        elif p.exists():
            out.append(p)
        else:
            print(f"warning: no such path: {p}", file=sys.stderr)
    return out


def fix_nfc(path: pathlib.Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    normalized = unicodedata.normalize("NFC", text)
    if normalized == text:
        return False
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(normalized)
    return True


def convert_tone_style(text: str, style: str) -> str:
    """Convert open-syllable oa/oe/uy tone placement to 'new' (hoà) or 'old' (hòa)."""
    mapping = _OLD_TO_NEW_PAIRS if style == "new" else _NEW_TO_OLD_PAIRS

    def _replace_word(match: re.Match) -> str:
        word = match.group(0)
        for src, dst in mapping.items():
            if word.endswith(src):
                return word[:-len(src)] + dst
        return word

    if style == "new":
        text = TONE_OLD_RE.sub(_replace_word, text)
        text = TONE_OLD_UY_RE.sub(_replace_word, text)
    elif style == "old":
        text = TONE_NEW_RE.sub(_replace_word, text)
        text = TONE_NEW_UY_RE.sub(_replace_word, text)
    return text


def fix_tone(path: pathlib.Path, style: str) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False
    updated = convert_tone_style(unicodedata.normalize("NFC", text), style)
    if updated == text:
        return False
    with path.open("w", encoding="utf-8", newline="") as handle:
        handle.write(updated)
    return True


def _force_utf8_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    _force_utf8_output()
    ap = argparse.ArgumentParser(
        prog="validate_copy.py",
        description="DESIGN:OS Vietnamese (vi-VN) copy, typography, and compliance linter.",
        epilog="Rules: " + ", ".join(f"{k} ({v})" for k, v in sorted(RULE_DOCS.items())),
    )
    ap.add_argument("paths", nargs="*", help="files or directories to check (or '-' for stdin)")
    ap.add_argument(
        "--domain",
        default=None,
        help="select domain ruleset(s) and reference tables (single domain, comma-separated list like finance,legal, or 'all')",
    )
    ap.add_argument(
        "--register",
        help="enable register-consistency check (PRO002); values defined in references/register-matrix.md",
    )
    ap.add_argument(
        "--doctype",
        default=None,
        help="declare artifact type to activate structural domain rules"
        + ("; one of: " + ", ".join(sorted(DOCTYPES)) if DOCTYPES else ""),
    )
    ap.add_argument("--json", action="store_true", dest="as_json", help="emit findings as JSON")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on warnings as well as errors")
    ap.add_argument("--fix", action="store_true", help="rewrite NFC violations in place, then re-check")
    ap.add_argument(
        "--fix-tone",
        choices=("new", "old"),
        default=None,
        help="normalize open-syllable oa/oe/uy tone placement in place to 'new' (hoà) or 'old' (hòa)",
    )
    ap.add_argument(
        "--output",
        default=None,
        help="write normalized/fixed output for the target file to this path instead of modifying in place",
    )
    ap.add_argument("--ext", default=",".join(DEFAULT_EXTENSIONS), help="comma-separated file extensions")
    ap.add_argument("--refs", default=None, help="directory holding reference markdown tables")
    ap.add_argument("--list-rules", action="store_true", help="print every rule this skill emits, then exit")
    args = ap.parse_args(argv)

    refs_dirs: List[pathlib.Path] = [pathlib.Path(args.refs)] if args.refs else [REF_DIR]
    if args.domain:
        raw_domains = [d.strip() for d in args.domain.split(",") if d.strip()]
        valid_choices = set(DOMAIN_SKILL_MAP) | {"all"}
        for d in raw_domains:
            if d not in valid_choices:
                print(
                    f"validate_copy.py: error: argument --domain: invalid choice: {d!r} "
                    f"(choose from {', '.join(repr(c) for c in sorted(valid_choices))})",
                    file=sys.stderr,
                )
                return 2
        if "all" in raw_domains:
            domain_tokens = sorted(set(DOMAIN_SKILL_MAP.values()))
        else:
            domain_tokens = []
            for d in raw_domains:
                slug = DOMAIN_SKILL_MAP[d]
                if slug not in domain_tokens:
                    domain_tokens.append(slug)
        script_dirs: List[pathlib.Path] = []
        domain_ref_dirs: List[pathlib.Path] = []
        for slug in domain_tokens:
            candidate_skill_dir = _resolve_domain_skill_dir(slug)
            if candidate_skill_dir is not None:
                if (candidate_skill_dir / "scripts").is_dir():
                    script_dirs.append(candidate_skill_dir / "scripts")
                if not args.refs and (candidate_skill_dir / "references").is_dir():
                    domain_ref_dirs.append(candidate_skill_dir / "references")
        if script_dirs:
            load_domain_rules_multi(script_dirs)
        if domain_ref_dirs and not args.refs:
            refs_dirs = domain_ref_dirs

    if args.doctype and DOCTYPES and args.doctype not in DOCTYPES:
        print(
            f"unknown doctype {args.doctype!r}; available doctypes: "
            + ", ".join(sorted(DOCTYPES)),
            file=sys.stderr,
        )
        return 2

    if args.list_rules:
        for rule, doc in sorted(RULE_DOCS.items()):
            print(f"{rule}  {doc}")
        return 0

    if not args.paths:
        ap.print_usage(sys.stderr)
        print("validate_copy.py: error: no paths given", file=sys.stderr)
        return 2

    blocklists = Blocklists(refs_dirs if len(refs_dirs) > 1 else refs_dirs[0])
    for missing in blocklists.missing:
        print(f"warning: reference file not found, some rules disabled: {missing}", file=sys.stderr)

    if args.register and args.register not in blocklists.registers:
        print(
            f"unknown register {args.register!r}; available registers: "
            + ", ".join(sorted(blocklists.registers)),
            file=sys.stderr,
        )
        return 2

    validator = Validator(blocklists, args.register, args.doctype)
    findings: List[Finding] = []

    if args.paths == ["-"]:
        stdin_text = sys.stdin.read()
        if args.output:
            out_path = pathlib.Path(args.output)
            if out_path.parent and not out_path.parent.exists():
                out_path.parent.mkdir(parents=True, exist_ok=True)
            out_text = unicodedata.normalize("NFC", stdin_text)
            if args.fix_tone:
                out_text = convert_tone_style(out_text, args.fix_tone)
            out_path.write_text(out_text, encoding="utf-8")
            if args.fix or args.fix_tone:
                stdin_text = out_text
        findings.extend(validator.check_text(stdin_text, pathlib.Path("<stdin>")))
        files_checked_count = 1
    else:
        extensions = tuple(
            e if e.startswith(".") else "." + e
            for e in (x.strip() for x in args.ext.split(","))
            if e
        )
        files = collect(args.paths, extensions)
        if not files:
            print("no files to check", file=sys.stderr)
            return 2

        target_files = files
        if args.output:
            if len(files) > 1:
                print("validate_copy.py: error: --output requires a single input file", file=sys.stderr)
                return 2
            out_path = pathlib.Path(args.output)
            if out_path.parent and not out_path.parent.exists():
                out_path.parent.mkdir(parents=True, exist_ok=True)
            src_text = files[0].read_text(encoding="utf-8")
            out_text = unicodedata.normalize("NFC", src_text)
            if args.fix_tone:
                out_text = convert_tone_style(out_text, args.fix_tone)
            out_path.write_text(out_text, encoding="utf-8")
            if (args.fix or args.fix_tone) and out_path.is_file():
                target_files = [out_path]
        else:
            if args.fix:
                for path in files:
                    if fix_nfc(path):
                        print(f"fixed NFC: {path}", file=sys.stderr)

            if args.fix_tone:
                for path in files:
                    if fix_tone(path, args.fix_tone):
                        print(f"fixed tone ({args.fix_tone}): {path}", file=sys.stderr)

        for path in target_files:
            findings.extend(validator.check_file(path))
        files_checked_count = len(files)

    errors = sum(1 for f in findings if f.severity == ERROR)
    warnings = len(findings) - errors

    if args.as_json:
        print(json.dumps({
            "files_checked": files_checked_count,
            "errors": errors,
            "warnings": warnings,
            "findings": [f.as_dict() for f in findings],
        }, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f.render())
        if findings:
            print()
        print(f"{files_checked_count} file(s) checked · {errors} error(s) · {warnings} warning(s)")
        if not findings:
            print("clean")

    if errors:
        return 1
    if warnings and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
