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
        self.assertEqual(
            proc.returncode,
            0,
            f"verify_ukmc.py failed:\n{proc.stdout}\n{proc.stderr}",
        )
        self.assertIn("files: 18", proc.stdout)
        self.assertIn("verified_claims: 19/19", proc.stdout)
        self.assertIn("independent_sources: 6", proc.stdout)
        self.assertIn("failures: 0", proc.stdout)
        self.assertIn("Decision: STOP_SUFFICIENT", proc.stdout)

    def test_sibling_knowledge_builder_if_installed(self) -> None:
        if not SIBLING_KB_SRC.is_dir():
            return
        env = dict(os.environ, PYTHONPATH=str(SIBLING_KB_SRC))
        for args, expected in (
            (["verify", str(KNOWLEDGE_ROOT), "--claims"], "failures: 0"),
            (["gate", "--root", str(KNOWLEDGE_ROOT), "--run-id", "vn-design-os-261026"], "Decision: STOP_SUFFICIENT"),
        ):
            proc = subprocess.run(
                [sys.executable, "-m", "knowledge_builder.cli", *args],
                cwd=str(REPO_ROOT),
                env=env,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, f"{args} failed:\n{proc.stdout}\n{proc.stderr}")
            self.assertIn(expected, proc.stdout)


if __name__ == "__main__":
    unittest.main()
