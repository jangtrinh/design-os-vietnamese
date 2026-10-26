---
id: "b2b-zns-and-admin-comms"
title: "Vietnamese Administrative Documents (Nghị định 30/2020/NĐ-CP) and Zalo ZNS / B2B Communications"
domain: "vietnamese-business-and-administrative-comms"
description: "Verified specification for Vietnamese clerical documents under Decree 30/2020/NĐ-CP (Công văn, Tờ trình, Quyết định, Biên bản) and Zalo Notification Service (ZNS) compliance under Decree 91/2020/NĐ-CP."
when:
  - "Drafting or validating Vietnamese administrative documents (Công văn, Tờ trình, Quyết định, Thông báo, Biên bản)"
  - "Designing Zalo Notification Service (ZNS) templates and B2B enterprise emails"
  - "Running validate_copy.py with --domain biz and --doctype cong-van|to-trinh|quyet-dinh|bien-ban|zns"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md"
    sha256: "c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290"
---

# Vietnamese Administrative Documents (Nghị định 30/2020/NĐ-CP) and Zalo ZNS / B2B Communications

## Purpose

Establishes the structural and regulatory rules for Vietnamese clerical documents under Decree 30/2020/NĐ-CP (`Công tác văn thư`) and Zalo Notification Service (ZNS) / B2B messaging under Decree 91/2020/NĐ-CP.

## When to Use / When NOT

- **When to Use:**
  - Authoring or reviewing official enterprise correspondence (`Công văn`, `Tờ trình`, `Quyết định`, `Thông báo`, `Biên bản`), B2B proposals, and Zalo ZNS templates.
- **When NOT to Use:**
  - Casual consumer social media posts or in-app gaming chat.

## Core Knowledge Content

### 1. Clerical and Archival Standards: Decree 30/2020/NĐ-CP (`BIZ001`–`BIZ003`)

Decree 30/2020/NĐ-CP on Clerical and Archival Work (`Công tác văn thư`) standardizes the national emblem header (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM / Độc lập - Tự do - Hạnh phúc`), reference number format (`Số: .../CV-...`), recipient block (`Kính gửi:`), and closing authority abbreviations (`TM.`, `KT.`, `TL.`, `TUQ.`) across `Công văn`, `Tờ trình`, `Quyết định`, `Thông báo`, and `Biên bản`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Decree 30/2020/NĐ-CP on Clerical and Archival Work (Công tác văn thư) standardizes the national emblem header ('CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM / Độc lập - Tự do - Hạnh phúc'), reference number format ('Số: .../CV-...'), recipient block ('Kính gửi:'), and closing authority abbreviations ('TM.', 'KT.', 'TL.', 'TUQ.') across Công văn, Tờ trình, Quyết định, Thông báo, and Biên bản." -->

### 2. Zalo Notification Service (ZNS) and Anti-Spam Compliance (`BIZ004`–`BIZ005`)

Decree 91/2020/NĐ-CP on anti-spam telecommunications requires prior opt-in, advertiser prefix tagging (`[QC]`), and explicit free opt-out syntax (`Soạn TC gửi...`) for promotional SMS/ZNS/emails, and strictly forbids disguising promotional incentives inside transactional Zalo Notification Service (ZNS) templates.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Decree 91/2020/NĐ-CP on anti-spam telecommunications requires prior opt-in, advertiser prefix tagging ('[QC]'), and explicit free opt-out syntax ('Soạn TC gửi...') for promotional SMS/ZNS/emails, and strictly forbids disguising promotional incentives inside transactional Zalo Notification Service (ZNS) templates." -->

## Failure Modes (Mandatory)

1. **Missing National Motto or Reference Number in Administrative Docs (`BIZ001`, `BIZ002`):** Issuing a formal `Công văn` or `Quyết định` without `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM / Độc lập - Tự do - Hạnh phúc` and `Số: .../...` violates Appendix I of Decree 30/2020/NĐ-CP.
2. **Promotional Copy Smuggled into Transactional ZNS (`BIZ005`):** Injecting `Giảm ngay 50% cho đơn tiếp theo!` into a Tag 1/Tag 2 order-confirmation ZNS template causes Zalo OA template rejection and penalties under Decree 91/2020/NĐ-CP.
3. **English Salutation Calques in B2B Emails (`BIZ003`):** Opening formal Vietnamese enterprise correspondence with `Gửi Anh Minh,` (literal calque of "Dear Minh,") instead of `Kính gửi anh Minh,` or `Thân gửi anh Minh,`.
