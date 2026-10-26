# Clinical & Electronic Medical Record (EMR) Writing Standards (`design-os-vietnamese`)

This guide establishes authoritative writing, formatting, and clinical documentation standards for electronic medical records (EMR), outpatient prescriptions, discharge summaries, and clinical notes in Vietnam, under **Luật Khám bệnh, chữa bệnh số 15/2023/QH15** and **Thông tư 32/2023/TT-BYT**.

---

## 1. Key Legislative Updates under Luật Khám bệnh, chữa bệnh 2023

Effective **01/01/2024**, Luật Khám bệnh, chữa bệnh số 15/2023/QH15 introduces fundamental transformations across medical administration in Vietnam:

### A. Obsolete vs. Current Licensing Terminology (`MED003`)
- ❌ **Cũ (Luật KCB 2009):** `Chứng chỉ hành nghề khám bệnh, chữa bệnh`, `Chứng chỉ hành nghề y`, `Chứng chỉ hành nghề y tế`.
- ✅ **Mới (Luật KCB 2023 Điều 26–35):** `Giấy phép hành nghề khám bệnh, chữa bệnh` (hoặc gọi ngắn gọn là `Giấy phép hành nghề`).
- **Thời hạn hiệu lực:** Giấy phép hành nghề có thời hạn **05 năm** (thay vì cấp một lần vô thời hạn như Chứng chỉ hành nghề trước đây). Người hành nghề phải cập nhật kiến thức y khoa liên tục (CME) để được gia hạn.

### B. Three-Tier Healthcare Delivery System (Phân cấp chuyên môn kỹ thuật)
Luật KCB 2023 bãi bỏ cách phân chia theo hạng bệnh viện (Hạng đặc biệt, Hạng I, II, III, IV) trong quản lý chuyên môn, thay bằng 3 cấp chuyên môn kỹ thuật:
1. **Cấp khám bệnh, chữa bệnh ban đầu:** Trạm y tế xã, phòng khám bác sĩ gia đình, phòng khám đa khoa sơ cấp, y tế cơ quan.
2. **Cấp khám bệnh, chữa bệnh cơ bản:** Bệnh viện quận/huyện, bệnh viện đa khoa/chuyên khoa tuyến tỉnh hạng trung bình.
3. **Cấp khám bệnh, chữa bệnh chuyên sâu:** Bệnh viện tuyến cuối, viện nghiên cứu chuyên khoa đầu ngành thực hiện kỹ thuật cao.

---

## 2. Electronic Medical Record (EMR) Standards under Thông tư 32/2023/TT-BYT

Thông tư 32/2023/TT-BYT (hiệu lực từ 01/01/2024) quy định chi tiết việc quản lý, khai thác hồ sơ bệnh án điện tử, thay thế hoàn toàn bệnh án giấy:

### A. Core EMR Architecture & Interoperability
- **Mã định danh duy nhất:** Mỗi người bệnh có một mã số định danh y tế (Mã người bệnh) thống nhất toàn quốc liên thông với Cơ sở dữ liệu Quốc gia về dân cư (VNeID / CCCD gắn chip).
- **Chữ ký số y tế (PKI & Timestamp):** Mọi ghi chép lâm sàng, kết quả xét nghiệm, chẩn đoán hình ảnh, y lệnh thuốc phải được ký số cá nhân của bác sĩ/điều dưỡng có thẩm quyền kèm dấu thời gian thực (timestamp), không được sửa xóa sau khi đã hoàn tất ký số.
- **Bảo mật và phân quyền:** Dữ liệu EMR phải tuân thủ cấp độ an toàn thông tin hệ thống y tế cấp 3 trở lên và quy định bảo vệ dữ liệu cá nhân (Nghị định 13/2023/NĐ-CP).

### B. Structured Clinical Documentation (Chuẩn SOAP)
Ghi chép diễn tiến bệnh hàng ngày trong EMR tuân theo chuẩn SOAP quốc tế được Việt hóa:
- **S (Subjective - Cơ năng):** Lời kể của người bệnh, triệu chứng đau, mệt mỏi, khó thở, cảm giác bất thường do người bệnh tự thuật.
- **O (Objective - Thực thể):**
  - Dấu hiệu sinh tồn: Mạch (lần/phút), Huyết áp (mmHg), Thân nhiệt (°C), Nhịp thở (lần/phút), SpO2 (%).
  - Khám thực thể theo cơ quan: Tim mạch, Hô hấp, Tiêu hóa, Thần kinh, Cơ xương khớp.
  - Kết quả cận lâm sàng: Công thức máu, Sinh hóa, X-quang, Siêu âm, CT/MRI.
- **A (Assessment - Đánh giá):** Chẩn đoán xác định, chẩn đoán phân biệt, đánh giá tiến triển sau dùng thuốc, mức độ nặng và biến chứng.
- **P (Plan - Kế hoạch):** Y lệnh dùng thuốc chi tiết, chế độ dinh dưỡng, chăm sóc điều dưỡng, chỉ định cận lâm sàng tiếp theo, hẹn tái khám hoặc hội chẩn.

---

## 3. ICD-10 & ICD-11 Diagnostic Coding Standards

Tất cả chẩn đoán y khoa trong EMR, phiếu thanh toán BHYT và giấy ra viện phải mã hóa chuẩn xác theo Danh mục mã bệnh ICD:

### A. Structure of Diagnostic Statements
Một chẩn đoán y khoa hoàn chỉnh phải gồm 3 phần:
1. **Bệnh chính (Primary Diagnosis):** Bệnh lý nguy hiểm nhất hoặc lý do chính khiến người bệnh nhập viện (kèm mã ICD-10/ICD-11 chính).
2. **Bệnh kèm theo (Comorbidity):** Các bệnh mạn tính hoặc bệnh lý nền đang cùng điều trị (tăng huyết áp, đái tháo đường, suy tim).
3. **Biến chứng (Complications):** Tình trạng phát sinh do bệnh chính gây ra (nhiễm toan ceton, phù phổi cấp, suy thận cấp).

### B. Example Formatting
- ❌ **Sai:** `Bệnh tiểu đường + huyết áp cao` *(thiếu tính chuyên môn y học, không mã hóa)*.
- ✅ **Chuẩn:**
  - `Bệnh chính: Đái tháo đường típ 2 có biến chứng mạch máu ngoại vi (E11.5)`
  - `Bệnh kèm theo: Tăng huyết áp nguyên phát giai đoạn 2 (I10)`
  - `Biến chứng: Loét bàn chân đái tháo đường độ 2 theo phân loại Wagner`

---

## 4. National Electronic Prescriptions (Thông tư 27/2021/TT-BYT & TT 52/2017/TT-BYT)

Đơn thuốc ngoại trú phải được lập điện tử, ký số và gửi lên Hệ thống thông tin quốc gia về quản lý kê đơn thuốc và bán thuốc theo đơn (`donthuocquocgia.vn`):

### A. Mandatory Elements of an Outpatient Prescription
1. **Thông tin cơ sở khám chữa bệnh:** Tên cơ sở, địa chỉ, số điện thoại hotline, mã định danh cơ sở y tế.
2. **Thông tin người bệnh:** Họ và tên (chữ in hoa), ngày tháng năm sinh, giới tính, số thẻ BHYT (nếu có), số CCCD/định danh cá nhân, cân nặng (đối với trẻ em dưới 72 tháng tuổi, bắt buộc ghi cân nặng và tên bố/mẹ).
3. **Chẩn đoán bệnh:** Tên bệnh và mã ICD-10 tương ứng.
4. **Chi tiết thuốc kê đơn:**
   - Tên thuốc: Tên gốc (Generic name) hoặc Tên biệt dược kèm tên hoạt chất trong ngoặc đơn.
   - Hàm lượng/Nồng độ: Ghi rõ hàm lượng (500 mg, 10 mg/5 ml).
   - Số lượng: Viết số lượng bằng số (và viết số lượng bằng chữ đối với thuốc gây nghiện, thuốc hướng thần).
   - Đơn vị tính: `viên`, `gói`, `lọ`, `ống`, `chai`.
5. **Hướng dẫn dùng thuốc (`MED004`):**
   - **Tuyệt đối cấm:** `uống khi cần`, `uống tùy ý`, `ngày uống vài lần`.
   - **Bắt buộc:** Đường dùng (`Uống`), liều lượng mỗi lần (`1 viên`), số lần trong ngày (`2 lần/ngày`), thời điểm (`Uống sau ăn sáng 30 phút và sau ăn tối 30 phút`).
6. **Lời dặn của bác sĩ:**
   - Dặn dò chế độ sinh hoạt, kiêng cữ.
   - Hướng dẫn theo dõi tác dụng phụ.
   - Dặn dò thời gian tái khám (`Tái khám sau 07 ngày hoặc tái khám ngay nếu xuất hiện sốt cao hoặc đau bụng dữ dội`).
7. **Thông tin người kê đơn:** Họ tên bác sĩ, chữ ký điện tử hoặc chữ ký tay, chức danh chuyên môn, mã số người hành nghề.

---

## 5. Discharge Summary Standards (Thông tư 32/2023/TT-BYT)

Giấy ra viện và Hướng dẫn chăm sóc sau xuất viện là tài liệu pháp lý quan trọng bàn giao cho người bệnh:

### A. Mandatory Sections in Discharge Summaries
1. **Thời gian nằm viện:** Ngày giờ vào viện và ngày giờ xuất viện.
2. **Quá trình điều trị tóm tắt:** Phương pháp điều trị chính (nội khoa, phẫu thuật, can thiệp mạch), thuốc đã dùng, kết quả điều trị (khỏi, đỡ/giảm, không thay đổi, nặng hơn, tử vong).
3. **Tình trạng người bệnh lúc xuất viện:** Toàn trạng, các chỉ số sinh tồn ổn định, vết mổ khô, các ống dẫn lưu đã rút.
4. **Hướng dẫn dùng thuốc tại nhà:** Liệt kê đơn thuốc ra viện rõ ràng liều dùng, giờ dùng.
5. **Dấu hiệu cảnh báo nguy hiểm (`MED007`):**
   - Phải có mục riêng: `Dấu hiệu cần tái khám ngay hoặc đến cơ sở y tế cấp cứu`.
   - Liệt kê cụ thể: Sốt cao liên tục trên 38,5 °C không hạ, vết mổ rỉ dịch mủ hoặc chảy máu tươi, nôn ói nhiều không ăn uống được, đau nhức tăng dần không đáp ứng thuốc giảm đau, khó thở, tức ngực.
6. **Hẹn ngày tái khám:** Ngày cụ thể (dd/MM/yyyy) hoặc số ngày sau xuất viện.
