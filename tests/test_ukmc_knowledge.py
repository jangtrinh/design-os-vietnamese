#!/usr/bin/env python3
"""Tests that knowledge/ conforms to UKMC.v1 and passes verify_ukmc (and knowledge_builder when available)."""

from __future__ import annotations

import os
import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_ROOT = REPO_ROOT / "knowledge"
VERIFY_UKMC = REPO_ROOT / "tools" / "verify_ukmc.py"
SIBLING_KB_SRC = REPO_ROOT.parent / "design-os-knowledge-builder" / "src"


class UKMCKnowledgeBaseTests(unittest.TestCase):
    def test_portable_ukmc_verifier_and_stopping_gate(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(VERIFY_UKMC), "--root", str(KNOWLEDGE_ROOT), "--run-id", "vn-design-os-261026"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        # The latest independent review (review.json) did not pass, so the verifier
        # honestly stops short of STOP. Every structural check must still hold, and the
        # review must be the only failure.
        self.assertEqual(proc.returncode, 1, f"verify_ukmc.py:\n{proc.stdout}\n{proc.stderr}")
        output = proc.stdout + proc.stderr
        failures = [line for line in output.splitlines() if line.startswith("FAIL:")]
        self.assertEqual(failures, ["FAIL: review.json did not pass independent review"])
        self.assertIn("files: 18", proc.stdout)
        self.assertIn("verified_claims: 65/65", proc.stdout)
        self.assertIn("independent_sources: 28", proc.stdout)
        self.assertIn("failures: 1", proc.stdout)
        self.assertIn("Decision: CONTINUE_GAP", proc.stdout)

    def test_sibling_knowledge_builder_if_installed(self) -> None:
        if not SIBLING_KB_SRC.is_dir():
            return
        env = dict(os.environ, PYTHONPATH=str(SIBLING_KB_SRC))
        # Rounds 6-13 found new statutory material and probes remain open, so the run is
        # honestly DEEPEN (exit 2), not STOP. Every hard gate must still hold.
        gate = ["gate", "--root", str(KNOWLEDGE_ROOT), "--run-id", "vn-design-os-261026"]
        for args, returncode, expected in (
            (["verify", str(KNOWLEDGE_ROOT), "--claims"], 0, ("failures: 0",)),
            (gate, 2, ("Hard Gates Passed: True", "Decision: DEEPEN")),
        ):
            proc = subprocess.run(
                [sys.executable, "-m", "knowledge_builder.cli", *args],
                cwd=str(REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, returncode, f"{args} failed:\n{proc.stdout}\n{proc.stderr}")
            for text in expected:
                self.assertIn(text, proc.stdout)


if __name__ == "__main__":
    unittest.main()
