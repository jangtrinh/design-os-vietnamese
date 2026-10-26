<!-- vlc-disable: all -->

# Medical & Healthcare Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese medical, hospital, clinical, EMR, and pharmaceutical terminology.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable Clinical, EMR, & Pharmaceutical Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ Y khoa chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| informed consent | `sự đồng ý được thông tin` | `giấy cam kết đồng thuận điều trị` / `đồng thuận phẫu thuật` | Thuật ngữ pháp lý y khoa theo Luật KCB 2023 | error |
| medical history | `lịch sử y tế` | `tiền sử bệnh` / `bệnh sử` | Thuật ngữ chuẩn trong hồ sơ bệnh án EMR | error |
| clinical trial | `thử nghiệm phòng khám` | `thử nghiệm lâm sàng` | Thuật ngữ Dược lâm sàng theo Luật Dược 2016 | error |
| vital signs | `các dấu hiệu cuộc sống` | `chỉ số sinh tồn` / `dấu hiệu sinh tồn` | Mạch, nhiệt độ, huyết áp, nhịp thở, SpO2 | error |
| inpatient | `bệnh nhân bên trong` | `người bệnh nội trú` | Luật KCB 2023 dùng chuẩn 'người bệnh nội trú' | error |
| outpatient | `bệnh nhân bên ngoài` | `người bệnh ngoại trú` | Phân loại theo Luật KCB 2023 | error |
| intensive care unit | `đơn vị chăm sóc mạnh mẽ` | `khoa hồi sức tích cực` / `khoa ICU` | Tên khoa chuyên môn bệnh viện | error |
| emergency department | `phòng ban khẩn cấp` | `khoa cấp cứu` | Tên khoa lâm sàng bệnh viện | error |
| discharge | `bị giải phóng khỏi viện` | `xuất viện` / `ra viện` | Thuật ngữ quản lý người bệnh | error |
| referral | `giới thiệu bệnh nhân` | `chuyển tuyến` / `giấy chuyển tuyến` | Quy chế chuyển tuyến khám chữa bệnh BHYT | error |
| side effect | `hiệu ứng phụ` | `tác dụng không mong muốn` / `tác dụng phụ` | Tờ hướng dẫn sử dụng thuốc TT 01/2018 | warn |
| adverse drug reaction | `phản ứng thuốc bất lợi` | `phản ứng có hại của thuốc` / `ADR` | Trung tâm DI & ADR Quốc gia | warn |
| contraindication | `chỉ định chống lại` | `chống chỉ định` | Dược thư Quốc gia Việt Nam | error |
| indication | `sự chỉ thị thuốc` | `chỉ định điều trị` | Dược thư Quốc gia Việt Nam | error |
| electronic medical record | `ghi chú y tế điện tử` | `bệnh án điện tử` / `hồ sơ bệnh án điện tử` | Thông tư 32/2023/TT-BYT | error |
| triage | `phân loại rác y tế` | `phân loại cấp cứu` / `phân luồng người bệnh` | Quy trình cấp cứu người bệnh | error |
| morbidity | `tính chất bệnh tật` | `tỷ lệ mắc bệnh` | Dịch tễ học y học | error |
| mortality | `tính chất tử vong` | `tỷ lệ tử vong` | Thống kê y tế công cộng | warn |
| prognosis | `sự dự đoán trước` | `tiên lượng` | Ghi chép bệnh án lâm sàng | error |
| diagnosis | `sự phán đoán bệnh` | `chẩn đoán` | Thuật ngữ lâm sàng bắt buộc | error |
| differential diagnosis | `chẩn đoán khác biệt` | `chẩn đoán phân biệt` | Quy chuẩn ghi bệnh án | error |
| primary diagnosis | `chẩn đoán nguyên thủy` | `chẩn đoán chính` | Theo chuẩn mã hóa bệnh tật ICD-10 | error |
| prescription | `đơn đặt hàng thuốc` | `đơn thuốc` | Thông tư 52/2017 & TT 27/2021/TT-BYT | error |
| over-the-counter | `qua mặt quầy` | `thuốc không kê đơn` / `thuốc OTC` | Danh mục thuốc không kê đơn Thông tư 07/2017 | error |
| prescription-only medicine | `thuốc chỉ theo toa` | `thuốc kê đơn` | Quy chế kê đơn Bộ Y tế | error |
| dietary supplement | `thuốc bổ sung ăn kiêng` | `thực phẩm bảo vệ sức khỏe` | Nghị định 15/2018/NĐ-CP | error |
| active pharmaceutical ingredient | `thành phần ma túy hoạt tính` | `dược chất` / `hoạt chất` | Luật Dược 2016 | error |
| excipient | `chất bổ trợ thụ động` | `tá dược` | Bào chế học dược phẩm | error |
| posology | `liều lượng học` | `liều dùng và cách dùng` | Mục bắt buộc trong đơn thuốc và SmPC | error |
| route of administration | `tuyến đường quản lý thuốc` | `đường dùng thuốc` | Uống, tiêm, bôi, đặt, khí dung | error |
| intravenous | `trong tĩnh mạch dây cáp` | `tiêm tĩnh mạch` / `truyền tĩnh mạch` | Viết tắt IV | error |
| intramuscular | `trong bắp thịt` | `tiêm bắp` | Viết tắt IM | error |
| subcutaneous | `dưới lớp da ngoài` | `tiêm dưới da` | Viết tắt SC | error |
| oral administration | `quản lý bằng miệng` | `đường uống` | Đường dùng thuốc phổ biến nhất | error |
| sublingual | `dưới cái lưỡi` | `ngậm dưới lưỡi` | Dạng dùng cấp cứu tim mạch | error |
| topical | `chủ đề ngoài da` | `dùng ngoài da` / `bôi ngoài da` | Dạng bào chế thuốc mỡ, gel, kem | error |
| palliative care | `chăm sóc giảm nhẹ gánh nặng` | `chăm sóc giảm nhẹ` | Chuyên ngành y học ung thư & lão khoa | warn |
| hemodialysis | `lọc máu bằng máy móc` | `thận nhân tạo` / `lọc máu chu kỳ` | Kỹ thuật hồi sức thận | error |
| hypertension | `sức ép máu cao` | `tăng huyết áp` | Bệnh lý tim mạch mạn tính | error |
| diabetes mellitus | `bệnh nước tiểu ngọt` | `đái tháo đường` | Nội tiết học chuẩn Bộ Y tế | error |
| myocardial infarction | `nhồi máu tim đột ngột` | `nhồi máu cơ tim` | Cấp cứu tim mạch | error |
| stroke | `đột quỵ đánh vào` | `tai biến mạch máu não` / `đột quỵ` | Bệnh lý thần kinh mạch máu | warn |
| cerebrovascular accident | `tai nạn mạch máu não` | `tai biến mạch máu não` | Thuật ngữ chuẩn trong hồ sơ bệnh án | error |
| anaphylaxis | `sốc phản vệ ngược lại` | `phản vệ` / `sốc phản vệ` | Phác đồ xử trí cấp cứu Thông tư 51/2017/TT-BYT | error |
| complete blood count | `đếm máu toàn bộ` | `tổng phân tích tế bào máu ngoại vi` | Xét nghiệm huyết học cơ bản | error |
| urinalysis | `phân tích nước tiểu tổng thể` | `tổng phân tích nước tiểu` | Xét nghiệm sinh hóa nước tiểu 10 thông số | warn |
| cerebrospinal fluid | `chất lỏng cột sống não` | `dịch não tủy` | Xét nghiệm chọc dò tủy sống | error |
| magnetic resonance imaging | `hình ảnh cộng hưởng từ trường` | `chụp cộng hưởng từ` / `chụp MRI` | Chẩn đoán hình ảnh chuyên sâu | error |
| computed tomography | `chụp cắt lớp máy tính toán` | `chụp cắt lớp vi tính` / `chụp CT` | Chẩn đoán hình ảnh | error |
| ultrasound | `siêu âm thanh` | `siêu âm` | Thăm dò chức năng chẩn đoán | error |
| biopsy | `sinh thiết cắt mô thịt` | `sinh thiết` | Giải phẫu bệnh học | warn |
| endoscopy | `nội soi nhìn vào trong` | `nội soi` | Thăm dò tiêu hóa/hô hấp | error |
| colonoscopy | `nội soi ruột già` | `nội soi đại tràng` | Thăm dò tiêu hóa dưới | error |
| gastroscopy | `nội soi bao tử` | `nội soi dạ dày` | Thăm dò tiêu hóa trên | error |
| follow-up examination | `kiểm tra theo dõi sau đó` | `tái khám` | Hướng dẫn quản lý sau điều trị | error |
| health insurance | `bảo hiểm sức khỏe công cộng` | `bảo hiểm y tế` / `BHYT` | Luật Bảo hiểm y tế | warn |
| co-payment | `đồng thanh toán tiền viện` | `đồng chi trả BHYT` | Chế độ thanh toán chi phí KCB BHYT | error |
| medical practitioner | `người thực hành y tế` | `người hành nghề khám bệnh, chữa bệnh` | Thuật ngữ định danh Luật KCB 2023 | warn |
| medical practice license | `chứng chỉ hành nghề y tế` | `giấy phép hành nghề khám bệnh, chữa bệnh` | Luật KCB 2023 thay thế toàn bộ chứng chỉ cũ | warn |
| medical record summary | `tóm tắt hồ sơ y khoa` | `tóm tắt hồ sơ bệnh án` | Biểu mẫu Thông tư 32/2023/TT-BYT | warn |
| acute respiratory distress | `suy sụp hô hấp nhọn` | `suy hô hấp cấp` | Cấp cứu hồi sức | error |
| septic shock | `sốc nhiễm trùng dơ bẩn` | `sốc nhiễm khuẩn` | Cấp cứu hồi sức tích cực | error |
| chronic kidney disease | `bệnh thận kinh niên kéo dài` | `bệnh thận mạn` | Danh pháp nội khoa hiện đại (thay bệnh thận mạn tính) | warn |
| liver cirrhosis | `xơ cứng gan vàng` | `xơ gan` | Bệnh lý tiêu hóa - gan mật | error |
| antimicrobial resistance | `kháng cự vi trùng` | `kháng kháng sinh` / `đề kháng kháng sinh` | Chiến lược Quốc gia phòng chống kháng thuốc | error |

---

## 2. Terminology Guidelines & Regulatory References

1. **Luật Khám bệnh, chữa bệnh 2023 (số 15/2023/QH15):**
   - Không gọi là `Chứng chỉ hành nghề`, bắt buộc dùng `Giấy phép hành nghề khám bệnh, chữa bệnh`.
   - Sử dụng từ ngữ chuẩn mực: `người bệnh` (thay vì chỉ dùng `bệnh nhân` trong văn bản pháp lý), `người hành nghề`.
2. **Thông tư 32/2023/TT-BYT về Bệnh án điện tử:**
   - Các trường thông tin hành chính, chẩn đoán (ICD-10/ICD-11), tóm tắt bệnh án, kết quả xét nghiệm, đơn thuốc phải liên thông theo định dạng chuẩn HL7/FHIR và dữ liệu Bộ Y tế.
3. **Nghị định 15/2018/NĐ-CP & Luật Dược 2016:**
   - Phân biệt tuyệt đối giữa `thuốc` (điều trị bệnh) và `thực phẩm bảo vệ sức khỏe` (hỗ trợ sức khỏe).
   - Tuyệt đối không dùng các từ ngữ hoán đổi gây hiểu nhầm bản chất sản phẩm.
