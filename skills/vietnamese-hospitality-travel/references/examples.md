<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-hospitality-travel`

> Auto-generated from `evals/vietnamese-hospitality-travel/pairs.jsonl` (32 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Pricing

### hos-plusplus-01 (Rules: `HOS001`)

```diff
- Giá phòng nghỉ dưỡng ưu đãi chỉ 1.500.000++ mỗi đêm.
+ Giá phòng nghỉ dưỡng ưu đãi: 1.500.000 ₫ mỗi đêm (chưa bao gồm 5% phí phục vụ và 8% thuế GTGT).
```

### hos-plusplus-02 (Rules: `HOS001`)

```diff
- Giá vé tiệc tối cuối tuần: 850.000 ₫++ dành cho một người.
+ Giá vé tiệc tối cuối tuần: 981.750 ₫ net dành cho một khách (đã bao gồm 5% phí phục vụ và 8% thuế GTGT).
```

### hos-plusplus-03 (Rules: `HOS001`)

```diff
- Chi phí gói spa trị liệu là 1.200.000 ₫ chưa gồm ++ theo quy định.
+ Chi phí gói trị liệu spa là 1.200.000 ₫ (chưa bao gồm 5% phí phục vụ và 10% thuế GTGT).
```

### hos-plusplus-04 (Rules: `HOS001`)

```diff
- Giá phòng Deluxe từ 2.000.000++ áp dụng cho đặt phòng trong tuần.
+ Giá phòng Deluxe từ 2.310.000 ₫ net mỗi đêm (đã bao gồm 5% phí phục vụ và 10% thuế GTGT).
```

### hos-plusplus-05 (Rules: `HOS001`)

```diff
- Thực đơn gọi món giá từ 350.000++ cho các món chính.
+ Thực đơn gọi món có giá từ 350.000 ₫ (chưa bao gồm 5% phí phục vụ và 8% thuế GTGT).
```

## Rating

### hos-star-01 (Rules: `HOS002`)

```diff
- Trải nghiệm dịch vụ nghỉ dưỡng tại khách sạn 6 sao đầu tiên tại Đà Nẵng.
+ Trải nghiệm dịch vụ nghỉ dưỡng tại khách sạn 5 sao sang trọng tại Đà Nẵng.
```

### hos-star-02 (Rules: `HOS002`)

```diff
- Khu nghỉ dưỡng resort 7 sao trên đảo Phú Quốc với bãi biển riêng.
+ Khu nghỉ dưỡng 5 sao cao cấp trên đảo Phú Quốc với bãi biển riêng biệt.
```

### hos-star-03 (Rules: `HOS002`)

```diff
- Tận hưởng kỳ nghỉ chuẩn tiêu chuẩn 6 sao quốc tế giữa lòng vịnh Hạ Long.
+ Tận hưởng kỳ nghỉ chuẩn 5 sao quốc tế giữa lòng vịnh Hạ Long.
```

### hos-star-04 (Rules: `HOS002`)

```diff
- Tòa tháp khách sạn cung cấp dịch vụ 6 sao dành riêng cho giới thượng lưu.
+ Tòa tháp khách sạn cung cấp dịch vụ chuẩn 5 sao quốc tế dành riêng cho thượng khách.
```

### hos-star-05 (Rules: `HOS002`)

```diff
- Biệt thự nghỉ dưỡng đẳng cấp 7 sao với quản gia phục vụ riêng.
+ Biệt thự nghỉ dưỡng 5 sao sang trọng với quản gia phục vụ riêng.
```

## Booking

### hos-booking-01 (Rules: `HOS003` · Doctype: `hotel-booking`)

```diff
- Xác nhận đặt phòng thành công cho khách hàng Nguyễn Văn An. Mã số phòng: 402.
+ Xác nhận đặt phòng thành công dành cho Quý khách Nguyễn Văn An. Thời gian nhận phòng từ 14:00 và trả phòng trước 12:00. Chính sách hoàn hủy: miễn phí trước 07 ngày nhận phòng, sau thời gian này áp dụng phụ thu theo quy định.
```

### hos-booking-02 (Rules: `HOS003` · Doctype: `hotel-booking`)

```diff
- Khách sạn đã ghi nhận đơn đặt phòng. Giờ nhận phòng từ 14:00 ngày mai.
+ Khách sạn đã ghi nhận đặt phòng của Quý khách. Giờ nhận phòng từ 14:00 và trả phòng trước 12:00. Trường hợp thay đổi lịch trình, Quý khách vui lòng tham khảo chính sách hoàn hủy phòng đính kèm.
```

### hos-booking-03 (Rules: `HOS003` · Doctype: `hotel-booking`)

```diff
- Chi tiết lưu trú: Khách trả phòng trước 12:00 trưa. Thanh toán tiền mặt khi tới nơi.
+ Chi tiết lưu trú: Quý khách nhận phòng từ 14:00 và trả phòng trước 12:00. Mọi yêu cầu hoàn hủy phòng hoặc nhận phòng sớm xin vui lòng liên hệ trước để áp dụng biểu phí phụ thu phù hợp.
```

### hos-booking-04 (Rules: `HOS003` · Doctype: `hotel-booking`)

```diff
- Xác nhận biệt thự nghỉ dưỡng. Giờ nhận phòng 14:00, trả phòng 12:00 ngày 25/08/2026.
+ Xác nhận biệt thự nghỉ dưỡng. Giờ nhận phòng từ 14:00 và trả phòng trước 12:00 ngày 25/08/2026. Quý khách được quyền hoàn hủy phòng miễn phí trước 05 ngày khởi hành; sau thời gian trên áp dụng mức phụ thu tương ứng.
```

## Aviation

### hos-flight-01 (Rules: `HOS004` · Doctype: `flight-notice`)

```diff
- Chuyến bay VN 154 bị chậm chuyến 3 tiếng do thời tiết xấu.
+ Chuyến bay VN 154 dự kiến khởi hành muộn 3 tiếng vì lý do thời tiết. Vietnam Airlines thành thật xin lỗi và mong Quý khách thông cảm vì sự chậm trễ này. Hãng hỗ trợ phục vụ ăn uống và quyền đổi chuyến bay miễn phí tại quầy dịch vụ.
```

### hos-flight-02 (Rules: `HOS004` · Doctype: `flight-notice`)

```diff
- Thông báo hủy chuyến bay QH 212 từ Hà Nội đi Đà Nẵng ngày hôm nay.
+ Bamboo Airways chân thành cáo lỗi và rất lấy làm tiếc thông báo chuyến bay QH 212 từ Hà Nội đi Đà Nẵng hôm nay phải hủy vì lý do kỹ thuật. Quý khách có quyền đổi chuyến bay kế tiếp miễn phí hoặc nhận hoàn vé toàn phần theo quy định.
```

### hos-flight-03 (Rules: `HOS004` · Doctype: `flight-notice`)

```diff
- Chuyến bay VJ 302 thay đổi giờ bay từ 08:00 sang 13:00. Hành khách có mặt đúng giờ mới.
+ Chuyến bay VJ 302 dự kiến thay đổi giờ bay từ 08:00 sang 13:00. Hãng hàng không thành thật xin lỗi và mong Quý khách thông cảm vì sự bất tiện này. Quý khách được hỗ trợ phục vụ bữa trưa tại sân bay và quyền đổi chuyến theo quy định.
```

### hos-flight-04 (Rules: `HOS004` · Doctype: `flight-notice`)

```diff
- Do sự cố khai thác, chuyến bay bị hoãn chuyến vô thời hạn.
+ Do điều kiện khai thác, chuyến bay tạm thời hoãn chuyến. Hãng hàng không thành thật xin lỗi và mong Quý khách thông cảm; nhân viên sân bay sẵn sàng hỗ trợ Quý khách chuyển chuyến hoặc hoàn vé ngay tại quầy thủ tục.
```

## Culinary

### hos-menu-01 (Rules: `HOS005` · Doctype: `fnb-menu`)

```diff
- Thực đơn Bếp trưởng: Súp nấm truffle, bò Wagyu áp chảo, bánh kem dâu tây.
+ Thực đơn Bếp trưởng: Súp nấm truffle, bò Wagyu áp chảo, bánh kem dâu tây. Lưu ý: Quý khách có tiền sử dị ứng thực phẩm vui lòng báo nhân viên phục vụ. Giá đã bao gồm 5% phí phục vụ và 8% thuế GTGT.
```

### hos-menu-02 (Rules: `HOS005` · Doctype: `fnb-menu`)

```diff
- Danh mục món khai vị: Hàu nướng phô mai, gỏi cá trích, salad rong biển. Đã bao gồm 10% thuế GTGT.
+ Danh mục món khai vị: Hàu nướng phô mai, gỏi cá trích, salad rong biển. Quý khách có tiền sử dị ứng hải sản xin thông báo trước. Giá món ăn đã bao gồm 5% phí phục vụ và 10% thuế GTGT.
```

### hos-menu-03 (Rules: `HOS005` · Doctype: `fnb-menu`)

```diff
- Thực đơn tráng miệng cao cấp: Bánh sô-cô-la tan chảy. Quý khách dị ứng đậu phộng xin lưu ý.
+ Thực đơn tráng miệng cao cấp: Bánh sô-cô-la tan chảy. Quý khách có tiền sử dị ứng thực phẩm xin vui lòng thông báo trước. Giá niêm yết đã bao gồm 5% phí phục vụ và 8% thuế GTGT.
```

## Etiquette

### hos-hostile-01 (Rules: `HOS006`)

```diff
- Cấm mang đồ ăn vào phòng ngủ dưới mọi hình thức.
+ Để đảm bảo an toàn vệ sinh và không gian trong lành, Quý khách vui lòng không sử dụng thức ăn mang từ ngoài vào phòng ngủ.
```

### hos-hostile-02 (Rules: `HOS006`)

```diff
- Khách tự chịu trách nhiệm nếu mất đồ tại khu vực bãi đỗ xe.
+ Để đảm bảo an toàn tài sản cá nhân, Quý khách vui lòng khóa xe cẩn thận và không để tư trang có giá trị trong xe.
```

### hos-hostile-03 (Rules: `HOS006`)

```diff
- Hút thuốc trong phòng phạt ngay 100% tiền cọc lưu trú.
+ Khách sạn áp dụng chính sách không hút thuốc trong phòng; Quý khách có nhu cầu vui lòng sử dụng khu vực ngoài trời được chỉ định riêng.
```

### hos-hostile-04 (Rules: `HOS006`)

```diff
- Tuyệt đối cấm tắm biển sau 18:00, cố tình vi phạm bắt buộc phải bồi thường nếu xảy ra sự cố.
+ Vì lý do an toàn khi thủy triều dâng, Quý khách vui lòng không tắm biển sau 18:00; đội ngũ cứu hộ chỉ túc trực trong khung giờ ban ngày.
```

## Terminology

### hos-calque-01 (Rules: `CAL001`)

```diff
- Quý khách vui lòng đến nhận buồng phòng tại quầy vào lúc 14:00.
+ Quý khách vui lòng làm thủ tục nhận phòng tại quầy lễ tân vào lúc 14:00.
```

### hos-calque-02 (Rules: `CAL001`)

```diff
- Trước khi rời đi, xin Quý khách hoàn tất thủ tục trả buồng phòng.
+ Trước khi rời đi, xin Quý khách hoàn tất thủ tục trả phòng tại quầy lễ tân.
```

### hos-calque-03 (Rules: `CAL001`)

```diff
- Hành khách vui lòng xuất trình thẻ lên máy bay tàu bay tại cửa khởi hành.
+ Hành khách vui lòng xuất trình thẻ lên tàu bay tại cửa khởi hành.
```

### hos-calque-04 (Rules: `CAL001`)

```diff
- Giá phòng đã bao gồm bữa sáng miễn trừ tại nhà hàng chính.
+ Giá phòng đã bao gồm bữa sáng miễn phí tại nhà hàng chính của khu nghỉ dưỡng.
```

### hos-calque-05 (Rules: `CAL001`)

```diff
- Đăng ký tham gia tour du lịch 0 đồng khám phá các danh lam thắng cảnh.
+ Đăng ký tham gia tour du lịch trọn gói tiết kiệm khám phá các danh lam thắng cảnh.
```

## Register

### hos-register-01 (Rules: `PRO002` · Register: `hospitality-luxury`)

```diff
- Bạn hãy liên hệ quầy lễ tân để nhận chìa khóa phòng nhé.
+ Quý khách vui lòng liên hệ quầy lễ tân để nhận thẻ từ phòng nghỉ.
```

### hos-register-02 (Rules: `PRO002` · Register: `hospitality-luxury`)

```diff
- Chúc cả nhà có một kỳ nghỉ thật vui vẻ bên bờ biển.
+ Kính chúc Quý khách có một kỳ nghỉ thật trọn vẹn và thư thái bên bờ biển.
```
