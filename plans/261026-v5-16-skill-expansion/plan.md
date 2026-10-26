# Implementation Plan — DESIGN:OS Vietnamese v5.0 (16-Skill Multi-Industry Expansion)

## Agreed Seams Under Test
1. **CLI Domain & Rule Engine Seam (`validate_copy.py --domain <d>`)**: 16 domains, 31 registers, 126 rules.
2. **Golden Evaluation Benchmark Seam (`evals/*/pairs.jsonl`)**: 489 pairs across 16 skills.
3. **UKMC.v1 Provenance Seam (`tools/verify_ukmc.py`)**: 18 verified knowledge modules.
4. **Repository Delivery & Self-QA Seam (`tests/test_qa_*.py`, `verify-repo-delivery.py`, `seo-aeo-geo-harness.py`)**.

## Vertical Slices

### Slice 1: Core Engine & Shared Registry Upgrade (Argon 4 Controller)
- Update `shared/scripts/validate_copy.py` (`DOMAIN_SKILL_MAP` with all 16 skills and aliases, `DEFAULT_REGISTERS` with 31 registers).
- Update `shared/references/register-matrix.md` with the 7 new audience registers (`realestate-luxury`, `construction-b2b`, `ecommerce-shopper`, `public-citizen`, `insurance-policyholder`, `infosec-advisory`, `crisis-comms`).
- Update `tools/sync_shared.py`, `tools/build_examples.py`, and `scripts/self_check.py` to include all 16 skills.

### Slice 2: Parallel 6-Skill, 6-UKMC Module & 150-Eval Pair Construction (3 Gemini 3.8 Flash Workers)
- **Worker A (Flash)**:
  - `skills/vietnamese-real-estate-construction/` (`rules_realestate.py`: `REA001`–`REA006`, `references/luat-kdbds-2023-nha-o-dat-dai-2024.md`, `glossary.md`, `banned-phrases.md`, `SKILL.md`)
  - `skills/vietnamese-ecommerce-retail/` (`rules_ecommerce.py`: `ECOM001`–`ECOM006`, `references/tmdt-nd85-bvqlntd-2023-logistics.md`, `glossary.md`, `banned-phrases.md`, `SKILL.md`)
  - `evals/vietnamese-real-estate-construction/pairs.jsonl` (25 pairs) & `evals/vietnamese-ecommerce-retail/pairs.jsonl` (25 pairs)
  - `knowledge/real-estate-and-construction-law.md` & `knowledge/ecommerce-retail-and-consumer-law.md` (UKMC.v1 verified)
- **Worker B (Flash)**:
  - `skills/vietnamese-government-public-service/` (`rules_gov.py`: `GOV001`–`GOV006`, `references/dich-vu-cong-nd42-de-an-06-vneid.md`, `glossary.md`, `banned-phrases.md`, `SKILL.md`)
  - `skills/vietnamese-insurance-insurtech/` (`rules_insurance.py`: `INS001`–`INS006`, `references/luat-kdbh-2022-tt67-2023-btc.md`, `glossary.md`, `banned-phrases.md`, `SKILL.md`)
  - `evals/vietnamese-government-public-service/pairs.jsonl` (25 pairs) & `evals/vietnamese-insurance-insurtech/pairs.jsonl` (25 pairs)
  - `knowledge/egovernment-dvc-and-vneid.md` & `knowledge/insurance-law-and-insurtech.md` (UKMC.v1 verified)
- **Worker C (Flash)**:
  - `skills/vietnamese-cybersecurity-infosec/` (`rules_cybersecurity.py`: `SEC001`–`SEC006`, `references/attt-cap-do-1-5-nd13-soc-pentest.md`, `glossary.md`, `banned-phrases.md`, `SKILL.md`)
  - `skills/vietnamese-media-journalism-pr/` (`rules_media.py`: `MEDJ001`–`MEDJ006`, `references/luat-bao-chi-2016-nd147-2024-pr.md`, `glossary.md`, `banned-phrases.md`, `SKILL.md`)
  - `evals/vietnamese-cybersecurity-infosec/pairs.jsonl` (25 pairs) & `evals/vietnamese-media-journalism-pr/pairs.jsonl` (25 pairs)
  - `knowledge/cybersecurity-attt-and-pdpd.md` & `knowledge/media-journalism-and-crisis-pr.md` (UKMC.v1 verified)

### Slice 3: Sync, Examples Generation, Docs/Pages Upgrade, Full Review Gate & Release v5.0.0
- Run `python3 tools/sync_shared.py` and `python3 tools/build_examples.py`.
- Update `README.md`, `README.vi.md`, `docs/index.html`, `docs/cookbook.md`, `llms.txt`, `docs/llms.txt`, `knowledge/README.md`, plugin manifests, and SVG/PNG architecture diagram (`16 Production Skills`).
- Run `es:review-gate --full` with independent verifier subagent, verify all tests (`42/42` across 16 skills & 489 eval pairs), capture fresh visual screenshot, push to `main`, and publish Release `v5.0.0`.
