# DESIGN:OS Vietnamese — UKMC.v1 Verified Knowledge Base

This directory contains the cryptographically provenance-pinned **Universal Knowledge Master Contract (UKMC.v1)** modules powering **DESIGN:OS Vietnamese**, verified and gated by `design-os-knowledge-builder`.

## Modules

| ID | File | Domain | Trust Tier |
|---|---|---|---|
| `unicode-and-phonology` | `unicode-and-phonology.md` | `vietnamese-language-engineering` | `verified` |
| `register-and-pragmatics` | `register-and-pragmatics.md` | `vietnamese-pragmatics-and-ux` | `verified` |
| `locale-and-icu-engineering` | `locale-and-icu-engineering.md` | `vietnamese-i18n-and-localization` | `verified` |
| `statutory-compliance-vi` | `statutory-compliance-vi.md` | `vietnamese-legal-and-regulatory-compliance` | `verified` |
| `typography-and-vertical-metrics` | `typography-and-vertical-metrics.md` | `vietnamese-typography-and-design-systems` | `verified` |
| `b2b-zns-and-admin-comms` | `b2b-zns-and-admin-comms.md` | `vietnamese-business-and-administrative-comms` | `verified` |
| `finance-tt99-and-fintech` | `finance-tt99-and-fintech.md` | `vietnamese-finance-and-accounting` | `verified` |
| `education-moet-and-edtech` | `education-moet-and-edtech.md` | `vietnamese-education-and-edtech` | `verified` |

## Verification Commands

```bash
PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli verify /Users/jangtrinh/Products/design-os-vietnamese/knowledge --claims

PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli index --root /Users/jangtrinh/Products/design-os-vietnamese/knowledge

PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli gate --root /Users/jangtrinh/Products/design-os-vietnamese/knowledge --run-id vn-design-os-261026
```
