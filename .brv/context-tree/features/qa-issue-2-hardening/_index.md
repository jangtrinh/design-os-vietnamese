# Feature Context — QA Issue #2 Resolution & Self-QA Hardening (`qa-issue-2-hardening`)

## Architecture & Decisions
1. **Domain Skill Resolution (`_resolve_domain_skill_dir` & `SKILL_DIR`)**:
   - Defined `SKILL_DIR = SCRIPT_DIR.parent` at module scope in `shared/scripts/validate_copy.py` (synced across all 10 `skills/*/scripts/validate_copy.py`).
   - Added `BASE_RULE_DOCS` snapshot so `load_domain_rules()` resets `RULE_DOCS` and `DOCTYPES` cleanly before loading a target domain's `rules_*.py`, preventing cross-domain rule leakage.
2. **Baseline Glossary Inheritance (`Blocklists`)**:
   - `Blocklists.__init__` automatically loads `shared/references/glossary.md` and `shared/references/banned-phrases.md` as a universal baseline before layering skill-specific `references/*.md`.
3. **Span-Based `CAL001` Deduplication**:
   - `_check_text_rules` groups winning calque hits by `(start, end)` span, merges distinct suggestions case-insensitively in deterministic order, and emits exactly 1 `CAL001` finding per span.
4. **Evidence Floor & Self-QA Hardening**:
   - Upgraded `tests/test_qa_findings_2026_10_26.py` and added `tests/test_qa_issue_2_2026_10_26.py` (42 total tests) verifying `returncode`, absence of `"Traceback"`, rule ID parity between docs and `--list-rules`, and zero personal machine paths across the entire repository.
