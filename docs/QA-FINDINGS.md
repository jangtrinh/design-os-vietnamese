# QA Findings — 2026-10-26

Scope: fresh clone of `main` (7743e68), Python 3, Linux, following the README as a new user.
QA only: this branch adds tests, fixtures and this document. **No product code is changed.**
Regression tests: `tests/test_qa_findings_2026_10_26.py` (14 tests, all fail today, each passes once its finding is fixed).
Run: `python3 -m unittest tests.test_qa_findings_2026_10_26 -v`

| ID | Severity | Title |
|---|---|---|
| F-01 | High | Checker misses its own headline calque; shared `glossary.md` / `banned-phrases.md` missing |
| F-02 | High | README commands fail: `--domain`, `--output`, `check_i18n_parity --source/--target` |
| F-03 | High | Knowledge verify steps and 2 tests depend on `/Users/jangtrinh/...` |
| F-04 | Medium (flag only) | LICENSE and READMEs say MIT; conflicts with the PolyForm Shield policy |
| F-05 | Medium | README skill table lists 18 reference files and `rules_biz.py`/`rules_edu.py` that do not exist |
| F-06 | Low | No GitHub releases, no images/screenshots |

## F-01 — Calque example not detected (High)
Repro:
```
printf 'Làm ơn nhập của bạn mật khẩu\n' > c.md
python3 shared/scripts/validate_copy.py c.md            # -> 0 warnings, "clean", exit 0
python3 skills/vn-design-system-ux/scripts/validate_copy.py c.md   # -> clean, exit 0
```
Expected: `CAL001` (README "Why" section item 1 uses this exact sentence as the example).
Actual: clean. The shared script prints
`warning: reference file not found, some rules disabled: shared/references/glossary.md` (and `banned-phrases.md`).
The skill copies have those files but still miss the calque, so the pattern itself is also missing.
Tests: `F01CalqueNotDetected` (4).

## F-02 — README quick-start commands are invalid (High)
- `validate_copy.py ... --domain ux --register ux-microcopy` → `error: unrecognized arguments: --domain ux` (exit 2). Same for `--domain biz`, `--domain finance`. Also in README.vi.md line 43.
- `--output path` (auto-fix example) is not a supported option.
- `check_i18n_parity.py --source ... --target ...` → `unrecognized arguments: --source --target`; it takes positional `source target`.
Tests: `test_documented_domain_flag_is_accepted`, `test_documented_output_flag_is_accepted`, `test_documented_i18n_parity_flags_accepted`.

## F-03 — Personal absolute paths (High)
README.md lines 118/122 and README.vi.md lines 49/52 use `PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src`. `design-os-knowledge-builder` is not published, so no outside user can run the UKMC verify step, and the two UKMC tests in `tests/test_ukmc_knowledge.py` are silently **skipped** (`design-os-knowledge-builder not present at /Users/jangtrinh/...`) while the suite reports OK. The "STOP_SUFFICIENT verified" badge cannot be reproduced.
Tests: `test_no_personal_absolute_paths_in_docs`, `test_no_personal_paths_in_tests`.

## F-04 — License conflict (Medium, flag only)
`LICENSE` is MIT; README.md line 10 (badge) and 162, README.vi.md line 61 say MIT. The stated DESIGN:OS policy is PolyForm Shield. Not changed here; owner decision.
Tests: `F03LicenseConflict` (2) — will pass once the license text and READMEs stop saying MIT.

## F-05 — README lists files that do not exist (Medium)
Skill table references e.g. `section-playbook.md`, `cta-library.md`, `headline-formulas.md`, `terminology.md`, `cong-van-format.md`, `accounting-tt99-2025.md`, `moet-curriculum-and-grading.md` (18 missing in total; see test output). Rule engines are named `rules_biz.py` / `rules_edu.py` but files are `rules_business.py` / `rules_education.py`.
Tests: `F04ReadmeReferencedFilesExist` (2).

## F-06 — No releases, no images (Low)
`gh release list -R jangtrinh/design-os-vietnamese` → empty. Repo has no PNG/JPG/SVG/GIF; README has no screenshot of output. Only one commit.
Test: `test_repo_has_at_least_one_image` (releases are checked manually).

## Other observations
- Existing suite: `python3 -m unittest discover -s tests` → 19 tests OK, 2 skipped (see F-03).
- `tools/sync_shared.py` ran clean with no diff.

Evidence: `/workspace/projects/design-os-vietnamese/qa/2026-10-26/` (local QA box).
