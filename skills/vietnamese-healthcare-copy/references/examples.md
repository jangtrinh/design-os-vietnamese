<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-healthcare-copy`

> Auto-generated from `evals/vietnamese-healthcare-copy/pairs.jsonl` (35 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Tpcn Compliance

### med-disclaimer-01 (Rules: `MED001` · Register: `healthcare` · Doctype: `tpcn-ad`)

```diff
- Thực phẩm bảo vệ sức khỏe Bio-Immune giúp Quý khách tăng cường sức đề kháng và giảm nguy cơ viêm đường hô hấp.
+ Thực phẩm bảo vệ sức khỏe Bio-Immune giúp Quý khách tăng cường sức đề kháng và giảm nguy cơ viêm đường hô hấp. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.
```

### med-disclaimer-02 (Rules: `MED001` · Register: `healthcare` · Doctype: `tpcn-ad`)

```diff
- Viên uống bổ gan Hepa-Life hỗ trợ thanh nhiệt giải độc gan cho Quý khách. Sản phẩm được chiết xuất từ thảo dược tự nhiên.
+ Viên uống bổ gan Hepa-Life hỗ trợ thanh nhiệt giải độc gan cho Quý khách. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.
```

## Therapeutic Claims

### med-curative-01 (Rules: `MED002`)

```diff
- Sản phẩm thảo dược cam kết chữa khỏi hoàn toàn 100% bệnh viêm xoang mãn tính.
+ Sản phẩm thảo dược hỗ trợ làm giảm triệu chứng nghẹt mũi và hỗ trợ thông mũi xoang.
```

### med-curative-02 (Rules: `MED002`)

```diff
- Phương pháp mới điều trị dứt điểm vĩnh viễn đái tháo đường không cần tiêm insulin.
+ Phương pháp hỗ trợ kiểm soát đường huyết và dự phòng biến chứng đái tháo đường.
```

### med-curative-03 (Rules: `MED002`)

```diff
- Cao thảo mộc gia truyền được ví như thần dược trị bách bệnh cho mọi lứa tuổi.
+ Sản phẩm cao thảo mộc hỗ trợ bồi bổ sức khỏe và tăng cường thể trạng cho người cao tuổi.
```

### med-curative-04 (Rules: `MED002`)

```diff
- Chúng tôi cam kết khỏi bệnh 100% đối với các trường hợp thoái hóa khớp gối.
+ Phác đồ điều trị hỗ trợ phục hồi vận động khớp gối và kiểm soát cơn đau thoái hóa.
```

### med-curative-05 (Rules: `MED002`)

```diff
- Viên uống thảo dược thay thế hoàn toàn thuốc đặc trị trong quá trình hạ men gan.
+ Viên uống thảo dược hỗ trợ bảo vệ tế bào gan bên cạnh phác đồ điều trị của bác sĩ.
```

## Licensing

### med-license-01 (Rules: `MED003`)

```diff
- Bác sĩ phụ trách phòng khám đã được cấp Chứng chỉ hành nghề y từ năm 2018.
+ Bác sĩ phụ trách phòng khám đã được cấp Giấy phép hành nghề khám bệnh, chữa bệnh theo quy định.
```

### med-license-02 (Rules: `MED003`)

```diff
- Toàn bộ đội ngũ bác sĩ đều có Chứng chỉ hành nghề khám bệnh, chữa bệnh do Bộ Y tế cấp.
+ Toàn bộ đội ngũ bác sĩ đều có Giấy phép hành nghề khám bệnh, chữa bệnh do Bộ Y tế cấp.
```

## Prescription

### med-prescription-vague-01 (Rules: `MED004` · Doctype: `prescription`)

```diff
- Paracetamol 500 mg, số lượng 10 viên. Hướng dẫn: uống khi cần. Tái khám ngay nếu xuất hiện sốt cao.
+ Paracetamol 500 mg, số lượng 10 viên. Hướng dẫn: uống 1 viên/lần, cách nhau tối thiểu 06 giờ khi sốt, uống sau ăn. Tái khám ngay nếu xuất hiện sốt cao.
```

### med-prescription-vague-02 (Rules: `MED004` · Doctype: `prescription`)

```diff
- Siro ho bổ phế, số lượng 1 chai. Ngày uống vài lần mỗi khi thấy ngứa cổ. Liên hệ bác sĩ nếu ho dai dẳng.
+ Siro ho bổ phế, số lượng 1 chai. Uống 10 ml/lần, ngày 3 lần sau ăn sáng, trưa, tối. Liên hệ bác sĩ nếu ho dai dẳng.
```

### med-prescription-units-01 (Rules: `MED004` · Doctype: `prescription`)

```diff
- Kháng sinh Amoxicillin 500, số lượng 20. Dùng 2 trong ngày. Tái khám ngay nếu xuất hiện phát ban.
+ Kháng sinh Amoxicillin 500 mg, số lượng 20 viên. Uống 1 viên/lần, 2 lần/ngày sau ăn sáng và tối. Tái khám ngay nếu xuất hiện phát ban.
```

### med-prescription-warning-01 (Rules: `MED004` · Doctype: `prescription`)

```diff
- Thuốc hạ huyết áp Amlodipin 5 mg, số lượng 30 viên. Uống 1 viên/lần, 1 lần/ngày vào buổi sáng sau ăn.
+ Thuốc hạ huyết áp Amlodipin 5 mg, số lượng 30 viên. Uống 1 viên/lần, 1 lần/ngày vào buổi sáng sau ăn. Tái khám ngay nếu xuất hiện hoa mắt chóng mặt hoặc hạ huyết áp quá mức.
```

## Advertising Compliance

### med-testimonial-01 (Rules: `MED005` · Register: `healthcare` · Doctype: `tpcn-ad`)

```diff
- Sản phẩm hỗ trợ tiêu hóa nhận được nhiều thư cảm ơn của bệnh nhân sau 2 tuần sử dụng. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.
+ Sản phẩm hỗ trợ tiêu hóa được Quý khách tin tưởng sử dụng để hỗ trợ duy trì hệ vi sinh đường ruột. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.
```

### med-testimonial-02 (Rules: `MED005` · Register: `healthcare` · Doctype: `tpcn-ad`)

```diff
- Bác sĩ khuyên dùng thực phẩm chức năng này để chữa bệnh viêm họng hạt. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.
+ Quý khách nên tham khảo ý kiến của bác sĩ chuyên khoa để được chẩn đoán và điều trị viêm họng hạt. Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh.
```

## Patient Communication

### med-stigma-01 (Rules: `MED006`)

```diff
- Ghi nhận người bệnh không chịu hợp tác trong việc thực hiện chế độ ăn kiêng đái tháo đường.
+ Ghi nhận người bệnh chưa phối hợp tuân thủ điều trị trong việc thực hiện chế độ ăn kiêng đái tháo đường.
```

### med-stigma-02 (Rules: `MED006`)

```diff
- Trường hợp ung thư gan giai đoạn muộn này là bệnh nan y vô phương cứu chữa.
+ Trường hợp ung thư gan giai đoạn muộn có tiên lượng rất dè dặt, cần tập trung chăm sóc giảm nhẹ.
```

### med-stigma-03 (Rules: `MED006`)

```diff
- Cần tăng cường an ninh tại khu vực điều trị đối với con nghiện nhập viện.
+ Cần tăng cường an ninh tại khu vực điều trị đối với người điều trị nghiện chất nhập viện.
```

## Discharge

### med-discharge-redflag-01 (Rules: `MED007` · Register: `healthcare` · Doctype: `discharge-summary`)

```diff
- Quý khách xuất viện sau phẫu thuật cắt túi mật. Vết mổ khô. Hẹn tái khám sau 07 ngày tại phòng khám ngoại.
+ Quý khách xuất viện sau phẫu thuật cắt túi mật. Vết mổ khô. Hẹn tái khám sau 07 ngày. Dấu hiệu cần tái khám ngay hoặc đến cơ sở y tế cấp cứu: sốt cao liên tục hoặc đau bụng dữ dội.
```

### med-discharge-redflag-02 (Rules: `MED007` · Doctype: `discharge-summary`)

```diff
- Bệnh nhi xuất viện sau điều trị viêm phổi ổn định. Tiếp tục uống kháng sinh theo đơn tại nhà.
+ Bệnh nhi xuất viện sau điều trị viêm phổi ổn định. Tiếp tục uống kháng sinh theo đơn tại nhà. Dấu hiệu cần tái khám ngay: trẻ sốt cao trở lại, thở nhanh, co rút lồng ngực hoặc bú kém.
```

## Terminology

### med-calque-informed-consent (Rules: `CAL001`)

```diff
- Người bệnh đã ký vào bản sự đồng ý được thông tin trước khi làm thủ thuật can thiệp.
+ Người bệnh đã ký vào giấy cam kết đồng thuận điều trị trước khi làm thủ thuật can thiệp.
```

### med-calque-medical-history (Rules: `CAL001`)

```diff
- Bác sĩ khai thác kỹ lịch sử y tế của người bệnh nhằm phát hiện tiền sử dị ứng thuốc.
+ Bác sĩ khai thác kỹ tiền sử bệnh của người bệnh nhằm phát hiện nguy cơ dị ứng thuốc.
```

### med-calque-vital-signs (Rules: `CAL001`)

```diff
- Điều dưỡng theo dõi sát các dấu hiệu cuộc sống của người bệnh mỗi 30 phút một lần.
+ Điều dưỡng theo dõi sát chỉ số sinh tồn của người bệnh mỗi 30 phút một lần.
```

### med-calque-icu (Rules: `CAL001`)

```diff
- Người bệnh vừa được chuyển khẩn cấp lên đơn vị chăm sóc mạnh mẽ để thở máy.
+ Người bệnh vừa được chuyển khẩn cấp lên khoa hồi sức tích cực để thở máy.
```

### med-calque-dietary-supplement (Rules: `CAL001`)

```diff
- Sản phẩm được xếp vào nhóm thuốc bổ sung ăn kiêng nhập khẩu từ châu Âu.
+ Sản phẩm được xếp vào nhóm thực phẩm bảo vệ sức khỏe nhập khẩu từ châu Âu.
```

## Compliance

### med-superlative-best (Rules: `LAW001`)

```diff
- Chúng tôi tự hào là phòng khám đa khoa uy tín nhất tại khu vực miền Bắc.
+ Chúng tôi là phòng khám đa khoa đạt chuẩn chất lượng với đội ngũ bác sĩ chuyên khoa giàu kinh nghiệm.
```

### med-superlative-number-one (Rules: `LAW001`)

```diff
- Đơn vị được đánh giá là bệnh viện số 1 về can thiệp tim mạch hiện nay.
+ Đơn vị chuyên sâu về can thiệp tim mạch với hệ thống phòng mổ đạt chuẩn quốc tế.
```

## Unicode

### med-nfd-normalization (Rules: `NFC001`)

```diff
- Khám sức khỏe định kỳ cho người bệnh tại khoa nội.
+ Khám sức khỏe định kỳ cho người bệnh tại khoa nội.
```

## Orthography

### med-dia-ascii-vietnamese (Rules: `DIA001`)

```diff
- Quy khach vui long dat lich kham truoc khi den benh vien.
+ Quý khách vui lòng đặt lịch khám trước khi đến bệnh viện.
```

## Formatting

### med-num-comma-grouping (Rules: `NUM001`)

```diff
- Tổng chi phí phẫu thuật nội soi nội trú là 15,500,000 VND.
+ Tổng chi phí phẫu thuật nội soi nội trú là 15.500.000 ₫.
```

### med-num-ungrouped-currency (Rules: `NUM002`)

```diff
- Tiền thuốc bảo hiểm y tế đồng chi trả: 250000 ₫.
+ Tiền thuốc bảo hiểm y tế đồng chi trả: 250.000 ₫.
```

### med-num-dot-decimal (Rules: `NUM003`)

```diff
- Tỷ lệ đường huyết gắn hemoglobin HbA1c của người bệnh là 7.2%.
+ Tỷ lệ đường huyết gắn hemoglobin HbA1c của người bệnh là 7,2%.
```

## Register

### med-pro-mixed-register (Rules: `PRO001`)

```diff
- Bệnh viện xin thông báo tới Quý khách về lịch hẹn khám bệnh. Bạn vui lòng có mặt đúng giờ.
+ Bệnh viện xin thông báo tới Quý khách về lịch hẹn khám bệnh. Quý khách vui lòng có mặt đúng giờ.
```

### med-pro-casual-in-healthcare (Rules: `PRO002` · Register: `healthcare`)

```diff
- Xin chào bạn, vui lòng xuất trình thẻ căn cước công dân gắn chip tại quầy tiếp đón.
+ Xin chào Quý khách, vui lòng xuất trình thẻ căn cước công dân gắn chip tại quầy tiếp đón.
```

### med-pro-casual-in-clinical (Rules: `PRO002` · Register: `healthcare-clinical`)

```diff
- Bác sĩ dặn bạn uống thuốc đều đặn mỗi ngày sau bữa ăn.
+ Bác sĩ dặn người bệnh uống thuốc đều đặn mỗi ngày sau bữa ăn.
```
