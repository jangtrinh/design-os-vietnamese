---
name: vietnamese-legal-contracts
description: Drafts, localizes, and audits native-quality Vietnamese (vi-VN) civil and commercial agreements, corporate governance contracts, Terms of Service (ToS), and Data Processing Agreements (DPA). Enforces statutory penalty caps under Article 301 of Commercial Law 2005 (Luật Thương mại 2005 trần phạt vi phạm 8%), general contract freedom under Civil Code 2015 (Bộ luật Dân sự 2015 Điều 418), deposit mechanisms (Điều 328), force majeure (Điều 156), and fundamental change of circumstances (Điều 420), statutory labor contract classifications under Labor Code 2019 (Bộ luật Lao động 2019 Điều 20 bãi bỏ hợp đồng mùa vụ, chỉ công nhận không xác định thời hạn và xác định thời hạn tối đa 36 tháng; thử việc Điều 25-26), non-compete agreements (NCA) and confidentiality agreements (NDA) under Article 21 Clause 2 BLLĐ and VIAC arbitration practice, unconscionable contract terms prohibition under Consumer Protection Law 2023 (Luật Bảo vệ quyền lợi người tiêu dùng 2023 Điều 25 cấm miễn trừ toàn bộ trách nhiệm và tước đoạt quyền khiếu nại của người tiêu dùng), Personal Data Protection Law compliance (Luật 91/2025/QH15 Điều 4 quyền của chủ thể dữ liệu gồm rút lại sự đồng ý và xóa dữ liệu, Điều 23 thông báo vi phạm dữ liệu trong 72 giờ cho Bộ Công an A05, Điều 24 DPIA và Điều 25 chuyển dữ liệu ra nước ngoài), and software intellectual property assignments under amended IP Law 2022 (Luật Sở hữu trí tuệ sửa đổi 2022 Điều 19 quyền nhân thân không thể chuyển nhượng vs Điều 20 quyền tài sản).
license: PolyForm-Shield-1.0.0
metadata:
  author: "Jang Trinh"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Legal Drafting & Contract Compliance (`vietnamese-legal-contracts`)

In Vietnamese jurisprudence, contract drafting carries **strict statutory nullity and regulatory sanctions**. Writing a commercial penalty exceeding 8% renders the clause partially void under Commercial Law 2005; drafting a seasonal labor contract breaches Labor Code 2019; and including blanket liability waivers in consumer Terms of Service (ToS) triggers statutory nullification under Consumer Protection Law 2023.

This skill equips legal counsels, procurement teams, and software engineers with authoritative, verified Vietnamese legal phrasing, contract structures, PDPD compliance clauses, and linter automation aligned with current Vietnamese legislation.

---

## 1. Register & Sociolinguistic Etiquette

Legal documents and contracts in Vietnam operate under strict formal conventions (`legal-contract` register):

| Document / Surface | Register | Address (`Hô`) | Speaker (`Xưng`) | Notes |
|---|---|---|---|---|
| Commercial & Civil Contracts | `legal-contract` | `Bên B` / `Khách hàng` | `Bên A` / `Doanh nghiệp` | Third-person only; zero second-person pronouns (`bạn`, `mình`, `em`) |
| Terms of Service (ToS) & EULA | `legal-contract` | `Người dùng` / `Khách hàng` | `Chúng tôi` / `Công ty` | Objective legal tone; explicit rights and dispute boundaries |
| PDPD Privacy Policy & DPA | `legal-contract` | `Chủ thể dữ liệu` | `Bên Kiểm soát dữ liệu` | Exact statutory terminology per Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 & Nghị định 356/2025/NĐ-CP |
| Employment Agreements & NDA | `legal-contract` | `Người lao động` | `Người sử dụng lao động` | High statutory formality per Bộ luật Lao động 2019 |

---

## 2. Supported Document Types (`DOCTYPES`)

The linter dynamically configures domain-specific statutory checks based on declared `--doctype`:

| Doctype Slug | Vietnamese Title & Statutory Scope | Key Statutory Checks |
|---|---|---|
| `commercial-contract` | Hợp đồng thương mại / Cung ứng dịch vụ B2B (Luật Thương mại 2005 & BLDS 2015) | `LEG001` (trần phạt vi phạm 8%), `LEG006` (trọng tài/tòa án & bất khả kháng) |
| `civil-contract` | Hợp đồng dân sự / Thuê tài sản / Vay tài sản (Bộ luật Dân sự 2015) | `LEG006` (điều khoản tranh chấp & bất khả kháng), tự do thỏa thuận phạt vi phạm |
| `labor-contract` | Hợp đồng lao động (Bộ luật Lao động 2019 — Luật số 45/2019/QH14) | `LEG002` (cấm hợp đồng mùa vụ), thời hạn tối đa 36 tháng, lương thử việc 85% |
| `terms-of-service` | Điều khoản sử dụng dịch vụ / Điều kiện giao dịch chung (Luật BVQLNTD 2023) | `LEG004` (cấm miễn trừ toàn bộ trách nhiệm & cấm tước đoạt quyền khiếu nại) |
| `pdpd-policy` | Chính sách bảo mật & Thỏa thuận DPA (Luật 91/2025/QH15, Nghị định 356/2025/NĐ-CP & Luật Dữ liệu 60/2024/QH15) | `LEG007` (quyền chủ thể dữ liệu theo Điều 4 Luật 91/2025/QH15), quyền rút lại sự đồng ý & yêu cầu xóa dữ liệu |

---

## 3. End-to-End Legal Drafting & Review Workflow

To produce compliant, enforceable legal instruments under Vietnamese law, follow this 5-stage workflow:

1. **Stage 1: Doctype Classification & Statutory Scope Determination:**
   - Identify whether the transaction is B2B commercial, civil, consumer, employment, or personal data processing.
   - Reference the governing statute (LTM 2005 for commercial profit activities, BLDS 2015 for general civil obligations).
2. **Stage 2: Register Enforcement & Party Pronoun Architecture:**
   - Establish consistent third-person identification (`Bên A`, `Bên B`, `Người lao động`, `Chủ thể dữ liệu`).
   - Eliminate all conversational or casual pronouns (`bạn`, `mình`, `cả nhà`, `em`, `con`, `cậu`).
3. **Stage 3: Operative Drafting & Statutory Boundary Verification:**
   - Enforce the **8% statutory cap** on breach penalties in commercial agreements under Article 301 LTM 2005.
   - Prohibit blanket liability disclaimers and consumer right forfeitures under Article 25 Consumer Protection Law 2023.
   - Verify that all statutory citations follow Vietnamese legislative hierarchy (`Khoản 2 Điều 15`, never `Điều 15.2`).
4. **Stage 4: Dispute Resolution & Force Majeure Allocation:**
   - Incorporate explicit governing law (pháp luật Việt Nam) and forum selection (VIAC arbitration or competent People's Court).
   - Formulate 3-element force majeure clauses under Article 156 Civil Code 2015 with 48-hour notification procedures.
5. **Stage 5: Automated Linter & Pre-Execution QA Gate:**
   - Run `validate_copy.py` with `--doctype`, `--register legal-contract`, and `--strict`.
   - Complete the 12-point pre-execution checklist in `references/qa-checklist.md`.

---

## 4. Commercial Law 2005 vs. Civil Code 2015 Drafting Rules

Contract drafters must navigate the boundary between general civil rules and specialized commercial caps:

1. **Breach Penalty 8% Cap (`LEG001`):**
   - Under **Điều 301 Luật Thương mại 2005**, agreed penalties for breach (`phạt vi phạm`) in commercial contracts between business entities are strictly capped at **8% of the breached obligation value**.
   - Contracts under the Civil Code (BLDS 2015 Điều 418) permit unlimited agreed penalties unless a specialized statute applies.
2. **Penalties vs. Damages (Điều 307 LTM & Điều 419 BLDS):**
   - Penalties require express agreement; damages do not require an express clause but require proof of actual loss.
   - Parties may claim both penalties (capped at 8%) and full actual damages (`bồi thường thiệt hại toàn bộ`) if explicitly stipulated.
3. **Security Deposit & Penalty (Điều 328 BLDS 2015):**
   - If the receiving party refuses execution, it must return the deposit and pay an equivalent amount (`phạt cọc`), unless agreed otherwise.
4. **Force Majeure & Hardship (Điều 156 & Điều 420 BLDS 2015):**
   - Force majeure requires objective impossibility, unforeseeability, and irremediability.
   - Hardship requires renegotiation before seeking judicial contract adjustment or termination.

---

## 5. Consumer Protection & PDPD Privacy Mandates

Digital platforms and online service providers face strict consumer and data regulations:

1. **Unconscionable Terms Prohibition (`LEG004`):**
   - Under **Điều 25 Luật Bảo vệ quyền lợi người tiêu dùng 2023**, blanket liability disclaimers, waivers of consumer complaint rights, and unilateral modification clauses without cancellation rights are **void ab initio (vô hiệu)**.
2. **Data Subject Rights (`LEG007`):**
   - Privacy policies and DPAs must enumerate the **data subject rights** under **Điều 4 khoản 1 Luật 91/2025/QH15** (the former 11-item list of Điều 9 Nghị định 13/2023/NĐ-CP is no longer in force), specifically including the right to withdraw consent (`rút lại sự đồng ý`) and right to erasure (`xóa dữ liệu cá nhân`).
3. **Data Breach Notification (Điều 23 Luật 91/2025/QH15; Mẫu số 08 NĐ 356/2025/NĐ-CP):**
   - Personal data breaches must be reported to the Ministry of Public Security (Department A05) within **72 hours** of discovery.

---

## 6. Labor Code 2019 & Intellectual Property Governance

1. **Abolition of Seasonal Contracts (`LEG002`):**
   - Article 20 of Labor Code 2019 recognizes only two contract forms: **indefinite-term** and **fixed-term up to 36 months**. Seasonal labor contracts (`hợp đồng mùa vụ`) are completely abolished.
2. **Non-Compete Agreements (NCA):**
   - Enforceable when executed as an independent agreement protecting trade secrets under Article 21 Clause 2 BLLĐ, supported by financial compensation, and arbitrated via VIAC.
3. **Moral vs. Economic IP Rights (Luật SHTT sửa đổi 2022):**
   - Moral rights under Article 19 Clauses 1, 2, and 4 (author name, integrity) are non-transferable.
   - Only economic rights under Article 20 and publication rights may be transferred or assigned.

---

## 7. Validation CLI & Rule Matrix

Execute the linter to verify contracts and policies before execution:

```bash
# Validate B2B Commercial Contract
python skills/vietnamese-legal-contracts/scripts/validate_copy.py hop-dong.md --doctype commercial-contract --register legal-contract --strict

# Validate Terms of Service (ToS)
python skills/vietnamese-legal-contracts/scripts/validate_copy.py tos.md --doctype terms-of-service --register legal-contract --strict

# Validate PDPD Privacy Policy or DPA
python skills/vietnamese-legal-contracts/scripts/validate_copy.py pdpd.md --doctype pdpd-policy --register legal-contract --strict

# Validate Employment Agreement
python skills/vietnamese-legal-contracts/scripts/validate_copy.py labor.md --doctype labor-contract --register legal-contract --strict
```

### Deterministic Rule Reference
- `LEG001`: Penalty for breach exceeding 8% statutory cap under Article 301 Commercial Law 2005.
- `LEG002`: Obsolete seasonal labor contract abolished under Article 20 Labor Code 2019.
- `LEG003`: Foreign statutory citation hierarchy (`Điều 15 Khoản 2`); standard order is `Khoản 2 Điều 15`.
- `LEG004`: Unconscionable blanket liability waiver in consumer terms prohibited under Article 25 Consumer Protection Law 2023.
- `LEG005`: Obsolete statute name without historical annotation (e.g. `Bộ luật Dân sự 2005`, `Bộ luật Lao động 2012`).
- `LEG006`: Contract missing mandatory dispute resolution clause (`Giải quyết tranh chấp` / `Tòa án` / `Trọng tài`) or force majeure clause (`Bất khả kháng`).
- `LEG007`: PDPD policy missing mandatory data subject rights under Article 4 of Law 91/2025/QH15 (the rule message still cites Decree 13/2023 Article 9).
- `CAL001`: English common-law calques and mistranslations (e.g., `bồi thường vô hại` -> `bồi thường thiệt hại`).
- `LAW001`: Unsubstantiated absolute representations and marketing superlatives.
- `PRO002`: Pronoun violations in the `legal-contract` register (e.g., casual `bạn`, `mình`).

---

## 8. Reference Documentation & Production Templates

- [references/glossary.md](references/glossary.md) — 65+ machine-readable civil law terms and English-Vietnamese equivalents.
- [references/banned-phrases.md](references/banned-phrases.md) — 33+ common-law calques, prohibited ToS clauses, and superlative patterns.
- [references/contract-drafting-blds-ltt.md](references/contract-drafting-blds-ltt.md) — Standard contract architecture, 8% penalty cap, deposit, and force majeure.
- [references/pdpd-and-consumer-protection.md](references/pdpd-and-consumer-protection.md) — Consumer Protection Law 2023 void clauses and PDPD Decree 13 DPA requirements.
- [references/labor-and-ip-clauses.md](references/labor-and-ip-clauses.md) — Labor Code 2019 classifications, NCA enforceability, and software IP transfer.
- [references/qa-checklist.md](references/qa-checklist.md) — 12-point pre-execution statutory and linguistic verification checklist.
- [assets/hop-dong-dich-vu-b2b.md.template](assets/hop-dong-dich-vu-b2b.md.template) — Fully compliant B2B technology services contract template.
- [assets/chinh-sach-bao-mat-pdpd.md.template](assets/chinh-sach-bao-mat-pdpd.md.template) — PDPD privacy policy template based on Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 & Nghị định 356/2025/NĐ-CP.
