#!/usr/bin/env python3
"""CLI tests for the writing-context dimension (``--context <preset>``, rules CTX001-CTX005).

Every CLI call goes through ``cli()``, which asserts the exact exit code and the
absence of a traceback; each test then asserts the payload. Everything is offline
and stdlib-only.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import unicodedata
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared" / "scripts" / "validate_copy.py"
SKILL_SCRIPTS = sorted((ROOT / "skills").glob("*/scripts/validate_copy.py"))

PRESETS = (
    "chat-close-friend",
    "chat-colleague",
    "chat-to-manager",
    "email-to-manager",
    "email-to-colleague",
    "email-to-team",
    "email-to-client",
    "job-application",
    "doc-for-executives",
    "doc-for-engineers",
)
CTX_RULES = ("CTX001", "CTX002", "CTX003", "CTX004", "CTX005")

# One representative defect per rule, each in a context where that rule is enabled.
BOSS_BAD_PRONOUN = "Kính gửi anh Nam,\n\nBạn xem giúp em báo cáo này nhé ạ.\n\nTrân trọng,\nLan\n"
BOSS_NO_PARTICLE = "Chào anh Nam,\n\nEm gửi anh báo cáo tuần này, anh xem giúp em.\n\nTrân trọng,\nLan\n"
BOSS_TEENCODE = "Kính gửi anh Nam,\n\nEm gửi anh báo cáo tuần này ạ, mai anh rảnh ko ạ?\n\nTrân trọng,\nLan\n"
EMAIL_NO_FRAME = "Em gửi anh báo cáo tuần này ạ, anh xem giúp em.\n"
BOSS_GOOD = "Kính gửi anh Nam,\n\nEm gửi anh báo cáo tuần này ạ. Anh xem giúp em nhé ạ.\n\nTrân trọng,\nLan\n"
EXEC_NO_SUMMARY = (
    "# Báo cáo quý 3\n\nDoanh thu tăng trưởng đều ở các thị trường chính.\n"
    "Chi phí vận hành được kiểm soát tốt trong ba tháng.\nBộ phận kỹ thuật hoàn thành bảy hạng mục.\n"
)
EXEC_WITH_SUMMARY = "# Báo cáo quý 3\n\n## Tóm tắt\n\nDoanh thu tăng 12% so với quý trước.\n"
FRIEND_TEENCODE = "ko biết nha mn, tối nay ae đi ăn ko, mai tao dc nghỉ r\n"


def cli(tc: unittest.TestCase, script: pathlib.Path, *args: str, stdin: str = "", code: int):
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        input=stdin, capture_output=True, text=True, cwd=str(ROOT),
    )
    tc.assertNotIn("Traceback", proc.stderr, proc.stderr)
    tc.assertEqual(proc.returncode, code, f"{args}\nstdout={proc.stdout}\nstderr={proc.stderr}")
    return proc


def findings(proc: subprocess.CompletedProcess) -> list:
    return json.loads(proc.stdout)["findings"]


def rules_of(proc: subprocess.CompletedProcess) -> set:
    return {f["rule"] for f in findings(proc)}


class ContextCliTests(unittest.TestCase):
    def test_list_rules_shows_every_ctx_rule_with_and_without_domain(self) -> None:
        for extra in ([], ["--domain", "all"], ["--domain", "finance"]):
            with self.subTest(extra=extra):
                r = cli(self, SHARED, "--list-rules", *extra, code=0)
                listed = {line.split()[0] for line in r.stdout.splitlines() if line.strip()}
                for rule in CTX_RULES:
                    self.assertIn(rule, listed)

    def test_unknown_context_exits_two_and_lists_every_preset(self) -> None:
        r = cli(self, SHARED, "--context", "chat-with-aliens", "-", stdin="Xin chào.\n", code=2)
        self.assertIn("unknown context 'chat-with-aliens'", r.stderr)
        for preset in PRESETS:
            self.assertIn(preset, r.stderr)
        self.assertEqual(r.stdout, "")

    def test_ctx001_forbidden_address_to_manager_is_an_error(self) -> None:
        r = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=BOSS_BAD_PRONOUN, code=1)
        hit = [f for f in findings(r) if f["rule"] == "CTX001"]
        self.assertEqual(len(hit), 1)
        self.assertEqual(hit[0]["severity"], "error")
        self.assertEqual(hit[0]["text"], "Bạn")

    def test_ctx001_is_only_a_warning_outside_up_contexts(self) -> None:
        r = cli(self, SHARED, "--json", "--context", "chat-close-friend", "-",
                stdin="Quý khách vui lòng đợi mình một chút nhé.\n", code=0)
        self.assertEqual([(f["rule"], f["severity"]) for f in findings(r)], [("CTX001", "warning")])

    def test_ctx002_missing_politeness_particle_is_a_warning_and_strict_fails_it(self) -> None:
        r = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=BOSS_NO_PARTICLE, code=0)
        self.assertEqual([(f["rule"], f["severity"]) for f in findings(r)], [("CTX002", "warning")])
        strict = cli(self, SHARED, "--json", "--strict", "--context", "email-to-manager", "-",
                     stdin=BOSS_NO_PARTICLE, code=1)
        self.assertEqual(rules_of(strict), {"CTX002"})

    def test_ctx003_chat_abbreviation_severity_follows_the_context(self) -> None:
        up = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=BOSS_TEENCODE, code=1)
        self.assertEqual([(f["rule"], f["severity"], f["text"]) for f in findings(up)], [("CTX003", "error", "ko")])
        peer = cli(self, SHARED, "--json", "--context", "email-to-colleague", "-",
                   stdin="Chào An,\n\nMai bạn rảnh ko?\n\nThân,\nBình\n", code=0)
        self.assertEqual([(f["rule"], f["severity"]) for f in findings(peer)], [("CTX003", "warning")])

    def test_ctx003_does_not_fire_inside_words_locale_codes_or_after_numbers(self) -> None:
        text = "Kính gửi anh Nam,\n\nEm đã thêm ngôn ngữ ko-KR và đo 5 ns, nhóm k8s xong rồi ạ.\n\nTrân trọng,\nLan\n"
        r = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=text, code=0)
        self.assertEqual(findings(r), [])

    def test_ctx004_email_without_greeting_and_sign_off(self) -> None:
        r = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=EMAIL_NO_FRAME, code=0)
        self.assertEqual([f["rule"] for f in findings(r)], ["CTX004", "CTX004"])

    def test_ctx005_executive_doc_needs_a_summary_in_the_opening_lines(self) -> None:
        bad = cli(self, SHARED, "--json", "--context", "doc-for-executives", "-", stdin=EXEC_NO_SUMMARY, code=0)
        self.assertEqual([f["rule"] for f in findings(bad)], ["CTX005"])
        good = cli(self, SHARED, "--json", "--context", "doc-for-executives", "-", stdin=EXEC_WITH_SUMMARY, code=0)
        self.assertEqual(findings(good), [])

    def test_good_email_is_clean(self) -> None:
        r = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=BOSS_GOOD, code=0)
        self.assertEqual(findings(r), [])

    def test_casual_chat_relaxes_unsuitable_rules_but_keeps_real_defects(self) -> None:
        text = "cam on nha, quán này rẻ nhất Sài Gòn, số 1 luôn\n"
        plain = cli(self, SHARED, "--json", "-", stdin=text, code=0)
        self.assertEqual(rules_of(plain), {"DIA001", "LAW001"})
        relaxed = cli(self, SHARED, "--json", "--context", "chat-close-friend", "-",
                      stdin=FRIEND_TEENCODE + text, code=0)
        self.assertEqual(findings(relaxed), [])
        mixed = cli(self, SHARED, "--json", "--context", "chat-close-friend", "-",
                    stdin="Quý khách ơi, bạn nhớ mang theo ví nhé.\n", code=0)
        self.assertEqual(rules_of(mixed), {"CTX001", "PRO001"})
        broken = cli(self, SHARED, "--json", "--context", "chat-close-friend", "-",
                     stdin=unicodedata.normalize("NFD", "tối nay đi ăn không\n"), code=1)
        self.assertEqual(rules_of(broken), {"NFC001"})

    def test_composes_with_domain_register_and_inline_disable(self) -> None:
        text = "Kính gửi anh Nam,\n\nBạn xem giúp em ạ. Cam kết lợi nhuận 18%/năm ạ.\n\nTrân trọng,\nLan\n"
        r = cli(self, SHARED, "--json", "--context", "email-to-manager", "--domain", "finance",
                "--register", "b2b", "-", stdin=text, code=1)
        self.assertTrue({"CTX001", "FIN001", "PRO002"} <= rules_of(r), rules_of(r))
        off = cli(self, SHARED, "--json", "--context", "email-to-manager", "-",
                  stdin=BOSS_BAD_PRONOUN.replace("nhé ạ.", "nhé ạ. <!-- vlc-disable-line: CTX001 -->"), code=0)
        self.assertEqual(findings(off), [])

    def test_without_context_no_ctx_rule_ever_fires(self) -> None:
        for text in (BOSS_BAD_PRONOUN, BOSS_TEENCODE, EMAIL_NO_FRAME, EXEC_NO_SUMMARY, FRIEND_TEENCODE):
            r = cli(self, SHARED, "--json", "-", stdin=text, code=0)
            self.assertFalse(rules_of(r) & set(CTX_RULES))

    def test_suggestion_goes_to_stderr_only_and_never_changes_stdout_or_exit_code(self) -> None:
        text = "Kính gửi anh Nam,\n\nEm xin báo cáo tiến độ tuần này.\n\nTrân trọng,\nLan\n"
        plain = cli(self, SHARED, "--json", "-", stdin=text, code=0)
        self.assertIn("email-to-manager", plain.stderr)
        self.assertEqual(json.loads(plain.stdout)["findings"], [])
        self.assertNotIn("email-to-manager", plain.stdout)
        declared = cli(self, SHARED, "--json", "--context", "email-to-manager", "-", stdin=text, code=0)
        self.assertEqual(declared.stderr, "")
        self.assertEqual(findings(declared), [])
        job = cli(self, SHARED, "-",
                  stdin="Kính gửi anh/chị,\n\nEm xin ứng tuyển vị trí Kế toán.\n\nTrân trọng,\nLan\n", code=0)
        self.assertIn("job-application", job.stderr)
        self.assertIn("clean", job.stdout)
        quiet = cli(self, SHARED, "-", stdin="Xin chào bạn, chúc một ngày tốt lành.\n", code=0)
        self.assertEqual(quiet.stderr, "")
        self.assertIn("clean", quiet.stdout)
        # "CV" in an official-letter number (công văn) is not a curriculum vitae.
        cong_van = cli(self, SHARED, "-",
                       stdin="Số: 12/CV-ABC\n\nKính gửi: Sở Thông tin và Truyền thông\n\nChúng tôi gửi công văn đề xuất hợp tác.\n",
                       code=0)
        self.assertEqual(cong_van.stderr, "")
        self.assertIn("clean", cong_van.stdout)

    def test_every_skill_copy_runs_the_context(self) -> None:
        self.assertEqual(len(SKILL_SCRIPTS), 16)
        for script in SKILL_SCRIPTS:
            with self.subTest(script=script.parent.parent.name):
                r = cli(self, script, "--json", "--context", "email-to-manager", "-", stdin=BOSS_BAD_PRONOUN, code=1)
                self.assertIn("CTX001", rules_of(r))
                ls = cli(self, script, "--list-rules", code=0)
                for rule in CTX_RULES:
                    self.assertIn(rule, ls.stdout)


if __name__ == "__main__":
    unittest.main()
