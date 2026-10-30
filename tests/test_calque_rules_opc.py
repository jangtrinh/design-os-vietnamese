#!/usr/bin/env python3
"""Calques that real Vietnamese copy carried over from English (CAL001 rows and
context patterns, five SYN001 patterns, the warn-only CAL002 heuristic), plus
must-stay-clean fixtures: ordinary Vietnamese that shares words with a calque.
"""

from __future__ import annotations

import subprocess
import sys
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "shared" / "scripts" / "validate_copy.py"
sys.path.insert(0, str(REPO_ROOT / "shared" / "scripts"))

import validate_copy  # noqa: E402


class CalqueRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = validate_copy.Validator(validate_copy.Blocklists())

    def _findings(self, text: str):
        return self.validator.check_text(text + "\n")

    def _rules(self, text: str) -> list[str]:
        return [f.rule for f in self._findings(text)]

    # -- CAL001: literal table rows ------------------------------------------------
    def test_cal001_table_rows_flag(self) -> None:
        cases = {
            "Mình chạy trên 1 hệ thống viết ra giấy.": ["CAL001", "CAL001"],
            "Check không nằm trên đường đi thì chỉ là tài liệu.": ["CAL001"],
            "Hãy đặt lên đường đi của khách hàng.": ["CAL001"],
            "Kernel giết process vì hết RAM.": ["CAL001"],
            "Hệ thống giết tiến trình con khi thoát.": ["CAL001"],
            "Đó chỉ là một lần thử mù.": ["CAL001"],
            "Giá trị này khớp với danh tính thương hiệu.": ["CAL001"],
            "Đổi lại vậy mình đỡ tốn thời gian hơn.": ["CAL001"],
            "Team mới onboard được lên quy trình này.": ["CAL001"],
            "Mình onboard vào quy trình mới.": ["CAL001"],
            "Khoá API được giấu khỏi người dùng.": ["CAL001"],
        }
        for text, expected in cases.items():
            with self.subTest(text=text):
                self.assertEqual(self._rules(text), expected)

    def test_cal001_table_row_severity(self) -> None:
        errors = {"nằm trên đường đi", "đặt lên đường đi", "giết process", "giết tiến trình",
                  "lần thử mù", "khớp với danh tính"}
        warns = {"viết ra giấy", "đổi lại vậy", "onboard được lên", "onboard vào", "được giấu khỏi"}
        sev = {}
        for phrase in errors | warns:
            found = [f for f in self._findings(f"Ghi chú: {phrase} ở đây.") if f.rule == "CAL001"]
            self.assertTrue(found, phrase)
            sev[phrase] = found[0].severity
        for phrase in errors:
            self.assertEqual(sev[phrase], validate_copy.ERROR, phrase)
        for phrase in warns:
            self.assertEqual(sev[phrase], validate_copy.WARN, phrase)

    # -- CAL001: context-restricted patterns (WARN) --------------------------------
    def test_cal001_context_patterns_flag_as_warn(self) -> None:
        cases = (
            "Mình chạy trên một hệ thống riêng.",
            "Check này có mặt trong repo.",
            "Cần giữ vững chất lượng của skill.",
            "An toàn đứng trên tốc độ.",
            "Trạng thái nằm trong file config.",
            "Chất lượng không thương lượng.",
            "Đây là bài toán mình đang sống cùng.",
            "Mọi bước đi qua cùng 1 dòng chảy.",
            "Đạt 7 trên 11.",
            "Qua 7 trên 11 lần thử.",
        )
        for text in cases:
            with self.subTest(text=text):
                found = self._findings(text)
                self.assertEqual([f.rule for f in found], ["CAL001"], text)
                self.assertEqual(found[0].severity, validate_copy.WARN)

    # -- SYN001 ---------------------------------------------------------------------
    def test_five_new_syn001_patterns_flag(self) -> None:
        cases = (
            "Chỉ vì mình lười nên là việc này bị bỏ.",
            "Không ai ship được mà không review.",
            "Luật nằm trong đầu mỗi người.",
            "Quy tắc nằm ở đâu đó trong team.",
            "Bài viết bắt đầu bằng việc giải thích vấn đề.",
            "Quy trình kết thúc bằng việc gửi báo cáo.",
            "Ai cần xem log thì bị chuyển sang trang khác.",
        )
        for text in cases:
            with self.subTest(text=text):
                self.assertEqual(self._rules(text), ["SYN001"])
                self.assertEqual(self._findings(text)[0].severity, validate_copy.WARN)

    # -- CAL002 ---------------------------------------------------------------------
    def test_cal002_flags_stacked_abstract_metaphors_as_warn(self) -> None:
        text = "Mình giữ danh tính và đặt vị trí trên tầng cao."
        found = self._findings(text)
        self.assertEqual([f.rule for f in found], ["CAL002"])
        self.assertEqual(found[0].severity, validate_copy.WARN)

    def test_cal002_needs_two_distinct_abstract_nouns_and_no_concrete_object(self) -> None:
        self.assertNotIn("CAL002", self._rules("Mình giữ danh tính thương hiệu."))
        for text in (
            "Mình giữ danh tính và đặt vị trí trên tầng 3.",
            "Mình giữ danh tính và đặt vị trí trong file brand.md.",
        ):
            with self.subTest(text=text):
                self.assertNotIn("CAL002", self._rules(text))
        # Two sentences with one phrase each is not stacking.
        self.assertNotIn("CAL002", self._rules("Mình giữ danh tính. Mình đặt vị trí rõ ràng."))

    def test_cal002_is_disabled_by_casual_chat_context(self) -> None:
        text = "Mình giữ danh tính và đặt vị trí trên tầng cao.\n"
        for preset, expect_rule in (("chat-close-friend", False), ("chat-colleague", False), ("chat-to-manager", True)):
            with self.subTest(preset=preset):
                r = subprocess.run(
                    [sys.executable, str(SCRIPT), "--context", preset, "-"],
                    input=text, capture_output=True, text=True, check=False,
                )
                self.assertEqual("CAL002" in r.stdout, expect_rule, r.stdout + r.stderr)

    def test_cal002_is_a_warning_so_default_exit_is_zero(self) -> None:
        text = "Mình giữ danh tính và đặt vị trí trên tầng cao.\n"
        default = subprocess.run([sys.executable, str(SCRIPT), "-"], input=text,
                                 capture_output=True, text=True, check=False)
        strict = subprocess.run([sys.executable, str(SCRIPT), "--strict", "-"], input=text,
                                capture_output=True, text=True, check=False)
        self.assertEqual(default.returncode, 0, default.stdout)
        self.assertIn("CAL002", default.stdout)
        self.assertNotEqual(strict.returncode, 0)  # --strict fails on any warning

    def test_cal002_is_documented(self) -> None:
        self.assertIn("CAL002", validate_copy.RULE_DOCS)
        r = subprocess.run([sys.executable, str(SCRIPT), "--list-rules"],
                           capture_output=True, text=True, check=False)
        self.assertIn("CAL002", r.stdout)

    # -- must stay clean --------------------------------------------------------------
    def test_legitimate_vietnamese_stays_clean(self) -> None:
        clean = (
            "Chị ấy có mặt ở buổi họp.",
            "Anh Nam có mặt đúng giờ.",
            "Giữ vững tinh thần.",
            "Đội giữ vững lập trường đến cuối.",
            "Thuê nhà trên đường Lê Lợi.",
            "Căn hộ nằm trên tầng 12.",
            "Quán nằm trong hẻm nhỏ.",
            "Giá không thương lượng.",
            "Dòng chảy của sông Hồng rất mạnh.",
            "Cá bơi ngược dòng chảy.",
            "Đạt hạng 7 trên 11.5 điểm.",
            "Tỉ lệ 3 trên 1000 là rất thấp.",
            "Anh ấy đứng trên bục phát biểu.",
            "Cô ấy giữ chìa khoá và mang theo ví.",
            "Đặt vé trên app Grab.",
            "Chạy trên Linux và macOS.",
        )
        for text in clean:
            with self.subTest(text=text):
                flagged = [f for f in self._findings(text) if f.rule in ("CAL001", "CAL002", "SYN001")]
                self.assertEqual(flagged, [], text)

    def test_literal_rows_keep_their_documented_strictness(self) -> None:
        # “viết ra giấy” can be literal (paper notes), so the row warns instead of failing the build.
        found = [f for f in self._findings("Hãy viết ra giấy nháp trước khi tính.") if f.rule == "CAL001"]
        self.assertEqual([f.severity for f in found], [validate_copy.WARN])

    def test_inline_disable_silences_the_new_rules(self) -> None:
        for rule, text in (
            ("CAL001", "Mình chạy trên 1 hệ thống riêng. <!-- vlc-disable-line: CAL001 -->"),
            ("SYN001", "Bài viết bắt đầu bằng việc giải thích. <!-- vlc-disable-line: SYN001 -->"),
            ("CAL002", "Mình giữ danh tính và đặt vị trí trên tầng cao. <!-- vlc-disable-line: CAL002 -->"),
        ):
            with self.subTest(rule=rule):
                self.assertNotIn(rule, self._rules(text))


if __name__ == "__main__":
    unittest.main()
