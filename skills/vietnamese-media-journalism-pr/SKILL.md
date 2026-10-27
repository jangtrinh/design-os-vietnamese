---
name: vietnamese-media-journalism-pr
description: Drafts, localizes, and audits native-quality Vietnamese (vi-VN) journalism copy, official press releases, press corrections and apologies under Article 42 of the Press Law 2016, and constructive crisis PR communications. Enforces constitutional presumption of innocence (Hiến pháp 2013 & BLTTHS 2015), strict child identity protection under the Law on Children 2016, Internet general news website (ICP) regulatory boundaries under Decree 147/2024/NĐ-CP, and eliminates clumsy English PR translationese.
version: "5.0.0"
author: "DESIGN:OS Vietnamese"
license: "PolyForm-Shield-1.0.0"
metadata:
  author: "DESIGN:OS Vietnamese"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Media, Journalism & Crisis PR (`vietnamese-media-journalism-pr`)

In Vietnamese media and public relations, language carries **direct legal enforceability, constitutional protections, and acute reputational risk**. Calling an unconvicted suspect a criminal breaches the constitutional presumption of innocence; operating an ICP website as a self-styled "Tòa soạn" without a press license violates Decree 147/2024/NĐ-CP; silently removing an inaccurate report without formal correction and apology breaches Article 42 of the Press Law 2016; and issuing retaliatory, victim-blaming crisis statements sparks severe regulatory and public backlashes.

This skill equips journalists, corporate PR practitioners, communications directors, and media editors with authoritative Vietnamese terminology, statutory press correction frameworks, and automated compliance validation.

---

## When to Use

- **Drafting Official Press Releases (`press-release`):** Writing new product announcements, strategic partnerships, and corporate milestones with formal datelines and dedicated media contact information.
- **Publishing Press Corrections & Apologies (`correction-apology`):** Structuring statutory corrections under Article 42 of the Press Law 2016 citing original article details and explicit apologies.
- **Formulating Crisis Communications (`crisis-statement`):** Developing empathetic, fact-grounded responses to operational incidents without defensive victim-blaming or retaliatory litigation threats.
- **Auditing Investigative & News Copy:** Ensuring constitutional presumption of innocence (`nghi phạm` / `bị can` vs. `tội phạm`), child anonymization under 16, and eliminating PR translationese calques.

---

## Quick Start

Validate any media or PR instrument against Vietnamese press laws and linguistic rules:

```bash
# Validate an official press release
python3 shared/scripts/validate_copy.py press-release.md --domain vietnamese-media-journalism-pr --doctype press-release --strict

# Validate a statutory press correction and apology under Article 42 Press Law
python3 shared/scripts/validate_copy.py correction.md --domain vietnamese-media-journalism-pr --doctype correction-apology --strict

# Validate a corporate crisis management statement
python3 shared/scripts/validate_copy.py crisis-statement.md --domain vietnamese-media-journalism-pr --doctype crisis-statement --strict
```

---

## Core Rules

| Rule ID | Severity | Statutory / Professional Baseline | Defect Description & Remediation |
|---|---|---|---|
| `MEDJ001` | `ERROR` | Luật Báo chí 2016 & Nghị định 147/2024 | General news website (ICP) or social page falsely claiming press agency status, using "Tòa soạn", or producing unauthorized investigative journalism. |
| `MEDJ002` | `ERROR` | Điều 42 Luật Báo chí 2016 | Press correction notice omitting explicit correction, apology, and original article details, or claiming silent deletion is permissible. |
| `MEDJ003` | `ERROR` | Hiến pháp 2013 Đ31 & BLTTHS 2015 Đ13 | Violating the presumption of innocence by labeling an unconvicted person a criminal (`tên tội phạm`, `hung thủ`) before an effective court judgment. |
| `MEDJ004` | `ERROR` | Điều 21 Luật Trẻ em 2016 & NĐ 56/2017 | Revealing the identity, full name, school address, or unblurred face of a child under 16 in media coverage without lawful consent. |
| `MEDJ005` | `WARN` | Vietnamese PR & Journalism Conventions | Clumsy English PR calques (`Để phát hành ngay lập tức`, `Trên hồ sơ`, `Câu chuyện dẫn đầu`), or press release missing location dateline or media contacts. |
| `MEDJ006` | `ERROR` | Ethical Crisis Communications Standard | Hostile, retaliatory, or victim-blaming crisis PR statements threatening lawsuits against consumers without verification or disclaiming company duty of explanation. |

---

## Register Matrix

Journalistic and media documents adhere to specific communicative registers:

| Document Type / Surface | Register | Reader Address | Speaker Identification | Tone & Pragmatics |
|---|---|---|---|---|
| Official Press Release | `press` / `formal` | `Quý cơ quan báo chí / Quý vị` | `[Tên doanh nghiệp / tổ chức]` | Professional, fact-driven, objective, third-person perspective |
| Press Correction & Apology | `formal` | `Quý bạn đọc / [Cá nhân/tổ chức]` | `Ban Biên tập / Tòa soạn` | Sincere, respectful, unambiguous acknowledgment of error |
| Crisis PR Statement | `crisis-comms` | `Quý khách hàng / Quý vị` | `Ban Lãnh đạo Công ty` | Empathetic, transparent, constructive, accountable |
| Investigative News Article | `eng-impersonal` | Third-person | `Phóng viên / Tác giả` | Objective evidence, rigorous procedural naming (`bị can`, `bị cáo`) |

---

## Workflow

To draft and publish compliant Vietnamese press and PR instruments, follow this 5-stage pipeline:

1. **Stage 1: Channel & Licensing Verification:**
   - Verify whether the publishing channel is a licensed press agency or an ICP aggregator.
   - For ICP portals, ensure all content is republished verbatim with written press permissions; prohibit original investigative reporting.
2. **Stage 2: Legal Safeguards & Presumption of Innocence:**
   - Audit all references to persons in criminal proceedings. Enforce `nghi phạm` (investigation), `bị can` (indictment), and `bị cáo` (court trial).
   - Verify strict anonymization and facial blurring for any minor under 16 years of age under Article 21 Law on Children 2016.
3. **Stage 3: Press Correction & Apology Compliance (Article 42):**
   - For errata, ensure explicit inclusion of both `Cải chính` and `Xin lỗi`, referencing the original headline, publication date, and corrected facts.
   - Prohibit any silent deletion of inaccurate reports.
4. **Stage 4: PR Architecture & Tone Sanitization:**
   - In press releases, enforce standard datelines (`Hà Nội, ngày ...`) and verified media relations contacts.
   - In crisis statements, remove defensive threats, victim-blaming rhetoric, and unverified allegations against consumers.
5. **Stage 5: Automated Linter & Pre-Flight Review:**
   - Run `validate_copy.py --domain vietnamese-media-journalism-pr --strict`.
   - Ensure 0 errors and 0 warnings before wire transmission or press conference distribution.

---

## Bundled References

- [references/glossary.md](references/glossary.md) — Machine-readable glossary of 30+ journalism, press release architecture, and PR terms with severity linting rules.
- [references/banned-phrases.md](references/banned-phrases.md) — Prohibited journalism calques, presumption-of-innocence violations, and retaliatory crisis statements.
- [references/qa-checklist.md](references/qa-checklist.md) — Comprehensive 4-tier pre-publish editorial, constitutional, and PR quality gate.
- [references/luat-bao-chi-2016-va-nd147-2024.md](references/luat-bao-chi-2016-va-nd147-2024.md) — Press Law 2016, Decree 147/2024/NĐ-CP, and Article 42 press correction procedures.
- [references/suy-doan-vo-toi-va-bao-ve-tre-em.md](references/suy-doan-vo-toi-va-bao-ve-tre-em.md) — Constitutional presumption of innocence and child identity protection standards.
- [references/press-release-and-crisis-pr.md](references/press-release-and-crisis-pr.md) — Press release architecture, journalism calques, and constructive crisis PR guidelines.
