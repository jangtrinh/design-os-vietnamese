#!/usr/bin/env python3
"""Tests that shared/ files and generated examples.md are in sync across all 6 skills."""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent


class SharedSyncTests(unittest.TestCase):
    def test_sync_shared_check_passes(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools" / "sync_shared.py"), "--check"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            proc.returncode,
            0,
            f"sync_shared.py --check failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}",
        )

    def test_build_examples_check_passes(self) -> None:
        proc = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools" / "build_examples.py"), "--check"],
            cwd=str(REPO_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(
            proc.returncode,
            0,
            f"build_examples.py --check failed:\nSTDOUT:\n{proc.stdout}\nSTDERR:\n{proc.stderr}",
        )


if __name__ == "__main__":
    unittest.main()
