<!-- synced from shared/references/locale-formatting.md (7661037f903ccd87) — edit shared/ source, not this copy -->
<!-- vlc-disable: NUM001, NUM002, NUM003, NUM004, DIA001, TONE001 -->

# Locale Formatting — `vi-VN` Standards (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. Locale formatting rules in Vietnam are objective, machine-checkable, and the exact inverse of US English conventions for numbers and dates.

---

## 1. Numbers, Decimals, and Currency (`VND` / `₫`)

**Thousands separator is a period (`.`). Decimal separator is a comma (`,`).**

| Category | ❌ Wrong (EN/US Default) | ✅ Correct (`vi-VN` Standard) | Rule ID |
|---|---|---|---|
| **Grouped Integer** | `1,250,000` | `1.250.000` | `NUM001` |
| **Ungrouped Currency** | `2500000 VND`, `50000đ` | `2.500.000 ₫` or `50.000 ₫` | `NUM002` |
| **Decimal Number** | `2.5 tỷ`, `3.6/4.0`, `12.5%` | `2,5 tỷ`, `3,6/4,0`, `12,5%` | `NUM003` |
| **Minor Units (Cents)** | `2.500.000,00 ₫` | `2.500.000 ₫` (ISO 4217: VND has 0 minor units) | — |

### Currency Symbol Placement & Register Selection:
- **UI Cards, E-Commerce, Pricing Tables:** Place `₫` (`U+20AB`) **after** the number separated by a space (prefer non-breaking space `\u00A0`): `2.500.000 ₫`.
- **Narrative Prose & Headlines:** Use colloquial scale words `tỷ` ($10^9$), `triệu` ($10^6$), `nghìn` / `ngàn` ($10^3$) with `đồng`: `Chỉ từ 2,5 tỷ đồng`, `35 triệu đồng/m²`, `499 nghìn đồng/tháng`.
- **Financial Statements, Accounting, E-Invoices:** Use full period-grouped digits (`2.500.000.000`) or declare a table-level unit header (`Đơn vị tính: triệu đồng` / `tỷ đồng` / `VND`). Never mix `2,5 tỷ` and `2.500.000.000` in the same table column.
- **Standard JS/TS Formatter:**
  ```ts
  const vnd = new Intl.NumberFormat('vi-VN', {
    style: 'currency',
    currency: 'VND',
    maximumFractionDigits: 0,
  });
  vnd.format(2500000); // "2.500.000 ₫"
  ```

---

## 2. Units of Measure & Hardware Disambiguation (`NUM004`)

- **Area & Volume Superscripts:** Always use Unicode superscripts `m²` (`U+00B2`), `m³` (`U+00B3`), `cm²`, `km²`, never ASCII `m2`, `m3`, `cm2`, `km2`.
- **Hardware Chip Disambiguation (Critical Guard):**
  In technical and e-commerce copy, `M2` and `M3` frequently refer to **Apple Silicon (`chip M2`, `MacBook Air M2`, `M2 Pro`, `M2 Max`, `M3 Ultra`)**, **NVMe SSD form factors (`SSD M.2`, `khe M2`)**, or **BMW M2/M3**. `validate_copy.py` includes a contextual guard so hardware identifiers are never falsely flagged as square/cubic meters.

---

## 3. Dates, Times, Phone Numbers, and Addresses

| Data Type | Canonical Format | Valid Examples | Defects Flagged |
|---|---|---|---|
| **Numeric Date** | `dd/MM/yyyy` | `26/10/2026`, `05/01/2026` | `DATE001` flags `MM/dd/yyyy` (e.g. `10/26/2026`) |
| **Administrative/Legal Date** | `[Địa danh], ngày DD tháng MM năm YYYY` | `Hà Nội, ngày 05 tháng 01 năm 2026` (zero-pad days `<10` and months `01, 02` per NĐ 30/2020) | — |
| **Time of Day** | 24-hour `HH:mm` | `08:30`, `14:00`, `21:45` (include `(GMT+7)` in cross-border/B2B invites) | Avoid `2:00 PM` in formal/UI copy |
| **Domestic Mobile** | `0xxx xxx xxx` (10 digits; prefixes `03`, `05`, `07`, `08`, `09`) | `0912 345 678`, `0987 654 321` | — |
| **International Phone** | `+84 xxx xxx xxx` (drop trunk `0`!) | `+84 912 345 678`, `+84 28 3822 xxxx` | `PHONE001` flags `+84 0912...` or `+84(0)9...` |
| **Service Hotline** | `1900 xxxx` / `1800 xxxx` (4 or 6 digits after prefix) | `1800 1090` (toll-free), `1900 5454 15` | — |
| **Vietnamese Address** | Smallest unit → Largest unit | `Số 12 Nguyễn Huệ, Phường Bến Nghé, Quận 1, TP. Hồ Chí Minh` (or post-consolidation `Số 12 Nguyễn Huệ, Phường Sài Gòn, TP. Hồ Chí Minh`) | Never use English big-to-small order |

---

## 4. Number-to-Words Orthography (Số tiền bằng chữ)

On contracts, quotations (`báo giá`), and e-invoices (`hóa đơn GTGT`), total amounts written in words must obey standard Vietnamese phonological rules:
- **`lăm` vs `năm`:** Use `lăm` after `mươi` (`mười`..`chín mươi`): `mười lăm` (15), `hai mươi lăm` (25). Use `năm` at the start of a group or after `trăm`/`không`: `năm triệu`, `một trăm linh năm` (105).
- **`mốt` vs `một`:** Use `mốt` after `hai mươi`..`chín mươi`: `hai mươi mốt` (21). Use `một` after `mười` or `trăm`: `mười một` (11), `một trăm linh một` (101).
- **`tư` vs `bốn`:** After `hai mươi`..`chín mươi`, both `tư` and `bốn` are accepted (`hai mươi tư` / `hai mươi bốn`), with `tư` preferred in formal accounting.
- **`linh` vs `lẻ`:** When the tens digit is zero and the units digit is non-zero (`105`), both `một trăm linh năm` (Northern/Statutory standard) and `một trăm lẻ năm` (Southern commercial) are valid; financial templates default to `linh` or `lẻ` consistently and always end with `đồng chẵn.` when there are no fractional units.

---

## 5. Multi-Line ICU MessageFormat & Localization Keys (`ICU001`, `ICU002`)

1. **CLDR Plural Rule (`ICU001`):**
   Vietnamese has **no grammatical plural inflection**. In Unicode CLDR, `vi` has only one plural category: `other`.
   - **Valid:** `{count, plural, =0 {Chưa có mục nào} other {# mục}}`
   - **Invalid (`ICU001` ERROR):** Any `one {...}`, `zero {...}`, `two {...}`, `few {...}`, or `many {...}` keyword branch—whether on a single line or spanning multiple lines.
2. **Placeholder Variable Integrity (`ICU002`):**
   - Never translate variable names inside `{...}`, `{{...}}`, or `$t(...)`: keep `{userName}`, `{{orderId}}`, `{count}` byte-identical to `en.json`. Translating `{name}` to `{tên}` breaks runtime interpolation.
3. **BCP-47 Language Tags:**
   - HTML root: `<html lang="vi">`
   - Regional formatting / OpenGraph: `vi-VN` (BCP-47) or `vi_VN` (OpenGraph `og:locale` only). Never use `vn` or `vi-VI`.
