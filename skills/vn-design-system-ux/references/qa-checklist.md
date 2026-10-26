<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese UI/UX QA & Release Checklist (`qa-checklist.md`)

> Comprehensive quality assurance checklist for verifying Vietnamese localization, typography metrics, component layout budgets, and interaction states prior to deployment.
> Every pull request touching UI strings, CSS design tokens, or localization catalogs (`vi.json`) must satisfy these gates.

---

## 1. Encoding & Unicode Normalization Gate

- [ ] **NFC Precomposed Normalization (`NFC001`):** All `.json`, `.tsx`, `.ts`, `.html`, and `.md` files are strictly normalized to Unicode NFC (`U+00E1` for `á`, not `a + U+0301`). Verified via `validate_copy.py --fix`.
- [ ] **Zero Mojibake / Corrupted Byte Sequences (`ENC001`):** No UTF-8 decoding artifacts (such as `Ã¡`, `Ã*`, `Ä‘`, `ï»¿`, or `\uFFFD`) exist in source files or bundle outputs.
- [ ] **Tone Placement Consistency (`TONE001`):** A single tone-mark convention is used consistently across the product: either kiểu mới (`hoà`, `thuỷ`) or kiểu cũ (`hòa`, `thủy`).

---

## 2. Typography & Leading Metrics Gate

- [ ] **Display & Heading Line-Height Floor (`UX006`):** All headings (`h1`–`h6`, `.heading`, `.title`) have `line-height >= 1.18` (recommended `1.20`–`1.30`).
- [ ] **Body Prose Line-Height Floor (`UX006`):** All paragraph and body text tokens have `line-height >= 1.35` (recommended `1.50`–`1.60`).
- [ ] **Zero Diacritic Clipping:** Stacked diacritics on uppercase vowels (`Ẫ`, `Ễ`, `Ộ`, `Ữ`, `Ậ`, `Ệ`) remain fully visible in containers with `overflow: hidden`.
- [ ] **Next.js Font Subsets (`UX007`):** All `next/font/google` declarations explicitly include `subsets: ['latin', 'vietnamese']`.
- [ ] **Neutral Tracking:** No negative `letter-spacing` (`letter-spacing < 0em`) is applied to Vietnamese body text or headings with stacked diacritics.
- [ ] **Heading Wrap Balancing:** `text-wrap: balance` is enabled on all H1–H3 headings to eliminate single-syllable trailing orphans.

---

## 3. Component Character Caps & Layout Budget Gate

- [ ] **Primary & Secondary Buttons (`UX001`):** Button labels are `<= 24 characters` NFC (hard cap 28). Labels are verb-first and never wrap to two lines.
- [ ] **Navigation Tabs (`UX001`):** Tab titles are `<= 18 characters` NFC.
- [ ] **Status Badges / Pills (`UX001`):** Status labels are `<= 16 characters` NFC and fit inside fixed vertical chips without clipping ascenders/descenders.
- [ ] **Toast Notifications (`UX001`):** Toast messages are `<= 90 characters` NFC and contain an immediate action recovery or `Hoàn tác` button where applicable.
- [ ] **No Fixed Widths on Text Containers:** Buttons, navigation pills, and table headers do not use hardcoded fixed CSS widths (e.g. `w-20` / `width: 80px`).
- [ ] **Clean Compact Labels (`UX002`):** Compact controls contain no pronouns (`bạn`, `tôi`, `chúng tôi`) or polite padding (`vui lòng`, `xin vui lòng`).

---

## 4. Operational State Microcopy Gate

- [ ] **Actionable Empty States (`UX003`):** Empty screens explain *why* there is no data and provide an immediate creation CTA (`+ Tạo mới`, `Tải lên tệp`). No dead-end `Không có dữ liệu` or `Trạng thái trống`.
- [ ] **Actionable Error States (`UX004`):** Error banners explain the cause in plain language and provide a clear recovery button (`Thử lại`, `Kiểm tra kết nối`). No dead-end `Đã xảy ra lỗi`.
- [ ] **Safe Destructive Modals (`UX005`):** Destructive confirmation dialogs explicitly state permanent consequences (`Hành động này không thể hoàn tác` / `bị xóa vĩnh viễn`) and use specific verb buttons (`Xóa vĩnh viễn`) rather than vague `OK` / `Đồng ý`.
- [ ] **Skeleton & Loading Alignment:** Skeleton loaders match the expanded vertical leading of Vietnamese typography. Spinners use active present-continuous verbs (`Đang tải...`, `Đang đồng bộ...`).

---

## 5. i18n Parity & Localization Catalog Gate

- [ ] **100% Key Parity (`check_i18n_parity.py`):** Every key in `en.json` has a corresponding key in `vi.json` with zero missing keys (`I18N001`) and zero orphaned keys (`I18N002`).
- [ ] **Placeholder Parity (`I18N003`):** Variable placeholders (`{name}`, `{{count}}`, `%s`, `%d`, `<0>...</0>`) match byte-for-byte between source and target catalogs.
- [ ] **ICU Plural Rule Compliance (`ICU001`):** Vietnamese plural strings define **only** the `other` branch (and optional `=0`). No `one`, `two`, `few`, or `many` branches exist.
- [ ] **ASCII Variable Identifiers (`ICU002`):** All placeholder variable identifiers remain pure ASCII (e.g. `{itemCount}`, never `{số_lượng}`).

---

## 6. Terminology, Banned Phrases, & Legal Compliance Gate

- [ ] **Zero Calques / Literalisms (`CAL001`):** No mechanical translationese from `references/glossary.md` or `references/banned-phrases.md` (e.g. `tiết kiệm thay đổi`, `bảng táp-lô`, `cài lại mật khẩu`).
- [ ] **Zero Syntactic Translationese (`SYN001`):** Natural clause order is observed; passive clauses (`được thực hiện bởi`, `được tiến hành`) are rewritten into active verbs.
- [ ] **Unsubstantiated Superlatives (`LAW001`):** Prohibited absolute advertising claims (`số 1`, `tốt nhất`, `hàng đầu`, `an toàn tuyệt đối`) are removed or accompanied by legally documented verification.
- [ ] **Locale Formatting Standards:**
  - Numbers: Period as thousands separator (`1.250.000`), comma as decimal (`12,5%`).
  - Currency: `150.000 ₫` with non-breaking space before symbol.
  - Dates: `dd/MM/yyyy` format (`26/10/2026`).
  - Phone: `+84 901 234 567` (no trunk zero after `+84`).

---

## 7. Mobile & Responsive Layout QA Gate

- [ ] **Minimum Touch Targets:** All interactive Vietnamese button and icon controls satisfy minimum 44×44pt touch bounding boxes on iOS / Android.
- [ ] **Bottom Sheet Height Flexibility:** Bottom sheets and action modals accommodate the 30% Vietnamese text expansion without truncating primary buttons.
- [ ] **Dynamic Type Resilience:** On iOS Safari with Dynamic Type scale set to +150%, stacked diacritics maintain line separation and do not overlap parent rows.
- [ ] **Single-Syllable Orphan Check:** Multi-line mobile headers do not break compound words onto a single-syllable trailing line (`khách` / `hàng`).

---

## 8. Automated CI/CD Pipeline Verification

Run these three deterministic CLI commands before tagging any release:

```bash
# 1. Validate all copy, typography, and microcopy rules
python3 skills/vn-design-system-ux/scripts/validate_copy.py app/src/locales/vi.json --strict

# 2. Check full i18n parity against source English catalog
python3 skills/vn-design-system-ux/scripts/check_i18n_parity.py app/src/locales/en.json app/src/locales/vi.json --strict

# 3. Verify font coverage for all 134 Vietnamese diacritics
python3 skills/vn-design-system-ux/scripts/check_font_coverage.py public/fonts/BeVietnamPro-Regular.ttf
```
