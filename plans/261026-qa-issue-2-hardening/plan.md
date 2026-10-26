# Implementation Plan — QA Issue #2 Resolution & Self-QA Hardening (`261026-qa-issue-2-hardening`)

## Context & References
- Brainstorm: `plans/specs/qa-issue-2-hardening/brainstorm.md`
- Use Cases: `plans/specs/qa-issue-2-hardening/usecases.md`
- Product Config: `.project-agent.md`, `CONTEXT.md`
- Issue Reference: `https://github.com/jangtrinh/design-os-vietnamese/issues/2`

## Agreed Seams Under Test
1. **CLI Process Seam (`subprocess.run` on `shared/scripts/validate_copy.py` and `skills/*/scripts/validate_copy.py`)**:
   - Tests invoke the CLI as a real subprocess and assert `returncode`, `"Traceback" not in stderr`, JSON findings count, and rule listing output.
2. **Repository File Tree Seam**:
   - Tests scan all repository markdown/config/tool files for personal paths (`<personal-home-path>`), license consistency (`PolyForm Shield`, `source-available`), and command validity.

## Vertical Slices

### Slice 1: Fix `--domain` `SKILL_DIR` Crash + `CAL001` Span Deduplication & Sync All 10 Skills
- **What it delivers**:
  - Define `SKILL_DIR = SCRIPT_DIR.parent` and `_resolve_domain_skill_dir(domain)` in `shared/scripts/validate_copy.py`.
  - Ensure `load_domain_rules` resets `DOCTYPES` when switching domains so `--domain` works identically whether invoked from `shared/scripts/validate_copy.py` or any `skills/<skill>/scripts/validate_copy.py`.
  - Group `CAL001` matches by winning `(start, end)` span in `_check_text_rules`, deduplicating suggestions case-insensitively and emitting exactly 1 `CAL001` finding per span.
  - Sync all 10 `skills/*/scripts/validate_copy.py` via `python3 tools/sync_shared.py`.
- **Blocked by**: None.

### Slice 2: Fix Documentation, License Wording, Personal Paths & `docs/QA-FINDINGS.md`
- **What it delivers**:
  - Update `README.md:225` (`open-source` -> `source-available`) and `docs/_config.yml:21` (`MIT` -> `PolyForm Shield 1.0.0`).
  - Update `knowledge/README.md:25-32` to use `python3 tools/verify_ukmc.py` and `$KNOWLEDGE_BUILDER_SRC` + repo-relative `knowledge` path (zero `<personal-home-path>` occurrences).
  - Update `tools/generate_landing_pairs.py:386` and `tools/generate_tech_pairs.py:349` to use `pathlib.Path(__file__).resolve().parent.parent` instead of `<personal-home-path>/...`.
  - Update `docs/QA-FINDINGS.md` lines 12-13, 37, 41-42, 56 to reflect that the license is now `PolyForm Shield License 1.0.0` (resolved) and remove raw `<personal-home-path>` strings.
- **Blocked by**: Slice 1.

### Slice 3: Non-Tautological Self-QA Test Suite & `scripts/self_check.py` Hardening
- **What it delivers**:
  - Strengthen `tests/test_qa_findings_2026_10_26.py` (`F02QuickStartBroken`) so `test_documented_domain_flag_is_accepted` and `test_documented_output_flag_is_accepted` assert `"Traceback" not in r.stderr` and exact exit codes.
  - Add `tests/test_qa_issue_2_2026_10_26.py` testing all 5 items from Issue #2 across `shared/` and all 10 `skills/*/` copies, plus a test that executes every CLI command in `README.md` Quick Start and verifies zero tracebacks.
  - Enhance `scripts/self_check.py` to run a `--domain` smoke check and personal-path/license guard.
- **Blocked by**: Slice 1, Slice 2.
