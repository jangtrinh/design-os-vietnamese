<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-finance-copy`

> Auto-generated from `evals/vietnamese-finance-copy/pairs.jsonl` (30 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Solicitation

### fin-guaranteed-01 (Rules: `FIN001`)

```diff
- Cam kết lợi nhuận 18%/năm cho mọi nhà đầu tư.
+ Lợi nhuận kỳ vọng 18%/năm. Đầu tư luôn tiềm ẩn rủi ro thị trường; kết quả trong quá khứ không mang tính bảo đảm cho tương lai.
```

### fin-guaranteed-02 (Rules: `FIN001`)

```diff
- Kênh đầu tư an toàn tuyệt đối, đảm bảo sinh lời mỗi tháng.
+ Sản phẩm quản lý tài sản phù hợp với nhà đầu tư có khẩu vị rủi ro trung bình, hướng tới mục tiêu tăng trưởng vốn dài hạn.
```

### fin-guaranteed-03 (Rules: `FIN001`)

```diff
- Gói gửi vốn bảo toàn vốn 100%, chắc chắn có lãi.
+ Sản phẩm đầu tư thận trọng với tỷ lệ phân bổ tài sản an toàn, hướng đến mục tiêu duy trì giá trị vốn danh nghĩa.
```

### fin-guaranteed-04 (Rules: `FIN001`)

```diff
- Cơ hội đầu tư không rủi ro, sinh lời chắc chắn trong năm 2026.
+ Kế hoạch đầu tư có chiến lược phân bổ tài sản linh hoạt nhằm kiểm soát rủi ro biến động thị trường trong năm 2026.
```

## Lending

### fin-zero-rate-01 (Rules: `FIN002` · Doctype: `financial-promotion`)

```diff
- Chương trình mua trước trả góp lãi suất 0% cho mọi khách hàng.
+ Chương trình mua trước trả góp lãi suất 0% — phí chuyển đổi 3%/khoản vay. Tổng chi phí phải trả: 10.300.000 ₫.
```

### fin-zero-rate-02 (Rules: `FIN002` · Doctype: `loan`)

```diff
- Vay tiêu dùng ưu đãi 0% lãi suất trong 12 tháng đầu tiên.
+ Vay tiêu dùng ưu đãi lãi suất 0% trong 12 tháng đầu — phí chuyển đổi 2,5%. Tổng số tiền phải trả: 51.250.000 ₫.
```

## Statement

### fin-statement-unit-01 (Rules: `FIN005` · Doctype: `statement`)

```diff
- | Mã số | Chỉ tiêu | Số tiền |
- |---|---|---|
- | 100 | Tài sản ngắn hạn | 150.000 |
+ Đơn vị tính: triệu đồng
+ 
+ | Mã số | Chỉ tiêu | Số tiền |
+ |---|---|---|
+ | 100 | Tài sản ngắn hạn | 150.000 |
```

### fin-statement-negative-01 (Rules: `FIN006` · Doctype: `statement`)

```diff
- Lợi nhuận sau thuế chưa phân phối kỳ này: -120.000.000 ₫
+ Lợi nhuận sau thuế chưa phân phối kỳ này: (120.000.000) ₫
```

### fin-statement-negative-02 (Rules: `FIN006` · Doctype: `statement`)

```diff
- Dự phòng phải thu khó đòi năm 2026: -45.000.000 ₫
+ Dự phòng phải thu khó đòi năm 2026: (45.000.000) ₫
```

## E Invoice

### fin-invoice-mst-01 (Rules: `FIN007` · Doctype: `e-invoice`)

```diff
- Hóa đơn bán hàng. Thuế suất thuế GTGT: 10%. Tiền thuế GTGT: 50.000 ₫. Tổng cộng tiền thanh toán: 550.000 ₫.
+ Hóa đơn bán hàng. Mã số thuế (MST): 0109876543. Thuế suất thuế GTGT: 10%. Tiền thuế GTGT: 50.000 ₫. Tổng cộng tiền thanh toán: 550.000 ₫.
```

### fin-invoice-vat-01 (Rules: `FIN007` · Doctype: `e-invoice`)

```diff
- Hóa đơn bán hàng của Công ty Cổ phần Alpha. Mã số thuế (MST): 0109988776. Tổng tiền thanh toán: 10.000.000 ₫.
+ Hóa đơn bán hàng của Công ty Cổ phần Alpha. Mã số thuế (MST): 0109988776. Thuế GTGT: 1.000.000 ₫. Tổng tiền thanh toán: 11.000.000 ₫.
```

## Insurance

### fin-insurance-ilp-01 (Rules: `FIN008` · Doctype: `insurance`)

```diff
- Sản phẩm bảo hiểm liên kết đầu tư mang lại lợi ích bảo vệ tài chính vượt trội cho cả gia đình.
+ Sản phẩm bảo hiểm liên kết đầu tư mang lại giải pháp bảo vệ tài chính. Đây là sản phẩm bảo hiểm, không phải là tiền gửi ngân hàng; bên mua bảo hiểm chịu mọi rủi ro đầu tư.
```

### fin-insurance-ilp-02 (Rules: `FIN008` · Doctype: `financial-promotion`)

```diff
- Gia nhập hợp đồng ILP hôm nay để gia tăng tài sản dài hạn.
+ Tham gia hợp đồng ILP nhằm bảo vệ tài chính trước rủi ro. Sản phẩm không phải là tiền gửi tiết kiệm; bên mua bảo hiểm chịu mọi rủi ro từ kết quả đầu tư.
```

### fin-insurance-ul-01 (Rules: `FIN008` · Doctype: `insurance`)

```diff
- Bảo hiểm liên kết chung kết hợp đầu tư tích lũy an toàn và bảo vệ toàn diện.
+ Bảo hiểm liên kết chung kết hợp bảo vệ sinh kỳ và tử kỳ. Đây là sản phẩm bảo hiểm, không phải tiền gửi ngân hàng; khách hàng chịu rủi ro theo kết quả đầu tư thực tế.
```

## Fintech

### fin-transfer-biometric-01 (Rules: `FIN009` · Doctype: `fintech-transfer`)

```diff
- Xác nhận giao dịch chuyển tiền trên 10 triệu đồng tới tài khoản người thụ hưởng.
+ Xác nhận giao dịch chuyển tiền trên 10 triệu đồng — vui lòng xác thực sinh trắc học khuôn mặt theo quy định để tiếp tục.
```

### fin-transfer-biometric-02 (Rules: `FIN009` · Doctype: `fintech-transfer`)

```diff
- Hạn mức chuyển khoản ngày trên 20 triệu đồng áp dụng cho khách hàng cá nhân.
+ Hạn mức chuyển khoản ngày trên 20 triệu đồng yêu cầu xác thực bằng khuôn mặt khớp với dữ liệu CCCD gắn chip.
```

## Terminology

### fin-calque-balance-sheet (Rules: `CAL001`)

```diff
- Công ty vừa công bố Bảng cân đối kế toán quý IV năm 2026.
+ Công ty vừa công bố Báo cáo tình hình tài chính quý IV năm 2026.
```

### fin-calque-equity (Rules: `CAL001`)

```diff
- Tăng cường nguồn sự công bằng của các cổ đông hiện hữu.
+ Tăng cường nguồn vốn chủ sở hữu của các cổ đông hiện hữu.
```

### fin-calque-principal (Rules: `CAL001`)

```diff
- Khoản thanh toán hàng tháng bao gồm hiệu trưởng và lãi vay.
+ Khoản thanh toán hàng tháng bao gồm tiền gốc và lãi vay.
```

### fin-calque-security (Rules: `CAL001`)

```diff
- Thị trường sự an toàn Việt Nam ghi nhận thanh khoản kỷ lục.
+ Thị trường chứng khoán Việt Nam ghi nhận thanh khoản kỷ lục.
```

### fin-calque-cash-flow (Rules: `CAL001`)

```diff
- Doanh nghiệp cần tối ưu hóa dòng chảy tiền mặt hàng tháng.
+ Doanh nghiệp cần tối ưu hóa lưu chuyển tiền tệ hàng tháng.
```

### fin-calque-accounts-receivable (Rules: `CAL001`)

```diff
- Kiểm toán lại tài khoản phải thu của các đối tác lớn.
+ Kiểm toán lại các khoản phải thu khách hàng của các đối tác lớn.
```

## Compliance

### fin-superlative-highest (Rules: `LAW001`)

```diff
- Ngân hàng mang đến gói tiền gửi lãi suất cao nhất thị trường.
+ Ngân hàng mang đến gói tiền gửi lãi suất từ 6,5%/năm áp dụng cho kỳ hạn 12 tháng.
```

### fin-superlative-number-one (Rules: `LAW001`)

```diff
- Chúng tôi là ứng dụng đầu tư tài chính số 1 tại Việt Nam.
+ Ứng dụng đầu tư tài chính được cấp phép chính thức bởi Ủy ban Chứng khoán Nhà nước.
```

## Formatting

### fin-number-comma (Rules: `NUM001`)

```diff
- Doanh thu thuần năm 2026 đạt 5,200,000,000 VND.
+ Doanh thu thuần năm 2026 đạt 5.200.000.000 ₫.
```

### fin-number-ungrouped (Rules: `NUM002`)

```diff
- Số dư khả dụng hiện tại trong tài khoản là 15000000 ₫.
+ Số dư khả dụng hiện tại trong tài khoản là 15.000.000 ₫.
```

### fin-number-dot-decimal (Rules: `NUM003`)

```diff
- Lãi suất tiết kiệm kỳ hạn 12 tháng được áp dụng ở mức 6.5%/năm.
+ Lãi suất tiết kiệm kỳ hạn 12 tháng được áp dụng ở mức 6,5%/năm.
```

## Pragmatics

### fin-register-mixed (Rules: `PRO001`)

```diff
- Kính gửi Quý khách bảng sao kê tài khoản tháng này, bạn hãy kiểm tra lại giao dịch.
+ Kính gửi Quý khách bảng sao kê tài khoản tháng này, xin quý khách vui lòng kiểm tra lại giao dịch.
```

### fin-register-pronoun (Rules: `PRO002` · Register: `finance-formal`)

```diff
- Bạn vui lòng đối chiếu lại các giao dịch phát sinh trên sao kê thẻ tín dụng.
+ Quý khách vui lòng đối chiếu lại các giao dịch phát sinh trên sao kê thẻ tín dụng.
```

## Encoding

### fin-nfc-decomposed (Rules: `NFC001`)

```diff
- Kỳ hạn thanh toán tiền gửi tiết kiệm của quý khách đã đến.
+ Kỳ hạn thanh toán tiền gửi tiết kiệm của quý khách đã đến.
```
