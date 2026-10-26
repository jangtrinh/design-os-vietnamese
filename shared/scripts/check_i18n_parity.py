#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""DESIGN:OS Vietnamese i18n Parity & UI Expansion Gate (en.json <-> vi.json).

Pure Python 3.9+ standard library. Zero external pip dependencies.
Verifies:
  1. Key parity between source (en.json) and target (vi.json) catalogs
  2. Placeholder parity ({name}, {{count}}, %s, %d, <0>...</0>)
  3. Precomposed NFC normalization of all Vietnamese values
  4. ICU plural rule compliance ('other'-only in vi.json)
  5. UI component character caps by emitter role inferred from key name
     (button/cta <= 28, tab <= 18, badge <= 16, toast <= 90)

Usage:
    python3 check_i18n_parity.py en.json vi.json
    python3 check_i18n_parity.py en.json vi.json --json --strict
"""
from __future__ import annotations

import argparse
import json
import pathlib
import re
import sys
import unicodedata
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

PLACEHOLDER_RE = re.compile(
    r"(\{\{\s*[\w.]+\s*\}\}|\{\s*[\w.]+\s*(?:,\s*(?:number|date|time|plural|select|selectordinal)\b)?|%\(\w+\)[sd]|%[sd]|<\d+>|<\/\d+>)"
)
ICU_PLURAL_RE = re.compile(r"\{\s*[\w.]+\s*,\s*plural\s*,", re.IGNORECASE)
ICU_FORBIDDEN_BRANCH_RE = re.compile(r"(?<!\w)(zero|one|two|few|many)\s*\{")

ROLE_CAPS: Tuple[Tuple[re.Pattern, str, int], ...] = (
    (re.compile(r"(?:^|\.)(?:cta|button|btn)(?:\.|$)", re.IGNORECASE), "button/CTA", 28),
    (re.compile(r"(?:^|\.)(?:tab|navItem)(?:\.|$)", re.IGNORECASE), "navigation tab", 18),
    (re.compile(r"(?:^|\.)(?:badge|pill|chip|statusTag)(?:\.|$)", re.IGNORECASE), "status badge", 16),
    (re.compile(r"(?:^|\.)(?:toast|snackbar)(?:\.|$)", re.IGNORECASE), "toast notification", 90),
)


def flatten_json(data: Any, prefix: str = "") -> Dict[str, str]:
    out: Dict[str, str] = {}
    if isinstance(data, dict):
        for k, v in data.items():
            key = f"{prefix}.{k}" if prefix else str(k)
            out.update(flatten_json(v, key))
    elif isinstance(data, str):
        out[prefix] = data
    return out


def extract_placeholders(text: str) -> Set[str]:
    tokens: Set[str] = set()
    for m in PLACEHOLDER_RE.finditer(text):
        raw = m.group(1).strip()
        if raw.startswith("{") and not raw.startswith("{{") and "," in raw:
            var_name = raw[1:].split(",", 1)[0].strip()
            tokens.add("{" + var_name + "}")
        else:
            tokens.add(re.sub(r"\s+", "", raw))
    return tokens


def compare_catalogs(en_path: pathlib.Path, vi_path: pathlib.Path) -> List[dict]:
    en_data = json.loads(en_path.read_text(encoding="utf-8"))
    vi_data = json.loads(vi_path.read_text(encoding="utf-8"))
    en_flat = flatten_json(en_data)
    vi_flat = flatten_json(vi_data)

    findings: List[dict] = []

    for key in sorted(set(en_flat) - set(vi_flat)):
        findings.append({
            "rule": "I18N001",
            "severity": "error",
            "key": key,
            "message": f"missing key in {vi_path.name}: {key!r}",
        })

    for key in sorted(set(vi_flat) - set(en_flat)):
        findings.append({
            "rule": "I18N002",
            "severity": "warning",
            "key": key,
            "message": f"extra key in {vi_path.name} not present in {en_path.name}: {key!r}",
        })

    for key in sorted(set(en_flat) & set(vi_flat)):
        en_val = en_flat[key]
        vi_val = vi_flat[key]

        if unicodedata.normalize("NFC", vi_val) != vi_val:
            findings.append({
                "rule": "NFC001",
                "severity": "error",
                "key": key,
                "message": f"decomposed NFD characters in key {key!r}",
            })

        en_ph = extract_placeholders(en_val)
        vi_ph = extract_placeholders(vi_val)
        if en_ph != vi_ph:
            findings.append({
                "rule": "I18N003",
                "severity": "error",
                "key": key,
                "message": f"placeholder mismatch in {key!r}: source={sorted(en_ph)} vs target={sorted(vi_ph)}",
            })

        if ICU_PLURAL_RE.search(vi_val):
            for m in ICU_FORBIDDEN_BRANCH_RE.finditer(vi_val):
                findings.append({
                    "rule": "ICU001",
                    "severity": "error",
                    "key": key,
                    "message": f"forbidden ICU plural branch {m.group(1)!r} in {key!r}; Vietnamese uses 'other' only",
                })

        vi_nfc_len = len(unicodedata.normalize("NFC", vi_val))
        for role_re, role_label, cap in ROLE_CAPS:
            if role_re.search(key) and vi_nfc_len > cap:
                findings.append({
                    "rule": "UX001",
                    "severity": "warning",
                    "key": key,
                    "message": f"{role_label} string {key!r} is {vi_nfc_len} chars (exceeds {cap}-char UI cap): {vi_val!r}",
                })

    return findings


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        prog="check_i18n_parity.py",
        description="Compare en.json and vi.json for key/placeholder parity and UI expansion caps.",
    )
    ap.add_argument("source", help="source catalog JSON (e.g. en.json)")
    ap.add_argument("target", help="target Vietnamese catalog JSON (e.g. vi.json)")
    ap.add_argument("--json", action="store_true", dest="as_json", help="emit findings as JSON")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on warnings too")
    args = ap.parse_args(argv)

    en_path = pathlib.Path(args.source)
    vi_path = pathlib.Path(args.target)
    if not en_path.is_file() or not vi_path.is_file():
        print("check_i18n_parity.py: error: both source and target JSON files must exist", file=sys.stderr)
        return 2

    try:
        findings = compare_catalogs(en_path, vi_path)
    except Exception as exc:
        print(f"check_i18n_parity.py: error: {exc}", file=sys.stderr)
        return 2

    errors = sum(1 for f in findings if f["severity"] == "error")
    warnings = len(findings) - errors

    if args.as_json:
        print(json.dumps({
            "source": str(en_path),
            "target": str(vi_path),
            "errors": errors,
            "warnings": warnings,
            "findings": findings,
        }, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{vi_path}:{f['key']}: {f['severity']} {f['rule']}  {f['message']}")
        print(f"checked {en_path.name} <-> {vi_path.name} · {errors} error(s) · {warnings} warning(s)")

    if errors or (warnings and args.strict):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
