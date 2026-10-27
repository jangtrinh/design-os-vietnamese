<!-- vlc-disable: all -->

# Vietnamese Insurance & InsurTech Pre-Publish QA Checklist (`vietnamese-insurance-insurtech`)

This checklist is an authoritative quality gate for insurance product managers, actuaries, legal counsels, underwriters, and InsurTech engineers prior to releasing policy illustrations, certificates, digital onboarding journeys, or bancassurance materials in Vietnam.

---

## Tier 1: Statutory & Regulatory Compliance Gate (P0 - Blocking)

- [ ] **1. Phân định rõ bảo hiểm liên kết đầu tư và tiền gửi tiết kiệm (`INS001`):**
  - Tài liệu minh họa bán hàng và ứng dụng InsurTech tuyệt đối không sử dụng các cụm từ mạo danh: `tiết kiệm ngân hàng cam kết lãi suất`, `gửi tiết kiệm đầu tư cam kết lợi nhuận cố định`, `lợi nhuận cố định 100% không rủi ro`.
  - Phân định rành mạch giữa phần phí bảo hiểm rủi ro thuần túy và phần phí phân bổ vào quỹ đầu tư theo Thông tư 67/2023/TT-BTC.
  - Hiển thị đầy đủ cảnh báo rủi ro đầu tư và các kịch bản tỷ suất lợi nhuận (thấp, trung bình, cao) theo khung hướng dẫn của Bộ Tài chính.
- [ ] **2. Thời gian cân nhắc tham gia bảo hiểm 21 ngày (`INS002`):**
  - Mọi tài liệu minh họa (`policy-illustration`) và hợp đồng bảo hiểm nhân thọ thời hạn trên 01 năm ghi rõ:
    `"Thời gian cân nhắc tham gia bảo hiểm là 21 ngày kể từ ngày nhận được hợp đồng bảo hiểm."`
  - Tuyệt đối không rút ngắn thời hạn cân nhắc xuống 7, 10, hay 14 ngày, và không có điều khoản khước từ quyền hủy hợp đồng nhận lại phí trong 21 ngày này theo Điều 35 Luật KDBH 2022.
- [ ] **3. Minh bạch điều khoản loại trừ trách nhiệm bảo hiểm (`INS003`):**
  - Giấy chứng nhận bảo hiểm (`insurance-certificate`) và tóm tắt hợp đồng bắt buộc có riêng mục `Điều khoản loại trừ trách nhiệm bảo hiểm`.
  - Tuyệt đối không có các tuyên bố sai sự thật: `không cần đọc điều khoản loại trừ`, `chi trả mọi rủi ro không loại trừ`, `cam kết chi trả 100% không loại trừ`.
  - Bằng chứng đại lý bảo hiểm đã giải thích rõ ràng, đầy đủ các trường hợp loại trừ cho bên mua bảo hiểm theo Điều 19 Luật KDBH 2022.
- [ ] **4. Nghiêm cấm ép buộc mua bảo hiểm trong kênh Bancassurance (`INS006`):**
  - Kiểm tra toàn bộ hợp đồng tín dụng, tài liệu tư vấn và luồng phê duyệt khoản vay tại ngân hàng: tuyệt đối không ràng buộc điều kiện `bắt buộc mua bảo hiểm nhân thọ mới được giải ngân khoản vay`.
  - Tôn trọng quyền tự nguyện lựa chọn của khách hàng theo quy định của Thông tư 67/2023/TT-BTC và Luật Các tổ chức tín dụng 2024.
- [ ] **5. Thời hạn giải quyết bồi thường chuẩn luật định (`INS005`):**
  - Hướng dẫn bồi thường (`claim-guide`) quy định thời hạn giải quyết bồi thường là `15 ngày kể từ ngày nhận đủ hồ sơ hợp lệ` (tối đa `30 ngày` nếu cần xác minh) theo Điều 31 Luật KDBH 2022.
  - Tuyệt đối không quy định các thời hạn kéo dài trái pháp luật như 45 ngày, 60 ngày hoặc 90 ngày.

---

## Tier 2: Contractual & Actuarial Precision Gate (P1 - High)

- [ ] **6. Chuẩn hóa 4 chủ thể pháp lý trong quan hệ bảo hiểm (`INS004`):**
  - Sử dụng chính xác: `Doanh nghiệp bảo hiểm` (không dùng 'nhà bảo hiểm/hãng bảo hiểm' trong hợp đồng), `Bên mua bảo hiểm` (không dùng 'người giữ chính sách'), `Người được bảo hiểm` (không dùng 'người được bảo đảm'), `Người thụ hưởng` (không dùng 'người hưởng lợi' chung chung).
- [ ] **7. Chuẩn hóa thuật ngữ tài chính - bảo hiểm (`INS004`):**
  - Dùng `Hợp đồng bảo hiểm` (thay vì 'chính sách bảo hiểm').
  - Dùng `Phí bảo hiểm` / `Phí bảo hiểm định kỳ` (thay vì 'tiền thưởng bảo hiểm').
  - Dùng `Phạm vi bảo hiểm` / `Quyền lợi bảo hiểm` (thay vì 'câu chuyện bảo hiểm').
  - Dùng `Giá trị hoàn lại` (thay vì 'giá trị tiền mặt sẵn có').
  - Dùng `Sự kiện bất khả kháng` / `Thiên tai` (thay vì 'sự kiện thiên Chúa').
- [ ] **8. Minh bạch các loại phí khấu trừ trong sản phẩm liên kết đầu tư:**
  - Tài liệu minh họa và bảng giá trị tài khoản liệt kê chi tiết: Phí ban đầu, phí bảo hiểm rủi ro, phí quản lý hợp đồng, phí quản lý quỹ, và phí chấm dứt hợp đồng trước hạn.

---

## Tier 3: Digital Product & Sociolinguistic Etiquette Gate (P2 - Medium)

- [ ] **9. Loại bỏ tuyên bố so sánh nhất chưa có kiểm chứng (`LAW001`):**
  - Không sử dụng các từ ngữ: `tốt nhất`, `số 1`, `hàng đầu`, `duy nhất`, `lãi suất cao nhất thị trường` khi chưa có chứng nhận hợp pháp của cơ quan nhà nước có thẩm quyền.
- [ ] **10. Nhất quán đại từ xưng hô theo Register:**
  - Trong tài liệu minh họa và hướng dẫn bồi thường (`insurance-policyholder`): Xưng hô tôn trọng `Quý khách`, bên bảo hiểm xưng `Công ty` hoặc `[Tên Doanh nghiệp Bảo hiểm]`.
  - Trong giấy chứng nhận hợp đồng (`legal-contract`): Sử dụng đại từ ngôi thứ ba trang trọng (`Bên mua bảo hiểm`, `Doanh nghiệp bảo hiểm`).
- [ ] **11. Giao diện InsurTech & Ứng dụng số (UI/UX):**
  - Giao diện ứng dụng ngân hàng số (Mobile Banking) khi phân phối bảo hiểm hiển thị rõ dòng nhãn nhận diện độc lập: `Sản phẩm bảo hiểm do [Tên DNBH] cung cấp, không phải sản phẩm tiền gửi của ngân hàng`.
  - Thiết kế bước xác nhận chủ động (affirmative consent checkbox) trước khi chuyển sang bước thanh toán phí bảo hiểm.

---

## Tier 4: Technical & Orthographic Standards (P3 - Polish)

- [ ] **12. Chuẩn Unicode NFC & Dấu thanh tiếng Việt (`NFC001`, `TONE001`):**
  - Toàn bộ văn bản hợp đồng và tài liệu số hóa tuân thủ chuẩn Unicode dựng sẵn (NFC).
  - Nhất quán kiểu bỏ dấu thanh trong toàn bộ văn bản (kiểu mới: `hoà, thuỷ` hoặc kiểu cũ: `hòa, thủy`).
- [ ] **13. Định dạng số tiền tệ và phân cách hàng nghìn chuẩn Việt Nam (`NUM001`–`NUM003`):**
  - Dấu chấm phân cách hàng nghìn: `25.000.000 ₫`, `100.000.000 ₫` (không dùng dấu phẩy `25,000,000`).
  - Dấu phẩy phân cách số thập phân: `tỷ suất đầu tư 7,5%/năm` (không dùng dấu chấm `7.5%`).
- [ ] **14. Định dạng ngày tháng và số điện thoại tổng đài CSKH (`DATE001`, `PHONE001`):**
  - Ngày tháng năm viết chuẩn `dd/MM/yyyy` (ví dụ: `27/10/2026`).
  - Số điện thoại tổng đài hỗ trợ bồi thường viết chuẩn quốc tế hoặc hotline trong nước: `1900 xxxx` hoặc `+84 24 3987 6543`.
- [ ] **15. Bảo mật dữ liệu cá nhân y tế và sức khỏe (Nghị định 13/2023/NĐ-CP):**
  - Dữ liệu tiền sử bệnh lý, hồ sơ sức khỏe và thông tin tài chính của người được bảo hiểm được phân loại là `dữ liệu cá nhân nhạy cảm`, bắt buộc mã hóa và bảo mật nghiêm ngặt.
