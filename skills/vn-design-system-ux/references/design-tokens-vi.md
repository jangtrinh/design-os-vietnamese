<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese Typography Tokens & Layout Specifications (`design-tokens-vi.md`)

> Complete design token system for Vietnamese (`vi-VN`) typography, vertical leading metrics, component width headrooms, and glyph rendering.
> Integrates with Tailwind CSS v4, W3C Design Tokens Community Group (DTCG) JSON schemas, and Figma Variables.

---

## 1. Vietnamese Font Stacks & Glyph Verification (`UX007`)

Vietnamese contains 134 precomposed vowel diacritics, `Đ/đ` (`U+0110/U+0111`), and the currency symbol `₫` (`U+20AB`).
Standard Latin font distributions frequently omit the Vietnamese subset or mangle the positioning of stacked accents (`Ẫ`, `Ễ`, `Ộ`, `Ữ`).

### Certified Production Font Stacks:

```css
/* UI / Dashboard / Operate Mode (Default Sans) */
--font-sans-vi: "Be Vietnam Pro", "Plus Jakarta Sans", "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;

/* High-Density Tables / Financial Grids / Dense Enterprise */
--font-mono-vi: "JetBrains Mono", "SF Mono", "Roboto Mono", "Fira Code", monospace;

/* Editorial / Long-Form Articles / Marketing Serifs */
--font-serif-vi: "Newsreader", "Lora", "Merriweather", "Playfair Display", Georgia, serif;
```

### Next.js Font Loading Requirement (`UX007`):
When importing fonts via `next/font/google`, **always** include `'vietnamese'` in the `subsets` array alongside `'latin'`:
```tsx
import { Be_Vietnam_Pro } from 'next/font/google';

export const fontSans = Be_Vietnam_Pro({
  subsets: ['latin', 'vietnamese'], // Mandatory for vi-VN
  weight: ['400', '500', '600', '700'],
  variable: '--font-sans',
  display: 'swap',
});
```

---

## 2. Mandatory Line-Height Leading Matrix (`UX006`)

Vietnamese vowels stack up to two diacritics above (`ẫ`, `ễ`, `ỗ`, `ữ`) or one diacritic above and a dot below (`ậ`, `ệ`, `ộ`, `ự`).
Tightly leading English font scales (`line-height: 1.0` or `1.1`) clip these glyphs, particularly in containers with `overflow: hidden`.

| Token Name | Font Size | English `line-height` | **Vietnamese Mandatory Floor** | Recommended Token (`vi-VN`) | Clipping Prevention Rule |
|---|---|---|---|---|---|
| `--lh-display-2xl` | `60px`–`72px` | `1.0` | **`>= 1.18`** | `1.20` | Protects uppercase `Ẫ`, `Ễ`, `Ộ`, `Ữ` |
| `--lh-display-xl` | `48px`–`56px` | `1.05` | **`>= 1.18`** | `1.20` | Prevents top-edge acute/circumflex slicing |
| `--lh-heading-lg` | `32px`–`40px` | `1.10` | **`>= 1.22`** | `1.25` | Prevents multi-line collision with descenders |
| `--lh-heading-md` | `24px`–`28px` | `1.15` | **`>= 1.25`** | `1.30` | Recommended for card titles and section H2s |
| `--lh-heading-sm` | `18px`–`20px` | `1.20` | **`>= 1.28`** | `1.32` | Modal headers, tab bar active headers |
| `--lh-body-lg` | `16px`–`18px` | `1.35` | **`>= 1.50`** | `1.55` | Eliminates visual diacritic crowding in prose |
| `--lh-body-md` | `14px`–`15px` | `1.40` | **`>= 1.50`** | `1.55` | Standard interface copy, table cells, form labels |
| `--lh-body-sm` | `12px`–`13px` | `1.35` | **`>= 1.45`** | `1.50` | Helper text, error messages, metadata rows |
| `--lh-caption` | `10px`–`11px` | `1.20` | **`>= 1.35`** | `1.40` | Micro-badges, timestamps, footnote notes |

---

## 3. Letter-Spacing (Tracking) Rules for Diacritic Legibility

Dense diacritical accents require open horizontal breathing room:
- **Never apply negative tracking (`letter-spacing: -0.03em` or `-0.05em`) to Vietnamese text**, even on display headings. Negative tracking causes adjacent diacritical marks to bleed together (e.g. `trường`, `nghiệp`).
- **Display Headings (`>= 32px`):** `letter-spacing: -0.01em` to `0em` (neutral).
- **Body Text (`14px`–`18px`):** `letter-spacing: 0em` (neutral).
- **All-Caps Acronyms / Micro-Labels (`11px`–`13px`):** `letter-spacing: +0.02em` to `+0.05em`.
- **Currency (`₫`):** Always insert a non-breaking space before the currency symbol: `150.000\u00A0₫`.

---

## 4. OpenType Features for Precision Typography

Activate modern OpenType features in CSS to maximize legibility and visual rhythm:

```css
.vi-typography {
  /* Kerning and contextual alternates */
  font-feature-settings: "kern" 1, "liga" 1, "calt" 1;
  /* Tabular figures for data tables, metrics, and pricing */
  font-variant-numeric: tabular-nums;
  /* Crisp subpixel font rendering */
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

---

## 5. CSS Wrap Balancing & Non-Breaking Compound-Word Binding (`\u00A0`)

Vietnamese words are composed of isolated syllables separated by spaces (`khách hàng`, `doanh nghiệp`, `thanh toán`).
Standard browser line breaks break compounds across lines, leaving single-syllable orphans on trailing lines.

### Automated CSS Text-Wrap Rules:
```css
/* All Headings (H1, H2, H3, Modal Titles): Balance line breaks across all lines */
h1, h2, h3, .heading {
  text-wrap: balance;
}

/* Body Prose, Card Descriptions, and Tooltips: Prevent single-word trailing orphans */
p, .prose, .card-desc {
  text-wrap: pretty;
}
```

### Code-Level Compound Word Binding:
In localization strings or hero titles where `text-wrap: balance` is unsupported (e.g. email templates, canvas rendering):
- Bind the final 2-syllable compound with `\u00A0` (Unicode Non-Breaking Space `U+00A0`):
  ```json
  "hero.title": "Giải pháp quản trị dữ liệu cho doanh\u00A0nghiệp"
  ```

---

## 6. Horizontal Container Expansion Headroom (+20% to +35%)

Because Vietnamese is monosyllabic and requires separate words for grammatical particles, translated copy expands by +20% to +35% compared to English:

| Component Type | Max English Length | Max Vietnamese Budget | Container Layout Headroom |
|---|---|---|---|
| **Primary CTA Button** | `12 chars` ("Get Started") | **`24 chars`** ("Bắt đầu sử dụng") | Allocate `min-width: 140px` (avoid fixed `w-24`) |
| **Tab Bar Items** | `8 chars` ("Overview") | **`18 chars`** ("Bảng điều khiển") | Use `flex-1` or auto-layout scrollable tabs |
| **Status Badge** | `8 chars` ("Pending") | **`16 chars`** ("Đang chờ duyệt") | Use `inline-flex px-2.5 py-0.5 whitespace-nowrap` |
| **Toast Notification** | `45 chars` | **`90 chars`** | `max-w-md w-full` with flexible vertical height |
| **Table Column Headers** | `10 chars` ("Quantity") | **`18 chars`** ("Số lượng") | Standardize short abbreviations (`SL`, `Đơn giá`) |

- **Layout Rule:** Never apply fixed horizontal widths (`width: 80px`) to buttons, dropdown items, or navigation tabs containing localized Vietnamese strings. Use auto-layout (`w-auto min-w-[...]`) with responsive padding.
