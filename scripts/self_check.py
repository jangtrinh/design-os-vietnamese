#!/usr/bin/env python3
"""self_check.py — Deterministic offline self-check for design-os-vietnamese."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_JSON = (
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".agents/plugins/marketplace.json",
    ".factory-plugin/plugin.json",
    ".factory-plugin/marketplace.json",
)

REQUIRED_FILES = (
    "README.md",
    "README.vi.md",
    "LICENSE",
    "PRIVACY.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "CHANGELOG.md",
    "llms.txt",
    "docs/cookbook.md",
    "docs/index.html",
    "docs/llms.txt",
    "docs/robots.txt",
    "docs/sitemap.xml",
    "commands/doctor.md",
    "prompts/doctor.md",
    "shared/scripts/validate_copy.py",
    "shared/scripts/check_i18n_parity.py",
    "shared/scripts/check_font_coverage.py",
    "tools/verify_ukmc.py",
)

EXPECTED_SKILLS = (
    "vn-design-system-ux",
    "vietnamese-landing-copy",
    "vietnamese-tech-writing",
    "vietnamese-business-comms",
    "vietnamese-finance-copy",
    "vietnamese-education-copy",
    "vietnamese-healthcare-copy",
    "vietnamese-legal-contracts",
    "vietnamese-hospitality-travel",
    "vietnamese-hr-recruitment",
)


def main() -> int:
    issues: list[str] = []
    for rel in REQUIRED_JSON:
        p = ROOT / rel
        if not p.is_file():
            issues.append(f"missing JSON manifest: {rel}")
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                issues.append(f"manifest is not a JSON object: {rel}")
        except Exception as exc:
            issues.append(f"invalid JSON in {rel}: {exc}")

    for rel in REQUIRED_FILES:
        p = ROOT / rel
        if not p.is_file() or p.stat().st_size == 0:
            issues.append(f"missing or empty required file: {rel}")

    for slug in EXPECTED_SKILLS:
        sf = ROOT / "skills" / slug / "SKILL.md"
        if not sf.is_file():
            issues.append(f"missing skill entrypoint: skills/{slug}/SKILL.md")

    if issues:
        for item in issues:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1

    print("ok: design-os-vietnamese self-check passed (10 skills, 12 UKMC.v1 modules)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
