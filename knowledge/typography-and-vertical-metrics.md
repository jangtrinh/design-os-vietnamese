---
id: "typography-and-vertical-metrics"
title: "DESIGN:OS Vietnamese Vertical Metrics, Stacked Diacritics, and Web Font Subsetting"
domain: "vietnamese-typography-and-design-systems"
description: "Verified specification for Vietnamese stacked diacritic vertical metrics, line-height floors, web font subsetting (134 precomposed glyphs + Đ/đ + ₫), and horizontal text expansion."
when:
  - "Configuring CSS/Tailwind typography tokens, line-heights, and font stacks for Vietnamese UI"
  - "Auditing .ttf/.otf/.woff2 fonts and @font-face unicode-range declarations with check_font_coverage.py"
  - "Preventing clipped diacritics (Ẫ, Ễ, Ộ, Ữ) and orphaned compound-word syllables"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md"
    sha256: "863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d"
---

# DESIGN:OS Vietnamese Vertical Metrics, Stacked Diacritics, and Web Font Subsetting

## Purpose

Defines the typographic and layout constraints required to render Vietnamese stacked diacritics (`Ẫ`, `Ễ`, `Ộ`, `Ữ`), prevent glyph fallback ("ransom-note" rendering), and accommodate `+20%` to `+35%` horizontal text expansion in DESIGN:OS interfaces.

## When to Use / When NOT

- **When to Use:**
  - Setting `line-height`, `overflow`, `padding-block`, and `@font-face` / `next/font/google` configurations in web or mobile design systems supporting `vi-VN`.
  - Auditing font files and CSS stylesheets with `check_font_coverage.py`.
- **When NOT to Use:**
  - Monospace ASCII-only terminal logs that never render natural-language Vietnamese text.

## Core Knowledge Content

### 1. Stacked Diacritic Vertical Excursions and Line-Height Floors

Vietnamese uppercase and lowercase vowels with circumflex or horn/breve plus a tone mark above (`Ấ, Ầ, Ẩ, Ẫ, Ế, Ề, Ể, Ễ, Ố, Ồ, Ổ, Ỗ, Ớ, Ờ, Ở, Ỡ, Ứ, Ừ, Ử, Ữ`) extend 25% to 38% above the Latin cap-height, while the dot-below tone mark (`Ạ, Ặ, Ậ, Ẹ, Ệ, Ị, Ọ, Ộ, Ợ, Ụ, Ự, Ỵ`) extends below the baseline into the descender zone.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Vietnamese uppercase and lowercase vowels with circumflex or horn/breve plus a tone mark above (Ấ, Ầ, Ẩ, Ẫ, Ế, Ề, Ể, Ễ, Ố, Ồ, Ổ, Ỗ, Ớ, Ờ, Ở, Ỡ, Ứ, Ừ, Ử, Ữ) extend 25% to 38% above the Latin cap-height, while the dot-below tone mark (Ạ, Ặ, Ậ, Ẹ, Ệ, Ị, Ọ, Ộ, Ợ, Ụ, Ự, Ỵ) extends below the baseline into the descender zone." -->

Applying English-tuned tight `line-height` values (such as Tailwind `leading-none` `1.0` or `leading-tight` `1.25` on body text) or placing `overflow: hidden` on single-line headings clips the top hook/tilde of `Ẩ/Ễ` and the bottom dot of `Ệ/Ộ`; DESIGN:OS enforces a minimum `line-height` of `1.5` for body text and `1.28` to `1.35` for display headings.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Applying English-tuned tight line-height values (such as Tailwind leading-none 1.0 or leading-tight 1.25 on body text) or placing overflow: hidden on single-line headings clips the top hook/tilde of 'Ẩ/Ễ' and the bottom dot of 'Ệ/Ộ'; DESIGN:OS enforces a minimum line-height of 1.5 for body text and 1.28 to 1.35 for display headings." -->

### 2. Web Font Subsetting (`vietnamese` Unicode Ranges)

Web font loading via `next/font/google` or `@font-face` must explicitly include the `vietnamese` subset (`U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB`); omitting it causes browser fallback to system fonts exclusively on accented characters ("ransom-note" glyph mismatch).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Web font loading via next/font/google or @font-face must explicitly include the 'vietnamese' subset (U+0102-0103, U+0110-0111, U+0128-0129, U+0168-0169, U+01A0-01A1, U+01AF-01B0, U+1EA0-1EF9, U+20AB); omitting it causes browser fallback to system fonts exclusively on accented characters ('ransom-note' glyph mismatch)." -->

### 3. Horizontal Expansion and Compound-Word Widow Prevention

Vietnamese translations expand horizontal string length by `+20%` to `+35%` compared to English (`Save` 4 chars -> `Lưu thay đổi` 12 chars); UI components must avoid fixed pixel widths and bind final two-syllable compound words with `U+00A0` non-breaking spaces to prevent orphaned syllables.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Vietnamese translations expand horizontal string length by +20% to +35% compared to English ('Save' 4 chars -> 'Lưu thay đổi' 12 chars); UI components must avoid fixed pixel widths and bind final two-syllable compound words with U+00A0 non-breaking spaces to prevent orphaned syllables." -->

## Failure Modes (Mandatory)

1. **Ransom-Note Font Fallback:** Configuring `Inter({ subsets: ['latin'] })` in Next.js without `'vietnamese'` renders `N, g, u, y, n` in Inter and `ễ` (`U+1EC5`) in Times New Roman or Arial.
2. **Clipped Uppercase Stacked Diacritics:** Applying `line-height: 1.05` and `overflow: hidden` on a hero title containing `CHUYỂN ĐỔI SỐ` or `NGUYỄN TRÃI` slices off the top hook/tilde of `Ể` and `Ễ`.
3. **Orphaned Final Compound Syllable:** Letting a hero headline wrap between `thành` and `công` (`...đăng ký thành` / `công`) instead of binding the compound word as `thành\u00A0công`.
