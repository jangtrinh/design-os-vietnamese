---
name: vietnamese-insurance-insurtech
description: Drafts, localizes, and audits native-quality Vietnamese (vi-VN) life insurance illustrations, general insurance policies, InsurTech digital platforms, claim settlement guides, and bancassurance agreements. Enforces Law on Insurance Business 2022 (Luật Kinh doanh bảo hiểm số 08/2022/QH15) and Circular 67/2023/TT-BTC, mandatory 21-day free-look periods (thời gian cân nhắc 21 ngày Điều 35), affirmative disclosure of liability exclusions (Điều 19), 15-day statutory claim settlement timelines (Điều 31), statutory roles (Bên mua bảo hiểm, Người được bảo hiểm, Người thụ hưởng Điều 4), prohibition of disguising investment-linked insurance as fixed bank savings deposits, and anti-coercion regulations in bancassurance credit disbursement.
version: "5.0.0"
license: PolyForm-Shield-1.0.0
metadata:
  author: "DESIGN:OS Vietnamese"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Insurance Law & InsurTech Compliance (`vietnamese-insurance-insurtech`)

In Vietnamese financial services, insurance copywriting and digital product design carry **strict regulatory liability and consumer protection mandates**. Misrepresenting investment-linked insurance as guaranteed bank savings deposits or coercing borrowers into purchasing insurance violates the Law on Insurance Business 2022 and Ministry of Finance Circular 67/2023/TT-BTC; truncating the 21-day free-look period breaches Article 35; concealing liability exclusion clauses triggers statutory invalidity under Article 19; and using clumsy translationese degrades trust and legal enforceability.

This skill equips insurance product managers, actuaries, legal counsels, and InsurTech engineers with authoritative, statutory Vietnamese insurance terminology, compliant disclosure structures, and linter automation aligned with Vietnamese insurance jurisprudence.

---

## 1. Register & Sociolinguistic Etiquette

Insurance communications operate under formal contractual and customer service registers:

| Document / Surface | Register | Address (`Hô`) | Speaker (`Xưng`) | Notes |
|---|---|---|---|---|
| Policy Illustration (`policy-illustration`) | `insurance-policyholder` | `Quý khách` / `Bên mua bảo hiểm` | `Công ty` / `Doanh nghiệp bảo hiểm` | Professional, transparent tone; explicit risk disclosures and return scenarios |
| Insurance Certificate (`insurance-certificate`) | `legal-contract` | `Bên mua bảo hiểm` / `Người được bảo hiểm` | `Doanh nghiệp bảo hiểm` | Third-person statutory precision; mandatory liability exclusions section |
| Claim Guide (`claim-guide`) | `insurance-policyholder` | `Quý khách` / `Người yêu cầu giải quyết` | `Công ty bảo hiểm` / `Bộ phận bồi thường` | Empathetic, clear, step-by-step guidance; statutory 15-day settlement deadline |

---

## 2. Supported Document Types (`DOCTYPES`)

The linter dynamically configures domain-specific statutory checks based on declared `--doctype`:

| Doctype Slug | Vietnamese Title & Statutory Scope | Key Statutory Checks |
|---|---|---|
| `policy-illustration` | Tài liệu minh họa bán hàng & Giới thiệu sản phẩm bảo hiểm nhân thọ / liên kết đầu tư (Luật KDBH 2022 & TT 67/2023/TT-BTC) | `INS001` (cấm mạo danh tiết kiệm), `INS002` (thời gian cân nhắc 21 ngày) |
| `insurance-certificate` | Giấy chứng nhận bảo hiểm & Tóm tắt quy tắc, điều khoản bảo hiểm (Luật Kinh doanh bảo hiểm 2022) | `INS003` (bắt buộc mục loại trừ trách nhiệm), `INS004` (chuẩn hóa thuật ngữ) |
| `claim-guide` | Hướng dẫn giải quyết quyền lợi bảo hiểm / Thông báo bồi thường (Điều 31 Luật KDBH 2022) | `INS005` (thời hạn chi trả tối đa 15 ngày), `INS006` (chống ép mua bảo hiểm) |

---

## 3. End-to-End Workflow

To produce compliant insurance copy and digital onboarding flows under Vietnamese law, follow this 5-stage workflow:

1. **Stage 1: Doctype Classification & Product Category Determination:**
   - Determine whether the instrument is a sales illustration (`policy-illustration`), insurance certificate (`insurance-certificate`), or claim procedure guide (`claim-guide`).
   - Identify whether the product is term life, endowment, unit-linked (`liên kết đơn vị`), or universal life (`liên kết chung`).
2. **Stage 2: Investment Transparency & Anti-Savings Governance:**
   - Verify that investment-linked products are never described as bank savings deposits or guaranteed yield accounts (`INS001`).
   - Include explicit fluctuating investment scenarios and capital loss risk disclaimers.
3. **Stage 3: Mandatory Statutory Rights & Exclusions Integration:**
   - Confirm explicit inclusion of the statutory **21-day free-look period** under Article 35 (`INS002`).
   - Confirm transparent, prominent display of **liability exclusion clauses** (`điều khoản loại trừ trách nhiệm bảo hiểm`) under Article 19 (`INS003`).
4. **Stage 4: Terminology Standardization & Anti-Coercion Check:**
   - Standardize all statutory roles (`Doanh nghiệp bảo hiểm`, `Bên mua bảo hiểm`, `Người được bảo hiểm`, `Người thụ hưởng`) and eliminate foreign calques (`INS004`).
   - Audit bancassurance copy to ensure zero tie-in coercion with credit disbursement (`INS006`).
   - Verify that claim settlement timelines do not exceed the statutory 15-day limit (`INS005`).
5. **Stage 5: Automated Linter & Pre-Publication Gate:**
   - Run `validate_copy.py` with `--domain vietnamese-insurance-insurtech` and `--doctype`.

---

## 4. Statutory Regulations & Transition Guidelines

1. **Investment-Linked Insurance vs. Bank Savings (`INS001`):**
   - Under **Thông tư 67/2023/TT-BTC**, insurers and bancassurance distribution channels are strictly prohibited from misrepresenting investment-linked products as savings accounts with fixed guaranteed interest.
2. **21-Day Free-Look Period (`INS002`):**
   - Under **Điều 35 Luật Kinh doanh bảo hiểm 2022**, life insurance contracts exceeding 1 year grant policyholders 21 days from contract receipt to cancel with full refund of paid premiums (less medical check costs).
   - Stating shorter periods (e.g. 7, 10, or 14 days) or waiving cancellation is illegal.
3. **Affirmative Disclosure of Liability Exclusions (`INS003`):**
   - Under **Điều 19 Luật Kinh doanh bảo hiểm 2022**, exclusion clauses must be explicitly explained to the policyholder upon signing; otherwise they are unenforceable.
4. **Statutory Terminology (`INS004`):**
   - Replace literal translationese with statutory Vietnamese insurance concepts:
     - `Hợp đồng bảo hiểm` (never `Chính sách bảo hiểm`)
     - `Bên mua bảo hiểm` (never `Người giữ chính sách`)
     - `Phí bảo hiểm` / `Phí bảo hiểm định kỳ hàng năm` (never `Tiền thưởng bảo hiểm`)
     - `Phạm vi bảo hiểm` (never `Câu chuyện bảo hiểm`)
     - `Sự kiện bất khả kháng` / `Thiên tai` (never `Sự kiện thiên Chúa`)
5. **Claim Settlement Timelines (`INS005`):**
   - Under **Điều 31 Luật Kinh doanh bảo hiểm 2022**, claims must be settled within 15 days of receiving a complete, valid dossier (maximum 30 days if verification is required).
6. **Anti-Coercion in Bancassurance (`INS006`):**
   - Under Circular 67/2023/TT-BTC and the Law on Credit Institutions 2024, tying loan approvals or disbursement to compulsory life insurance purchases is strictly prohibited.

---

## 5. Deterministic Rule Reference

- `INS001`: Disguising investment-linked life insurance as a fixed-rate bank savings deposit.
- `INS002`: Truncating or omitting the mandatory 21-day free-look period for life insurance.
- `INS003`: Concealing, waiving, or omitting the disclosure of liability exclusion clauses.
- `INS004`: Using machine-translated insurance calques (`chính sách bảo hiểm`, `người giữ chính sách`, `tiền thưởng bảo hiểm`).
- `INS005`: Imposing unlawful claim settlement timelines exceeding statutory limits (e.g. 60 or 90 days).
- `INS006`: Coercive bancassurance tying insurance purchase to credit disbursement.

---

## 6. Bundled References

- [references/luat-kinh-doanh-bao-hiem-2022.md](references/luat-kinh-doanh-bao-hiem-2022.md) — Law on Insurance Business 2022 key provisions: 4 statutory roles, 21-day free-look, exclusion clauses, and 15-day claim timelines.
- [references/thong-tu-67-2023-bancassurance.md](references/thong-tu-67-2023-bancassurance.md) — Circular 67/2023/TT-BTC bancassurance anti-coercion regulations and investment-linked illustration standards.
- [references/insurance-terminology-and-calques.md](references/insurance-terminology-and-calques.md) — Statutory Vietnamese insurance glossary and English translationese lookup table.
