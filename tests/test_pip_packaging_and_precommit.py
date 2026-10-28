#!/usr/bin/env python3
"""Regression tests: pip-installable console commands and portable pre-commit hooks.

Defects covered
---------------
1. ``.pre-commit-hooks.yaml`` used ``language: system`` with a repo-relative
   ``entry`` (``python3 shared/scripts/...``). pre-commit runs hooks in the
   *consumer* repo, so the script path never exists there.
2. ``pyproject.toml`` shipped ``py-modules = []`` and no ``[project.scripts]``,
   so ``pip install`` installed neither code nor commands.

All tests are offline and stdlib-only. The wheel-layout test additionally needs
``setuptools`` (a build-time dependency) and is skipped when it is missing; CI
installs the project for real.
"""
from __future__ import annotations

import json
import os
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
import zipfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED_SCRIPTS = ROOT / "shared" / "scripts"
HOOKS_FILE = ROOT / ".pre-commit-hooks.yaml"
PYPROJECT = ROOT / "pyproject.toml"

# console command -> (hook id, shared script it must mirror, cli function name)
COMMANDS = {
    "vi-validate-copy": ("validate-copy", "validate_copy.py", "validate_copy_main"),
    "vi-i18n-parity": ("check-i18n-parity", "check_i18n_parity.py", "i18n_parity_main"),
    "vi-font-coverage": ("check-font-coverage", "check_font_coverage.py", "font_coverage_main"),
}
PACKAGE = "vi_design_os"

BAD_DATE = "Hạn chót: 12/25/2026.\n"
GOOD_LINE = "Xin chào bạn.\n"
FIN_LINE = "Cam kết lợi nhuận 18%/năm.\n"


def parse_hooks(text: str) -> list:
    """Minimal parser for the flat list-of-mappings layout of .pre-commit-hooks.yaml."""
    hooks: list = []
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^- (\w+):\s*(.*)$", line)
        if m:
            hooks.append({m.group(1): m.group(2).strip()})
            continue
        m = re.match(r"^\s+(\w+):\s*(.*)$", line)
        if m and hooks:
            hooks[-1][m.group(1)] = m.group(2).strip()
    return hooks


def project_scripts(text: str) -> dict:
    section = re.search(r"^\[project\.scripts\]\s*\n(.*?)(?=^\[|\Z)", text, re.M | re.S)
    if not section:
        return {}
    out = {}
    for m in re.finditer(r'^([\w.-]+)\s*=\s*"([^"]+)"\s*$', section.group(1), re.M):
        out[m.group(1)] = m.group(2)
    return out


def run_entry(func: str, *args: str, stdin: str = "", cwd: pathlib.Path = ROOT, env=None):
    code = f"import sys; from {PACKAGE}.cli import {func}; sys.exit({func}())"
    return subprocess.run(
        [sys.executable, "-c", code, *args],
        input=stdin,
        capture_output=True,
        text=True,
        cwd=str(cwd),
        env=env,
    )


def run_script(script: str, *args: str, stdin: str = ""):
    return subprocess.run(
        [sys.executable, str(SHARED_SCRIPTS / script), *args],
        input=stdin,
        capture_output=True,
        text=True,
        cwd=str(ROOT),
    )


class PreCommitHookDefinitionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.hooks = parse_hooks(HOOKS_FILE.read_text(encoding="utf-8"))

    def test_all_three_hook_ids_are_kept(self) -> None:
        self.assertEqual(
            sorted(h["id"] for h in self.hooks),
            sorted(spec[0] for spec in COMMANDS.values()),
        )

    def test_no_hook_relies_on_language_system(self) -> None:
        for hook in self.hooks:
            self.assertNotEqual(hook.get("language"), "system", hook["id"])
            self.assertEqual(hook.get("language"), "python", hook["id"])

    def test_no_hook_entry_uses_a_repo_relative_script_path(self) -> None:
        for hook in self.hooks:
            entry = hook["entry"]
            self.assertNotIn("shared/scripts", entry, hook["id"])
            self.assertNotIn(".py", entry, hook["id"])
            self.assertNotIn("python3", entry, hook["id"])

    def test_every_hook_entry_is_a_declared_console_script(self) -> None:
        declared = project_scripts(PYPROJECT.read_text(encoding="utf-8"))
        by_id = {spec[0]: cmd for cmd, spec in COMMANDS.items()}
        for hook in self.hooks:
            self.assertEqual(hook["entry"], by_id[hook["id"]], hook["id"])
            self.assertIn(hook["entry"], declared, hook["id"])


class PyprojectPackagingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.text = PYPROJECT.read_text(encoding="utf-8")

    def test_three_console_scripts_are_declared_and_importable_targets_exist(self) -> None:
        scripts = project_scripts(self.text)
        for cmd, (_hook, _script, func) in COMMANDS.items():
            self.assertEqual(scripts.get(cmd), f"{PACKAGE}.cli:{func}", cmd)

    def test_package_ships_code_and_data(self) -> None:
        self.assertNotRegex(self.text, r"(?m)^py-modules\s*=\s*\[\s*\]")
        self.assertIn(f'"{PACKAGE}"', self.text)
        self.assertIn("rules_*.py", self.text)
        self.assertIn("scripts/*.py", self.text)

    def test_runtime_dependencies_stay_empty(self) -> None:
        self.assertRegex(self.text, r"(?m)^dependencies\s*=\s*\[\s*\]")


class ConsoleEntryPointParityTests(unittest.TestCase):
    """Each entry point must behave exactly like the script it wraps."""

    def _assert_same(self, func: str, script: str, args, stdin: str = "") -> subprocess.CompletedProcess:
        via_entry = run_entry(func, *args, stdin=stdin)
        via_script = run_script(script, *args, stdin=stdin)
        self.assertNotIn("Traceback", via_entry.stderr, via_entry.stderr)
        self.assertEqual(via_entry.returncode, via_script.returncode, via_entry.stderr)
        self.assertEqual(via_entry.stdout, via_script.stdout)
        return via_entry

    def test_help_exits_zero_for_every_command(self) -> None:
        for _cmd, (_hook, script, func) in COMMANDS.items():
            r = self._assert_same(func, script, ["--help"])
            self.assertEqual(r.returncode, 0)
            self.assertIn("usage:", r.stdout)

    def test_validate_copy_list_rules_matches_script(self) -> None:
        r = self._assert_same("validate_copy_main", "validate_copy.py", ["--list-rules", "--domain", "all"])
        self.assertEqual(r.returncode, 0)
        self.assertGreaterEqual(len(r.stdout.splitlines()), 126)

    def test_validate_copy_stdin_domain_rule_fin001(self) -> None:
        r = self._assert_same(
            "validate_copy_main", "validate_copy.py", ["--json", "--domain", "finance", "-"], stdin=FIN_LINE
        )
        self.assertEqual(r.returncode, 0)  # FIN001 is a warning without --strict
        rules = {f["rule"] for f in json.loads(r.stdout)["findings"]}
        self.assertIn("FIN001", rules)

    def test_validate_copy_bad_date_exits_one_and_clean_exits_zero(self) -> None:
        bad = self._assert_same("validate_copy_main", "validate_copy.py", ["-"], stdin=BAD_DATE)
        self.assertEqual(bad.returncode, 1)
        self.assertIn("DATE001", bad.stdout)
        good = self._assert_same("validate_copy_main", "validate_copy.py", ["-"], stdin=GOOD_LINE)
        self.assertEqual(good.returncode, 0)
        self.assertIn("clean", good.stdout)

    def test_i18n_parity_matched_and_mismatched_catalogs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            en = pathlib.Path(tmp) / "en.json"
            vi_ok = pathlib.Path(tmp) / "vi_ok.json"
            vi_bad = pathlib.Path(tmp) / "vi_bad.json"
            en.write_text(json.dumps({"a": "Hello {name}", "b": "Save"}), encoding="utf-8")
            vi_ok.write_text(json.dumps({"a": "Xin chào {name}", "b": "Lưu"}, ensure_ascii=False), encoding="utf-8")
            vi_bad.write_text(json.dumps({"a": "Xin chào"}, ensure_ascii=False), encoding="utf-8")
            ok = self._assert_same("i18n_parity_main", "check_i18n_parity.py", [str(en), str(vi_ok), "--json"])
            self.assertEqual(ok.returncode, 0)
            self.assertEqual(json.loads(ok.stdout)["findings"], [])
            bad = self._assert_same("i18n_parity_main", "check_i18n_parity.py", [str(en), str(vi_bad), "--json"])
            self.assertEqual(bad.returncode, 1)
            self.assertTrue(json.loads(bad.stdout)["findings"])

    def test_font_coverage_covered_and_uncovered_ranges(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            copy = pathlib.Path(tmp) / "vi.md"
            copy.write_text("Xin chào, giá 50.000 ₫ ạ ế\n", encoding="utf-8")
            css = pathlib.Path(tmp) / "latin-only.css"
            css.write_text("@font-face { font-family: X; unicode-range: U+0000-00FF; }\n", encoding="utf-8")
            ok = self._assert_same("font_coverage_main", "check_font_coverage.py", [str(copy)])
            self.assertEqual(ok.returncode, 0)
            bad = self._assert_same(
                "font_coverage_main", "check_font_coverage.py", [str(copy), "--from-css", str(css)]
            )
            self.assertEqual(bad.returncode, 1)
            self.assertIn("uncovered", bad.stdout)


@unittest.skipUnless(shutil.which(sys.executable) and __import__("importlib.util").util.find_spec("setuptools"),
                     "setuptools not installed; CI builds and installs the package for real")
class BuiltWheelLayoutTests(unittest.TestCase):
    """Build the wheel and run the entry points from the extracted layout, away from the repo."""

    @classmethod
    def setUpClass(cls) -> None:
        cls._tmp = tempfile.TemporaryDirectory()
        base = pathlib.Path(cls._tmp.name)
        src = base / "src"
        shutil.copytree(
            ROOT,
            src,
            ignore=shutil.ignore_patterns(
                ".git", "__pycache__", "*.pyc", "build", "dist", "*.egg-info", ".claude", "plans", "knowledge"
            ),
        )
        out = base / "wheelhouse"
        out.mkdir()
        proc = subprocess.run(
            [
                sys.executable,
                "-c",
                "import sys; from setuptools import build_meta; "
                "print(build_meta.build_wheel(sys.argv[1]))",
                str(out),
            ],
            cwd=str(src),
            capture_output=True,
            text=True,
        )
        if proc.returncode != 0:
            raise AssertionError(f"wheel build failed:\n{proc.stdout}\n{proc.stderr}")
        cls.wheel = out / proc.stdout.strip().splitlines()[-1]
        cls.site = base / "site"
        with zipfile.ZipFile(cls.wheel) as zf:
            cls.names = zf.namelist()
            zf.extractall(cls.site)
        cls.elsewhere = base / "elsewhere"
        cls.elsewhere.mkdir()

    @classmethod
    def tearDownClass(cls) -> None:
        cls._tmp.cleanup()

    def _env(self) -> dict:
        env = dict(os.environ)
        env["PYTHONPATH"] = str(self.site)
        return env

    def test_wheel_declares_console_scripts(self) -> None:
        entry = [n for n in self.names if n.endswith("entry_points.txt")]
        self.assertEqual(len(entry), 1)
        text = (self.site / entry[0]).read_text(encoding="utf-8")
        for cmd, (_hook, _script, func) in COMMANDS.items():
            self.assertIn(f"{cmd} = {PACKAGE}.cli:{func}", text)

    def test_wheel_keeps_shared_and_skills_as_siblings(self) -> None:
        self.assertIn(f"{PACKAGE}/shared/scripts/validate_copy.py", self.names)
        self.assertIn(f"{PACKAGE}/shared/references/glossary.md", self.names)
        rules = [n for n in self.names if re.fullmatch(rf"{PACKAGE}/skills/[^/]+/scripts/rules_\w+\.py", n)]
        self.assertEqual(len(rules), 16)

    def test_installed_list_rules_matches_repo_script(self) -> None:
        r = run_entry("validate_copy_main", "--list-rules", "--domain", "all", cwd=self.elsewhere, env=self._env())
        self.assertNotIn("Traceback", r.stderr, r.stderr)
        self.assertEqual(r.returncode, 0)
        expected = run_script("validate_copy.py", "--list-rules", "--domain", "all")
        self.assertEqual(r.stdout, expected.stdout)
        self.assertEqual(len(r.stdout.splitlines()), len(expected.stdout.splitlines()))

    def test_installed_domain_rule_fires_outside_the_repo(self) -> None:
        r = run_entry(
            "validate_copy_main", "--json", "--domain", "finance", "-",
            stdin=FIN_LINE, cwd=self.elsewhere, env=self._env(),
        )
        self.assertNotIn("Traceback", r.stderr, r.stderr)
        self.assertEqual(r.returncode, 0)
        self.assertIn("FIN001", {f["rule"] for f in json.loads(r.stdout)["findings"]})


if __name__ == "__main__":
    unittest.main()
