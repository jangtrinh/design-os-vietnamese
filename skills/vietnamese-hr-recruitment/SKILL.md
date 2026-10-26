---
name: vietnamese-hr-recruitment
description: Writes, localizes, and audits native-quality Vietnamese (vi-VN) human resources, talent acquisition, recruitment marketing, and employment compliance communications. Enforces statutory labor protections under Bộ luật Lao động 2019 (prohibiting recruitment discrimination under Điều 8 khoản 1, withholding original diplomas or identity documents under Điều 17, and illegal punitive wage deductions under Điều 128), statutory probation ceilings and 85% salary floor under Điều 25 & 26, transparent Gross vs Net compensation disclosures in Offer Letters, modern outcome-oriented Job Descriptions (JD) eliminating toxic workplace clichés, objective Situation-Behavior-Impact (SBI) performance appraisals (OKR / KPI / 360 Feedback), and candidate-centric etiquette using the hr-candidate register (Anh/Chị).
license: PolyForm-Shield-1.0.0
metadata:
  author: "Jang Trinh"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese HR, Recruitment, & Labor Compliance Copywriting (`vietnamese-hr-recruitment`)

In Vietnamese human resources, recruitment marketing, and talent operations, copywriting is not merely an administrative task—it is a **binding legal representation and cultural contract**. An ill-conceived Job Description (JD) specifying gender or age restrictions exposes the enterprise to administrative penalties for discrimination under the Labor Code 2019; an Offer Letter that ambiguously states a salary figure without defining Gross versus Net breeds toxic labor disputes; and subjective, aggressive language in performance appraisals (*"thái độ kém cỏi"*, *"lười biếng"*) destroys psychological safety and employee retention.

This skill equips People Operations leaders, technical recruiters, hiring managers, and copywriters with authoritative, verified Vietnamese terminology, empathetic candidate etiquette, and statutory compliance frameworks grounded in current Vietnamese labor legislation.

---

## 1. Register & Sociolinguistic Etiquette (`hr-candidate`)

Human resources communication in Vietnam operates under the respectful, egalitarian conventions established in [references/register-matrix.md](references/register-matrix.md):

| Context / Surface | Register | Candidate Address (`Hô`) | Employer Reference (`Xưng`) | Tone Principles |
|---|---|---|---|---|
| Job descriptions (JD) & career pages | `hr-candidate` | `Ứng viên` / `Anh/Chị` | `Công ty` / `Chúng tôi` | Inclusive, inspiring, outcome-oriented |
| Offer letters & interview invitations | `hr-candidate` | `Anh/Chị` | `Công ty` / `Chúng tôi` | Warm, welcoming, legally meticulous |
| Performance appraisals (OKR / KPI / 360) | `hr-candidate` | `Anh/Chị` | `Quản lý trực tiếp` / `Tôi` | Objective, developmental, SBI-grounded |
| Internal labor policies & handbooks | `gov-admin` / `formal` | `Người lao động` | `Người sử dụng lao động` | Clear, equitable, strictly compliant |

> [!IMPORTANT]
> **Candidate Respect Floor:** In Vietnamese talent acquisition, addressing a professional candidate as `mày`, `cậu`, `con`, or `cả nhà` is strictly prohibited (`PRO002`). Always address the candidate as `Anh/Chị` to establish mutual respect.

---

## 2. Statutory Labor Code Compliance (Bộ luật Lao động 2019)

As detailed in [references/labor-code-and-offer-letters.md](references/labor-code-and-offer-letters.md), all employment copy must strictly align with statutory labor safeguards:

1. **Anti-Discrimination in Hiring (`HR001`):**
   - Under Article 8 Clause 1 of Bộ luật Lao động 2019, recruitment communications must never discriminate based on gender (*"chỉ tuyển nam/nữ"*), marital status (*"yêu cầu chưa kết hôn"*), pregnancy (*"cam kết không mang thai"*), or appearance (*"ngoại hình ưa nhìn"*).
2. **Probation Duration & Statutory Salary Floor (`HR002`):**
   - **Duration Cap (Điều 25):** Maximum **60 days** for roles requiring collegiate/university qualifications (engineers, designers, managers). A 3-month or 90-day probation is illegal unless specifically for enterprise executives (up to 180 days).
   - **Salary Floor (Điều 26):** Probation salary must equal **at least 85%** of official salary (*"lương thử việc tối thiểu 85%"*). Paying 70% or 75% violates the law.
3. **No Original Document Retention or Financial Deposits (`HR004`):**
   - Under Article 17, employers are strictly forbidden from withholding original diplomas (*"giữ bằng đại học gốc"*), identity cards (*"giữ CCCD gốc"*), or demanding monetary deposits (*"đặt cọc tiền đi làm"*).
4. **No Punitive Wage Deductions (`HR004`):**
   - Under Article 128, imposing monetary fines or salary cuts (*"phạt trừ lương"*) in lieu of standard labor disciplinary proceedings is illegal.

---

## 3. Offer Letter Architecture & Salary Transparency

As established in [references/labor-code-and-offer-letters.md](references/labor-code-and-offer-letters.md), every Offer Letter (`doctype == "offer-letter"`) must maintain absolute compensation transparency:

1. **Gross vs. Net Disclosure (`HR003`):**
   - Stating a bare salary figure (e.g., `30.000.000 ₫/tháng`) without clarifying tax and social insurance deductions triggers candidate disputes.
   - Every salary figure must explicitly designate **Gross** (pre-tax and statutory insurance deductions) or **Net** (take-home pay with company covering taxes and contributions).
2. **Statutory Social Insurance Breakdown (Luật BHXH 41/2024/QH15):**
   - Disclose mandatory contributions: **21.5%** borne by employer, **10.5%** withheld from employee Gross salary (8% retirement/survivorship, 1.5% health insurance, 1% unemployment insurance).

---

## 4. Modern Outcome-Oriented Job Descriptions (JD)

As outlined in [references/jd-and-employer-branding.md](references/jd-and-employer-branding.md), modern recruitment copy focuses on impact and candidate value proposition (EVP):

1. **Deliverables Over Task-Dumping:**
   - Replace tedious operational task lists with outcome-focused ownership (*"Chịu trách nhiệm thiết kế kiến trúc hệ thống backend chịu tải cao với thời gian hoạt động 99,9%"*).
2. **Elimination of Toxic Clichés (`HR005`):**
   - Eliminate exploitative clichés:
     - ❌ `Coi công ty là nhà, làm việc hết mình 24/7 bất kể ngày đêm.`
     - ✅ `Môi trường tôn trọng cân bằng cuộc sống; công ty áp dụng chế độ làm thêm giờ (OT) có trả lương đầy đủ theo luật định.`
     - ❌ `Lương hấp dẫn theo năng lực.`
     - ✅ `Dải thu nhập minh bạch: 25.000.000 ₫ – 35.000.000 ₫ Gross/tháng + thưởng KPI.`

---

## 5. Constructive SBI Performance Appraisals

As detailed in [references/okr-kpi-and-performance-review.md](references/okr-kpi-and-performance-review.md), performance appraisals (`doctype == "performance-review"`) must protect psychological safety:

1. **The SBI Framework (Situation – Behavior – Impact):**
   - Frame feedback around verifiable facts and measurable impact rather than subjective personality judgments (`HR006`).
2. **Eliminating Personal Attacks (`HR006`):**
   - Prohibit abusive phrases (*"thái độ kém cỏi"*, *"lười biếng"*, *"thiếu năng lực bẩm sinh"*). Describe specific observed behaviors and provide forward-looking developmental recommendations.

---

## 6. Typographic & Numerical Standards in Vietnamese HR

To ensure professional documentation and eliminate legal ambiguity:
- **Tiền lương (Salary Notation):** Viết `30.000.000 ₫` kèm số tiền bằng chữ trong các văn bản cam kết thu nhập chính thức: *"Ba mươi triệu đồng chẵn"*.
- **Thời hạn & Ngày tháng (Dates):** Viết theo định dạng ngày/tháng/năm `dd/MM/yyyy` (ví dụ: `01/04/2026`).
- **Giờ làm việc tiêu chuẩn:** Định dạng 24 giờ: `từ 08:30 đến 17:30` (tránh `8:30 AM – 5:30 PM`).
- **Tên viết tắt luật định:** Sử dụng đúng các từ viết tắt pháp luật lao động: `BHXH` (Bảo hiểm xã hội), `BHYT` (Bảo hiểm y tế), `BHTN` (Bảo hiểm thất nghiệp), `thuế TNCN` (Thuế thu nhập cá nhân).

---

## 7. Domain Rules Reference (`HR001`–`HR006`)

| Rule Code | Severity | Context | Description & Statutory Reference |
|---|---|---|---|
| `HR001` | `ERROR` | All copy | Discriminatory hiring criteria (gender, marital status, pregnancy, appearance, age caps) |
| `HR002` | `ERROR` | All copy | Probation salary below 85% floor or duration exceeding 60-day cap for skilled roles |
| `HR003` | `WARN` | `offer-letter` | Stating salary figure without specifying Gross (trước thuế) or Net (thực lĩnh) |
| `HR004` | `ERROR` | All copy | Threatening original document retention, cash deposits, or punitive wage deductions |
| `HR005` | `WARN` | All copy | Vague or toxic JD clichés (`lương hấp dẫn theo năng lực`, `coi công ty là nhà 24/7`) |
| `HR006` | `WARN` | `performance-review` | Subjective personal attacks (`thái độ kém cỏi`, `lười biếng`) instead of SBI feedback |

---

## 8. Reference Documents & Verification Checklist

Review the accompanying reference guides for deep domain knowledge:
- [references/glossary.md](references/glossary.md): 55+ standardized HR, recruitment, and labor law terms.
- [references/banned-phrases.md](references/banned-phrases.md): Prohibited claims, toxic clichés, and discriminatory criteria.
- [references/labor-code-and-offer-letters.md](references/labor-code-and-offer-letters.md): Labor Code 2019 compliance, probation, and offer letters.
- [references/jd-and-employer-branding.md](references/jd-and-employer-branding.md): Modern outcome-oriented JDs and salary transparency.
- [references/okr-kpi-and-performance-review.md](references/okr-kpi-and-performance-review.md): SBI feedback model and OKR/KPI appraisal structures.
- [references/qa-checklist.md](references/qa-checklist.md): Comprehensive pre-publication inspection checklist.
- [references/examples.md](references/examples.md): 32 verified diagnostic pairs with before/after diffs.
- [assets/thu-moi-nhan-viec-offer.md.template](assets/thu-moi-nhan-viec-offer.md.template): Production-grade compliant job offer letter template.

---

## 9. Verification CLI Commands

Audit any recruitment or HR document using `validate_copy.py`:

```bash
# Validate a job offer letter with strict register enforcement
python skills/vietnamese-hr-recruitment/scripts/validate_copy.py \
  path/to/offer.md \
  --doctype offer-letter \
  --register hr-candidate \
  --strict

# Validate a job description
python skills/vietnamese-hr-recruitment/scripts/validate_copy.py \
  path/to/jd.md \
  --doctype job-description \
  --register hr-candidate
```
