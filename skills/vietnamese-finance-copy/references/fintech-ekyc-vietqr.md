<!-- vlc-disable: all -->

# FinTech UX, VietQR Standards, & Biometric Step-Up (`design-os-vietnamese`)

This reference provides production-grade UI microcopy, field definitions, and error handling for Vietnamese FinTech applications, instant interbank payment rails (VietQR / NAPAS 247), citizen eKYC NFC scanning, and biometric step-up flows under **Quyết định 2345/QĐ-NHNN**.

---

## 1. VietQR & NAPAS 247 Instant Transfer Microcopy

Vietnam's national payment switch (NAPAS) and the VietQR standard standardize payment fields across commercial banking applications and digital wallets.

### Standard Field Nomenclature
| UI Element | Standard Vietnamese Microcopy | English Purpose | Guidance |
|---|---|---|---|
| Recipient Bank | `Ngân hàng thụ hưởng` | Beneficiary Bank | Display bank brand logo + official short name (e.g. `Vietcombank`, `Techcombank`, `MBBank`) |
| Account Number | `Số tài khoản` / `Số thẻ` | Account or Card Number | Format with clean spacing or auto-detection |
| Beneficiary Name | `Tên người thụ hưởng` | Account Holder Name | Auto-retrieved via NAPAS API; display in UPPERCASE without diacritics (e.g. `NGUYEN VAN A`) |
| Transfer Amount | `Số tiền chuyển` | Amount to transfer | Real-time Vietnamese number-to-words helper below the input field (e.g. `5.000.000 ₫` → `Năm triệu đồng`) |
| Transaction Note | `Nội dung chuyển tiền` | Transfer Message / Note | Enforce character limits (max 50 chars); strip accented diacritics or special characters |
| Fee Payer | `Phí chuyển tiền` | Transaction Fee | Typically `Miễn phí` (Free) on modern digital retail rails |

### Transaction Note Sanitization Copy
- Helper note: `"Nội dung không chứa ký tự đặc biệt (@, #, $, %) hoặc các từ nhạy cảm liên quan đến tiền ảo, cờ bạc."`
- Empty state: `"Nhập nội dung chuyển tiền (ví dụ: Nguyen Van A chuyen tien)"`

### VietQR Technical Field Architecture (EMVCo Compatible)
VietQR encodes payment data into an interoperable QR standard governed by NAPAS:
- **Tag 00 (Payload Format Indicator):** Constant value `01`.
- **Tag 01 (Point of Initiation Method):** `11` (Static QR) or `12` (Dynamic QR with embedded amount).
- **Tag 26 (Merchant Account Information - NAPAS):**
  - Sub-tag `00`: Globally unique identifier (`A000000727` - NAPAS).
  - Sub-tag `01`: Beneficiary Organization (`9704xx` Bank Identification Number - BIN code + Account Number).
  - Sub-tag `02`: Service Code (`QRIBFTTA` - Transfer to Account; `QRIBFTTC` - Transfer to Card).
- **Tag 53 (Transaction Currency):** `704` (ISO 4217 code for Vietnamese Đồng - VNĐ).
- **Tag 54 (Transaction Amount):** Formatted integer or decimal string without grouping symbols in payload.
- **Tag 62 (Additional Data Field):** Purpose of transaction and invoice reference code.

---

## 2. Chip-Enabled Citizen ID (CCCD Gắn Chip) NFC Scanning UX

Digital banks, brokerages, and payment providers in Vietnam verify user identity via the embedded ICAO 9303 contactless chip inside citizen ID cards (CCCD gắn chip). Scanning this chip requires precise hardware positioning guidance.

### Step-by-Step User Prompts

#### Step 1: Preparation & Positioning
```markdown
### Quét chip trên Căn cước công dân
1. Chuẩn bị thẻ CCCD gắn chip (12 số) chính chủ còn hiệu lực.
2. Tháo ốp lưng kim loại hoặc ốp dày của điện thoại để tránh cản trở sóng NFC.
3. Bật kết nối NFC trong phần Cài đặt thiết bị (đối với điện thoại Android).
```

#### Step 2: Device-Specific Antenna Guidance
- **For iPhone (iOS):**
  `"Áp phần chip kim loại (ở mặt sau thẻ CCCD) vào khu vực đỉnh máy, cạnh camera sau của iPhone. Giữ cố định và không di chuyển trong 3–5 giây cho đến khi có rung báo hiệu."`
- **For Android Devices:**
  `"Áp mặt sau thẻ CCCD vào chính giữa lưng điện thoại (vị trí ăng-ten NFC). Giữ yên thiết bị và thẻ cho đến khi màn hình hiển thị thông báo đọc chip thành công."`

#### Step 3: Scanning Feedback States
- **Reading in progress:** `"Đang đọc dữ liệu từ chip CCCD... Vui lòng giữ yên thẻ."`
- **Success state:** `"Xác thực chip CCCD thành công! Thông tin cá nhân đã được đồng bộ hóa với Bộ Công an."`

#### Step 4: Troubleshooting & Error Recovery Microcopy
| Failure Mode | User-Facing Microcopy | Recovery Action |
|---|---|---|
| Card moved too early | `"Mất kết nối NFC. Vui lòng giữ yên thẻ CCCD áp sát lưng máy trong suốt quá trình đọc."` | Retry button: `Thử lại` |
| NFC disabled | `"Chưa bật tính năng NFC trên thiết bị. Quý khách vui lòng vào Cài đặt để kích hoạt NFC."` | Deep link CTA: `Mở Cài đặt NFC` |
| Chip not detected | `"Không tìm thấy chip CCCD. Hãy thử xê dịch nhẹ thẻ lên xuống khoảng 1 cm quanh cụm camera."` | Interactive guide: `Xem hướng dẫn chi tiết` |
| Metal obstruction | `"Tín hiệu NFC bị cản trở. Quý khách vui lòng tháo ốp lưng điện thoại và quét lại trên bề mặt phẳng."` | Visual tutorial illustration |
| Expired card | `"Thẻ CCCD đã hết hạn sử dụng. Quý khách vui lòng làm mới thẻ tại cơ quan Công an."` | Support link |
| Chip data mismatch | `"Thông tin đọc từ chip không trùng khớp với ảnh chụp CCCD. Vui lòng chụp lại rõ nét cả 2 mặt thẻ."` | Re-capture photo flow |

---

## 3. Biometric Step-Up Authentication (Quyết định 2345/QĐ-NHNN — `FIN009`)

Effective **01/07/2024**, State Bank of Vietnam Directive **Quyết định 2345/QĐ-NHNN** mandates biometric authentication (facial recognition matching biometric data stored in CCCD chip or VNeID Level 2) for high-value banking and wallet transactions:

### Statutory Trigger Thresholds
1. **Single Transaction Threshold:** Any transfer exceeding **10.000.000 ₫ per transaction**.
2. **Daily Cumulative Threshold:** Any cumulative transfer exceeding **20.000.000 ₫ in a single day**.
3. **First-time Device / Reset Login:** Changing mobile device, re-installing app, or resetting login credentials.

### Production UI Modal Copy (`FIN009`)

```markdown
### Xác thực sinh trắc học khuôn mặt
Theo Quyết định 2345/QĐ-NHNN của Ngân hàng Nhà nước, giao dịch chuyển khoản trên 10.000.000 ₫ (hoặc tổng giao dịch trong ngày vượt 20.000.000 ₫) cần được xác thực bằng sinh trắc học khuôn mặt.

- Số tiền chuyển: 15.000.000 ₫
- Phương thức xác thực: Nhận diện khuôn mặt khớp với dữ liệu CCCD gắn chip

[Nút chính]: Quét khuôn mặt để tiếp tục
[Nút phụ]: Hủy giao dịch
```

### Camera Liveness Guidance
- `"Đưa khuôn mặt vào trong khung hình elip."`
- `"Giữ khuôn mặt thẳng, không đeo kính râm hoặc khẩu trang, đảm bảo môi trường đủ ánh sáng."`
- `"Chớp mắt từ từ và quay mặt nhẹ sang phải theo hướng dẫn."`
- `"Xác thực sinh trắc học thành công. Đang tiến hành thực hiện giao dịch chuyển tiền."`

If a transaction UI or documentation describes transfers exceeding 10.000.000 ₫ or daily limits over 20.000.000 ₫ without specifying the biometric authentication requirement (`sinh trắc học` / `khuôn mặt` / `CCCD gắn chip`), `validate_copy.py` emits `FIN009`.

---

## 4. NAPAS 247 Instant Transfer Error Handling & Recovery States

When an instant interbank transaction encounters payment network delays or account discrepancies, clear user-facing microcopy prevents duplicate transfers and customer panic:

| Payment Gateway Error | Vietnamese System Error Microcopy | Recovery Action & User Advice |
|---|---|---|
| Beneficiary account inactive | `"Tài khoản thụ hưởng đang bị tạm khóa hoặc không tồn tại. Quý khách vui lòng kiểm tra lại thông tin."` | Action: `Kiểm tra lại số tài khoản` |
| Interbank gateway timeout | `"Giao dịch đang được xử lý bởi ngân hàng thụ hưởng. Quý khách vui lòng không thực hiện lại giao dịch để tránh trừ tiền hai lần."` | Action: `Xem lịch sử giao dịch` |
| Exceeded daily limit | `"Giao dịch vượt quá hạn mức thanh toán trong ngày (20.000.000 ₫). Quý khách vui lòng xác thực sinh trắc học để nâng hạn mức."` | Action: `Cập nhật sinh trắc học` |
| Insufficient balance | `"Số dư khả dụng trong tài khoản không đủ để thực hiện giao dịch. Vui lòng nạp thêm tiền và thử lại."` | Action: `Nạp tiền vào tài khoản` |
| Maintenance window | `"Hệ thống chuyển khoản liên ngân hàng đang bảo trì định kỳ. Quý khách vui lòng thử lại sau 30 phút."` | Action: `Thử lại sau` |

---

## 5. VNeID Level 2 Authentication Handshake Guidance

For users authenticating via the National Electronic Identification application (VNeID Mức 2):
- **App switch prompt:** `"Ứng dụng sẽ tự động chuyển sang VNeID để xác thực định danh điện tử. Vui lòng mở VNeID và xác nhận bằng mã khóa bảo mật."`
- **Return callback prompt:** `"Xác thực VNeID Mức 2 thành công! Hệ thống đang quay lại ứng dụng ngân hàng để hoàn tất đăng ký."`
- **Timeout warning:** `"Hết thời gian xác thực trên VNeID. Quý khách vui lòng thực hiện lại từ đầu."`
