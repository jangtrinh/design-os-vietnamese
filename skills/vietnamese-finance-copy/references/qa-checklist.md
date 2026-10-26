<!-- vlc-disable: all -->

# Financial Copywriting & Regulatory QA Checklist (`design-os-vietnamese`)

Before releasing financial statements, investor updates, credit marketing campaigns, electronic invoices, or FinTech payment microcopy, perform this exhaustive quality assurance audit.

---

## 1. Statutory Accounting & Statement Hygiene

- [ ] **1. Statement Title Check (Thông tư 99/2025/TT-BTC):**
  - Is the balance sheet titled `Báo cáo tình hình tài chính`?
  - Has all deprecated `Bảng cân đối kế toán` phrasing been eliminated for post-2025 periods?
- [ ] **2. Four Core Forms Verified:**
  - `Báo cáo tình hình tài chính` (Mẫu B01-DN)
  - `Báo cáo kết quả hoạt động kinh doanh` (Mẫu B02-DN)
  - `Báo cáo lưu chuyển tiền tệ` (Mẫu B03-DN)
  - `Bản thuyết minh báo cáo tài chính` (Mẫu B09-DN)
- [ ] **3. Reporting Period Formatting:**
  - Are fiscal quarters formatted with Roman numerals (`Quý I`, `Quý II`, `Quý III`, `Quý IV`)?
  - Are slash quarters (`Q1`, `Q4`) or Arabic notations (`quý 1`) absent?
- [ ] **4. Unit of Measurement (`Đơn vị tính` — `FIN005`):**
  - Does every financial table feature an explicit `Đơn vị tính: triệu đồng` (or `tỷ đồng`, `VND`) in its header?
- [ ] **5. Parenthesised Negatives (`FIN006`):**
  - Are all negative figures, accumulated depreciation, contra-asset allowances, and losses enclosed in parentheses (e.g. `(1.250.000) ₫`) rather than ASCII minuses (`-1.250.000`)?
- [ ] **6. Number-to-Words Orthography (`Số tiền bằng chữ`):**
  - Is the amount in words fully written out with correct orthography (`mười lăm`, `hai mươi mốt`, `không trăm linh năm`)?
  - Does the text end with `đồng` or `đồng chẵn`?

---

## 2. Tax & Electronic Invoice Verification (NĐ 123/2020 & NĐ 70/2025)

- [ ] **7. Statutory Tax Nomenclature:**
  - Are Vietnamese tax acronyms used exclusively (`thuế GTGT`, `thuế TNDN`, `thuế TNCN`, `MST`)?
  - Are foreign acronyms (`VAT`, `CIT`, `PIT`, `TIN`) removed from statutory prose?
- [ ] **8. Mandatory E-Invoice Fields (`FIN007`):**
  - Is the Seller's legal name, address, and `MST` present?
  - Is the Buyer's legal name, address, and `MST` present (for B2B transactions)?
  - Is the VAT treatment (`thuế suất thuế GTGT` and `tiền thuế GTGT`) clearly separated?
  - Are invoice template number, serial number, and sequential invoice number present?
- [ ] **9. Tax Code Integrity:**
  - Are seller and buyer MSTs verified as valid 10-digit or 13-digit numbers in the national tax registry?

---

## 3. Financial Promotion, Lending, & Insurance Compliance

- [ ] **10. Zero Guaranteed-Return Phrasing (`FIN001`):**
  - Are all claims of `cam kết lợi nhuận`, `đảm bảo sinh lời`, `bảo toàn vốn`, `đầu tư không rủi ro`, or `chắc chắn có lãi` completely eradicated?
  - Has copy been replaced with `lợi nhuận kỳ vọng` accompanied by an explicit investment risk disclaimer?
- [ ] **11. Consumer Credit & 0% Rate Transparency (`FIN002`):**
  - If a promotional `0%` rate or `trả góp 0%` is advertised, does the copy visibly disclose the conversion fee (`phí chuyển đổi`), total repayment cost (`tổng chi phí / tổng số tiền phải trả`), and effective annual percentage rate (`lãi suất thực tế`)?
- [ ] **12. Investment-Linked Insurance Disclaimers (`FIN008`):**
  - Does unit-linked (ILP) or universal life (UL) copy explicitly state that it is an insurance product, not a bank savings deposit (`không phải là tiền gửi tiết kiệm ngân hàng`)?
  - Does copy explicitly state that the policyholder bears all investment risk (`bên mua bảo hiểm chịu mọi rủi ro đầu tư`)?
- [ ] **13. Digital Assets Regulatory Boundaries:**
  - Is there an explicit disclaimer confirming digital assets are not legal tender in Vietnam (`không phải là phương tiện thanh toán hợp pháp`)?
- [ ] **14. Unlicensed Securities / Fund Solicitation:**
  - Are offshore trading platforms and unregulated forex/crypto brokers unendorsed?
- [ ] **15. Private Placement Corporate Bond Compliance:**
  - Is private bond marketing strictly restricted to certified professional securities investors under Nghị định 65/2022/NĐ-CP?

---

## 4. FinTech UX, eKYC, & Security Thresholds

- [ ] **16. High-Value Transfer Biometrics (`FIN009`):**
  - For transfers exceeding 10.000.000 ₫ per transaction or daily totals exceeding 20.000.000 ₫, is the facial biometric authentication step (`xác thực sinh trắc học khuôn mặt`) explicitly announced to the user under Quyết định 2345/QĐ-NHNN?
- [ ] **17. NFC CCCD Chip Guidance:**
  - Does eKYC onboarding provide explicit antenna placement instructions for iOS (near camera) and Android (center back)?
- [ ] **18. Foreign Exchange Control (Pháp lệnh Ngoại hối):**
  - Are all domestic transactions, price quotations, and invoices quoted exclusively in Vietnamese Đồng (`VNĐ`), without unauthorized foreign currency indexing?
- [ ] **19. Register Consistency (`finance-formal`):**
  - Is the customer addressed with dignity as `Quý khách` throughout the transactional flow?
  - Is casual second-person address (`bạn`, `mình`, `cả nhà`) completely absent from legal and money screens?
- [ ] **20. Automated Linter Gate:**
  - Has the copy passed `validate_copy.py` with `--strict` enabled and zero errors?

---

## 5. Document Archiving & Statutory Record-Keeping (Luật Kế toán)

- [ ] **21. Minimum Archival Periods:**
  - Are electronic invoices and supporting vouchers scheduled for 10-year statutory archiving under Article 41 of the Accounting Law?
  - Are audit trails, digital signatures, and eKYC biometric verification logs cryptographically preserved for compliance audits?

---

## 6. Formal Corporate Sign-Off

Before publishing financial copy, formal sign-off must be recorded:
- **Kế toán trưởng / Giám đốc Tài chính:** Họ và tên, Ngày ký, Xác nhận tính chính xác của số liệu kế toán và biểu thuế.
- **Phòng Pháp chế & Tuân thủ:** Họ và tên, Ngày ký, Xác nhận tuân thủ Luật Chứng khoán, Luật Quảng cáo, và các Thông tư chuyên ngành.
- **Giám đốc Sản phẩm FinTech:** Họ và tên, Ngày ký, Xác nhận tuân thủ luồng bảo mật sinh trắc học QĐ 2345.
