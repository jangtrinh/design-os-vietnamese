#!/usr/bin/env python3
"""Provenance checks for knowledge/data: every statutory or attested row must quote a frozen source
whose sha256 still matches, and every case file row must name a rule that has a variant table."""

from __future__ import annotations

import hashlib
import json
import re
import unicodedata
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
KNOWLEDGE_ROOT = REPO_ROOT / "knowledge"
DATA_DIR = KNOWLEDGE_ROOT / "data"
RUN_DIR = KNOWLEDGE_ROOT / "_evidence" / "vn-design-os-261026"
CLASSES = {"statutory", "attested-in-statute", "proposed"}


def _evidence_objects(node):
    if isinstance(node, dict):
        if {"source_uri", "sha256", "quote"} <= node.keys():
            yield node
        for value in node.values():
            yield from _evidence_objects(value)
    elif isinstance(node, list):
        for value in node:
            yield from _evidence_objects(value)


def _rows(node):
    if isinstance(node, dict):
        if "class" in node:
            yield node
        for value in node.values():
            yield from _rows(value)
    elif isinstance(node, list):
        for value in node:
            yield from _rows(value)


class RuleVariantTableTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.tables = json.loads((DATA_DIR / "rule-variant-tables.json").read_text(encoding="utf-8"))
        ledger = (RUN_DIR / "evidence.jsonl").read_text(encoding="utf-8").splitlines()
        cls.atom_ids = {json.loads(line)["id"] for line in ledger if line.strip()}
        cls.required = set(json.loads((RUN_DIR / "state.json").read_text(encoding="utf-8"))["required_claim_ids"])

    def test_every_quote_is_in_its_frozen_source(self) -> None:
        evidence = list(_evidence_objects(self.tables))
        self.assertGreater(len(evidence), 0)
        for ev in evidence:
            path = KNOWLEDGE_ROOT / ev["source_uri"]
            raw = path.read_bytes()
            self.assertEqual(hashlib.sha256(raw).hexdigest(), ev["sha256"], ev["source_uri"])
            self.assertIn(ev["quote"], raw.decode("utf-8"), ev["source_uri"])

    def test_cited_claims_are_required_atoms(self) -> None:
        for ev in _evidence_objects(self.tables):
            if "claim" in ev:
                self.assertIn(ev["claim"], self.atom_ids)
                self.assertIn(ev["claim"], self.required)

    def test_evidence_class_matches_evidence(self) -> None:
        for row in _rows(self.tables["rules"]):
            self.assertIn(row["class"], CLASSES, row)
            if row["class"] in {"statutory", "attested-in-statute"}:
                self.assertIn("evidence", row, row)
            else:
                self.assertNotIn("evidence", row, row)

    def test_proposed_patterns_compile(self) -> None:
        for rule in self.tables["rules"].values():
            for pattern in rule.get("proposed_patterns", []):
                re.compile(pattern, re.IGNORECASE)

    def test_case_files_are_well_formed(self) -> None:
        for name, expect in (("rule-negation-cases.jsonl", "no-finding"), ("heldout-candidates.jsonl", "finding")):
            lines = [line for line in (DATA_DIR / name).read_text(encoding="utf-8").splitlines() if line.strip()]
            self.assertGreater(len(lines), 0, name)
            for line in lines:
                row = json.loads(line)
                self.assertIn(row["rule"], self.tables["rules"], name)
                self.assertEqual(row["expect"], expect, name)
                self.assertTrue(unicodedata.is_normalized("NFC", row["text"]), row["text"])


if __name__ == "__main__":
    unittest.main()
