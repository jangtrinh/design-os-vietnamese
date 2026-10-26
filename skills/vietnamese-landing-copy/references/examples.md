<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-landing-copy`

> Auto-generated from `evals/vietnamese-landing-copy/pairs.jsonl` (37 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Calque

### cal-learn-more (Rules: `CAL001`)

```diff
- Học thêm về dự án của chúng tôi
+ Tìm hiểu thêm về dự án
```
- **Why:** `Học thêm` is academic tutoring/studying; commercial information discovery uses `Tìm hiểu thêm`.

### cal-get-started (Rules: `CAL001`)

```diff
- Bắt đầu được với phần mềm của chúng tôi
+ Bắt đầu ngay với phần mềm của chúng tôi
```
- **Why:** `Bắt đầu được` imports an English particle into a modal capability sense; write `Bắt đầu ngay`.

### cal-see-details (Rules: `CAL001`)

```diff
- Nhìn chi tiết bảng giá
+ Xem chi tiết bảng giá
```
- **Why:** Physical looking (`nhìn`) is incorrect for examining documents or web listings (`xem`).

### cal-sign-up (Rules: `CAL001`)

```diff
- Ký lên để nhận tin
+ Đăng ký nhận tin
```
- **Why:** `Ký lên` is a word-for-word calque of 'sign up'; the standard term is `đăng ký`.

### cal-contact-us (Rules: `CAL001`)

```diff
- Liên lạc chúng tôi ngay hôm nay
+ Liên hệ ngay với chúng tôi
```
- **Why:** `Liên lạc` refers to radio/phone transmission channels; inbound sales enquiries use `liên hệ`.

### cal-testimonials (Rules: `CAL001`)

```diff
- Lời chứng thực từ đối tác
+ Cảm nhận khách hàng từ đối tác
```
- **Why:** `Chứng thực` is legal notarial verification; marketing endorsements are `cảm nhận khách hàng`.

### cal-trusted-by (Rules: `CAL001`)

```diff
- Tin tưởng bởi 500 doanh nghiệp
+ Được 500 doanh nghiệp tin dùng
```
- **Why:** Passive 'by' calqued as `bởi`; Vietnamese uses `Được [agent] tin dùng`.

### cal-free-shipping (Rules: `CAL001`)

```diff
- Vận chuyển tự do toàn quốc
+ Miễn phí giao hàng toàn quốc
```
- **Why:** `Tự do` means liberty/unconstrained, not zero monetary cost; use `miễn phí giao hàng`.

### cal-add-to-cart (Rules: `CAL001`)

```diff
- Thêm vào xe đẩy ngay
+ Thêm vào giỏ hàng ngay
```
- **Why:** `Xe đẩy` is a physical supermarket trolley; web shopping uses `giỏ hàng`.

### cal-privacy-policy (Rules: `CAL001`)

```diff
- Xem Chính sách riêng tư của chúng tôi
+ Xem Chính sách bảo mật của chúng tôi
```
- **Why:** `Riêng tư` refers to personal lifestyle privacy; statutory documents use `Chính sách bảo mật`.

### cal-one-stop (Rules: `CAL001`)

```diff
- Giải pháp một cửa cho văn phòng hiện đại
+ Giải pháp trọn gói cho văn phòng hiện đại
```
- **Why:** `Một cửa` is state public administration; commercial turnkey packages are `trọn gói`.

### cal-click-here (Rules: `CAL001`)

```diff
- Nhấp vào đây để nhận ưu đãi
+ Xem chi tiết để nhận ưu đãi
```
- **Why:** 'Click here' (`nhấp vào đây`) is weak microcopy; state the user outcome directly.

### cal-order-in-stock (Rules: `CAL001`)

```diff
- Sản phẩm hiện đang trong cổ phiếu
+ Sản phẩm hiện đang còn hàng
```
- **Why:** `Cổ phiếu` means financial equities; warehouse stock is `còn hàng`.

### cal-real-time (Rules: `CAL001`)

```diff
- Cập nhật dữ liệu trong thời gian thực
+ Cập nhật dữ liệu theo thời gian thực
```
- **Why:** Vietnamese uses preposition `theo` for dynamic tracking, not static containment `trong`.

## Word Order

### cal-word-order (Rules: `CAL001`)

```diff
- Khám phá các cao cấp căn hộ ven sông
+ Khám phá các căn hộ cao cấp ven sông
```
- **Why:** Vietnamese places qualifying adjectives after nouns (`căn hộ cao cấp`).

## Register

### cal-chung-ta (Rules: `CAL001`)

```diff
- Chúng ta cung cấp nền tảng quản trị kho
+ Chúng tôi cung cấp nền tảng quản trị kho
```
- **Why:** Inclusive `chúng ta` mistakenly claims the customer is part of the corporate entity.

### pro-mixed-document (Rules: `PRO001`)

```diff
- Kính chào Quý khách. Bạn hãy đăng ký tham quan nhà mẫu ngay.
+ Kính chào Quý khách. Quý khách vui lòng đăng ký tham quan nhà mẫu ngay.
```
- **Why:** A document must maintain one consistent audience address register throughout.

### pro-register-mismatch (Rules: `PRO002` · Register: `saas`)

```diff
- Kính chào Quý khách đến với nền tảng của chúng tôi.
+ Chào mừng bạn đến với nền tảng của chúng tôi.
```
- **Why:** The `saas` register is approachable and peer-level (`bạn`); `Quý khách` signals corporate stiffness.

## Legal

### law-number-one (Rules: `LAW001`)

```diff
- Thương hiệu ghế massage số 1 Việt Nam
+ Thương hiệu ghế massage được hơn 50.000 gia đình tin dùng
```
- **Why:** `số 1` without certified proof violates Điều 8 khoản 11 Luật Quảng cáo.

### law-best-market (Rules: `LAW001`)

```diff
- Dự án căn hộ tốt nhất thị trường
+ Dự án căn hộ chuẩn sinh thái ven sông
```
- **Why:** `tốt nhất` is an unproven absolute superlative; replace with an aspirational feature phrase.

### law-leading-developer (Rules: `LAW001`)

```diff
- Chủ đầu tư hàng đầu Việt Nam
+ Chủ đầu tư với hơn 20 năm kinh nghiệm tại Việt Nam
```
- **Why:** `hàng đầu` is a regulated superiority claim requiring licensed market survey proof.

## Unicode

### nfc-decomposed (Rules: `NFC001`)

```diff
- Căn hộ cao cấp tại dự án mới
+ Căn hộ cao cấp tại dự án mới
```
- **Why:** NFD decomposed diacritics break web font layout and text length counting.

## Diacritics

### dia-unaccented (Rules: `DIA001`)

```diff
- Can ho cao cap quan 9 mo ban gia goc
+ Căn hộ cao cấp Quận 9 mở bán giá gốc
```
- **Why:** Unaccented Vietnamese belongs in search URLs and slugs, never in user-facing marketing copy.

## Tone

### tone-mixed-style (Rules: `TONE001`)

```diff
- Dự án khu đô thị hoà bình và hòa thuận.
+ Dự án khu đô thị hoà bình và hoà thuận.
```
- **Why:** Inconsistent tone placement within a single document looks unproofread.

## Number

### num-comma-group (Rules: `NUM001`)

```diff
- Ưu đãi đặt cọc chỉ 50,000 ₫ hôm nay.
+ Ưu đãi đặt cọc chỉ 50.000 ₫ hôm nay.
```
- **Why:** Vietnamese currency groups thousands with periods (`50.000 ₫`), not commas.

### num-ungrouped (Rules: `NUM002`)

```diff
- Giá thuê khởi điểm từ 50000 ₫ một ngày.
+ Giá thuê khởi điểm từ 50.000 ₫ một ngày.
```
- **Why:** Amounts of 5 digits or more must group thousands with periods.

### num-dot-decimal (Rules: `NUM003`)

```diff
- Tỷ lệ hấp thụ sản phẩm đạt 15.5% trong tuần đầu.
+ Tỷ lệ hấp thụ sản phẩm đạt 15,5% trong tuần đầu.
```
- **Why:** Vietnamese uses comma for decimal fractions (`15,5%`).

### num-ascii-sqm (Rules: `NUM004`)

```diff
- Giá thuê mặt bằng chỉ từ 350.000 ₫/m2 một tháng.
+ Giá thuê mặt bằng chỉ từ 350.000 ₫/m² một tháng.
```
- **Why:** Professional typography uses superscript `m²` for square meters.

## Date

### date-mm-dd (Rules: `DATE001`)

```diff
- Thời hạn đăng ký trước ngày 09/28/2026.
+ Thời hạn đăng ký trước ngày 28/09/2026.
```
- **Why:** Vietnamese locale formatting strictly requires dd/MM/yyyy date ordering.

## Phone

### phone-trunk-zero (Rules: `PHONE001`)

```diff
- Tổng đài chăm sóc khách hàng: +84 0912 345 678.
+ Tổng đài chăm sóc khách hàng: +84 912 345 678.
```
- **Why:** The leading 0 must be dropped when using country code +84.

## I18N

### icu-plural-branches (Rules: `ICU001`)

```diff
- {"units": "{count, plural, one {# căn hộ} other {# căn hộ}}"}
+ {"units": "{count, plural, other {# căn hộ}}"}
```
- **Why:** Vietnamese CLDR plural has only the `other` branch; `one` is a copy-paste error from English.

## Syntax

### syn-dummy-subject (Rules: `SYN001`)

```diff
- Nó là rất quan trọng để tối ưu hóa quy trình bán hàng.
+ Việc tối ưu hóa quy trình bán hàng là rất quan trọng.
```
- **Why:** Vietnamese has no dummy 'it'; recast as a topicalized noun clause or direct verb.

## Landing

### lnd-hero-passive (Rules: `LND001` · Doctype: `hero`)

```diff
- Biệt thự ven sông được thiết kế bởi kiến trúc sư Foster.
+ Biệt thự ven sông do kiến trúc sư Foster thiết kế.
```
- **Why:** Hero headlines should front the actor active-voice (`Do [agent] thiết kế`).

### lnd-leadform-compliance (Rules: `LND002` · Doctype: `lead-form`)

```diff
- Để lại thông tin gồm họ và tên và số điện thoại để nhận tư vấn ngay.
+ Để lại họ và tên và số điện thoại. Tôi đồng ý để công ty xử lý dữ liệu cá nhân theo Chính sách bảo mật nhằm mục đích tư vấn sản phẩm.
```
- **Why:** Nghị định 13/2023/NĐ-CP requires stating the processing purpose and referencing Chính sách bảo mật.

### lnd-footer-compliance (Rules: `LND003` · Doctype: `ecommerce-footer`)

```diff
- Công ty TNHH Bán Lẻ Thời Trang. Địa chỉ trụ sở: 45 Lê Duẩn, Quận 1. Hotline: 0912345678.
+ Công ty TNHH Bán Lẻ Thời Trang. MST: 0312345678. Địa chỉ trụ sở: 45 Lê Duẩn, Quận 1. Hotline: 0912345678. Đã thông báo Bộ Công Thương.
```
- **Why:** Nghị định 52/2013/NĐ-CP & 85/2021/NĐ-CP mandate displaying MST and Bộ Công Thương registration.

### lnd-pricing-month (Rules: `LND004` · Doctype: `pricing-table`)

```diff
- Gói dịch vụ chuyên nghiệp giá 499.000 ₫/month dành cho đội nhóm.
+ Gói dịch vụ chuyên nghiệp giá 499.000 ₫/tháng dành cho đội nhóm.
```
- **Why:** Pricing tables on Vietnamese sites must use `/tháng` or `/năm`, not English `/month`.

### lnd-pricing-mixed-scale (Rules: `LND004` · Doctype: `pricing-table`)

```diff
- Gói cơ bản giá 500k một tháng, gói nâng cao giá 1.500.000 ₫ một tháng.
+ Gói cơ bản giá 500.000 ₫ một tháng, gói nâng cao giá 1.500.000 ₫ một tháng.
```
- **Why:** Pricing tables must maintain uniform denomination formatting across tiers.
