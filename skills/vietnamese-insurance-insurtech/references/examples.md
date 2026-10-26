<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-insurance-insurtech`

> Auto-generated from `evals/vietnamese-insurance-insurtech/pairs.jsonl` (25 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Investment Linked

### ins-savings-disguise-01 (Rules: `INS001`)

```diff
- Gói bảo hiểm liên kết đầu tư cam kết lợi nhuận cố định 100% không rủi ro cho toàn bộ vốn ủy thác của khách hàng.
+ Sản phẩm bảo hiểm liên kết đầu tư mang lại cơ hội gia tăng tài sản gắn liền với kết quả hoạt động của các quỹ liên kết đơn vị.
```

### ins-savings-disguise-02 (Rules: `INS001`)

```diff
- Tư vấn viên giới thiệu đây là sản phẩm tiết kiệm ngân hàng lãi suất cam kết 12%/năm kết hợp bảo vệ y tế trọn đời.
+ Tư vấn viên giải thích rõ đây là hợp đồng bảo hiểm nhân thọ kết hợp đầu tư, phân định rõ phí bảo vệ và phần vốn đầu tư theo quy định.
```

### ins-savings-disguise-03 (Rules: `INS001`)

```diff
- Gửi tiết kiệm đầu tư cam kết lợi nhuận cố định và rút vốn linh hoạt tại quầy giao dịch ngân hàng bất kỳ lúc nào.
+ Khách hàng tham gia sản phẩm bảo hiểm liên kết chung được hưởng quyền lợi bảo vệ và tích lũy giá trị tài khoản theo lãi suất công bố thực tế.
```

## Free Look

### ins-free-look-shortened-01 (Rules: `INS002`)

```diff
- Hợp đồng bảo hiểm nhân thọ quy định thời gian cân nhắc là 7 ngày kể từ thời điểm bàn giao bộ hợp đồng gốc.
+ Hợp đồng bảo hiểm nhân thọ quy định thời gian cân nhắc tham gia bảo hiểm là 21 ngày kể từ ngày nhận được hợp đồng bảo hiểm.
```

### ins-free-look-shortened-02 (Rules: `INS002`)

```diff
- Bên mua bảo hiểm có thời gian cân nhắc 14 ngày để xem xét điều khoản và quyết định tiếp tục duy trì hợp đồng.
+ Bên mua bảo hiểm có thời gian cân nhắc tham gia bảo hiểm 21 ngày để nghiên cứu quy tắc và yêu cầu hủy hợp đồng nhận lại phí nếu có nguyện vọng.
```

### ins-free-look-waived-03 (Rules: `INS002`)

```diff
- Khách hàng không được hủy hợp đồng sau khi ký và toàn bộ phí bảo hiểm đã nộp sẽ không được hoàn lại dưới mọi hình thức.
+ Trong thời gian cân nhắc 21 ngày kể từ ngày nhận hợp đồng, bên mua bảo hiểm có quyền từ chối tiếp tục tham gia và nhận lại toàn bộ phí bảo hiểm đã đóng.
```

## Policy Illustration

### ins-illustration-missing-freelook (Rules: `INS002` · Doctype: `policy-illustration`)

```diff
- Tài liệu minh họa bán hàng sản phẩm bảo hiểm nhân thọ trọn đời.
- 
- Quyền lợi tử vong: Chi trả 100% số tiền bảo hiểm gia tăng.
- 
- Phí bảo hiểm định kỳ: 25.000.000 ₫ đóng hàng năm trong thời hạn 15 năm.
- 
- Bảng minh họa giá trị hoàn lại tích lũy qua các năm hợp đồng.
+ Tài liệu minh họa bán hàng sản phẩm bảo hiểm nhân thọ trọn đời.
+ 
+ Quyền lợi tử vong: Chi trả 100% số tiền bảo hiểm gia tăng.
+ 
+ Phí bảo hiểm định kỳ: 25.000.000 ₫ đóng hàng năm trong thời hạn 15 năm.
+ 
+ Thời gian cân nhắc tham gia bảo hiểm là 21 ngày kể từ ngày nhận hợp đồng bảo hiểm.
+ 
+ Bảng minh họa giá trị hoàn lại tích lũy qua các năm hợp đồng.
```

## Exclusion Disclosure

### ins-exclusion-waived-01 (Rules: `INS003`)

```diff
- Đại lý tư vấn cho khách hàng không cần đọc điều khoản loại trừ vì hợp đồng đã được thiết kế bảo vệ toàn diện.
+ Đại lý có nghĩa vụ giải thích rõ ràng và đầy đủ các điều khoản loại trừ trách nhiệm bảo hiểm cho bên mua bảo hiểm trước khi ký kết.
```

### ins-exclusion-unconditional-02 (Rules: `INS003`)

```diff
- Gói bảo hiểm chi trả mọi rủi ro không có bất kỳ điều khoản loại trừ nào nhằm mang lại sự an tâm tuyệt đối.
+ Gói bảo hiểm chi trả quyền lợi theo danh mục bệnh lý quy định, các trường hợp loại trừ trách nhiệm bảo hiểm được nêu chi tiết tại Quy tắc bảo hiểm.
```

### ins-exclusion-100pct-03 (Rules: `INS003`)

```diff
- Doanh nghiệp bảo hiểm cam kết chi trả 100% không loại trừ bất kỳ trường hợp nào đối với tai nạn cá nhân.
+ Doanh nghiệp bảo hiểm giải quyết bồi thường tai nạn cá nhân theo hạn mức và các điểm loại trừ quy định trong hợp đồng.
```

## Insurance Certificate

### ins-certificate-missing-exclusion (Rules: `INS003` · Doctype: `insurance-certificate`)

```diff
- Giấy chứng nhận bảo hiểm sức khỏe cá nhân.
- 
- Bên mua bảo hiểm: Ông Nguyễn Văn A.
- 
- Người được bảo hiểm: Ông Nguyễn Văn A.
- 
- Số tiền bảo hiểm: 200.000.000 ₫.
- 
- Thời hạn bảo hiểm: Từ 00:00 ngày 01/01/2026 đến 23:59 ngày 31/12/2026.
+ Giấy chứng nhận bảo hiểm sức khỏe cá nhân.
+ 
+ Bên mua bảo hiểm: Ông Nguyễn Văn A.
+ 
+ Người được bảo hiểm: Ông Nguyễn Văn A.
+ 
+ Số tiền bảo hiểm: 200.000.000 ₫.
+ 
+ Thời hạn bảo hiểm: Từ 00:00 ngày 01/01/2026 đến 23:59 ngày 31/12/2026.
+ 
+ Điều khoản loại trừ trách nhiệm bảo hiểm: Không chi trả cho các tình trạng y tế có trước và hành vi cố ý vi phạm pháp luật.
```

## Translationese

### ins-calque-policy-01 (Rules: `INS004`)

```diff
- Quý khách vui lòng kiểm tra kỹ nội dung chính sách bảo hiểm trước khi thực hiện thanh toán phí đầu tiên.
+ Quý khách vui lòng kiểm tra kỹ nội dung hợp đồng bảo hiểm trước khi thực hiện thanh toán phí đầu tiên.
```

### ins-calque-policyholder-02 (Rules: `INS004`)

```diff
- Thông tin cá nhân của người giữ chính sách phải trùng khớp với dữ liệu trên thẻ căn cước hợp lệ.
+ Thông tin cá nhân của bên mua bảo hiểm phải trùng khớp với dữ liệu trên thẻ căn cước hợp lệ.
```

### ins-calque-coverage-03 (Rules: `INS004`)

```diff
- Bản tóm tắt nêu rõ câu chuyện bảo hiểm và các mốc quyền lợi chi trả khi xảy ra sự kiện y tế.
+ Bản tóm tắt nêu rõ phạm vi bảo hiểm và các mốc quyền lợi chi trả khi xảy ra sự kiện y tế.
```

### ins-calque-premium-04 (Rules: `INS004`)

```diff
- Mức tiền thưởng bảo hiểm hàng năm được tính toán căn cứ trên độ tuổi và tình trạng sức khỏe của người được bảo hiểm.
+ Mức phí bảo hiểm định kỳ hàng năm được tính toán căn cứ trên độ tuổi và tình trạng sức khỏe của người được bảo hiểm.
```

### ins-calque-act-of-god-05 (Rules: `INS004`)

```diff
- Công ty bảo hiểm được miễn trừ nghĩa vụ bồi thường thiệt hại phát sinh do sự kiện thiên Chúa như bão lũ động đất.
+ Công ty bảo hiểm giải quyết quyền lợi theo thỏa thuận hợp đồng đối với tổn thất do thiên tai và sự kiện bất khả kháng.
```

### ins-calque-life-policy-06 (Rules: `INS004`)

```diff
- Khách hàng ký kết chính sách bảo hiểm nhân thọ thời hạn 20 năm tại đại lý ủy quyền của tổng công ty.
+ Khách hàng giao kết hợp đồng bảo hiểm nhân thọ thời hạn 20 năm tại đại lý ủy quyền của tổng công ty.
```

## Claim Timeline

### ins-timeline-excessive-90d (Rules: `INS005`)

```diff
- Quy trình xử lý hồ sơ: Thời hạn giải quyết bồi thường là 90 ngày làm việc kể từ khi nhận đủ hồ sơ hợp lệ.
+ Quy trình xử lý hồ sơ: Thời hạn giải quyết bồi thường là 15 ngày kể từ khi nhận đủ hồ sơ hợp lệ theo quy định pháp luật.
```

### ins-timeline-excessive-60d (Rules: `INS005`)

```diff
- Công ty cam kết chi trả quyền lợi bảo hiểm trong vòng 60 ngày sau khi nhận đủ hồ sơ yêu cầu bồi thường.
+ Công ty cam kết chi trả quyền lợi bảo hiểm trong vòng 15 ngày sau khi nhận đủ hồ sơ yêu cầu bồi thường hợp lệ.
```

## Bancassurance

### ins-bancassurance-coercion-01 (Rules: `INS006`)

```diff
- Ngân hàng quy định khách hàng bắt buộc mua bảo hiểm nhân thọ mới được giải ngân khoản vay sản xuất kinh doanh.
+ Ngân hàng thực hiện thẩm định và giải ngân khoản vay căn cứ vào năng lực tài chính và phương án kinh doanh khả thi của khách hàng.
```

### ins-bancassurance-coercion-02 (Rules: `INS006`)

```diff
- Cán bộ tín dụng thông báo sẽ từ chối phê duyệt hồ sơ vay vốn nếu khách hàng không tham gia gói bảo hiểm liên kết đầu tư.
+ Cán bộ tín dụng tư vấn các gói bảo hiểm tự nguyện độc lập và tôn trọng quyền tự do lựa chọn của khách hàng vay vốn.
```

### ins-bancassurance-coercion-03 (Rules: `INS006`)

```diff
- Thông báo duyệt vay: Điều kiện bắt buộc để giải ngân là phải mua bảo hiểm nhân thọ trị giá 30 triệu đồng.
+ Thông báo duyệt vay: Khoản tín dụng được giải ngân khi khách hàng hoàn tất thủ tục công chứng hợp đồng thế chấp tài sản theo quy định.
```

## Superlative

### ins-superlative-best-ins (Rules: `LAW001`)

```diff
- Công ty tự hào cung cấp sản phẩm bảo hiểm sức khỏe tốt nhất thị trường với hạn mức quyền lợi vượt trội.
+ Công ty cung cấp sản phẩm bảo hiểm sức khỏe toàn diện với nhiều gói quyền lợi nội trú và ngoại trú linh hoạt.
```

## Typography

### ins-currency-comma-format (Rules: `NUM001`)

```diff
- Phí bảo hiểm định kỳ hàng năm là 15,000,000 ₫ được đóng vào đầu mỗi năm hợp đồng.
+ Phí bảo hiểm định kỳ hàng năm là 15.000.000 ₫ được đóng vào đầu mỗi năm hợp đồng.
```

## Register

### ins-register-pronoun-mixed (Rules: `PRO001`)

```diff
- Kính gửi Quý khách thông báo đóng phí định kỳ. Bạn hãy hoàn tất chuyển khoản trước ngày đến hạn.
+ Kính gửi Quý khách thông báo đóng phí định kỳ. Quý khách vui lòng hoàn tất chuyển khoản trước ngày đến hạn.
```
