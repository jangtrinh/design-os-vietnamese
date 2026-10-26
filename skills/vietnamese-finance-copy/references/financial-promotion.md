<!-- vlc-disable: all -->

# Financial Promotions, Consumer Lending, & Regulatory Boundaries (`design-os-vietnamese`)

This guide outlines statutory constraints governing marketing, consumer lending disclosures, fund solicitation, investment-linked insurance, and digital assets under Vietnamese law.

---

## 1. Absolute Prohibition of Guaranteed Returns (`FIN001`)

Under Vietnamese law, no broker, investment fund, fintech platform, or corporate entity may promise guaranteed profits, capital safety, or risk-free returns to the public.

### Statutory Foundations
1. **Luật Chứng khoán 2019 (Luật số 54/2019/QH14 Điều 12 khoản 1):**
   - Prohibits false, misleading, or deceptive disclosures and fraudulent guarantees regarding securities investment performance.
2. **Nghị định 155/2020/NĐ-CP Điều 217 & Điều 286:**
   - Forbids fund management companies, securities brokerages, and fund distribution agents from making commitments regarding future investment yields or capital protection.
   - Prohibits publishing projections of future portfolio growth that are not supported by audited financial models and clear risk sensitivity ranges.
3. **Nghị định 38/2018/NĐ-CP Điều 2 khoản 4:**
   - Prohibits fraudulent capital raising schemes promising guaranteed interest yields exceeding reasonable economic parameters.
4. **Nghị định 65/2022/NĐ-CP về chào bán trái phiếu doanh nghiệp riêng lẻ:**
   - Strictly forbids marketing private placement corporate bonds to non-professional retail investors through public social media or mass distribution channels.
   - Forbids phrasing that implies private corporate bonds are "tiền gửi tiết kiệm" or "không rủi ro".

### Blacklisted Phrasing & Required Rewrites
| Prohibited Solicitation Phrasing | Why It Violates Law | Compliant Formulation |
|---|---|---|
| `Cam kết lợi nhuận 15%/năm` | Direct return guarantee banned under Luật CK Đ12 | `Lợi nhuận kỳ vọng 15%/năm (đầu tư có rủi ro)` |
| `Bảo toàn vốn 100%` | Capital safety guarantee | `Sản phẩm có mức độ rủi ro vốn thấp` |
| `Đầu tư an toàn, không có rủi ro` | Misrepresentation of financial market realities | `Sản phẩm phù hợp với nhà đầu tư thận trọng` |
| `Chắc chắn có lãi mỗi tháng` | False promise of unconditional yields | `Mục tiêu phân bổ lợi nhuận định kỳ hàng tháng` |
| `Sinh lời chắc chắn không lo thị trường giảm` | Deceptive downside protection claim | `Chiến lược phòng hộ rủi ro biến động thị trường` |
| `Đầu tư bất động sản cam kết thuê lại lãi 12%` | Banned yield-guarantee structure | `Lợi nhuận cho thuê ước tính từ 8–10%/năm` |
| `Cơ hội x2 tài khoản trong 6 tháng` | Sensational solicitation slop | `Kế hoạch tích lũy tài sản trung và dài hạn` |

> [!WARNING]
> `FIN001` is emitted across **all document types** without restriction. If copy contains any guaranteed-return phrase, the validator flags a warning directing the draft to formal legal counsel review.

---

## 2. Consumer Credit & BNPL Transparency (TT 43/2016 & TT 18/2019 — `FIN002`)

The State Bank of Vietnam strictly regulates retail lending, credit cards, consumer finance companies, and Buy Now Pay Later (BNPL) platforms through **Thông tư 43/2016/TT-NHNN** as amended by **Thông tư 18/2019/TT-NHNN Điều 9, 10a**.

### The "0% Interest" Deception Trap
Promoting `Lãi suất 0%` or `Trả góp 0%` while quietly levying heavy conversion fees, administrative charges, or insurance fees without simultaneous disclosure constitutes deceptive advertising under Vietnamese consumer protection laws.

### Mandatory Disclosure Requirements
Any promotional headline featuring `0%` or a discounted rate must display the following data points on the identical visual surface:
1. **Phí chuyển đổi giao dịch / Phí dịch vụ** (Conversion / Processing Fee): Stated as an exact percentage or fixed VND amount.
2. **Tổng chi phí / Tổng số tiền phải trả** (Total Repayment Cost): Sum of principal and all applicable fees.
3. **Lãi suất thực tế áp dụng** (Effective Annual Percentage Rate - APR): Calculated on the reducing balance.

### Mathematical Representation of Repayment
Under Circular 18/2019/TT-NHNN, lenders must publish an illustrative repayment table demonstrating how payments are allocated:
- Allocation priority order: `Chi phí phát sinh` $\rightarrow$ `Tiền lãi quá hạn` $\rightarrow$ `Tiền lãi trong hạn` $\rightarrow$ `Tiền gốc quá hạn` $\rightarrow$ `Tiền gốc trong hạn`.

### Compliant Layout Example
```markdown
### MUA TRƯỚC TRẢ SAU — TRẢ GÓP LÃI SUẤT 0%
- Giá trị đơn hàng: 12.000.000 ₫
- Kỳ hạn trả góp: 6 tháng (2.000.000 ₫/tháng)
- Lãi suất danh nghĩa: 0%
- Phí chuyển đổi trả góp: 3% (360.000 ₫)
- Tổng chi phí phải trả: 12.360.000 ₫
- Lãi suất thực tế theo dư nợ giảm dần: 10,2%/năm
```

If marketing copy promotes `lãi suất 0%` or `trả góp 0%` without displaying `phí chuyển đổi`, `tổng chi phí`, or `tổng số tiền phải trả`, `validate_copy.py` emits `FIN002`.

---

## 3. Investment-Linked Insurance Disclosures (TT 67/2023/TT-BTC Điều 53 — `FIN008`)

Bancassurance mis-selling (confusing life insurance with high-interest bank savings) led the Ministry of Finance to enact stringent rules under **Thông tư 67/2023/TT-BTC Điều 53**:

### The Two Mandatory Disclaimers
Any promotional material, product brochure, website copy, or quotation for investment-linked insurance (`Bảo hiểm liên kết đơn vị - ILP` hoặc `Bảo hiểm liên kết chung - UL`) must display two conspicuous disclosures:
1. **The Non-Deposit Disclaimer:**
   `"Đây là sản phẩm bảo hiểm, không phải là tiền gửi tiết kiệm ngân hàng."`
2. **The Investment Risk Disclaimer:**
   `"Kết quả đầu tư không được đảm bảo; bên mua bảo hiểm chịu toàn bộ rủi ro đầu tư."`

### Strict Prohibitions in Insurance Marketing
- Never compare insurance expected returns directly with bank deposit interest rates (`lãi suất cao hơn ngân hàng`).
- Never refer to premiums as "tiền gửi" or "tiền tiết kiệm".
- Never promise fixed investment returns on unit-linked investment funds.
- Must clearly separate the insurance premium allocation: `Phí ban đầu`, `Phí bảo hiểm rủi ro`, `Phí quản lý hợp đồng`, `Phí quản lý quỹ`, and `Giá trị tài khoản hợp đồng`.

---

## 4. Digital Assets & Cryptocurrency Boundaries (NQ 05/2025/NQ-CP & Luật 71/2025)

The legal status of digital assets, cryptocurrencies, and virtual currencies in Vietnam is explicitly defined:

### Core Legal Tenets
1. **Not Legal Tender:** Under Decree 80/2016/NĐ-CP and Decree 52/2024/NĐ-CP, cryptocurrencies (Bitcoin, USDT, etc.) are **not lawful means of payment** in Vietnam. Using crypto to settle goods and services is subject to administrative and criminal penalties.
2. **Nghị quyết 05/2025/NQ-CP Pilot Sandbox:**
   - Provides a controlled pilot sandbox for digital asset trading platforms supervised by the Ministry of Finance (Bộ Tài chính) and the State Bank of Vietnam (NHNN).
   - Only institutions formally licensed under the sandbox may solicit retail participants. Unlicensed offshore exchanges (e.g. `sàn quốc tế uy tín`) remain strictly illegal.
3. **Luật Công nghiệp Công nghệ số 71/2025/QH15:**
   - Defines digital assets as intangible assets represented in digital form, distinct from national fiat currency (`VNĐ`).

### Copywriting Rules for Digital Asset Products
- Never state that tokens can be used to "thanh toán hóa đơn", "mua sắm", or "thay thế tiền mặt".
- Mandatory disclaimer: `"Tài sản số không phải là phương tiện thanh toán hợp pháp tại Việt Nam và không được bảo hiểm tiền gửi Nhà nước bảo vệ."`
- Avoid deceptive hype words: `x100 tài khoản`, `tiền ảo sinh lời khủng`, `chắc chắn tăng giá`.

---

## 5. Omnichannel Financial Copywriting Matrix

Financial marketing copy is deployed across distinct digital surfaces, each governed by specific statutory and technical rules:

| Distribution Channel | Formality Floor | Disclaimers Required | Prohibited Techniques |
|---|---|---|---|
| **Official Website & Landing Page** | `finance-formal` (`Quý khách` or impersonal) | Full disclaimers in main body; fee schedules | Hiding fees in accordion or micro-footnotes |
| **Zalo ZNS / Notification** | `finance-formal` (`Quý khách`) | Transaction purpose, customer care phone | Promotional upselling in transactional templates |
| **Facebook / Meta Paid Ads** | `saas` / `finance-formal` | Risk statement in primary text | Unsubstantiated claims of `số 1`, `lãi suất cao nhất` |
| **Mobile App Push Notifications** | `ux-microcopy` (impersonal / `Quý khách`) | Specific transaction amount and balance | Misleading clickbait phrasing (`Bạn vừa nhận 50 triệu`) |
| **In-Branch Print Flyers / Posters** | `finance-formal` | Complete license number, issuing bank | Omission of APR or conversion fees |

---

## 6. Regulatory Legal Review Workflow

Every financial promotion must follow a two-stage pre-clearance gate before release:
1. **Phase 1: Automated Rule Verification (`validate_copy.py`):**
   - Check against blocklists (`FIN001`, `FIN002`, `FIN008`, `LAW001`, `NUM001`).
2. **Phase 2: Registered Legal & Compliance Sign-Off:**
   - Certified Legal Counsel evaluates regulatory suitability, licensed disclosures, and consumer protection mandates.
   - For investment fund and insurance promotions, review requires approval by an appointed compliance officer (`Người phụ trách tuân thủ`).
   - For credit products, fee schedule must be certified compliant with State Bank of Vietnam regulations.
