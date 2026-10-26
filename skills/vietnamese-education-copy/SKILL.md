---
name: vietnamese-education-copy
description: Writes, evaluates, and pedagogically audits native-quality Vietnamese (vi-VN) educational, academic, and EdTech communications. Enforces statutory Ministry of Education and Training (Bộ GD&ĐT) grading and assessment circulars, including Thông tư 22/2021/TT-BGDĐT for secondary and high schools (THCS/THPT evaluation scale of Tốt, Khá, Đạt, Chưa đạt and total abolition of học sinh tiên tiến), Thông tư 27/2020/TT-BGDĐT for primary education (mandating the statutory cần cố gắng over the calque cần cải thiện), Thông tư 08/2021/TT-BGDĐT for higher education (tín chỉ for academic credits and Vietnamese decimal comma GPA notation), and Thông tư 21/2019/TT-BGDĐT for diploma issuance (bản sao từ sổ gốc). Embeds modern learning science and EdTech AI tutoring frameworks (Spaced Repetition, 3PL IRT adaptive difficulty scaling, ZPD 3-tier scaffolding, Goodness of Pronunciation [GOP] Sandwich feedback for all 6 Vietnamese tones, and Self-Determination Theory to prevent overjustification), statutory child data protection compliance under Nghị định 13/2023/NĐ-CP Điều 20 (minor double consent requiring verified approval from phụ huynh or người giám hộ), and sociolinguistic register discipline across edu-k12, edu-k12-primary, edu-parent, and edu-uni.
license: MIT
metadata:
  version: "2.0.0"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Educational Copywriting & Learning Science (`vietnamese-education-copy`)

Writing for education in Vietnam fails when it flattens a deeply hierarchical, pedagogically codified, and legally regulated ecosystem into a generic Western tone. In Vietnam, a teacher writing report-card remarks for an 8-year-old (`thầy/cô` $\rightarrow$ `con`), an AI agent tutoring high-school pronunciation (`thầy/cô` $\rightarrow$ `em`), a school broadcasting to parents (`nhà trường` $\rightarrow$ `Quý phụ huynh`), and a university registrar publishing a syllabus (`edu-uni`, impersonal third-person) inhabit distinct sociolinguistic registers. Addressing a secondary student as `bạn` immediately reveals careless translation, while outputting abolished grading terms (`học sinh tiên tiến`, `xếp loại giỏi`) invalidates formal student transcripts (`học bạ`).

This skill provides educators, instructional designers, and EdTech product developers with authoritative guidelines, statutory MoET compliance checks, and pedagogical feedback frameworks.

---

## 1. Register Architecture & Persona Mapping

Vietnamese educational address (`xưng – hô`) encodes age group, institutional authority, and emotional warmth:

| Context / Surface | Register | Reader (`Hô`) | Speaker (`Xưng`) | Pedagogical Function & Guidelines |
|---|---|---|---|---|
| Primary School (Lớp 1–5, Tiểu học) | `edu-k12-primary` | `con` | `thầy` / `cô` | Nurturing, family-like pastoral care. Forbids `bạn`, `quý khách`, `em`. |
| Secondary & High School (Lớp 6–12, THCS/THPT) | `edu-k12` | `em` | `thầy` / `cô` | Traditional Vietnamese classroom register. Respectful mentor dynamic. Forbids `bạn`, `quý khách`. |
| School / App $\rightarrow$ Parents | `edu-parent` | `Quý phụ huynh` | `Nhà trường` / `Hệ thống` | Formal school-to-home partnership (`sổ liên lạc`). Forbids casual `bạn`, `mình`, `cả nhà`. |
| University & Higher Ed | `edu-uni` | *(impersonal)* | *(impersonal)* | Syllabi, transcripts, administrative notices. Refers to learner as `sinh viên` / `học viên`. |
| EdTech AI Tutor / Mascot | `edu-k12` / `edu-k12-primary` | `em` / `con` / `bạn nhỏ` | `thầy` / `cô` / `[Tên linh vật]` | Growth Mindset mentor. Forbids harsh or discouraging evaluation tags. |

---

## 2. Statutory MoET Grading Circulars (Bộ GD&ĐT)

Vietnamese grading systems are codified by specific Ministry of Education and Training circulars. Do not guess terminology:

### A. Secondary & High School (THCS & THPT — Thông tư 22/2021/TT-BGDĐT)
Effective since 2021, Thông tư 22/2021 established a four-tier overall evaluation scale:
- **Statutory Tiers:** `Tốt`, `Khá`, `Đạt`, `Chưa đạt`.
- **Abolished Titles (`EDU001`):**
  - ❌ `Học sinh Tiên tiến` *(completely abolished; replaced by `Học sinh Khá`)*
  - ❌ `Xếp loại Giỏi / Trung bình / Yếu / Kém` *(abolished as overall report-card classification)*
  - ✅ `Học sinh Xuất sắc`, `Học sinh Giỏi` *(merit recognition titles)*

### B. Primary School Routine Assessment (Tiểu học — Thông tư 27/2020/TT-BGDĐT)
- **Qualitative Assessment Scale:** `Hoàn thành tốt`, `Hoàn thành`, `Cần cố gắng`.
- **The Calque Trap (`EDU003`):**
  - ❌ `Cần cải thiện` *(literal English calque for "needs improvement")*
  - ✅ `Cần cố gắng` *(mandatory statutory phrase under Thông tư 27/2020 Điều 7)*

### C. Higher Education Credit & GPA (Đại học — Thông tư 08/2021/TT-BGDĐT)
- **Academic Credit (`EDU005`):**
  - ❌ `Tín dụng` *(financial loan/credit)*
  - ✅ `Tín chỉ` *(academic course credit)*
- **GPA Decimal Notation (`EDU006`):**
  - Vietnamese transcripts write GPA using a **decimal comma**: `3,6/4,0` or `8,5/10` (never dot `3.6/4.0`).
- **Academic Honours:** `Xuất sắc`, `Giỏi`, `Khá`, `Trung bình`.

### D. Diploma Issuance & Reissuance (Thông tư 21/2019/TT-BGDĐT)
- Original degrees and diplomas (`văn bằng, chứng chỉ`) are issued **only once**.
- When lost or damaged, educational institutions **never re-issue an original diploma**. They only grant a certified copy from the master registry (`cấp bản sao từ sổ gốc`). Outputting "cấp lại bằng gốc" is a legal impossibility.

---

## 3. Learning Science & EdTech Pedagogical Frameworks

### A. The Sandwich Feedback Model for Pronunciation (`EDU009`)
When delivering acoustic scoring feedback (GOP - Goodness of Pronunciation across Vietnamese's 6 phonemic tones: *ngang, huyền, sắc, hỏi, ngã, nặng*):
- ❌ **Harsh / Unpedagogical:** `Sai rồi! Điểm của bạn là 35%. Bạn đã phát âm sai thanh ngã.`
- ✅ **Compliant Sandwich Model:**
  1. *Praise Effort:* `"Em đã phát âm phụ âm đầu rất rõ ràng!"`
  2. *Actionable Phoneme Guidance:* `"Ở thanh ngã (~), em hãy thử nâng cao cao độ và ngắt nhẹ hơi ở giữa âm tiết nhé."`
  3. *Growth Mindset Encouragement:* `"Hãy bấm nút và thử lại lần nữa nào, em sắp làm chủ được từ này rồi!"`

### B. Adaptive Assessment (3PL IRT & ZPD Scaffolding)
- Integrate Item Response Theory (IRT parameters: $a$ discrimination, $b$ difficulty, $c$ pseudo-guessing) into question generation.
- Scaffold assistance within Vygotsky's Zone of Proximal Development (ZPD) through 3-tier fading hints:
  - *Tier 1 (Conceptual):* Remind of the underlying grammar rule or formula.
  - *Tier 2 (Strategic):* Provide a directional hint or eliminate two distractors.
  - *Tier 3 (Operational):* Walk through the step-by-step resolution.

### C. Actionable Empty States (`EDU007`)
In student dashboards and homework lists:
- ❌ `Trạng thái trống` / `Không có dữ liệu` *(cold technical calques)*
- ✅ `"Chưa có bài tập nào cần nộp hôm nay! Em có muốn ôn lại bài kiểm tra tuần trước không?"` *(actionable CTA)*

---

## 4. Child Data Protection & Privacy (Nghị định 13/2023/NĐ-CP Điều 20 — `EDU010`)

Under Vietnam's Personal Data Protection Decree (**Nghị định 13/2023/NĐ-CP Điều 20**), processing personal data of children ($\ge 7$ years old) requires **double consent**:
1. Consent of the child.
2. Verified consent of the child's parent or legal guardian (`phụ huynh` hoặc `người giám hộ`).

Any student onboarding flow, EdTech registration, voice-recording consent, or behavioral telemetry collection that omits explicit parental/guardian consent triggers `EDU010`.

---

## 5. Validation & CLI Usage

Audit educational markdown files, syllabi, report cards, or app copy using the integrated linter:

```bash
# Secondary school report card / học bạ
python skills/vietnamese-education-copy/scripts/validate_copy.py hoc-ba.md --doctype secondary-report-card --register edu-k12 --strict

# Primary school sổ liên lạc
python skills/vietnamese-education-copy/scripts/validate_copy.py so-lien-lac.md --doctype primary-report-card --register edu-parent --strict

# Teacher direct remark
python skills/vietnamese-education-copy/scripts/validate_copy.py remark.md --doctype teacher-to-student --register edu-k12 --strict

# University syllabus / transcript
python skills/vietnamese-education-copy/scripts/validate_copy.py syllabus.md --doctype higher-ed --register edu-uni --strict
python skills/vietnamese-education-copy/scripts/validate_copy.py transcript.md --doctype transcript --register edu-uni --strict

# EdTech app microcopy and child consent flow
python skills/vietnamese-education-copy/scripts/validate_copy.py app.md --doctype edtech-microcopy --strict
python skills/vietnamese-education-copy/scripts/validate_copy.py onboarding.md --doctype child-consent --strict
```

### Validator Rule Reference
- `EDU001`: Abolished secondary classification (`học sinh tiên tiến`, `xếp loại giỏi/yếu`).
- `EDU002`: Teacher addressing a student as `bạn`.
- `EDU003`: Primary assessment using `cần cải thiện` instead of statutory `cần cố gắng`.
- `EDU005`: Academic credit written as `tín dụng` instead of `tín chỉ`.
- `EDU006`: GPA formatted with dot decimal (`3.8/4.0`) instead of comma (`3,8/4,0`).
- `EDU007`: Literal cold empty state on EdTech interface.
- `EDU009`: Harsh, unpedagogical pronunciation feedback violating the Sandwich model.
- `EDU010`: Child data onboarding omitting mandatory parental/guardian consent.

---

## 6. Reference Guides

- [references/glossary.md](references/glossary.md) — 65+ statutory school, academic, and EdTech terms.
- [references/banned-phrases.md](references/banned-phrases.md) — Educational calques, unpedagogical phrases, and admissions superlatives.
- [references/grading-terminology.md](references/grading-terminology.md) — Full text breakdown of TT 22/2021, TT 27/2020, TT 08/2021, and GDPT 2018 qualities & competencies.
- [references/doc-registers.md](references/doc-registers.md) — Register matrix and tone guidelines across K-12, university, and parent communications.
- [references/edtech-pedagogy.md](references/edtech-pedagogy.md) — Learning science frameworks: 3PL IRT, ZPD scaffolding, GOP 6-tone acoustics, SDT, and child privacy.
- [references/qa-checklist.md](references/qa-checklist.md) — Comprehensive pre-publishing checklist for educators and instructional designers.
- [assets/phieu-nhan-xet-hoc-ba.md.template](assets/phieu-nhan-xet-hoc-ba.md.template) — Clean secondary report-card template.
