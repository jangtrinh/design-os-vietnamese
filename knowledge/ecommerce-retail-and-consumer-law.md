---
id: "ecommerce-retail-and-consumer-law"
title: "Vietnamese E-Commerce, Retail & Consumer Protection Compliance: Decree 52/2013/NĐ-CP, Decree 85/2021/NĐ-CP, Decree 81/2018/NĐ-CP, and Law on Protection of Consumers' Rights 19/2023/QH15"
domain: "vietnamese-ecommerce-and-retail"
description: "Verified statutory specifications for e-commerce website notification badges (Blue vs Red), promotional discount caps (50%), mandatory Vietnamese product labeling (NĐ 43/2017 & NĐ 111/2021), and unlawful return-refusal prohibitions."
when:
  - "Authoring or auditing e-commerce product detail pages (PDP), promotional flash sale campaigns, checkout flows, and return policies"
  - "Enforcing ECOM001–ECOM006 rules in validate_copy.py for vietnamese-ecommerce-retail"
  - "Auditing consumer transparency and regulatory badge representations under MoIT regulations"
trust_tier: "verified"
version: "5.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md"
    sha256: "a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4"
---

# Vietnamese E-Commerce, Retail & Consumer Protection Compliance: Decree 52/2013/NĐ-CP, Decree 85/2021/NĐ-CP, Decree 81/2018/NĐ-CP, and Law on Protection of Consumers' Rights 19/2023/QH15

## Purpose

Defines statutory consumer protection and commercial disclosure requirements for Vietnamese e-commerce storefronts, marketplace platforms, promotional campaigns (flash sales), digital checkout flows, and product return policies.

## When to Use / When NOT

- **When to Use:**
  - Authoring or auditing e-commerce PDPs, checkout funnels, promotional terms, return/warranty policies, and shipping notices in Vietnam.
  - Ensuring compliance with Decree 52/2013/NĐ-CP & Decree 85/2021/NĐ-CP (E-Commerce), Decree 81/2018/NĐ-CP & Decree 128/2024/NĐ-CP (Promotions), Decree 43/2017/NĐ-CP & Decree 111/2021/NĐ-CP (Product Labeling), and Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng số 19/2023/QH15).
- **When NOT to Use:**
  - B2B construction procurement contracts or residential off-plan real estate agreements governed by specialized construction/property codes.

## Core Knowledge Content

### 1. MoIT E-Commerce Badging & Quality Endorsement Prohibitions (`ECOM001`)

E-commerce websites and marketplaces in Vietnam are subject to distinct regulatory regimes under the Ministry of Industry and Trade (Bộ Công Thương).
Under Decree 52/2013/NĐ-CP and Decree 85/2021/NĐ-CP on E-Commerce, sales websites/apps ('website/ứng dụng thương mại điện tử bán hàng') display the blue 'Đã thông báo Bộ Công Thương' badge whereas e-commerce marketplace/service platforms ('sàn giao dịch thương mại điện tử') display the red 'Đã đăng ký Bộ Công Thương' badge, and merchants must never claim that Ministry of Industry and Trade notification constitutes state certification of product quality or origin.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under Decree 52/2013/NĐ-CP and Decree 85/2021/NĐ-CP on E-Commerce, sales websites/apps ('website/ứng dụng thương mại điện tử bán hàng') display the blue 'Đã thông báo Bộ Công Thương' badge whereas e-commerce marketplace/service platforms ('sàn giao dịch thương mại điện tử') display the red 'Đã đăng ký Bộ Công Thương' badge, and merchants must never claim that Ministry of Industry and Trade notification constitutes state certification of product quality or origin." -->

### 2. Statutory Promotion Discount Cap (50%), Return Rights, and Mandatory Product Labeling (`ECOM002`, `ECOM003`, `ECOM004`)

Promotional campaigns and commercial sales must respect statutory price limits and consumer return protections.
Under Decree 81/2018/NĐ-CP and Decree 128/2024/NĐ-CP on commercial promotions, maximum discount rates ('hạn mức tối đa về giá trị hàng hóa, dịch vụ dùng để khuyến mại') cannot exceed 50% of the pre-promotion price except during state-organized concentrated promotion programs; concurrently, the Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng số 19/2023/QH15) and Decree 43/2017/NĐ-CP (amended by Decree 111/2021/NĐ-CP) prohibit unconditional 'no return under any circumstances' ('mua rồi miễn đổi trả mọi trường hợp') clauses and require mandatory Vietnamese product labeling (product name, origin, responsible entity, and manufacturing/expiry dates).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under Decree 81/2018/NĐ-CP and Decree 128/2024/NĐ-CP on commercial promotions, maximum discount rates ('hạn mức tối đa về giá trị hàng hóa, dịch vụ dùng để khuyến mại') cannot exceed 50% of the pre-promotion price except during state-organized concentrated promotion programs; concurrently, the Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng số 19/2023/QH15) and Decree 43/2017/NĐ-CP (amended by Decree 111/2021/NĐ-CP) prohibit unconditional 'no return under any circumstances' ('mua rồi miễn đổi trả mọi trường hợp') clauses and require mandatory Vietnamese product labeling (product name, origin, responsible entity, and manufacturing/expiry dates)." -->

## Failure Modes (Mandatory)

1. **MoIT Badge Confusion & Quality Certification Misrepresentations (`ECOM001`):** Claiming an e-commerce platform only needs the blue "Đã thông báo" badge or claiming MoIT notification certifies genuine product authenticity 100%.
2. **Promotions Exceeding 50% Discount Cap (`ECOM002`):** Advertising 70%–90% discounts without state concentrated promotion authorization or fabricating pre-discount anchor prices.
3. **Unlawful Blanket No-Return Clauses (`ECOM003`):** Denying returns under all circumstances, even for defective goods or manufacturer errors, violating Consumer Protection Law 2023.
4. **Missing Mandatory Vietnamese Labeling (`ECOM004`):** Omitting origin (`Xuất xứ`), manufacturer, or responsible business entity details on product listings.
5. **Machine-Translated Logistics Calques (`ECOM005`):** Using literal translationese like `Ra ngoài để giao hàng` instead of `Đang giao hàng` or `Tiền mặt trên giao hàng` instead of `Thanh toán khi nhận hàng (COD)`.
6. **Dark-Pattern Urgency and Coercion (`ECOM006`):** Threatening salary deductions for couriers if buyers cancel, or claiming account termination for non-payment within minutes.
