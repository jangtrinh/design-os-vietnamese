---
id: "cybersecurity-attt-and-pdpd"
title: "Vietnamese Cybersecurity & InfoSec Compliance: Luật 91/2025/QH15 & Nghị định 356/2025/NĐ-CP (PDPD), Decree 85/2016/NĐ-CP & Circular 12/2022/TT-BTTTT (ATTT Levels 1–5)"
domain: "vietnamese-cybersecurity-and-infosec"
description: "Verified specification for Vietnamese information security, cyber incident response, 72-hour personal data breach notifications under Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 Điều 23 and Nghị định 356/2025/NĐ-CP (Decree 13/2023/NĐ-CP no longer in force from 01/01/2026), and 5-tier information system classification under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT."
when:
  - "Drafting or auditing personal data breach notifications to the Ministry of Public Security PDP agency under Luật 91/2025/QH15 Điều 23 and Nghị định 356/2025/NĐ-CP Điều 28 (Mẫu số 08)"
  - "Authoring vulnerability advisories, CVE patches, SOC bulletins, and pentest reports in Vietnam"
  - "Enforcing SEC001–SEC006 rules in validate_copy.py for vietnamese-cybersecurity-infosec"
  - "Classifying information system security levels 1–5 under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT"
trust_tier: "verified"
version: "5.2.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md"
    sha256: "a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4"
  - uri: "_evidence/vn-design-os-261026/sources/07-vbpl-luat-91-2025-qh15-bao-ve-du-lieu-ca-nhan.txt"
    sha256: "11c381fa968c8e8456c2ddbcc37738682ceb60633788d68cfd87dbb104b90715"
  - uri: "_evidence/vn-design-os-261026/sources/08-vbpl-nd-356-2025-nd-cp-huong-dan-luat-bvdlcn.txt"
    sha256: "350ed8ae5ac5688457ced3ecd8d7c629744371cca386a393809ef76b9e118990"
  - uri: "_evidence/vn-design-os-261026/sources/09-vbpl-nd-13-2023-nd-cp-bao-ve-du-lieu-ca-nhan.txt"
    sha256: "c1b26a1eb5a94e3cdd3830aacf73e775d3bc0d8ddac4a9b0e4cde368126e35f9"
  - uri: "_evidence/vn-design-os-261026/sources/23-vbpl-nd-330-2026-nd-cp-xu-phat-an-ninh-mang-bvdlcn.txt"
    sha256: "0d77caf6604fdcb07512cf643832ff580575c3cd0b3b2eaa0c1bfdea92970b34"
---

# Vietnamese Cybersecurity & InfoSec Compliance: Luật 91/2025/QH15 & Nghị định 356/2025/NĐ-CP (PDPD), Decree 85/2016/NĐ-CP & Circular 12/2022/TT-BTTTT (ATTT Levels 1–5)

## Purpose

Defines statutory cybersecurity, incident reporting, personal data breach notification procedures, information system security level classifications (Cấp độ 1–5), and authoritative InfoSec terminology for enterprise SOCs, VNCERT/CC coordination, and NCSC advisories in Vietnam.

## When to Use / When NOT

- **When to Use:**
  - Authoring or auditing personal data protection breach notifications (`Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân`), security incident reports, vulnerability advisories (`Cảnh báo lỗ hổng bảo mật`), SOC alert runbooks, and penetration testing reports (`Báo cáo kiểm thử xâm nhập`).
- **When NOT to Use:**
  - Generic IT infrastructure guides or non-security technical documentation that do not handle security classifications, breach responses, or vulnerabilities.

## Core Knowledge Content

### 1. PDPD 72-Hour Notice of Violations to the Specialised PDP Agency, a Unit under Bộ Công an (`SEC001`, `SEC006`)

Current basis (from 01/01/2026): Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 Điều 23 khoản 1 requires notice to the specialised personal-data-protection agency within 72 hours of discovering a qualifying violation.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/07-vbpl-luat-91-2025-qh15-bao-ve-du-lieu-ca-nhan.txt" sha256="11c381fa968c8e8456c2ddbcc37738682ceb60633788d68cfd87dbb104b90715" quote="Luật này có hiệu lực thi hành từ ngày 01 tháng 01 năm 2026." -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/07-vbpl-luat-91-2025-qh15-bao-ve-du-lieu-ca-nhan.txt" sha256="11c381fa968c8e8456c2ddbcc37738682ceb60633788d68cfd87dbb104b90715" quote="thì phải thông báo cho cơ quan chuyên trách bảo vệ dữ liệu cá nhân chậm nhất là 72 giờ kể từ khi phát hiện hành vi vi phạm." -->

The notice content is set by Nghị định 356/2025/NĐ-CP Điều 28 and is filed on Mẫu số 08, directly or through the national PDP portal. In Decree 356, Mẫu 03a/03b is the impact-assessment update form (Điều 20 khoản 3), so `Form 03a` is the wrong form for a breach notice.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/08-vbpl-nd-356-2025-nd-cp-huong-dan-luat-bvdlcn.txt" sha256="350ed8ae5ac5688457ced3ecd8d7c629744371cca386a393809ef76b9e118990" quote="Việc cập nhật hồ sơ đánh giá tác động xử lý dữ liệu cá nhân và hồ sơ đánh giá tác động chuyển dữ liệu cá nhân xuyên biên giới được thực hiện theo Mẫu số 03a/03b tại Phụ lục của Nghị định này" -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/08-vbpl-nd-356-2025-nd-cp-huong-dan-luat-bvdlcn.txt" sha256="350ed8ae5ac5688457ced3ecd8d7c629744371cca386a393809ef76b9e118990" quote="gửi thông báo vi phạm quy định về dữ liệu cá nhân đến cơ quan chuyên trách bảo vệ dữ liệu cá nhân hoặc qua Cổng thông tin quốc gia về bảo vệ dữ liệu cá nhân theo Mẫu số 08 tại Phụ lục của Nghị định này." -->

Decree 356 Điều 39 defines the agency only as a unit under the Ministry of Public Security, without naming it.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/08-vbpl-nd-356-2025-nd-cp-huong-dan-luat-bvdlcn.txt" sha256="350ed8ae5ac5688457ced3ecd8d7c629744371cca386a393809ef76b9e118990" quote="Cơ quan chuyên trách bảo vệ dữ liệu cá nhân là đơn vị trực thuộc Bộ Công an" -->

The penalty decree, Nghị định 330/2026/NĐ-CP (in force from 19/08/2026), names Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an) as the unit that receives the impact-assessment dossier (Điều 55 khoản 1 điểm b). Reading the Cục as the specialised agency is this module's inference, not a quoted statement. A text search of the frozen Law 91, Decree 356 and Decree 330 finds no `A05`. In user copy, use the statutory term "cơ quan chuyên trách bảo vệ dữ liệu cá nhân" (a unit under Bộ Công an per NĐ 356 Điều 39 khoản 1), not the code.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/23-vbpl-nd-330-2026-nd-cp-xu-phat-an-ninh-mang-bvdlcn.txt" sha256="0d77caf6604fdcb07512cf643832ff580575c3cd0b3b2eaa0c1bfdea92970b34" quote="Nghị định này có hiệu lực thi hành kể từ ngày 19 tháng 8 năm 2026." -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/08-vbpl-nd-356-2025-nd-cp-huong-dan-luat-bvdlcn.txt" sha256="350ed8ae5ac5688457ced3ecd8d7c629744371cca386a393809ef76b9e118990" quote="Cơ quan chuyên trách bảo vệ dữ liệu cá nhân là đơn vị trực thuộc Bộ Công an" -->
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/23-vbpl-nd-330-2026-nd-cp-xu-phat-an-ninh-mang-bvdlcn.txt" sha256="0d77caf6604fdcb07512cf643832ff580575c3cd0b3b2eaa0c1bfdea92970b34" quote="cho Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an) trong thời gian 60 ngày" -->

The national legal database lists Decree 13/2023/NĐ-CP as no longer in force.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/09-vbpl-nd-13-2023-nd-cp-bao-ve-du-lieu-ca-nhan.txt" sha256="c1b26a1eb5a94e3cdd3830aacf73e775d3bc0d8ddac4a9b0e4cde368126e35f9" quote="legislationIdentifier=13/2023/NĐ-CP; legislationDate=2023-04-17; legislationLegalForce=NotInForce" -->

Historical (Decree 13/2023, no longer in force): Article 23 of Decree 13/2023/NĐ-CP on Personal Data Protection requires data controllers and processors to notify the Department of Cybersecurity and High-Tech Crime Prevention (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao — A05, Bộ Công an) within 72 hours of detecting a personal data protection violation using Form 03a, and Article 2 distinguishes Basic Personal Data ('dữ liệu cá nhân cơ bản') from Sensitive Personal Data ('dữ liệu cá nhân nhạy cảm').
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Article 23 of Decree 13/2023/NĐ-CP on Personal Data Protection requires data controllers and processors to notify the Department of Cybersecurity and High-Tech Crime Prevention (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao — A05, Bộ Công an) within 72 hours of detecting a personal data protection violation using Form 03a, and Article 2 distinguishes Basic Personal Data ('dữ liệu cá nhân cơ bản') from Sensitive Personal Data ('dữ liệu cá nhân nhạy cảm')." -->

### 2. Information System Security Levels 1–5 and InfoSec Terminology (`SEC002`, `SEC003`, `SEC004`, `SEC005`)

Under the Law on Cyberinformation Security 2015, Decree 85/2016/NĐ-CP, and Circular 12/2022/TT-BTTTT, information system security in Vietnam is classified strictly from Level 1 to Level 5 ('An toàn hệ thống thông tin theo cấp độ 1 đến cấp độ 5'), prohibiting fabricated Level 6 or Level 7 claims; furthermore, security advisories and vulnerability disclosures must use standard Vietnamese InfoSec terminology ('lỗ hổng bảo mật', 'mã độc tống tiền', 'xác thực đa yếu tố', 'tấn công giả mạo') and must never ask users to reply with passwords, PINs, OTPs, or CVV codes.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under the Law on Cyberinformation Security 2015, Decree 85/2016/NĐ-CP, and Circular 12/2022/TT-BTTTT, information system security in Vietnam is classified strictly from Level 1 to Level 5 ('An toàn hệ thống thông tin theo cấp độ 1 đến cấp độ 5'), prohibiting fabricated Level 6 or Level 7 claims; furthermore, security advisories and vulnerability disclosures must use standard Vietnamese InfoSec terminology ('lỗ hổng bảo mật', 'mã độc tống tiền', 'xác thực đa yếu tố', 'tấn công giả mạo') and must never ask users to reply with passwords, PINs, OTPs, or CVV codes." -->

## Failure Modes (Mandatory)

1. **Exceeding 72-Hour Statutory Breach Window or Omitting the PDP agency (`SEC001`):** Drafting breach procedures stating reports will be filed after 7 days or 30 days, or failing to address the notification to the Ministry of Public Security PDP agency (Luật 91/2025/QH15 Điều 23; Mẫu số 08 of Nghị định 356/2025/NĐ-CP).
2. **Fabricating System Security Levels Above Level 5 (`SEC002`):** Marketing enterprise software as compliant with "An toàn thông tin Cấp độ 6" or "Cấp độ 7", which do not exist in Vietnamese law.
3. **Machine-Translated Cybersecurity Slang (`SEC003`):** Using calques like "tấn công câu cá" (phishing) or "mã độc chuộc lỗi" / "phần mềm đòi tiền chuộc" (ransomware) instead of standard Vietnamese terminology.
4. **Credential Solicitation in Security Communications (`SEC004`):** Asking users or administrators to send passwords, OTPs, PINs, or CVVs via email or text messages under the guise of account verification.
5. **Vulnerability Advisory Missing Remediation (`SEC005`):** Disclosing a CVE vulnerability without specifying its severity rating (CVSS) and actionable remediation or patching guidance.
6. **Misclassifying Sensitive Personal Data (`SEC006`):** Treating financial data, biometric info, health records, or location history as "dữ liệu cá nhân cơ bản". The current lists are Nghị định 356/2025/NĐ-CP Điều 3 (basic) and Điều 4 (sensitive); Decree 13/2023/NĐ-CP no longer applies.
