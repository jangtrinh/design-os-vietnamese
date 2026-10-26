---
name: vietnamese-finance-copy
description: Writes, localizes, and audits native-quality Vietnamese (vi-VN) financial, banking, accounting, and FinTech communications. Enforces statutory financial statement terminology under Thông tư 99/2025/TT-BTC (mandatory rename of Bảng cân đối kế toán to Báo cáo tình hình tài chính from 01/01/2026), electronic invoice (hóa đơn điện tử) field requirements and tax formatting under Nghị định 123/2020/NĐ-CP and Nghị định 70/2025/NĐ-CP (MST, thuế GTGT, số tiền bằng chữ), consumer lending and BNPL interest transparency under Thông tư 43/2016/TT-NHNN and Thông tư 18/2019/TT-NHNN (explicit fee schedule and total repayment cost for promotional 0% rates), securities solicitation restrictions under Luật Chứng khoán 2019 and Nghị định 38/2018/NĐ-CP (strict prohibition of guaranteed-return claims), investment-linked insurance disclaimers under Thông tư 67/2023/TT-BTC Điều 53 (mandating policyholder risk acknowledgment and non-deposit disclosure), digital asset regulatory parameters under Nghị quyết 05/2025/NQ-CP and Luật 71/2025, and FinTech payment microcopy (VietQR / NAPAS 247 instant interbank transfers, chip-based CCCD NFC scanning UX, and Quyết định 2345/QĐ-NHNN biometric authentication step-up rules for transactions over 10.000.000 ₫).
license: MIT
metadata:
  version: "2.0.0"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Finance Copywriting & Regulatory Compliance (`vietnamese-finance-copy`)

In Vietnamese finance, copywriting errors carry **statutory, civil, and criminal liability** rather than mere aesthetic awkwardness. Writing an outdated statement title invalidates a public disclosure filing; writing a casual marketing slogan like `Cam kết sinh lời 12%/năm` breaches securities law; and omitting biometric verification copy on high-value transfers violates State Bank of Vietnam security directives.

This skill equips engineers, product managers, and copywriters with authoritative, verified Vietnamese financial phrasing, accounting structures, tax nomenclature, and FinTech UX copy aligned with current legislation.

---

## 1. Register & Sociolinguistic Etiquette

Finance communication in Vietnam operates under strict sociolinguistic conventions:

| Context / Surface | Register | Reader Address (`Hô`) | Speaker (`Xưng`) | Notes |
|---|---|---|---|---|
| BCTC, disclosures, tax filings, legal policies | `finance-formal` | *(impersonal third-person)* | `Doanh nghiệp` / `Công ty` | Zero direct second-person address (`bạn`, `anh/chị` are forbidden) |
| Customer-facing banking, wealth, credit, insurance | `finance-formal` | `Quý khách` | `Chúng tôi` / `[Tên ngân hàng]` | High respect floor; never use `bạn` or `cả nhà` |
| Retail FinTech apps (onboarding, dashboards) | `ux-microcopy` | *(omit on buttons/labels)*; `bạn` in dialogs | *(impersonal)* | Switch immediately to `Quý khách` or impersonal on money-movement screens |
| High-value transfer verification & security alerts | `finance-formal` | `Quý khách` | `Hệ thống` / `Ngân hàng` | Statutory step-up tone under QĐ 2345/QĐ-NHNN |

> [!IMPORTANT]
> The **Channel Override Law**: Even if a digital bank or FinTech brand adopts a friendly, youthful persona (`bạn`) on social media, all transactional confirmations, e-invoices, credit contracts, and regulatory disclaimers **must revert to `Quý khách` or impersonal third person**.

---

## 2. Statutory Financial Statement Rules (Thông tư 99/2025/TT-BTC)

Effective **01/01/2026**, Thông tư 99/2025/TT-BTC replaces Thông tư 200/2014/TT-BTC, introducing sweeping accounting nomenclature updates:

1. **Balance Sheet Renamed:**
   - ❌ `Bảng cân đối kế toán` *(stale terminology, flags `CAL001` at `error` severity)*
   - ✅ `Báo cáo tình hình tài chính` *(statutory form B01-DN)*
2. **Four Primary Financial Statements:**
   - **B01-DN:** `Báo cáo tình hình tài chính` *(Statement of Financial Position)*
   - **B02-DN:** `Báo cáo kết quả hoạt động kinh doanh` *(Statement of Income)*
   - **B03-DN:** `Báo cáo lưu chuyển tiền tệ` *(Statement of Cash Flows)*
   - **B09-DN:** `Bản thuyết minh báo cáo tài chính` *(Notes to the Financial Statements)*
3. **Roman Numerals for Quarters:**
   - Write `Quý I`, `Quý II`, `Quý III`, `Quý IV`. Never write `Q1`, `Q4`, or Arabic `Quý 1`.
4. **Official Tax Abbreviations:**
   - Use Vietnamese statutory acronyms: `thuế GTGT` (Value Added Tax), `thuế TNDN` (Corporate Income Tax), `thuế TNCN` (Personal Income Tax), `MST` (Tax Identification Number).
   - Never use English acronyms (`VAT`, `CIT`, `PIT`) in Vietnamese statutory or reporting contexts.

---

## 3. Financial Table & Number Typography

Financial tables require exact typographic and orthographic treatment:

- **Negative Numbers in Parentheses (`FIN006`):**
  Financial statements write negatives enclosed in parentheses, never with a raw ASCII minus sign:
  - ❌ `-1.234.500.000` / `- 500 triệu`
  - ✅ `(1.234.500.000)` / `(500.000.000) ₫`
- **Mandatory "Đơn vị tính" Header (`FIN005`):**
  Every financial statement table must declare its unit of magnitude:
  - `Đơn vị tính: triệu đồng` (or `tỷ đồng`, `VND`). Without this header, readers and auditors cannot determine transactional scale.
- **Vietnamese Digit Grouping (`NUM001` & `NUM003`):**
  - Thousands grouped by period: `2.500.000 ₫` (never comma `2,500,000`).
  - Decimal fractions separated by comma: `5,8%`, `12,75%` (never dot `5.8%`).
- **Number-to-Words Orthography (`Số tiền bằng chữ`):**
  - Standard capitalization: capitalize the first word and end with `đồng` or `đồng chẵn`.
  - Orthography rules: `mười lăm` (15, with `l`), `hai mươi mốt` (21, with `mốt`), `ba mươi lăm` (35, with `lăm`), `bốn` or `tư` (40: `bốn mươi`, 44: `bốn mươi tư`).

---

## 4. Regulated Phrasing & Advertising Prohibitions

### A. Prohibited Guaranteed-Return Solicitation (`FIN001`)
Under **Luật Chứng khoán 2019 Điều 12** and **Nghị định 38/2018/NĐ-CP Điều 2 khoản 4**, soliciting investors with promises of guaranteed profit or capital preservation is strictly prohibited:
- ❌ Prohibited: `cam kết lợi nhuận 15%/năm`, `đảm bảo sinh lời`, `bảo toàn vốn 100%`, `đầu tư không rủi ro`, `chắc chắn có lãi`.
- ✅ Compliant: `Lợi nhuận kỳ vọng 15%/năm. Đầu tư có rủi ro; kết quả trong quá khứ không đảm bảo cho tương lai.`

### B. Promotional 0% Interest Rate Disclosures (`FIN002`)
Under **Thông tư 43/2016/TT-NHNN** (as amended by **Thông tư 18/2019/TT-NHNN**), lenders and BNPL platforms advertising promotional 0% rates must clearly disclose all associated fees and total repayment costs:
- ❌ Prohibited: `Trả góp 0% lãi suất cho mọi đơn hàng` *(omitting conversion or administrative fees)*.
- ✅ Compliant: `Trả góp lãi suất 0% — phí chuyển đổi 3%/khoản vay. Tổng số tiền phải trả: 10.300.000 ₫. Lãi suất thực tế: 6,2%/năm.`

### C. Investment-Linked Insurance Disclaimers (`FIN008`)
Under **Thông tư 67/2023/TT-BTC Điều 53**, marketing and documentation for unit-linked (ILP) or universal life (UL) products must feature prominent disclaimers:
1. This is an insurance contract, not a bank savings deposit (`không phải là tiền gửi ngân hàng/tiết kiệm`).
2. The policyholder bears all investment risk (`bên mua bảo hiểm chịu mọi rủi ro đầu tư`).

### D. Digital Assets Regulatory Stance (NQ 05/2025/NQ-CP & Luật 71/2025)
- Digital assets (cryptocurrency, tokens) are **not legal tender** in Vietnam (`không phải là phương tiện thanh toán hợp pháp`).
- Any sandbox trading platform copy must clarify that transactions are limited to authorized pilot participants under Bộ Tài chính supervision.

---

## 5. FinTech UX, VietQR, & Biometric Step-Up (QĐ 2345/QĐ-NHNN)

Modern Vietnamese FinTech applications require precise UX microcopy across payment rails:

1. **VietQR / NAPAS 247 Instant Transfer:**
   - Standard field labels: `Ngân hàng thụ hưởng`, `Số tài khoản`, `Tên người thụ hưởng`, `Số tiền chuyển`, `Nội dung chuyển khoản`.
   - Remind users that transfer descriptions must avoid ambiguous payment codes and special characters.
2. **Chip-Enabled Citizen ID (CCCD gắn chip) NFC Scanning UX:**
   - Clear hardware instructions: `Đặt mặt sau CCCD áp sát khu vực ăng-ten NFC (gần camera trên iPhone hoặc giữa lưng máy Android). Giữ yên thiết bị trong 3–5 giây.`
   - Graceful troubleshooting copy for metal cases or NFC connection timeouts.
3. **Quyết định 2345/QĐ-NHNN Biometric Authentication Step-Up (`FIN009`):**
   - Transactions exceeding **10.000.000 ₫ per transfer** or cumulative transfers exceeding **20.000.000 ₫ in a single day** require biometric authentication matching the citizen database:
   - Copy requirement: Explicitly inform users that facial authentication (`xác thực sinh trắc học khuôn mặt`) is required before confirming the transaction.

---

## 6. Validation & CLI Usage

Run the integrated validator before publishing or committing any financial documentation:

```bash
# Validate financial statement table
python skills/vietnamese-finance-copy/scripts/validate_copy.py bctc.md --doctype statement --register finance-formal --strict

# Validate electronic invoice
python skills/vietnamese-finance-copy/scripts/validate_copy.py invoice.md --doctype e-invoice --register finance-formal --strict

# Validate consumer credit or installment campaign
python skills/vietnamese-finance-copy/scripts/validate_copy.py tra-gop.md --doctype loan --register finance-formal --strict

# Validate investment-linked insurance copy
python skills/vietnamese-finance-copy/scripts/validate_copy.py bao-hiem.md --doctype insurance --register finance-formal --strict

# Validate FinTech high-value payment UI
python skills/vietnamese-finance-copy/scripts/validate_copy.py transfer.md --doctype fintech-transfer --strict
```

### Validator Rule Reference
- `FIN001`: Guaranteed-return language prohibited in solicitation.
- `FIN002`: Promotional 0% rate without explicit fee or total-cost disclosure.
- `FIN005`: Financial statement table missing `Đơn vị tính` header.
- `FIN006`: Negative number written with ASCII minus instead of parentheses in statements.
- `FIN007`: E-invoice missing mandatory statutory fields (`MST` or `thuế GTGT`).
- `FIN008`: Investment-linked insurance missing mandatory risk and non-deposit disclaimers.
- `FIN009`: High-value bank transfer UI omitting biometric authentication requirement.
- `CAL001`: Financial translationese and stale terminology (e.g., `Bảng cân đối kế toán`).
- `LAW001`: Unsubstantiated financial superlatives (`lãi suất cao nhất thị trường`).
- `NUM001` / `NUM003`: Vietnamese number grouping and decimal comma conventions.
- `PRO001` / `PRO002`: Register violations (e.g. casual `bạn` in formal financial contracts).

---

## 7. Reference Files

- [references/glossary.md](references/glossary.md) — 55+ statutory finance, accounting, tax, and FinTech terms.
- [references/banned-phrases.md](references/banned-phrases.md) — Prohibited marketing claims, misleading rate tricks, and superlative patterns.
- [references/statement-terminology.md](references/statement-terminology.md) — Comprehensive TT 99/2025/TT-BTC line items, B01-B09 form breakdown, and tax codes.
- [references/statement-formatting.md](references/statement-formatting.md) — Table formatting, units of measure, negative parentheses, and number-to-words orthography.
- [references/financial-promotion.md](references/financial-promotion.md) — In-depth legal breakdown of consumer credit, securities solicitation, insurance disclosures, and crypto status.
- [references/fintech-ekyc-vietqr.md](references/fintech-ekyc-vietqr.md) — VietQR guidelines, NFC CCCD chip reading prompts, and QĐ 2345 biometric step-up UX.
- [references/qa-checklist.md](references/qa-checklist.md) — 12-point pre-publish review checklist for accountants and legal counsel.
- [assets/hoa-don-gtgt.md.template](assets/hoa-don-gtgt.md.template) — Fully compliant electronic invoice template.
