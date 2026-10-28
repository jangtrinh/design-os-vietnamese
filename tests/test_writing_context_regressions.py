#!/usr/bin/env python3
"""Regression tests for false positives and gaps found by the independent review.

Each CLI call asserts the exact exit code, the absence of a traceback and the
payload. Templates vary on purpose (openers, closers, signature blocks) so the
rules are not tuned to one letter. Offline and stdlib-only.
"""
from __future__ import annotations

import json
import pathlib
import re
import subprocess
import sys
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared" / "scripts" / "validate_copy.py"
MATRIX = ROOT / "shared" / "references" / "context-matrix.md"


def run(tc: unittest.TestCase, *args: str, stdin: str = "", code: int, script: pathlib.Path = SHARED):
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        input=stdin, capture_output=True, text=True, cwd=str(ROOT),
    )
    tc.assertNotIn("Traceback", proc.stderr, proc.stderr)
    tc.assertEqual(proc.returncode, code, f"{args}\nstdout={proc.stdout}\nstderr={proc.stderr}")
    return proc


def findings(tc: unittest.TestCase, context: str, text: str, *, code: int = 0, extra=()) -> list:
    proc = run(tc, "--json", "--context", context, *extra, "-", stdin=text, code=code)
    return json.loads(proc.stdout)["findings"]


def rules(tc: unittest.TestCase, context: str, text: str, *, code: int = 0) -> list:
    return [(f["rule"], f["text"]) for f in findings(tc, context, text, code=code)]


class PronounGuardTests(unittest.TestCase):
    def test_het_minh_and_ve_phan_minh_are_idioms_not_pronouns(self) -> None:
        self.assertEqual(rules(self, "chat-to-manager", "Em sẽ cố gắng hết mình cho dự án này ạ.\n"), [])
        letter = "Kính gửi anh/chị,\n\nVề phần mình, tôi sẵn sàng làm việc hết mình.\n\nTrân trọng,\nAn\n"
        self.assertEqual(rules(self, "job-application", letter), [])
        client = "Kính gửi anh Hùng,\n\nChúng tôi đã làm hết mình để kịp tiến độ.\n\nTrân trọng,\nMai\n"
        self.assertEqual(rules(self, "email-to-client", client), [])

    def test_reflexive_cua_minh_after_a_first_person_subject_is_fine(self) -> None:
        letter = "Kính gửi anh/chị,\n\nTôi tin rằng kinh nghiệm của mình sẽ giúp ích cho Quý công ty.\n\nTrân trọng,\nAn\n"
        self.assertEqual(rules(self, "job-application", letter), [])
        chat = "Anh ơi, em đã kiểm tra lại phần việc của mình rồi ạ.\n"
        self.assertEqual(rules(self, "chat-to-manager", chat), [])

    def test_cua_minh_without_a_first_person_subject_is_still_flagged(self) -> None:
        got = rules(self, "chat-to-manager", "Sếp gửi giúp file của mình ạ.\n", code=1)
        self.assertEqual(got, [("CTX001", "mình")])

    def test_third_person_ban_noun_phrases_are_not_direct_address(self) -> None:
        letter = "Kính gửi anh/chị,\n\nTôi từng hướng dẫn các bạn thực tập sinh trong nhóm.\n\nTrân trọng,\nAn\n"
        self.assertEqual(rules(self, "job-application", letter), [])
        report = "Kính gửi anh Nam,\n\nEm đã nhờ bạn Lan hỗ trợ phần dữ liệu ạ.\n\nTrân trọng,\nHà\n"
        self.assertEqual(rules(self, "email-to-manager", report), [])

    def test_direct_address_ban_and_minh_are_still_errors(self) -> None:
        got = rules(self, "email-to-manager", "Chào sếp,\n\nBạn xem giúp mình nhé ạ.\n\nThân,\nHà\n", code=1)
        self.assertEqual(got, [("CTX001", "Bạn"), ("CTX001", "mình")])


class QuotedReplyTests(unittest.TestCase):
    BODY = "Kính gửi anh Hùng,\n\nTôi đã nhận được phản hồi và sẽ gửi báo giá mới trong hôm nay.\n\nTrân trọng,\nMai\n\n"
    QUOTED = "> Chào bạn,\n> Bên mình cần báo giá lại cho 200 bộ bàn ghế.\n> Bạn gửi sớm giúp mình nhé, tuần sau mình chốt.\n> Hùng\n"

    def test_every_quote_marker_cuts_the_body(self) -> None:
        markers = (
            "Vào Thứ Ba, 28/10/2026, Lê Hùng đã viết:\n",
            "On Tue, 28 Oct 2026, Hung Le wrote:\n",
            "-----Original Message-----\n",
            "----- Tin nhắn gốc -----\n",
            "",
        )
        for marker in markers:
            with self.subTest(marker=marker.strip()):
                self.assertEqual(rules(self, "email-to-client", self.BODY + marker + self.QUOTED), [])

    def test_unquoted_text_after_a_marker_line_is_also_cut(self) -> None:
        text = self.BODY + "Vào 28/10/2026, Lê Hùng đã viết:\nChào bạn, bên mình cần báo giá lại.\n"
        self.assertEqual(rules(self, "email-to-client", text), [])

    def test_quoted_thanks_never_counts_as_the_sign_off(self) -> None:
        text = "Kính gửi anh Hùng,\n\nTôi gửi anh báo giá đính kèm.\n\n> Cảm ơn em.\n> Hùng\n"
        got = findings(self, "email-to-client", text)
        self.assertEqual([(f["rule"], f["line"]) for f in got], [("CTX004", 3)])
        self.assertIn("sign-off", got[0]["message"])

    def test_a_real_sign_off_survives_a_long_quoted_thread(self) -> None:
        thread = "".join(f"> trích dẫn dòng {i}\n" for i in range(30))
        self.assertEqual(rules(self, "email-to-client", self.BODY + "On Tue, Hung Le wrote:\n" + thread), [])

    def test_document_blockquotes_are_the_writers_own_text(self) -> None:
        doc = "> Tóm tắt: nên chọn nhà cung cấp B.\n\n# Đánh giá nhà cung cấp\n\nChi tiết nằm ở phụ lục.\n"
        self.assertEqual(rules(self, "doc-for-executives", doc), [])


class AbbreviationGuardTests(unittest.TestCase):
    def test_email_addresses_and_file_names_are_not_teencode(self) -> None:
        signature = (
            "Kính gửi anh Nam,\n\nEm gửi anh file ạ.\n\nTrân trọng,\nLan\n"
            "Email: j.doe@abc.vn\nk.nguyen@abc.vn\nhttps://abc.vn/r/k\n"
        )
        self.assertEqual(rules(self, "email-to-manager", signature), [])
        self.assertEqual(rules(self, "chat-to-manager", "Anh ơi, em đã đổi tên file thành r.py như anh dặn ạ.\n"), [])

    def test_sentence_final_abbreviation_is_still_caught(self) -> None:
        got = rules(self, "chat-to-manager", "Anh ơi, em xong việc r. Em báo anh ạ.\n")
        self.assertEqual(got, [("CTX003", "r")])

    def test_vs_and_math_letters_are_not_flagged_in_documents(self) -> None:
        vs_doc = "# Báo cáo\n\n## Tóm tắt\n\nDoanh thu tháng này vs tháng trước tăng mạnh.\n"
        self.assertEqual(rules(self, "doc-for-executives", vs_doc), [])
        corr = "# Phân tích hiệu quả quảng cáo\n\n## Kết luận\n\nHệ số tương quan r giữa chi phí quảng cáo và doanh thu là 0,82.\n"
        self.assertEqual(rules(self, "doc-for-executives", corr), [])

    def test_vs_hint_offers_so_voi_not_only_voi(self) -> None:
        text = "Chào An,\n\nSo sánh A vs B giúp mình nhé.\n\nCảm ơn,\nBình\n"
        got = findings(self, "email-to-colleague", text)
        self.assertEqual([f["rule"] for f in got], ["CTX003"])
        self.assertIn("so với", got[0]["hint"])
        self.assertIn("với", got[0]["hint"])

    def test_all_caps_teencode_and_extra_tokens_are_caught(self) -> None:
        self.assertEqual(rules(self, "chat-to-manager", "Anh ơi KO kịp ạ.\n"), [("CTX003", "KO")])
        self.assertEqual(rules(self, "chat-to-manager", "Anh ơi ĐC rồi ạ.\n"), [("CTX003", "ĐC")])
        kn = "Kính gửi anh/chị,\n\nEm có 2 năm kn kế toán. Mong a/c phản hồi.\n\nTrân trọng,\nLan\n"
        self.assertEqual([t for _r, t in rules(self, "job-application", kn, code=1)], ["kn", "a/c"])

    def test_tui_is_a_forbidden_self_term_toward_a_superior(self) -> None:
        self.assertEqual(rules(self, "chat-to-manager", "Sếp ơi, tui xin nghỉ một buổi ạ.\n", code=1), [("CTX001", "tui")])
        self.assertEqual(rules(self, "chat-close-friend", "tui đi trước nha\n"), [])


class EmailFrameTests(unittest.TestCase):
    def test_wider_openers_and_closers_are_accepted(self) -> None:
        cases = (
            ("email-to-manager", "Thưa anh,\n\nEm xin báo cáo tiến độ dự án CRM ạ.\n\nEm cảm ơn anh ạ.\nHà\n"),
            ("email-to-manager", "Dạ chào anh,\n\nEm gửi anh file ạ.\n\nEm cám ơn anh.\nHà\n"),
            ("email-to-manager", "Dạ thưa anh,\n\nEm gửi anh file ạ.\n\nBest,\nHà\n"),
            ("job-application", "Kính thưa anh/chị,\n\nTôi xin ứng tuyển vị trí Kế toán.\n\nTôi xin chân thành cảm ơn anh/chị.\nLan\n"),
            ("email-to-colleague", "Anh Tuấn thân mến,\n\nMình gửi anh bản nháp nhé.\n\nThân,\nHà\n"),
            ("email-to-colleague", "Chị Hoa thân mến,\n\nMình gửi chị bản nháp nhé.\n\nCám ơn chị,\nHà\n"),
        )
        for ctx, text in cases:
            with self.subTest(ctx=ctx, opener=text.splitlines()[0]):
                self.assertEqual(rules(self, ctx, text), [])

    def test_sign_off_is_found_above_a_long_signature_block(self) -> None:
        text = (
            "Kính gửi chị Lan,\n\nEm gửi chị kế hoạch quý IV ạ.\n\nTrân trọng,\nNguyễn Văn Minh\n"
            "Chuyên viên Kế hoạch\nPhòng Kinh doanh\nCông ty Cổ phần ABC\nĐiện thoại: 0912 345 678\nEmail: minh.nv@abc.vn\n"
        )
        self.assertEqual(rules(self, "email-to-manager", text), [])

    def test_missing_sign_off_is_still_reported_with_a_signature_block(self) -> None:
        text = (
            "Kính gửi chị Lan,\n\nEm gửi chị kế hoạch quý IV ạ.\n\nNguyễn Văn Minh\n"
            "Chuyên viên Kế hoạch\nPhòng Kinh doanh\nCông ty Cổ phần ABC\nĐiện thoại: 0912 345 678\nEmail: minh.nv@abc.vn\n"
        )
        got = findings(self, "email-to-manager", text)
        self.assertEqual([f["rule"] for f in got], ["CTX004"])
        self.assertIn("sign-off", got[0]["message"])

    def test_vv_subject_line_is_skipped_when_looking_for_the_greeting(self) -> None:
        text = "V/v: Báo cáo tuần 43\n\nKính gửi anh Nam,\n\nEm gửi anh báo cáo ạ.\n\nTrân trọng,\nLan\n"
        self.assertEqual(rules(self, "email-to-manager", text), [])

    def test_formal_opener_needs_no_politeness_particle(self) -> None:
        for opener in ("Kính gửi anh Tuấn,", "Kính thưa anh Tuấn,", "Thưa anh Tuấn,"):
            with self.subTest(opener=opener):
                text = f"{opener}\n\nEm xin gửi anh báo cáo tháng 9. Kính mong anh xem xét và cho ý kiến.\n\nTrân trọng,\nHà\n"
                self.assertEqual(rules(self, "email-to-manager", text), [])

    def test_casual_opener_without_a_particle_is_still_flagged(self) -> None:
        text = "Chào anh Tuấn,\n\nEm gửi anh báo cáo tháng 9, anh xem giúp em.\n\nThân,\nHà\n"
        self.assertEqual([r for r, _t in rules(self, "email-to-manager", text)], ["CTX002"])


class ExecutiveSummaryTests(unittest.TestCase):
    def test_de_nghi_and_kien_nghi_count_as_the_conclusion(self) -> None:
        de_nghi = "# Tờ trình về việc lựa chọn nhà cung cấp phần mềm\n\nKính gửi: Ban Giám đốc\n\nĐề nghị Ban Giám đốc phê duyệt lựa chọn nhà cung cấp B với chi phí 1,8 tỷ đồng.\n"
        self.assertEqual(rules(self, "doc-for-executives", de_nghi), [])
        kien_nghi = "# Báo cáo quý 3\n\n## Kiến nghị\n\nTăng ngân sách marketing thêm 10%.\n"
        self.assertEqual(rules(self, "doc-for-executives", kien_nghi), [])
        tom_lai = "# Báo cáo quý 3\n\nTóm lại, doanh thu tăng 12% so với quý trước.\n"
        self.assertEqual(rules(self, "doc-for-executives", tom_lai), [])


class SuggestionTests(unittest.TestCase):
    def hint(self, text: str, *args: str, script: pathlib.Path = SHARED) -> str:
        return run(self, *args, "-", stdin=text, code=0, script=script).stderr

    def test_meta_text_about_pronouns_does_not_hint(self) -> None:
        for text in (
            'Bài viết hướng dẫn: tránh dùng "mày" và "tao" trong email công việc.\n',
            "Quy tắc: không dùng `mày` hoặc `tao` khi viết cho cấp trên; hãy xưng em.\n",
            "Trong chat bạn thân, người ta hay xưng tao và gọi mày, nhưng văn bản công việc thì không.\n",
        ):
            with self.subTest(text=text[:30]):
                self.assertEqual(self.hint(text), "")

    def test_notices_to_candidates_and_customers_do_not_hint(self) -> None:
        hr = "Kính gửi các ứng viên,\n\nCông ty ABC trân trọng thông báo kết quả vòng hồ sơ ứng tuyển vị trí Kế toán tổng hợp.\n\nTrân trọng,\nPhòng Nhân sự\n"
        self.assertEqual(self.hint(hr), "")
        cs = "Kính gửi anh/chị,\n\nEm là Linh, nhân viên chăm sóc khách hàng của ABC. Em xin thông báo đơn hàng của anh/chị đã được giao.\n"
        self.assertEqual(self.hint(cs), "")

    def test_hint_requires_the_pattern_at_the_start_of_the_text(self) -> None:
        late = "# Mẫu thư\n\nVí dụ bên dưới.\n\nKính gửi anh Nam,\n\nEm xin báo cáo tiến độ ạ.\n"
        self.assertEqual(self.hint(late), "")

    def test_a_declared_register_silences_the_hint(self) -> None:
        text = "Kính gửi anh Nam,\n\nEm xin báo cáo tiến độ tuần này.\n\nTrân trọng,\nLan\n"
        self.assertIn("email-to-manager", self.hint(text))
        self.assertEqual(self.hint(text, "--register", "b2b"), "")

    def test_real_signals_still_hint(self) -> None:
        self.assertIn("job-application", self.hint("Kính thưa anh/chị,\n\nTôi xin ứng tuyển vị trí Kế toán tổng hợp.\n\nTrân trọng,\nAn\n"))
        self.assertIn("chat-close-friend", self.hint("Mày đi không? Tao đợi ở cổng nhé.\n"))

    def test_no_markdown_file_in_the_repository_triggers_a_hint(self) -> None:
        sys.path.insert(0, str(ROOT / "shared" / "scripts"))
        try:
            import validate_copy
        finally:
            sys.path.pop(0)
        blocklists = validate_copy.Blocklists()
        offenders = []
        checked = 0
        for path in sorted(ROOT.rglob("*.md")):
            if ".git" in path.relative_to(ROOT).parts:
                continue
            validator = validate_copy.Validator(blocklists)
            validator.check_file(path)
            checked += 1
            if validator.suggestions:
                offenders.append((path.relative_to(ROOT).as_posix(), validator.suggestions[0][1]))
        self.assertGreater(checked, 250)
        self.assertEqual(offenders, [])


class CliArgumentTests(unittest.TestCase):
    def test_empty_context_exits_two_like_an_unknown_id(self) -> None:
        for args in (["--context="], ["--context", ""]):
            with self.subTest(args=args):
                proc = run(self, *args, "-", stdin="Mày ơi\n", code=2)
                self.assertIn("unknown context ''", proc.stderr)
                self.assertIn("email-to-manager", proc.stderr)
                self.assertEqual(proc.stdout, "")


class MatrixDecisionTests(unittest.TestCase):
    def test_num002_is_off_for_friends_but_on_for_colleagues(self) -> None:
        text = "bạn gửi mình file hợp đồng 12000000đ nhé\n"
        friend = rules(self, "chat-close-friend", text)
        self.assertEqual(friend, [])
        colleague = rules(self, "chat-colleague", text)
        self.assertEqual([r for r, _t in colleague], ["NUM002"])

    def test_matrix_rationale_names_the_amount_rule_decision(self) -> None:
        prose = MATRIX.read_text(encoding="utf-8")
        self.assertRegex(prose, re.compile(r"NUM002.{0,200}chat-colleague", re.S))


class WorkflowFileTests(unittest.TestCase):
    def test_ci_installs_setuptools_before_the_unittest_step(self) -> None:
        ci = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
        install = ci.index("python -m pip install setuptools")
        unittest_step = ci.index("python3 -m unittest discover -s tests -v")
        self.assertLess(install, unittest_step)


if __name__ == "__main__":
    unittest.main()
