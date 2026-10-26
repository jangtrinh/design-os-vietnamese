---
name: vn-design-system-ux
description: "Vietnamese UI/UX microcopy, design systems, typography tokens, stacked-diacritic line-height gates, button/tab/badge/toast character caps, state copy (empty, loading, optimistic, partial failure, destructive modals, biometric/passkey prompts, AI streaming UX), widow/orphan compound-word binding (\\u00A0), and en.json <-> vi.json i18n parity."
repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# `vn-design-system-ux`: Flagship Vietnamese UI/UX & Design System Engine

> The flagship DESIGN:OS design system and microcopy skill for engineering production-grade software interfaces in Vietnamese (`vi-VN`).
> Governs typography vertical metrics, diacritic clipping floors, component character budgets, state-first UX writing, and bidirectional localization parity.

---

## 1. Core Engineering Workflow

Building or localizing a modern digital product in Vietnamese requires strict adherence to vertical diacritical physics, horizontal syllabic expansion (+25% to +35%), and conversational clarity:

```
[1. Font & Glyph Audit]
       │  check_font_coverage.py
       ▼
[2. Typography Tokens & Leading Floors]
       │  references/design-tokens-vi.md, references/typography-and-layout.md
       ▼
[3. State-First UX Microcopy & Character Caps]
       │  references/microcopy-states.md, references/glossary.md, references/banned-phrases.md
       ▼
[4. Register Contract & Locale Formatting]
       │  references/register-matrix.md, references/unicode-and-tone.md, references/locale-formatting.md
       ▼
[5. i18n Catalog & Placeholder Parity]
       │  check_i18n_parity.py, assets/en.sample.json, assets/vi.sample.json
       ▼
[6. Automated Copy & Domain Rule Linting]
       │  validate_copy.py, references/examples.md
       ▼
[7. Pre-Deploy Release Verification]
          references/qa-checklist.md
```

---

## 2. Step-by-Step Implementation Guide

### Step 1: Font Selection & Glyph Coverage Verification
Before applying any typography styles, ensure your web font contains all 134 precomposed Vietnamese diacritics, `Đ/đ` (`U+0110/U+0111`), and the currency symbol `₫` (`U+20AB`):
- Consult [typography-and-layout.md](references/typography-and-layout.md) for approved production typefaces (`Be Vietnam Pro`, `Plus Jakarta Sans`, `Inter`).
- When configuring `next/font/google`, enforce `subsets: ['latin', 'vietnamese']` to prevent fallback font flashing on stacked diacritics (`UX007`).
- Run font coverage verification:
  ```bash
  python3 skills/vn-design-system-ux/scripts/check_font_coverage.py public/fonts/BeVietnamPro-Regular.ttf
  ```

### Step 2: Establish Design Tokens & Vertical Leading Floors
Vietnamese stacked diacritics (`Ẫ`, `Ễ`, `Ộ`, `Ữ`, `Ậ`, `Ệ`) collide or clip under standard English tight leading:
- Load the standardized W3C Design Tokens from [assets/design-tokens.vi.json](assets/design-tokens.vi.json).
- Review leading specifications in [design-tokens-vi.md](references/design-tokens-vi.md) and [typography-and-layout.md](references/typography-and-layout.md).
- Enforce mandatory line-height floors (`UX006`):
  - **Headings (`h1`–`h6`, `.title`):** `line-height >= 1.18` (recommended `1.20`–`1.30`).
  - **Body Prose (`p`, `.prose`):** `line-height >= 1.35` (recommended `1.50`–`1.60`).
- Apply CSS `text-wrap: balance` on headings to eliminate single-syllable trailing orphans, or bind final compounds with `\u00A0`.

### Step 3: Craft State-First Microcopy Within Component Caps
Write clear, verb-first microcopy for all UI controls following [microcopy-states.md](references/microcopy-states.md):
- **Component Character Caps (`UX001`):**
  - Buttons (`ui-button`): `<= 24 characters` NFC (`Tạo dự án mới`, `Lưu thay đổi`).
  - Navigation Tabs (`ui-tab`): `<= 18 characters` NFC (`Tổng quan`, `Thanh toán`).
  - Status Badges (`ui-badge`): `<= 16 characters` NFC (`Đang hoạt động`, `Quá hạn`).
  - Toast Notifications (`ui-toast`): `<= 90 characters` NFC (`Đã xóa 3 tệp. Hoàn tác`).
- **Eliminate Padding & Pronouns in Compact Controls (`UX002`):** Strip conversational pronouns (`bạn`, `tôi`) and polite padding (`vui lòng`) from buttons and tabs.
- **Empty States (`UX003`):** Replace raw dead-end placeholders (`Không có dữ liệu`) with contextual explanations and creation CTAs.
- **Error States (`UX004`):** Replace generic errors (`Đã xảy ra lỗi`) with plain-language causes and actionable recovery buttons (`Thử lại`).
- **Destructive Modals (`UX005`):** Explicitly warn that actions cannot be undone (`Hành động này không thể hoàn tác`) and replace vague `OK`/`Đồng ý` with specific verbs (`Xóa vĩnh viễn`).

### Step 4: Validate Terminology, Registers, & Compliance
Check all interface strings against standardized dictionaries and legal constraints:
- Filter calques and machine translation artifacts using [glossary.md](references/glossary.md) and [banned-phrases.md](references/banned-phrases.md).
- Enforce the `ux-microcopy` register contract defined in [register-matrix.md](references/register-matrix.md) (`bạn` or implicit subject; forbid `quý khách` in SaaS).
- Validate tone placement consistency and NFC normalization via [unicode-and-tone.md](references/unicode-and-tone.md).
- Format numbers, currencies, dates, and phone numbers in accordance with [locale-formatting.md](references/locale-formatting.md).
- Guard against unsubstantiated superlatives (`số 1`, `hàng đầu`) as required by [compliance.md](references/compliance.md).

### Step 5: Audit i18n Localization Parity
Maintain bidirectional parity between English source catalogs and Vietnamese target catalogs:
- Reference canonical localization models in [assets/en.sample.json](assets/en.sample.json) and [assets/vi.sample.json](assets/vi.sample.json).
- Run the strict i18n parity linter:
  ```bash
  python3 skills/vn-design-system-ux/scripts/check_i18n_parity.py en.json vi.json --strict
  ```
- Verify:
  1. Key parity (zero missing keys, zero orphaned keys).
  2. Exact placeholder alignment (`{name}`, `{{count}}`).
  3. Precomposed NFC encoding across all Vietnamese values.
  4. ICU plural compliance: only the `other` branch is permitted in Vietnamese (no `one`, `few`, `many`).

### Step 6: Automated Copy & Domain Rule Linting
Run the complete automated validator across UI source files and locale bundles:
- Study worked diagnostic pairs in [examples.md](references/examples.md) to understand defect remediation patterns.
- Execute linter across project catalogs:
  ```bash
  python3 skills/vn-design-system-ux/scripts/validate_copy.py src/locales/vi.json --strict
  ```
- Validate specialized component states using doctypes:
  ```bash
  # Check button copy against 24-character cap and pronoun padding
  python3 skills/vn-design-system-ux/scripts/validate_copy.py button.txt --doctype ui-button --strict

  # Check tab label against 18-character cap
  python3 skills/vn-design-system-ux/scripts/validate_copy.py tabs.txt --doctype ui-tab --strict

  # Check empty state card for creation CTA
  python3 skills/vn-design-system-ux/scripts/validate_copy.py empty-card.md --doctype ui-empty --strict

  # Check error state for actionable recovery
  python3 skills/vn-design-system-ux/scripts/validate_copy.py error-banner.txt --doctype ui-error --strict

  # Check destructive modal for permanent consequence
  python3 skills/vn-design-system-ux/scripts/validate_copy.py modal.txt --doctype ui-destructive-modal --strict

  # Check CSS tokens for stacked diacritic leading floors
  python3 skills/vn-design-system-ux/scripts/validate_copy.py styles/tokens.css --doctype css-tokens --strict

  # Check Next.js font declaration for vietnamese subset
  python3 skills/vn-design-system-ux/scripts/validate_copy.py src/app/layout.tsx --doctype nextjs-font --strict
  ```

### Step 7: Release Readiness Sign-Off
Complete the comprehensive release gate defined in [qa-checklist.md](references/qa-checklist.md):
- [ ] NFC Unicode precomposed normalization confirmed (`--fix`).
- [ ] Display and body leading tokens meet or exceed Vietnamese mandatory floors (`UX006`).
- [ ] Next.js Google font loaders include `'vietnamese'` subset (`UX007`).
- [ ] Buttons, tabs, badges, and toasts adhere to NFC character caps (`UX001`).
- [ ] Empty, error, and destructive dialog states provide clear user agency (`UX003`, `UX004`, `UX005`).
- [ ] i18n catalog parity passes with 0 errors and 0 warnings.

---

## 3. Defect Remediation Quick Reference

| Symptom / Defect | Rule ID | Root Cause | Production Remediation |
|---|---|---|---|
| Diacritics on `Ẫ`, `Ệ` sliced off | `UX006` | Leading `< 1.18` on headings | Bump heading `line-height` to `>= 1.20` |
| Font switches to fallback mid-word | `UX007` | Missing `vietnamese` subset | Add `'vietnamese'` to Google Font loader |
| Button wraps to 2 lines | `UX001` | Label exceeds 24 characters | Shorten to verb-first action (`Tạo dự án`) |
| Conversational button padding | `UX002` | Label contains `bạn` or `vui lòng` | Remove conversational filler |
| Dead-end "Không có dữ liệu" | `UX003` | Empty state lacks action | Add contextual reason and `+ Tạo mới` CTA |
| Dead-end "Đã xảy ra lỗi" | `UX004` | Error state lacks recovery | State plain cause + provide `Thử lại` button |
| Dangerous vague modal button | `UX005` | Destructive modal uses `Đồng ý` | Use `Xóa vĩnh viễn` + warn cannot undo |

---

## 4. Tool & CLI Reference

| Tool | Script Path | Primary Responsibility |
|---|---|---|
| **Copy & UX Linter** | `scripts/validate_copy.py` | Validates NFC, calques, registers, and domain rules (`UX001`–`UX007`) |
| **i18n Parity Gate** | `scripts/check_i18n_parity.py` | Verifies key, placeholder, ICU plural, and cap parity (`en.json` <-> `vi.json`) |
| **Font Coverage Checker** | `scripts/check_font_coverage.py` | Scans TTF/OTF cmap tables and WOFF2 unicode-ranges for 134 vi-VN glyphs |

---

## 5. Reference Library Map

- **Typography & Metrics:** [typography-and-layout.md](references/typography-and-layout.md) · [design-tokens-vi.md](references/design-tokens-vi.md)
- **Microcopy & States:** [microcopy-states.md](references/microcopy-states.md) · [glossary.md](references/glossary.md) · [banned-phrases.md](references/banned-phrases.md)
- **Linguistic Rules:** [register-matrix.md](references/register-matrix.md) · [unicode-and-tone.md](references/unicode-and-tone.md) · [locale-formatting.md](references/locale-formatting.md) · [compliance.md](references/compliance.md)
- **Diagnostics & QA:** [examples.md](references/examples.md) · [qa-checklist.md](references/qa-checklist.md)
- **Token & Asset Catalogs:** [design-tokens.vi.json](assets/design-tokens.vi.json) · [en.sample.json](assets/en.sample.json) · [vi.sample.json](assets/vi.sample.json)
