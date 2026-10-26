#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build references/examples.md for each skill from evals/<skill>/pairs.jsonl.

Usage:
    python3 tools/build_examples.py          # write skills/*/references/examples.md
    python3 tools/build_examples.py --check  # exit 1 if any examples.md is out of date
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
from collections import defaultdict
from typing import Dict, List

ROOT = pathlib.Path(__file__).resolve().parent.parent
EVALS_DIR = ROOT / "evals"
SKILLS_DIR = ROOT / "skills"


def render_examples(skill_name: str, pairs_path: pathlib.Path) -> str:
    by_category: Dict[str, List[dict]] = defaultdict(list)
    lines_raw = [l.strip() for l in pairs_path.read_text(encoding="utf-8").splitlines() if l.strip()]
    for idx, raw in enumerate(lines_raw, 1):
        item = json.loads(raw)
        cat = item.get("category", "general")
        by_category[cat].append(item)

    out = [
        "<!-- vlc-disable: all -->",
        f"# Worked Diagnostic Pairs — `{skill_name}`",
        "",
        f"> Auto-generated from `evals/{skill_name}/pairs.jsonl` ({len(lines_raw)} verified pairs). "
        "Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.",
        "",
    ]

    for cat, items in by_category.items():
        title = cat.replace("-", " ").replace("_", " ").title()
        out.append(f"## {title}")
        out.append("")
        for item in items:
            pid = item.get("id", "")
            bad = item["bad"]
            good = item["good"]
            rules = ", ".join(f"`{r}`" for r in item.get("expected_rules", []))
            why = item.get("why", item.get("note", ""))
            doctype = item.get("doctype")
            register = item.get("register")
            meta_parts = []
            if rules:
                meta_parts.append(f"Rules: {rules}")
            if register:
                meta_parts.append(f"Register: `{register}`")
            if doctype:
                meta_parts.append(f"Doctype: `{doctype}`")
            meta_str = " · ".join(meta_parts)
            out.append(f"### {pid}" + (f" ({meta_str})" if meta_str else ""))
            out.append("")
            out.append("```diff")
            for b_line in bad.splitlines():
                out.append(f"- {b_line}")
            for g_line in good.splitlines():
                out.append(f"+ {g_line}")
            out.append("```")
            if why:
                out.append(f"- **Why:** {why}")
            out.append("")

    return "\n".join(out).rstrip() + "\n"


def build_all(check_only: bool = False) -> int:
    drifted = []
    count = 0
    for skill_dir in sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir()):
        skill_name = skill_dir.name
        pairs_path = EVALS_DIR / skill_name / "pairs.jsonl"
        if not pairs_path.is_file():
            continue
        expected = render_examples(skill_name, pairs_path)
        dest = skill_dir / "references" / "examples.md"
        count += 1
        if check_only:
            if not dest.is_file() or dest.read_text(encoding="utf-8") != expected:
                drifted.append(dest.relative_to(ROOT).as_posix())
        else:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(expected, encoding="utf-8")

    if check_only:
        if drifted:
            for d in drifted:
                print(f"drift: {d} is out of date with evals/ (run: python3 tools/build_examples.py)", file=sys.stderr)
            return 1
        print(f"build_examples: {count} skills verified up-to-date")
    else:
        print(f"build_examples: generated examples.md for {count} skills")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()
    return build_all(check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
