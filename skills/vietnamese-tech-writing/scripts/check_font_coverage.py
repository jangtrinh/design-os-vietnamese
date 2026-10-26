#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# synced from shared/scripts/check_font_coverage.py (60b0608ed7e6dd05) — edit shared/ source, not this copy
"""DESIGN:OS Vietnamese Font & Glyph Coverage Inspector (vi-VN).

Pure Python 3.9+ standard library. Zero external pip dependencies.
Inspects:
  1. CSS `unicode-range` declarations (`--from-css`)
  2. Binary `.ttf` / `.otf` OpenType `cmap` Format 4 & Format 12 tables (`--font-file`)
  3. Default Google Fonts Vietnamese subset (`--range`)
  4. All 134 precomposed Vietnamese vowels + Đ/đ + ₫ (U+20AB) + m²/m³

Usage:
    python3 check_font_coverage.py copy.md
    python3 check_font_coverage.py src/ --from-css app/globals.css
    python3 check_font_coverage.py copy.md --font-file public/fonts/Inter-Regular.ttf
    python3 check_font_coverage.py --list-required
"""
from __future__ import annotations

import argparse
import os
import pathlib
import re
import struct
import sys
import unicodedata
from typing import Iterable, List, Optional, Sequence, Set, Tuple

EXCLUDED_DIRS = frozenset({
    ".git", ".hg", ".svn", "node_modules", ".next", ".nuxt", "dist", "build", "out",
    "target", "vendor", ".venv", "venv", "__pycache__", ".cache", ".turbo", ".yarn",
    "coverage", ".pytest_cache", ".mypy_cache", ".tox", "_evidence",
})

DEFAULT_RANGE = (
    "U+0000-00FF, U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, "
    "U+01A0-01A1, U+01AF-01B0, U+0300-0301, U+0303-0304, U+0308-0309, "
    "U+0323, U+0329, U+1EA0-1EF9, U+2018-2019, U+201C-201D, U+2013-2014, "
    "U+2026, U+00B2, U+00B3, U+20AB"
)

# All 134 precomposed Vietnamese vowels (67 lowercase + 67 uppercase) + Đ/đ + ₫
REQUIRED_SAMPLE = (
    "ăâđêôơưĂÂĐÊÔƠƯ"
    "áàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩị"
    "óòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ"
    "ÁÀẢÃẠẤẦẨẪẬẮẰẲẴẶÉÈẺẼẸẾỀỂỄỆÍÌỈĨỊ"
    "ÓÒỎÕỌỐỒỔỖỘỚỜỞỠỢÚÙỦŨỤỨỪỬỮỰÝỲỶỸỴ₫"
)

KNOWN_GAP = "ỲỳỴỵỶỷỸỹ"

RANGE_TOKEN_RE = re.compile(r"[uU]\+([0-9A-Fa-f]{1,6})(?:-([0-9A-Fa-f]{1,6}))?")
UNICODE_RANGE_DECL_RE = re.compile(r"unicode-range\s*:\s*([^;}]+)", re.IGNORECASE)

DEFAULT_EXTENSIONS = (
    ".md", ".mdx", ".markdown", ".txt", ".json", ".html", ".htm",
    ".yaml", ".yml", ".ts", ".tsx", ".js", ".jsx", ".vue", ".svelte",
)


def parse_range(spec: str) -> List[Tuple[int, int]]:
    ranges: List[Tuple[int, int]] = []
    for match in RANGE_TOKEN_RE.finditer(spec):
        start = int(match.group(1), 16)
        end = int(match.group(2), 16) if match.group(2) else start
        ranges.append((start, end))
    if not ranges:
        raise ValueError(f"no U+ tokens found in range spec: {spec!r}")
    return ranges


def ranges_from_css(path: pathlib.Path) -> List[Tuple[int, int]]:
    text = path.read_text(encoding="utf-8", errors="replace")
    declarations = UNICODE_RANGE_DECL_RE.findall(text)
    if not declarations:
        raise ValueError(f"no unicode-range declarations in {path}")
    ranges: List[Tuple[int, int]] = []
    for decl in declarations:
        ranges.extend(parse_range(decl))
    return ranges


def ranges_from_ttf(path: pathlib.Path) -> List[Tuple[int, int]]:
    """Parse binary TrueType/OpenType (.ttf/.otf) cmap Format 4 & Format 12 tables."""
    data = path.read_bytes()
    if len(data) < 12:
        raise ValueError(f"file too short to be a TTF/OTF font: {path}")
    _sfnt_version, num_tables = struct.unpack(">IH", data[:6])
    cmap_offset = None
    cmap_length = None
    for i in range(num_tables):
        rec_pos = 12 + i * 16
        if rec_pos + 16 > len(data):
            break
        tag, _checksum, offset, length = struct.unpack(">4sIII", data[rec_pos:rec_pos + 16])
        if tag == b"cmap":
            cmap_offset = offset
            cmap_length = length
            break
    if cmap_offset is None or cmap_offset + 4 > len(data):
        raise ValueError(f"no cmap table found in font: {path}")

    _version, num_subtables = struct.unpack(">HH", data[cmap_offset:cmap_offset + 4])
    ranges: List[Tuple[int, int]] = []
    for i in range(num_subtables):
        sub_rec = cmap_offset + 4 + i * 8
        if sub_rec + 8 > len(data):
            break
        platform_id, encoding_id, sub_offset = struct.unpack(">HHI", data[sub_rec:sub_rec + 8])
        if platform_id not in (0, 3):  # Unicode or Windows Unicode
            continue
        pos = cmap_offset + sub_offset
        if pos + 2 > len(data):
            continue
        fmt = struct.unpack(">H", data[pos:pos + 2])[0]
        if fmt == 4 and pos + 14 <= len(data):
            seg_count_x2 = struct.unpack(">H", data[pos + 6:pos + 8])[0]
            seg_count = seg_count_x2 // 2
            end_codes_pos = pos + 14
            start_codes_pos = end_codes_pos + seg_count_x2 + 2
            if start_codes_pos + seg_count_x2 > len(data):
                continue
            end_codes = struct.unpack(f">{seg_count}H", data[end_codes_pos:end_codes_pos + seg_count_x2])
            start_codes = struct.unpack(f">{seg_count}H", data[start_codes_pos:start_codes_pos + seg_count_x2])
            for s, e in zip(start_codes, end_codes):
                if s != 0xFFFF:
                    ranges.append((s, e))
        elif fmt == 12 and pos + 16 <= len(data):
            num_groups = struct.unpack(">I", data[pos + 12:pos + 16])[0]
            grp_pos = pos + 16
            for g in range(num_groups):
                if grp_pos + 12 > len(data):
                    break
                s, e, _gid = struct.unpack(">III", data[grp_pos:grp_pos + 12])
                ranges.append((s, e))
                grp_pos += 12
    if not ranges:
        raise ValueError(f"could not extract Unicode cmap ranges from {path}")
    return ranges


def covered(codepoint: int, ranges: Sequence[Tuple[int, int]]) -> bool:
    return any(start <= codepoint <= end for start, end in ranges)


def describe(codepoint: int) -> str:
    try:
        name = unicodedata.name(chr(codepoint))
    except ValueError:
        name = "<unnamed>"
    char = chr(codepoint)
    shown = repr(char) if char.isprintable() else "<non-printing>"
    return f"U+{codepoint:04X} {shown:>6}  {name}"


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


def _force_utf8_output() -> None:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass


def main(argv: Optional[Sequence[str]] = None) -> int:
    _force_utf8_output()
    ap = argparse.ArgumentParser(
        prog="check_font_coverage.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    ap.add_argument("paths", nargs="*", help="files or directories of copy to check")
    ap.add_argument("--range", default=DEFAULT_RANGE, help="CSS unicode-range to test against")
    ap.add_argument("--from-css", metavar="FILE", help="read unicode-range declarations from CSS")
    ap.add_argument("--font-file", metavar="TTF_OTF", help="read binary cmap table from .ttf/.otf")
    ap.add_argument("--list-required", action="store_true", help="print all required Vietnamese codepoints")
    ap.add_argument("--ext", default=",".join(DEFAULT_EXTENSIONS), help="comma-separated extensions")
    args = ap.parse_args(argv)

    if args.list_required:
        for ch in sorted(set(REQUIRED_SAMPLE)):
            print(describe(ord(ch)))
        return 0

    if not args.paths:
        ap.error("give at least one file or directory (or use --list-required)")

    try:
        if args.font_file:
            ranges = ranges_from_ttf(pathlib.Path(args.font_file))
        elif args.from_css:
            ranges = ranges_from_css(pathlib.Path(args.from_css))
        else:
            ranges = parse_range(args.range)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    extensions = tuple(
        e if e.startswith(".") else "." + e
        for e in (x.strip() for x in args.ext.split(","))
        if e
    )
    files = collect(args.paths, extensions)
    if not files:
        print("no files to check", file=sys.stderr)
        return 2

    used: Set[int] = set()
    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            print(f"warning: skipping {path}: {exc}", file=sys.stderr)
            continue
        used.update(ord(ch) for ch in unicodedata.normalize("NFC", text))

    for ctrl in (0x0A, 0x0D, 0x09):
        used.discard(ctrl)

    uncovered = sorted(cp for cp in used if not covered(cp, ranges))
    print(f"{len(files)} file(s) · {len(used)} distinct codepoints · {len(ranges)} range(s) in font")

    gaps_in_font = [ch for ch in KNOWN_GAP if not covered(ord(ch), ranges)]
    if gaps_in_font:
        print(
            f"\nnote: this font subset is missing {''.join(gaps_in_font)} (google/fonts#189 trap). "
            "Words like 'kỳ vọng', 'tỷ đồng', 'Mỹ' will trigger fallback font substitution."
        )

    if not uncovered:
        print("\nclean — every codepoint is inside the declared font coverage")
        return 0

    print(f"\n{len(uncovered)} uncovered codepoint(s):")
    for cp in uncovered:
        print(f"  {describe(cp)}")
    print("\nSelect a Vietnamese-complete typeface (e.g. Be Vietnam Pro, Plus Jakarta Sans, Inter)")
    print("and include the 'vietnamese' subset in next/font or @font-face.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
