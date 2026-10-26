---
id: "hr-labor-code-and-bhxh"
title: "Vietnamese HR & Recruitment Compliance: Labor Code 2019 (Articles 8, 17, 25, 26) and Social Insurance Law 2024"
domain: "vietnamese-hr-and-recruitment"
description: "Verified specification for Vietnamese job descriptions (JD), offer letters, probation terms (>=85% salary floor, 6/30/60/180-day caps), anti-discrimination rules, and performance reviews under the Labor Code 2019."
when:
  - "Writing or auditing job descriptions (JD), offer letters (Thư mời nhận việc), internal HR policies, or OKR/KPI performance reviews"
  - "Enforcing HR001–HR006 rules in validate_copy.py for vietnamese-hr-recruitment"
  - "Verifying probation duration and probation wage floors under Articles 25 & 26 of the Labor Code 2019"
trust_tier: "verified"
version: "4.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md"
    sha256: "a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed"
---

# Vietnamese HR & Recruitment Compliance: Labor Code 2019 (Articles 8, 17, 25, 26) and Social Insurance Law 2024

## Purpose

Defines the statutory labor law rules and professional HR communication standards for recruitment announcements (`JD`), offer letters (`Thư mời nhận việc`), onboarding policies, and OKR/KPI performance reviews in Vietnam.

## When to Use / When NOT

- **When to Use:**
  - Drafting or auditing job descriptions, candidate offer letters, probation clauses, internal employee handbooks (`Nội quy lao động`), and performance review templates in Vietnam.
- **When NOT to Use:**
  - Independent B2B contractor agreements governed purely by the Commercial Law 2005.

## Core Knowledge Content

### 1. Anti-Discrimination and Prohibition on Document/Deposit Retention (`HR001`, `HR004`)

Article 8 Clause 1 of the Labor Code 2019 strictly prohibits employment discrimination based on gender, marital status, pregnancy, age, ethnicity, religion, or disability in recruitment announcements (JD), while Article 17 forbids employers from retaining original identity cards, diplomas, or certificates or requiring monetary/asset deposits from employees as a condition of employment.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Article 8 Clause 1 of the Labor Code 2019 strictly prohibits employment discrimination based on gender, marital status, pregnancy, age, ethnicity, religion, or disability in recruitment announcements (JD), while Article 17 forbids employers from retaining original identity cards, diplomas, or certificates or requiring monetary/asset deposits from employees as a condition of employment." -->

### 2. Statutory Probation Duration Caps and 85% Wage Floor (`HR002`, `HR003`)

Under Articles 25 and 26 of the Labor Code 2019, probation periods may not exceed 180 days for enterprise managers (Luật Doanh nghiệp), 60 days for positions requiring college (`Cao đẳng`) or higher degrees, 30 days for intermediate/technical roles, and 6 working days for other jobs, and probation salary must be at least 85% of the official wage for that job.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Under Articles 25 and 26 of the Labor Code 2019, probation periods may not exceed 180 days for enterprise managers (Luật Doanh nghiệp), 60 days for positions requiring college (Cao đẳng) or higher degrees, 30 days for intermediate/technical roles, and 6 working days for other jobs, and probation salary must be at least 85% of the official wage for that job." -->

## Failure Modes (Mandatory)

1. **Discriminatory Job Descriptions (`HR001`):** Posting `Chỉ tuyển nữ từ 20–25 tuổi, ngoại hình ưa nhìn, cam kết không kết hôn/mang thai trong 2 năm đầu` in violation of Article 8 of the Labor Code 2019.
2. **Sub-85% Probation Pay or 90-Day Probation for Non-Managers (`HR002`):** Issuing an Offer Letter for a software engineer or accountant stating `Thời gian thử việc: 03 tháng (90 ngày), hưởng 75% lương chính thức` in violation of Articles 25 & 26 of the Labor Code 2019.
3. **Retaining Original Diplomas or Requiring Cash Deposits (`HR004`):** Requiring new hires to submit their original university diploma (`giữ bằng đại học gốc`) or pay a security deposit (`đặt cọc 5.000.000 ₫`) in violation of Article 17 of the Labor Code 2019.
