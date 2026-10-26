<!-- vlc-disable: all -->

# Financial Statement Formatting & E-Invoice Architecture (`design-os-vietnamese`)

This document details the numeric formatting, table structure, number-to-words conversion rules, and statutory electronic invoice layout required by Vietnamese tax and accounting regulations.

---

## 1. Unit of Measurement Header (`Đơn vị tính` — `FIN005`)

Under Vietnamese accounting standards, every financial table must explicitly state its currency and magnitude unit in the upper right header, directly beneath the statement title:

- Standard declarations:
  - `Đơn vị tính: triệu đồng` (Units in millions of VND)
  - `Đơn vị tính: tỷ đồng` (Units in billions of VND)
  - `Đơn vị tính: VND` / `Đơn vị tính: đồng` (Units in standard VND)
  - `Đơn vị tính: USD` (For authorized foreign currency reporting entities)

### Table Placement Pattern
```markdown
# BÁO CÁO TÌNH HÌNH TÀI CHÍNH
Tại ngày 31 tháng 12 năm 2026

*Đơn vị tính: triệu đồng*

| Mã số | Thuyết minh | Chỉ tiêu | Số cuối năm | Số đầu năm |
|---|---|---|---|---|
| 100 | V.01 | **A. TÀI SẢN NGẮN HẠN** | **150.250** | **120.800** |
```

If a table containing financial figures lacks the `Đơn vị tính` declaration, `validate_copy.py` emits `FIN005`. Readers cannot discern whether `150.250` denotes 150.250 VND, 150.250.000 VND (triệu đồng), or 150.250.000.000 VND (tỷ đồng).

---

## 2. Parenthesised Negative Numbers (`FIN006`)

Financial statements and accounting ledgers in Vietnam represent negative balances, deductions, contra-asset provisions, and operational deficits in **parentheses**, never with a raw mathematical minus sign:

| Accounting Item | ❌ Wrong (ASCII Minus) | ✅ Correct (Accounting Parentheses) |
|---|---|---|
| Lỗ ròng sau thuế | `-250.000.000 ₫` | `(250.000.000) ₫` |
| Giá trị hao mòn lũy kế TSCĐ | `-1.450.000` | `(1.450.000)` |
| Dự phòng nợ phải thu khó đòi | `-85.000` | `(85.000)` |
| Các khoản giảm trừ doanh thu | `-12.500.000 ₫` | `(12.500.000) ₫` |
| Lưu chuyển tiền thuần từ HĐĐT âm | `-540.000` | `(540.000)` |

### Why ASCII Minus Fails in Finance
1. **Auditing Standards:** Vietnamese Accounting Standards (VAS) and Circular 99/2025 require parenthesised formatting to eliminate visual confusion with table divider hyphens (`---`) or transaction reference codes.
2. **OCR & Banking Parsing:** Automated bank reconciliation tools and tax portal OCR engines parse `-` as an invalid delimiter or text hyphen, causing automated filing rejection.

---

## 3. Vietnamese Number-to-Words Orthography (`Số tiền bằng chữ`)

All payment vouchers, tax invoices, checks, promissory notes, and banking withdrawal slips must include the monetary amount written out in Vietnamese words (`Số tiền bằng chữ`).

### Mandatory Orthographic Rules
1. **Capitalization:** Only capitalize the initial letter of the full phrase, or initial letters of proper nouns. End with `đồng` or `đồng chẵn`.
2. **Numbers ending in 1 (`mốt` vs `một`):**
   - For numbers from 21 to 91, write `mốt`: `hai mươi mốt`, `ba mươi mốt`, `chín mươi mốt`.
   - For 01 or 11, write `một`: `linh một` / `lẻ một`, `mười một`.
3. **Numbers ending in 4 (`tư` vs `bốn`):**
   - Numbers 24, 34, 44... can be written as `hai mươi tư` or `hai mươi bốn`. In formal banking, `hai mươi tư` is traditional.
   - For 14, write `mười bốn` (never `mười tư`).
   - For 04, write `linh bốn` or `lẻ bốn`.
4. **Numbers ending in 5 (`lăm` vs `năm`):**
   - For numbers greater than 10 where the unit is 5, always write `lăm`: `mười lăm`, `hai mươi lăm`, `bốn mươi lăm`.
   - Never write `mười năm` (which means "ten years", a completely different word).
5. **Zero hundreds (`không trăm`):**
   - In numbers like 1.050.000, write `Một triệu không trăm năm mươi nghìn đồng`. Never omit the `không trăm`.
6. **Zero tens (`linh` vs `lẻ`):**
   - Northern administrative standard prefers `linh`: `Một triệu không trăm linh năm nghìn đồng`.
   - Southern colloquial usage often uses `lẻ`: both are legally valid, but maintain consistency within the document.
7. **`Nghìn` vs `Ngàn`:**
   - Both are legally recognized. Standard central administrative texts (Bộ Tài chính) use `nghìn`. Southern commercial practice frequently uses `ngàn`.

### Canonical Worked Examples
- `15.350.000 ₫` → `Mười lăm triệu ba trăm năm mươi nghìn đồng.`
- `21.005.021 ₫` → `Hai mươi mốt triệu không trăm linh năm nghìn không trăm hai mươi mốt đồng.`
- `105.000.000 ₫` → `Một trăm linh năm triệu đồng chẵn.`
- `1.000.000.000 ₫` → `Một tỷ đồng chẵn.`

---

## 4. Statutory Electronic Invoice Architecture (NĐ 123/2020 & NĐ 70/2025)

Under **Nghị định 123/2020/NĐ-CP** (as amended by **Nghị định 70/2025/NĐ-CP**), an electronic value-added tax invoice (`Hóa đơn giá trị gia tăng điện tử`) must contain all mandatory metadata fields:

### Statutory Field Checklist (`FIN007`)
1. **Invoice Identification:**
   - `Tên hóa đơn`: HÓA ĐƠN GIÁ TRỊ GIA TĂNG (hoặc HÓA ĐƠN BÁN HÀNG)
   - `Ký hiệu mẫu số hóa đơn`: e.g., `1` (Hóa đơn GTGT)
   - `Ký hiệu hóa đơn`: e.g., `C26TAA` (`C` = có mã của cơ quan thuế, `26` = năm 2026, `T` = hóa đơn điện tử do doanh nghiệp đăng ký, `AA` = ký hiệu quản lý nội bộ)
   - `Số hóa đơn`: 8 digits (e.g., `00000001` to `99999999`)
   - `Ngày, tháng, năm lập hóa đơn`
2. **Seller Information (`Bên bán`):**
   - `Tên người bán` (Company Legal Name)
   - `Địa chỉ người bán`
   - `Mã số thuế người bán` (`MST` — mandatory!)
   - `Điện thoại / Email / Website`
3. **Buyer Information (`Bên mua`):**
   - `Tên người mua` / `Tên đơn vị`
   - `Địa chỉ người mua`
   - `Mã số thuế người mua` (`MST` — mandatory for enterprise B2B sales)
   - `Hình thức thanh toán` (e.g., `TM/CK` - Tiền mặt / Chuyển khoản)
4. **Goods and Services Breakdown:**
   - Table columns: `STT`, `Tên hàng hóa, dịch vụ`, `Đơn vị tính`, `Số lượng`, `Đơn giá`, `Thành tiền`
5. **Tax & Total Calculations:**
   - `Cộng tiền hàng` (Subtotal before tax)
   - `Thuế suất thuế GTGT`: Standard rates `5%`, `8%`, `10%`, or `KCT` (không chịu thuế), `0%`
   - `Tiền thuế GTGT` (Total VAT amount — mandatory!)
   - `Tổng cộng tiền thanh toán` (Total payable amount)
   - `Số tiền viết bằng chữ` (Number written in Vietnamese words)
6. **Authentication & Authority:**
   - `Chữ ký số, chữ ký điện tử của người bán` (Timestamped digital signature)
   - `Mã của cơ quan thuế` (For invoices with tax authority verification code)
