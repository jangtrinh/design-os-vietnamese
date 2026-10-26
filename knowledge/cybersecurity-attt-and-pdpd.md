---
id: "cybersecurity-attt-and-pdpd"
title: "Vietnamese Cybersecurity & InfoSec Compliance: Decree 13/2023/NĐ-CP (PDPD), Decree 85/2016/NĐ-CP & Circular 12/2022/TT-BTTTT (ATTT Levels 1–5)"
domain: "vietnamese-cybersecurity-and-infosec"
description: "Verified specification for Vietnamese information security, cyber incident response, 72-hour A05 personal data breach notifications under Decree 13/2023/NĐ-CP, and 5-tier information system classification under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT."
when:
  - "Drafting or auditing personal data breach notifications to A05 Ministry of Public Security under Article 23 Decree 13/2023/NĐ-CP"
  - "Authoring vulnerability advisories, CVE patches, SOC bulletins, and pentest reports in Vietnam"
  - "Enforcing SEC001–SEC006 rules in validate_copy.py for vietnamese-cybersecurity-infosec"
  - "Classifying information system security levels 1–5 under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT"
trust_tier: "verified"
version: "5.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md"
    sha256: "a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4"
---

# Vietnamese Cybersecurity & InfoSec Compliance: Decree 13/2023/NĐ-CP (PDPD), Decree 85/2016/NĐ-CP & Circular 12/2022/TT-BTTTT (ATTT Levels 1–5)

## Purpose

Defines statutory cybersecurity, incident reporting, personal data breach notification procedures, information system security level classifications (Cấp độ 1–5), and authoritative InfoSec terminology for enterprise SOCs, VNCERT/CC coordination, and NCSC advisories in Vietnam.

## When to Use / When NOT

- **When to Use:**
  - Authoring or auditing personal data protection breach notifications (`Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân`), security incident reports, vulnerability advisories (`Cảnh báo lỗ hổng bảo mật`), SOC alert runbooks, and penetration testing reports (`Báo cáo kiểm thử xâm nhập`).
- **When NOT to Use:**
  - Generic IT infrastructure guides or non-security technical documentation that do not handle security classifications, breach responses, or vulnerabilities.

## Core Knowledge Content

### 1. PDPD 72-Hour Statutory Breach Notification to A05 Ministry of Public Security (`SEC001`, `SEC006`)

Article 23 of Decree 13/2023/NĐ-CP on Personal Data Protection requires data controllers and processors to notify the Department of Cybersecurity and High-Tech Crime Prevention (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao — A05, Bộ Công an) within 72 hours of detecting a personal data protection violation using Form 03a, and Article 2 distinguishes Basic Personal Data ('dữ liệu cá nhân cơ bản') from Sensitive Personal Data ('dữ liệu cá nhân nhạy cảm').
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Article 23 of Decree 13/2023/NĐ-CP on Personal Data Protection requires data controllers and processors to notify the Department of Cybersecurity and High-Tech Crime Prevention (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao — A05, Bộ Công an) within 72 hours of detecting a personal data protection violation using Form 03a, and Article 2 distinguishes Basic Personal Data ('dữ liệu cá nhân cơ bản') from Sensitive Personal Data ('dữ liệu cá nhân nhạy cảm')." -->

### 2. Information System Security Levels 1–5 and InfoSec Terminology (`SEC002`, `SEC003`, `SEC004`, `SEC005`)

Under the Law on Cyberinformation Security 2015, Decree 85/2016/NĐ-CP, and Circular 12/2022/TT-BTTTT, information system security in Vietnam is classified strictly from Level 1 to Level 5 ('An toàn hệ thống thông tin theo cấp độ 1 đến cấp độ 5'), prohibiting fabricated Level 6 or Level 7 claims; furthermore, security advisories and vulnerability disclosures must use standard Vietnamese InfoSec terminology ('lỗ hổng bảo mật', 'mã độc tống tiền', 'xác thực đa yếu tố', 'tấn công giả mạo') and must never ask users to reply with passwords, PINs, OTPs, or CVV codes.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under the Law on Cyberinformation Security 2015, Decree 85/2016/NĐ-CP, and Circular 12/2022/TT-BTTTT, information system security in Vietnam is classified strictly from Level 1 to Level 5 ('An toàn hệ thống thông tin theo cấp độ 1 đến cấp độ 5'), prohibiting fabricated Level 6 or Level 7 claims; furthermore, security advisories and vulnerability disclosures must use standard Vietnamese InfoSec terminology ('lỗ hổng bảo mật', 'mã độc tống tiền', 'xác thực đa yếu tố', 'tấn công giả mạo') and must never ask users to reply with passwords, PINs, OTPs, or CVV codes." -->

## Failure Modes (Mandatory)

1. **Exceeding 72-Hour Statutory Breach Window or Omitting A05 (`SEC001`):** Drafting breach procedures stating reports will be filed after 7 days or 30 days, or failing to address the notification to Cục A05 - Bộ Công an.
2. **Fabricating System Security Levels Above Level 5 (`SEC002`):** Marketing enterprise software as compliant with "An toàn thông tin Cấp độ 6" or "Cấp độ 7", which do not exist in Vietnamese law.
3. **Machine-Translated Cybersecurity Slang (`SEC003`):** Using calques like "tấn công câu cá" (phishing) or "mã độc chuộc lỗi" / "phần mềm đòi tiền chuộc" (ransomware) instead of standard Vietnamese terminology.
4. **Credential Solicitation in Security Communications (`SEC004`):** Asking users or administrators to send passwords, OTPs, PINs, or CVVs via email or text messages under the guise of account verification.
5. **Vulnerability Advisory Missing Remediation (`SEC005`):** Disclosing a CVE vulnerability without specifying its severity rating (CVSS) and actionable remediation or patching guidance.
6. **Misclassifying Sensitive Personal Data (`SEC006`):** Treating financial data, biometric info, health records, or location history as "dữ liệu cá nhân cơ bản" under Decree 13/2023/NĐ-CP.
