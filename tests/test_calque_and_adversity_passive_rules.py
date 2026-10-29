#!/usr/bin/env python3
"""CAL001 / SYN001 must catch the calque patterns the README advertises:
"Làm ơn + verb", "của bạn" placed before the noun after a verb, and the adversity
passive "bị" paired with a positive outcome ("bị hủy thành công", "bị nâng cấp").
Also guards against false positives on legitimate Vietnamese.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "shared" / "scripts"))

import validate_copy  # noqa: E402


class CalqueAndAdversityPassiveTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = validate_copy.Validator(validate_copy.Blocklists())

    def _rules(self, text: str) -> list[str]:
        return [f.rule for f in self.validator.check_text(text + "\n")]

    # -- CAL001: "Làm ơn" + verb ------------------------------------------------
    def test_lam_on_plus_ui_verb_flags_cal001(self) -> None:
        for text in (
            "Làm ơn nhập của bạn mật khẩu.",
            "Làm ơn nhập mật khẩu.",
            "Làm ơn đợi trong giây lát.",
            "Làm ơn xác nhận email.",
            "Làm ơn thử lại.",
        ):
            with self.subTest(text=text):
                self.assertEqual(self._rules(text), ["CAL001"])

    def test_lam_on_idiom_and_favour_sense_do_not_flag(self) -> None:
        for text in (
            "Làm ơn mắc oán là câu tục ngữ quen thuộc.",
            "Anh ấy từng làm ơn cho cả xóm.",
        ):
            with self.subTest(text=text):
                self.assertNotIn("CAL001", self._rules(text))

    # -- CAL001: "của bạn" before the noun --------------------------------------
    def test_cua_ban_before_noun_after_verb_flags_cal001(self) -> None:
        for text in (
            "Vui lòng nhập của bạn mật khẩu.",
            "Vui lòng nhập của bạn email.",
            "Xem của bạn đơn hàng.",
            "Chọn của bạn gói dịch vụ.",
        ):
            with self.subTest(text=text):
                self.assertEqual(self._rules(text), ["CAL001"])

    def test_single_cal001_per_span_when_table_and_pattern_overlap(self) -> None:
        self.assertEqual(self._rules("Làm ơn nhập của bạn mật khẩu."), ["CAL001"])
        self.assertEqual(self._rules("Vui lòng nhập của bạn tài khoản."), ["CAL001"])
        # Two distinct defects ("Please" calque + inverted possessive) stay two findings.
        self.assertEqual(self._rules("Làm ơn nhập của bạn email."), ["CAL001", "CAL001"])

    # -- SYN001: adversity passive + positive outcome ---------------------------
    def test_bi_with_positive_outcome_flags_syn001(self) -> None:
        for text in (
            "Đơn hàng của bạn đã bị hủy thành công.",
            "Tài khoản bị nâng cấp thành công.",
            "Gói dịch vụ bị nâng cấp.",
            "Nhân viên bị thăng chức.",
        ):
            with self.subTest(text=text):
                self.assertEqual(self._rules(text), ["SYN001"])

    # -- False positives --------------------------------------------------------
    def test_legitimate_vietnamese_does_not_flag(self) -> None:
        for text in (
            "Mời bạn bè cùng dùng thử.",
            "Gửi ý kiến cho bạn đọc.",
            "Kết bạn với người dùng khác.",
            "Xóa không gian làm việc của bạn?",
            "Vui lòng nhập mật khẩu của bạn.",
            "Đơn hàng của bạn đã được hủy.",
            "Đơn hàng đã được hủy.",
            "Đơn hàng bị hủy do hết hàng.",
            "Tài khoản bị khóa.",
            "Tài khoản không bị nâng cấp.",
            "Đơn hàng bị lỗi, thanh toán thành công.",
            "Gửi không thành công.",
            "Quý I đạt mục tiêu.",
            "Một món quà quý giá.",
            "Xem tài khoản của bạn đã được nâng cấp.",
        ):
            with self.subTest(text=text):
                self.assertEqual(self._rules(text), [])

    # -- Every skill ships the same behaviour -----------------------------------
    def test_every_skill_validator_reports_same_rules(self) -> None:
        sentences = {
            "Làm ơn nhập của bạn mật khẩu.": "CAL001",
            "Vui lòng nhập của bạn mật khẩu.": "CAL001",
            "Đơn hàng của bạn đã bị hủy thành công.": "SYN001",
            "Tài khoản bị nâng cấp thành công.": "SYN001",
        }
        scripts = sorted((REPO_ROOT / "skills").glob("*/scripts/validate_copy.py"))
        self.assertTrue(scripts)
        with tempfile.TemporaryDirectory() as tmp:
            for text, expected in sentences.items():
                sample = Path(tmp) / "sample.md"
                sample.write_text(text + "\n", encoding="utf-8")
                for script in scripts:
                    with self.subTest(skill=script.parts[-3], text=text):
                        proc = subprocess.run(
                            [sys.executable, str(script), str(sample)],
                            capture_output=True, text=True, check=False,
                        )
                        self.assertIn(expected, proc.stdout, proc.stdout + proc.stderr)


if __name__ == "__main__":
    unittest.main()
