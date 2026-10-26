# Brainstorm — QA Issue #2 Resolution & Self-QA Hardening (`qa-issue-2-hardening`)

## 1. Press Release (Internal Working Backwards)
**Headline**: `design-os-vietnamese` v4.0.1 eliminates the `--domain` `SKILL_DIR` `NameError` crash, deduplicates overlapping `CAL001` span findings, removes all remaining personal paths and license wording drift across the entire repository, and introduces a strict self-QA regression suite that rejects false-green tests.

**Problem**:
External QA (`Issue #2` on commit `13eea76`) found 5 defects that our unit suite missed:
1. **Blocker**: Passing `--domain <d>` to `shared/scripts/validate_copy.py` or `skills/*/scripts/validate_copy.py` crashed with `NameError: name 'SKILL_DIR' is not defined` at line 977 because `SKILL_DIR` was never defined at module scope, and `F02QuickStartBroken.test_documented_domain_flag_is_accepted` only checked `assertNotIn("unrecognized arguments", r.stderr)` (a classic **False-Green / Cannot-Fail** test).
2. **Medium**: `README.md:225` described `DESIGN:OS` as an `"open-source engineering ecosystem"`, conflicting with `PolyForm Shield License 1.0.0` (source-available). Additionally, `docs/_config.yml:21` still had a scaffolded `MIT` footer entry.
3. **Low**: `knowledge/README.md:25-32` (and `tools/generate_landing_pairs.py`, `tools/generate_tech_pairs.py`) contained hardcoded `<personal-home-path>/Products/...` paths because `test_no_personal_absolute_paths_in_docs` only scanned `README.md` and `README.vi.md`.
4. **Low**: `CAL001` emitted 3 findings at `1:1` for `"Làm ơn nhập của bạn mật khẩu"` because `BUILTIN_CALQUES`, `glossary.md`, and `banned-phrases.md` all matched the exact same `(0, 28)` span, and the longest-span filter only suppressed strictly shorter spans (`>`), not equal-length duplicate spans.
5. **Low**: `docs/QA-FINDINGS.md` lines 13 and 41-42 still stated `"LICENSE is MIT"` without noting the resolution to `PolyForm Shield License 1.0.0`.

## 2. MoSCoW Scope
- **Must Have**:
  - Define `SKILL_DIR = SCRIPT_DIR.parent` and `_resolve_domain_skill_dir(domain)` in `shared/scripts/validate_copy.py`, sync to all 10 skills, and verify `--domain` loads the target domain's `rules_*.py` and `references/`.
  - Deduplicate `CAL001` hits sharing the exact same `(start, end)` span on a line, merging distinct suggestions and emitting exactly 1 finding per winning span.
  - Replace `"open-source"` in `README.md:225` with `"source-available"` and `"MIT"` in `docs/_config.yml:21` with `"PolyForm Shield 1.0.0"`.
  - Remove all `<personal-home-path>/...` and `/workspace/...` paths from `knowledge/README.md`, `tools/generate_landing_pairs.py`, `tools/generate_tech_pairs.py`, and `docs/QA-FINDINGS.md`.
  - Update `docs/QA-FINDINGS.md` to reflect that the license is now `PolyForm Shield License 1.0.0` (resolved).
  - Add non-tautological regression tests in `tests/test_qa_findings_2026_10_26.py` and `tests/test_qa_issue_2_2026_10_26.py` that check `returncode`, `"Traceback" not in stderr`, domain rule loading across all 10 domains & 11 script copies, single-finding `CAL001` span deduplication, and repo-wide path/license hygiene.
- **Should Have**:
  - Integrate repo-wide path/license/domain smoke checks directly into `scripts/self_check.py`.
- **Won't Have**:
  - External pip dependencies or network-dependent tests in `unittest`.
