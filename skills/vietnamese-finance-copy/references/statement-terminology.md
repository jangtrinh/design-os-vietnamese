<!-- vlc-disable: all -->

# Financial Statement Terminology & Classification (`design-os-vietnamese`)

This document defines official financial statement nomenclature and line-item vocabulary in Vietnam.
Under **Thông tư 99/2025/TT-BTC** (replacing Thông tư 200/2014/TT-BTC effective **01/01/2026**), corporate financial statements undergo statutory renaming. Any document or software model outputting pre-2026 terminology fails statutory compliance.

---

## 1. Statutory Statement Names (Forms B01 through B09)

Vietnamese corporate accounting requires four core components in a complete financial statement package (`Báo cáo tài chính - BCTC`):

| Form Code | Official Vietnamese Title (TT 99/2025) | Pre-2026 Title (TT 200/2014) | English Accounting Equivalent |
|---|---|---|---|
| **Mẫu B01-DN** | `Báo cáo tình hình tài chính` | `Bảng cân đối kế toán` | Statement of Financial Position (Balance Sheet) |
| **Mẫu B02-DN** | `Báo cáo kết quả hoạt động kinh doanh` | `Báo cáo kết quả hoạt động kinh doanh` | Income Statement / Statement of Comprehensive Income |
| **Mẫu B03-DN** | `Báo cáo lưu chuyển tiền tệ` | `Báo cáo lưu chuyển tiền tệ` | Statement of Cash Flows |
| **Mẫu B09-DN** | `Bản thuyết minh báo cáo tài chính` | `Bản thuyết minh báo cáo tài chính` | Notes to the Financial Statements |

> [!CAUTION]
> Using `Bảng cân đối kế toán` for financial statements dated 2026 onwards is an active regulatory defect. `validate_copy.py` flags this as `CAL001` at `error` severity.

---

## 2. Standard Tax Abbreviations & Identity Codes

Statutory tax correspondence, financial reports, and corporate governance documents in Vietnam use standardized Vietnamese acronyms. English loan-acronyms (`VAT`, `CIT`, `PIT`, `TIN`) are non-compliant in official Vietnamese filings.

| Vietnamese Statutory Term | Mandatory Abbreviation | English Equivalent | Prohibited Calque Acronyms |
|---|---|---|---|
| Thuế giá trị gia tăng | `thuế GTGT` | Value Added Tax (VAT) | ❌ `thuế VAT` |
| Thuế thu nhập doanh nghiệp | `thuế TNDN` | Corporate Income Tax (CIT) | ❌ `thuế CIT` |
| Thuế thu nhập cá nhân | `thuế TNCN` | Personal Income Tax (PIT) | ❌ `thuế PIT` |
| Mã số thuế | `MST` | Tax Identification Number | ❌ `TIN`, `Tax Code` |
| Bảo hiểm xã hội | `BHXH` | Social Insurance | ❌ `SI` |
| Bảo hiểm y tế | `BHYT` | Health Insurance | ❌ `HI` |
| Bảo hiểm thất nghiệp | `BHTN` | Unemployment Insurance | ❌ `UI` |
| Kinh phí công đoàn | `KPCĐ` | Trade Union Funds | ❌ `TUF` |

---

## 3. Reporting Periods & Quarter Orthography

Vietnamese financial reporting mandates Roman numerals for fiscal quarters. Arabic numerals or western abbreviations (`Q1`, `Q2`) are unacceptable in formal statements:

- ✅ `Quý I/2026`, `Quý II/2026`, `Quý III/2026`, `Quý IV/2026`
- ✅ `Báo cáo tài chính bán niên 2026` (Semi-annual Financial Report)
- ✅ `Năm tài chính kết thúc ngày 31/12/2026` (Fiscal Year ended December 31, 2026)
- ❌ `Q1 2026`, `Q4 2026`, `quý 1`, `quý 4`

---

## 4. Primary Line Items: Báo cáo tình hình tài chính (Mẫu B01-DN)

### Tài sản (Assets)
1. **A - TÀI SẢN NGẮN HẠN (Current Assets):**
   - `Tiền và các khoản tương đương tiền` (Cash and cash equivalents)
   - `Đầu tư tài chính ngắn hạn` (Short-term financial investments)
   - `Các khoản phải thu ngắn hạn` (Short-term receivables)
     - `Phải thu ngắn hạn của khách hàng` (Short-term trade receivables)
     - `Trả trước cho người bán ngắn hạn` (Short-term prepayments to suppliers)
     - `Phải thu ngắn hạn khác` (Other short-term receivables)
     - `Dự phòng phải thu ngắn hạn khó đòi` (Provision for doubtful short-term receivables - *parenthesised negative*)
   - `Hàng tồn kho` (Inventories)
     - `Dự phòng giảm giá hàng tồn kho` (Provision for devaluation of inventories - *parenthesised negative*)
   - `Tài sản ngắn hạn khác` (Other current assets)
2. **B - TÀI SẢN DÀI HẠN (Non-current Assets):**
   - `Các khoản phải thu dài hạn` (Long-term receivables)
   - `Tài sản cố định` (Fixed assets)
     - `Tài sản cố định hữu hình` (Tangible fixed assets)
       - `Nguyên giá` (Historical cost)
       - `Giá trị hao mòn lũy kế` (Accumulated depreciation - *parenthesised negative*)
     - `Tài sản cố định vô hình` (Intangible fixed assets)
   - `Bất động sản đầu tư` (Investment properties)
   - `Tài sản dở dang dài hạn` (Long-term assets in progress)
   - `Đầu tư tài chính dài hạn` (Long-term financial investments)
   - `Tài sản dài hạn khác` (Other long-term assets)

### Nguồn vốn (Equity & Liabilities)
1. **C - NỢ PHẢI TRẢ (Liabilities):**
   - `Nợ ngắn hạn` (Current liabilities)
     - `Phải trả người bán ngắn hạn` (Short-term trade payables)
     - `Người mua trả tiền trước ngắn hạn` (Short-term advances from customers)
     - `Thuế và các khoản phải nộp Nhà nước` (Taxes and amounts payable to the State budget)
     - `Phải trả người lao động` (Payables to employees)
     - `Chi phí phải trả ngắn hạn` (Short-term accrued expenses)
     - `Vay và nợ thuê tài chính ngắn hạn` (Short-term borrowings and finance lease liabilities)
   - `Nợ dài hạn` (Non-current liabilities)
     - `Phải trả dài hạn người bán` (Long-term trade payables)
     - `Vay và nợ thuê tài chính dài hạn` (Long-term borrowings and finance lease liabilities)
2. **D - VỐN CHỦ SỞ HỮU (Owner's Equity):**
   - `Vốn góp của chủ sở hữu` (Contributed capital)
   - `Thặng dư vốn cổ phần` (Share premium)
   - `Cổ phiếu quỹ` (Treasury shares - *parenthesised negative*)
   - `Các quỹ thuộc vốn chủ sở hữu` (Funds belonging to owner's equity)
   - `Lợi nhuận sau thuế chưa phân phối` (Undistributed earnings after tax)
     - `Lợi nhuận sau thuế chưa phân phối lũy kế đến cuối kỳ trước`
     - `Lợi nhuận sau thuế chưa phân phối kỳ này`

---

## 5. Primary Line Items: Báo cáo kết quả hoạt động kinh doanh (Mẫu B02-DN)

1. `Doanh thu bán hàng và cung cấp dịch vụ` (Gross revenue from goods sold and services rendered)
2. `Các khoản giảm trừ doanh thu` (Revenue deductions: chiết khấu thương mại, giảm giá hàng bán, hàng bán bị trả lại)
3. `Doanh thu thuần về bán hàng và cung cấp dịch vụ` (Net revenue)
4. `Giá vốn hàng bán` (Cost of goods sold)
5. `Lợi nhuận gộp về bán hàng và cung cấp dịch vụ` (Gross profit)
6. `Doanh thu hoạt động tài chính` (Financial income)
7. `Chi phí tài chính` (Financial expenses)
   - *Trong đó:* `Chi phí lãi vay` (Interest expense)
8. `Chi phí bán hàng` (Selling expenses)
9. `Chi phí quản lý doanh nghiệp` (General and administrative expenses)
10. `Lợi nhuận thuần từ hoạt động kinh doanh` (Net operating profit)
11. `Thu nhập khác` (Other income)
12. `Chi phí khác` (Other expenses)
13. `Lợi nhuận khác` (Other profit)
14. `Tổng lợi nhuận kế toán trước thuế` (Total accounting profit before tax)
15. `Chi phí thuế thu nhập doanh nghiệp hiện hành` (Current corporate income tax expense)
16. `Chi phí thuế thu nhập doanh nghiệp hoãn lại` (Deferred corporate income tax expense)
17. `Lợi nhuận sau thuế thu nhập doanh nghiệp` (Net profit after corporate income tax)
18. `Lãi cơ bản trên cổ phiếu` (Basic earnings per share - EPS)
19. `Lãi suy giảm trên cổ phiếu` (Diluted earnings per share)

---

## 6. Audit & Signature Section Requirements

Formal financial statements in Vietnam must conclude with four distinct corporate signatories:
1. `Người lập biểu` (Preparer - ký, ghi rõ họ tên)
2. `Kế toán trưởng` (Chief Accountant - ký, ghi rõ họ tên)
3. `Giám đốc` / `Tổng Giám đốc` / `Người đại diện theo pháp luật` (Legal Representative / CEO - ký, ghi rõ họ tên, đóng dấu pháp nhân)
4. Date notation: `Lập, ngày ... tháng ... năm ...` (never standard slash date like `2026/03/31` in signature blocks).
