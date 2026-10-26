# QA Findings — 2026-10-26 (All Resolved)

Scope: fresh clone of `main`, Python 3, Linux/macOS, following the README as a new user.
Regression tests: `tests/test_qa_findings_2026_10_26.py` (14 tests) and `tests/test_qa_issue_2_2026_10_26.py` (6 tests).
Run: `python3 -m unittest discover -s tests -v`

| ID | Severity | Status | Title |
|---|---|---|---|
| F-01 | High | **RESOLVED** | Checker detects headline calques (`CAL001`, 1 deduplicated finding per span); shared `glossary.md` / `banned-phrases.md` present |
| F-02 | High | **RESOLVED** | README commands (`--domain`, `--output`, `check_i18n_parity --source/--target`) work across `shared/` and all 10 `skills/*/` copies |
| F-03 | High | **RESOLVED** | Portable `tools/verify_ukmc.py` requires zero personal paths; `knowledge/README.md` uses repo-relative paths |
| F-04 | Medium | **RESOLVED** | `LICENSE`, `README.md`, `README.vi.md`, and `docs/_config.yml` consistently use **PolyForm Shield License 1.0.0** (source-available) |
| F-05 | Medium | **RESOLVED** | All reference files and rule engines (`rules_*.py`) listed in the README skill table exist on disk |
| F-06 | Low | **RESOLVED** | GitHub Release `v4.0.0` published; architecture diagrams (`assets/design-os-vietnamese-architecture.svg`, `docs/images/cover.png`) included |

## F-01 — Calque detection & span deduplication (Resolved)
Repro:
```bash
printf 'Làm ơn nhập của bạn mật khẩu\n' > c.md
python3 shared/scripts/validate_copy.py c.md
python3 skills/vn-design-system-ux/scripts/validate_copy.py c.md
```
Resolution: `shared/references/glossary.md` and `shared/references/banned-phrases.md` are included in the repository, and `_check_text_rules` groups overlapping/identical-span calques so `Làm ơn nhập của bạn mật khẩu` emits exactly **1** `CAL001` error at `1:1` (`1 file(s) checked · 1 error(s) · 0 warning(s)`).
Tests: `F01CalqueNotDetected` (4) + `Issue2CalqueDeduplicationTests` (1).

## F-02 — README quick-start commands & `--domain` loading (Resolved)
- `validate_copy.py ... --domain <d> --register <r>` resolves the target skill directory via `SKILL_DIR` (`_resolve_domain_skill_dir`) and loads its `rules_*.py` and `references/*.md` without error across both `shared/scripts/validate_copy.py` and all 10 `skills/*/scripts/validate_copy.py` copies.
- `--output <path>` writes normalized/fixed output to the target path without mutating the source file in place.
- `check_i18n_parity.py` accepts both `--source ... --target ...` flags and positional `source target` arguments.
Tests: `F02QuickStartBroken` (5) + `Issue2DomainCrashRegressionTests` (2).

## F-03 — Portable UKMC.v1 verification without personal paths (Resolved)
`tools/verify_ukmc.py` verifies all 12 `knowledge/*.md` modules (`53 SHA-256 anchors`, `STOP_SUFFICIENT`) using only the Python 3.9+ standard library. `README.md`, `README.vi.md`, `knowledge/README.md`, and `tools/*.py` contain zero personal machine paths.
Tests: `test_no_personal_absolute_paths_in_docs`, `test_no_personal_paths_in_tests`, `test_no_personal_paths_anywhere_in_repo_outside_test_assertions`.

## F-04 — License consistency: PolyForm Shield License 1.0.0 (Resolved)
`LICENSE`, `README.md`, `README.vi.md`, `docs/_config.yml`, and `docs/index.html` all specify **PolyForm Shield License 1.0.0** (`source-available`, non-competing).
Tests: `F03LicenseConflict` (2) + `test_readme_uses_source_available_not_open_source` + `test_qa_findings_doc_and_config_reflect_polyform_shield`.

## F-05 — Skill reference files & rule engine filenames (Resolved)
All reference markdown files and `rules_*.py` modules referenced in `README.md` exist under `skills/*/references/` and `skills/*/scripts/`.
Tests: `F04ReadmeReferencedFilesExist` (2).

## F-06 — Releases & visual assets (Resolved)
GitHub Release `v4.0.0` is published and visual architecture diagrams (`assets/design-os-vietnamese-architecture.svg`, `docs/images/cover.svg`, `docs/images/cover.png`) are committed.
Test: `F05Images` (1).
