# DESIGN:OS Vietnamese (`design-os-vietnamese`)

> **Sovereign Vietnamese Language, Typography, UX Writing, Statutory Compliance & UKMC.v1 Knowledge Suite for AI Agents & Design Systems.**
>
> Built and maintained by **Jang Trinh / DESIGN:OS** (`https://github.com/jangtrinh/design-os-vietnamese`).

[![UKMC.v1 Verified](https://img.shields.io/badge/UKMC.v1-STOP__SUFFICIENT-10b981)](#ukmcv1-cryptographically-verified-knowledge-base)
[![Skills](https://img.shields.io/badge/Skills-6%20Production%20Modules-2563eb)](#the-6-production-skills)
[![Validator](https://img.shields.io/badge/Engine-validate__copy.py%20v3.0-f59e0b)](#deterministic-validation--tooling-suite)
[![License: MIT](https://img.shields.io/badge/License-MIT-zinc.svg)](LICENSE)

[Tiếng Việt (`README.vi.md`)](README.vi.md)

---

## Why DESIGN:OS Vietnamese?

Generic LLM outputs in Vietnamese suffer from systematic failure modes that break production interfaces, violate Vietnamese statutory regulations, and erode user trust:

1. **English-to-Vietnamese Calques (`CAL001`, `SYN001`):** Word-by-word translations (`"Làm ơn nhập của bạn mật khẩu"`, `"Đơn hàng của bạn đã bị hủy thành công"`) confuse adversity passive (`bị`) with beneficiary passive (`được`) and violate head-first Vietnamese noun phrase syntax.
2. **Stacked Diacritic Vertical Clipping:** Uppercase and lowercase Vietnamese vowels with circumflex/horn/breve plus tone marks (`Ẫ, Ễ, Ổ, Ữ, Ệ, Ộ`) extend `25%–38%` above the Latin cap-height and into the descender zone. Applying English-tuned tight line-heights (`leading-none`, `leading-tight`) or `overflow: hidden` slices off tone marks, while omitting the `'vietnamese'` font subset triggers "ransom-note" browser fallback.
3. **Unicode NFD & Telex/VNI IME Hazards (`NFC001`, `ENC001`):** macOS APFS file names, Google Docs, and PDF exports emit decomposed NFD sequences (`o + U+0302 + U+0309`) that break database queries and detach diacritics. Unfiltered React `onChange` mutations during active Telex/VNI composition (`event.nativeEvent.isComposing`) corrupt user input into `"Tiênsg Viêjt"`.
4. **CLDR `vi-VN` & Multi-Line ICU MessageFormat Defects (`ICU001`, `ICU002`, `NUM001–NUM004`):** Copy-pasted English `one`/`other` plural branches in `.arb`/`.json` localization catalogs, unformatted VND currency (`50000đ`, `1.5M VND`), and naive unit regexes that falsely flag hardware processors (`Apple M2`, `MacBook Air M2`) as square meters (`m²`).
5. **2025–2026 Vietnamese Statutory & Regulatory Non-Compliance (`LAW001`, `FIN001`, `EDU001`, `BIZ001`):**
   - **Advertising Law 2012 & Law No. 75/2025/QH15** (effective `01/01/2026`): Prohibits unverified superlatives (`nhất`, `duy nhất`, `tốt nhất`, `số 1`) and mandates influencer (KOL/KOC) sponsorship disclosure.
   - **Decree 13/2023/NĐ-CP (PDPD):** Requires explicit 6-element consent and dual parent + child verification for ages `7` to under `16` (Article 20).
   - **Circular 99/2025/TT-BTC** (effective `01/01/2026`, superseding Circular 200/2014/TT-BTC): Renames *Bảng cân đối kế toán* to **Báo cáo tình hình tài chính** and introduces Accounts `215` (Biological Assets), `332` (Dividends Payable), and `82112` (Pillar Two Global Minimum Tax).
   - **MOET Circular 22/2021/TT-BGDĐT (GDPT 2018):** Replaces legacy *Học lực Giỏi/Tiên tiến/Yếu/Kém* with **Tốt — Khá — Đạt — Chưa đạt**.
   - **Decree 30/2020/NĐ-CP & Decree 91/2020/NĐ-CP:** Governs clerical document headers (`Công văn`, `Tờ trình`, `Quyết định`, `Biên bản`) and Zalo Notification Service (ZNS) anti-spam tagging.

---

## The 6 Production Skills

| Skill | Domain Scope | Domain Rule Engine | Key References & Assets |
|---|---|---|---|
| [`vn-design-system-ux`](skills/vn-design-system-ux/SKILL.md) | Product UI, UX writing, microcopy states, design tokens (`Be Vietnam Pro`), Telex/VNI IME safety, i18n parity (`.json`/`.arb`) | `rules_ux.py` (`UX001`–`UX006`) | `glossary.md`, `banned-phrases.md`, `microcopy-states.md`, `design-tokens-vi.md`, `design-tokens.vi.json` |
| [`vietnamese-landing-copy`](skills/vietnamese-landing-copy/SKILL.md) | SaaS & e-commerce landing pages, Hero/CTA hierarchy, VND pricing tables, PDPD consent, Decree 81/128 promo caps | `rules_landing.py` (`LAND001`–`LAND003`) | `section-playbook.md`, `promo-law.md`, `cta-library.md`, `headline-formulas.md` |
| [`vietnamese-tech-writing`](skills/vietnamese-tech-writing/SKILL.md) | Developer docs, API references, ADRs, Runbooks, Post-mortems, Changelogs, code-switching rules | `rules_tech.py` (`TECH001`–`TECH003`) | `terminology.md`, `doc-patterns.md`, `error-messages.md`, `release-notes-and-rca.md` |
| [`vietnamese-business-comms`](skills/vietnamese-business-comms/SKILL.md) | Decree 30/2020/NĐ-CP administrative documents (`Công văn`, `Tờ trình`, `Quyết định`, `Biên bản`), B2B emails, Zalo ZNS | `rules_biz.py` (`BIZ001`–`BIZ005`) | `cong-van-format.md`, `email-etiquette.md`, `zalo-zns-patterns.md`, 6 `.md.template` assets |
| [`vietnamese-finance-copy`](skills/vietnamese-finance-copy/SKILL.md) | Retail banking, Napas 247 / VietQR, securities, insurance, Circular 99/2025/TT-BTC accounting & ERP | `rules_finance.py` (`FIN001`–`FIN003`) | `accounting-tt99-2025.md`, `banking-and-payments.md`, `securities-and-investing.md`, `number-to-words-vnd.md` |
| [`vietnamese-education-copy`](skills/vietnamese-education-copy/SKILL.md) | EdTech, LMS microcopy, K-12 MOET Circular 22/2021/TT-BGDĐT (`học bạ số`), university syllabi, KNLNN 6 bậc (VSTEP) | `rules_edu.py` (`EDU001`–`EDU003`) | `moet-curriculum-and-grading.md`, `certification-and-cefr.md`, `instructional-design.md`, `lms-and-student-ux.md` |

---

## Deterministic Validation & Tooling Suite

All scripts run on **Python 3.9+ standard library only** (zero third-party pip packages required).

### 1. `validate_copy.py` (v3.0 Linguistic & Statutory Linter)

```bash
# Run core + domain validation on a file or stdin
python3 shared/scripts/validate_copy.py path/to/copy.md --domain ux --register ux-microcopy

# Validate an administrative Công văn under Decree 30/2020/NĐ-CP
python3 shared/scripts/validate_copy.py path/to/cong-van.md --domain biz --doctype cong-van

# Auto-fix NFC normalization (NFC001), superscripts (NUM004), and normalize tone style (TONE001)
python3 shared/scripts/validate_copy.py path/to/copy.md --fix --fix-tone new --output path/to/copy.fixed.md

# Emit machine-readable JSON diagnostics for CI/CD pipelines
python3 shared/scripts/validate_copy.py path/to/copy.md --domain finance --json
```

#### Core Rule Matrix (`validate_copy.py`)

| Rule ID | Severity | Description | Auto-Fix |
|---|---|---|---|
| `NFC001` | `ERROR` | Decomposed Unicode NFD combining marks (`U+0300–U+036F`, `U+0340–U+0341`) | `--fix` |
| `ENC001` | `ERROR` | Legacy TCVN3 / VNI-Windows / CP1258 encoding or double-encoded UTF-8 mojibake (`Ã¡`, `á»‡`, `Æ°`) | — |
| `CAL001` | `WARNING` | Direct English-to-Vietnamese calques (`Làm ơn + verb`, `Của bạn + noun`, `nó là quan trọng`) | — |
| `SYN001` | `WARNING` | Adversity passive `bị` paired with a positive outcome (`bị hủy thành công`, `bị nâng cấp`) | — |
| `LAW001` | `ERROR` | Unverified superlatives (`nhất`, `duy nhất`, `tốt nhất`, `số 1`) under Advertising Law Art. 8(11) | — |
| `DIA001` | `ERROR` | Stripped Vietnamese diacritics across 120+ UI, SaaS, Tech, Finance, Edu, and Real-Estate phrases | — |
| `TONE001` | `INFO` | Intra-document mixed tone placement on open syllables `oa`, `oe`, `uy` (`hòa` vs `hoà`) | `--fix-tone new\|old` |
| `NUM001` | `WARNING` | English thousands comma or decimal dot in Vietnamese numeric prose | — |
| `NUM002` | `WARNING` | Unformatted 4+ digit VND amounts (`50000đ`, `1500000 VND`) | — |
| `NUM003` | `WARNING` | English currency shorthand (`1.5M VND`, `$50K`) instead of `tr`, `tỷ`, `nghìn` | — |
| `NUM004` | `WARNING` | ASCII unit `m2`/`m3`/`cm2`/`km2` instead of `m²`/`m³` (with `Apple M2`/`M3` hardware guard) | `--fix` |
| `DATE001` | `WARNING` | Ambiguous US `MM/DD/YYYY` date or `Tháng 1-12` capitalization drift | — |
| `PHONE001` | `INFO` | Unformatted 10-digit Vietnamese mobile number or `+840...` trunk-zero redundancy | — |
| `ICU001` | `ERROR` | Multi-line or single-line ICU MessageFormat `plural` using `zero`/`one`/`two`/`few`/`many` in `vi-VN` | — |
| `ICU002` | `WARNING` | Malformed ICU braces or ASCII camelCase/snake_case placeholder key in Vietnamese prose | — |
| `PRO001` | `WARNING` | Intra-document formal (`Quý khách`) vs casual (`bạn`) pronoun drift (exempts compound words) | — |
| `PRO002` | `WARNING` | Pronoun mismatch against `--register <register-id>` | — |

### 2. `check_font_coverage.py` (TrueType/OpenType Binary `cmap` & CSS `unicode-range` Auditor)

```bash
# Audit a binary .ttf/.otf font for all 134 precomposed Vietnamese vowels + Đ/đ + ₫ (U+20AB)
python3 shared/scripts/check_font_coverage.py path/to/BeVietnamPro-Regular.ttf --json

# Audit a CSS file's @font-face unicode-range declarations
python3 shared/scripts/check_font_coverage.py path/to/fonts.css
```

### 3. `check_i18n_parity.py` (EN/VI Localization Catalog Parity & Length Expansion Checker)

```bash
python3 shared/scripts/check_i18n_parity.py \
  --source skills/vn-design-system-ux/assets/en.sample.json \
  --target skills/vn-design-system-ux/assets/vi.sample.json \
  --json
```

---

## UKMC.v1 Cryptographically Verified Knowledge Base

The [`knowledge/`](knowledge/README.md) directory is structured and verified under the **Universal Knowledge Master Contract (UKMC.v1)** using `design-os-knowledge-builder`:

- **8 Verified Knowledge Modules** (`trust_tier: "verified"`), each containing SHA-256 provenance-pinned `source_attribution` and 38 inline `<!-- ease:source uri="..." sha256="..." quote="..." -->` anchors verified verbatim against primary source dossiers in `knowledge/_evidence/vn-design-os-261026/sources/`.
- **Certified `STOP_SUFFICIENT` Epistemic Gate:** 8/8 required claims verified, 4 independent source dossiers, execution proof recorded, counterevidence/failure modes cataloged, and independent cross-runtime review (`gemini-4-argon-high` reviewing `gemini-3.8-flash-worker`).

```bash
# Verify all 8 UKMC.v1 modules and 38 quote anchors
PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli verify knowledge --claims

# Evaluate the epistemic stopping gate
PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli gate --root knowledge --run-id vn-design-os-261026
```

---

## Repository Structure

```text
design-os-vietnamese/
├── knowledge/                       # UKMC.v1 cryptographically verified knowledge base (8 modules + index.json)
│   └── _evidence/vn-design-os-261026/
├── shared/                          # Canonical source of truth synced into every skill
│   ├── references/                  # 5 shared linguistic, legal, locale, unicode & typography manuals
│   └── scripts/                     # validate_copy.py, check_font_coverage.py, check_i18n_parity.py
├── skills/                          # 6 self-contained agent skills
│   ├── vn-design-system-ux/
│   ├── vietnamese-landing-copy/
│   ├── vietnamese-tech-writing/
│   ├── vietnamese-business-comms/
│   ├── vietnamese-finance-copy/
│   └── vietnamese-education-copy/
├── evals/                           # 180+ golden bad/good JSONL benchmark pairs + 120 trigger queries
├── tools/                           # sync_shared.py & build_examples.py
└── tests/                           # Comprehensive automated unittest suite
```

## Running Tests & Maintainer Sync

```bash
# Sync shared references & scripts into all 6 skills and regenerate examples.md from evals/
python3 tools/sync_shared.py
python3 tools/build_examples.py

# Run the full test suite
python3 -m unittest discover -s tests -v
```

## License

Released under the [MIT License](LICENSE). Copyright (c) 2026 Jang Trinh / DESIGN:OS.
