<!-- vlc-disable: TONE001, DIA001 -->

# DESIGN:OS Vietnamese Typography, Vertical Metrics, & UI Layout (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. Vietnamese is the most vertically and horizontally demanding Latin-script language in modern UI engineering: it stacks up to **two diacritical marks above a vowel** (`Ẫ`, `Ễ`, `Ộ`, `Ữ`) or **one mark above and one dot below** (`Ậ`, `Ệ`, `Ộ`, `Ự`), while expanding horizontal button and navigation copy by **20%–35%** compared to English.

---

## 1. Vertical Metrics & Stacked-Diacritic Clipping (`UX005`)

Standard Latin type scales designed around English ascenders (`h`, `k`, `l`) and descenders (`g`, `p`, `y`) routinely clip Vietnamese stacked diacritics when tight leading (`line-height: 1.0` or `1.1`) or `overflow: hidden` with a fixed container height is applied.

### Mandatory Line-Height Floors for Vietnamese UI:
| Typography Token Tier | English Typical `line-height` | **Vietnamese Mandatory Floor (`vi-VN`)** | Why It Clips Below the Floor |
|---|---|---|---|
| **Display / Hero (`≥ 36px`)** | `1.0` – `1.08` | **`≥ 1.18`** (`1.20` recommended) | Uppercase `Ẫ`, `Ễ`, `Ộ`, `Ữ` collide with the descender or dot-below (`ậ`, `ệ`, `ự`, `g`, `y`) of the line above |
| **Section Heading (`20px–32px`)** | `1.15` – `1.20` | **`≥ 1.25`** (`1.30` recommended) | Two-line card titles clip the acute/hook on `ể`, `ử`, `ỗ` |
| **Body Prose (`14px–18px`)** | `1.35` – `1.45` | **`≥ 1.50`** (`1.55`–`1.65` recommended) | Dense diacritic clusters reduce inter-line whitespace, causing visual fatigue ("diacritic crowding") |
| **Compact Controls / Badges (`11px–13px`)** | `1.0` | **`≥ 1.25`** + vertical padding `≥ 4px` | Fixed `height: 20px` + `overflow: hidden` slices off the top of `Ấ`, `Ế` and bottom of `ự`, `ỵ` |

- **Never pair `overflow: hidden` with `line-height < 1.25` on single-line headings** unless vertical padding compensates.
- **Avoid `text-transform: uppercase` on long Vietnamese phrases:** Uppercase stacked diacritics (`ĐĂNG KÝ NHẬN BẢNG GIÁ CĂN HỘ MẪU`) create extreme top-edge visual noise and fail on display fonts whose uppercase diacritics are poorly kerned. Prefer **Sentence case** (`Đăng ký nhận bảng giá`) or **Title Case for proper nouns only**.

---

## 2. Font Selection & Glyph Coverage Verification (`check_font_coverage.py`)

A font is **not** production-ready for Vietnamese unless its `cmap` table and `vietnamese` WOFF2 subset include all **134 precomposed Vietnamese vowels**, `Đ/đ` (`U+0110/U+0111`), and `₫` (`U+20AB`).

### Tier-1 Production Typefaces for Vietnamese UI:
1. **`Be Vietnam Pro`** (Designed specifically by Vietnamese typographers for UI/Display — compact horizontal width, balanced stacked marks, native `₫`).
2. **`Plus Jakarta Sans` / `Inter` / `Geist`** (Clean Operate-mode SaaS UI; verify `vietnamese` subset is loaded).
3. **`Noto Sans` / `IBM Plex Sans` / `Roboto` / `Public Sans`** (High-density tables, enterprise dashboards, finance).
4. **Editorial Serif:** `Newsreader`, `Lora`, `Merriweather`, `Literata`, `Playfair Display` (always test uppercase `Ẫ`, `Ễ`, `Ộ`, `Ữ`, `Ỷ`, `Ỹ` at `700` weight).

### The `Ỳ ỳ Ỵ ỵ Ỷ ỷ Ỹ ỹ` Subset Trap:
Legacy Google Fonts subsets historically omitted `Ỳ/ỳ` (`U+1EF2/U+1EF3`), `Ỵ/ỵ` (`U+1EF4/U+1EF5`), `Ỷ/ỷ` (`U+1EF6/U+1EF7`), and `Ỹ/ỹ` (`U+1EF8/U+1EF9`), causing browsers to substitute a system fallback font mid-word in words like `kỳ vọng`, `Mỹ`, `tỷ đồng`, `kỹ thuật`, `lý thuyết`.
- Always include `'vietnamese'` in `next/font/google`:
  ```tsx
  import { Be_Vietnam_Pro } from 'next/font/google';
  export const fontSans = Be_Vietnam_Pro({
    subsets: ['latin', 'vietnamese'],
    weight: ['400', '500', '600', '700'],
    display: 'swap',
  });
  ```
- Run `python3 scripts/check_font_coverage.py` against CSS `unicode-range` declarations, `next/font` source files, or binary `.ttf`/`.otf` font files.

---

## 3. UI String Expansion Budgets & Component Character Caps

Vietnamese is an analytic, isolating language where each syllable is space-separated. Translating English UI strings into Vietnamese typically expands character length by **+20% to +35%**:
- `Save` (4 chars) → `Lưu` (3 chars, `-25%`) or `Lưu thay đổi` (12 chars)
- `Edit` (4 chars) → `Chỉnh sửa` (9 chars, `+125%`)
- `Settings` (8 chars) → `Cài đặt` (7 chars) or `Thiết lập` (9 chars)
- `Cancel` (6 chars) → `Hủy` (3 chars)
- `Sign up` (7 chars) → `Đăng ký` (7 chars)
- `Dashboard` (9 chars) → `Tổng quan` (9 chars) or `Bảng điều khiển` (15 chars, `+67%`)

### DESIGN:OS Component Character Caps (`check_i18n_parity.py` & `UX001`):
| UI Emitter Role | Max Recommended Length (`vi-VN` NFC chars) | Max Syllables | Layout Rule |
|---|---|---|---|
| **Primary / Secondary Button (`cta`, `button`)** | **24 chars** (hard cap **28**) | 2–5 syllables | Verb-first (`Tạo dự án`, `Lưu thay đổi`, `Xuất báo cáo`). Never wrap to 2 lines |
| **Navigation Tab / Segmented Control (`tab`)** | **18 chars** | 2–3 syllables | Noun or short verb phrase (`Tổng quan`, `Thanh toán`, `Thành viên`) |
| **Status Badge / Pill (`badge`, `status`)** | **16 chars** | 2–3 syllables | State participle (`Đang xử lý`, `Đã hoàn tất`, `Quá hạn`, `Bản nháp`) |
| **Toast / Snackbar (`toast`)** | **90 chars** | ≤ 16 syllables | `[Trạng thái đã xảy ra]. [Hành động khôi phục ngắn]` (`Đã xóa tệp. Hoàn tác`) |
| **Table Column Header (`th`)** | **22 chars** | 2–4 syllables | Use standard abbreviations (`SL`, `Đơn giá`, `Thành tiền`, `Trạng thái`) |
| **App Store Title / Subtitle** | **30 chars** (Apple/Play hard cap) | ≤ 6 syllables | Enforced by `PROD003` |
| **Google Play Short Description** | **80 chars** (Play hard cap) | ≤ 15 syllables | Enforced by `PROD003` |

---

## 4. Widow / Orphan Compound-Word Binding (`TYP002`)

In Vietnamese, a two-syllable word (`từ ghép`) is written with a normal ASCII space (`U+0020`) between its two syllables (e.g., `khách hàng`, `đăng ký`, `hành trình`, `thương hiệu`, `tài chính`, `tương lai`, `công nghệ`).
When a headline or hero subheadline wraps just before the last syllable, it leaves a **1-syllable orphan on the final line**:

```text
❌ Broken Visual Rhythm (1-syllable orphan splits the compound word "khách hàng"):
Nền tảng quản trị trải nghiệm khách
hàng toàn diện cho doanh nghiệp
```

### The Non-Breaking Space (`\u00A0` / `&nbsp;`) Binding Rule:
- Bind the final 2-syllable compound word of any Hero headline, section H2, or card title with a non-breaking space (`\u00A0` in JSON/TSX or `text-wrap: balance` in CSS):
  ```text
  ✅ Bound Compound Word ("doanh\u00A0nghiệp"):
  Nền tảng quản trị trải nghiệm khách hàng
  toàn diện cho doanh nghiệp
  ```
- Always apply `text-wrap: balance` on headings (`h1`–`h3`) and `text-wrap: pretty` on body paragraphs (`p`).
