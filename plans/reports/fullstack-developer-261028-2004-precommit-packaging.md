# Report: pre-commit hooks + pip packaging (P0 #1 + #3)

Branch: `worktree-agent-af7187dc3581908c6` (not `main`). Worktree: `.claude/worktrees/agent-af7187dc3581908c6`. Not pushed.

## Commits
```
3e98879 feat(packaging): ship pip-installable vi-validate-copy, vi-i18n-parity, vi-font-coverage commands
1ff68da fix(pre-commit): run hooks through installed console commands instead of repo-relative scripts
9227575 ci: install the package and exercise the console commands and pre-commit hooks
546ff03 docs(readme): document pip/uvx commands and a working pre-commit config
240a955 ci: assert exact exit code and finding in the installed-command smoke step
(+ one final commit adding this report)
```

## Design
- New package `vi_design_os/` (`__init__.py`, `cli.py`, ~60 lines). `shared/scripts/*.py` is NOT edited; the 16 skill copies stay byte-identical (`sync_shared --check` green).
- `pyproject.toml`: `[project.scripts]` -> `vi-validate-copy`, `vi-i18n-parity`, `vi-font-coverage` = `vi_design_os.cli:{validate_copy,i18n_parity,font_coverage}_main`. `[tool.setuptools.package-dir]` maps `vi_design_os.shared` -> `shared/` and `vi_design_os.skills` -> `skills/`; `package-data` ships `shared/scripts/*.py`, `shared/references/*.md`, and per skill `scripts/rules_*.py` + `references/{glossary,banned-phrases,register-matrix}.md`. Installed layout = `vi_design_os/{cli.py, shared/, skills/}` so `SKILL_DIR.parent/"skills"/<slug>` and `SKILL_DIR.parent/"shared"/"references"` resolve exactly as in a checkout (AC2).
- `cli.py` loads the script from `bundle_root()/shared/scripts/<name>.py` via `importlib` and returns `module.main(argv)`. `bundle_root()` = package dir when installed, repo root in a source checkout/editable install. Flags and exit codes are the script's own.
- Why this over runpy/copying scripts: smallest design, single implementation, no duplicate of the 16 self-contained skill copies, no edit to rule logic. Why only `rules_*.py` + 3 reference files: grep of `skills/*/scripts/rules_*.py` shows the only runtime file read is `rules_finance.py` -> `references/glossary.md`; `validate_copy.py` reads only `glossary.md`, `banned-phrases.md`, `register-matrix.md` from reference dirs.
- Hooks: `language: python`, entry = the console command, hook ids unchanged.
- `.gitignore` gained `build/`, `dist/`, `*.egg-info/` (OUTSIDE the stated file list). Reason: `pip install <dir>` does an in-tree build and leaves `build/` and `design_os_vietnamese.egg-info/` in the checkout (it did here); in CI that would pollute the tree before `try-repo`, and stale `build/lib` can ship stale files.

## AC6: red first (pre-fix tree b3cfb55 + new test file)
Authoritative red, clean venv with only setuptools (no vi_design_os installed): 15 of 17 FAIL (the 2 `ok` are the intentional guards "hook ids kept" and "runtime deps stay empty").
```
test_installed_domain_rule_fires_outside_the_repo ... FAIL
test_installed_list_rules_matches_repo_script ... FAIL
test_wheel_declares_console_scripts ... FAIL
test_wheel_keeps_shared_and_skills_as_siblings ... FAIL
test_font_coverage_covered_and_uncovered_ranges ... FAIL
test_help_exits_zero_for_every_command ... FAIL
test_i18n_parity_matched_and_mismatched_catalogs ... FAIL
test_validate_copy_bad_date_exits_one_and_clean_exits_zero ... FAIL
test_validate_copy_list_rules_matches_script ... FAIL
test_validate_copy_stdin_domain_rule_fin001 ... FAIL
test_all_three_hook_ids_are_kept ... ok
test_every_hook_entry_is_a_declared_console_script ... FAIL
test_no_hook_entry_uses_a_repo_relative_script_path ... FAIL
test_no_hook_relies_on_language_system ... FAIL
test_package_ships_code_and_data ... FAIL
test_runtime_dependencies_stay_empty ... ok
test_three_console_scripts_are_declared_and_importable_targets_exist ... FAIL
Ran 17 tests in 0.650s
FAILED (failures=15)
```
First attempt with system `python3` (no setuptools): `FAILED (failures=11, skipped=4)`, e.g.
```
AssertionError: 'system' == 'system' : validate-copy
AssertionError: 'shared/scripts' unexpectedly found in 'python3 shared/scripts/validate_copy.py' : validate-copy
ModuleNotFoundError: No module named 'vi_design_os'
```
Note: one intermediate run against the pre-fix tree inside a venv that already had the package installed gave 7 failures (entry-point tests resolved the installed package). That is environment contamination, not a test gap; the clean-venv run above is the reference.

Green after fix: system python3 `Ran 78 tests ... OK (skipped=4)` (wheel tests skip without setuptools, by design); venv with setuptools `Ran 78 tests ... OK` (0 skipped), exit 0. Every CLI test asserts `Traceback` not in stderr, exact exit code, and payload (parity with the script's stdout/exit code).

## AC1-AC3 (fresh venv outside worktree, `pip install <worktree>`)
```
vi-validate-copy --help exit=0 stderr_bytes=0
vi-i18n-parity --help exit=0 stderr_bytes=0
vi-font-coverage --help exit=0 stderr_bytes=0
installed rule lines: 126
repo rule lines:      126
list-rules output byte-identical
--- AC3 FIN001   exit=0 (FIN001 is severity warning; JSON contains "rule": "FIN001")
--- AC3 DATE001
<stdin>:1:11: error DATE001  date “12/25/2026” looks like MM/dd/yyyy
1 file(s) checked · 1 error(s) · 0 warning(s)
exit=1
--- AC3 clean  -> "clean"  exit=0
```
Behavioural parity sweep (beyond `--list-rules`): all 489 eval pairs (bad + good = 978 texts) piped through installed `vi-validate-copy --json --domain all -` vs `python3 shared/scripts/validate_copy.py --json --domain all -`: `texts compared: 978 mismatches: 0 distinct rules fired: 70`, no Traceback.
Also verified: sdist built from `git archive` contains `shared/`, `skills/*/scripts/rules_*.py`, `vi_design_os/cli.py`; wheel built from that sdist has 82 files; `pip install -e <worktree>` gives 126 rules and FIN001 works.

## AC4 (scratch consumer repo, `uvx pre-commit try-repo <worktree> <hook> --files ...`)
```
validate-copy --files bad.md      -> Failed, exit code 1: bad.md:1:11: error DATE001 ... "1 file(s) checked · 1 error(s)"   (exit=1)
validate-copy --files good.md     -> Passed (exit=0)
check-i18n-parity en.json vi_bad.json -> Failed, exit code 1:
    vi_bad.json:b: error I18N001  missing key in vi_bad.json: 'b'
    vi_bad.json:a: error I18N003  placeholder mismatch in 'a': source=['{name}'] vs target=[]   (exit=1)
check-i18n-parity en.json vi_ok.json  -> Passed (exit=0)
check-font-coverage --files vi.md / good.md -> Passed (exit=0)
```
Font hook bad case: `try-repo` cannot pass `args`, and the default range accepts every Vietnamese codepoint, so no bad case exists through `try-repo`. Bad case proven with a real `.pre-commit-config.yaml` (`repo: <worktree>`, `args: [--from-css, latin.css]`):
```
DESIGN:OS Vietnamese Font & Glyph Coverage Inspector....Failed
- exit code: 1
3 uncovered codepoint(s):  U+1EA1 'ạ', U+1EBF 'ế', U+20AB '₫'
```
README snippet replayed (local path instead of URL, `args: [--domain, ux, --register, ux-microcopy]`, `files:` regex on i18n hook): validate-copy Failed on `bad.md` DATE001 ("4 file(s) checked · 1 error(s)"), i18n and font Passed; `pre-commit run --all-files` exit 1 as expected.

## AC5 gates (after last code edit)
```
python3 -m unittest discover -s tests -v   -> Ran 78 tests, OK (skipped=4), exit 0   [setuptools venv: OK, 0 skipped]
python3 scripts/self_check.py              -> ok: ... self-check passed (16 skills, 18 UKMC.v1 modules), exit 0
python3 tools/sync_shared.py --check       -> 16 skills verified byte-identical to shared/, exit 0
python3 tools/build_examples.py --check    -> 16 skills verified up-to-date, exit 0
python3 tools/verify_ukmc.py               -> files: 18 · anchors: 66 · failures: 0 ... Decision: STOP_SUFFICIENT
```

## AC7 / AC8
- `.github/workflows/ci.yml`: new job `packaging` (py 3.9 + 3.12): fresh venv `pip install .`, smoke the three commands from `$RUNNER_TEMP` (help, >=126 rules, FIN001, bad.md must exit exactly 1 with DATE001, good.md exit 0); on 3.12 installs pre-commit and runs the three hooks via `try-repo` in a scratch consumer repo, requiring failures to contain `DATE001` / `I18N001` (a startup error cannot satisfy it). YAML parsed with PyYAML (jobs: verify, packaging); the consumer step was replayed locally with `uvx pre-commit` (`CI_STEP_OK`). NOT executed on GitHub Actions.
- README.md / README.vi.md: pip/uvx usage + `.pre-commit-config.yaml` snippet; CHANGELOG `## [Unreleased]`. `grep "/Users/\|/home/"` over all touched files: no match.

## Assumptions / caveats
- README snippet uses `rev: main` (no released tag contains the `vi-*` commands; v5.1.0 does not). Confidence high. Flips once a release is tagged: replace with the tag.
- `check-i18n-parity` has no `types`/`files` filter (pre-existing): without `files:` in the consumer config it receives all staged files and argparse exits 2. README documents the `files:` restriction. Not changed (hook semantics were out of scope).
- `build/` / `*.egg-info/` ignore added to `.gitignore` (outside the listed files) as explained above.
- Wheel-layout tests skip when setuptools is missing (system python); CI and any venv with setuptools run them.
- Cleaned up: all scratch venvs, consumer repos, temp copies in the session scratchpad; the worktree's `build/` and `*.egg-info/` were removed.

Status: DONE
Summary: Three console commands + `language: python` hooks implemented; AC1-AC8 evidenced (AC7 CI not run on GitHub, replayed locally). `shared/scripts` untouched, version unchanged.
Concerns/Blockers: none blocking. `.gitignore` edit outside file list; README uses `rev: main` until a tag ships; CI job unverified on real GitHub runners.

## Fix round 1 (review NEEDS_CHANGES: B1, B2, H1)

### B1: dead CI assertion (`.github/workflows/ci.yml`)
Cause: under `bash -e`, a failing non-final command in an `&&` list does not abort, so `test "$status" -eq 1 && grep -q DATE001 bad.out` could never fail the step.
Fix: split into two lines. Sweep of `ci.yml` for the same pattern: three more non-final `&&` chains in the consumer step (`mkdir && cd`, `git init && git config && git config`, `git add && git commit`) split into single commands. Remaining pipes and `||` checked and left alone: `... | grep -q FIN001` (the final command is the assertion), `|| status=$?` (intentional capture), `grep -q "$pattern" || { ...; exit 1; }` (explicit exit).
The replay harness extracts the real step body from `ci.yml` and runs it under `bash -e` against the installed commands.
RED (before fix, `bad.md` mutated to a clean date `25/12/2026`; the step must fail but does not):
```
step rc=0
clean
1 file(s) checked · 0 error(s) · 0 warning(s)
clean
```
GREEN (after fix):
```
== clean bad.md (must be rc!=0)
step rc=1
1 file(s) checked · 0 error(s) · 0 warning(s)
clean
== real bad.md (must be rc=0)
step rc=0
1 file(s) checked · 1 error(s) · 0 warning(s)
1 file(s) checked · 0 error(s) · 0 warning(s)
clean
```

### B2: README `check-i18n-parity` snippet (README.md, README.vi.md)
Fix: `pass_filenames: false` plus `args: [locales/en.json, locales/vi.json]`, with `files:` kept only as the trigger. One explanatory sentence in each README (EN and VI), which also notes source-before-target ordering for Android. `.pre-commit-hooks.yaml` NOT changed: the README fix alone is sufficient (below).
Consumer repo with a real `.pre-commit-config.yaml` (`repo:` = worktree, `rev:` = HEAD SHA), `locales/en.json` and `locales/vi.json` committed in parity.
RED (old snippet; only `vi.json` staged with parity intact, then `vi.json` with a missing key):
```
=== [old] commit changes only vi.json, parity intact
DESIGN:OS Vietnamese i18n Catalog Parity Gate (...).......Failed
- exit code: 2
check_i18n_parity.py: error: both source and target JSON files are required
rc=1
=== [old] vi.json drops key b
- exit code: 2
check_i18n_parity.py: error: both source and target JSON files are required
rc=1
```
GREEN (new snippet):
```
=== [new] commit changes only vi.json, parity intact
DESIGN:OS Vietnamese i18n Catalog Parity Gate (...).......Passed
rc=0
=== [new] vi.json drops key b
- exit code: 1
locales/vi.json:b: error I18N001  missing key in vi.json: 'b'
checked en.json <-> vi.json · 1 error(s) · 0 warning(s)
rc=1
```
Explicit ordered `args` also removes the Android `values-vi/` before `values/` swap, because the pair no longer comes from pre-commit's sorted path order. I did not run an Android consumer case this round (JSON only).

### H1: wheel test did not protect per-skill reference tables
Added `test_wheel_ships_every_per_skill_reference_table_the_runtime_reads`: every `skills/*/references/{glossary,banned-phrases,register-matrix}.md` that exists must be in the built wheel (at least 16 expected).
RED (temporarily deleted the three `*/references/...` globs from `[tool.setuptools.package-data]`, setuptools env):
```
FAIL: test_wheel_ships_every_per_skill_reference_table_the_runtime_reads
AssertionError: Lists differ: ['vi_design_os/skills/vietnamese-business-[3719 chars].md'] != []
Ran 18 tests in 1.308s
FAILED (failures=1)
```
GREEN (`pyproject.toml` restored; `git diff pyproject.toml` empty):
```
Ran 18 tests in 1.347s
OK
```

### Gates after the last edit
```
python3 -m unittest discover -s tests          -> Ran 79 tests, OK (skipped=5), rc=0   [system python, no setuptools]
<setuptools env> -m unittest discover -s tests -> Ran 79 tests, OK (0 skipped), rc=0
python3 scripts/self_check.py                  -> ok: self-check passed (16 skills, 18 UKMC.v1 modules)
python3 tools/sync_shared.py --check           -> 16 skills verified byte-identical to shared/
python3 tools/build_examples.py --check        -> 16 skills verified up-to-date
python3 tools/verify_ukmc.py                   -> verified_claims 19/19 · Decision: STOP_SUFFICIENT
```
Not touched (out of scope): `rev: main`, license field form, `validate-copy` `text` type, font-hook CI bad case, `_load_script` cleanup. `ci.yml` still not run on GitHub. Temp envs and consumers removed.

Status: DONE
Summary: B1, B2 and H1 fixed test-first with RED/GREEN evidence; all gates green after the last edit.
Concerns/Blockers: none new; Android consumer case for B2 not exercised; CI still not run on real runners.
