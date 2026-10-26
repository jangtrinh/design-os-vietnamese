---
id: "media-journalism-and-crisis-pr"
title: "Vietnamese Media, Press Law 2016, Decree 147/2024/NĐ-CP, Presumption of Innocence, and Crisis PR"
domain: "vietnamese-media-journalism-and-pr"
description: "Verified specification for Vietnamese press communications, Press Law 2016, general news website regulation (Decree 147/2024/NĐ-CP), press corrections and apologies, child identity protection under the Law on Children 2016, and professional crisis PR response."
when:
  - "Publishing press releases, news articles, or crisis communications statements in Vietnam"
  - "Drafting formal press corrections and apologies under Article 42 Press Law 2016"
  - "Enforcing MEDJ001–MEDJ006 rules in validate_copy.py for vietnamese-media-journalism-pr"
  - "Ensuring presumption of innocence and child anonymization in legal and investigative reporting"
trust_tier: "verified"
version: "5.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md"
    sha256: "a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4"
---

# Vietnamese Media, Press Law 2016, Decree 147/2024/NĐ-CP, Presumption of Innocence, and Crisis PR

## Purpose

Defines legal and professional communication standards for press agencies, corporate PR departments, news portals, and social media channels under the Press Law 2016, Decree 147/2024/NĐ-CP, the Constitution 2013, and the Law on Children 2016 in Vietnam.

## When to Use / When NOT

- **When to Use:**
  - Authoring or auditing official press releases (`Thông cáo báo chí`), press corrections and apologies (`Cải chính và xin lỗi`), investigative reporting, crisis management statements (`Thông cáo xử lý khủng hoảng`), and news aggregation portals.
- **When NOT to Use:**
  - Internal corporate memos, purely technical release notes, or informal creative writing not distributed to the public or press.

## Core Knowledge Content

### 1. Press Licensing vs ICP Websites and Mandatory Correction/Apology Rules (`MEDJ001`, `MEDJ002`)

Under the Press Law 2016 (Luật Báo chí số 103/2016/QH13) and Decree 147/2024/NĐ-CP on management, provision, and use of Internet services and online information, general news websites ('Trang thông tin điện tử tổng hợp' — ICP) and social networks ('Mạng xã hội') must not misrepresent themselves as licensed press agencies ('Cơ quan báo chí') and must cite verbatim sources with explicit written consent, while Article 42 of the Press Law mandates that press corrections and apologies ('Cải chính trên báo chí') be published in the exact same position, section, and font size as the erroneous article.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under the Press Law 2016 (Luật Báo chí số 103/2016/QH13) and Decree 147/2024/NĐ-CP on management, provision, and use of Internet services and online information, general news websites ('Trang thông tin điện tử tổng hợp' — ICP) and social networks ('Mạng xã hội') must not misrepresent themselves as licensed press agencies ('Cơ quan báo chí') and must cite verbatim sources with explicit written consent, while Article 42 of the Press Law mandates that press corrections and apologies ('Cải chính trên báo chí') be published in the exact same position, section, and font size as the erroneous article." -->

### 2. Presumption of Innocence and Child Identity Protection (`MEDJ003`, `MEDJ004`, `MEDJ005`, `MEDJ006`)

Under Article 31 of the Constitution 2013, Article 13 of the Criminal Procedure Code 2015, and Article 9 of the Press Law 2016, press copy must respect the presumption of innocence by distinguishing 'nghi phạm' (suspect), 'bị can' (indicted person), and 'bị cáo' (defendant brought to trial) and must never label a person a 'tội phạm', 'hung thủ', or 'kẻ giết người' prior to a legally effective court judgment; simultaneously, Article 21 of the Law on Children 2016 and Decree 56/2017/NĐ-CP mandate strict anonymization of children under 16 in press coverage.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under Article 31 of the Constitution 2013, Article 13 of the Criminal Procedure Code 2015, and Article 9 of the Press Law 2016, press copy must respect the presumption of innocence by distinguishing 'nghi phạm' (suspect), 'bị can' (indicted person), and 'bị cáo' (defendant brought to trial) and must never label a person a 'tội phạm', 'hung thủ', or 'kẻ giết người' prior to a legally effective court judgment; simultaneously, Article 21 of the Law on Children 2016 and Decree 56/2017/NĐ-CP mandate strict anonymization of children under 16 in press coverage." -->

## Failure Modes (Mandatory)

1. **Press Agencification of ICP Portals (`MEDJ001`):** Operating a general news website (ICP) under titles like "Báo điện tử", "Tòa soạn", or producing original investigative journalism without a press license.
2. **Silent Deletion without Statutory Correction (`MEDJ002`):** Removing erroneous articles silently instead of publishing a formal correction and apology under Article 42 Press Law 2016.
3. **Violating Presumption of Innocence (`MEDJ003`):** Naming an arrested suspect or indicted person a "tên tội phạm", "hung thủ", or "kẻ giết người" before a court verdict takes legal effect.
4. **Publishing Child Identity or Unblurred Photos (`MEDJ004`):** Revealing the full name, school, home address, or clear face photo of a child under 16 involved in legal cases or accidents.
5. **English PR Calques or Missing Dateline (`MEDJ005`):** Using literal translations such as "Để phát hành ngay lập tức" or omitting city/date dateline and media contact details in press releases.
6. **Hostile or Retaliatory Crisis Statements (`MEDJ006`):** Threatening to sue complaining consumers or blaming users for corporate service interruptions.
