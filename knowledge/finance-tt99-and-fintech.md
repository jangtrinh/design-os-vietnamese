---
id: "finance-tt99-and-fintech"
title: "Vietnamese Corporate Accounting (Thông tư 99/2025/TT-BTC) and Banking/Fintech Compliance"
domain: "vietnamese-finance-and-accounting"
description: "Verified specification for Circular 99/2025/TT-BTC accounting terminology (superseding TT 200/2014/TT-BTC from 01/01/2026) and SBV/SSC banking, securities, and e-wallet disclosures."
when:
  - "Writing or validating Vietnamese accounting, ERP, banking, securities, insurance, or e-wallet copy"
  - "Migrating financial statements and chart of accounts from Circular 200/2014/TT-BTC to Circular 99/2025/TT-BTC"
  - "Auditing investment/savings terminology and interest-rate disclosures with --domain finance"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md"
    sha256: "c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290"
---

# Vietnamese Corporate Accounting (Thông tư 99/2025/TT-BTC) and Banking/Fintech Compliance

## Purpose

Defines the mandatory accounting terminology under Ministry of Finance Circular 99/2025/TT-BTC (effective 01/01/2026) and regulatory disclosure rules for retail banking, securities, consumer lending, and Napas VietQR payments.

## When to Use / When NOT

- **When to Use:**
  - Designing or auditing fintech apps, ERP accounting modules, financial reports, loan calculators, and investment dashboards in Vietnam.
- **When NOT to Use:**
  - Historical audit reports covering fiscal years prior to 2026 that intentionally cite legacy Circular 200/2014/TT-BTC terminology.

## Core Knowledge Content

### 1. Circular 99/2025/TT-BTC Accounting Reform (`FIN001`)

Circular 99/2025/TT-BTC issued by the Ministry of Finance on 27/10/2025 supersedes Circular 200/2014/TT-BTC for fiscal years beginning on or after 01/01/2026, officially renaming `Bảng cân đối kế toán` (Form B 01-DN) to `Báo cáo tình hình tài chính` (Statement of Financial Position) in alignment with IAS 1 / IFRS.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Circular 99/2025/TT-BTC issued by the Ministry of Finance on 27/10/2025 supersedes Circular 200/2014/TT-BTC for fiscal years beginning on or after 01/01/2026, officially renaming 'Bảng cân đối kế toán' (Form B 01-DN) to 'Báo cáo tình hình tài chính' (Statement of Financial Position) in alignment with IAS 1 / IFRS." -->

Circular 99/2025/TT-BTC introduces Account 215 (`Tài sản sinh học` / Biological Assets), Account 332 (`Phải trả cổ tức, lợi nhuận` / Dividends and Profits Payable), and Account 82112 (`Chi phí thuế TNDN bổ sung theo quy định về thuế tối thiểu toàn cầu` / Pillar Two Global Minimum Tax Expense).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Circular 99/2025/TT-BTC introduces Account 215 ('Tài sản sinh học' / Biological Assets), Account 332 ('Phải trả cổ tức, lợi nhuận' / Dividends and Profits Payable), and Account 82112 ('Chi phí thuế TNDN bổ sung theo quy định về thuế tối thiểu toàn cầu' / Pillar Two Global Minimum Tax Expense)." -->

### 2. Investment Risk and Interest Rate Disclosures (`FIN002`, `FIN003`)

In Vietnamese retail banking, securities, and e-wallet interfaces, bonds (`trái phiếu doanh nghiệp`), mutual fund certificates (`chứng chỉ quỹ`), and gold/crypto assets must never be labeled `tiền gửi tiết kiệm` (savings deposit) or `cam kết lãi suất cố định không rủi ro`, and credit copy must clearly distinguish flat nominal interest (`lãi suất trên dư nợ gốc ban đầu`) from effective reducing-balance interest (`lãi suất trên dư nợ giảm dần`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="In Vietnamese retail banking, securities, and e-wallet interfaces, bonds ('trái phiếu doanh nghiệp'), mutual fund certificates ('chứng chỉ quỹ'), and gold/crypto assets must never be labeled 'tiền gửi tiết kiệm' (savings deposit) or 'cam kết lãi suất cố định không rủi ro', and credit copy must clearly distinguish flat nominal interest ('lãi suất trên dư nợ gốc ban đầu') from effective reducing-balance interest ('lãi suất trên dư nợ giảm dần')." -->

## Failure Modes (Mandatory)

1. **Stale Circular 200 Terminology (`FIN001`):** Labeling post-2026 ERP financial reports as `Bảng cân đối kế toán (theo Thông tư 200/2014/TT-BTC)` instead of `Báo cáo tình hình tài chính (theo Thông tư 99/2025/TT-BTC)`.
2. **Misleading "Risk-Free Savings" Bond Copy (`FIN002`):** Marketing corporate bonds or fund certificates as `Tiết kiệm linh hoạt cam kết lợi nhuận 12%/năm, an toàn tuyệt đối 100%`.
3. **Ambiguous Loan Interest Basis (`FIN003`):** Advertising `Lãi suất vay chỉ 0,8%/tháng` without disclosing whether it is calculated on original principal (`dư nợ gốc ban đầu`) or reducing balance (`dư nợ giảm dần`) and the annualized APR (`%/năm`).
