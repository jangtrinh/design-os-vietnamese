<!-- vlc-disable: all -->

# Vietnamese Cybersecurity & InfoSec Pre-Publish QA Checklist (`vietnamese-cybersecurity-infosec`)

This checklist is an authoritative quality gate for Chief Information Security Officers (CISO), SOC managers, CSIRT incident response teams, penetration testers, and compliance officers prior to releasing security advisories, pentest reports, incident notifications, or regulatory submissions in Vietnam.

---

## Tier 1: Statutory & Incident Notification Gate (P0 - Blocking)

- [ ] **1. Thời hạn thông báo rò rỉ dữ liệu cá nhân 72 giờ gửi Cục A05 (`SEC001`):**
  - Mọi tài liệu thông báo vi phạm bảo vệ dữ liệu cá nhân (`breach-notification`) phải ghi rõ:
    - Cơ quan tiếp nhận: `Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) - Bộ Công an`.
    - Thời hạn thông báo: `trong thời hạn 72 giờ kể từ khi phát hiện vi phạm` theo Điều 23 Nghị định 13/2023/NĐ-CP (Mẫu số 03a).
  - Tuyệt đối không quy định thời hạn vượt quá 72 giờ (ví dụ: ghi 5 ngày, 7 ngày).
- [ ] **2. Thẩm định cấp độ an toàn hệ thống thông tin Cấp độ 1 đến Cấp độ 5 (`SEC002`):**
  - Báo cáo đánh giá hệ thống và hồ sơ đề xuất cấp độ tuân thủ nghiêm ngặt khung Cấp độ 1 đến Cấp độ 5 theo Nghị định 85/2016/NĐ-CP và Thông tư 12/2022/TT-BTTTT.
  - Tuyệt đối không tự ý bịa đặt hoặc sử dụng các danh xưng: `ATTT cấp độ 6`, `cấp độ 7`, `tiêu chuẩn bảo mật cấp độ 6`.
- [ ] **3. Phân loại chuẩn xác dữ liệu cá nhân cơ bản và nhạy cảm (`SEC006`):**
  - Phân loại chính xác theo Điều 2 Khoản 4 Nghị định 13/2023/NĐ-CP:
    - `Dữ liệu cá nhân nhạy cảm`: Dữ liệu sức khỏe/bệnh án, thông tin tài khoản/số dư ngân hàng, dữ liệu sinh trắc học, dữ liệu định vị cá nhân.
    - Áp dụng các biện pháp bảo vệ tăng cường và chỉ định bộ phận/nhân sự bảo vệ dữ liệu (DPO).
- [ ] **4. Báo cáo sự cố an toàn thông tin mạng theo Điều 20 Luật ATTT mạng 2015:**
  - Quy trình ứng cứu sự cố tuân thủ Thông tư 20/2017/TT-BTTTT, thực hiện thông báo cho VNCERT/CC (Cục An toàn thông tin) đối với các sự cố nghiêm trọng.

---

## Tier 2: Technical Integrity & Vulnerability Advisory Gate (P1 - High)

- [ ] **5. Đầy đủ điểm CVSS và Mức độ nghiêm trọng trong cảnh báo bảo mật (`SEC005`):**
  - Bản tin cảnh báo lỗ hổng bảo mật (`security-advisory`) bắt buộc có mục:
    - `Mức độ nghiêm trọng` (Thấp, Trung bình, Cao, Nghiêm trọng) kèm điểm số `CVSS` v3.1 / v4.0 rõ ràng.
- [ ] **6. Biện pháp khắc phục và hướng dẫn bản vá khả thi (`SEC005`):**
  - Bắt buộc có mục `Biện pháp khắc phục` hoặc `Khuyến nghị cập nhật bản vá` chỉ rõ phiên bản cập nhật hoặc giải pháp thay thế tạm thời (workaround) từ nhà sản xuất.
- [ ] **7. Tuyệt đối không yêu cầu thông tin xác thực nhạy cảm (`SEC004`):**
  - Rà soát toàn bộ thông báo nội bộ, email cảnh báo người dùng và kịch bản hỗ trợ kỹ thuật:
    - Tuyệt đối không yêu cầu người dùng gửi `mật khẩu`, `mã OTP`, `mã PIN`, hoặc `số CVV`.
    - Luôn kèm theo khuyến cáo an toàn: *"Quản trị viên không bao giờ yêu cầu người dùng cung cấp mật khẩu hay mã xác thực."*
- [ ] **8. Cấu trúc báo cáo kiểm thử xâm nhập (Pentest Report):**
  - Báo cáo (`pentest-report`) có đầy đủ: Tóm tắt cho ban lãnh đạo (Executive Summary), Phạm vi đánh giá (Scope), Phương pháp luận (OWASP/NIST), Chi tiết phát hiện kèm bằng chứng thực nghiệm (PoC), và Biện pháp khắc phục cụ thể.

---

## Tier 3: Terminology & Sociolinguistic Etiquette Gate (P2 - Medium)

- [ ] **9. Loại bỏ hoàn toàn thuật ngữ dịch máy thô ráp (calque) (`SEC003`):**
  - Dùng `tấn công giả mạo` (thay vì 'cuộc tấn công câu cá').
  - Dùng `mã độc tống tiền` (thay vì 'phần mềm đòi tiền chuộc / mã độc chuộc lỗi').
  - Dùng `tấn công phi kỹ thuật` / `thao túng tâm lý` (thay vì 'kỹ thuật xã hội').
  - Dùng `bề mặt tấn công` (thay vì 'bề mặt cuộc tấn công').
  - Dùng `tường lửa thế hệ mới` (thay vì 'tường lửa thế hệ tiếp theo').
  - Dùng `kiểm thử xâm nhập` (thay vì 'kiểm toán cây bút').
- [ ] **10. Không sử dụng tuyên bố an toàn tuyệt đối 100% (`LAW001`):**
  - Loại bỏ các tuyên bố phản khoa học: `miễn nhiễm 100% với mã độc`, `an toàn tuyệt đối 100%`, `bất khả xâm phạm`.
  - Sử dụng văn phong khách quan, quản trị rủi ro và phòng thủ theo chiều sâu (defense-in-depth).
- [ ] **11. Nhất quán đại từ xưng hô theo Register:**
  - Thông báo vi phạm gửi cơ quan quản lý (`gov-admin`): Đại từ trang trọng, văn phong hành chính nhà nước.
  - Cảnh báo bảo mật kỹ thuật (`infosec-advisory` / `eng-impersonal`): Ngôi thứ ba khách quan, gãy gọn, chính xác.

---

## Tier 4: Technical & Orthographic Standards (P3 - Polish)

- [ ] **12. Chuẩn Unicode NFC & Dấu thanh tiếng Việt (`NFC001`, `TONE001`):**
  - Toàn bộ văn bản kỹ thuật đã được chuẩn hóa Unicode dựng sẵn (NFC).
  - Nhất quán kiểu bỏ dấu thanh trong toàn bộ văn bản (kiểu mới: `hoà, thuỷ` hoặc kiểu cũ: `hòa, thủy`).
- [ ] **13. Chuẩn hóa mã định danh CVE và thuật ngữ quốc tế:**
  - Mã định danh CVE viết hoa chuẩn: `CVE-2026-1026`.
  - Các chỉ số kỹ thuật, vector tấn công CVSS (ví dụ: `CVSS:3.1/AV:N/AC:L/...`) giữ nguyên định dạng chuẩn quốc tế.
- [ ] **14. Định dạng thời gian xảy ra sự cố và nhật ký (`DATE001`):**
  - Thời gian sự cố ghi rõ ngày tháng năm `dd/MM/yyyy` và giờ phút giây theo giờ Việt Nam (UTC+7 / ICT).
- [ ] **15. Bảo mật thông tin trong báo cáo công khai:**
  - Che mờ (masking) địa chỉ IP nội bộ nhạy cảm, tên người dùng, và chuỗi mã hash trước khi công bố ra bên ngoài.
