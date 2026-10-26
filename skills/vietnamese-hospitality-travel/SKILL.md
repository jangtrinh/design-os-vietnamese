---
name: vietnamese-hospitality-travel
description: Writes, localizes, and audits native-quality Vietnamese (vi-VN) hospitality, resort, civil aviation, culinary F&B, and tourism communications. Enforces statutory hotel star rating boundaries under Luật Du lịch 2017 Điều 50 (1 to 5 stars only; prohibiting illegal 6-star or 7-star claims), transparent pricing under Luật Giá and Nghị định 109/2013/NĐ-CP (disclosing 5% service charge and 8% or 10% VAT for Net vs ++ rates), airline passenger care and refund rights during flight delays or cancellations under Thông tư 14/2015/TT-BGTVT and Thông tư 19/2023/TT-BGTVT, fine dining menu copywriting with mandatory allergen and tax footnotes, package tour contract structures under Luật Du lịch 2017 Điều 39 & 40, and courteous hospitality guest-address etiquette using the hospitality-luxury register (Quý khách).
license: PolyForm-Shield-1.0.0
metadata:
  author: "Jang Trinh"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Hospitality, Aviation, & Travel Copywriting (`vietnamese-hospitality-travel`)

In hospitality, luxury resort management, commercial aviation, and gastronomy, communication style defines the guest experience and brand prestige. A single bureaucratic or abrupt phrase (*"Cấm mang đồ ăn vào phòng"* or *"Khách tự chịu trách nhiệm nếu mất đồ"*) shatters the atmosphere of hospitality; an unexplained `++` price quotation breaches statutory pricing transparency; and a casual announcement of a cancelled flight omitting passenger rebooking rights violates civil aviation directives.

This skill equips engineers, hoteliers, airline operations teams, and marketing copywriters with authoritative, verified Vietnamese terminology, guest etiquette, and legal compliance structures aligned with current Vietnamese tourism and aviation law.

---

## 1. Register & Sociolinguistic Etiquette (`hospitality-luxury`)

Hospitality communication in Vietnam operates under refined sociolinguistic conventions established in [references/register-matrix.md](references/register-matrix.md):

| Context / Surface | Register | Reader Address (`Hô`) | Speaker (`Xưng`) | Tone Principles |
|---|---|---|---|---|
| 4–5 star hotels, luxury resorts, luxury villas | `hospitality-luxury` | `Quý khách` | `khu nghỉ dưỡng` / `khách sạn` / `chúng tôi` | Utmost courtesy, warmth, guest-centric phrasing |
| Commercial airlines (boarding pass, flight notices) | `hospitality-luxury` | `Quý khách` | `hãng hàng không` / `chúng tôi` | Authoritative, calm, deeply empathetic during disruptions |
| Fine Dining & contemporary gastronomy menus | `hospitality-luxury` | `Quý khách` | `nhà hàng` / `đội ngũ bếp` | Poetic, sensory, precise ingredient provenance |
| Tour itineraries & travel contracts | `hospitality-luxury` | `Quý khách` | `công ty lữ hành` / `chúng tôi` | Transparent inclusions, clear schedules, safety reassurance |

> [!IMPORTANT]
> **The Hospitality Formality Floor:** In Vietnamese customer service, addressing a resort guest or airline passenger as `bạn`, `mình`, or `cả nhà` is a severe defect (`PRO002`). Always address the guest as `Quý khách` (capitalizing `Q` as a sign of respect).

---

## 2. Statutory Hotel & Resort Standards (Luật Du lịch 2017 Điều 50)

As detailed in [references/hotel-and-resort-standards.md](references/hotel-and-resort-standards.md), Vietnamese law strictly regulates accommodation classifications:

1. **Star Rating Boundaries (`HOS002`):**
   - Official ratings span **1 to 5 stars only** (`1 sao đến 5 sao`), appraised exclusively by the Vietnam National Authority of Tourism (4–5 stars) or provincial tourism departments (1–3 stars).
   - Marketing claims of `khách sạn 6 sao`, `resort 7 sao`, or `tiêu chuẩn 6 sao` are deceptive advertising violations under Article 50 of Luật Du lịch 2017.
2. **Pricing Transparency: Net vs. "++" (`HOS001`):**
   - Unexplained `++` shorthand (e.g., `2.500.000++`) without itemizing service charge and VAT violates price disclosure regulations.
   - Always quote **Net prices** (*"2.887.500 ₫ net/đêm đã bao gồm 5% phí phục vụ và 10% thuế GTGT"*) or explicitly state the percentage breakdown (*"2.500.000 ₫ chưa bao gồm 5% phí phục vụ và 8% thuế GTGT"*).
3. **Mandatory Booking Disclosures (`HOS003`):**
   - A valid booking confirmation (`doctype == "hotel-booking"`) must clearly state standard check-in time (`từ 14:00`), standard check-out time (`trước 12:00`), early check-in / late check-out surcharges (`phụ thu`), and cancellation policies (`chính sách hoàn hủy`).
4. **Courteous Guest Phrasing (`HOS006`):**
   - Rephrase bureaucratic prohibitions into polite, guest-protective invitations:
     - ❌ `Cấm mang sầu riêng vào phòng.`
     - ✅ `Để bảo đảm không gian trong lành cho mọi kỳ nghỉ, Quý khách vui lòng không mang sầu riêng vào phòng ngủ.`

---

## 3. Civil Aviation Disruption Protocols (Thông tư 19/2023/TT-BGTVT)

As outlined in [references/aviation-and-tour-policies.md](references/aviation-and-tour-policies.md), Circular Thông tư 19/2023/TT-BGTVT governs airline communications during flight delays and cancellations (`HOS004`):

1. **Mandatory Elements of Disruption Notices (`doctype == "flight-notice"`):**
   - **Courteous Apology:** Must contain sincere regret (*"thành thật xin lỗi và mong Quý khách thông cảm"*).
   - **Statutory Passenger Rights:** Clearly state options for free rebooking (*"đổi chuyến bay miễn phí"*), meals/refreshments (*"phục vụ ăn uống"*), or ticket refunds (*"hoàn vé tự động"*).
2. **Standard Flight Fare Families:**
   - Standardize fare classes: `Phổ thông Tiết kiệm` (Economy Lite), `Phổ thông Tiêu chuẩn` (Economy Standard), `Phổ thông Đặc biệt` (Premium Economy), `Hạng Thương gia` (Business Class).

---

## 4. Culinary Copywriting & Menu Disclosures

As established in [references/fnb-and-culinary-copy.md](references/fnb-and-culinary-copy.md), luxury dining menus (`doctype == "fnb-menu"`) must balance sensory elegance with guest safety:

1. **Mandatory Disclosures (`HOS005`):**
   - **Allergen Warning:** Every menu must notify guests regarding food allergens (*"Quý khách có tiền sử dị ứng thực phẩm, xin vui lòng thông báo cho nhân viên phục vụ trước khi gọi món"*).
   - **Tax & Service Charge Status:** State clearly whether prices are Net or subject to 5% service charge and VAT.
2. **Three-Layer Dish Description Structure:**
   - Core dish title (`Bò Wagyu Nướng Than Hoa`) + cooking technique and local heritage origin (`tiêu rừng Tây Giang`) + puree/reduction sauce (`sốt rượu vang đỏ`).

---

## 5. Tour Itineraries & Package Contracts (Luật Du lịch 2017 Điều 39 & 40)

For outbound and inbound travel agencies (`doctype == "tour-itinerary"`):
1. **Mandatory Itinerary Breakdown:**
   - Explicit day-by-day schedules (morning, afternoon, evening activities).
   - Distinct enumeration of Inclusions (`đã bao gồm vé máy bay, khách sạn 4 sao, bảo hiểm du lịch`) and Exclusions (`chưa bao gồm chi phí cá nhân, tiền bồi dưỡng`).
2. **Travel Insurance & Emergency Support:**
   - Always state the comprehensive travel insurance coverage limit (`mức trách nhiệm bảo hiểm du lịch tối thiểu`).
   - Clearly delineate force majeure conditions (`thiên tai, dịch bệnh, hoàn cảnh bất khả kháng`).

---

## 6. Typographic & Numerical Formatting in Vietnamese Hospitality

To deliver seamless, professional communications, observe these typographical rules:
- **Tiền tệ (Currency):** Viết `2.500.000 ₫` (dấu chấm phân tách hàng nghìn, khoảng trắng mỏng và ký hiệu `₫`). Không viết `2,500,000 VND` hay `2.500k`.
- **Thời gian (24-Hour Clock):** Sử dụng định dạng `14:00`, `18:30`. Không dùng `2:00 PM` trong văn bản tiếng Việt chuẩn.
- **Ngày tháng (Date format):** Luôn theo thứ tự ngày/tháng/năm: `dd/MM/yyyy` (ví dụ: `20/04/2026`).
- **Số điện thoại hotline:** Định dạng quốc tế chuẩn `+84 297 388 9999` (bỏ số 0 đầu sau mã quốc gia +84).

---

## 7. Domain Rules Reference (`HOS001`–`HOS006`)

| Rule Code | Severity | Context | Description & Statutory Reference |
|---|---|---|---|
| `HOS001` | `ERROR` | All copy | Unexplained `++` pricing shorthand without disclosing service charge and VAT |
| `HOS002` | `ERROR` | All copy | Unrecognized/illegal star rating claim (`6 sao`, `7 sao` — Luật Du lịch 2017 Điều 50) |
| `HOS003` | `ERROR` | `hotel-booking` | Booking confirmation missing check-in/out times or cancellation/surcharge policy |
| `HOS004` | `ERROR` | `flight-notice` | Flight disruption notice missing polite apology or statutory passenger care rights |
| `HOS005` | `WARN` | `fnb-menu` | Menu missing allergen warning or tax/service charge status footnote |
| `HOS006` | `WARN` | All copy | Hostile or bureaucratic imperative phrasing toward guests |

---

## 8. Reference Documents & Verification Checklist

Review the accompanying reference guides for deep domain knowledge:
- [references/glossary.md](references/glossary.md): 55+ standardized hospitality, aviation, and culinary terms.
- [references/banned-phrases.md](references/banned-phrases.md): Prohibited claims, hostile imperatives, and superlatives.
- [references/hotel-and-resort-standards.md](references/hotel-and-resort-standards.md): Accommodation ratings, Net pricing, and surcharge rules.
- [references/aviation-and-tour-policies.md](references/aviation-and-tour-policies.md): Circular 19/2023/TT-BGTVT passenger rights and tour contracts.
- [references/fnb-and-culinary-copy.md](references/fnb-and-culinary-copy.md): Menu dish nomenclature, wine pairings, and allergen notices.
- [references/qa-checklist.md](references/qa-checklist.md): Comprehensive pre-publication inspection checklist.
- [references/examples.md](references/examples.md): 32 verified diagnostic pairs with before/after diffs.
- [assets/xac-nhan-dat-phong-resort.md.template](assets/xac-nhan-dat-phong-resort.md.template): Production-grade resort booking confirmation template.

---

## 9. Verification CLI Commands

Audit any hospitality markdown or text document using `validate_copy.py`:

```bash
# Validate a hotel booking confirmation with strict register enforcement
python skills/vietnamese-hospitality-travel/scripts/validate_copy.py \
  path/to/booking.md \
  --doctype hotel-booking \
  --register hospitality-luxury \
  --strict

# Validate a fine dining menu
python skills/vietnamese-hospitality-travel/scripts/validate_copy.py \
  path/to/menu.md \
  --doctype fnb-menu \
  --register hospitality-luxury
```
