#!/usr/bin/env python3
"""Comprehensive unit and benchmark test suite for validate_copy.py v3.0,
check_font_coverage.py, check_i18n_parity.py, and all 6 skill evals.
"""

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unicodedata
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SHARED_SCRIPTS = REPO_ROOT / "shared" / "scripts"
sys.path.insert(0, str(SHARED_SCRIPTS))

import validate_copy  # noqa: E402
import check_font_coverage  # noqa: E402
import check_i18n_parity  # noqa: E402


def _load_skill_validator(skill_name: str):
    """Load the skill-specific validate_copy.py (with its domain rules_<domain>.py) in isolation."""
    skill_dir = REPO_ROOT / "skills" / skill_name
    scripts_dir = skill_dir / "scripts"
    refs_dir = skill_dir / "references"

    # Ensure the skill's scripts dir is at index 0 so validate_copy imports its local rules_*.py
    sys.path.insert(0, str(scripts_dir))
    try:
        for mod_name in list(sys.modules):
            if mod_name.startswith("rules_"):
                sys.modules.pop(mod_name, None)
        spec = importlib.util.spec_from_file_location(
            f"validate_copy_{skill_name.replace('-', '_')}",
            scripts_dir / "validate_copy.py",
        )
        module = importlib.util.module_from_spec(spec)
        assert spec.loader is not None
        spec.loader.exec_module(module)
        blocklists = module.Blocklists(refs_dir)
        return module, blocklists
    finally:
        if sys.path and sys.path[0] == str(scripts_dir):
            sys.path.pop(0)


class ValidateCopyCoreEngineTests(unittest.TestCase):
    """Tests for the 15 core rule families and v3.0 bug fixes in validate_copy.py."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.vc_mod, cls.blocklists = _load_skill_validator("vn-design-system-ux")

    def _codes(self, text: str, register: str | None = None, doctype: str | None = None) -> set[str]:
        validator = self.vc_mod.Validator(self.blocklists, register=register, doctype=doctype)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as fh:
            fh.write(text)
            tmp_path = Path(fh.name)
        try:
            findings = validator.check_file(tmp_path)
            return {f.rule for f in findings}
        finally:
            tmp_path.unlink(missing_ok=True)

    def test_nfc001_detects_nfd_and_autofixes(self) -> None:
        nfd_text = unicodedata.normalize("NFD", "Chuyển đổi số quốc gia")
        self.assertIn("NFC001", self._codes(nfd_text))
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as fh:
            fh.write(nfd_text)
            tmp_path = Path(fh.name)
        try:
            changed = self.vc_mod.fix_nfc(tmp_path)
            self.assertTrue(changed)
            fixed = tmp_path.read_text(encoding="utf-8")
            self.assertEqual(fixed, "Chuyển đổi số quốc gia")
            self.assertNotIn("NFC001", self._codes(fixed))
        finally:
            tmp_path.unlink(missing_ok=True)

    def test_enc001_detects_utf8_mojibake(self) -> None:
        mojibake = "ChÃ o má»«ng báº¡n Ä‘áº¿n vá»›i há»‡ thá»‘ng"
        self.assertIn("ENC001", self._codes(mojibake))

    def test_cal001_and_syn001_detect_english_calques_and_adversity_passive(self) -> None:
        self.assertIn("CAL001", self._codes("Vui lòng tiến hành đăng nhập vào hệ thống."))
        self.assertIn("SYN001", self._codes("Nó là quan trọng để bảo mật tài khoản của bạn."))

    def test_law001_flags_unverified_superlatives_with_negation_guard(self) -> None:
        self.assertIn("LAW001", self._codes("Giải pháp quản lý bán hàng tốt nhất Việt Nam."))
        self.assertNotIn("LAW001", self._codes("Chúng tôi không phải là đơn vị rẻ nhất."))

    def test_dia001_detects_multi_domain_ascii_vietnamese(self) -> None:
        self.assertIn("DIA001", self._codes("Vui long dang nhap tai khoan de thanh toan don hang."))
        self.assertIn("DIA001", self._codes("Chuyen khoan ngan hang va bao cao tai chinh."))

    def test_tone001_detects_mixed_tone_and_fix_tone_styles(self) -> None:
        mixed = "Chúng tôi chúc bạn sức khỏe dồi dào, hoà bình và hòa hợp trong cuộc sống."
        self.assertIn("TONE001", self._codes(mixed))
        fixed_new = self.vc_mod.convert_tone_style(mixed, "new")
        self.assertIn("khoẻ", fixed_new)
        self.assertIn("hoà hợp", fixed_new)
        self.assertNotIn("TONE001", self._codes(fixed_new))
        fixed_old = self.vc_mod.convert_tone_style(mixed, "old")
        self.assertIn("khỏe", fixed_old)
        self.assertIn("hòa bình", fixed_old)
        self.assertNotIn("TONE001", self._codes(fixed_old))

    def test_num002_and_num003_detect_unformatted_vnd_and_english_decimals(self) -> None:
        self.assertIn("NUM002", self._codes("Phí dịch vụ chỉ 50000đ mỗi tháng."))
        self.assertIn("NUM003", self._codes("Tăng trưởng đạt 12.5% trong kỳ."))
        self.assertNotIn("NUM002", self._codes("Phí dịch vụ chỉ 50.000 ₫ mỗi tháng."))

    def test_num004_flags_square_meters_but_exempts_apple_m2_m3_chips(self) -> None:
        self.assertIn("NUM004", self._codes("Văn phòng có diện tích 120 m2 và thể tích 360 m3."))
        hw_text = "Ứng dụng biên dịch mượt trên MacBook Air M2, chip Apple M2 Max và MacBook Pro M3."
        self.assertNotIn("NUM004", self._codes(hw_text))

    def test_icu001_detects_single_and_multiline_english_plural_branches(self) -> None:
        single_line = "{count, plural, one {# tệp} other {# tệp}}"
        self.assertIn("ICU001", self._codes(single_line))
        multi_line = (
            "{\n"
            '  "filesCount": "{count, plural,\n'
            "    =0 {Không có tệp nào}\n"
            "    one {1 tệp}\n"
            '    other {# tệp}}"\n'
            "}"
        )
        self.assertIn("ICU001", self._codes(multi_line))
        valid_vi_icu = "{count, plural, =0 {Không có tệp nào} other {# tệp}}"
        self.assertNotIn("ICU001", self._codes(valid_vi_icu))

    def test_pro001_and_pro002_exempt_compound_morphemes(self) -> None:
        compound_safe = (
            "Quý khách có thể chia sẻ tài liệu quý giá này với bạn bè và bạn đọc trong Quý II/2026."
        )
        self.assertNotIn("PRO001", self._codes(compound_safe))
        collision = "Kính chào Quý khách, hệ thống đã cập nhật mật khẩu của bạn."
        self.assertIn("PRO001", self._codes(collision))


class CheckFontAndI18nScriptsTests(unittest.TestCase):
    """Tests for check_font_coverage.py and check_i18n_parity.py."""

    def test_css_unicode_range_coverage_check(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            css_ok = Path(tmp) / "ok.css"
            css_ok.write_text(
                f"@font-face {{ font-family: 'Be Vietnam Pro'; unicode-range: {check_font_coverage.DEFAULT_RANGE}; }}",
                encoding="utf-8",
            )
            ranges = check_font_coverage.ranges_from_css(css_ok)
            self.assertTrue(len(ranges) > 5)

    def test_i18n_parity_checker_detects_missing_keys_and_icu_defects(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            en_path = Path(tmp) / "en.json"
            vi_path = Path(tmp) / "vi.json"
            en_path.write_text(
                json.dumps(
                    {
                        "btn.save": "Save",
                        "msg.welcome": "Hello {userName}",
                        "msg.files": "{count, plural, one {# file} other {# files}}",
                    }
                ),
                encoding="utf-8",
            )
            vi_path.write_text(
                json.dumps(
                    {
                        "btn.save": "Lưu thay đổi",
                        "msg.welcome": "Xin chào {tenNguoiDung}",
                        "msg.files": "{count, plural, one {# tệp} other {# tệp}}",
                    }
                ),
                encoding="utf-8",
            )
            findings = check_i18n_parity.compare_catalogs(en_path, vi_path)
            rules = {f["rule"] for f in findings}
            self.assertTrue(rules, f"Expected i18n parity findings, got {findings}")


class GoldenEvalPairsBenchmarkTests(unittest.TestCase):
    """Validates all golden bad/good benchmark pairs in evals/*/pairs.jsonl across all 10 skills."""

    SKILLS = (
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

    def test_all_eval_pairs_pass_bad_and_good_assertions(self) -> None:
        evals_root = REPO_ROOT / "evals"
        for skill_name in self.SKILLS:
            pairs_file = evals_root / skill_name / "pairs.jsonl"
            self.assertTrue(pairs_file.is_file(), f"Missing {pairs_file}")
            vc_mod, blocklists = _load_skill_validator(skill_name)
            lines = [
                ln.strip()
                for ln in pairs_file.read_text(encoding="utf-8").splitlines()
                if ln.strip()
            ]
            self.assertGreaterEqual(
                len(lines),
                20,
                f"{skill_name}/pairs.jsonl must have >= 20 pairs (found {len(lines)})",
            )
            for idx, line in enumerate(lines, start=1):
                row = json.loads(line)
                pair_id = row.get("id", f"{skill_name}#{idx}")
                register = row.get("register")
                doctype = row.get("doctype")
                expected_rules = set(row.get("expected_rules") or row.get("rules") or [])
                self.assertTrue(expected_rules, f"{pair_id}: expected_rules must be non-empty")

                validator = vc_mod.Validator(blocklists, register=register, doctype=doctype)

                with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f_bad:
                    f_bad.write(row["bad"])
                    bad_path = Path(f_bad.name)
                try:
                    bad_findings = validator.check_file(bad_path)
                finally:
                    bad_path.unlink(missing_ok=True)
                bad_codes = {f.rule for f in bad_findings}
                missing = expected_rules - bad_codes
                self.assertFalse(
                    missing,
                    f"{pair_id} ({skill_name}): bad text did not trigger {missing} (got {bad_codes})",
                )

                with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".md", delete=False) as f_good:
                    f_good.write(row["good"])
                    good_path = Path(f_good.name)
                try:
                    good_findings = validator.check_file(good_path)
                finally:
                    good_path.unlink(missing_ok=True)
                good_codes = {f.rule for f in good_findings}
                still_present = expected_rules & good_codes
                self.assertFalse(
                    still_present,
                    f"{pair_id} ({skill_name}): good text still triggered {still_present}",
                )


if __name__ == "__main__":
    unittest.main()
