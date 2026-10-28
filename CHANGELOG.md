# Changelog (`CHANGELOG.md`)

All notable changes to `design-os-vietnamese` are documented in this file.

## [Unreleased]

### Added
- **Writing context (`--context <preset>`)**: a new dimension for one person writing to a specific person, next to `--register` (organisation to customer). Ten presets (`chat-close-friend`, `chat-colleague`, `chat-to-manager`, `email-to-manager`, `email-to-colleague`, `email-to-team`, `email-to-client`, `job-application`, `doc-for-executives`, `doc-for-engineers`) are bundles over five facets in the new `shared/references/context-matrix.md`, synced to every skill. New rules `CTX001`–`CTX005` (forbidden address terms, missing politeness particle, chat abbreviations, missing email greeting/sign-off, missing executive summary). Casual chat presets relax rules that do not suit them (`DIA001`, `CAL001`, `LAW001`, `SYN001`, `NUM004`, `TONE001`, plus `NUM002` for `chat-close-friend` only) while keeping `NFC001`, `ENC001` and `PRO001`. Logic lives in the new `shared/scripts/writing_context.py`, `context_matrix.py` and `context_suggestion.py`, loaded by file path from the repo script, every skill copy and the installed wheel. Presets and word lists are marked `proposed` (convention, not statute).
- Without `--context`, the linter may print one stderr hint (never a finding, never in `--json` stdout, never an exit-code change) when strong signals appear, for example `Kính gửi anh/chị` plus `Em xin…`.
- `evals/contexts/pairs.jsonl`: bad/good pairs for all ten presets plus must-stay-clean casual texts, run by `tests/test_writing_context.py`.
- **Installable console commands**: `pip install` / `uvx` now provides `vi-validate-copy`, `vi-i18n-parity` and `vi-font-coverage` (same flags and exit codes as the `shared/scripts/` checkers). `shared/` and `skills/` rule data ship inside the `vi_design_os` package as siblings, so domain rules and references resolve exactly as in a checkout. Runtime stays standard-library only.
- CI job `packaging`: installs the package into a fresh virtualenv, smokes the three commands from outside the checkout, and runs all three hooks through `pre-commit try-repo` in a scratch consumer repository.
- README (EN/VI): pip/uvx usage and a working `.pre-commit-config.yaml` snippet.

### Fixed
- **pre-commit hooks failed in every consumer repository**: hooks used `language: system` with `entry: python3 shared/scripts/...`, which pre-commit runs in the consumer's working directory (`can't open file`). Hooks now use `language: python` with the `vi-*` commands as entry; hook ids are unchanged.
- **`pip install` installed no code and no commands**: `pyproject.toml` declared `py-modules = []` and no `[project.scripts]`.

## [5.1.0] — 2026-10-27

### Added
- **Multi-Domain Rule Composition (`--domain finance,legal,cybersecurity` & `--domain all`)**: `validate_copy.py` now accepts comma-separated domain lists or `all` to audit hybrid documents (e.g., Bancassurance contracts, PropTech mortgage agreements, or FinTech privacy notices) in a single pass.
- **Stdin (`-`) & Pre-Commit / CI Integration**: Added `validate_copy.py -` stdin support, `.pre-commit-hooks.yaml`, `pyproject.toml`, and `.github/workflows/ci.yml` (Python 3.9/3.11/3.12 matrix).
- **Apple Xcode `.xcstrings` & Android `strings.xml` Parity Support**: `check_i18n_parity.py` now natively parses `.xcstrings` String Catalogs (single-file or dual-file), Android `strings.xml`, nested JSON arrays (`list`), ICU `{count, number}` formatted placeholders, and positional printf tokens (`%1$s`, `%@`).
- **Complete Reference Suites for All 16 Skills**: Added comprehensive `references/glossary.md`, `references/banned-phrases.md`, and `references/qa-checklist.md` across all 6 v5.0 regulated industry skills (`realestate`, `ecommerce`, `gov`, `insurance`, `cybersecurity`, `media`).
- **Statutory Coverage Expansion**: Added `Luật Giao dịch điện tử 2005` / `Luật Viễn thông 2009` detection (`LEG005`, replaced by 2023 Laws) and logistics calque detection (`ECOM005`: `pod`, `awb`, `3pl`, `out for delivery`).

### Fixed (Red Team Hardening)
- **Unicode NFD Normalization Before Rule Evaluation**: `validate_copy.py` now normalizes decomposed NFD lines to NFC in memory immediately after recording `NFC001`, preventing NFD text from bypassing linguistic, calque, tone, pronoun, or statutory regex rules.
- **Vietnamese Thousand Grouping vs Decimal Period (`NUM003`)**: Refined `NUM003` so valid Vietnamese thousand-grouped figures (`5.000 tỷ`, `20.000 m²`, `1.500 điểm`) are never falsely flagged as Anglo-American decimal points.
- **Unaccented Diacritic Detector (`DIA001`)**: Fixed `"thanh cong"` entry in `DIACRITIC_PHRASES` so properly accented `", thành công"` never triggers a false positive.
- **Square/Cubic Meter & Hardware `M2 SSD` Disambiguation (`NUM004`)**: Catches unspaced `50m2` / `120m3` while exempting hardware terms (`Apple M2`, `chip M2`, `Ổ cứng M2 SSD 1TB`).
- **Superlative Ordinals (`LAW001`) & Pronoun Compounds (`PRO002`)**: Exempted ordinal labels (`bước số 1`, `trang số 1`, `phụ lục số 1`, `để có trải nghiệm tốt nhất`) and compound nouns (`người bạn`, `bạn cùng phòng`, `quý công ty`, `quý này`).
- **Code Block & JSON Key Masking (`ICU001`, `ICU002`)**: Masked Markdown fenced code blocks before `ICU001`/`ICU002` checks and masked JSON keys in `.json`/`.xcstrings` files.
- **Negation & Meta-Discourse Context Guard**: Added `_is_negated_or_meta()` across domain rule engines so regulatory explanations (e.g., `"đã bãi bỏ hợp đồng mùa vụ"`, `"không được quảng cáo là thần dược"`) and HTML `<ul>` tags (`FIN008`), student loans (`tín dụng sinh viên`, `EDU005`), or revenue milestones (`Doanh thu đợt 1`, `REA002`) do not trigger false positives.
- **Font Coverage JSON & Non-Latin Symbol Filtering (`check_font_coverage.py`)**: Added `--json` output and `--strict-symbols` so Markdown arrows (`→`) and emojis (`✅`) do not trigger false font subset failures by default.

## [5.0.0] — 2026-10-26

### Added
- **Multi-Industry Expansion to 16 Production Skills**: Added 6 regulated Vietnamese industry skills:
  - `vietnamese-real-estate-construction` (`REA001`–`REA006`): Law on Real Estate Business 2023 (5% deposit cap Art. 23, 30%/70%/95% off-plan payment schedule Art. 25), Land Law 2024 (official certificate title & condotel/officetel tenure), Housing Law 2023 (`thông thủy` vs `tim tường` Art. 141 & 2% maintenance fund Art. 152), and Construction BOQ (Decree 37/2015/NĐ-CP).
  - `vietnamese-ecommerce-retail` (`ECOM001`–`ECOM006`): Decrees 52/2013 & 85/2021 (`Đã thông báo BCT` vs `Đã đăng ký BCT`), Decrees 81/2018 & 128/2024 (50% promotion discount cap), Consumer Protection Law 2023 (return/COD inspection rights & anti-dark-patterns), and Decrees 43/2017 & 111/2021 product labeling.
  - `vietnamese-government-public-service` (`GOV001`–`GOV006`): Decree 42/2022 (`DVC trực tuyến toàn trình` & `một phần`), Law on Identification 2023 (`Thẻ căn cước` & expiration of 9-digit CMND), Decree 69/2024 (`VNeID Mức độ 1 / Mức độ 2`), and Law on Residence 2020 (abolition of paper `Sổ hộ khẩu`).
  - `vietnamese-insurance-insurtech` (`INS001`–`INS006`): Law on Insurance Business 2022 & Circular 67/2023/TT-BTC (ban on disguising investment-linked insurance as fixed-interest deposits, 21-day free-look period Art. 35, affirmative exclusion disclosure Art. 19, 15-day claim payout Art. 31, and bancassurance anti-coercion).
  - `vietnamese-cybersecurity-infosec` (`SEC001`–`SEC006`): Decree 13/2023/NĐ-CP Article 23 (<=72-hour personal data breach reporting to A05 Ministry of Public Security & Sensitive vs Basic data classification), Decree 85/2016 & Circular 12/2022/TT-BTTTT (`ATTT Cấp độ 1–5`), and VNCERT/NCSC CVE advisory standards.
  - `vietnamese-media-journalism-pr` (`MEDJ001`–`MEDJ006`): Press Law 2016 & Decree 147/2024/NĐ-CP (Press Agency vs ICP distinction, Article 42 correction formatting, Article 9 presumption of innocence `nghi phạm / bị can / bị cáo`), Law on Children 2016 Article 21 (<16 child anonymization), and Crisis PR standards.
- **31 Audience Registers, 126 Deterministic Rules, 18 UKMC.v1 Modules & 489 Golden Evaluation Pairs**: Expanded `register-matrix.md`, `validate_copy.py`, `knowledge/` (`66 anchors`, `STOP_SUFFICIENT`), and `evals/*/pairs.jsonl` (150 new golden pairs across the 6 new domains).
- **Resolved All Issue #2 QA Findings**: Fixed `--domain` `SKILL_DIR` binding, `CAL001` span deduplication, `--output` parent directory creation & single-file guard, license wording parity (`source-available`), and removed personal workstation paths.

## [4.0.0] — 2026-10-26

### Added
- **Multi-Industry Expansion to 10 Production Skills**: Added `vietnamese-healthcare-copy` (`MED001`–`MED007`), `vietnamese-legal-contracts` (`LEG001`–`LEG007`), `vietnamese-hospitality-travel` (`HOS001`–`HOS006`), and `vietnamese-hr-recruitment` (`HR001`–`HR006`).
- **Full 7-Tier Vietnamese Pedagogy Continuum**: Upgraded `vietnamese-education-copy` (`EDU001`–`EDU012`, 46 golden pairs) covering Preschool (`Mầm non: Nhà trẻ 3–36 tháng & Mẫu giáo 3–6 tuổi` — VBHN 01/VBHN-BGDĐT), Primary (TT 27/2020), Secondary/High School (TT 22/2021), TVET (TT 04/2022), Undergraduate VQF Level 6 (TT 08/2021), Master's VQF Level 7 (TT 23/2021), and Doctoral VQF Level 8 + `GS./PGS.` Academic Ranks (TT 18/2021 & QĐ 37/2018/QĐ-TTg).
- **24 Audience Registers & 339 Golden Evaluation Pairs**: Expanded `register-matrix.md` and `validate_copy.py` to 24 registers and 339 benchmark pairs across `evals/*/pairs.jsonl`.
- **12 UKMC.v1 Cryptographic Knowledge Modules**: Added 4 new verified modules in `knowledge/` (`53 anchors`, `STOP_SUFFICIENT`) and portable `tools/verify_ukmc.py`.
- **9-Tier GitHub Pages Site & 5-Layer AI-Ready Delivery Package**: Added `docs/index.html`, `docs/cookbook.md`, `llms.txt`, `.claude-plugin`, `.codex-plugin`, `.agents`, `.factory-plugin`, `/doctor`, and `scripts/self_check.py`.
- **Resolved All PR #1 QA Findings (`F-01`–`F-06`)**: Added `shared/references/{glossary,banned-phrases}.md`, `--domain`, `--output`, `--source/--target` CLI flags, and standardized on `PolyForm Shield License 1.0.0`.
