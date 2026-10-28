---
name: vietnamese-healthcare-copy
description: Writes, localizes, and audits native-quality Vietnamese (vi-VN) healthcare, medical, hospital, EMR, clinical, pharmacy, and dietary supplement (TPCN) communications. Enforces statutory terminology under Luật Khám bệnh, chữa bệnh 2023 số 15/2023/QH15 (mandatory replacement of 'Chứng chỉ hành nghề' with 'Giấy phép hành nghề khám bệnh, chữa bệnh' from 01/01/2024), electronic medical record (EMR) documentation standards under Thông tư 32/2023/TT-BYT, national electronic prescription requirements under Thông tư 52/2017/TT-BYT and Thông tư 27/2021/TT-BYT (strict prohibition of vague dosage instructions like 'uống khi cần', 'uống tùy ý'), dietary supplement (TPCN) advertising rules under Nghị định 15/2018/NĐ-CP (mandatory statutory disclaimer 'Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh', strict ban on doctor testimonials and patient letters), prohibitions against absolute curative claims ('chữa khỏi hoàn toàn 100%', 'thần dược trị bách bệnh'), patient-centered communication and SPIKES breaking bad news protocol, discharge summary red-flag return instructions under Thông tư 32/2023, and health data confidentiality under Điều 10 Luật KCB and Luật 91/2025/QH15 Điều 26 PDPD.
license: PolyForm-Shield-1.0.0
metadata:
  author: "Jang Trinh"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Healthcare Copywriting & Clinical Compliance (`vietnamese-healthcare-copy`)

In Vietnamese healthcare, copywriting mistakes carry **direct medical, ethical, and statutory liability** rather than mere stylistic flaws. Writing an obsolete licensing term like `Chứng chỉ hành nghề` violates Luật Khám bệnh, chữa bệnh 2023; promising `Chữa khỏi dứt điểm 100%` breaches advertising and medical statutes; omitting the mandatory statutory disclaimer on health supplements triggers immediate sanctions under Nghị định 15/2018/NĐ-CP; and vague dosage instructions like `uống khi cần` threaten patient safety.

This skill equips clinicians, hospital administrators, pharmaceutical marketers, and health-tech developers with authoritative Vietnamese medical copy, clinical EMR standards, and regulatory compliance tools.

---

## 1. Register & Sociolinguistic Etiquette in Healthcare

Healthcare communications in Vietnam operate under strict sociolinguistic conventions:

| Context / Surface | Register | Reader Address (`Hô`) | Speaker (`Xưng`) | Notes |
|---|---|---|---|---|
| Hospital patient portal, appointment booking, discharge instructions | `healthcare` | `Quý khách` | `Chúng tôi` / `[Tên bệnh viện]` | High-respect floor; never use `bạn` or `cả nhà` |
| Electronic Medical Record (EMR), SOAP notes, lab results, prescriptions | `healthcare-clinical` | *(impersonal third-person)* | `Bác sĩ` / *(impersonal)* | Objective third-person (`người bệnh`, `bác sĩ`); zero `bạn`/`quý khách` |
| Dietary supplement (TPCN) landing pages, public health articles | `healthcare` | `Quý khách` / `Người đọc` | `Chúng tôi` / `[Tên thương hiệu]` | Maintain professional advisory tone |
| Emergency return instructions & critical red-flag alerts | `healthcare` | `Quý khách` / `Người bệnh` | `Khoa Cấp cứu` / `Bác sĩ điều trị` | Clear, imperative, urgent action orientation |

> [!IMPORTANT]
> **The Clinical Register Law:** In EMR records, clinical consultation notes, and official prescription orders, the communication must remain strictly impersonal and objective (`healthcare-clinical`). Direct second-person pronouns (`bạn`, `anh/chị`, `em`) are forbidden in clinical notes to preserve legal objectivity.

---

## 2. Supported Healthcare Doctypes

The validator evaluates copy against 5 domain-specific healthcare doctypes:

1. **`tpcn-ad` (Quảng cáo / Mô tả Thực phẩm bảo vệ sức khỏe):**
   - Regulated under Nghị định 15/2018/NĐ-CP Điều 27 and Thông tư 05/2018/TT-BYT.
   - Requires mandatory statutory disclaimer (`MED001`) and strictly prohibits doctor testimonials (`MED005`).
2. **`prescription` (Đơn thuốc ngoại trú / Hướng dẫn dùng thuốc):**
   - Regulated under Thông tư 52/2017/TT-BYT, Thông tư 18/2018/TT-BYT, and Thông tư 27/2021/TT-BYT.
   - Enforces explicit route, single dosage, frequency, timing (`sau ăn`), and warning directions (`MED004`).
3. **`discharge-summary` (Giấy ra viện / Hướng dẫn chăm sóc sau xuất viện):**
   - Regulated under Thông tư 32/2023/TT-BYT (mẫu Giấy ra viện và tóm tắt bệnh án).
   - Enforces emergency red-flag instructions (`MED007`) to protect patients against post-operative complications.
4. **`emr-note` (Hồ sơ bệnh án điện tử EMR / Phiếu kết quả cận lâm sàng):**
   - Regulated under Luật Khám bệnh, chữa bệnh 2023 and Thông tư 32/2023/TT-BYT.
   - Requires standardized SOAP note structure, ICD-10/ICD-11 diagnostic coding, and objective tone.
5. **`clinic-landing` (Trang giới thiệu bệnh viện, phòng khám chuyên khoa, tầm soát):**
   - Regulated under Luật Quảng cáo 2012 và Luật Khám bệnh, chữa bệnh 2023.
   - Enforces Giấy phép hoạt động, Giấy phép hành nghề (`MED003`), and bans unverified superlatives (`LAW001`).

---

## 3. Clinical & EMR Standards (Luật KCB 2023 & Thông tư 32/2023/TT-BYT)

1. **Licensing Terminology Update (`MED003`):**
   - ❌ `Chứng chỉ hành nghề khám bệnh, chữa bệnh` / `Chứng chỉ hành nghề y` *(stale terminology under repealed 2009 law)*.
   - ✅ `Giấy phép hành nghề khám bệnh, chữa bệnh` (or `Giấy phép hành nghề`) under Luật Khám bệnh, chữa bệnh số 15/2023/QH15.
2. **Electronic Prescriptions (Thông tư 52/2017 & TT 27/2021/TT-BYT):**
   - Vague dosage instructions (`MED004`) like `uống khi cần`, `uống tùy ý`, `ngày uống vài lần` are strictly prohibited.
   - Prescriptions must specify route (`Uống`), single dose (`1 viên`), daily frequency (`2 lần/ngày`), timing (`sau ăn 30 phút`), and warning instructions (`Tái khám ngay nếu có dấu hiệu bất thường`).
3. **Discharge Summary Red Flags (`MED007`):**
   - Every discharge summary must feature explicit emergency warning instructions (`Dấu hiệu cần tái khám ngay hoặc đến cơ sở y tế cấp cứu`) covering persistent high fever, incision bleeding/pus, acute pain, or respiratory distress.
4. **Structured Clinical SOAP Notes & Diagnostic Coding:**
   - Diagnostic statements must follow standardized ICD-10/ICD-11 syntax: Primary diagnosis (`Bệnh chính`), comorbidities (`Bệnh kèm theo`), and complications (`Biến chứng`).

---

## 4. Pharmaceutical & Dietary Supplement (TPCN) Compliance

1. **Mandatory Statutory Disclaimer (`MED001`):**
   - Under **Nghị định 15/2018/NĐ-CP Điều 27**, all health supplement advertising and packaging must display:
     `"Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."`
2. **Prohibition of Curative & Absolute Claims (`MED002`):**
   - Absolute therapeutic promises are illegal: `chữa khỏi hoàn toàn 100%`, `điều trị dứt điểm vĩnh viễn`, `cam kết khỏi bệnh 100%`, `thần dược trị bách bệnh`, `thay thế hoàn toàn thuốc đặc trị`.
3. **Ban on Doctor Endorsements & Patient Testimonials (`MED005`):**
   - Advertising health supplements using physician imagery, medical uniforms, patient thank-you letters (`thư cảm ơn của bệnh nhân`), or testimonial videos is strictly prohibited under Decree 15/2018/NĐ-CP Điều 27 khoản 2.
4. **Medical Device Classification (Nghị định 98/2021 & 07/2023):**
   - Distinguish Category A (low risk), Category B (low-moderate risk), Category C (moderate-high risk), and Category D (high risk/implantables).

---

## 5. Patient-Centered Communication & Empathetic Tone

1. **Eliminate Stigmatizing & Blaming Language (`MED006`):**
   - ❌ `Bệnh nhân không chịu hợp tác` → ✅ `Người bệnh chưa phối hợp tuân thủ điều trị`.
   - ❌ `Bệnh nan y vô phương cứu chữa` → ✅ `Tiên lượng dè dặt / bệnh giai đoạn tiến triển`.
   - ❌ `Con nghiện` → ✅ `Người điều trị nghiện chất` / `Người bệnh rối loạn sử dụng chất`.
   - ❌ `Kẻ tâm thần`, `Bị điên` → ✅ `Người bệnh rối loạn sức khỏe tâm thần`.
2. **Breaking Bad News (SPIKES Protocol in Vietnamese):**
   - Structured 6-step approach: Setting (bối cảnh riêng tư) → Perception (thăm dò nhận thức) → Invitation (thăm dò nhu cầu thông tin) → Knowledge (trao đổi thông tin y khoa bình dị) → Empathy (thấu cảm, đồng hành) → Strategy & Summary (phác đồ điều trị tiếp theo).
3. **Health Data Privacy (Điều 10 Luật KCB 2023 & Luật 91/2025/QH15 Điều 26):**
   - Medical records and health conditions are sensitive personal data; public disclosure without written consent is strictly prohibited. De-identify all patient identifiers in academic or clinical case reports.

---

## 6. Medical Number Typography & Lab Formatting

- **Vietnamese Digit Grouping (`NUM001` & `NUM003`):**
  - Group thousands with periods: `1.500.000 ₫`, `250.000 ₫` (never commas: `1,500,000`).
  - Decimal fractions separated by comma: `HbA1c 6,5%`, `đường huyết 7,2 mmol/L`, `thân nhiệt 38,5 °C` (never periods: `6.5%`).
- **Standard Clinical Units & Orthography:**
  - Standardized units: `g/dL`, `mmol/L`, `mmHg`, `lần/phút`, `mg/ngày`.
  - Date format: strict `dd/MM/yyyy` (`26/10/2026`).

---

## 7. Validation & CLI Usage

Run the integrated validator before publishing or committing healthcare documentation:

```bash
# Validate discharge summary under healthcare register
python skills/vietnamese-healthcare-copy/scripts/validate_copy.py discharge.md --doctype discharge-summary --register healthcare --strict

# Validate dietary supplement (TPCN) advertising copy
python skills/vietnamese-healthcare-copy/scripts/validate_copy.py tpcn.md --doctype tpcn-ad --register healthcare --strict

# Validate outpatient electronic prescription
python skills/vietnamese-healthcare-copy/scripts/validate_copy.py prescription.md --doctype prescription --register healthcare-clinical --strict

# Validate hospital or clinic landing page
python skills/vietnamese-healthcare-copy/scripts/validate_copy.py landing.md --doctype clinic-landing --strict

# Validate clinical EMR note
python skills/vietnamese-healthcare-copy/scripts/validate_copy.py emr.md --doctype emr-note --register healthcare-clinical --strict
```

---

## 8. Validator Rule Reference

| Rule Code | Severity | Description |
|---|---|---|
| `MED001` | ERROR | Missing mandatory statutory disclaimer in TPCN copy (NĐ 15/2018/NĐ-CP) |
| `MED002` | ERROR | Prohibited therapeutic or curative claims (`chữa khỏi hoàn toàn 100%`, `thần dược`) |
| `MED003` | WARNING | Obsolete licensing terminology (`Chứng chỉ hành nghề y/KCB` replaced by `Giấy phép hành nghề`) |
| `MED004` | ERROR | Vague dosage instructions (`uống khi cần`) or missing dosage units/warning signs in prescription |
| `MED005` | ERROR | Prohibited patient testimonial or doctor endorsement tactics in healthcare/TPCN copy |
| `MED006` | WARNING | Stigmatizing, alarmist, or patient-blaming language in clinical or patient communications |
| `MED007` | ERROR | Discharge summary missing red-flag emergency return instructions |
| `CAL001` | ERROR / WARN | Healthcare translationese and medical calques from `glossary.md` and `banned-phrases.md` |
| `LAW001` | ERROR | Unsubstantiated medical superlatives (`bệnh viện tốt nhất`, `phòng khám số 1`) |
| `NUM001`–`NUM003` | ERROR / WARN | Vietnamese thousand periods (`2.500.000 ₫`) and decimal comma (`6,8 mmol/L`) |
| `PRO001` / `PRO002` | WARNING | Healthcare register violations (casual `bạn` in formal medical care communications) |

---

## 9. Reference Files

- [references/glossary.md](references/glossary.md) — 60+ standardized medical, hospital, EMR, and pharmaceutical terms.
- [references/banned-phrases.md](references/banned-phrases.md) — Prohibited curative claims, fake doctor endorsement patterns, and superlatives.
- [references/clinical-and-emr-writing.md](references/clinical-and-emr-writing.md) — Comprehensive guide on Luật KCB 2023, EMR Thông tư 32/2023, ICD coding, and national e-prescriptions.
- [references/pharma-and-tpcn-compliance.md](references/pharma-and-tpcn-compliance.md) — Statutory compliance for health supplements (TPCN), SmPC/PIL package inserts, and medical device tiers.
- [references/patient-communication.md](references/patient-communication.md) — Patient-centered communication, SPIKES protocol for breaking bad news, procedure preparation, and PDPD privacy.
- [references/qa-checklist.md](references/qa-checklist.md) — 15-point pre-publish quality gate for clinicians, marketers, and legal counsel.
- [assets/huong-dan-xuat-vien.md.template](assets/huong-dan-xuat-vien.md.template) — Fully compliant discharge summary template.
- [assets/thong-tin-tpcn.md.template](assets/thong-tin-tpcn.md.template) — Fully compliant health supplement (TPCN) disclosure template.
