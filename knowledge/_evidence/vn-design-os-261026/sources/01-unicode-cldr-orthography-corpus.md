# Primary Source Dossier 01: Unicode UAX #15, Orthography (Decision 1989/QĐ-BGDĐT), IME Composition, and CLDR vi-VN Collation

## 1. Unicode Normalization Form C (NFC) vs Normalization Form D (NFD)
- Quote-ID [claim-unicode-nfc-1]: "All Vietnamese digital text, source code, JSON payloads, and UI strings must be stored and transmitted in Unicode Normalization Form C (NFC) per Unicode Standard Annex #15 (UAX #15)."
- Quote-ID [claim-unicode-nfc-2]: "macOS APFS/HFS+ file names, Google Docs clipboard exports, and PDF text extractors frequently emit decomposed NFD sequences where a base vowel (e.g., U+006F 'o') is followed by combining circumflex (U+0302) and combining hook above (U+0309) instead of the single precomposed code point U+1ED5 ('ổ')."
- Quote-ID [claim-unicode-nfc-3]: "When NFD strings enter web or mobile interfaces without NFC normalization, font engines with incomplete OpenType GPOS mark-to-mark attachment tables render the tone mark detached to the right of the vowel, string.length increases by 1 to 2 code units per vowel, and exact substring or regex searches against NFC database indexes fail silently."

## 2. Legacy Vietnamese Encodings and UTF-8 Mojibake Detection
- Quote-ID [claim-unicode-nfc-4]: "Legacy Vietnamese encodings including TCVN3 (ABC, 1-byte shifting uppercase into control/extended ranges), VNI-Windows (2-byte vowel + tone code points), and Windows-1258 (CP1258, precomposed vowels + combining tone marks) must be converted to UTF-8 NFC before ingestion."
- Quote-ID [claim-unicode-nfc-5]: "Double-encoded UTF-8 mojibake (UTF-8 bytes misinterpreted as Latin-1/Windows-1252 and re-encoded to UTF-8) produces signature bigrams such as 'Ã¡', 'Ã ', 'áº£', 'á»‡', 'Æ°', 'Æ¡', and 'Ä‘', which rule ENC001 detects deterministically."

## 3. Vietnamese Tone Placement: New Style (Decision 1989/QĐ-BGDĐT) vs Traditional Style
- Quote-ID [claim-tone-orthography-1]: "Vietnamese tone placement diverges ONLY on open syllables containing the vowel sequences oa, oe, and uy (such as hòa vs hoà, khỏe vs khoẻ, thủy vs thuỷ, quý vs quí)."
- Quote-ID [claim-tone-orthography-2]: "Under Ministry of Education and Training (MOET) Decision 1989/QĐ-BGDĐT (2018), modern phonological style places the tone mark on the second vowel (hoà, khoẻ, thuỷ), whereas traditional typographical style places the tone mark on the first vowel (hòa, khỏe, thủy)."
- Quote-ID [claim-tone-orthography-3]: "Closed syllables ending in a consonant or semivowel (toàn, hoàn, doanh, khuynh, tuyệt, huyết), the consonant cluster qu + vowel (quả, quá, quản, quốc), the cluster gi + vowel (già, giá, giải), and all diphthongs/triphthongs with a diacritic vowel (iê, yê, uô, ươ) have invariant tone placement across both styles."
- Quote-ID [claim-tone-orthography-4]: "Rule TONE001 enforces intra-document consistency across lowercase, Title Case, and ALL CAPS occurrences of oa/oe/uy, and supports automated normalization via --fix-tone new or --fix-tone old."

## 4. Telex and VNI Input Method Editor (IME) Composition Hazards
- Quote-ID [claim-unicode-nfc-6]: "Vietnamese IMEs (macOS Native Vietnamese, Unikey, EVKey, OpenKey, Gboard) mutate preceding characters during active composition when the user types tone keys (s, f, r, x, j in Telex; 1-5 in VNI) or vowel modifiers (a, e, o, w, d in Telex; 6-9 in VNI)."
- Quote-ID [claim-unicode-nfc-7]: "Calling setState, string.trim(), toUpperCase(), or regex replacement inside an onChange handler while event.nativeEvent.isComposing is true aborts the active IME buffer and produces broken sequences such as 'Tiênsg Viêjt' or 'Ngaân haøng'."

## 5. CLDR vi-VN Collation and Diacritic-Insensitive Search
- Quote-ID [claim-unicode-nfc-8]: "Standard Unicode code-point sorting places 'Đ' (U+0110) and 'Ă' (U+0102) after 'Z' (U+005A); Vietnamese interfaces must sort lists using Intl.Collator('vi-VN', { usage: 'sort', sensitivity: 'variant' }) so the 29-letter Vietnamese alphabet orders A, Ă, Â, B, C, D, Đ, E, Ê, G, H, I, K, L, M, N, O, Ô, Ơ, P, Q, R, S, T, U, Ư, V, X, Y."
