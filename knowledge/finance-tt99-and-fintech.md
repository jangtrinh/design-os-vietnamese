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
version: "3.2.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md"
    sha256: "c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290"
  - uri: "_evidence/vn-design-os-261026/sources/12-vbpl-luat-54-2019-qh14-chung-khoan.txt"
    sha256: "3bc5fc03a97453ed0e5bf6f86fb50c8ea5d57797292866a1f2237f29f452ff0e"
  - uri: "_evidence/vn-design-os-261026/sources/24-vbpl-nd-38-2018-nd-cp-dau-tu-khoi-nghiep-sang-tao.txt"
    sha256: "8a22a4d2816a1950a3f194321b93c1dd7a36b5a90961dbf6775d6c12aa494e08"
  - uri: "_evidence/vn-design-os-261026/sources/25-vbpl-luat-56-2024-qh15-sua-doi-luat-chung-khoan.txt"
    sha256: "61f028e5b33f1a27b53e5b431d337df320ab51d84a71304bb55ba4f26015daad"
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

### 3. Statutory Basis for the Guaranteed-Return Ban (`FIN001`)

The guaranteed-return ban sits in Luật Chứng khoán 2019 (54/2019/QH14) Điều 91 khoản 1, a restriction on securities companies and fund managers: no statement or guarantee to a client about an income or profit level, and no guarantee against loss. Fixed-income securities are the only exception. Điều 12 of the same Law (prohibited market acts: fraud, insider dealing, manipulation) contains no guarantee clause, so `Luật CK Đ12` alone is not the right citation for `FIN001`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/12-vbpl-luat-54-2019-qh14-chung-khoan.txt" sha256="3bc5fc03a97453ed0e5bf6f86fb50c8ea5d57797292866a1f2237f29f452ff0e" quote="Không được đưa ra nhận định hoặc bảo đảm với khách hàng về mức thu nhập hoặc lợi nhuận đạt được trên khoản đầu tư của mình hoặc bảo đảm khách hàng không bị thua lỗ, trừ trường hợp đầu tư vào chứng khoán có thu nhập cố định." -->

The statutory wording names three things to match: `bảo đảm` + `mức thu nhập` / `lợi nhuận`, and `bảo đảm khách hàng không bị thua lỗ`. Variants such as `cam kết`, `đảm bảo`, `lãi`, `lời`, `sinh lời` express the same meaning; the variant table in `knowledge/data/rule-variant-tables.json` marks which rows the statute states and which are proposed.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/12-vbpl-luat-54-2019-qh14-chung-khoan.txt" sha256="3bc5fc03a97453ed0e5bf6f86fb50c8ea5d57797292866a1f2237f29f452ff0e" quote="Không được đưa ra nhận định hoặc bảo đảm với khách hàng về mức thu nhập hoặc lợi nhuận đạt được trên khoản đầu tư của mình hoặc bảo đảm khách hàng không bị thua lỗ, trừ trường hợp đầu tư vào chứng khoán có thu nhập cố định." -->

`NĐ 38/2018/NĐ-CP`, the second basis `FIN001` cites, governs investment in innovative small and medium start-ups and start-up investment funds (Điều 1 khoản 1). Its Điều 2 khoản 4 only defines the start-up fund management company, so it is not a basis for the guaranteed-return ban.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/24-vbpl-nd-38-2018-nd-cp-dau-tu-khoi-nghiep-sang-tao.txt" sha256="8a22a4d2816a1950a3f194321b93c1dd7a36b5a90961dbf6775d6c12aa494e08" quote="Nghị định này hướng dẫn về đầu tư cho doanh nghiệp nhỏ và vừa khởi nghiệp sáng tạo; việc thành lập, tổ chức quản lý và hoạt động của quỹ đầu tư khởi nghiệp sáng tạo" -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/24-vbpl-nd-38-2018-nd-cp-dau-tu-khoi-nghiep-sang-tao.txt" sha256="8a22a4d2816a1950a3f194321b93c1dd7a36b5a90961dbf6775d6c12aa494e08" quote="4. Công ty thực hiện quản lý quỹ đầu tư khởi nghiệp sáng tạo là công ty được thành lập theo pháp luật về doanh nghiệp, có ngành, nghề quản lý quỹ đầu tư khởi nghiệp sáng tạo." -->

Luật 56/2024/QH15 amended the Securities Law from 01/01/2025. Its only change to Điều 12 is khoản 3 (market manipulation), and none of its securities items amends Điều 91. The register records Luật 56/2024 as fully out of force from 01/01/2026 without naming its replacement, so a later amendment to Điều 91 has not been checked.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/25-vbpl-luat-56-2024-qh15-sua-doi-luat-chung-khoan.txt" sha256="61f028e5b33f1a27b53e5b431d337df320ab51d84a71304bb55ba4f26015daad" quote="5. Sửa đổi, bổ sung khoản 3 Điều 12 như sau:" -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/25-vbpl-luat-56-2024-qh15-sua-doi-luat-chung-khoan.txt" sha256="61f028e5b33f1a27b53e5b431d337df320ab51d84a71304bb55ba4f26015daad" quote="effFrom=2025-01-01; effTo=2026-01-01; effStatus=Hết hiệu lực toàn bộ" -->

## Failure Modes (Mandatory)

1. **Stale Circular 200 Terminology (`FIN001`):** Labeling post-2026 ERP financial reports as `Bảng cân đối kế toán (theo Thông tư 200/2014/TT-BTC)` instead of `Báo cáo tình hình tài chính (theo Thông tư 99/2025/TT-BTC)`.
2. **Misleading "Risk-Free Savings" Bond Copy (`FIN002`):** Marketing corporate bonds or fund certificates as `Tiết kiệm linh hoạt cam kết lợi nhuận 12%/năm, an toàn tuyệt đối 100%`.
3. **Ambiguous Loan Interest Basis (`FIN003`):** Advertising `Lãi suất vay chỉ 0,8%/tháng` without disclosing whether it is calculated on original principal (`dư nợ gốc ban đầu`) or reducing balance (`dư nợ giảm dần`) and the annualized APR (`%/năm`).
