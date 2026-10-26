---
name: vietnamese-real-estate-construction
description: Drafts, localizes, and audits native-quality Vietnamese (vi-VN) real estate project communications, off-plan residential sales contracts, booking agreements, condominium brochures, and construction BOQ specifications. Enforces statutory deposit caps (5%) under Article 23 Clause 5 and installment payment schedules (30%/70%/95%) under Article 25 of the Law on Real Estate Business 2023 (Luật Kinh doanh bất động sản 2023), land tenure accuracy (condotel/officetel 50-year leasehold vs residential title) under Land Law 2024 (Luật Đất đai 2024), apartment carpet area (thông thủy vs tim tường) under Article 141 and mandatory 2% apartment maintenance fund under Article 152 of Housing Law 2023 (Luật Nhà ở 2023), and eliminates construction BOQ English calques under Decree 37/2015/NĐ-CP.
version: "5.0.0"
author: "DESIGN:OS Vietnamese"
license: "PolyForm-Shield-1.0.0"
metadata:
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Real Estate & Construction Engineering (`vietnamese-real-estate-construction`)

In Vietnamese real estate and construction, precision in statutory disclosures is vital. Marketing an off-plan property with deposit terms exceeding 5% violates the Law on Real Estate Business 2023; promising "sổ đỏ lâu dài" for condotels or officetels breaches Land Law 2024; stating apartment areas without distinguishing usable carpet area (`diện tích thông thủy`) from gross area (`diện tích tim tường`) breaches Housing Law 2023; and using literal English calques like "vùng xanh lá cây" or "tài sản thực" signals unvetted machine translation.

This skill equips property developers, project marketing agencies, legal counsels, and general contractors with authoritative, verified Vietnamese real estate drafting rules, statutory compliance checks, and linter automation aligned with current 2023–2024 legislation.

---

## When to Use

Use this skill when:
- Authoring or auditing off-plan sales contracts (`Hợp đồng mua bán nhà ở hình thành trong tương lai`), deposit agreements (`Thỏa thuận đặt cọc`), and payment schedules in Vietnam.
- Preparing marketing brochures, landing pages, and sales kit materials for residential apartments, villas, condotels, officetels, and commercial shophouses.
- Formulating construction bidding documents, bills of quantities (BOQ), and site acceptance certificates (`Biên bản nghiệm thu bàn giao`).
- Running copy validation using `--domain vietnamese-real-estate-construction` or `--doctype off-plan-contract / project-brochure / construction-boq`.

---

## Quick Start

Validate real estate copy and construction contracts with the command-line validator:

```bash
# Validate an off-plan sales contract
python shared/scripts/validate_copy.py hop-dong-mua-ban.md --domain vietnamese-real-estate-construction --doctype off-plan-contract --strict

# Validate a property project brochure
python shared/scripts/validate_copy.py brochure-du-an.md --domain vietnamese-real-estate-construction --doctype project-brochure --strict

# Validate a construction procurement BOQ specification
python shared/scripts/validate_copy.py boq-goi-thau.md --domain vietnamese-real-estate-construction --doctype construction-boq --strict
```

---

## Register Matrix

Real estate and construction copy demands tailored sociolinguistic registers:

| Document / Surface | Target Register | Address (`Hô`) | Speaker (`Xưng`) | Tone & Statutory Standard |
|---|---|---|---|---|
| Luxury Residential Project Brochure | `realestate-luxury` | `Quý khách` | `Chúng tôi` / `Chủ đầu tư` | Refined, respectful, architectural elegance; zero casual pronouns (`bạn`, `mình`). |
| Off-Plan Apartment Sales Contract | `legal-contract` | `Bên B` / `Bên Mua` | `Bên A` / `Chủ đầu tư` | Third-person statutory precision per Luật KDBĐS 2023 & Luật Nhà ở 2023. |
| Construction BOQ & Site Acceptance | `construction-b2b` | `Nhà thầu thi công` | `Chủ đầu tư` / `Tư vấn giám sát` | Technical engineering rigor; zero marketing fluff; strict metric symbols (`m²`, `m³`). |

---

## Core Rules

The real estate validator enforces 6 domain-specific rules (`REA001`–`REA006`):

### 1. `REA001` (ERROR) — Off-Plan Deposit Cap (5%) & Capital Mobilization
- **Statute:** Article 23 Clause 5 of the Law on Real Estate Business 2023 (Luật Kinh doanh bất động sản 2023).
- **Rule:** Off-plan property deposits (`tiền đặt cọc`) cannot exceed **5% of the selling or lease-purchase price**.
- **Prohibition:** Disguised capital mobilization through goodwill booking agreements or capital contribution agreements (`hợp đồng góp vốn / giữ chỗ thiện chí`) collecting 10%–30% prior to satisfying statutory sale conditions is strictly prohibited.

### 2. `REA002` (ERROR) — Statutory Installment Payment Schedule
- **Statute:** Article 25 of the Law on Real Estate Business 2023.
- **Rule:** Payment schedules must strictly respect phased completion ceilings:
  - First installment (`thanh toán đợt 1` / `đợt đầu`): maximum **30% of contract value** (inclusive of deposit).
  - Cumulative payments prior to handover (`trước khi bàn giao nhà`): maximum **70% of contract value** (or **50%** for foreign-invested enterprises / FDI developers).
  - Cumulative payments prior to certificate issuance (`trước khi cấp Giấy chứng nhận`): maximum **95% of contract value**. Collecting 100% before certificate grant is prohibited.

### 3. `REA003` (ERROR) — Land Tenure Accuracy for Commercial-Service Properties
- **Statute:** Article 134 of Land Law 2024 (Luật Đất đai 2024).
- **Rule:** Commercial-service properties (`condotel`, `officetel`, `căn hộ du lịch`, `biệt thự nghỉ dưỡng`, `shophouse thương mại dịch vụ`) situated on commercial land have finite leasehold tenure (typically 50 years, or up to 70 years).
- **Prohibition:** Promising permanent residential title (`sổ đỏ lâu dài`, `sổ hồng vĩnh viễn`, `sở hữu lâu dài`) for commercial-service units is unlawful and deceptive.

### 4. `REA004` (WARN) — Apartment Carpet Area vs. Wall-Center Area
- **Statute:** Article 141 of Housing Law 2023 (Luật Nhà ở 2023).
- **Rule:** Stating apartment area requires explicit clarification of usable carpet area (`diện tích thông thủy`) and wall-center gross area (`diện tích tim tường`).
- **Prohibition:** Using ambiguous terms like `diện tích phủ bì` or stating `diện tích căn hộ` without distinguishing carpet from wall-center dimensions.

### 5. `REA005` (ERROR) — Mandatory 2% Apartment Maintenance Fund
- **Statute:** Article 152 of Housing Law 2023.
- **Rule:** All apartment sales contracts must explicitly disclose the **2% common maintenance fund** (`kinh phí bảo trì phần sở hữu chung nhà chung cư 2%`).
- **Prohibition:** Charging maintenance funds in excess of 2% (e.g. 3% or 5%) or demanding payment of the 2% fund at the deposit stage or initial installment before physical handover.

### 6. `REA006` (WARN) — Literal English Calques in Real Estate & BOQ
- **Rule:** Eliminate awkward literal translations and calques:
  - `vùng xanh lá cây` ➔ `mảng xanh` / `công viên cây xanh`
  - `tài sản thực` ➔ `bất động sản`
  - `danh sách số lượng` ➔ `bảng tiên lượng mời thầu / bảng khối lượng mời thầu (BOQ)`
  - `căn hộ trên kế hoạch` / `tài sản ngoài kế hoạch` ➔ `nhà ở hình thành trong tương lai` / `bất động sản hình thành trong tương lai`
  - `bàn giao thô ráp` ➔ `bàn giao thô`
  - `chứng chỉ hoàn thành thực chất` ➔ `biên bản nghiệm thu hoàn thành công trình đưa vào sử dụng`

---

## Workflow

To draft or audit compliant real estate instruments, execute this 4-step workflow:

1. **Step 1: Classify Asset Type & Land Tenure:**
   - Determine whether the project is residential (đất ở lâu dài) or commercial-service (đất thương mại dịch vụ 50 năm).
   - Enforce explicit leasehold disclosures for condotels, officetels, and commercial shophouses (`REA003`).
2. **Step 2: Audit Deposit & Payment Milestones:**
   - Verify that deposit amounts do not exceed the 5% cap under Article 23 Clause 5 Luật KDBĐS 2023 (`REA001`).
   - Audit installment schedules against the 30% / 70% (50% FDI) / 95% statutory thresholds (`REA002`).
3. **Step 3: Verify Metric Standards & Maintenance Fund:**
   - Confirm explicit statement of both `diện tích thông thủy` and `diện tích tim tường` (`REA004`).
   - Ensure the 2% maintenance fund is scheduled at handover, never at deposit (`REA005`).
   - Format metric exponents using superscript Unicode (`m²`, `m³`) per `NUM004`.
4. **Step 4: Execute Linter & Address Checks:**
   - Run `validate_copy.py` with `--domain vietnamese-real-estate-construction` and declared `--doctype`.
   - Ensure zero pronoun leakage (`PRO001`, `PRO002`) and zero unverified superlatives (`LAW001`).

---

## Bundled References

- [references/luat-kinh-doanh-bds-2023.md](references/luat-kinh-doanh-bds-2023.md) — Comprehensive guide to the Law on Real Estate Business 2023: 5% deposit cap, 30%/70%/95% payment schedules, and bank guarantees.
- [references/luat-dat-dai-2024-va-nha-o-2023.md](references/luat-dat-dai-2024-va-nha-o-2023.md) — Land Law 2024 & Housing Law 2023: commercial land tenure limits, carpet area measurement rules, and 2% maintenance fund requirements.
- [references/construction-boq-and-calques.md](references/construction-boq-and-calques.md) — Decree 37/2015/NĐ-CP construction contracts, BOQ standards, and English-Vietnamese calque blocklist.
