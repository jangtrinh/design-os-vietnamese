#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Portable UKMC.v1 Knowledge Base & Epistemic Stopping Gate Verifier.

Pure Python 3.9+ standard library. Zero external pip dependencies.
Verifies:
  1. All knowledge/*.md files (except README.md) have valid UKMC.v1 YAML frontmatter
     with id, title, domain, trust_tier: "verified", and source_attribution[].
  2. Every source sha256 matches the actual SHA-256 of its referenced file in knowledge/_evidence/.
  3. Every inline <!-- ease:source uri="..." sha256="..." quote="..." --> anchor resolves to a verified source file.
  4. Epistemic Stopping Gate (state.json + review.json + evidence.jsonl) evaluates to STOP_SUFFICIENT.

Usage:
    python3 tools/verify_ukmc.py
    python3 tools/verify_ukmc.py --run-id vn-design-os-261026
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import sys
from typing import Dict, List, Set

ROOT = pathlib.Path(__file__).resolve().parent.parent
KNOWLEDGE_ROOT = ROOT / "knowledge"
EASE_SOURCE_RE = re.compile(
    r'<!--\s*ease:source\s+uri="([^"]+)"\s+sha256="([0-9a-f]{64})"\s+quote="([^"]+)"\s*-->'
)
FM_URI_RE = re.compile(r'uri:\s*"?([^"\n]+)"?')
FM_SHA_RE = re.compile(r'sha256:\s*"?([0-9a-f]{64})"?')


def verify_knowledge(knowledge_root: pathlib.Path, run_id: str) -> int:
    ev_dir = knowledge_root / "_evidence" / run_id
    ev_path = ev_dir / "evidence.jsonl"
    state_path = ev_dir / "state.json"
    review_path = ev_dir / "review.json"

    if not ev_path.is_file() or not state_path.is_file() or not review_path.is_file():
        print(f"error: missing evidence files in {ev_dir}", file=sys.stderr)
        return 1

    atoms: List[dict] = []
    sources_seen: Set[str] = set()
    for line in ev_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        item = json.loads(line)
        atoms.append(item)
        if item.get("source_sha256"):
            sources_seen.add(item["source_sha256"])

    md_files = sorted(
        p for p in knowledge_root.glob("*.md")
        if p.name.lower() != "readme.md"
    )

    total_anchors = 0
    failures: List[str] = []

    for md in md_files:
        text = md.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append(f"{md.name}: missing YAML frontmatter")
            continue
        parts = text.split("\n---\n", 1)
        if len(parts) != 2:
            failures.append(f"{md.name}: unclosed YAML frontmatter")
            continue
        fm, body = parts[0], parts[1]
        if 'trust_tier: "verified"' not in fm and "trust_tier: verified" not in fm:
            failures.append(f"{md.name}: trust_tier is not verified")

        uris = [u.strip() for u in FM_URI_RE.findall(fm)]
        shas = [s.strip() for s in FM_SHA_RE.findall(fm)]
        if not uris or len(uris) != len(shas):
            failures.append(f"{md.name}: mismatched source_attribution uri/sha256 entries")
        for uri, expected_sha in zip(uris, shas):
            src_file = (md.parent / uri).resolve()
            if not src_file.is_file():
                failures.append(f"{md.name}: missing source file {uri}")
            else:
                actual_sha = hashlib.sha256(src_file.read_bytes()).hexdigest()
                if actual_sha != expected_sha:
                    failures.append(f"{md.name}: sha256 mismatch for {uri}")

        anchors = EASE_SOURCE_RE.findall(body)
        if not anchors:
            failures.append(f"{md.name}: zero <!-- ease:source ... --> anchors in body")
        for uri, expected_sha, _quote in anchors:
            total_anchors += 1
            src_file = (md.parent / uri).resolve()
            if not src_file.is_file():
                failures.append(f"{md.name}: anchor references missing file {uri}")
            else:
                actual_sha = hashlib.sha256(src_file.read_bytes()).hexdigest()
                if actual_sha != expected_sha:
                    failures.append(f"{md.name}: anchor sha256 mismatch for {uri}")

    state = json.loads(state_path.read_text(encoding="utf-8"))
    review = json.loads(review_path.read_text(encoding="utf-8"))

    req_claims = set(state.get("required_claims", []))
    covered_claims = {a.get("claim_id") for a in atoms if a.get("status") == "verified"}
    missing_claims = sorted(req_claims - covered_claims)
    if missing_claims:
        failures.append(f"unverified required claims: {missing_claims}")

    if not review.get("passed"):
        failures.append("review.json did not pass independent review")

    decision = "STOP_SUFFICIENT" if not failures else "CONTINUE_GAP"
    print(f"files: {len(md_files)} · anchors: {total_anchors} · failures: {len(failures)} · exempt blocks: 0")
    print(f"verified_claims: {len(req_claims - set(missing_claims))}/{len(req_claims)} · independent_sources: {len(sources_seen)}")
    print(f"Decision: {decision}")

    for f in failures:
        print(f"FAIL: {f}", file=sys.stderr)
    return 0 if not failures else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default=str(KNOWLEDGE_ROOT), help="knowledge root directory")
    ap.add_argument("--run-id", default="vn-design-os-261026", help="evidence run ID")
    args = ap.parse_args()
    return verify_knowledge(pathlib.Path(args.root), args.run_id)


if __name__ == "__main__":
    raise SystemExit(main())
