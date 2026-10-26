---
id: "locale-and-icu-engineering"
title: "CLDR vi-VN Number, Currency, Unit Disambiguation, and ICU MessageFormat Engineering"
domain: "vietnamese-i18n-and-localization"
description: "Verified specification for Vietnamese CLDR number/currency formatting, Apple Silicon M2/M3 vs m²/m³ contextual disambiguation, and multi-line ICU MessageFormat validation."
when:
  - "Formatting VND currency, percentages, dates, phone numbers, and physical units in Vietnamese"
  - "Validating .json, .arb, or .strings localization catalogs with ICU MessageFormat plurals"
  - "Preventing false-positive NUM004 unit errors on hardware processor names (Apple M2/M3)"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md"
    sha256: "863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d"
  - uri: "_evidence/vn-design-os-261026/sources/04-engine-execution-verification-log.txt"
    sha256: "4149a4846143aa45aec3a7089226ddf8f8e791c97c437acb311b2d9910bdf4ef"
---

# CLDR vi-VN Number, Currency, Unit Disambiguation, and ICU MessageFormat Engineering

## Purpose

Defines the deterministic formatting rules for numbers, VND currency, dates, phone numbers, superscript units (`m²`, `m³`), and ICU MessageFormat plural/placeholder validation in `vi-VN`.

## When to Use / When NOT

- **When to Use:**
  - Formatting prices, invoices, interest rates, timestamps, and physical dimensions for Vietnamese users.
  - Auditing `en.json` and `vi.json` localization files with `validate_copy.py` and `check_i18n_parity.py`.
- **When NOT to Use:**
  - Machine-to-machine JSON numeric fields, SQL numeric literals, or CSS pixel/rem declarations where locale separators are syntactically invalid.

## Core Knowledge Content

### 1. CLDR `vi-VN` Number and Currency Separators (`NUM001`, `NUM002`, `NUM003`)

Under CLDR `vi-VN` and Vietnamese accounting conventions, thousands are separated by dots (`.`) and decimal fractions by commas (`,`); VND amounts use no decimal places (`1.250.000 ₫` or `1.250.000 VND`), while compact shorthand uses `tr` (triệu), `tỷ`, or `nghìn`/`ngàn` rather than English `1.5M VND` (`NUM003`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Under CLDR vi-VN and Vietnamese accounting conventions, thousands are separated by dots ('.') and decimal fractions by commas (','); VND amounts use no decimal places ('1.250.000 ₫' or '1.250.000 VND'), while compact shorthand uses 'tr' (triệu), 'tỷ', or 'nghìn'/'ngàn' rather than English '1.5M VND' (NUM003)." -->

### 2. Superscript Unit Symbols vs Hardware Processor Tokens (`NUM004`)

Unit symbols `m²` and `m³` must use Unicode superscripts (`U+00B2`, `U+00B3`) rather than ASCII `m2`/`m3` (`NUM004`), but validator rules must exempt hardware processor tokens such as `Apple M2`, `MacBook Air M2`, `chip M2 Pro`, `M2 Max`, `M2 Ultra`, and `iPad M2`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Unit symbols m² and m³ must use Unicode superscripts (U+00B2, U+00B3) rather than ASCII 'm2'/'m3' (NUM004), but validator rules must exempt hardware processor tokens such as 'Apple M2', 'MacBook Air M2', 'chip M2 Pro', 'M2 Max', 'M2 Ultra', and 'iPad M2'." -->

Naive regex `(?<![\w])m2(?![\w])` with `re.IGNORECASE` falsely flags hardware processor names such as `Apple M2`, `MacBook Air M2`, and `chip M2 Max` as unformatted square meters (`m²`). Mitigated in `validate_copy.py` v3.0 via `HARDWARE_M2_CONTEXT_RE` contextual guard.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/04-engine-execution-verification-log.txt" sha256="4149a4846143aa45aec3a7089226ddf8f8e791c97c437acb311b2d9910bdf4ef" quote="FAILURE_MODE [NUM004-APPLE-M2]: Naive regex `(?<![\\w])m2(?![\\w])` with `re.IGNORECASE` falsely flags hardware processor names such as 'Apple M2', 'MacBook Air M2', and 'chip M2 Max' as unformatted square meters (`m²`). Mitigated in validate_copy.py v3.0 via `HARDWARE_M2_CONTEXT_RE` contextual guard." -->

### 3. Multi-Line ICU MessageFormat Plural Validation (`ICU001`, `ICU002`)

Vietnamese has a single CLDR plural category (`other`); ICU MessageFormat strings in `vi-VN` must define only the `=0` (optional exact zero) and `other` branches, and multi-line ICU blocks containing English `one`, `two`, `few`, or `many` selectors must be flagged by a balanced-brace parser (`ICU001`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Vietnamese has a single CLDR plural category ('other'); ICU MessageFormat strings in vi-VN must define only the '=0' (optional exact zero) and 'other' branches, and multi-line ICU blocks containing English 'one', 'two', 'few', or 'many' selectors must be flagged by a balanced-brace parser (ICU001)." -->

Line-by-line regex checking `plural` and `one {` on the same line fails on 100% of formatted multi-line ICU MessageFormat blocks in `.arb` and `.json` files. Mitigated in `validate_copy.py` v3.0 via `_check_multiline_icu` balanced-brace AST scanner.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/04-engine-execution-verification-log.txt" sha256="4149a4846143aa45aec3a7089226ddf8f8e791c97c437acb311b2d9910bdf4ef" quote="FAILURE_MODE [ICU001-MULTILINE]: Line-by-line regex checking `plural` and `one {` on the same line fails on 100% of formatted multi-line ICU MessageFormat blocks in `.arb` and `.json` files. Mitigated in validate_copy.py v3.0 via `_check_multiline_icu` balanced-brace AST scanner." -->

## Failure Modes (Mandatory)

1. **Apple Silicon `M2`/`M3` False Positives (`NUM004`):** Running a case-insensitive `m2` regex on tech product descriptions corrupts `MacBook Air M2` into `MacBook Air m²` if `--fix` is applied without `HARDWARE_M2_CONTEXT_RE`.
2. **Multi-Line ICU Blindness (`ICU001`):** Pretty-printed `.arb` and `.json` localization catalogs place `{count, plural,` on line 1 and `one {1 tệp}` on line 2, bypassing single-line regex validators.
3. **Translated Placeholder Keys (`ICU002`):** Translating `{userName}` into `{tenNguoiDung}` inside `vi.json` throws runtime formatting exceptions in `react-intl`, `next-intl`, and `i18next`.
