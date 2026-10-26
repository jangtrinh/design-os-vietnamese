<!-- vlc-disable: all -->

# Vietnamese i18n Hazards & Engineering Defect Catalog (`vietnamese-tech-writing`)

Internationalizing software for Vietnamese (`vi-VN`) involves subtler engineering challenges than standard Latin languages. Beyond Unicode normalization, Vietnamese implementations encounter critical build-time and runtime hazards across string layout, character limits, telecommunication encoding, input method engines (IME), and database collation.

---

## 1. String Expansion & UI Layout Resilience

English-to-Vietnamese translation consistently expands string length by **25% to 35%**. For short buttons, tabs, and menu items, expansion can reach **100%**.

### String Expansion Multipliers in Product Surfaces

| English UI String | Length (Chars) | Vietnamese Translation | Length (Chars) | Expansion Rate |
|---|:---:|---|:---:|:---:|
| `Save` | 4 | `Lưu thay đổi` | 13 | **+225%** |
| `Cancel` | 6 | `Hủy bỏ` | 6 | 0% |
| `View cart` | 9 | `Xem giỏ hàng` | 12 | **+33%** |
| `Forgot password?` | 16 | `Quên mật khẩu?` | 14 | -12% |
| `Settings` | 8 | `Cài đặt hệ thống` | 17 | **+112%** |
| `Get started` | 11 | `Bắt đầu ngay hôm nay` | 21 | **+91%** |
| `Checkout` | 8 | `Tiến hành thanh toán` | 20 | **+150%** |

### Frontend Architectural Defenses
1. **Never Hardcode Fixed Widths on Action Buttons:**
   ```css
   /* ❌ Defective: Truncates Vietnamese text */
   .btn-primary { width: 120px; overflow: hidden; text-overflow: ellipsis; }

   /* ✅ Resilient: Content-driven with min-width safety */
   .btn-primary { min-width: 120px; width: auto; padding: 0.5rem 1.25rem; white-space: nowrap; }
   ```
2. **Multi-line Flexibility in Card Headings:**
   Hero headlines and card titles must permit flex-wrapping onto two lines at tablet and mobile breakpoints.
3. **Table Column Auto-Layout:**
   Data grid headers must allow auto-layout or text wrapping rather than fixed pixel constraints.

---

## 2. The UCS-2 70-Character SMS Cliff

Vietnamese telecommunication channels (OTP verification, transaction alerts, banking notifications) present a major cost cliff due to GSM character encoding:

- **Standard GSM 7-bit:** Unaccented ASCII text permits **160 characters per single SMS segment**.
- **UCS-2 (Unicode):** The presence of **even one Vietnamese diacritic** (e.g. `ế`, `ạ`, `đ`) instantly forces the telecommunication gateway to switch to UCS-2 encoding.
- Under UCS-2, the single segment limit drops precipitously from 160 characters to **70 characters**.
- Concatenated multipart SMS under UCS-2 drops to **67 characters per segment**.

```
Example:
"Ma xac thuc OTP cua ban la 123456. Ma co hieu luc trong 5 phut."
→ 64 chars, 0 diacritics → GSM 7-bit → 1 SMS segment (Cost: 1x).

"Mã xác thực OTP của bạn là 123456. Mã có hiệu lực trong 5 phút."
→ 64 chars, 14 diacritics → UCS-2 → 1 SMS segment (Cost: 1x, near 70-char cliff).

"Mã xác thực OTP của bạn là 123456. Mã có hiệu lực trong 5 phút. Vui lòng không chia sẻ mã này cho bất kỳ ai."
→ 107 chars → UCS-2 → 2 SMS segments (Cost: 2x!).
```

### Engineering Recommendation
- For low-cost SMS OTP: Transmit clean unaccented Vietnamese (*"Ma xac thuc..."*) if approved by compliance, or strictly engineer the accented message body to stay **under 70 characters**.
- For rich messaging: Migrate transactional alerts to Zalo Notification Service (ZNS) or In-App Push notifications where UTF-8 is supported without length-penalty multipliers.

---

## 3. ICU Plural Format: `other` Only

Vietnamese is an isolating, uninflected language with **zero grammatical plural inflections**. Plurality is indicated via lexical numerals or classifiers (`những`, `các`, `mỗi`).

Under Unicode Common Locale Data Repository (CLDR), Vietnamese defines exactly **one plural category: `other`**.

### The Copy-Paste ICU Defect (`ICU001`)

```json
// ❌ WRONG: Copy-pasted from English en.json containing 'one' branch
{
  "cartItemCount": "{count, plural, one {# sản phẩm} other {# sản phẩm}}"
}

// ✅ CORRECT: Pure Vietnamese CLDR format with 'other' only
{
  "cartItemCount": "{count, plural, other {# sản phẩm}}"
}

// ✅ CORRECT: Optional explicit zero branch (=0) is permitted for empty state
{
  "cartItemCount": "{count, plural, =0 {Chưa có sản phẩm nào} other {# sản phẩm}}"
}
```

---

## 4. Vietnamese Collation & Alphabetical Sorting

Sorting Vietnamese lists using standard ASCII code-point sorting (`Array.prototype.sort()`) results in completely broken alphabetical order:
- `Đ` (U+0110) sorts after `Z` in ASCII, whereas in Vietnamese it must sort immediately after `D`.
- Tone marks on vowels must be sorted hierarchically: Unaccented (`a`) → Huyền (`à`) → Hỏi (`ả`) → Ngã (`ã`) → Sắc (`á`) → Nặng (`ạ`).

### Production JavaScript Solution
```typescript
// ❌ WRONG: ASCII code-point sorting
const names = ["Đức", "An", "Bình", "Dương"];
names.sort(); // Output: ["An", "Bình", "Dương", "Đức"] (Đ placed at end!)

// ✅ CORRECT: Intl.Collator with Vietnamese locale
const viCollator = new Intl.Collator("vi", { sensitivity: "base", numeric: true });
names.sort(viCollator.compare);
// Output: ["An", "Bình", "Dương", "Đức"] (Đ correctly placed after D)
```

In SQL databases (PostgreSQL), configure the database or column collation to `vi_VN.UTF-8` or use ICU provider `collkey(name, 'vi-u-kn-true')`.

---

## 5. The Telex/VNI IME React Input Composition Bug

In modern React and Next.js applications, Vietnamese users typing via Telex or VNI input methods (Unikey, EVKey, macOS native Vietnamese keyboard) trigger **composition events** (`compositionstart`, `compositionupdate`, `compositionend`).

### The Bug
When an input field fires an `onChange` event during an active composition, premature keystrokes are evaluated before the tone mark combines with the vowel. This breaks controlled search inputs, autocomplete dropdowns, and form validation masks.

### The Production React Solution
```tsx
import React, { useState } from "react";

export function ResilientVietnameseSearchInput({ onSearch }: { onSearch: (query: string) => void }) {
  const [value, setValue] = useState("");
  const [isComposing, setIsComposing] = useState(false);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setValue(e.target.value);
    // Do not trigger search queries while user is actively composing a Telex tone
    if (!isComposing) {
      onSearch(e.target.value);
    }
  };

  const handleCompositionEnd = (e: React.CompositionEvent<HTMLInputElement>) => {
    setIsComposing(false);
    // Fire search once the tone mark has fully combined
    onSearch(e.currentTarget.value);
  };

  return (
    <input
      type="text"
      value={value}
      onChange={handleChange}
      onCompositionStart={() => setIsComposing(true)}
      onCompositionEnd={handleCompositionEnd}
      placeholder="Tìm kiếm tài liệu hoặc API..."
      className="search-input"
    />
  );
}
```

---

## 6. Web Font Subsetting & Tone Glyph Collisions

Vietnamese utilizes stacked diacritics where a vowel possesses both a vowel mutation (horn/breve/circumflex) and a tone mark simultaneously (`ễ`, `ệ`, `ộ`, `ữ`, `ỡ`).

### Web Font Pitfalls
1. **Incomplete Subsets:** Using generic "Latin" font subsets lacks the Latin Extended-B glyphs necessary for Vietnamese, causing browser fallback to mismatched system fonts ("ransom note effect"). Always load the dedicated `vietnamese` subset in Google Fonts / Next.js Font.
2. **Vertical Clipping (`line-height`):** Stacked diacritics extend above standard Latin ascenders and below baselines. Insufficient `line-height` or strict `overflow: hidden` clips uppercase stacked marks (`Ễ`, `Ệ`, `Ộ`). Maintain `line-height >= 1.4` for Vietnamese headings.
