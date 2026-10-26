<!-- vlc-disable: all -->

# Personal Data Breach Incident Response & 72-Hour A05 Notification Guide

> Statutory mandate: **Nghị định số 13/2023/NĐ-CP** (Nghị định về Bảo vệ dữ liệu cá nhân - PDPD), effective July 1, 2023.

---

## 1. Statutory Breach Notification Timeline (Điều 23 NĐ 13/2023/NĐ-CP)

Under **Điều 23 Nghị định 13/2023/NĐ-CP**, in the event of an incident involving personal data leakage, loss, or unauthorized breach:

1. **72-Hour Mandatory Window:**
   - The Data Controller (`Bên Kiểm soát dữ liệu cá nhân`) and Data Processor (`Bên Xử lý dữ liệu cá nhân`) must formally notify the **Department of Cybersecurity and High-Tech Crime Prevention (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao — A05, Bộ Công an)** within **72 hours** from the time of detecting the breach.
   - Any internal policy specifying deadlines longer than 72 hours (e.g. 7 days, 15 days, 30 days) is **statutorily void and subject to administrative penalties**.

2. **Official Form 03a (Mẫu số 03a):**
   - The notification must be drafted in Vietnamese according to **Mẫu số 03a ban hành kèm theo Nghị định số 13/2023/NĐ-CP**.
   - Core required sections:
     - Tên cơ quan, tổ chức, cá nhân thông báo;
     - Mô tả bản chất vụ vi phạm (thời gian, địa điểm, cách thức xảy ra sự cố);
     - Loại dữ liệu cá nhân và số lượng chủ thể dữ liệu ước tính bị ảnh hưởng;
     - Tên, thông tin liên hệ của Nhân sự bảo vệ dữ liệu (DPO) hoặc bộ phận đầu mối;
     - Đánh giá hậu quả và thiệt hại có thể xảy ra;
     - Các biện pháp đã áp dụng và kế hoạch ngăn chặn, khắc phục hậu quả.

---

## 2. Classification of Personal Data (Điều 2 NĐ 13/2023/NĐ-CP)

Under **Điều 2 Khoản 3 và Khoản 4 Nghị định 13/2023/NĐ-CP**, personal data is divided into two strict legal categories:

### A. Dữ liệu cá nhân cơ bản (Basic Personal Data — Khoản 3)
- Họ, chữ đệm và tên khai sinh, tên gọi khác;
- Ngày, tháng, năm sinh; giới tính;
- Nơi sinh, nơi thường trú, nơi tạm trú, quê quán;
- Quốc tịch; hình ảnh cá nhân;
- Số điện thoại, địa chỉ thư điện tử;
- Số định danh cá nhân (CCCD), số hộ chiếu, mã số thuế.

### B. Dữ liệu cá nhân nhạy cảm (Sensitive Personal Data — Khoản 4)
*Requires enhanced administrative, organizational, and technical safeguards. Misclassifying these as basic data violates PDPD:*
- Quan điểm chính trị, quan điểm tôn giáo;
- **Tình trạng sức khỏe** và đời tư ghi trong hồ sơ bệnh án;
- **Thông tin liên quan đến nguồn gốc chủng tộc, nguồn gốc dân tộc**;
- **Đặc điểm di truyền**, **thuộc tính sinh trắc học**;
- Đời sống tình dục, xu hướng tình dục;
- Dữ liệu về tội phạm, hành vi phạm tội được thu thập từ cơ quan điều tra;
- **Thông tin khách hàng của tổ chức tín dụng, chi nhánh ngân hàng nước ngoài, tổ chức cung ứng dịch vụ trung gian thanh toán** (thông tin định danh, tài khoản, số dư, tiền gửi, lịch sử giao dịch);
- **Dữ liệu về vị trí của cá nhân** được xác định qua dịch vụ định vị;
- Dữ liệu cá nhân khác được pháp luật quy định là đặc thù và cần có biện pháp bảo vệ cần thiết.

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
[Soạn thảo Mẫu số 03a NĐ 13]                           [Bảo toàn chứng cứ số (Digital Forensics)]
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
