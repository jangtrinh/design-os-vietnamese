#!/usr/bin/env python3
"""QA findings 2026-10-26 (see docs/QA-FINDINGS.md).
These tests are expected to FAIL on the current main and PASS once fixed."""
from __future__ import annotations
import re, subprocess, sys, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared" / "scripts" / "validate_copy.py"
UX = ROOT / "skills" / "vn-design-system-ux" / "scripts" / "validate_copy.py"
FIX = ROOT / "tests" / "fixtures" / "qa"
README = (ROOT / "README.md").read_text(encoding="utf-8")
README_VI = (ROOT / "README.vi.md").read_text(encoding="utf-8")


def run(*args):
    return subprocess.run([sys.executable, *map(str, args)], capture_output=True,
                          text=True, cwd=ROOT)


class F01CalqueNotDetected(unittest.TestCase):
    def test_shared_validator_flags_readme_calque(self):
        r = run(SHARED, FIX / "calque_readme_example.md", "--json")
        self.assertIn("CAL001", r.stdout + r.stderr)

    def test_ux_skill_validator_flags_readme_calque(self):
        r = run(UX, FIX / "calque_readme_example.md", "--json")
        self.assertIn("CAL001", r.stdout + r.stderr)

    def test_shared_references_present(self):
        for name in ("glossary.md", "banned-phrases.md"):
            self.assertTrue((ROOT / "shared" / "references" / name).is_file(), name)

    def test_no_rules_disabled_warning(self):
        r = run(SHARED, FIX / "calque_readme_example.md")
        self.assertNotIn("some rules disabled", r.stderr)


class F02QuickStartBroken(unittest.TestCase):
    def test_documented_domain_flag_is_accepted(self):
        r = run(SHARED, FIX / "calque_readme_example.md", "--domain", "ux",
                "--register", "ux-microcopy")
        self.assertNotIn("unrecognized arguments", r.stderr)

    def test_documented_i18n_parity_flags_accepted(self):
        r = run(ROOT / "shared/scripts/check_i18n_parity.py",
                "--source", "skills/vn-design-system-ux/assets/en.sample.json",
                "--target", "skills/vn-design-system-ux/assets/vi.sample.json", "--json")
        self.assertNotIn("unrecognized arguments", r.stderr)

    def test_documented_output_flag_is_accepted(self):
        r = run(SHARED, FIX / "calque_readme_example.md", "--output", "/dev/null")
        self.assertNotIn("unrecognized arguments", r.stderr)

    def test_no_personal_absolute_paths_in_docs(self):
        for text in (README, README_VI):
            self.assertFalse("/Users/jangtrinh" in text, "personal /Users/jangtrinh path in README")

    def test_no_personal_paths_in_tests(self):
        for p in (ROOT / "tests").glob("test_*.py"):
            if p.name == Path(__file__).name:
                continue
            self.assertNotIn("/Users/jangtrinh", p.read_text(encoding="utf-8"), p.name)


class F03LicenseConflict(unittest.TestCase):
    """Flag only: policy is PolyForm Shield; repo says MIT."""
    def test_license_is_not_mit(self):
        self.assertNotIn("MIT License", (ROOT / "LICENSE").read_text(encoding="utf-8"))

    def test_readmes_do_not_claim_mit(self):
        for text in (README, README_VI):
            self.assertIsNone(re.search(r"\bMIT\b", text), "README claims MIT")


class F04ReadmeReferencedFilesExist(unittest.TestCase):
    def test_reference_files_listed_in_skill_table_exist(self):
        names = set(re.findall(r"`([a-z0-9\-]+\.md)`", README.split("## Deterministic")[0]))
        missing = [n for n in sorted(names)
                   if not list((ROOT / "skills").glob(f"*/references/{n}"))]
        self.assertEqual(missing, [])

    def test_rule_engine_filenames_match(self):
        for n in set(re.findall(r"`(rules_[a-z]+\.py)`", README)):
            self.assertTrue(list((ROOT / "skills").glob(f"*/scripts/{n}")), n)


class F05Images(unittest.TestCase):
    def test_repo_has_at_least_one_image(self):
        imgs = [p for ext in ("png", "jpg", "jpeg", "svg", "gif", "webp")
                for p in ROOT.rglob(f"*.{ext}") if ".git" not in p.parts]
        self.assertTrue(imgs, "no images in repo")


if __name__ == "__main__":
    unittest.main()
