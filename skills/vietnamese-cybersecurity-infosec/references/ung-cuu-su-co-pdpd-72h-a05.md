<!-- vlc-disable: all -->

# Personal Data Breach Incident Response & 72-Hour A05 Notification Guide

> Statutory mandate (from 01/01/2026): **Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15** and **Nghị định số 356/2025/NĐ-CP**. Nghị định 13/2023/NĐ-CP (effective 01/07/2023) is no longer in force (NĐ 356/2025 Điều 42 khoản 2).

---

## 1. Statutory Breach Notification Timeline (Điều 23 Luật 91/2025/QH15)

Under **Điều 23 Luật 91/2025/QH15**, in the event of an incident involving personal data leakage, loss, or unauthorized breach:

1. **72-Hour Mandatory Window:**
   - The Data Controller (`Bên Kiểm soát dữ liệu cá nhân`) and Data Processor (`Bên Xử lý dữ liệu cá nhân`) must formally notify the **Department of Cybersecurity and High-Tech Crime Prevention (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao — A05, Bộ Công an)** within **72 hours** from the time of detecting the breach.
   - Any internal policy specifying deadlines longer than 72 hours (e.g. 7 days, 15 days, 30 days) is **statutorily void and subject to administrative penalties**.

2. **Official Form: Mẫu số 08 (Nghị định 356/2025/NĐ-CP); formerly Mẫu số 03a of Nghị định 13/2023/NĐ-CP:**
   - The notification must be drafted in Vietnamese according to **Mẫu số 08 ban hành kèm theo Nghị định số 356/2025/NĐ-CP** (content per Điều 28; Mẫu 03a/03b of Decree 356 is the impact-assessment update form).
   - Core required sections (Nghị định 356/2025/NĐ-CP Điều 28 khoản 1, điểm a–d):
     - Tên cơ quan, tổ chức, cá nhân thông báo;
     - Mô tả bản chất vụ vi phạm (thời gian, địa điểm, cách thức xảy ra sự cố);
     - Loại dữ liệu cá nhân và số lượng chủ thể dữ liệu ước tính bị ảnh hưởng;
     - Tên, thông tin liên hệ của Nhân sự bảo vệ dữ liệu (DPO) hoặc bộ phận đầu mối;
     - Đánh giá hậu quả và thiệt hại có thể xảy ra;
     - Các biện pháp đã áp dụng và kế hoạch ngăn chặn, khắc phục hậu quả.

---

## 2. Classification of Personal Data (Điều 2 Luật 91/2025/QH15; Điều 3–4 NĐ 356/2025/NĐ-CP)

Under **Điều 2 khoản 2 và khoản 3 Luật 91/2025/QH15** (lists in **Điều 3 and Điều 4 Nghị định 356/2025/NĐ-CP**), personal data is divided into two strict legal categories:

### A. Dữ liệu cá nhân cơ bản (Basic Personal Data — Điều 3 NĐ 356/2025/NĐ-CP, verbatim)
- 1. Họ, chữ đệm và tên khai sinh, tên gọi khác (nếu có);
- 2. Ngày, tháng, năm sinh; ngày, tháng, năm chết hoặc mất tích;
- 3. Giới tính;
- 4. Nơi sinh, nơi đăng ký khai sinh, nơi đăng ký thường trú, nơi đăng ký tạm trú, nơi ở hiện tại, quê quán, địa chỉ liên hệ;
- 5. Quốc tịch;
- 6. Hình ảnh của cá nhân;
- 7. Số điện thoại, số định danh cá nhân, số hộ chiếu, số giấy phép lái xe, số biển số xe;
- 8. Tình trạng hôn nhân;
- 9. Thông tin về mối quan hệ gia đình (cha mẹ, con, vợ, chồng);
- 10. Thông tin về tài khoản số của cá nhân;
- 11. Các thông tin khác gắn liền với một con người cụ thể hoặc giúp xác định một con người cụ thể không thuộc quy định tại Điều 4 Nghị định này.

### B. Dữ liệu cá nhân nhạy cảm (Sensitive Personal Data — Điều 4 khoản 1 NĐ 356/2025/NĐ-CP, verbatim)
*Requires enhanced administrative, organizational, and technical safeguards. Misclassifying these as basic data violates PDPD:*
- a) Dữ liệu tiết lộ nguồn gốc chủng tộc, nguồn gốc dân tộc;
- b) Quan điểm về chính trị, tôn giáo, tín ngưỡng;
- c) Thông tin về đời sống riêng tư, bí mật cá nhân, bí mật gia đình;
- d) Tình trạng sức khỏe;
- đ) Dữ liệu sinh trắc học, đặc điểm di truyền;
- e) Dữ liệu tiết lộ đời sống tình dục, xu hướng tình dục của cá nhân;
- g) Dữ liệu về tội phạm, vi phạm pháp luật được thu thập, lưu trữ bởi các cơ quan thực thi pháp luật;
- h) Vị trí của cá nhân được xác định qua dịch vụ định vị;
- i) Thông tin tên đăng nhập và mật khẩu truy cập tài khoản định danh điện tử của cá nhân; hình ảnh thẻ căn cước, thẻ căn cước công dân, chứng minh nhân dân;
- k) Tên đăng nhập, mật khẩu truy cập của tài khoản ngân hàng; thông tin thẻ ngân hàng, dữ liệu về lịch sử giao dịch của tài khoản ngân hàng; thông tin tài chính, tín dụng và các thông tin về hoạt động, lịch sử giao dịch tài chính, chứng khoán, bảo hiểm của khách hàng tại các tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, tổ chức cung ứng dịch vụ trung gian thanh toán, chứng khoán, bảo hiểm, các tổ chức được phép khác;
- l) Dữ liệu theo dõi hành vi, hoạt động sử dụng dịch vụ viễn thông, mạng xã hội, dịch vụ truyền thông trực tuyến và các dịch vụ khác trên không gian mạng;
- m) Dữ liệu cá nhân khác được pháp luật quy định cần giữ bí mật hoặc cần có biện pháp bảo mật chặt chẽ.

---

## 3. Incident Communication Workflow & Escalation Architecture

```
[Phát hiện vi phạm (T0)]
        │
        ├───────────────────────────────────────────────────────┐
        ▼ (Trong vòng 24 giờ)                                    ▼
[Kích hoạt Đội CSIRT & DPO]                            [Cách ly hệ thống bị xâm nhập]
        │                                                       │
        ▼ (Phân tích phạm vi, số lượng chủ thể)                ▼
[Soạn thảo Mẫu số 08 NĐ 356]                          [Bảo toàn chứng cứ số (Digital Forensics)]
        │
        ▼ (Trước T0 + 72 giờ)
[Gửi Thông báo vi phạm chính thức tới Cục A05 Bộ Công an]
        │
        ▼
[Thông báo cho Chủ thể dữ liệu nếu có nguy cơ gây thiệt hại nghiêm trọng]
```

---

## 4. Standard SOC Communication Guidelines

- **Never Solicit Credentials:** Notifications, customer advisories, and breach responses must NEVER ask affected users to reply with passwords, OTPs, PINs, or CVV numbers.
- **Empathetic and Actionable:** Detail exact containment steps taken and concrete user actions (reset credentials via official portal, monitor bank account statements).
