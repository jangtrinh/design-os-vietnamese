#!/usr/bin/env python3
"""Tests that knowledge/ conforms to UKMC.v1 and passes design-os-knowledge-builder verify & gate."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_ROOT = REPO_ROOT / "knowledge"
KB_SRC = Path("/Users/jangtrinh/Products/design-os-knowledge-builder/src")


@unittest.skipUnless(KB_SRC.is_dir(), "design-os-knowledge-builder not present at /Users/jangtrinh/Products/design-os-knowledge-builder")
class UKMCKnowledgeBaseTests(unittest.TestCase):
    def test_ukmc_verify_claims_zero_failures(self) -> None:
        env = dict(**__import__("os").environ, PYTHONPATH=str(KB_SRC))
        proc = subprocess.run(
            [
                sys.executable,
                "-m",
                "knowledge_builder.cli",
                "verify",
                str(KNOWLEDGE_ROOT),
                "--claims",
            ],
            cwd=str(REPO_ROOT),
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            proc.returncode,
            0,
            f"knowledge_builder verify --claims failed:\n{proc.stdout}\n{proc.stderr}",
        )
        self.assertIn("files: 8", proc.stdout)
        self.assertIn("failures: 0", proc.stdout)

    def test_ukmc_stopping_gate_stop_sufficient(self) -> None:
        env = dict(**__import__("os").environ, PYTHONPATH=str(KB_SRC))
        proc = subprocess.run(
            [
                sys.executable,
                "-m",
                "knowledge_builder.cli",
                "gate",
                "--root",
                str(KNOWLEDGE_ROOT),
                "--run-id",
                "vn-design-os-261026",
            ],
            cwd=str(REPO_ROOT),
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            proc.returncode,
            0,
            f"knowledge_builder gate failed:\n{proc.stdout}\n{proc.stderr}",
        )
        self.assertIn("Decision: STOP_SUFFICIENT", proc.stdout)


if __name__ == "__main__":
    unittest.main()
