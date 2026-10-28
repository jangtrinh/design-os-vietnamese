#!/usr/bin/env python3
"""Guard: rule messages, eval data and pair generators must cite current law.

Decree 13/2023/NĐ-CP stopped being in force on 01/01/2026 (replaced by
Luật 91/2025/QH15 + Nghị định 356/2025/NĐ-CP). Any remaining mention must be
labelled as expired. Also bans the stale breach form "03a", the unit code
"A05", and the FIN001 basis "Đ12; NĐ 38" / "NĐ 38/2018".
"""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

RULES_FILES = [
    REPO_ROOT / "skills" / "vietnamese-cybersecurity-infosec" / "scripts" / "rules_cybersecurity.py",
    REPO_ROOT / "skills" / "vietnamese-education-copy" / "scripts" / "rules_education.py",
    REPO_ROOT / "skills" / "vietnamese-landing-copy" / "scripts" / "rules_landing.py",
    REPO_ROOT / "skills" / "vietnamese-legal-contracts" / "scripts" / "rules_legal.py",
    REPO_ROOT / "skills" / "vietnamese-tech-writing" / "scripts" / "rules_tech.py",
    REPO_ROOT / "skills" / "vietnamese-finance-copy" / "scripts" / "rules_finance.py",
]

SCANNED_FILES = sorted(
    RULES_FILES
    + [REPO_ROOT / "evals" / "trigger-queries.md"]
    + list(REPO_ROOT.glob("evals/*/pairs.jsonl"))
    + [
        REPO_ROOT / "tools" / "generate_landing_pairs.py",
        REPO_ROOT / "tools" / "generate_tech_pairs.py",
    ]
)

DECREE_13_RE = re.compile(r"13/2023")
EXPIRED_MARKER = "hết hiệu lực"
EXPIRED_WINDOW = 40
OTHER_STALE_PATTERNS = {
    "03a": re.compile(r"03a"),
    "A05": re.compile(r"A05"),
    "Đ12; NĐ 38": re.compile(r"Đ12;\s*NĐ 38"),
    "NĐ 38/2018": re.compile(r"NĐ 38/2018"),
}


# Detection may still accept the legacy code so older copy that names "Cục A05" is not
# flagged for omitting the agency; only messages, hints and eval text must drop it.
ALLOWED_STALE_LINES = {
    ("skills/vietnamese-cybersecurity-infosec/scripts/rules_cybersecurity.py", "A05"): r"Cục\s+A05|A05|",
}


def _rel(path: Path) -> str:
    return str(path.relative_to(REPO_ROOT))


class CurrentPdpdCitationsTest(unittest.TestCase):
    def test_scan_set_is_complete(self):
        self.assertEqual(len(RULES_FILES), 6)
        for path in SCANNED_FILES:
            self.assertTrue(path.exists(), _rel(path))

    def test_decree_13_2023_only_cited_as_expired(self):
        offenders = []
        for path in SCANNED_FILES:
            text = path.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), start=1):
                for match in DECREE_13_RE.finditer(line):
                    tail = line[match.end():match.end() + EXPIRED_WINDOW]
                    if EXPIRED_MARKER not in tail:
                        offenders.append(f"{_rel(path)}:{lineno}")
        self.assertEqual(offenders, [], "13/2023 cited as current law")

    def test_no_other_stale_citations(self):
        offenders = []
        for path in SCANNED_FILES:
            text = path.read_text(encoding="utf-8")
            for lineno, line in enumerate(text.splitlines(), start=1):
                for label, pattern in OTHER_STALE_PATTERNS.items():
                    allowed = ALLOWED_STALE_LINES.get((_rel(path), label))
                    if allowed and allowed in line:
                        continue
                    if pattern.search(line):
                        offenders.append(f"{_rel(path)}:{lineno} [{label}]")
        self.assertEqual(offenders, [], "stale citation or form code present")


if __name__ == "__main__":
    unittest.main()
