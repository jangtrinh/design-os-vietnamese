# DESIGN:OS Vietnamese — UKMC.v1 Verified Knowledge Base (12 Modules)

This directory contains the cryptographically provenance-pinned **Universal Knowledge Master Contract (UKMC.v1)** modules powering **DESIGN:OS Vietnamese**, verified and gated by `design-os-knowledge-builder`.

## Modules (12 Verified Modules)

| ID | File | Domain | Trust Tier |
|---|---|---|---|
| `unicode-and-phonology` | `unicode-and-phonology.md` | `vietnamese-language-engineering` | `verified` |
| `register-and-pragmatics` | `register-and-pragmatics.md` | `vietnamese-pragmatics-and-ux` | `verified` |
| `locale-and-icu-engineering` | `locale-and-icu-engineering.md` | `vietnamese-i18n-and-localization` | `verified` |
| `statutory-compliance-vi` | `statutory-compliance-vi.md` | `vietnamese-legal-and-regulatory-compliance` | `verified` |
| `typography-and-vertical-metrics` | `typography-and-vertical-metrics.md` | `vietnamese-typography-and-design-systems` | `verified` |
| `b2b-zns-and-admin-comms` | `b2b-zns-and-admin-comms.md` | `vietnamese-business-and-administrative-comms` | `verified` |
| `finance-tt99-and-fintech` | `finance-tt99-and-fintech.md` | `vietnamese-finance-and-accounting` | `verified` |
| `education-moet-and-edtech` | `education-moet-and-edtech.md` | `vietnamese-education-and-edtech` (7-Tier: Mầm non -> Tiến sĩ & GS/PGS) | `verified` |
| `healthcare-by-law-and-emr` | `healthcare-by-law-and-emr.md` | `vietnamese-healthcare-and-pharma` | `verified` |
| `legal-contracts-civil-commercial` | `legal-contracts-civil-commercial.md` | `vietnamese-legal-and-contracts` | `verified` |
| `hospitality-aviation-tourism` | `hospitality-aviation-tourism.md` | `vietnamese-hospitality-and-travel` | `verified` |
| `hr-labor-code-and-bhxh` | `hr-labor-code-and-bhxh.md` | `vietnamese-hr-and-recruitment` | `verified` |

## Verification Commands

```bash
# 1. Self-contained UKMC.v1 verifier (zero external dependencies)
python3 tools/verify_ukmc.py

# 2. Optional: verify/index/gate via external design-os-knowledge-builder checkout
PYTHONPATH="${KNOWLEDGE_BUILDER_SRC:-../design-os-knowledge-builder}/src" \
  python3 -m knowledge_builder.cli verify ./knowledge --claims

PYTHONPATH="${KNOWLEDGE_BUILDER_SRC:-../design-os-knowledge-builder}/src" \
  python3 -m knowledge_builder.cli index --root ./knowledge

PYTHONPATH="${KNOWLEDGE_BUILDER_SRC:-../design-os-knowledge-builder}/src" \
  python3 -m knowledge_builder.cli gate --root ./knowledge --run-id vn-design-os-261026
```
