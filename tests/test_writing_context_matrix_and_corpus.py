#!/usr/bin/env python3
"""Matrix consistency and golden-pair tests for the writing-context dimension.

Runs the Validator in-process against ``shared/references/context-matrix.md`` and
``evals/contexts/pairs.jsonl``. Offline and stdlib-only.
"""
from __future__ import annotations

import json
import pathlib
import sys
import unicodedata
import unittest

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAIRS = ROOT / "evals" / "contexts" / "pairs.jsonl"
MATRIX = ROOT / "shared" / "references" / "context-matrix.md"

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


def read_pairs() -> list:
    return [
        json.loads(line)
        for line in PAIRS.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


class ContextMatrixTests(unittest.TestCase):
    def setUp(self) -> None:
        sys.path.insert(0, str(ROOT / "shared" / "scripts"))
        try:
            import validate_copy  # noqa: WPS433
        finally:
            sys.path.pop(0)
        self.vc = validate_copy
        text = MATRIX.read_text(encoding="utf-8")
        self.header, self.rows = self.vc._table_with_header(text, "<!-- machine-readable: contexts -->")

    def test_matrix_has_exactly_the_ten_presets_each_marked_proposed(self) -> None:
        names = [self.vc._unwrap(r[0]) for r in self.rows]
        self.assertEqual(sorted(names), sorted(PRESETS))
        basis = self.header.index("basis")
        for row in self.rows:
            self.assertEqual(self.vc._unwrap(row[basis]), "proposed", row[0])

    def test_matrix_rule_references_resolve_to_known_rules(self) -> None:
        known = set(self.vc.RULE_DOCS)
        dis, ena = self.header.index("disables"), self.header.index("enables")
        for row in self.rows:
            for col in (dis, ena):
                for token in (self.vc._unwrap(p) for p in row[col].split(",")):
                    if token and token != "—":
                        self.assertIn(token, known, f"{row[0]}: {token}")
            for token in (self.vc._unwrap(p) for p in row[ena].split(",")):
                if token and token != "—":
                    self.assertTrue(token.startswith("CTX"), f"{row[0]} enables non-CTX rule {token}")

    def test_casual_chats_disable_the_mandated_rules_and_keep_unicode_and_address_checks(self) -> None:
        dis = self.header.index("disables")
        for row in self.rows:
            if self.vc._unwrap(row[0]) in ("chat-close-friend", "chat-colleague"):
                disabled = {self.vc._unwrap(p) for p in row[dis].split(",")}
                self.assertTrue({"DIA001", "CAL001", "LAW001", "SYN001", "CTX003"} <= disabled, row[0])
                self.assertFalse(disabled & {"NFC001", "ENC001", "PRO001"}, row[0])

    def test_every_ctx_rule_is_enabled_by_at_least_one_preset(self) -> None:
        ena = self.header.index("enables")
        enabled = {self.vc._unwrap(p) for row in self.rows for p in row[ena].split(",")}
        for rule in CTX_RULES:
            self.assertIn(rule, enabled)


class ContextGoldenPairsTests(unittest.TestCase):
    """Bad/good pairs per preset plus must-stay-clean casual texts (evals/contexts/pairs.jsonl)."""

    @classmethod
    def setUpClass(cls) -> None:
        sys.path.insert(0, str(ROOT / "shared" / "scripts"))
        try:
            import validate_copy
        finally:
            sys.path.pop(0)
        cls.vc = validate_copy
        cls.blocklists = validate_copy.Blocklists()

    def _codes(self, preset: str, text: str, register=None) -> list:
        validator = self.vc.Validator(self.blocklists, register=register, context=preset)
        return validator.check_text(text)

    def test_corpus_shape(self) -> None:
        rows = read_pairs()
        pairs = [r for r in rows if r.get("kind", "pair") == "pair"]
        clean = [r for r in rows if r.get("kind") == "clean"]
        self.assertGreaterEqual(len(pairs), 50)
        for preset in PRESETS:
            count = sum(1 for r in pairs if r["context"] == preset)
            self.assertGreaterEqual(count, 5, f"{preset} has {count} pairs")
        self.assertGreaterEqual(len(clean), 10)
        self.assertTrue({"chat-close-friend", "chat-colleague"} <= {r["context"] for r in clean})
        ids = [r["id"] for r in rows]
        self.assertEqual(len(ids), len(set(ids)), "duplicate ids")
        for rule in CTX_RULES:
            self.assertTrue(any(rule in r.get("expected_rules", []) for r in pairs), rule)

    def test_every_text_is_nfc_except_deliberate_nfd_defects(self) -> None:
        for row in read_pairs():
            for field in ("bad", "good", "clean"):
                text = row.get(field)
                if text is None:
                    continue
                deliberate = field == "bad" and "NFC001" in row.get("expected_rules", [])
                if not deliberate:
                    self.assertEqual(unicodedata.normalize("NFC", text), text, f"{row['id']}.{field}")

    def test_bad_triggers_expected_rules_and_good_is_free_of_them_and_of_all_ctx(self) -> None:
        for row in read_pairs():
            if row.get("kind", "pair") != "pair":
                continue
            with self.subTest(pair=row["id"]):
                expected = set(row["expected_rules"])
                self.assertTrue(expected, "expected_rules must be non-empty")
                bad = {f.rule for f in self._codes(row["context"], row["bad"], row.get("register"))}
                self.assertFalse(expected - bad, f"bad text missed {expected - bad} (got {sorted(bad)})")
                good = self._codes(row["context"], row["good"], row.get("register"))
                good_codes = {f.rule for f in good}
                self.assertFalse(expected & good_codes, f"good text still triggers {expected & good_codes}")
                self.assertFalse(
                    [r for r in good_codes if r.startswith("CTX")],
                    f"good text triggers CTX rules {sorted(good_codes)}",
                )
                self.assertEqual([(f.rule, f.text) for f in good], [], "good text must be clean")

    def test_clean_casual_texts_produce_zero_findings(self) -> None:
        for row in read_pairs():
            if row.get("kind") != "clean":
                continue
            with self.subTest(clean=row["id"]):
                got = self._codes(row["context"], row["clean"], row.get("register"))
                self.assertEqual([(f.rule, f.text) for f in got], [])

    def test_clean_casual_texts_would_be_flagged_without_the_context(self) -> None:
        flagged = 0
        for row in read_pairs():
            if row.get("kind") != "clean":
                continue
            plain = self.vc.Validator(self.blocklists).check_text(row["clean"])
            flagged += bool(plain)
        self.assertGreaterEqual(flagged, 6, "the clean corpus must actually exercise the relaxation")


if __name__ == "__main__":
    unittest.main()
