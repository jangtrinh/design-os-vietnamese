# Changelog (`CHANGELOG.md`)

All notable changes to `design-os-vietnamese` are documented in this file.

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
