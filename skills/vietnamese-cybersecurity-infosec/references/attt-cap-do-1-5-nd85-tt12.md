<!-- vlc-disable: all -->

# Information System Security Classification: Levels 1–5 (NĐ 85/2016 & TT 12/2022)

> Statutory framework: **Luật An toàn thông tin mạng 2015** (Luật số 86/2015/QH13), **Nghị định 85/2016/NĐ-CP**, and **Thông tư 12/2022/TT-BTTTT** of the Ministry of Information and Communications.

---

## 1. Statutory 5-Tier Classification Architecture

Under **Điều 21 Luật An toàn thông tin mạng 2015** and **Nghị định số 85/2016/NĐ-CP**, all information systems operating within Vietnamese jurisdiction are classified into strictly **five security levels (Cấp độ 1 đến Cấp độ 5)** based on the severity of damage caused to national interests, public order, and organizations/individuals upon compromise:

| Cấp độ ATTT | Tên gọi & Định nghĩa luật định | Phạm vi & Tác động khi bị sự cố | Thẩm quyền thẩm định / phê duyệt |
|---|---|---|---|
| **Cấp độ 1** | Hệ thống thông tin cấp độ 1 | Phục vụ nội bộ cơ quan, tổ chức; gián đoạn không gây tổn hại lớn đến hoạt động | Chủ quản hệ thống thông tin |
| **Cấp độ 2** | Hệ thống thông tin cấp độ 2 | Phục vụ công chúng hoặc xử lý thông tin nội bộ có giá trị; gián đoạn gây ảnh hưởng cục bộ | Chủ quản hệ thống thông tin |
| **Cấp độ 3** | Hệ thống thông tin cấp độ 3 | Cung cấp dịch vụ công trực tuyến, cổng thông tin điện tử cấp tỉnh/bộ, hoặc hệ thống tài chính quy mô lớn; gián đoạn gây hậu quả trên phạm vi ngành hoặc địa phương | Đơn vị chuyên trách ATTT của Bộ, ngành, địa phương |
| **Cấp độ 4** | Hệ thống thông tin cấp độ 4 | Hệ thống thông tin quan trọng phục vụ quản lý nhà nước tầm quốc gia; gián đoạn gây hậu quả nghiêm trọng trên phạm vi toàn quốc | Cục An toàn thông tin (Bộ TT&TT) hoặc Bộ Công an/Bộ Quốc phòng |
| **Cấp độ 5** | Hệ thống thông tin cấp độ 5 (Hệ thống thông tin quan trọng quốc gia) | Hệ thống phục vụ an ninh quốc gia, quốc phòng, năng lượng, viễn thông cốt lõi; gián đoạn đe dọa chủ quyền và an ninh quốc gia | Thủ tướng Chính phủ phê duyệt sau khi Bộ TT&TT thẩm định |

---

## 2. Prohibition of Fabricated Security Levels (SEC002)

- **Strict Boundary:** The Vietnamese legal system **DOES NOT RECOGNIZE** any security levels beyond Level 5.
- **Illegal Claims:** Advertising or asserting that a system or cloud software meets "An toàn hệ thống thông tin cấp độ 6", "cấp độ 7", or "tiêu chuẩn bảo mật cấp 8 Bộ TT&TT" constitutes false advertising and regulatory deception under **Luật Quảng cáo 2012** and **Luật An toàn thông tin mạng 2015**.

---

## 3. Pentest Reporting & System Security Assessment Requirements

When authoring a Penetration Testing Report (`Báo cáo kiểm thử xâm nhập`) or Security Dossier (`Hồ sơ đề xuất cấp độ`):

1. **Mandatory Technical Standard:** Comply with **Thông tư số 12/2022/TT-BTTTT** quy định chi tiết và hướng dẫn một số điều của Nghị định 85/2016/NĐ-CP.
2. **Evaluation Criteria:**
   - Bảo đảm an toàn thông tin theo mô hình 4 lớp (Đội ngũ tại chỗ, Tổ chức giám sát độc lập, Tổ chức đánh giá độc lập, Kết nối chia sẻ thông tin với NCSC).
   - Thiết kế an toàn mạng, an toàn máy chủ, an toàn ứng dụng, an toàn dữ liệu, và quản lý vận hành.
3. **Remediation Plan:** Every identified CVE or misconfiguration must specify:
   - Điểm đánh giá mức độ nghiêm trọng (CVSS v3.1 / CVSS v4.0);
   - Khả năng khai thác (Exploitability);
   - Biện pháp khắc phục chi tiết (Workaround & Official Vendor Patch).
