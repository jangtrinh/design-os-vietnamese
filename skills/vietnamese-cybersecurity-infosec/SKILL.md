---
name: vietnamese-cybersecurity-infosec
description: Drafts, localizes, and audits native-quality Vietnamese (vi-VN) cybersecurity incident communications, personal data breach notifications under Law 91/2025/QH15 Article 23 and Decree 356/2025/NĐ-CP (PDPD 72-hour notification to the Ministry of Public Security, Mẫu số 08), 5-tier information system security assessments under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT, vulnerability disclosures (CVE/CVSS advisories), and penetration testing reports. Enforces standard Vietnamese InfoSec terminology, eliminates awkward translationese calques, and guards against credential solicitation and sensitive data misclassification.
version: "5.0.0"
author: "DESIGN:OS Vietnamese"
license: "PolyForm-Shield-1.0.0"
metadata:
  author: "DESIGN:OS Vietnamese"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Cybersecurity & InfoSec Compliance (`vietnamese-cybersecurity-infosec`)

In Vietnamese cybersecurity governance, communication failures carry **immediate statutory penalties and severe operational liabilities**. Reporting a personal data breach after the statutory 72-hour deadline breaches Article 23 of Law 91/2025/QH15; claiming a system is certified to non-existent "ATTT Cấp độ 6" violates Decree 85/2016/NĐ-CP; soliciting user passwords or OTPs in security advisories mimics phishing tactics; and omitting CVSS ratings or remediation patches in vulnerability notices cripples enterprise incident response.

This skill equips Security Operations Centers (SOC), Computer Security Incident Response Teams (CSIRT), penetration testers, and Chief Information Security Officers (CISO) with verified Vietnamese phrasing, statutory incident notification procedures, and automated linter validation.

---

## When to Use

- **Drafting Statutory Breach Notifications (`breach-notification`):** Authoring formal notifications to the cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) within the mandatory 72-hour window under Article 23 of Law 91/2025/QH15, on Mẫu số 08 of Decree 356/2025/NĐ-CP.
- **Authoring Vulnerability Advisories (`security-advisory`):** Writing CVE bulletins and NCSC/VNCERT coordination notices containing CVSS severity ratings, attack vectors, and vendor patch recommendations.
- **Publishing Penetration Testing Reports (`pentest-report`):** Structuring system assessment findings and security level proposals aligned strictly with Levels 1–5 under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT.
- **Auditing SOC Communications & Microcopy:** Eliminating machine-translated terminology (e.g. replacing `tấn công câu cá` with `tấn công giả mạo`) and preventing insecure credential requests.

---

## Quick Start

Validate any cybersecurity document against statutory requirements and InfoSec rules using the DESIGN:OS validator:

```bash
# Validate a 72-hour PDPD breach notification to A05
python3 shared/scripts/validate_copy.py incident-report.md --domain vietnamese-cybersecurity-infosec --doctype breach-notification --strict

# Validate a vulnerability advisory with CVSS and patch recommendations
python3 shared/scripts/validate_copy.py cve-advisory.md --domain vietnamese-cybersecurity-infosec --doctype security-advisory --strict

# Validate a penetration testing report according to ATTT Levels 1–5
python3 shared/scripts/validate_copy.py pentest.md --domain vietnamese-cybersecurity-infosec --doctype pentest-report --strict
```

---

## Core Rules

| Rule ID | Severity | Statutory / Technical Anchor | Defect Description & Remediation |
|---|---|---|---|
| `SEC001` | `ERROR` | Điều 23 Luật 91/2025/QH15 | Personal data breach notification stating a deadline exceeding 72 hours, or omitting notification to the cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) and the 72-hour timeframe. |
| `SEC002` | `ERROR` | Nghị định 85/2016 & Thông tư 12/2022 | Fabricated information system security level above Level 5 (`Cấp độ 6`, `Cấp độ 7`, `ATTT cấp 6`). Vietnamese law strictly recognizes only Levels 1 to 5. |
| `SEC003` | `WARN` | VNCERT/CC & NCSC Glossary | Awkward machine-translated InfoSec calques (`cuộc tấn công câu cá` → `tấn công giả mạo`, `mã độc chuộc lỗi` → `mã độc tống tiền`, `kỹ thuật xã hội` → `tấn công phi kỹ thuật`). |
| `SEC004` | `ERROR` | OWASP & Phishing Prevention Baseline | Insecure credential solicitation asking users to send passwords, OTPs, PINs, or CVVs via email, text, or unauthenticated forms. |
| `SEC005` | `ERROR` | NCSC & CVE Standard Protocol | Security advisory missing mandatory vulnerability severity rating (`Mức độ nghiêm trọng` / `CVSS`) or remediation guidance (`Biện pháp khắc phục` / `Bản vá`). |
| `SEC006` | `WARN` | Điều 2 khoản 3 Luật 91/2025/QH15; Điều 4 Nghị định 356/2025/NĐ-CP | Misclassifying health, financial/banking, biometric, or location data as basic personal data instead of sensitive personal data (`dữ liệu cá nhân nhạy cảm`). |

---

## Register Matrix

Cybersecurity communications operate primarily within objective technical and statutory registers:

| Document Type / Surface | Register | Reader Address | Speaker Identification | Tone & Pragmatics |
|---|---|---|---|---|
| PDPD Breach Notification | `gov-admin` / `formal` | `Cục A05 - Bộ Công an` | `Tổ chức / Doanh nghiệp` | Statutory formality, rigorous fact enumeration, no emotional embellishment |
| Security Advisory & CVE | `infosec-advisory` | `Quản trị viên / Người dùng` | `Bộ phận An ninh mạng / SOC` | Objective, concise, actionable urgency without panic |
| Penetration Testing Report | `eng-impersonal` | Third-person (`Hệ thống`) | `Đơn vị đánh giá / Pentester` | Empirical evidence, CVSS metrics, reproducible proof-of-concept |
| Security Incident Alert | `ux-microcopy` | `Bạn` | `Hệ thống bảo mật` | Direct, step-by-step guidance, zero password requests |

---

## Workflow

To draft and audit high-assurance Vietnamese cybersecurity instruments, follow this 5-stage pipeline:

1. **Stage 1: Statutory Scope & Threat Classification:**
   - Determine whether the event involves personal data leakage (triggering PDPD Decree 13) or infrastructure intrusion (triggering Decree 85/2016/NĐ-CP).
   - Classify all affected data assets: identify sensitive personal data (banking, biometric, health, location) requiring elevated protection.
2. **Stage 2: 72-Hour Breach Notification Protocol (A05):**
   - If personal data is compromised, draft the breach notice on Mẫu số 08 (Nghị định 356/2025/NĐ-CP Điều 28) addressed to the cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an), directly or via the national PDP portal.
   - Enforce the non-negotiable **72-hour statutory deadline** from the moment of detection.
3. **Stage 3: Terminology & System Level Verification:**
   - Audit system classification against Decree 85/2016 Levels 1–5 (`Cấp độ 1 đến Cấp độ 5`). Reject any claims of Levels 6+.
   - Replace English translationese with authoritative Vietnamese InfoSec terminology (`mã độc tống tiền`, `tấn công giả mạo`, `tường lửa thế hệ mới`).
4. **Stage 4: Advisory Completeness & Credential Safety Check:**
   - Verify that every vulnerability advisory provides a clear severity rating (CVSS) and verified vendor remediation steps.
   - Strip any phrasing that prompts users to transmit secrets, OTPs, PINs, or credentials.
5. **Stage 5: Automated Linter & Pre-Publication Gate:**
   - Execute `validate_copy.py --domain vietnamese-cybersecurity-infosec --strict`.
   - Ensure 0 errors and 0 warnings before internal executive review or external dispatch.

---

## Bundled References

- [references/glossary.md](references/glossary.md) — Machine-readable glossary of 30+ cybersecurity, SOC, and threat intelligence terms with severity linting rules.
- [references/banned-phrases.md](references/banned-phrases.md) — Prohibited InfoSec calques, credential solicitation phrases, and fabricated security levels.
- [references/qa-checklist.md](references/qa-checklist.md) — Comprehensive 4-tier pre-publish incident notification and advisory quality gate.
- [references/ung-cuu-su-co-pdpd-72h-a05.md](references/ung-cuu-su-co-pdpd-72h-a05.md) — 72-hour A05 personal data breach notification procedure and Form 03a structure.
- [references/attt-cap-do-1-5-nd85-tt12.md](references/attt-cap-do-1-5-nd85-tt12.md) — Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT 5-tier system security levels.
- [references/infosec-terminology-and-calques.md](references/infosec-terminology-and-calques.md) — Authoritative cybersecurity terms, translationese blocklist, and SOC conventions.
