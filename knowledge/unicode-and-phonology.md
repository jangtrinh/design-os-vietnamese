---
id: "unicode-and-phonology"
title: "Vietnamese Unicode Normalization (NFC), Orthography (Decision 1989/QĐ-BGDĐT), and IME Composition"
domain: "vietnamese-language-engineering"
description: "Cryptographically verified specification for Vietnamese UTF-8 NFC normalization, legacy TCVN3/VNI/CP1258 mojibake detection, oa/oe/uy tone placement, Telex/VNI IME composition guards, and CLDR vi-VN collation."
when:
  - "Validating or normalizing Vietnamese strings in UI, APIs, databases, or i18n catalogs"
  - "Configuring Telex/VNI input handlers in React, Vue, SwiftUI, or Flutter"
  - "Resolving new-style (hoà, thuỷ) vs old-style (hòa, thủy) tone placement"
trust_tier: "verified"
version: "3.1.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md"
    sha256: "50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae"
  - uri: "_evidence/vn-design-os-261026/sources/04-engine-execution-verification-log.txt"
    sha256: "4149a4846143aa45aec3a7089226ddf8f8e791c97c437acb311b2d9910bdf4ef"
  - uri: "_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt"
    sha256: "abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b"
---

# Vietnamese Unicode Normalization (NFC), Orthography (Decision 1989/QĐ-BGDĐT), and IME Composition

## Purpose

Defines the foundational character-encoding, orthographic tone-placement, input-method composition, and alphabetical collation invariants required for zero-defect Vietnamese software and content systems in **DESIGN:OS Vietnamese**.

## When to Use / When NOT

- **When to Use:**
  - Ingesting text from macOS APFS file systems, Google Docs, PDFs, or legacy Vietnamese databases (`TCVN3`, `VNI-Windows`, `CP1258`).
  - Enforcing intra-document orthographic tone consistency (`TONE001`) across `oa`, `oe`, and `uy` vowel sequences.
  - Implementing controlled text inputs, search bars, or slug generators that interact with Vietnamese Telex/VNI IMEs.
- **When NOT to Use:**
  - Phonetic IPA transcription of regional Vietnamese dialects where non-standard orthography is intentionally preserved as linguistic data.

## Core Knowledge Content

### 1. UTF-8 Normalization Form C (NFC) Mandate (`NFC001`)

All Vietnamese digital text, source code, JSON payloads, and UI strings must be stored and transmitted in Unicode Normalization Form C (NFC) per Unicode Standard Annex #15 (UAX #15).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="All Vietnamese digital text, source code, JSON payloads, and UI strings must be stored and transmitted in Unicode Normalization Form C (NFC) per Unicode Standard Annex #15 (UAX #15)." -->

macOS APFS/HFS+ file names, Google Docs clipboard exports, and PDF text extractors frequently emit decomposed NFD sequences where a base vowel (`U+006F` `o`) is followed by combining circumflex (`U+0302`) and combining hook above (`U+0309`) instead of the single precomposed code point `U+1ED5` (`ổ`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="macOS APFS/HFS+ file names, Google Docs clipboard exports, and PDF text extractors frequently emit decomposed NFD sequences where a base vowel (e.g., U+006F 'o') is followed by combining circumflex (U+0302) and combining hook above (U+0309) instead of the single precomposed code point U+1ED5 ('ổ')." -->

When NFD strings enter web or mobile interfaces without NFC normalization, font engines with incomplete OpenType GPOS mark-to-mark attachment tables render the tone mark detached to the right of the vowel, `string.length` increases by 1 to 2 code units per vowel, and exact substring or regex searches against NFC database indexes fail silently.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="When NFD strings enter web or mobile interfaces without NFC normalization, font engines with incomplete OpenType GPOS mark-to-mark attachment tables render the tone mark detached to the right of the vowel, string.length increases by 1 to 2 code units per vowel, and exact substring or regex searches against NFC database indexes fail silently." -->

### 2. Legacy Vietnamese Encodings and Mojibake Detection (`ENC001`)

Legacy Vietnamese encodings including TCVN3 (ABC), VNI-Windows, and Windows-1258 (CP1258) must be converted to UTF-8 NFC before ingestion.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Legacy Vietnamese encodings including TCVN3 (ABC, 1-byte shifting uppercase into control/extended ranges), VNI-Windows (2-byte vowel + tone code points), and Windows-1258 (CP1258, precomposed vowels + combining tone marks) must be converted to UTF-8 NFC before ingestion." -->

Double-encoded UTF-8 mojibake (UTF-8 bytes misinterpreted as Latin-1/Windows-1252 and re-encoded to UTF-8) produces signature bigrams such as `Ã¡`, `Ã `, `áº£`, `á»‡`, `Æ°`, `Æ¡`, and `Ä‘`, which rule `ENC001` detects deterministically.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Double-encoded UTF-8 mojibake (UTF-8 bytes misinterpreted as Latin-1/Windows-1252 and re-encoded to UTF-8) produces signature bigrams such as 'Ã¡', 'Ã ', 'áº£', 'á»‡', 'Æ°', 'Æ¡', and 'Ä‘', which rule ENC001 detects deterministically." -->

### 3. Orthographic Tone Placement (`TONE001`)

Vietnamese tone placement diverges ONLY on open syllables containing the vowel sequences `oa`, `oe`, and `uy` (such as `hòa` vs `hoà`, `khỏe` vs `khoẻ`, `thủy` vs `thuỷ`, `quý` vs `quí`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Vietnamese tone placement diverges ONLY on open syllables containing the vowel sequences oa, oe, and uy (such as hòa vs hoà, khỏe vs khoẻ, thủy vs thuỷ, quý vs quí)." -->

Under Ministry of Education and Training (MOET) Decision 1989/QĐ-BGDĐT (2018), modern phonological style places the tone mark on the second vowel (`hoà`, `khoẻ`, `thuỷ`), whereas traditional typographical style places the tone mark on the first vowel (`hòa`, `khỏe`, `thủy`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Under Ministry of Education and Training (MOET) Decision 1989/QĐ-BGDĐT (2018), modern phonological style places the tone mark on the second vowel (hoà, khoẻ, thuỷ), whereas traditional typographical style places the tone mark on the first vowel (hòa, khỏe, thủy)." -->

Closed syllables ending in a consonant or semivowel (`toàn`, `hoàn`, `doanh`, `khuynh`, `tuyệt`, `huyết`), the consonant cluster `qu` + vowel (`quả`, `quá`, `quản`, `quốc`), the cluster `gi` + vowel (`già`, `giá`, `giải`), and all diphthongs/triphthongs with a diacritic vowel (`iê`, `yê`, `uô`, `ươ`) have invariant tone placement across both styles.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Closed syllables ending in a consonant or semivowel (toàn, hoàn, doanh, khuynh, tuyệt, huyết), the consonant cluster qu + vowel (quả, quá, quản, quốc), the cluster gi + vowel (già, giá, giải), and all diphthongs/triphthongs with a diacritic vowel (iê, yê, uô, ươ) have invariant tone placement across both styles." -->

Rule `TONE001` enforces intra-document consistency across lowercase, Title Case, and ALL CAPS occurrences of `oa`/`oe`/`uy`, and supports automated normalization via `--fix-tone new` or `--fix-tone old`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Rule TONE001 enforces intra-document consistency across lowercase, Title Case, and ALL CAPS occurrences of oa/oe/uy, and supports automated normalization via --fix-tone new or --fix-tone old." -->

Primary text of Quyết định 1989/QĐ-BGDĐT (25/5/2018), frozen from a mirror (hoatieu.vn). Its scope is the general-education curriculum and textbooks; it is not binding on product UI copy.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="BAN HÀNH QUY ĐỊNH VỀ CHÍNH TẢ TRONG CHƯƠNG TRÌNH, SÁCH GIÁO KHOA GIÁO DỤC PHỔ THÔNG" -->

Điều 8 puts the tone mark on the letter that writes the main vowel. Its own examples are `hoà`, `hoá`, `thuỷ`, `khoẻ`, which is the modern style for `oa`/`oe`/`uy`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="Trường hợp âm chính của âm tiết được ghi bằng một chữ cái, dấu thanh được đặt trên hoặc dưới chữ cái ghi âm chính của mỗi âm tiết, ví dụ: mái nhà, hoà nhạc, quý hoá, thuỷ thủ, mạnh khoẻ, trí tuệ,..." -->

Two-letter main vowels: `ia`, `ua`, `ưa` take the mark on the first letter; `iê`, `yê`, `uô`, `uơ` on the second.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="Đối với các kí hiệu ia, ua, ưa, dấu thanh đặt trên hoặc dưới chữ cái thứ nhất, ví dụ: bìa, lụa, lửa,..." -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="Đối với các kí hiệu iê, yê, uô, uơ, dấu thanh đặt trên hoặc dưới chữ cái thứ hai, ví dụ: biển, thuyền, nhuộm, được,..." -->

The decision states the placement rule, not the claim that styles diverge only on `oa`/`oe`/`uy`; that narrower claim is an inference from Điều 8 and rests on the project corpus above.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="Trường hợp âm chính của âm tiết được ghi bằng một chữ cái, dấu thanh được đặt trên hoặc dưới chữ cái ghi âm chính của mỗi âm tiết, ví dụ: mái nhà, hoà nhạc, quý hoá, thuỷ thủ, mạnh khoẻ, trí tuệ,..." -->

Related textbook rules: a bare `i` after an initial consonant is written `i` (`kỉ niệm`, `lí luận`, `mĩ thuật`), and decimals use a comma.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="Trường hợp âm i đứng ngay sau phụ âm đầu thì được viết bằng chữ i, ví dụ: hi vọng, kỉ niệm, lí luận, mĩ thuật, bác sĩ, tỉ lệ,..." -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/16-mirror-qd-1989-qd-bgddt-2018-chinh-ta-sgk.txt" sha256="abf5c4e412c53330c2b4f4b53fe1a4210d42f3d8de9a2b2c04138c72863d6d9b" quote="Khi viết các số thập phân, sử dụng dấu phẩy để ngăn cách giữa phần nguyên và phần thập phân, ví dụ: 3,8; 5,21; 10,43,..." -->

### 4. Telex/VNI IME Composition Safety and CLDR Collation

Vietnamese IMEs (macOS Native Vietnamese, Unikey, EVKey, OpenKey, Gboard) mutate preceding characters during active composition when the user types tone keys (`s, f, r, x, j` in Telex; `1-5` in VNI) or vowel modifiers (`a, e, o, w, d` in Telex; `6-9` in VNI).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Vietnamese IMEs (macOS Native Vietnamese, Unikey, EVKey, OpenKey, Gboard) mutate preceding characters during active composition when the user types tone keys (s, f, r, x, j in Telex; 1-5 in VNI) or vowel modifiers (a, e, o, w, d in Telex; 6-9 in VNI)." -->

Calling `setState`, `string.trim()`, `toUpperCase()`, or regex replacement inside an `onChange` handler while `event.nativeEvent.isComposing` is true aborts the active IME buffer and produces broken sequences such as `Tiênsg Viêjt` or `Ngaân haøng`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Calling setState, string.trim(), toUpperCase(), or regex replacement inside an onChange handler while event.nativeEvent.isComposing is true aborts the active IME buffer and produces broken sequences such as 'Tiênsg Viêjt' or 'Ngaân haøng'." -->

Standard Unicode code-point sorting places `Đ` (`U+0110`) and `Ă` (`U+0102`) after `Z` (`U+005A`); Vietnamese interfaces must sort lists using `Intl.Collator('vi-VN', { usage: 'sort', sensitivity: 'variant' })` so the 29-letter Vietnamese alphabet orders `A, Ă, Â, B, C, D, Đ, E, Ê, G, H, I, K, L, M, N, O, Ô, Ơ, P, Q, R, S, T, U, Ư, V, X, Y`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/01-unicode-cldr-orthography-corpus.md" sha256="50a85a767aeee5790aa442deb2346390d7f6bce8a87676d22bdb4c2b1b0958ae" quote="Standard Unicode code-point sorting places 'Đ' (U+0110) and 'Ă' (U+0102) after 'Z' (U+005A); Vietnamese interfaces must sort lists using Intl.Collator('vi-VN', { usage: 'sort', sensitivity: 'variant' }) so the 29-letter Vietnamese alphabet orders A, Ă, Â, B, C, D, Đ, E, Ê, G, H, I, K, L, M, N, O, Ô, Ơ, P, Q, R, S, T, U, Ư, V, X, Y." -->

## Failure Modes (Mandatory)

1. **Silent NFD Database Miss (`NFC001`):** Storing macOS clipboard text without `.normalize('NFC')` causes SQL `WHERE name = 'Nguyễn'` to return 0 rows when the stored bytes contain `e + U+0302 + U+0303`.
2. **Closed-Syllable Tone Corruption (`TONE001`):** Naive regex replace of `òa -> oà` without checking syllable closure corrupts `toàn` into invalid `toàn -> toà-n`. Always restrict `TONE001` to open syllables (`(?![a-zA-ZÀ-ỹ])`).
3. **React Controlled Input IME Tear:** Applying live formatting (slugify, uppercase, trim) inside `onChange` without guarding `if (e.nativeEvent.isComposing) return;` breaks Telex/VNI typing on macOS Safari and Chrome.
4. **Diacritic Strip Missing `Đ/đ`:** Using `.normalize('NFD').replace(/[\u0300-\u036f]/g, '')` leaves `Đ` (`U+0110`) and `đ` (`U+0111`) intact because the crossbar is a distinct base letter, not a combining mark. Always chain `.replace(/đ/g, 'd').replace(/Đ/g, 'D')`.
