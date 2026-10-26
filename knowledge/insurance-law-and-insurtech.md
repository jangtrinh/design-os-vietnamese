---
id: "insurance-law-and-insurtech"
title: "Vietnamese Insurance Business Law, InsurTech Compliance, and Bancassurance Governance"
domain: "vietnamese-insurance-and-insurtech"
description: "Verified specification for Vietnamese insurance product disclosures, sales illustrations, bancassurance anti-tying, free-look periods, liability exclusion disclosure, and claim settlement under Law on Insurance Business 08/2022/QH15 and Circular 67/2023/TT-BTC."
when:
  - "Authoring or auditing insurance policy illustrations, insurance certificates, claim settlement guidelines, and InsurTech digital product interfaces"
  - "Enforcing INS001–INS006 rules in validate_copy.py for vietnamese-insurance-insurtech"
  - "Ensuring compliance with bancassurance anti-coercion regulations and mandatory statutory disclosure standards"
trust_tier: "verified"
version: "5.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md"
    sha256: "a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4"
---

# Vietnamese Insurance Business Law, InsurTech Compliance, and Bancassurance Governance

## Purpose

Defines regulatory compliance requirements, statutory terminology, and consumer protection boundaries for Vietnamese life insurance, general insurance, investment-linked insurance, InsurTech digital platforms, and banking insurance distribution (Bancassurance).

## When to Use / When NOT

- **When to Use:**
  - Drafting or validating insurance sales illustrations (`Tài liệu minh họa bán hàng`), policy summaries, insurance certificates (`Giấy chứng nhận bảo hiểm`), and policy wordings (`Quy tắc và điều khoản bảo hiểm`).
  - Designing claim submission portals, claim settlement guides (`Hướng dẫn giải quyết quyền lợi bảo hiểm`), and rejection notices.
  - Auditing bancassurance scripts, customer acquisition workflows, and digital onboarding to prevent cross-selling coercion and savings confusion.
  - Localizing international insurance and InsurTech platforms into statutory Vietnamese insurance terminology.
- **When NOT to Use:**
  - Statutory social insurance (`Bảo hiểm xã hội` — BHXH) or mandatory state health insurance (`Bảo hiểm y tế` — BHYT) under the Ministry of Labor, Invalids and Social Affairs, which operate under distinct public social welfare laws.

## Core Knowledge Content

### 1. Investment-Linked Insurance & Bancassurance Anti-Coercion Regulations (`INS001`, `INS006`)

Under the Law on Insurance Business 2022 (Luật Kinh doanh bảo hiểm số 08/2022/QH15) and Ministry of Finance Circular 67/2023/TT-BTC, insurers, agents, and bancassurance partners are strictly prohibited from misrepresenting investment-linked life insurance ('bảo hiểm liên kết đầu tư: liên kết chung / liên kết đơn vị') as bank savings deposits with guaranteed interest rates ('tiết kiệm ngân hàng cam kết lãi suất cố định') or coercing borrowers into purchasing non-mandatory insurance as a condition for credit disbursement.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under the Law on Insurance Business 2022 (Luật Kinh doanh bảo hiểm số 08/2022/QH15) and Ministry of Finance Circular 67/2023/TT-BTC, insurers, agents, and bancassurance partners are strictly prohibited from misrepresenting investment-linked life insurance ('bảo hiểm liên kết đầu tư: liên kết chung / liên kết đơn vị') as bank savings deposits with guaranteed interest rates ('tiết kiệm ngân hàng cam kết lãi suất cố định') or coercing borrowers into purchasing non-mandatory insurance as a condition for credit disbursement." -->

### 2. Free-Look Period, Exclusion Clauses, Statutory Roles, and Claim Timelines (`INS002`, `INS003`, `INS004`, `INS005`)

Article 35 of the Law on Insurance Business 2022 mandates a 21-day free-look period ('thời gian cân nhắc tham gia bảo hiểm 21 ngày') for life insurance contracts with terms exceeding 1 year, Article 19 requires explicit affirmative disclosure of liability exclusion clauses ('điều khoản loại trừ trách nhiệm bảo hiểm') to prevent invalidity, Article 4 distinguishes the four statutory roles ('Doanh nghiệp bảo hiểm', 'Bên mua bảo hiểm', 'Người được bảo hiểm', 'Người thụ hưởng'), and Article 31 requires claim payout within 15 days of receiving a complete and valid claim dossier where no contract timeframe is specified.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Article 35 of the Law on Insurance Business 2022 mandates a 21-day free-look period ('thời gian cân nhắc tham gia bảo hiểm 21 ngày') for life insurance contracts with terms exceeding 1 year, Article 19 requires explicit affirmative disclosure of liability exclusion clauses ('điều khoản loại trừ trách nhiệm bảo hiểm') to prevent invalidity, Article 4 distinguishes the four statutory roles ('Doanh nghiệp bảo hiểm', 'Bên mua bảo hiểm', 'Người được bảo hiểm', 'Người thụ hưởng'), and Article 31 requires claim payout within 15 days of receiving a complete and valid claim dossier where no contract timeframe is specified." -->

## Failure Modes (Mandatory)

1. **Disguising Insurance as Bank Savings (`INS001`):** Advertising investment-linked insurance as fixed-yield savings deposits.
2. **Shortening or Omitting the 21-Day Free-Look Period (`INS002`):** Stating 7-day, 10-day, or 14-day free-look, or omitting the 21-day cooling-off notice in sales illustrations.
3. **Concealing Liability Exclusion Clauses (`INS003`):** Promising unconditional payout without exclusions or omitting the exclusions section in certificates.
4. **Machine-Translated Insurance Jargon (`INS004`):** Using literal translationese like `chính sách bảo hiểm`, `người giữ chính sách`, or `tiền thưởng bảo hiểm`.
5. **Excessive Claim Settlement Timelines (`INS005`):** Unlawfully delaying claim payout beyond statutory limits (e.g. claiming 60 or 90 business days).
6. **Coercive Bancassurance Tying (`INS006`):** Forcing loan applicants to buy life insurance as a mandatory condition for loan disbursement.
