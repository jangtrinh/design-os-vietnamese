<!-- vlc-disable: all -->

# Public Administration & Citizen Service QA Checklist (`design-os-vietnamese`)

This checklist is an authoritative quality gate for public administrative officers, digital transformation committees, government portal content editors, civil service software designers, and clerical staff prior to publishing online public service guidelines, administrative notifications, citizen correspondence, or civic software interfaces in Vietnam.

---

## Tier 1: Regulatory & Statutory Compliance Gate (P0 - Blocking)

- [ ] **1. Chuẩn hóa 2 mức độ dịch vụ công trực tuyến (`GOV001`):**
  - Đã loại bỏ hoàn toàn cách phân loại 4 mức độ cũ (`Mức độ 1`, `Mức độ 2`, `Mức độ 3`, `Mức độ 4`, `DVC mức 3/4`).
  - Sử dụng chính xác hai mức độ per Điều 11 Nghị định 42/2022/NĐ-CP: `Dịch vụ công trực tuyến toàn trình` hoặc `Dịch vụ công trực tuyến một phần`.
- [ ] **2. Cập nhật Thẻ căn cước & chấm dứt CMND 9 số (`GOV002`):**
  - Tên gọi giấy tờ tùy thân được cập nhật thành `Thẻ căn cước` (cấp mới từ 01/07/2024 per Luật Căn cước 2023).
  - Thẻ CCCD gắn chip đã cấp trước đó vẫn có giá trị sử dụng đến hết thời hạn ghi trên thẻ.
  - Tuyệt đối không yêu cầu xuất trình hoặc nộp bản sao `Chứng minh nhân dân (CMND) 9 số` (đã chính thức hết hạn sử dụng từ ngày 31/12/2024 per Điều 46 Luật Căn cước 2023).
- [ ] **3. Tính hợp lệ của cấp độ định danh điện tử VNeID (`GOV003`):**
  - Tài khoản VNeID chỉ có hai mức độ: `Tài khoản định danh điện tử mức độ 1` và `Tài khoản định danh điện tử mức độ 2` per Nghị định 69/2024/NĐ-CP.
  - Tuyệt đối không xuất hiện các danh xưng giả mạo: `VNeID mức độ 3`, `VNeID mức độ 4`, `Tài khoản định danh cấp 3`, `VNeID hạng vàng`.
- [ ] **4. Nghiêm cấm đòi hỏi Sổ hộ khẩu và Sổ tạm trú giấy (`GOV004`):**
  - Đã xóa bỏ 100% yêu cầu nộp bản chính hoặc bản sao công chứng Sổ hộ khẩu giấy, Sổ tạm trú giấy (hết giá trị per Điều 38 Luật Cư trú 2020 và Nghị định 104/2022/NĐ-CP).
  - Cơ quan nhà nước thực hiện tra cứu thông tin cư trú của công dân qua ứng dụng VNeID, quét mã QR trên Thẻ căn cước hoặc kết nối Cơ sở dữ liệu quốc gia về dân cư.
- [ ] **5. Đầy đủ 3 trường TTHC bắt buộc trong tài liệu hướng dẫn (`GOV005`):**
  - Mọi hướng dẫn TTHC (`doctype == dvc-guide`) bắt buộc phải có đầy đủ 03 thành phần:
    1. **Trình tự thực hiện / Cách thức thực hiện**
    2. **Thành phần hồ sơ**
    3. **Thời hạn giải quyết**.

---

## Tier 2: Administrative Procedure & Clerical Standards Gate (P1 - High)

- [ ] **6. Thể thức văn bản hành chính theo Nghị định 30/2020/NĐ-CP:**
  - Quốc hiệu, Tiêu ngữ đúng quy chuẩn: `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` / `Độc lập - Tự do - Hạnh phúc`.
  - Tên cơ quan, tổ chức ban hành, số ký hiệu văn bản, địa danh và ngày tháng năm ban hành văn bản.
  - Tên loại văn bản và trích yếu nội dung văn bản.
  - Chữ ký số chuyên dùng công vụ của cơ quan và người có thẩm quyền.
- [ ] **7. Mẫu Giấy tiếp nhận hồ sơ và hẹn trả kết quả:**
  - Áp dụng Mẫu số 01 Thông tư 01/2018/TT-VPCP, ghi rõ mã số hồ sơ, thời gian tiếp nhận, thời hạn trả kết quả và chữ ký của cán bộ một cửa.
- [ ] **8. Quy định giải quyết thủ tục liên thông & biên nhận điện tử:**
  - Tích hợp cổng thanh toán phí, lệ phí trực tuyến qua Cổng Dịch vụ công Quốc gia, cấp biên lai điện tử hợp lệ.

---

## Tier 3: Civil Service Etiquette & Citizen-Centric Language Gate (P2 - Medium)

- [ ] **9. Xóa bỏ thái độ cửa quyền, dọa dẫm công dân (`GOV006`):**
  - Loại bỏ hoàn toàn các phát ngôn hách dịch: `Công dân tự chịu hoàn toàn hậu quả nếu không biết thao tác máy tính`, `Cấm hỏi nhiều tại quầy một cửa`, `Cán bộ không có nghĩa vụ giải thích`.
  - Thay thế bằng hướng dẫn chu đáo, tận tâm: `Quý công dân gặp khó khăn khi thao tác vui lòng liên hệ tổng đài để được cán bộ hỗ trợ`.
- [ ] **10. Loại bỏ 100% calque dịch thô hành chính (`GOV006`):**
  - Thay thế `dịch vụ công cộng trên đường dây` bằng `Dịch vụ công trực tuyến`.
  - Thay thế `cửa hàng một điểm dừng` bằng `Bộ phận Một cửa` / `Trung tâm Phục vụ hành chính công`.
  - Thay thế `bàn dịch vụ công dân` bằng `Bộ phận tiếp nhận và trả kết quả`.
- [ ] **11. Chuẩn hóa đại từ xưng hô tôn trọng nhân dân:**
  - Xưng hô chuẩn mực: Người dân/doanh nghiệp gọi là `Quý công dân`, `Quý tổ chức`, `Người yêu cầu`.
  - Cơ quan nhà nước xưng `Chúng tôi` hoặc `[Tên cơ quan hành chính]`.
  - Không sử dụng các đại từ xưng hô suồng sã thiếu trang trọng (`bạn`, `mình`).
- [ ] **12. Tuân thủ luật quảng cáo & cấm từ ngữ so sánh nhất (`LAW001`):**
  - Không sử dụng các từ ngữ khẳng định mang tính thương mại: `dịch vụ công nhanh nhất thị trường`, `cổng thông tin số 1`.

---

## Tier 4: Technical & Orthographic Standards (P3 - Polish)

- [ ] **13. Định dạng ngày tháng năm chuẩn Việt Nam (`DATE001`):**
  - Ngày tháng năm viết chuẩn `dd/MM/yyyy` (ví dụ: `28/12/2026`, tuyệt đối không viết ngược kiểu Mỹ `12/28/2026`).
- [ ] **14. Quy tắc viết hoa tên cơ quan, tổ chức per Nghị định 30/2020/NĐ-CP:**
  - Viết hoa chữ cái đầu của các từ, cụm từ chỉ tên cơ quan, tổ chức: `Ủy ban nhân dân`, `Hội đồng nhân dân`, `Bộ Công an`, `Sở Tư pháp`.
  - Viết hoa chức vụ, chức danh lãnh đạo: `Chủ tịch Ủy ban nhân dân`, `Giám đốc Sở`.
- [ ] **15. Chuẩn hóa Unicode NFC & Dấu thanh tiếng Việt (`NFC001`, `TONE001`):**
  - Văn bản được chuẩn hóa Unicode dựng sẵn (NFC).
  - Nhất quán kiểu bỏ dấu thanh trong toàn bộ văn bản (kiểu mới: `hòa, thủy`).
