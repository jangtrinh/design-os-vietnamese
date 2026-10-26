<!-- vlc-disable: TONE001, DIA001 -->

# Unicode, Phonology, and Tone-Mark Standards (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. Encoding defects and mixed tone-mark conventions are **invisible to the naked eye** in most editors yet break web fonts, inflate database/SMS byte counts, corrupt full-text search, and cause string equality assertions to fail.

---

## 1. Always Emit Precomposed Unicode (`NFC`)

Every accented Vietnamese vowel with a tone mark can be represented in two canonically equivalent Unicode forms:

| Normalization Form | Codepoint Sequence for `ế` | `len(s)` in Python/JS | UTF-8 Bytes | Behavior in Production |
|---|---|---|---|---|
| **NFC (Precomposed — Mandatory)** | `U+1EBF` (`LATIN SMALL LETTER E WITH CIRCUMFLEX AND ACUTE`) | `1` | `3 bytes` (`\xE1\xBA\xBF`) | Matches font `cmap` glyphs, exact character limits, and search indexes |
| **NFD (Decomposed — Forbidden)** | `U+0065` (`e`) + `U+0302` (`̂`) + `U+0301` (`́`) | `3` | `5 bytes` | Detached/shifted accents in subset fonts, false character-limit overflows, failed SQL/JSON key lookups |

- **Rule `NFC001` (ERROR):** Any line where `unicodedata.normalize("NFC", line) != line` is rejected.
- **Auto-Repair:** Run `python3 scripts/validate_copy.py --fix <path>` to deterministically rewrite NFD to NFC in place.
- **Common NFD Vectors:** macOS APFS/HFS+ filenames (`os.listdir` returns NFD), text copied from Figma/PDF exports, and iOS clipboard payloads. Always call `.normalize('NFC')` at system ingestion boundaries.

---

## 2. Legacy Encoding & Mojibake Defense (`ENC001`)

Before UTF-8 became universal in Vietnam, four legacy encodings were widely used in government, accounting, and publishing:
1. **TCVN3 (ABC / TCVN 5712:1993):** 1-byte encoding that repurposes control characters and Latin-1 slots (`µ`, `¸`, `¹`, `¶`, `·`, `®`, `©`, `ª`, `«`, `¬`, `­`).
2. **VNI-Windows:** 2-byte composite encoding where vowel modifiers are suffix digits/bytes (`aù`, `aø`, `aû`, `aõ`, `aï`, `aâ`, `aê`, `oâ`, `où`, `uõ`, `ñ`).
3. **Windows-1258 (CP1258):** Microsoft Vietnamese codepage using combining tone marks (`0xCC`, `0xEC`, `0xD2`, `0xDE`, `0xF2`).
4. **UTF-8 Decoded as Latin-1 / CP1252 (Mojibake):** Produces signature byte-pair sequences such as `Ã¡`, `Ã `, `áº¡`, `áº£`, `Ã¢`, `áº¥`, `Ä‘`, `Æ°`, `Æ¡`, `á»™`.

- **Rule `ENC001` (ERROR):** `validate_copy.py` scans for UTF-8 mojibake and VNI/TCVN3 artifacts and flags corrupted strings immediately.

---

## 3. Tone-Mark Placement: Kiểu Mới vs Kiểu Cũ (`TONE001`)

Vietnamese orthography has two coexisting conventions for placing tone marks (`huyền`, `sắc`, `hỏi`, `ngã`, `nặng`) on syllables with **open medial+main vowel clusters** (`oa`, `oe`, `uy`) when **no final consonant** follows:

| Syllable Nucleus | Kiểu cũ (Traditional / Visually Centered) | Kiểu mới (QĐ 1989/QĐ-BGDĐT — Phonetic Main Vowel) | With Final Consonant (Identical in Both!) |
|---|---|---|---|
| **oa** (`o` = medial, `a` = main vowel) | `hòa`, `tòa`, `hóa`, `khóa`, `thỏa`, `họa`, `lòa`, `xóa` | `hoà`, `toà`, `hoá`, `khoá`, `thoả`, `hoạ`, `loà`, `xoá` | `toàn`, `hoàng`, `khoản`, `hoạt`, `toán`, `doanh` (always on `a`) |
| **oe** (`o` = medial, `e` = main vowel) | `khỏe`, `xòe`, `lòe`, `hòe`, `chóe`, `ngoẻo`* | `khoẻ`, `xoè`, `loè`, `hoè`, `choé` | `khoét`, `nhoèn`, `hoen` (always on `e`) |
| **uy** (`u` = medial, `y` = main vowel, excluding `qu-`) | `thủy`, `hủy`, `tùy`, `tụy`, `túy`, `lụy`, `nhụy`, `ngụy` | `thuỷ`, `huỷ`, `tuỳ`, `tuỵ`, `tuý`, `luỵ`, `nhuỵ`, `nguỵ` | `thuyền`, `huyện`, `quỳnh`, `quyết`, `tuyệt` (always on `y`/`ê`) |

### Invariant Nuclei (Never Shift the Tone Mark!)
Regardless of whether a project uses *kiểu mới* or *kiểu cũ*, the following vowel clusters have **one mandatory tone position**:
- **`qu + y`:** After `q`, `u` is part of the initial consonant cluster (`qu-`), so `y` is the sole vowel: **always** `quý`, `quỳ`, `quỷ`, `quỹ`, `quỵ` (never `qúy`).
- **`gi + a/e/o/u`:** In `già`, `giá`, `giả`, `giã`, `giạ`, `gió`, `giữ`, `giữa`, `gi` is the initial consonant; the tone mark sits on the main vowel (`a`, `o`, `ữ`), never on `i` (except when `i` is the only vowel: `gì`, `gỉ`).
- **Diphthongs with diacritic vowels (`iê`, `yê`, `uô`, `ươ`):** Tone mark **always** sits on the vowel carrying the diacritic (`ê`, `ô`, `ơ`): `tiến`, `kiểm`, `yếu`, `cuộc`, `muốn`, `trường`, `mượn`, `nước`, `tưởng`. When open (`ưa`, `ia`, `ua` without `qu-`): tone sits on the first vowel (`múa`, `chùa`, `mía`, `lừa`, `sữa`, `cửa`).
- **Triphthongs (`oai`, `oay`, `uây`, `uôi`, `ươi`, `iêu`, `yêu`, `uêu`, `uya`):** Tone mark sits on the middle (nuclear) vowel (`ngoài`, `xoáy`, `khuấy`, `cuối`, `mười`, `nhiều`, `khuya`).

### Policy & Deterministic Auto-Fix (`--fix-tone`)
- **Both `kiểu mới` and `kiểu cũ` are valid.** *Kiểu mới* aligns with Ministry of Education & Training textbooks (`Quyết định 1989/QĐ-BGDĐT`); *kiểu cũ* remains prevalent in legacy newspapers and corporate branding.
- **Mixing both within the same document or UI catalog is a defect (`TONE001`).**
- **Auto-Normalization:** `validate_copy.py` supports `--fix-tone new` and `--fix-tone old` to deterministically convert all open `oa/oe/uy` syllables (preserving lowercase, Title Case, and ALL CAPS) across an entire codebase.

---

## 4. Input Method Editors (Telex / VNI) & Frontend Composition Hazards

Vietnamese users type diacritics via **Telex** (`aw` → `ă`, `aa` → `â`, `dd` → `đ`, `ee` → `ê`, `ow` → `ơ`, `uw`/`w` → `ư`; tones `s` sắc, `f` huyền, `r` hỏi, `x` ngã, `j` nặng, `z` xóa dấu) or **VNI** (`1`–`5` for tones, `6`–`9` for diacritics).

### Critical Engineering Rules for UI Inputs:
1. **Never trigger search/submit or character-strip inside an active IME composition:**
   - In React/Next.js/Vue inputs, calling `.toUpperCase()`, `.replace()`, or slug-formatting inside `onChange` **while `event.nativeEvent.isComposing === true`** destroys the active Telex buffer (turning `Nguyễn` into `Nguyeenx` or `N-g-u-y-e-n`).
   - Always guard input transforms with `onCompositionStart` / `onCompositionEnd` or inspect `e.nativeEvent.isComposing`.
2. **Never strip diacritics from Personal Names:**
   - `Nguyễn Thị Minh Ánh` is the legal name; only bank wire fields explicitly constrained by SWIFT/NAPAS ASCII legacy rails may transliterate to `NGUYEN THI MINH ANH` (and must do so automatically in a preview without rejecting accented user input).

---

## 5. Collation, Sorting, and Accent-Insensitive Search

1. **Alphabetical Sort Order (`vi-VN` Collation):**
   - Standard Vietnamese order: `a, ă, â, b, c, d, đ, e, ê, g, h, i, k, l, m, n, o, ô, ơ, p, q, r, s, t, u, ư, v, x, y`.
   - Naive ASCII/UTF-8 codepoint sort (`Array.prototype.sort()`) places `đ` (`U+0111`) and `ă` (`U+0103`) **after `z`**, and scrambles `á, à, ả, ã, ạ` (`U+00E0` vs `U+1EA1`).
   - Always sort with `Intl.Collator('vi-VN', { sensitivity: 'variant' })` in JS/TS or `COLLATE "vi-VN-x-icu"` in PostgreSQL.
2. **Dual-Representation Search Indexing:**
   - Users frequently type search queries without diacritics (`can ho quan 2`, `giay chay bo nam`).
   - Normalize search queries and index a folded shadow column (`unicodedata.normalize('NFD', s)` → strip `Mn` combining marks → `.replace('đ', 'd').replace('Đ', 'D').lower()`).
