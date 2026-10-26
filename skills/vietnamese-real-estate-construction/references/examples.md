<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-real-estate-construction`

> Auto-generated from `evals/vietnamese-real-estate-construction/pairs.jsonl` (25 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Off Plan Deposit

### rea-deposit-cap-01 (Rules: `REA001`)

```diff
- Khách hàng ký thỏa thuận đặt cọc 15% giá bán căn hộ hình thành trong tương lai ngay khi đăng ký nguyện vọng.
+ Khách hàng ký thỏa thuận đặt cọc 5% giá bán căn hộ hình thành trong tương lai khi dự án đã đủ điều kiện mở bán theo luật định.
```

### rea-deposit-cap-02 (Rules: `REA001`)

```diff
- Bên mua nộp tiền đặt cọc 10% tổng giá trị căn hộ khi ký thỏa thuận đặt cọc giữ chỗ.
+ Bên mua nộp tiền đặt cọc 5% tổng giá trị căn hộ khi ký thỏa thuận đặt cọc theo quy định của Luật Kinh doanh bất động sản 2023.
```

### rea-deposit-cap-03 (Rules: `REA001`)

```diff
- Chủ đầu tư thu tiền cọc 20% giá bán nhà ở hình thành trong tương lai tại thời điểm ký kết.
+ Chủ đầu tư thu tiền đặt cọc 5% giá bán nhà ở hình thành trong tương lai tại thời điểm ký hợp đồng đặt cọc.
```

## Capital Mobilization

### rea-capital-mobilization-01 (Rules: `REA001`)

```diff
- Chủ đầu tư thực hiện thỏa thuận giữ chỗ khi chưa có văn bản đủ điều kiện bán nhà ở hình thành trong tương lai của Sở Xây dựng.
+ Chủ đầu tư ký hợp đồng mua bán sau khi đã có văn bản thông báo đủ điều kiện bán nhà ở hình thành trong tương lai của Sở Xây dựng.
```

## Payment Schedule

### rea-installment-first-01 (Rules: `REA002`)

```diff
- Thanh toán đợt 1 là 40% giá trị hợp đồng ngay khi ký hợp đồng mua bán nhà ở.
+ Thanh toán đợt 1 là 30% giá trị hợp đồng (đã bao gồm tiền đặt cọc) ngay khi ký hợp đồng mua bán nhà ở.
```

### rea-installment-first-02 (Rules: `REA002`)

```diff
- Bên mua thanh toán đợt đầu 50% giá trị hợp đồng trong vòng 10 ngày kể từ ngày ký.
+ Bên mua thanh toán đợt đầu 30% giá trị hợp đồng theo quy định của Luật Kinh doanh bất động sản 2023.
```

### rea-pre-handover-cap-01 (Rules: `REA002`)

```diff
- Bên mua phải hoàn tất thanh toán 80% trước khi bàn giao nhà từ chủ đầu tư.
+ Bên mua hoàn tất thanh toán 70% giá trị hợp đồng trước khi bàn giao nhà theo quy định pháp luật.
```

### rea-pre-cert-cap-01 (Rules: `REA002`)

```diff
- Chủ đầu tư thu 100% giá trị hợp đồng trước khi bàn giao sổ hồng cho khách hàng.
+ Chủ đầu tư thu 95% giá trị hợp đồng trước khi bàn giao sổ hồng; 5% còn lại thanh toán khi nhận Giấy chứng nhận.
```

## Land Tenure

### rea-tenure-condotel-01 (Rules: `REA003`)

```diff
- Dự án căn hộ condotel ven biển sở hữu sổ đỏ lâu dài và cam kết lợi nhuận trọn đời.
+ Dự án căn hộ du lịch ven biển có thời hạn sở hữu theo thời hạn giao đất của dự án là 50 năm.
```

### rea-tenure-officetel-01 (Rules: `REA003`)

```diff
- Toàn bộ các căn hộ officetel tại tòa tháp được cấp sổ hồng vĩnh viễn cho cư dân.
+ Các căn hộ văn phòng lưu trú tại tòa tháp có thời hạn sở hữu 50 năm theo quy hoạch đất thương mại dịch vụ.
```

### rea-tenure-shophouse-01 (Rules: `REA003`)

```diff
- Khu shophouse thương mại dịch vụ sở hữu lâu dài vĩnh viễn với tiềm năng kinh doanh vượt trội.
+ Khu shophouse thương mại dịch vụ có thời hạn sử dụng đất 50 năm theo quy định của Luật Đất đai 2024.
```

### rea-tenure-villa-01 (Rules: `REA003`)

```diff
- Biệt thự nghỉ dưỡng trên đất thương mại dịch vụ cam kết cấp sổ hồng vĩnh viễn cho từng chủ nhân.
+ Biệt thự nghỉ dưỡng trên đất thương mại dịch vụ được cấp Giấy chứng nhận với thời hạn sử dụng 50 năm.
```

## Apartment Area

### rea-area-ambiguous-01 (Rules: `REA004`)

```diff
- Mỗi diện tích căn hộ tiêu chuẩn tại dự án là 85 m² với tầm nhìn hướng công viên.
+ Mỗi căn hộ tiêu chuẩn có diện tích thông thủy là 78 m² và diện tích tim tường là 85 m².
```

### rea-area-ambiguous-02 (Rules: `REA004`)

```diff
- Căn hộ hai phòng ngủ có diện tích phủ bì là 90 m² gồm hai ban công thoáng mát.
+ Căn hộ hai phòng ngủ có diện tích thông thủy là 82 m² và diện tích tim tường là 90 m².
```

### rea-area-ambiguous-03 (Rules: `REA004`)

```diff
- Thiết kế diện tích căn hộ từ 65 m² đến 105 m² phù hợp cho gia đình trẻ.
+ Thiết kế diện tích thông thủy từ 60 m² đến 98 m² (diện tích tim tường từ 65 m² đến 105 m²).
```

### rea-area-ambiguous-04 (Rules: `REA004`)

```diff
- Bản vẽ thiết kế quy định diện tích phủ bì của căn góc ba phòng ngủ là 120 m².
+ Bản vẽ thiết kế quy định diện tích thông thủy của căn góc ba phòng ngủ là 110 m² và diện tích tim tường là 120 m².
```

## Maintenance Fund

### rea-maintenance-fund-01 (Rules: `REA005`)

```diff
- Người mua nhà chung cư có nghĩa vụ đóng phí bảo trì 5% giá trị hợp đồng trước thuế.
+ Người mua nhà chung cư có nghĩa vụ đóng kinh phí bảo trì 2% giá trị căn hộ trước thuế.
```

### rea-maintenance-fund-02 (Rules: `REA005`)

```diff
- Khách hàng nộp kinh phí bảo trì 2% ngay khi ký thỏa thuận đặt cọc căn hộ.
+ Khách hàng nộp kinh phí bảo trì 2% khi nhận bàn giao căn hộ theo thông báo của chủ đầu tư.
```

### rea-maintenance-fund-03 (Rules: `REA005`)

```diff
- Bên mua có trách nhiệm thanh toán kinh phí bảo trì 3% vào tài khoản phong tỏa của ban quản trị.
+ Bên mua có trách nhiệm thanh toán kinh phí bảo trì 2% vào tài khoản kinh phí bảo trì theo luật định.
```

### rea-maintenance-fund-04 (Rules: `REA005` · Doctype: `off-plan-contract`)

```diff
- Hợp đồng mua bán căn hộ hình thành trong tương lai quy định giá bán và tiến độ bàn giao nhà ở.
+ Hợp đồng mua bán căn hộ hình thành trong tương lai quy định giá bán, tiến độ bàn giao và kinh phí bảo trì 2%.
```

## Calque

### rea-calque-greenery-01 (Rules: `REA006`)

```diff
- Dự án sở hữu vùng xanh lá cây rộng lớn cùng danh mục tài sản thực đa dạng.
+ Dự án sở hữu công viên cây xanh rộng lớn cùng danh mục bất động sản đa dạng.
```

### rea-calque-boq-01 (Rules: `REA006`)

```diff
- Nhà thầu xây dựng có trách nhiệm nộp danh sách số lượng kèm đơn giá dự thầu.
+ Nhà thầu xây dựng có trách nhiệm nộp bảng tiên lượng mời thầu (BOQ) kèm đơn giá dự thầu.
```

### rea-calque-handover-01 (Rules: `REA006`)

```diff
- Dự án mở bán các căn hộ trên kế hoạch với tiêu chuẩn bàn giao thô ráp tại tòa tháp.
+ Dự án mở bán nhà ở hình thành trong tương lai với tiêu chuẩn bàn giao thô tại tòa tháp.
```

## Superlative

### rea-superlative-01 (Rules: `LAW001`)

```diff
- Khu đô thị sinh thái số 1 Việt Nam với không gian sống hoàn hảo nhất Đông Nam Á.
+ Khu đô thị sinh thái tiêu chuẩn quốc tế với không gian sống tiện nghi ven sông.
```

## Typography Unit

### rea-unit-exponent-01 (Rules: `NUM004`)

```diff
- Căn hộ penthouse có diện tích thông thủy 185 m2 và ban công rộng 25 m2 hướng hồ.
+ Căn hộ penthouse có diện tích thông thủy 185 m² và ban công rộng 25 m² hướng hồ.
```
