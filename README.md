# DESIGN:OS Vietnamese (`vi-VN`) — v4.0 Multi-Industry Suite

> **Sovereign Vietnamese Language, Typography, UX Design System, Multi-Industry Copywriting, 7-Tier Pedagogy (Mầm non → Tiến sĩ), & Statutory Compliance Suite for AI Coding Agents**
> Built on **DESIGN:OS** and verified with the **Universal Knowledge Master Contract (`UKMC.v1`)** epistemic pipeline.

[![Schema: UKMC.v1](https://img.shields.io/badge/Knowledge_Schema-UKMC.v1_Verified-10B981)](knowledge/)
[![Skills: 10 Production](https://img.shields.io/badge/Skills-10_Production-3B82F6)](skills/)
[![Registers: 24 Profiles](https://img.shields.io/badge/Registers-24_Audience_Profiles-8B5CF6)](shared/references/register-matrix.md)
[![Gate: STOP_SUFFICIENT](https://img.shields.io/badge/Epistemic_Gate-STOP__SUFFICIENT-F59E0B)](knowledge/_evidence/vn-design-os-261026/state.json)
[![License: PolyForm Shield 1.0.0](https://img.shields.io/badge/License-PolyForm_Shield_1.0.0-111827)](LICENSE)

[Tiếng Việt (`README.vi.md`)](README.vi.md)

![DESIGN:OS Vietnamese v4.0 Multi-Industry Architecture](assets/design-os-vietnamese-architecture.svg)

---

## Why DESIGN:OS Vietnamese?

Generic LLMs treat Vietnamese (`vi-VN`) as word-by-word translated English. In production software and regulated industries, that creates four systemic failure modes:

1. **Translationese & Syntactic Calques**: Literal English-to-Vietnamese phrasing (*"Làm ơn nhập của bạn mật khẩu"*, *"Như một người dùng, tôi muốn..."*, *"Thực hiện một quyết định"*) that immediately breaks native trust.
2. **Stacked Diacritic Clipping & UI Expansion**: Vietnamese combines base vowels with circumflex/breve/horn modifiers (`ă, â, ê, ô, ơ, ư`) and five tone marks (`Ấ, Ệ, Ữ, Ợ`), increasing vertical glyph bounds by **25–35%** and expanding string length by **22–38%** over English. Standard `line-height: 1.2` and fixed-width English buttons clip accents or overflow containers.
3. **Encoding & ICU Localization Bugs**: Decomposed Unicode `NFD` from macOS clipboard/filesystems breaks search and regex; `one`/`other` ICU plural branches fail because Vietnamese uses only `other` (`CLDR`).
4. **Statutory & Multi-Industry Regulatory Violations**:
   - **Advertising & E-commerce**: Unsubstantiated superlatives (*"số 1"*, *"tốt nhất"*, *"duy nhất"*) violate **Luật Quảng cáo 2012 (sửa đổi bởi Luật số 75/2025/QH15)**.
   - **7-Tier Education Continuum (Mầm non → Tiến sĩ)**: Confusing Preschool developmental domains (**VBHN 01/VBHN-BGDĐT**), Primary 3-tier assessment (**Thông tư 27/2020/TT-BGDĐT**), Secondary 4-tier assessment (**Thông tư 22/2021/TT-BGDĐT**), TVET modules (**Thông tư 04/2022/TT-BLĐTBXH**), and Higher-Ed/Postgraduate theses (*Khóa luận cử nhân* vs *Luận văn thạc sĩ* vs *Luận án tiến sĩ*; *Học vị* `TS.` vs *Học hàm* `GS./PGS.`).
   - **Healthcare, Legal, Hospitality & HR**: Missing mandatory TPCN disclaimers (**Nghị định 15/2018/NĐ-CP**), commercial contract penalty caps over 8% (**Luật Thương mại 2005 Điều 301**), opaque hotel `++` pricing, or discriminatory job descriptions and sub-85% probation wages (**Bộ luật Lao động 2019 Điều 8, Điều 26**).

---

## Architecture: 10 Production Skills + 12 UKMC.v1 Knowledge Modules

| # | Skill | Domain & Target Artifacts | Domain Rule Engine | Key Reference Modules |
|---|---|---|---|---|
| **1** | [`vn-design-system-ux`](skills/vn-design-system-ux/SKILL.md) | **Design Tokens, Typography, UI Microcopy & i18n**: line-height gates, character caps, empty/loading/error states, passkeys, AI streaming UX, `U+00A0` compound-word binding | `rules_ux.py` (`UX001`–`UX010`) | `design-tokens-vi.md`, `microcopy-states.md`, `glossary.md`, `banned-phrases.md` |
| **2** | [`vietnamese-landing-copy`](skills/vietnamese-landing-copy/SKILL.md) | **Landing Pages, SaaS, E-Commerce & Real Estate**: Hero formulas, value props, pricing tables, CTAs, Luật Quảng cáo 75/2025 & NĐ 98/2020 compliance | `rules_landing.py` (`LND001`–`LND007`) | `vertical-playbooks.md`, `legal-copy.md`, `register-guide.md`, `examples.md` |
| **3** | [`vietnamese-tech-writing`](skills/vietnamese-tech-writing/SKILL.md) | **Developer Docs, API Specs, Runbooks, Changelogs, ADRs & Surveys**: Code-switching rules, CLI/SDK docs, postmortems, Likert scales | `rules_tech.py` (`TECH001`–`TECH006`) | `code-switching.md`, `i18n-hazards.md`, `survey-design.md`, `doc-registers.md` |
| **4** | [`vietnamese-business-comms`](skills/vietnamese-business-comms/SKILL.md) | **B2B Emails, Zalo OA/ZNS, Proposals & Administrative *Công văn***: Nghị định 30/2020/NĐ-CP format, Nghị định 13/2023/NĐ-CP PDPD consent | `rules_business.py` (`BIZ001`–`BIZ007`) | `admin-decree-30.md`, `b2b-xung-ho.md`, `channel-guide.md`, `promo-law.md` |
| **5** | [`vietnamese-finance-copy`](skills/vietnamese-finance-copy/SKILL.md) | **Fintech, Banking, Tax, Invoices & Financial Reports**: Thông tư 99/2025/TT-BTC (replacing TT 200), Nghị định 70/2025/NĐ-CP e-invoices, VietQR/Napas | `rules_finance.py` (`FIN001`–`FIN006`) | `fintech-ekyc-vietqr.md`, `statement-formatting.md`, `statement-terminology.md`, `financial-promotion.md` |
| **6** | [`vietnamese-education-copy`](skills/vietnamese-education-copy/SKILL.md) | **Full 7-Tier Pedagogy Continuum (Mầm non → Tiểu học → THCS/THPT → GDNN → Đại học → Thạc sĩ → Tiến sĩ & GS/PGS)**: VBHN 01, TT 27/2020, TT 22/2021, TT 04/2022, TT 08/2021, TT 23/2021, TT 18/2021, QĐ 37/2018 | `rules_education.py` (`EDU001`–`EDU012`) | `preschool-to-postgrad-continuum.md`, `grading-terminology.md`, `edtech-pedagogy.md`, `doc-registers.md` |
| **7** | [`vietnamese-healthcare-copy`](skills/vietnamese-healthcare-copy/SKILL.md) | **Clinical EMR, E-Prescriptions, Hospital Discharge & Pharma/TPCN Compliance**: Luật KCB 15/2023/QH15, TT 32/2023/TT-BYT, NĐ 15/2018/NĐ-CP | `rules_healthcare.py` (`MED001`–`MED007`) | `clinical-and-emr-writing.md`, `pharma-and-tpcn-compliance.md`, `patient-communication.md`, `qa-checklist.md` |
| **8** | [`vietnamese-legal-contracts`](skills/vietnamese-legal-contracts/SKILL.md) | **Civil, Commercial & Labor Contracts, NDAs, Terms of Service & Privacy Notices**: BLDS 2015, Luật Thương mại 2005 (8% penalty cap), Luật BVQLNTD 2023 | `rules_legal.py` (`LEG001`–`LEG007`) | `contract-drafting-blds-ltt.md`, `labor-and-ip-clauses.md`, `pdpd-and-consumer-protection.md` |
| **9** | [`vietnamese-hospitality-travel`](skills/vietnamese-hospitality-travel/SKILL.md) | **5-Star Hotels, Resorts, Aviation, OTA Booking & Culinary/F&B**: Luật Du lịch 2017 (Điều 50), transparent `++` pricing, TT 14/2015 & 19/2023 aviation rights | `rules_hospitality.py` (`HOS001`–`HOS006`) | `hotel-and-resort-standards.md`, `aviation-and-tour-policies.md`, `fnb-and-culinary-copy.md` |
| **10** | [`vietnamese-hr-recruitment`](skills/vietnamese-hr-recruitment/SKILL.md) | **Job Descriptions (JD), Offer Letters, Labor Contracts, Probation & BHXH/PIT**: Bộ luật Lao động 2019 (Điều 8, 17, 20, 25, 26), Luật BHXH 41/2024/QH15 | `rules_hr.py` (`HR001`–`HR006`) | `labor-code-and-offer-letters.md`, `jd-and-employer-branding.md`, `okr-kpi-and-performance-review.md` |

---

## Deterministic Tooling & Static Linters

Every skill bundles three zero-dependency Python 3.9+ CLI tools synchronized from [`shared/scripts/`](shared/scripts/):

### 1. `validate_copy.py` — Universal + Domain-Specific Vietnamese Copy Linter

Detects **18 universal rules** plus **70+ domain rules** across all 10 skills:

| Rule Code | Severity | Check Description |
|---|---|---|
| `NFC001` | `ERROR` | Detects decomposed Unicode `NFD` combining marks (`--fix` auto-normalizes to `NFC`) |
| `ENC001` | `ERROR` | Detects UTF-8 Mojibake (`Ã¡`, `áº¡`, `Æ°`, `Ä‘`) and legacy VNI/TCVN3 corruption |
| `CAL001` | `ERROR`/`WARN` | Flags literal English-to-Vietnamese calques (`làm ơn nhập của bạn mật khẩu`, `như một...`, `thực hiện việc...`) |
| `SYN001` | `WARN` | Flags syntactic translationese word order and passive `bị`/`được` misuse |
| `LAW001` | `ERROR` | Flags unsubstantiated superlatives (`số 1`, `tốt nhất`, `duy nhất`, `100%`) unless backed by `<!-- proof: ... -->` or negated |
| `DIA001` | `ERROR` | Detects unaccented Vietnamese prose across 140+ multi-word phrases |
| `TONE001` | `WARN` | Enforces document-wide consistency between `kiểu mới` (`hoà, thuỷ`) and `kiểu cũ` (`hòa, thủy`) (`--fix-tone new\|old`) |
| `NUM001`–`NUM004` | `ERROR`/`WARN` | Period thousands (`1.250.000 ₫`), comma decimals (`3,5%`), and superscript `m²`/`m³` (with hardware chip guard for `Apple M2/M3`, `SSD M.2`, `BMW M2/M3`) |
| `DATE001` / `PHONE001` | `ERROR` | Flags US `MM/dd/yyyy` dates and redundant trunk zero `+84 (0)9...` |
| `ICU001` / `ICU002` | `ERROR` | Multi-line ICU plural block parser (`other`-only) and translated placeholder detector (`{tên}`) |
| `PRO001` / `PRO002` | `ERROR`/`WARN` | Enforces pronoun consistency across **24 audience registers** (`ux-microcopy`, `edu-preschool`, `edu-postgrad`, `healthcare-clinical`, `legal-contract`, `hospitality-luxury`, `hr-candidate`, etc.) |

```bash
# Validate a Vietnamese UI or Markdown file with domain & register rules
python3 shared/scripts/validate_copy.py path/to/copy.md --domain ux --register ux-microcopy

# Auto-fix decomposed NFD Unicode and normalize tone marks to kiểu mới (hoà, thuỷ)
python3 shared/scripts/validate_copy.py path/to/copy.md --fix --fix-tone new --output path/to/copy.clean.md

# Validate a 7-tier education document (e.g., Preschool report or Doctoral dissertation)
python3 skills/vietnamese-education-copy/scripts/validate_copy.py path/to/de-cuong.md --doctype doctoral-dissertation --register edu-postgrad

# Validate a clinical or TPCN healthcare document
python3 skills/vietnamese-healthcare-copy/scripts/validate_copy.py path/to/tpcn.md --doctype tpcn-ad --register healthcare
```

### 2. `check_i18n_parity.py` — `en.json` ↔ `vi.json` Catalog & UI Expansion Gate

```bash
python3 shared/scripts/check_i18n_parity.py \
  --source skills/vn-design-system-ux/assets/en.sample.json \
  --target skills/vn-design-system-ux/assets/vi.sample.json \
  --json
```

### 3. `check_font_coverage.py` — Vietnamese 134-Glyph Precomposed Coverage Auditor

```bash
python3 shared/scripts/check_font_coverage.py --css path/to/tokens.css
```

---

## UKMC.v1 Cryptographic Knowledge Base (`knowledge/`)

All 12 foundational knowledge documents in [`knowledge/`](knowledge/) are compiled and audited under the **Universal Knowledge Master Contract (`UKMC.v1`)** with SHA-256 source provenance and inline `[ev:...]` evidence anchors:

```bash
# Run the portable UKMC.v1 claim verifier and Epistemic Stopping Gate (STOP_SUFFICIENT)
python3 tools/verify_ukmc.py
```

---

## Testing & Verification Suite

Run the full unit test, golden evaluation (`310+ pairs.jsonl`), skill specification, QA regression, and UKMC.v1 verification suite:

```bash
python3 -m unittest discover -s tests -v
python3 tools/sync_shared.py --check
python3 tools/build_examples.py --check
```

---

## License

Released under the [PolyForm Shield License 1.0.0](LICENSE). Copyright © 2026 DESIGN:OS (Jang Trinh).
