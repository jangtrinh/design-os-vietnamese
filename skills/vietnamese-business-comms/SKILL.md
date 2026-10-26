---
name: vietnamese-business-comms
description: "Authoritative Vietnamese omnichannel marketing and B2B commercial communications engineering skill for DESIGN:OS. Enforces strict linguistic pragmatics (xưng - hô), channel quotas, and statutory compliance across Zalo OA (ZNS/ZBS 400-char NFC limit), email campaigns, Shopee/Lazada/TikTok Shop product titles and livestream scripts, corporate press releases, KOL/KOC briefs under Luật 75/2025/QH15, B2B cold outreach, commercial quotations (báo giá with VAT and validity terms), dunning sequences (T-3 to T+30), administrative dispatches (công văn under Nghị định 30/2020/NĐ-CP), and corporate Tết/holiday greetings."
repository: "https://github.com/jangtrinh/design-os-vietnamese"
version: "1.0.0"
category: "linguistic-engineering"
locales: ["vi-VN"]
---

# Vietnamese Business Communications (`vietnamese-business-comms`)

Authoritative linguistic engineering and compliance skill for omnichannel business, sales, marketing, and administrative communications in Vietnamese (`vi-VN`).

Vietnamese business communication differs fundamentally from English: there is **no neutral "you."** Every interaction encodes hierarchy, age, institutional authority, and channel context directly into the pronoun pair (**xưng – hô**). In addition, Vietnamese commercial law actively penalizes misleading marketing, unproven superlatives, undisclosed influencer sponsorships, unauthorized discounts, and non-compliant administrative formats.

This skill equips agents and engineers to draft, review, and validate production-ready copy across all B2B and B2C touchpoints with automated linter enforcement.

---

## 1. Trigger Scenarios & Activation Keywords

Activate this skill whenever generating, reviewing, or translating copy for:
- **Zalo OA:** ZNS transactional templates, ZBS promotional broadcasts, customer care automation.
- **E-Commerce & Marketplaces:** Shopee, Lazada, TikTok Shop product titles, descriptions, and livestream sales scripts.
- **B2B Commercial Outreach:** B2B cold emails, partnership pitches, follow-ups, and senior executive correspondence.
- **Commercial Documents:** Báo giá (quotations), hợp đồng nguyên tắc (MSAs), phạm vi công việc (SOWs), and biên bản làm việc.
- **Financial Dunning:** Payment reminders and accounts receivable escalation sequences (T-3 to T+30).
- **Public & Corporate Relations:** Thông cáo báo chí (press releases), executive interview briefs, and brand manifestos.
- **Administrative Clerical:** Công văn, tờ trình, thông báo, biên bản conforming to Nghị định 30/2020/NĐ-CP.
- **Seasonal Corporate:** Thư chúc Tết, thiệp chúc mừng năm mới, thông báo lịch nghỉ lễ và trực Tết.

---

## 2. Pragmatics & Register Matrix (`--register`)

Vietnamese business communication operates on strict register boundaries:

<!-- machine-readable: comms-registers -->

| Register | Expects (`Hô`) | Forbids | Primary Touchpoints & Tone |
|---|---|---|---|
| `b2b` | `anh/chị` | `bạn`, `quý vị`, `cả nhà` | B2B cold outreach, sales proposals, báo giá, commercial follow-ups |
| `zns` | `quý khách` | `bạn`, `mình`, `cả nhà` | Zalo OA ZNS/ZBS transactional and customer care notifications |
| `press` | `quý vị` | `bạn`, `mình`, `bọn mình`, `cả nhà` | Corporate press releases, public announcements, investor updates |
| `livestream` | `cả nhà` | `quý vị`, `quý khách` | TikTok Shop / Shopee Live spoken selling scripts, social commerce |
| `gov-admin` | *(impersonal)* | `bạn`, `mình`, `em`, `con`, `cả nhà` | Statutory administrative dispatches (công văn) per Nghị định 30/2020 |
| `formal` | `quý vị` | `bạn`, `mình`, `cả nhà` | Keynote addresses, shareholder meetings, formal enterprise events |

---

## 3. Statutory Compliance & Domain Rules (`rules_business.py`)

This skill integrates dedicated automated checks via `validate_copy.py` with custom `--doctype` rules:

| Rule ID | Severity | Scope / Doctype | Statutory or Channel Standard |
|---|---|---|---|
| `ZNS001` | ERROR | `zns-transactional` | Zalo strictly bans marketing/promotional words (`giảm giá`, `voucher`, `ưu đãi`, `deal`, `mua ngay`) in transactional templates |
| `ZNS002` | ERROR | `zns`, `zns-transactional` | Zalo enforces a strict 400-character NFC quota per template body |
| `MKT001` | ERROR | `marketplace-title` | Shopee, Lazada, TikTok Shop prohibit ALL-CAPS words (>= 4 letters, non-whitelisted) and spam emojis (`🔥`, `💥`, `⚡`, `❌`) |
| `MKT002` | ERROR | All marketing copy | Promotional discount > 50% is illegal under NĐ 81/2018 & NĐ 128/2024 unless annotated with `<!-- khuyen-mai-tap-trung: ... -->` |
| `MKT003` | ERROR | `influencer-post` | KOL/KOC sponsored posts must explicitly disclose sponsorship (`#QuảngCáo`, `#Ad`, `Tài trợ bởi`) per Luật 75/2025/QH15 |
| `SALES001`| ERROR | `cold-outreach`, `bao-gia`, `dunning`, `cong-van` | Casual pronouns (`bạn`, `mình`, `bọn mình`, `cậu`) are forbidden in B2B and administrative communications |
| `SALES003`| ERROR | `cold-outreach` | B2B cold outreach must open with a courteous salutation (`Kính gửi`, `Kính chào`, `Chào anh/chị`) |
| `SALES004`| ERROR | `bao-gia` | Commercial quotations must explicitly state VAT treatment (`thuế GTGT`/`VAT`) and validity period (`hiệu lực`) |
| `SPAM001` | ERROR | `bulk-message`, `promo` | Bulk marketing messages must include an explicit opt-out mechanism (`Soạn TC`, `Hủy nhận tin`) per NĐ 91/2020 Điều 13 |
| `ADMIN001`| ERROR | `cong-van` | Official administrative dispatches must include statutory Quốc hiệu (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`) and Tiêu ngữ (`Độc lập - Tự do - Hạnh phúc`) per Nghị định 30/2020 |

---

## 4. Workflows & Channel Guides

### A. B2B Sales Proposals & Quotations (`bao-gia`)
1. **Opening:** State recipient entity, representative, and background discussion.
2. **Table of Items:** Specification, unit, quantity, unit price (formatted with periods `1.500.000 VND`), total.
3. **Statutory Terms (`SALES004`):**
   - Must specify VAT: *"Đơn giá chưa bao gồm 10% thuế GTGT"* or *"Đơn giá đã bao gồm thuế GTGT"*.
   - Must specify validity: *"Báo giá có hiệu lực trong vòng 30 ngày kể từ ngày ban hành"*.
4. **Validation:**
   ```bash
   python3 skills/vietnamese-business-comms/scripts/validate_copy.py assets/bao-gia.md.template --doctype bao-gia --register b2b --strict
   ```

### B. Administrative Dispatches (`cong-van`)
1. **Header Layout (`ADMIN001`):**
   - Top-left: Issuing organization name, document number (`Số: .../CV-...`).
   - Top-right: Quốc hiệu (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`), Tiêu ngữ (`Độc lập - Tự do - Hạnh phúc`).
   - Date: `Hà Nội, ngày DD tháng MM năm YYYY`.
2. **Content:** Objective, factual, impersonal register (`--register gov-admin`).
3. **Closing & Signing:**
   - Signatory authority: `TM.` (Thay mặt), `KT.` (Ký thay), `TL.` (Thừa lệnh), `TUQ.` (Thừa ủy quyền).
   - Recipient block ending with `- Lưu: VT, [Đơn vị]`.
4. **Validation:**
   ```bash
   python3 skills/vietnamese-business-comms/scripts/validate_copy.py assets/cong-van.md.template --doctype cong-van --register gov-admin --strict
   ```

### C. E-Commerce Marketplace Listings (`marketplace-title`)
1. **Title Formula:** `[Thương hiệu] + [Tên sản phẩm] + [Đặc tính/Model] + [Quy cách/Dung tích/Màu sắc]`.
2. **Banned Patterns (`MKT001`):**
   - No ALL-CAPS words >= 4 letters (e.g. `GIẢM GIÁ`, `CHÍNH HÃNG`), except whitelisted technical standards (`HDMI`, `USB`, `OLED`, `WIFI`) and global brand marks.
   - Zero spam emojis (`🔥`, `💥`, `⚡`, `❌`, `⚠️`, `🚀`, `🎁`).
3. **Validation:**
   ```bash
   python3 skills/vietnamese-business-comms/scripts/validate_copy.py title.txt --doctype marketplace-title --strict
   ```

### D. Zalo ZNS Templates (`zns`, `zns-transactional`)
1. **Budget Check (`ZNS002`):** Body text must remain strictly within 400 NFC characters, including real-world parameter lengths.
2. **Promotional Ban (`ZNS001`):** Zero marketing words in transactional templates.
3. **Validation:**
   ```bash
   python3 skills/vietnamese-business-comms/scripts/validate_copy.py zns.txt --doctype zns-transactional --register zns --strict
   ```

---

## 5. Reference Library

- [`b2b-xung-ho.md`](references/b2b-xung-ho.md): Detailed seniority, kinship, C-level matrix, dunning escalation ladder (T-3 to T+30), and Tết corporate greetings protocol.
- [`channel-guide.md`](references/channel-guide.md): Technical constraints for ZNS/ZBS, UCS-2 SMS Brandname math, Shopee/Lazada title formula, livestream register, and press release structure.
- [`promo-law.md`](references/promo-law.md): Legal constraints of NĐ 81/2018, NĐ 128/2024 (50% discount ceiling), Luật 75/2025/QH15 (influencer disclosure), and NĐ 91/2020 (anti-spam).
- [`admin-decree-30.md`](references/admin-decree-30.md): Complete clerical standard for official dispatches (công văn) under Decree 30/2020/NĐ-CP.
- [`glossary.md`](references/glossary.md): 60+ canonical bilingual terms for B2B, sales, e-commerce, and administrative communications.
- [`banned-phrases.md`](references/banned-phrases.md): 35+ calques and 12+ advertising superlative regex patterns.
- [`qa-checklist.md`](references/qa-checklist.md): 9-point pre-flight checklist for all business communications.
