<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-business-comms`

> Auto-generated from `evals/vietnamese-business-comms/pairs.jsonl` (31 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Zalo Oa

### ZNS001-promo-voucher (Rules: `ZNS001` · Doctype: `zns-transactional`)

```diff
- Kính gửi Quý khách, đơn hàng #12345 đã được đóng gói. Nhận ngay voucher giảm giá 20% cho đơn tiếp theo!
+ Kính gửi Quý khách, đơn hàng #12345 đã được bàn giao cho đơn vị vận chuyển. Mã vận đơn: VN12345678.
```
- **Why:** Transactional Zalo ZNS templates strictly forbid promotional phrases like 'voucher', 'giảm giá', or discounts.

### ZNS001-promo-deal (Rules: `ZNS001` · Doctype: `zns-transactional`)

```diff
- Tài khoản của Quý khách đã gia hạn thành công. Đặt mua ngay hôm nay để nhận ưu đãi đặc biệt!
+ Tài khoản của Quý khách đã gia hạn thành công. Gói dịch vụ có hiệu lực đến ngày 31/12/2026.
```
- **Why:** Transactional ZNS must not contain marketing callouts like 'mua ngay' or 'ưu đãi'; marketing belongs in ZBS.

### ZNS002-body-exceeds-400-nfc (Rules: `ZNS002` · Doctype: `zns`)

```diff
- Kính gửi Quý khách Nguyễn Văn An, Công ty Cổ phần Giải pháp Số xin trân trọng thông báo: Hệ sinh thái phần mềm quản trị doanh nghiệp của Quý khách đã hoàn tất đợt bảo trì nâng cấp định kỳ quý 1 năm 2026 vào lúc 04:00 sáng nay. Toàn bộ cơ sở dữ liệu và các phân hệ kế toán, quản trị đơn hàng, xuất hóa đơn điện tử, đồng bộ cổng thanh toán trực tuyến đã được kiểm tra và vận hành với độ ổn định tối đa. Nếu Quý khách gặp bất kỳ vấn đề kỹ thuật nào trong quá trình sử dụng hệ thống, xin vui lòng liên hệ ngay với đường dây nóng hỗ trợ kỹ thuật trực ban 24/7 của chúng tôi qua số tổng đài 1900 xxxx hoặc gửi thư điện tử về hòm thư hotro@domain.vn để được xử lý kịp thời. Trân trọng cảm ơn Quý khách!
+ Kính gửi Quý khách Nguyễn Văn An, hệ thống của Quý khách đã hoàn tất đợt bảo trì nâng cấp vào lúc 04:00 sáng nay. Mọi dịch vụ đã hoạt động ổn định bình thường. Mọi thắc mắc xin vui lòng liên hệ tổng đài 1900 xxxx hoặc email hotro@domain.vn để được hỗ trợ kịp thời. Trân trọng cảm ơn Quý khách!
```
- **Why:** Zalo Notification Service templates enforce a strict statutory limit of 400 NFC characters per body.

## Marketplace

### MKT001-title-spam-emoji (Rules: `MKT001` · Doctype: `marketplace-title`)

```diff
- 🔥 Cáp sạc nhanh Anker USB Type-C 100W bọc dù dài 1.2m màu đen
+ Anker Cáp sạc nhanh USB Type-C 100W bọc dù dài 1.2m màu đen
```
- **Why:** Shopee, Lazada, and TikTok Shop listing algorithms penalize spam emojis in product titles.

### MKT001-title-all-caps (Rules: `MKT001` · Doctype: `marketplace-title`)

```diff
- Samsung Tai nghe không dây SIÊU RẺ Galaxy Buds chống ồn chủ động màu trắng
+ Samsung Tai nghe không dây Galaxy Buds chống ồn chủ động màu trắng
```
- **Why:** ALL-CAPS words of 4+ letters (excluding whitelisted brands and technical standards) are banned on marketplace listing titles.

## Marketing Law

### MKT002-discount-over-50-unannotated (Rules: `MKT002` · Doctype: `promo`)

```diff
- Siêu hội mua sắm cuối năm giảm giá 70% toàn bộ phụ kiện công nghệ.
+ Siêu hội mua sắm cuối năm giảm giá 70% toàn bộ phụ kiện công nghệ. <!-- khuyen-mai-tap-trung: Quyết định số 1820/QĐ-BCT Tháng khuyến mại tập trung quốc gia 2026 -->
```
- **Why:** Promotions exceeding 50% are illegal under NĐ 81/2018 & NĐ 128/2024 without concentrated promotion approval annotation.

### MKT002-discount-over-50-cap (Rules: `MKT002` · Doctype: `promo`)

```diff
- Ưu đãi đặc biệt chiết khấu 60% cho khách hàng đăng ký sớm.
+ Ưu đãi đặc biệt chiết khấu 50% cho khách hàng đăng ký sớm.
```
- **Why:** Ordinary commercial discount without state-approved concentrated promotion program must be capped at 50%.

### MKT003-influencer-missing-disclosure (Rules: `MKT003` · Doctype: `influencer-post`)

```diff
- Sau 2 tuần trải nghiệm máy lọc không khí này thì mình thấy phòng ngủ đỡ bụi hẳn, recommend mọi người nên dùng thử nha.
+ #QuảngCáo Sau 2 tuần trải nghiệm máy lọc không khí do nhãn hàng tài trợ, mình thấy không gian phòng ngủ thông thoáng hơn rõ rệt.
```
- **Why:** Luật 75/2025/QH15 requires influencers to explicitly disclose sponsored content with tags like #QuảngCáo or 'Tài trợ bởi'.

### MKT003-influencer-partnership-tag (Rules: `MKT003` · Doctype: `influencer-post`)

```diff
- Bộ kem dưỡng ẩm này cứu rỗi làn da mùa đông của mình, mọi người nhấn link bio để xem chi tiết nhé.
+ Nội dung được tài trợ bởi Thương hiệu Mỹ phẩm ABC. Bộ kem dưỡng ẩm này giúp cấp ẩm hiệu quả cho làn da trong mùa hanh khô.
```
- **Why:** Sponsored promotional posts by KOL/KOC must carry explicit sponsorship disclosure before or within the post.

### SPAM001-bulk-sms-missing-optout (Rules: `SPAM001` · Doctype: `bulk-message`)

```diff
- Mừng khai xuân, tặng ngay mã ưu đãi 20% cho đơn hàng tiếp theo tại cửa hàng ABC.
+ Mừng khai xuân, tặng ngay mã ưu đãi 20% cho đơn hàng tiếp theo tại cửa hàng ABC. Để từ chối nhận tin, soạn TC gửi 1324.
```
- **Why:** Nghị định 91/2020 Điều 13 mandates an explicit, free refusal instruction in all promotional bulk messages.

### SPAM001-bulk-email-missing-unsubscribe (Rules: `SPAM001` · Doctype: `bulk-message`)

```diff
- Tri ân khách hàng thân thiết, nhận quà tặng đặc biệt khi mua sắm trong tuần này.
+ Tri ân khách hàng thân thiết, nhận quà tặng đặc biệt khi mua sắm trong tuần này. Nhấp vào đây để hủy nhận tin.
```
- **Why:** Bulk marketing broadcasts must provide a clear mechanism for recipients to opt out or unsubscribe.

### LAW001-superlative-so-1 (Rules: `LAW001`)

```diff
- Đây là nền tảng quản trị bán hàng số 1 Việt Nam hiện nay.
+ Đây là nền tảng quản trị bán hàng số 1 Việt Nam hiện nay. <!-- proof: Báo cáo thị trường của Hiệp hội Thương mại Điện tử Việt Nam 2025 -->
```
- **Why:** Claims of 'số 1' require documented proof under Luật Quảng cáo Đ8 K11 and Luật 75/2025/QH15.

### LAW001-superlative-tot-nhat (Rules: `LAW001`)

```diff
- Chúng tôi cam kết cung cấp dịch vụ máy chủ tốt nhất thị trường.
+ Chúng tôi cam kết cung cấp dịch vụ máy chủ đạt tiêu chuẩn quốc tế Tier 3 với độ sẵn sàng 99,99%.
```
- **Why:** Subjective superlatives like 'tốt nhất' are forbidden without certification; replace with verifiable metrics.

## B2B Sales

### SALES001-casual-pronoun-outreach (Rules: `SALES001` · Doctype: `cold-outreach`)

```diff
- Kính chào anh/chị, mình gửi bạn bản đề xuất giải pháp quản trị doanh nghiệp.
+ Kính chào anh/chị, em xin gửi anh/chị bản đề xuất giải pháp quản trị doanh nghiệp.
```
- **Why:** Casual pronouns like 'bạn' and 'mình' are forbidden in B2B commercial outreach; use kinship 'anh/chị' or 'em'.

### SALES001-casual-pronoun-dunning (Rules: `SALES001` · Doctype: `dunning`)

```diff
- Kính gửi đối tác, bên mình xin nhắc bạn thanh toán hóa đơn quá hạn.
+ Kính gửi Quý Doanh nghiệp, chúng tôi xin trân trọng thông báo đối chiếu công nợ cho hóa đơn quá hạn.
```
- **Why:** Dunning communications must use respectful professional pronouns ('chúng tôi' - 'Quý Doanh nghiệp'), never casual 'bạn' or 'mình'.

### SALES003-missing-courteous-opening-1 (Rules: `SALES003` · Doctype: `cold-outreach`)

```diff
- Tôi muốn giới thiệu giải pháp phần mềm tự động hóa quy trình nghiệp vụ cho doanh nghiệp của anh/chị.
+ Kính gửi Anh/Chị, tôi xin trân trọng giới thiệu giải pháp phần mềm tự động hóa quy trình nghiệp vụ cho doanh nghiệp.
```
- **Why:** B2B cold outreach emails must open with a courteous salutation like 'Kính gửi', 'Kính chào', or 'Chào Anh/Chị'.

### SALES003-missing-courteous-opening-2 (Rules: `SALES003` · Doctype: `cold-outreach`)

```diff
- Công ty chúng tôi vừa ra mắt nền tảng thương mại số, mong có cơ hội trao đổi cùng anh/chị.
+ Kính chào Quý Doanh nghiệp, chúng tôi xin trân trọng giới thiệu nền tảng thương mại số vừa ra mắt.
```
- **Why:** Unsolicited B2B sales outreach without courteous salutation damages brand reputation and triggers anti-spam filters.

### SALES004-quotation-missing-vat (Rules: `SALES004` · Doctype: `bao-gia`)

```diff
- Kính gửi Anh/Chị, bảng báo giá phần mềm trị giá 50.000.000 VND. Báo giá này có hiệu lực trong vòng 30 ngày.
+ Kính gửi Anh/Chị, bảng báo giá phần mềm trị giá 50.000.000 VND, chưa bao gồm 10% thuế GTGT. Báo giá này có hiệu lực trong vòng 30 ngày.
```
- **Why:** Quotations (báo giá) must explicitly disclose VAT status ('thuế GTGT' or 'VAT') to prevent commercial and tax disputes.

### SALES004-quotation-missing-validity (Rules: `SALES004` · Doctype: `bao-gia`)

```diff
- Kính gửi Anh/Chị, tổng chi phí triển khai giải pháp là 80.000.000 VND (đã bao gồm thuế GTGT).
+ Kính gửi Anh/Chị, tổng chi phí triển khai giải pháp là 80.000.000 VND (đã bao gồm thuế GTGT). Báo giá có giá trị đến ngày 30/04/2026.
```
- **Why:** Quotations must specify validity duration ('hiệu lực' or 'có giá trị đến') to avoid open-ended pricing liability.

## Admin Compliance

### ADMIN001-cong-van-missing-headers (Rules: `ADMIN001` · Doctype: `cong-van`)

```diff
- CÔNG TY CỔ PHẦN CÔNG NGHỆ ABC
- Số: 12/CV-ABC
- Hà Nội, ngày 10 tháng 03 năm 2026
- 
- V/v đề xuất hợp tác
- 
- Kính gửi: Sở Thông tin và Truyền thông
- 
- Chúng tôi trân trọng gửi công văn đề xuất hợp tác.
+ CÔNG TY CỔ PHẦN CÔNG NGHỆ ABC <!-- vlc-disable-line ENC001 -->        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
+ Số: 12/CV-ABC                                    Độc lập - Tự do - Hạnh phúc
+ Hà Nội, ngày 10 tháng 03 năm 2026
+ 
+ V/v đề xuất hợp tác
+ 
+ Kính gửi: Sở Thông tin và Truyền thông
+ 
+ Chúng tôi trân trọng gửi công văn đề xuất hợp tác.
```
- **Why:** Administrative dispatches (công văn) must include statutory Quốc hiệu and Tiêu ngữ under Nghị định 30/2020/NĐ-CP.

### ADMIN001-cong-van-missing-tieu-ngu (Rules: `ADMIN001` · Doctype: `cong-van`)

```diff
- CÔNG TY CỔ PHẦN CÔNG NGHỆ ABC <!-- vlc-disable-line ENC001 -->        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
- Số: 15/CV-ABC
- Hà Nội, ngày 12 tháng 03 năm 2026
- 
- V/v giải trình tiến độ
- 
- Kính gửi: Cục Thuế thành phố Hà Nội
- 
- Chúng tôi xin giải trình tiến độ nộp báo cáo.
+ CÔNG TY CỔ PHẦN CÔNG NGHỆ ABC <!-- vlc-disable-line ENC001 -->        CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
+ Số: 15/CV-ABC                                    Độc lập - Tự do - Hạnh phúc
+ Hà Nội, ngày 12 tháng 03 năm 2026
+ 
+ V/v giải trình tiến độ
+ 
+ Kính gửi: Cục Thuế thành phố Hà Nội
+ 
+ Chúng tôi xin giải trình tiến độ nộp báo cáo.
```
- **Why:** Quốc hiệu must be paired with statutory Tiêu ngữ 'Độc lập - Tự do - Hạnh phúc' separated by spaced hyphens.

## Calques

### CAL001-we-are-excited (Rules: `CAL001`)

```diff
- Chúng tôi là phấn khích thông báo tính năng mới đến các đối tác.
+ Chúng tôi rất vinh hạnh thông báo tính năng mới đến các đối tác.
```
- **Why:** 'Chúng tôi là phấn khích' is an unedited calque of English 'We are excited'.

### CAL001-hope-email-finds-you (Rules: `CAL001`)

```diff
- Hy vọng email này tìm thấy bạn khỏe mạnh và công việc thuận lợi.
+ Kính chúc anh/chị nhiều sức khỏe và công việc gặt hái nhiều thắng lợi.
```
- **Why:** 'Hy vọng email này tìm thấy bạn' is a literal translation of 'Hope this email finds you well'.

## Formatting

### NUM001-thousands-comma (Rules: `NUM001`)

```diff
- Tổng chi phí đầu tư hạ tầng mạng là 1,500,000 VND mỗi tháng.
+ Tổng chi phí đầu tư hạ tầng mạng là 1.500.000 VND mỗi tháng.
```
- **Why:** Vietnamese locale formatting uses periods (.) as thousands separators, not commas (,).

### NUM002-ungrouped-currency (Rules: `NUM002`)

```diff
- Gói dịch vụ cao cấp có mức giá ưu đãi là 2500000 VND.
+ Gói dịch vụ cao cấp có mức giá ưu đãi là 2.500.000 VND.
```
- **Why:** Currency amounts in Vietnamese must be grouped with periods every 3 digits (e.g. 2.500.000 VND).

### NUM003-decimal-period (Rules: `NUM003`)

```diff
- Tỷ lệ chuyển đổi đơn hàng trung bình đạt 4.5% trong quý vừa qua.
+ Tỷ lệ chuyển đổi đơn hàng trung bình đạt 4,5% trong quý vừa qua.
```
- **Why:** Vietnamese uses a comma (,) as a decimal separator, not a period (.).

## Pragmatics

### PRO001-mixed-formal-casual (Rules: `PRO001`)

```diff
- Kính mời Quý khách tham quan gian hàng. Bạn hãy nhấn vào liên kết bên dưới để nhận quà.
+ Kính mời Quý khách tham quan gian hàng. Quý khách vui lòng nhấn vào liên kết bên dưới để nhận quà.
```
- **Why:** Mixing formal ('Quý khách') and casual ('bạn') pronouns in the same document is a severe register defect.

### PRO002-zns-register-mismatch (Rules: `PRO002` · Register: `zns`)

```diff
- Đơn hàng của bạn đã được xác nhận thành công.
+ Đơn hàng của Quý khách đã được xác nhận thành công.
```
- **Why:** The ZNS register strictly forbids 'bạn' and expects 'Quý khách'.

### PRO002-b2b-register-mismatch (Rules: `PRO002` · Register: `b2b`)

```diff
- Kính chào anh/chị, em xin gửi thông tin chi tiết cho bạn qua thư này.
+ Kính chào anh/chị, em xin gửi thông tin chi tiết cho anh/chị qua thư này.
```
- **Why:** B2B commercial register addresses the counterparty as 'anh/chị', forbidding casual 'bạn'.

## Encoding

### NFC001-decomposed-unicode (Rules: `NFC001`)

```diff
- Đơn hàng số 12345 đã được giao thành công.
+ Đơn hàng số 12345 đã được giao thành công.
```
- **Why:** Vietnamese digital copy must use precomposed Unicode (NFC), not decomposed combining diacritics (NFD).

## Orthography

### TONE001-mixed-tone-placement (Rules: `TONE001`)

```diff
- Công ty mong muốn hợp tác hòa bình và tạo ra môi trường làm việc hoà hợp.
+ Công ty mong muốn hợp tác hòa bình và tạo ra môi trường làm việc hòa hợp.
```
- **Why:** Mixing both tone placement conventions (hòa vs hoà) in the same document violates Vietnamese orthographic consistency.
