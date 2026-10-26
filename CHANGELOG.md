# Changelog (`CHANGELOG.md`)

All notable changes to `design-os-vietnamese` are documented in this file.

## [4.0.0] — 2026-10-26

### Added
- **Multi-Industry Expansion to 10 Production Skills**: Added `vietnamese-healthcare-copy` (`MED001`–`MED007`), `vietnamese-legal-contracts` (`LEG001`–`LEG007`), `vietnamese-hospitality-travel` (`HOS001`–`HOS006`), and `vietnamese-hr-recruitment` (`HR001`–`HR006`).
- **Full 7-Tier Vietnamese Pedagogy Continuum**: Upgraded `vietnamese-education-copy` (`EDU001`–`EDU012`, 46 golden pairs) covering Preschool (`Mầm non: Nhà trẻ 3–36 tháng & Mẫu giáo 3–6 tuổi` — VBHN 01/VBHN-BGDĐT), Primary (TT 27/2020), Secondary/High School (TT 22/2021), TVET (TT 04/2022), Undergraduate VQF Level 6 (TT 08/2021), Master's VQF Level 7 (TT 23/2021), and Doctoral VQF Level 8 + `GS./PGS.` Academic Ranks (TT 18/2021 & QĐ 37/2018/QĐ-TTg).
- **24 Audience Registers & 339 Golden Evaluation Pairs**: Expanded `register-matrix.md` and `validate_copy.py` to 24 registers and 339 benchmark pairs across `evals/*/pairs.jsonl`.
- **12 UKMC.v1 Cryptographic Knowledge Modules**: Added 4 new verified modules in `knowledge/` (`53 anchors`, `STOP_SUFFICIENT`) and portable `tools/verify_ukmc.py`.
- **9-Tier GitHub Pages Site & 5-Layer AI-Ready Delivery Package**: Added `docs/index.html`, `docs/cookbook.md`, `llms.txt`, `.claude-plugin`, `.codex-plugin`, `.agents`, `.factory-plugin`, `/doctor`, and `scripts/self_check.py`.
- **Resolved All PR #1 QA Findings (`F-01`–`F-06`)**: Added `shared/references/{glossary,banned-phrases}.md`, `--domain`, `--output`, `--source/--target` CLI flags, and standardized on `PolyForm Shield License 1.0.0`.
