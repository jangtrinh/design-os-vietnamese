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
import xml.etree.ElementTree as ET
from typing import Any, Dict, List, Optional, Sequence, Set, Tuple

PLACEHOLDER_RE = re.compile(
    r"(\{\{\s*[\w.]+\s*\}\}|\{\s*[\w.]+\s*,\s*(?:number|date|time|plural|select|selectordinal)\b|\{\s*[\w.]+\s*\}|%\(\w+\)[sdif]|%(?:\d+\$)?(?:\.\d+)?[sdif@]|<\/?\d+>)"
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
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            key = f"{prefix}[{idx}]" if prefix else f"[{idx}]"
            out.update(flatten_json(item, key))
    elif isinstance(data, str):
        out[prefix] = data
    return out


def _flatten_xcstrings_locale(strings_obj: Dict[str, Any], lang: str, is_source: bool = False) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for key, entry in strings_obj.items():
        if not isinstance(entry, dict):
            continue
        if entry.get("shouldTranslate") is False:
            continue
        locs = entry.get("localizations", {})
        loc = locs.get(lang)
        if not isinstance(loc, dict):
            if is_source:
                out[key] = str(key)
            continue
        unit = loc.get("stringUnit")
        if isinstance(unit, dict) and isinstance(unit.get("value"), str):
            out[key] = unit["value"]
        variations = loc.get("variations", {})
        if isinstance(variations, dict):
            plural = variations.get("plural", {})
            if isinstance(plural, dict):
                branches = []
                for branch_name, branch_obj in plural.items():
                    if isinstance(branch_obj, dict):
                        b_unit = branch_obj.get("stringUnit", {})
                        if isinstance(b_unit, dict) and isinstance(b_unit.get("value"), str):
                            branches.append(f"{branch_name} {{{b_unit['value']}}}")
                if branches:
                    out[key] = "{count, plural, " + " ".join(branches) + "}"
    return out


def _flatten_android_xml(path: pathlib.Path) -> Dict[str, str]:
    tree = ET.parse(path)
    root = tree.getroot()
    out: Dict[str, str] = {}
    for elem in root:
        if elem.attrib.get("translatable") == "false":
            continue
        name = elem.attrib.get("name", "")
        if not name:
            continue
        if elem.tag == "string":
            out[name] = "".join(elem.itertext())
        elif elem.tag == "string-array":
            for idx, item in enumerate(elem.findall("item")):
                out[f"{name}[{idx}]"] = "".join(item.itertext())
        elif elem.tag == "plurals":
            branches = []
            for item in elem.findall("item"):
                qty = item.attrib.get("quantity", "other")
                branches.append(f"{qty} {{{''.join(item.itertext())}}}")
            if branches:
                out[name] = "{count, plural, " + " ".join(branches) + "}"
    return out


def extract_placeholders(text: str) -> Set[str]:
    tokens: Set[str] = set()
    for m in PLACEHOLDER_RE.finditer(text):
        raw = m.group(1).strip()
        if raw.startswith("{{"):
            inner = raw[2:-2].strip()
            tokens.add("{{" + inner + "}}")
        elif raw.startswith("{"):
            inner = raw[1:].rstrip("}").split(",", 1)[0].strip()
            tokens.add("{" + inner + "}")
        else:
            tokens.add(re.sub(r"\s+", "", raw))
    return tokens


def compare_catalogs(en_path: pathlib.Path, vi_path: pathlib.Path) -> List[dict]:
    if en_path.suffix.lower() == ".xcstrings" or vi_path.suffix.lower() == ".xcstrings":
        xc_data = json.loads(en_path.read_text(encoding="utf-8"))
        src_lang = xc_data.get("sourceLanguage", "en")
        strings_obj = xc_data.get("strings", {})
        en_flat = _flatten_xcstrings_locale(strings_obj, src_lang, is_source=True)
        vi_flat = _flatten_xcstrings_locale(strings_obj, "vi", is_source=False)
    elif en_path.suffix.lower() == ".xml" and vi_path.suffix.lower() == ".xml":
        en_flat = _flatten_android_xml(en_path)
        vi_flat = _flatten_android_xml(vi_path)
    else:
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

        visible_vi = re.sub(
            r"\{\{?\s*[\w.]+\s*\}?\}|%(?:\d+\$)?[-+#0 ]*(?:\d+|\*)?(?:\.(?:\d+|\*))?[hlL]?[diuoxXfFeEgGaAcCsSp@]",
            "X",
            unicodedata.normalize("NFC", vi_val),
        )
        vi_nfc_len = len(visible_vi)
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
        description="Compare en.json/vi.json, Localizable.xcstrings, or strings.xml for key/placeholder parity and UI expansion caps.",
    )
    ap.add_argument("pos_source", nargs="?", help="source catalog (en.json, Localizable.xcstrings, or values/strings.xml)")
    ap.add_argument("pos_target", nargs="?", help="target Vietnamese catalog (vi.json, Localizable.xcstrings, or values-vi/strings.xml)")
    ap.add_argument("--source", dest="opt_source", default=None, help="source catalog")
    ap.add_argument("--target", dest="opt_target", default=None, help="target Vietnamese catalog")
    ap.add_argument("--json", action="store_true", dest="as_json", help="emit findings as JSON")
    ap.add_argument("--strict", action="store_true", help="exit non-zero on warnings too")
    args = ap.parse_args(argv)

    src_arg = args.opt_source or args.pos_source
    tgt_arg = args.opt_target or args.pos_target
    if src_arg and not tgt_arg and src_arg.lower().endswith(".xcstrings"):
        tgt_arg = src_arg
    if not src_arg or not tgt_arg:
        ap.print_usage(sys.stderr)
        print("check_i18n_parity.py: error: both source and target JSON files are required", file=sys.stderr)
        return 2

    en_path = pathlib.Path(src_arg)
    vi_path = pathlib.Path(tgt_arg)
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
