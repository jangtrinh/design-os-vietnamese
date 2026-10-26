---
id: "statutory-compliance-vi"
title: "Vietnamese Statutory Compliance: Advertising Law 75/2025/QH15, PDPD Decree 13/2023, and Promotions Decree 128/2024"
domain: "vietnamese-legal-and-regulatory-compliance"
description: "Verified statutory compliance requirements for Vietnamese advertising copy, influencer disclosures, personal data protection (PDPD), promotional discount caps, and anti-spam telecommunications."
when:
  - "Reviewing landing pages, ad copy, pricing tables, consent modals, or promotional campaigns for the Vietnam market"
  - "Enforcing LAW001 unverified superlative restrictions and Decree 13/2023/NĐ-CP explicit consent"
  - "Validating promotional discount percentages against Decree 81/2018/NĐ-CP and Decree 128/2024/NĐ-CP"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md"
    sha256: "c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290"
---

# Vietnamese Statutory Compliance: Advertising Law 75/2025/QH15, PDPD Decree 13/2023, and Promotions Decree 128/2024

## Purpose

Codifies the binding Vietnamese statutory requirements governing digital advertising claims, influencer sponsorship disclosures, personal data consent flows, promotional discount caps, and anti-spam messaging.

## When to Use / When NOT

- **When to Use:**
  - Auditing marketing landing pages, checkout consent checkboxes, promotional banners, SMS/ZNS templates, and e-commerce footers targeting users in Vietnam.
- **When NOT to Use:**
  - Internal engineering architecture diagrams or non-commercial academic papers that make no product, pricing, or data-collection claims.

## Core Knowledge Content

### 1. Law on Advertising 2012 & Law No. 75/2025/QH15 (`LAW001`)

Article 8 Clause 11 of the Law on Advertising 2012 (Luật Quảng cáo số 16/2012/QH13), as amended by Law No. 75/2025/QH15 (effective 01/01/2026), prohibits advertising that uses `nhất`, `duy nhất`, `tốt nhất`, `số một` or words of equivalent meaning without statutory supporting documentation, and mandates explicit sponsorship disclosure by influencers (KOL/KOC).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Article 8 Clause 11 of the Law on Advertising 2012 (Luật Quảng cáo số 16/2012/QH13), as amended by Law No. 75/2025/QH15 (effective 01/01/2026), prohibits advertising that uses 'nhất', 'duy nhất', 'tốt nhất', 'số một' or words of equivalent meaning without statutory supporting documentation, and mandates explicit sponsorship disclosure by influencers (KOL/KOC)." -->

### 2. Personal Data Protection Decree 13/2023/NĐ-CP (PDPD)

Decree 13/2023/NĐ-CP on Personal Data Protection (PDPD) invalidates pre-ticked checkboxes and implied "By continuing you agree" banners; Article 11 requires explicit consent covering data types, processing purposes, third parties, and data subject rights, while Article 20 mandates dual verification of both the child's consent (for ages 7 to under 16) and the parent or legal guardian's consent.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Decree 13/2023/NĐ-CP on Personal Data Protection (PDPD) invalidates pre-ticked checkboxes and implied 'By continuing you agree' banners; Article 11 requires explicit consent covering data types, processing purposes, third parties, and data subject rights, while Article 20 mandates dual verification of both the child's consent (for ages 7 to under 16) and the parent or legal guardian's consent." -->

### 3. Promotional Discount Caps: Decree 81/2018/NĐ-CP & Decree 128/2024/NĐ-CP

Decree 81/2018/NĐ-CP (Article 6 & 7) as amended by Decree 128/2024/NĐ-CP caps standard commercial promotional discounts at 50% of the goods/service price immediately preceding the promotion, permitting up to 100% discount only within government-organized concentrated promotional programs (`Tháng khuyến mại tập trung quốc gia`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Decree 81/2018/NĐ-CP (Article 6 & 7) as amended by Decree 128/2024/NĐ-CP caps standard commercial promotional discounts at 50% of the goods/service price immediately preceding the promotion, permitting up to 100% discount only within government-organized concentrated promotional programs (Tháng khuyến mại tập trung quốc gia)." -->

### 4. Anti-Spam Telecommunications: Decree 91/2020/NĐ-CP

Decree 91/2020/NĐ-CP on anti-spam telecommunications requires prior opt-in, advertiser prefix tagging (`[QC]`), and explicit free opt-out syntax (`Soạn TC gửi...`) for promotional SMS/ZNS/emails, and strictly forbids disguising promotional incentives inside transactional Zalo Notification Service (ZNS) templates.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Decree 91/2020/NĐ-CP on anti-spam telecommunications requires prior opt-in, advertiser prefix tagging ('[QC]'), and explicit free opt-out syntax ('Soạn TC gửi...') for promotional SMS/ZNS/emails, and strictly forbids disguising promotional incentives inside transactional Zalo Notification Service (ZNS) templates." -->

## Failure Modes (Mandatory)

1. **Unverified Superlative Headline (`LAW001`):** Publishing `Nền tảng quản lý bán hàng số 1 Việt Nam` without citing a dated market research report or government award triggers statutory penalties under Article 8 Clause 11 of the Law on Advertising.
2. **Invalid Implied Consent Banner (PDPD Decree 13/2023):** Using `Bằng việc tiếp tục sử dụng trang web, bạn đồng ý với Chính sách bảo mật` or pre-checked consent boxes violates Article 11 of Decree 13/2023/NĐ-CP.
3. **Illegal >50% Self-Run Flash Sale (Decree 81/2018 & 128/2024):** Running an ordinary merchant promotion advertised as `Giảm giá 70%–90% toàn bộ sản phẩm` outside a state-sponsored concentrated promotional program violates the 50% statutory cap.
