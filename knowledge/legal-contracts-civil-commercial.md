---
id: "legal-contracts-civil-commercial"
title: "Vietnamese Contract & Corporate Law: Civil Code 2015, Commercial Law 2005 (8% Penalty Cap), and Consumer Protection Law 2023"
domain: "vietnamese-legal-and-contracts"
description: "Verified specification for drafting Vietnamese civil, commercial, labor, and consumer contracts under the Civil Code 2015, Commercial Law 2005 (Article 301), Labor Code 2019 (Article 20), and Consumer Protection Law 2023 (Article 25)."
when:
  - "Drafting or auditing B2B service contracts, civil leases, labor contracts, Terms of Service (ToS), or PDPD Data Processing Agreements (DPA)"
  - "Enforcing LEG001–LEG007 rules in validate_copy.py for vietnamese-legal-contracts"
  - "Replacing Anglo-American common-law translationese calques with authentic Vietnamese civil-law terminology"
trust_tier: "verified"
version: "4.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md"
    sha256: "a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed"
---

# Vietnamese Contract & Corporate Law: Civil Code 2015, Commercial Law 2005 (8% Penalty Cap), and Consumer Protection Law 2023

## Purpose

Defines the statutory contract rules, penalty caps, labor contract classifications, consumer protection safeguards, and legislative citation ordering required for enforceable Vietnamese legal instruments.

## When to Use / When NOT

- **When to Use:**
  - Authoring or reviewing B2B commercial contracts (`Hợp đồng cung ứng dịch vụ`), civil agreements, labor contracts (`Hợp đồng lao động`), Terms of Service (`Điều khoản sử dụng`), and PDPD Privacy Policies / DPAs in Vietnam.
- **When NOT to Use:**
  - Contracts governed exclusively by foreign law (e.g., Singapore or English law) where Vietnamese statutory caps do not apply.

## Core Knowledge Content

### 1. Commercial Breach Penalty 8% Cap vs Civil Penalty (`LEG001`)

Article 301 of the Commercial Law 2005 (Luật Thương mại số 36/2005/QH11) caps contractual breach penalties (`phạt vi phạm`) in commercial contracts at 8% of the value of the breached contractual obligation, contrasting with civil contracts under Article 418 of the Civil Code 2015 (Bộ luật Dân sự số 91/2015/QH13) where penalty levels are freely agreed by the parties.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Article 301 of the Commercial Law 2005 (Luật Thương mại số 36/2005/QH11) caps contractual breach penalties ('phạt vi phạm') in commercial contracts at 8% of the value of the breached contractual obligation, contrasting with civil contracts under Article 418 of the Civil Code 2015 (Bộ luật Dân sự số 91/2015/QH13) where penalty levels are freely agreed by the parties." -->

### 2. Abolition of Seasonal Labor Contracts (`LEG002`)

Article 20 of the Labor Code 2019 (Bộ luật Lao động số 45/2019/QH14) abolished seasonal labor contracts (`hợp đồng lao động mùa vụ`), permitting only indefinite-term contracts (`hợp đồng lao động không xác định thời hạn`) and fixed-term contracts not exceeding 36 months (`hợp đồng lao động xác định thời hạn không quá 36 tháng`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Article 20 of the Labor Code 2019 (Bộ luật Lao động số 45/2019/QH14) abolished seasonal labor contracts ('hợp đồng lao động mùa vụ'), permitting only indefinite-term contracts ('hợp đồng lao động không xác định thời hạn') and fixed-term contracts not exceeding 36 months ('hợp đồng lao động xác định thời hạn không quá 36 tháng')." -->

### 3. Consumer Protection Liability Waivers and Statutory Citation Hierarchy (`LEG003`, `LEG004`)

Article 25 of the Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng số 19/2023/QH15) invalidates standard-form contract clauses that unconditionally exempt the business from statutory liability; additionally, Vietnamese statutory citations must follow ascending-to-descending or specific-to-general Vietnamese legislative hierarchy (`Điểm a Khoản 2 Điều 15`) rather than Anglo-American `Điều 15.2(a)`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Article 25 of the Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng số 19/2023/QH15) invalidates standard-form contract clauses that unconditionally exempt the business from statutory liability; additionally, Vietnamese statutory citations must follow ascending-to-descending or specific-to-general Vietnamese legislative hierarchy ('Điểm a Khoản 2 Điều 15') rather than Anglo-American 'Điều 15.2(a)'." -->

## Failure Modes (Mandatory)

1. **Illegal >8% Penalty Clause in Commercial Contracts (`LEG001`):** Drafting `Bên vi phạm chịu phạt 20% tổng giá trị Hợp đồng` in a B2B commercial service contract governed by the Commercial Law 2005.
2. **Drafting Abolished Seasonal Labor Contracts (`LEG002`):** Using a pre-2021 template titled `Hợp đồng lao động mùa vụ` instead of a fixed-term labor contract under Article 20 of the Labor Code 2019.
3. **Unenforceable Blanket Liability Waivers (`LEG004`):** Copying US SaaS boilerplate `Trong mọi trường hợp, Công ty hoàn toàn không chịu bất kỳ trách nhiệm nào đối với người tiêu dùng` into a Vietnamese consumer ToS.
