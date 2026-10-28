#!/usr/bin/env python3
"""Regression tests for GitHub Issue #2 (https://github.com/jangtrinh/design-os-vietnamese/issues/2)
and comprehensive self-QA across all 10 skills and repository documentation."""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared" / "scripts" / "validate_copy.py"
FIX = ROOT / "tests" / "fixtures" / "qa" / "calque_readme_example.md"

DOMAIN_EXPECTED_RULE_PREFIX = {
    "ux": "UX001",
    "landing": "LND001",
    "tech": "ENG001",
    "biz": "ADMIN001",
    "finance": "FIN001",
    "edu": "EDU001",
    "healthcare": "MED001",
    "legal": "LEG001",
    "hospitality": "HOS001",
    "hr": "HR001",
    "realestate": "REA001",
    "ecommerce": "ECOM001",
    "gov": "GOV001",
    "insurance": "INS001",
    "cybersecurity": "SEC001",
    "media": "MEDJ001",
}


def run_cli(*args: object) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *map(str, args)],
        capture_output=True,
        text=True,
        cwd=ROOT,
    )


class Issue2DomainCrashRegressionTests(unittest.TestCase):
    """Issue #2 Item 1 (BLOCKER): any --domain call must not crash with NameError: SKILL_DIR."""

    def test_shared_and_all_10_skill_copies_accept_domain_on_clean_and_violation_files(self) -> None:
        scripts = [SHARED] + sorted(ROOT.glob("skills/*/scripts/validate_copy.py"))
        self.assertEqual(len(scripts), 17)

        with tempfile.NamedTemporaryFile("w", suffix=".md", encoding="utf-8", delete=False) as tf:
            tf.write("Xin chào bạn, hệ thống đã lưu cấu hình thành công.\n")
            clean_path = pathlib.Path(tf.name)

        try:
            for script in scripts:
                # 1. Clean file with --domain ux --register ux-microcopy -> exit 0, no Traceback
                r_clean = run_cli(script, clean_path, "--domain", "ux", "--register", "ux-microcopy")
                self.assertNotIn("Traceback", r_clean.stderr, f"{script} crashed: {r_clean.stderr}")
                self.assertEqual(r_clean.returncode, 0, f"{script} failed on clean file: {r_clean.stdout} {r_clean.stderr}")

                # 2. Calque fixture with --domain ux --register ux-microcopy -> exit 1, no Traceback
                r_bad = run_cli(script, FIX, "--domain", "ux", "--register", "ux-microcopy")
                self.assertNotIn("Traceback", r_bad.stderr, f"{script} crashed: {r_bad.stderr}")
                self.assertEqual(r_bad.returncode, 1, f"{script} wrong exit code: {r_bad.stdout}")
                self.assertIn("CAL001", r_bad.stdout)
        finally:
            clean_path.unlink(missing_ok=True)

    def test_all_10_domains_load_their_domain_rule_prefixes(self) -> None:
        for domain, expected_rule in DOMAIN_EXPECTED_RULE_PREFIX.items():
            r = run_cli(SHARED, "--domain", domain, "--list-rules")
            self.assertNotIn("Traceback", r.stderr, f"--domain {domain} crashed: {r.stderr}")
            self.assertEqual(r.returncode, 0)
            self.assertIn(expected_rule, r.stdout, f"--domain {domain} did not load {expected_rule}")

    def test_cross_domain_rule_docs_do_not_leak_from_skill_script(self) -> None:
        ux_script = ROOT / "skills" / "vn-design-system-ux" / "scripts" / "validate_copy.py"
        r = run_cli(ux_script, "--domain", "edu", "--list-rules")
        self.assertEqual(r.returncode, 0)
        self.assertIn("EDU001", r.stdout)
        self.assertNotIn("UX001", r.stdout)

    def test_output_flag_creates_nested_parent_and_rejects_multiple_inputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            nested_out = pathlib.Path(tmpdir) / "nested" / "dir" / "out.md"
            r = run_cli(SHARED, FIX, "--output", nested_out)
            self.assertNotIn("Traceback", r.stderr)
            self.assertTrue(nested_out.is_file())

            r_multi = run_cli(SHARED, FIX, ROOT / "README.md", "--output", nested_out)
            self.assertEqual(r_multi.returncode, 2)
            self.assertIn("--output requires a single input file", r_multi.stderr)

    def test_all_rule_ids_mentioned_in_docs_exist_in_engine(self) -> None:
        all_rules: set[str] = set()
        for domain in [None, *DOMAIN_EXPECTED_RULE_PREFIX.keys()]:
            args = [SHARED, "--list-rules"]
            if domain:
                args.extend(["--domain", domain])
            r = run_cli(*args)
            self.assertEqual(r.returncode, 0)
            for line in r.stdout.splitlines():
                if line.strip():
                    all_rules.add(line.split()[0])

        rule_re = re.compile(
            r"\b(?:NFC|ENC|CAL|SYN|LAW|DIA|TONE|NUM|DATE|PHONE|ICU|PRO|CTX|UX|LND|TECH|BIZ|ENG|PROD|ADMIN|MKT|SALES|SPAM|ZNS|FIN|EDU|MED|LEG|HOS|HR|REA|ECOM|GOV|INS|SEC|MEDJ)\d{3}\b"
        )
        for rel in ("README.md", "README.vi.md", "docs/index.html", "llms.txt", "docs/llms.txt"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            mentioned = set(rule_re.findall(text))
            missing = sorted(mentioned - all_rules)
            self.assertEqual(missing, [], f"{rel} mentions non-existent rule IDs: {missing}")


class Issue2CalqueDeduplicationTests(unittest.TestCase):
    """Issue #2 Item 4: CAL001 must emit 1 finding per span with deduplicated suggestions."""

    def test_calque_fixture_emits_single_deduplicated_finding(self) -> None:
        r_json = run_cli(SHARED, FIX, "--json")
        self.assertNotIn("Traceback", r_json.stderr)
        self.assertEqual(r_json.returncode, 1)
        payload = json.loads(r_json.stdout)
        cal_findings = [f for f in payload["findings"] if f["rule"] == "CAL001"]
        self.assertEqual(
            len(cal_findings),
            1,
            f"Expected 1 CAL001 finding for single span, got {len(cal_findings)}: {cal_findings}",
        )
        self.assertEqual(payload["errors"], 1)

        r_text = run_cli(SHARED, FIX)
        self.assertIn("1 error(s) · 0 warning(s)", r_text.stdout)
        self.assertEqual(r_text.stdout.count("error CAL001"), 1)


class Issue2DocsAndPathHygieneTests(unittest.TestCase):
    """Issue #2 Items 2, 3, 5: source-available wording, zero personal paths repo-wide, updated QA-FINDINGS.md."""

    def test_readme_uses_source_available_not_open_source(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIsNone(
            re.search(r"open[- ]source", readme, re.IGNORECASE),
            "README.md claims open-source; license is PolyForm Shield 1.0.0 (source-available)",
        )
        self.assertIn("source-available", readme)

    @staticmethod
    def _candidate_files() -> list[pathlib.Path]:
        """Files to scan: git-tracked files, so untracked local worktrees and scratch dirs
        never leak into the result. Falls back to a filesystem walk (skipping .git and
        .claude) when git is unavailable or ROOT is not a git work tree."""
        try:
            proc = subprocess.run(
                ["git", "ls-files", "-z"],
                capture_output=True,
                cwd=ROOT,
                check=True,
            )
        except (OSError, subprocess.CalledProcessError):
            return sorted(
                p for p in ROOT.rglob("*") if ".git" not in p.parts and ".claude" not in p.parts
            )
        names = [n for n in proc.stdout.decode("utf-8", errors="surrogateescape").split("\0") if n]
        return sorted(ROOT / n for n in names)

    def test_no_personal_paths_anywhere_in_repo_outside_test_assertions(self) -> None:
        personal_token = "/" + "/".join(("Users", "jangtrinh"))
        offenders: list[str] = []
        for p in self._candidate_files():
            if ".git" in p.parts or "__pycache__" in p.parts or not p.is_file():
                continue
            if p.parent == ROOT / "tests":
                continue
            try:
                text = p.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if personal_token in text:
                offenders.append(str(p.relative_to(ROOT)))
        self.assertEqual(offenders, [], f"Found personal absolute paths in: {offenders}")

    def test_qa_findings_doc_and_config_reflect_polyform_shield(self) -> None:
        qa_doc = (ROOT / "docs" / "QA-FINDINGS.md").read_text(encoding="utf-8")
        self.assertNotIn("LICENSE is MIT", qa_doc)
        self.assertNotIn("LICENSE and READMEs say MIT", qa_doc)
        self.assertIn("PolyForm Shield", qa_doc)

        config_yml = (ROOT / "docs" / "_config.yml").read_text(encoding="utf-8")
        self.assertIsNone(re.search(r"\bMIT\b", config_yml))


if __name__ == "__main__":
    unittest.main()
