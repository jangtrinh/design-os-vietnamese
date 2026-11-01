#!/usr/bin/env python3
"""Tests for the plain-tone rule family PLAIN001-PLAIN007 in ``validate_copy.py``.

The rules catch prose that passes every mechanical check yet reads as long-winded
and machine-written: very long sentences, audit labels left in prose, meta openers,
filler, "không chỉ ... mà còn", dash asides and stacked parentheses.

Library tests drive ``Validator`` in-process; CLI tests go through ``cli()``, which
asserts the exact exit code and the absence of a traceback. Everything is offline
and stdlib-only.
"""
from __future__ import annotations

import json
import pathlib
import subprocess
import sys
import tempfile
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED_DIR = ROOT / "shared" / "scripts"
SHARED = SHARED_DIR / "validate_copy.py"
REFERENCE = ROOT / "shared" / "references" / "plain-vietnamese.md"
SKILL_SCRIPTS = sorted((ROOT / "skills").glob("*/scripts/validate_copy.py"))

sys.path.insert(0, str(SHARED_DIR))
import validate_copy  # noqa: E402

PLAIN_RULES = tuple(f"PLAIN00{n}" for n in range(1, 8))
FAKE_MD = pathlib.Path("sample.md")


def sentence(n_words: int) -> str:
    """A sentence of exactly ``n_words`` space-separated words, free of every other rule."""
    return " ".join(f"từ{i}" for i in range(n_words)) + "."


def cli(tc: unittest.TestCase, *args: str, stdin: str = "", code: int, script: pathlib.Path = SHARED):
    proc = subprocess.run(
        [sys.executable, str(script), *args],
        input=stdin, capture_output=True, text=True, cwd=str(ROOT),
    )
    tc.assertNotIn("Traceback", proc.stderr, proc.stderr)
    tc.assertEqual(proc.returncode, code, f"{args}\nstdout={proc.stdout}\nstderr={proc.stderr}")
    return proc


def plain(found) -> list:
    return [f for f in found if f.rule.startswith("PLAIN")]


class PlainRuleTestCase(unittest.TestCase):
    validator = None

    @classmethod
    def setUpClass(cls) -> None:
        cls.validator = validate_copy.Validator(validate_copy.Blocklists())

    def check(self, text: str, path: pathlib.Path = FAKE_MD, **kwargs):
        validator = self.validator
        if kwargs:
            validator = validate_copy.Validator(validate_copy.Blocklists(), **kwargs)
        return plain(validator.check_text(text, path))

    def rules(self, text: str, **kwargs) -> list:
        return [f.rule for f in self.check(text, **kwargs)]

    def assertFires(self, rule: str, text: str, **kwargs) -> None:
        self.assertIn(rule, self.rules(text, **kwargs), text)

    def assertQuiet(self, text: str, **kwargs) -> None:
        self.assertEqual(self.rules(text, **kwargs), [], text)


class RuleRegistryTests(PlainRuleTestCase):
    def test_every_plain_rule_is_documented(self) -> None:
        for rule in PLAIN_RULES:
            self.assertIn(rule, validate_copy.RULE_DOCS)

    def test_default_severity_is_warning(self) -> None:
        found = self.check(sentence(40))
        self.assertEqual([(f.rule, f.severity) for f in found], [("PLAIN001", validate_copy.WARN)])


class LongSentenceTests(PlainRuleTestCase):
    def test_limit_is_exclusive_at_thirty_words(self) -> None:
        self.assertQuiet(sentence(30))
        self.assertFires("PLAIN001", sentence(31))

    def test_message_names_the_count_and_the_limit(self) -> None:
        (hit,) = self.check(sentence(36))
        self.assertIn("36", hit.message)
        self.assertIn("30", hit.message)

    def test_limit_is_configurable(self) -> None:
        self.assertFires("PLAIN001", sentence(12), max_sentence_words=10)
        self.assertQuiet(sentence(12), max_sentence_words=12)

    def test_words_inside_backticks_do_not_count(self) -> None:
        code = "`" + " ".join(f"arg{i}" for i in range(40)) + "`"
        self.assertQuiet(f"Chạy lệnh {code} để xuất báo cáo.")

    def test_fenced_code_and_tables_and_headings_are_not_prose(self) -> None:
        fenced = "```\n" + sentence(60) + "\n```\n"
        self.assertQuiet(fenced)
        self.assertQuiet("| Cột | " + sentence(60) + " |\n")
        self.assertQuiet("# " + sentence(60) + "\n")

    def test_full_stops_end_sentences_but_decimals_and_versions_do_not(self) -> None:
        self.assertQuiet(sentence(20) + " " + sentence(20))
        self.assertQuiet("Phiên bản v2.1 giảm thời gian giao từ 3,5 xuống 2.5 giờ.")

    def test_a_sentence_wrapped_over_several_lines_is_measured_whole(self) -> None:
        wrapped = " ".join(f"từ{i}" for i in range(20)) + "\n" + " ".join(f"từ{i}" for i in range(20, 40)) + ".\n"
        found = self.check(wrapped)
        self.assertEqual([f.rule for f in found], ["PLAIN001"])
        self.assertEqual((found[0].line, found[0].col), (1, 1))

    def test_blank_lines_and_list_items_separate_sentences(self) -> None:
        self.assertQuiet(" ".join(f"từ{i}" for i in range(20)) + "\n\n" + " ".join(f"từ{i}" for i in range(20)) + "\n")
        items = "- " + " ".join(f"từ{i}" for i in range(20)) + "\n- " + " ".join(f"từ{i}" for i in range(20)) + "\n"
        self.assertQuiet(items)

    def test_finding_points_at_the_line_where_the_sentence_starts(self) -> None:
        text = "Đơn đã giao.\n\nGhi chú ngắn.\n\n" + sentence(35) + "\n"
        (hit,) = self.check(text)
        self.assertEqual((hit.rule, hit.line, hit.col), ("PLAIN001", 5, 1))


class AuditLabelTests(PlainRuleTestCase):
    def test_labels_in_prose_fire(self) -> None:
        for label in ("FACT", "INFERENCE", "ASSUMPTION", "UNKNOWN"):
            with self.subTest(label=label):
                self.assertFires("PLAIN002", f"{label}: tỷ lệ giao trễ giảm xuống 4%.")

    def test_labels_inside_code_identifiers_and_lowercase_words_stay_clean(self) -> None:
        self.assertQuiet("Trạng thái `UNKNOWN` được trả về khi chưa có đơn.")
        self.assertQuiet("Hằng số UNKNOWN_ERROR không đổi.")
        self.assertQuiet("Thực tế là tỷ lệ giao trễ giảm xuống 4%.")
        self.assertQuiet("Bảng fact và dimension nằm trong kho dữ liệu.")


class MetaOpenerTests(PlainRuleTestCase):
    def test_openers_at_the_start_of_a_sentence_fire(self) -> None:
        for text in (
            "Bản đánh giá này cho thấy tỷ lệ giao trễ giảm.",
            "Lưu ý: đơn trên 2 triệu cần xác nhận.",
            "Phần mới: bảng điều khiển theo giờ.",
            "Hệ quả: tài xế nhận đơn chậm hơn.",
            "**Lưu ý:** đơn trên 2 triệu cần xác nhận.",
            "- Hệ quả: tài xế nhận đơn chậm hơn.",
            "Giá giảm 10%. Phần mới: bảng điều khiển theo giờ.",
        ):
            with self.subTest(text=text):
                self.assertFires("PLAIN003", text)

    def test_the_same_words_mid_sentence_stay_clean(self) -> None:
        self.assertQuiet("Chúng tôi đã gửi bản đánh giá này cho nhóm vận hành.")
        self.assertQuiet("Mọi hệ quả đều ghi trong biên bản.")


class FillerTests(PlainRuleTestCase):
    def test_owner_listed_fillers_fire_in_any_case(self) -> None:
        for phrase in ("điều này", "nhìn chung", "đáng chú ý", "một cách", "thực hiện", "tiến hành"):
            for text in (f"Đơn giao {phrase} rồi.", f"{phrase.capitalize()} đơn giao rồi."):
                with self.subTest(text=text):
                    self.assertFires("PLAIN004", text)

    def test_plain_wording_stays_clean(self) -> None:
        self.assertQuiet("Đơn giao trong 30 phút. Tài xế gọi trước khi đến.")

    def test_a_filler_is_matched_as_a_whole_phrase(self) -> None:
        self.assertQuiet("Đây là thực hiệnx.")


class NotOnlyButAlsoTests(PlainRuleTestCase):
    def test_both_halves_in_one_sentence_fire(self) -> None:
        self.assertFires("PLAIN005", "Ứng dụng không chỉ giao nhanh mà còn rẻ hơn.")
        self.assertFires("PLAIN005", "Ứng dụng không những giao nhanh mà còn rẻ hơn.")

    def test_halves_in_different_sentences_or_one_half_alone_stay_clean(self) -> None:
        self.assertQuiet("Ứng dụng không chỉ giao nhanh. Nó còn rẻ hơn.")
        self.assertQuiet("Đơn không chỉ có món chính.")
        self.assertQuiet("Giao nhanh mà còn rẻ.")


class DashAsideTests(PlainRuleTestCase):
    def test_spaced_dash_aside_fires_once_per_sentence(self) -> None:
        text = "Ứng dụng giao nhanh — kể cả giờ cao điểm — và rẻ hơn."
        self.assertEqual(self.rules(text), ["PLAIN006"])
        self.assertFires("PLAIN006", "Ứng dụng giao nhanh – kể cả giờ cao điểm.")

    def test_number_ranges_unspaced_dashes_hyphens_and_table_cells_stay_clean(self) -> None:
        self.assertQuiet("Phí giao từ 10 – 20 nghìn đồng.")
        self.assertQuiet("Giao nhanh—kể cả giờ cao điểm.")
        self.assertQuiet("Khu vực giao-nhận mở cửa từ 6 giờ.")
        self.assertQuiet("| Cột | Giá trị |\n|---|---|\n| Phí giao | — |\n")


class ParenthesesTests(PlainRuleTestCase):
    def test_three_parentheses_in_one_sentence_fire(self) -> None:
        self.assertFires("PLAIN007", "Đơn (loại A) giao trong 30 phút (nội thành) hoặc 60 phút (ngoại thành).")

    def test_two_parentheses_or_spread_over_sentences_stay_clean(self) -> None:
        self.assertQuiet("Đơn (loại A) giao trong 30 phút (nội thành).")
        self.assertQuiet("Đơn (loại A) giao nhanh. Đơn (loại B) giao chậm. Đơn (loại C) hẹn giờ.")


class SuppressionAndScopeTests(PlainRuleTestCase):
    def test_file_level_directive_switches_one_rule_off(self) -> None:
        text = "<!-- vlc-disable: PLAIN001 -->\n\n" + sentence(40) + "\nĐơn giao thực hiện xong.\n"
        self.assertEqual(self.rules(text), ["PLAIN004"])

    def test_all_directive_switches_every_plain_rule_off(self) -> None:
        self.assertQuiet("<!-- vlc-disable: all -->\n" + sentence(40) + "\nFACT: một cách.\n")

    def test_line_level_directive_silences_only_that_line(self) -> None:
        text = "Đơn giao thực hiện xong. <!-- vlc-disable-line: PLAIN004 -->\nĐơn khác giao thực hiện xong.\n"
        found = self.check(text)
        self.assertEqual([(f.rule, f.line) for f in found], [("PLAIN004", 2)])

    def test_only_prose_files_are_checked(self) -> None:
        text = "Đơn giao thực hiện xong. " + sentence(40)
        for suffix in (".json", ".ts", ".html", ".css"):
            with self.subTest(suffix=suffix):
                self.assertEqual(self.check(text, pathlib.Path("sample" + suffix)), [])
        for suffix in (".md", ".txt"):
            with self.subTest(suffix=suffix):
                self.assertTrue(self.check(text, pathlib.Path("sample" + suffix)))

    def test_english_sentences_are_not_judged(self) -> None:
        english = " ".join(["word"] * 40) + " — and (one) (two) (three), not only fast but also cheap."
        self.assertQuiet(english)
        self.assertFires("PLAIN001", english.replace("word", "từ", 1))

    def test_quoted_lines_keep_their_wording(self) -> None:
        self.assertQuiet("> " + sentence(40) + "\n> Đơn giao thực hiện xong.\n")

    def test_email_contexts_ignore_the_quoted_reply_thread(self) -> None:
        matrix = validate_copy.load_context_matrix()
        validator = validate_copy.Validator(
            validate_copy.Blocklists(), context="email-to-colleague", context_matrix=matrix,
        )
        reply = "Chào An,\n\nĐơn giao xong.\n\nThân,\nBình\n\nOn Tue, An Le wrote:\n" + sentence(40) + "\nGiao thực hiện xong.\n"
        self.assertEqual(plain(validator.check_text(reply, FAKE_MD)), [])
        self.assertTrue(plain(validate_copy.Validator(validate_copy.Blocklists()).check_text(reply, FAKE_MD)))

    def test_front_matter_is_not_prose(self) -> None:
        self.assertQuiet("---\ntitle: " + sentence(40) + "\n---\n\nĐơn giao trong 30 phút.\n")


class ExecutiveContextTests(PlainRuleTestCase):
    def test_executive_context_raises_every_plain_finding_to_error(self) -> None:
        matrix = validate_copy.load_context_matrix()
        validator = validate_copy.Validator(
            validate_copy.Blocklists(), context="doc-for-executives", context_matrix=matrix,
        )
        found = plain(validator.check_text("## Tóm tắt\n\n" + sentence(40) + "\nĐơn giao thực hiện xong.\n", FAKE_MD))
        self.assertEqual({f.rule for f in found}, {"PLAIN001", "PLAIN004"})
        self.assertEqual({f.severity for f in found}, {validate_copy.ERROR})

    def test_other_contexts_keep_warnings(self) -> None:
        matrix = validate_copy.load_context_matrix()
        validator = validate_copy.Validator(
            validate_copy.Blocklists(), context="email-to-colleague", context_matrix=matrix,
        )
        found = plain(validator.check_text("Chào An,\n\nĐơn giao thực hiện xong.\n\nThân,\nBình\n", FAKE_MD))
        self.assertEqual([(f.rule, f.severity) for f in found], [("PLAIN004", validate_copy.WARN)])


class PhraseTableTests(PlainRuleTestCase):
    def test_reference_table_is_machine_readable_and_complete(self) -> None:
        phrases = validate_copy.load_plain_phrases()
        self.assertIsNotNone(phrases)
        self.assertEqual({p for p, _ in phrases.labels}, {"FACT", "INFERENCE", "ASSUMPTION", "UNKNOWN"})
        openers = {p.lower() for p, _ in phrases.openers}
        for expected in ("bản đánh giá này", "phần mới:", "lưu ý:", "hệ quả:"):
            self.assertIn(expected, openers)
        fillers = {p.lower() for p, _ in phrases.fillers}
        for expected in ("điều này", "nhìn chung", "đáng chú ý", "một cách", "thực hiện", "tiến hành"):
            self.assertIn(expected, fillers)

    def test_phrases_come_from_the_markdown_table_not_from_python(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            table = (
                "<!-- machine-readable: plain-phrases -->\n"
                "| Cụm từ | Loại | Gợi ý viết lại |\n|---|---|---|\n"
                "| vô cùng | filler | bỏ |\n"
                "| Tóm lại, | opener | vào thẳng ý chính |\n"
            )
            pathlib.Path(tmp, "plain-vietnamese.md").write_text(table, encoding="utf-8")
            custom = validate_copy.load_plain_phrases([pathlib.Path(tmp)])
        self.assertEqual([p for p, _ in custom.fillers], ["vô cùng"])
        self.assertEqual(custom.labels, [])
        self.assertFires("PLAIN004", "Giao hàng vô cùng nhanh.", plain_phrases=custom)
        self.assertFires("PLAIN003", "Tóm lại, giao hàng nhanh.", plain_phrases=custom)
        self.assertQuiet("Đơn giao thực hiện xong. FACT: ổn.", plain_phrases=custom)

    def test_missing_table_still_runs_the_structural_rules(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            self.assertIsNone(validate_copy.load_plain_phrases([pathlib.Path(tmp)], fallback=False))
        validator = validate_copy.Validator(validate_copy.Blocklists(), plain_phrases=validate_copy.NO_PLAIN_PHRASES)
        found = plain(validator.check_text("Đơn giao thực hiện xong. " + sentence(40), FAKE_MD))
        self.assertEqual([f.rule for f in found], ["PLAIN001"])


class ReferencePageExampleTests(PlainRuleTestCase):
    """Every before/after pair on the reference page is executed, so the page cannot rot."""

    def examples(self) -> list:
        text = REFERENCE.read_text(encoding="utf-8")
        header, rows = validate_copy._table_with_header(text, "<!-- machine-readable: plain-examples -->")
        self.assertEqual(header[:3], ["trước", "sau", "quy tắc"])
        return [(validate_copy._unwrap(r[0]), validate_copy._unwrap(r[1]), validate_copy._unwrap(r[2])) for r in rows]

    def test_page_has_five_to_eight_pairs(self) -> None:
        self.assertGreaterEqual(len(self.examples()), 5)
        self.assertLessEqual(len(self.examples()), 8)

    def test_every_before_triggers_its_rule_and_every_after_is_clean(self) -> None:
        for before, after, rule in self.examples():
            with self.subTest(before=before):
                self.assertIn(rule, PLAIN_RULES)
                self.assertFires(rule, before)
                self.assertQuiet(after)
                self.assertEqual([f.rule for f in validate_copy.Validator(validate_copy.Blocklists()).check_text(after, FAKE_MD)
                                  if f.severity == validate_copy.ERROR], [])

    def test_page_names_no_outside_project(self) -> None:
        text = REFERENCE.read_text(encoding="utf-8")
        for token in ("http://", "https://", "/" + "Users" + "/", "@"):
            self.assertNotIn(token, text)


class CliTests(unittest.TestCase):
    BAD = "Đơn giao thực hiện xong. " + sentence(40) + "\n"

    def test_list_rules_shows_every_plain_rule_in_shared_and_every_skill_copy(self) -> None:
        for script in [SHARED, *SKILL_SCRIPTS]:
            for extra in ([], ["--domain", "all"]):
                with self.subTest(script=script.parent.parent.name, extra=extra):
                    r = cli(self, "--list-rules", *extra, code=0, script=script)
                    listed = {line.split()[0] for line in r.stdout.splitlines() if line.strip()}
                    for rule in PLAIN_RULES:
                        self.assertIn(rule, listed)

    def test_warnings_exit_zero_and_strict_exits_one(self) -> None:
        r = cli(self, "--json", "-", stdin=self.BAD, code=0)
        payload = json.loads(r.stdout)["findings"]
        self.assertEqual({(f["rule"], f["severity"]) for f in payload},
                         {("PLAIN001", "warning"), ("PLAIN004", "warning")})
        strict = cli(self, "--json", "--strict", "-", stdin=self.BAD, code=1)
        self.assertEqual({f["rule"] for f in json.loads(strict.stdout)["findings"]}, {"PLAIN001", "PLAIN004"})

    def test_executive_context_exits_one_without_strict(self) -> None:
        text = "## Tóm tắt\n\n" + self.BAD
        r = cli(self, "--json", "--context", "doc-for-executives", "-", stdin=text, code=1)
        severities = {f["rule"]: f["severity"] for f in json.loads(r.stdout)["findings"] if f["rule"].startswith("PLAIN")}
        self.assertEqual(severities, {"PLAIN001": "error", "PLAIN004": "error"})

    def test_max_sentence_words_flag(self) -> None:
        text = sentence(12) + "\n"
        cli(self, "--json", "-", stdin=text, code=0)
        r = cli(self, "--json", "--max-sentence-words", "10", "-", stdin=text, code=0)
        self.assertEqual([f["rule"] for f in json.loads(r.stdout)["findings"]], ["PLAIN001"])
        bad = cli(self, "--max-sentence-words", "0", "-", stdin=text, code=2)
        self.assertIn("--max-sentence-words", bad.stderr)

    def test_clean_prose_exits_zero_with_no_findings(self) -> None:
        r = cli(self, "--json", "--strict", "-", stdin="Đơn giao trong 30 phút. Tài xế gọi trước khi đến.\n", code=0)
        self.assertEqual(json.loads(r.stdout)["findings"], [])

    def test_skill_copies_report_the_same_plain_findings(self) -> None:
        reference = None
        for script in [SHARED, *SKILL_SCRIPTS]:
            r = cli(self, "--json", "-", stdin=self.BAD, code=0, script=script)
            got = sorted((f["rule"], f["line"], f["column"]) for f in json.loads(r.stdout)["findings"]
                         if f["rule"].startswith("PLAIN"))
            reference = reference or got
            self.assertEqual(got, reference, script)


if __name__ == "__main__":
    unittest.main()
