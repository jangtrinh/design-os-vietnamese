---
name: vietnamese-ecommerce-retail
description: Drafts, localizes, and audits native-quality Vietnamese (vi-VN) e-commerce storefront copy, product detail pages (PDP), promotional flash sale campaigns, checkout UX microcopy, and customer return policies. Enforces Ministry of Industry and Trade (Bộ Công Thương) badging accuracy under Decree 52/2013/NĐ-CP & Decree 85/2021/NĐ-CP (distinguishing blue 'Đã thông báo' from red 'Đã đăng ký' and banning false quality endorsement claims), statutory 50% promotional discount caps under Decree 81/2018/NĐ-CP & Decree 128/2024/NĐ-CP, mandatory product labeling disclosures under Decree 43/2017/NĐ-CP & Decree 111/2021/NĐ-CP, statutory consumer return rights under the Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng 2023), and eliminates logistics translationese and manipulative checkout dark patterns.
version: "5.0.0"
author: "DESIGN:OS Vietnamese"
license: "PolyForm-Shield-1.0.0"
metadata:
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese E-Commerce, Retail & Consumer Protection (`vietnamese-ecommerce-retail`)

Vietnamese e-commerce and retail storefronts must comply with strict commercial disclosure regulations and consumer protection laws. Misrepresenting the Ministry of Industry and Trade (Bộ Công Thương) blue notification badge as state quality certification violates Decree 52/2013/NĐ-CP and Decree 85/2021/NĐ-CP; running unapproved discounts exceeding the 50% statutory ceiling breaches Decree 81/2018/NĐ-CP and Decree 128/2024/NĐ-CP; writing unconditional "miễn đổi trả trong mọi trường hợp" clauses is void ab initio under the Law on Protection of Consumers' Rights 2023; omitting origin information on product listings violates Decree 43/2017/NĐ-CP; and using literal logistics calques like "Ra ngoài để giao hàng" or manipulative dark patterns destroys consumer trust.

This skill equips e-commerce platform developers, D2C brand marketers, catalog operations teams, and customer service specialists with authoritative Vietnamese e-commerce phrasing, statutory consumer protection boundaries, and automated linting rules.

---

## When to Use

Use this skill when:
- Authoring or auditing e-commerce product detail pages (PDP), catalog specs, and electronic product labels.
- Formulating commercial promotions, discount campaigns, flash sales, voucher terms, and marketing banners.
- Drafting or reviewing customer return, refund, warranty, and cash-on-delivery (COD) policies.
- Developing checkout microcopy, order tracking statuses, and shipping notification messages.
- Running copy validation using `--domain vietnamese-ecommerce-retail` or `--doctype product-pdp / flash-sale-promo / return-policy`.

---

## Quick Start

Validate e-commerce copy and policy instruments with the command-line validator:

```bash
# Validate a product detail page (PDP)
python shared/scripts/validate_copy.py san-pham.md --domain vietnamese-ecommerce-retail --doctype product-pdp --strict

# Validate a promotional campaign banner or flash-sale terms
python shared/scripts/validate_copy.py flash-sale.md --domain vietnamese-ecommerce-retail --doctype flash-sale-promo --strict

# Validate a customer return and refund policy
python shared/scripts/validate_copy.py doi-tra.md --domain vietnamese-ecommerce-retail --doctype return-policy --strict
```

---

## Register Matrix

E-commerce surfaces balance conversion velocity with statutory consumer transparency:

| Surface / Flow | Target Register | Address (`Hô`) | Speaker (`Xưng`) | Tone & Statutory Standard |
|---|---|---|---|---|
| E-Commerce Shopper UX & PDP | `ecommerce-shopper` | `Bạn` | `Chúng tôi` / Tên thương hiệu | Friendly, helpful, transparent; clear prices with period thousand separators (`250.000 ₫`). |
| Return & Warranty Policy | `legal-contract` | `Người tiêu dùng` / `Khách hàng` | `Người bán` / `Doanh nghiệp` | Objective, legally precise, non-adversarial; compliant with Luật BVQLNTD 2023. |
| Customer Support & Order Updates | `consult` | `Anh/chị` | `Em` / `Shop` | Warm, attentive, solutions-oriented; standard order statuses per logistics conventions. |

---

## Core Rules

The e-commerce validator enforces 6 domain-specific rules (`ECOM001`–`ECOM006`):

### 1. `ECOM001` (ERROR) — MoIT Badging Accuracy & Quality Claim Ban
- **Statute:** Decree 52/2013/NĐ-CP and Decree 85/2021/NĐ-CP on E-Commerce.
- **Rule:** Differentiate the blue "Đã thông báo Bộ Công Thương" badge (for sales websites/apps) from the red "Đã đăng ký Bộ Công Thương" badge (for marketplace platforms).
- **Prohibition:** Falsely claiming that Ministry of Industry and Trade notification or registration constitutes government quality certification (`Bộ Công Thương bảo chứng chất lượng 100%`, `Logo Bộ Công Thương chứng nhận hàng chính hãng tuyệt đối`).

### 2. `ECOM002` (ERROR) — Statutory 50% Promotional Discount Ceiling & Fake Anchors
- **Statute:** Decree 81/2018/NĐ-CP and Decree 128/2024/NĐ-CP on commercial promotions.
- **Rule:** Promotional discounts cannot exceed **50% of the pre-promotion price**, except during officially organized state concentrated promotion programs (`Tháng khuyến mại tập trung quốc gia`) or liquidation of discontinued inventory.
- **Prohibition:** Advertising unapproved 60%–90% discounts or fabricating inflated pre-discount prices to display fake discounts (`nâng khống giá gốc để giảm giá ảo`).

### 3. `ECOM003` (ERROR) — Unlawful Blanket No-Return Policies
- **Statute:** Article 25 of the Law on Protection of Consumers' Rights 2023 (Luật Bảo vệ quyền lợi người tiêu dùng 2023).
- **Rule:** Consumers have an inalienable statutory right to return defective goods, receive replacements, or obtain refunds when products fail to match descriptions or suffer manufacturer defects.
- **Prohibition:** Blanket clauses such as "Hàng mua rồi miễn đổi trả trong mọi trường hợp" or denying inspection and refunds for defective merchandise are void ab initio.

### 4. `ECOM004` (WARN) — Mandatory Vietnamese Product Labeling Disclosures (PDP)
- **Statute:** Decree 43/2017/NĐ-CP and Decree 111/2021/NĐ-CP on goods labeling.
- **Rule:** Product detail pages (`doctype == "product-pdp"`) must display mandatory labeling items:
  1. Product origin (`Xuất xứ` / `Sản xuất tại`).
  2. Responsible commercial entity (`Thương nhân chịu trách nhiệm` / `Nhà sản xuất` / `Đơn vị nhập khẩu`).

### 5. `ECOM005` (WARN) — Awkward E-Commerce & Logistics Calques
- **Rule:** Replace literal machine translations with conventional Vietnamese e-commerce terms:
  - `Ra ngoài để giao hàng` ➔ `Đang giao hàng`
  - `Sự hoàn thành đơn hàng` ➔ `Hoàn tất đơn hàng`
  - `Thêm vào xe đẩy` / `Bỏ vào giỏ xe` ➔ `Thêm vào giỏ hàng`
  - `Tiền mặt trên giao hàng` ➔ `Thanh toán khi nhận hàng (COD)`
  - `Chính sách trở lại` ➔ `Chính sách đổi trả`
  - `Người vận chuyển cuối cùng` ➔ `Đơn vị vận chuyển chặng cuối`

### 6. `ECOM006` (ERROR) — Prohibited Checkout Dark Patterns & Coercion
- **Statute:** Article 10 of the Law on Protection of Consumers' Rights 2023.
- **Rule:** Checkout funnels must respect user autonomy and transparency.
- **Prohibition:** Coercive guilt manipulation ("Nhân viên giao hàng sẽ bị trừ lương nếu bạn hủy đơn"), unjustified threats of account closure for non-payment within minutes, and automatic hidden enrollment in paid recurring subscriptions without explicit affirmative consent.

---

## Workflow

To publish compliant e-commerce listings and campaigns, execute this 4-step workflow:

1. **Step 1: Audit Promotional Pricing & Discounts:**
   - Verify that advertised discounts do not exceed the 50% cap unless tied to an authorized concentrated promotion program (`ECOM002`).
   - Format prices with periods for thousands separators (`250.000 ₫`) and never commas (`NUM001`).
2. **Step 2: Inspect PDP Mandatory Disclosures:**
   - Ensure the product listing includes product name, origin (`Xuất xứ`), and responsible entity details (`ECOM004`).
   - Eliminate misleading claims regarding Ministry of Industry and Trade product quality endorsement (`ECOM001`).
3. **Step 3: Verify Return & Checkout Terms:**
   - Review return and exchange clauses to eliminate illegal blanket return bans (`ECOM003`).
   - Check checkout copy to remove coercive dark patterns or sneaky continuity subscriptions (`ECOM006`).
4. **Step 4: Execute Linter QA Gate:**
   - Run `validate_copy.py` with `--domain vietnamese-ecommerce-retail` and declared `--doctype`.
   - Ensure natural logistics status wording (`ECOM005`) and register pronoun consistency (`ecommerce-shopper`).

---

## Bundled References

- [references/tmdt-nd52-nd85-va-bct.md](references/tmdt-nd52-nd85-va-bct.md) — Decree 52/2013/NĐ-CP & Decree 85/2021/NĐ-CP: MoIT notification vs. registration logos and mandatory storefront disclosures.
- [references/khuyen-mai-nd81-nd128-va-bvqlntd.md](references/khuyen-mai-nd81-nd128-va-bvqlntd.md) — Decree 81/2018/NĐ-CP discount limits, Consumer Protection Law 2023 void clauses, PDP labeling, and dark pattern prohibitions.
- [references/ecommerce-logistics-and-calques.md](references/ecommerce-logistics-and-calques.md) — E-commerce lifecycle statuses, payment terms (COD/BNPL), and English-Vietnamese logistics calque blocklist.
