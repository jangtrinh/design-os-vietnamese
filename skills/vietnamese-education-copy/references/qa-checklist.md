<!-- vlc-disable: all -->

# Educational Copywriting & Pedagogical QA Checklist (`design-os-vietnamese`)

Before publishing student report-card entries, teacher evaluation remarks, school-to-home broadcast notices, university syllabi, or EdTech application microcopy, verify all criteria against this checklist.

---

## 1. Register & Sociolinguistic Etiquette

- [ ] **1. K-12 Student Direct Address (`EDU002`):**
  - Are secondary/high school students (THCS/THPT) addressed with dignity as `em`?
  - Are primary school pupils addressed warmly as `con` or `bạn nhỏ`?
  - Is `bạn` strictly eliminated from teacher-to-student instructions and automated AI tutor dialogues?
- [ ] **2. School-to-Parent Respect (`edu-parent`):**
  - Do announcements and messages address parents collectively as `Quý phụ huynh`?
  - Are inappropriate commercial registers (`Quý khách`) or literal translations (`các cha mẹ`) completely avoided?
- [ ] **3. University Administrative Tone (`edu-uni`):**
  - Are university syllabi, regulations, and official course announcements written in impersonal third-person, referring to the learner as `sinh viên`?
  - Are casual second-person pronouns (`bạn`, `em`) absent from statutory university regulations?

---

## 2. Statutory MoET Grading Compliance (Bộ GD&ĐT)

- [ ] **4. Secondary Evaluation Tiers (Thông tư 22/2021/TT-BGDĐT — `EDU001`):**
  - Is the overall classification scale strictly limited to `Tốt`, `Khá`, `Đạt`, `Chưa đạt`?
  - Have deprecated titles like `Học sinh Tiên tiến` or overall labels of `Giỏi/Trung bình` been eliminated?
- [ ] **5. Primary Qualitative Remarks (Thông tư 27/2020/TT-BGDĐT — `EDU003`):**
  - Is the phrase `Cần cố gắng` used for routine formative assessment?
  - Has the English calque `Cần cải thiện` been replaced?
- [ ] **6. Academic Credits in Higher Ed (Thông tư 08/2021/TT-BGDĐT — `EDU005`):**
  - Is academic course credit referred to as `tín chỉ`?
  - Is `tín dụng` strictly reserved for financial loan contexts?
- [ ] **7. Vietnamese GPA Decimal Comma (`EDU006`):**
  - Are GPA and course grade averages formatted with a Vietnamese decimal comma (e.g. `3,6/4,0` or `8,5/10`)?
- [ ] **8. Diploma Reissuance Integrity (Thông tư 21/2019/TT-BGDĐT):**
  - Does the text specify `cấp bản sao từ sổ gốc` for lost credentials?
  - Is the legally void claim of "cấp lại bằng gốc" absent?
- [ ] **9. Electronic School Ledger Standards (Sổ điểm và học bạ điện tử):**
  - Are digital signature blocks and timestamp formats compliant with Ministry of Education regulations?

---

## 3. Learning Science & EdTech Pedagogical UX

- [ ] **10. Sandwich Pronunciation Feedback (`EDU009`):**
  - Does speaking/pronunciation feedback open with praise for effort or correct phonemes?
  - Does it provide concrete guidance for pitch, tone, or tongue placement?
  - Does it conclude with Growth Mindset encouragement rather than blunt failure tags (`Sai rồi`)?
- [ ] **11. Actionable Empty States (`EDU007`):**
  - Do blank homework lists, course dashboards, or quiz screens provide an encouraging call to action rather than raw `Trạng thái trống` or `Không có dữ liệu`?
- [ ] **12. Child Personal Data Double Consent (Luật 91/2025/QH15 Điều 24 — `EDU010`):**
  - Does any onboarding or account registration flow for children under 16 explicitly require verified consent from `phụ huynh` or `người giám hộ`?
- [ ] **13. Adherence to GDPT 2018 Dimensions:**
  - Do qualitative report-card comments evaluate student progress across the 5 Core Qualities (*Yêu nước, Nhân ái, Chăm chỉ, Trung thực, Trách nhiệm*) and Core Competencies?
- [ ] **14. Retention Nudges & Habit Loops:**
  - Are reminder notifications framed around positive cognitive benefits rather than shame or guilt?
- [ ] **15. Anti-Overjustification in Gamification:**
  - Are badges and points balanced with genuine feedback on competence and problem-solving strategy?
- [ ] **16. Positive Discipline & Emotional Safety:**
  - Does commentary uphold principles of positive discipline without sarcastic or comparative remarks between students?

---

## 4. Inclusive Education & Assistive Accessibility

- [ ] **17. Inclusive Pedagogy (Giáo dục hòa nhập):**
  - Are learning materials adapted with descriptive alt-text and screen-reader accessibility for visually or hearing impaired students?
  - Does evaluation respect individualized learning plans (Kế hoạch giáo dục cá nhân - IEP) for students with special educational needs?

---

## 5. Academic Integrity & Quality Sign-Off

- [ ] **18. Plagiarism & Generative AI Policy:**
  - Do course syllabi explicitly state the institution's academic integrity expectations and guidelines for citation of AI tools?
- [ ] **19. Automated Linter Verification:**
  - Has the copy passed `validate_copy.py` with `--strict` enabled and zero findings?

---

## 6. Formal Institutional Sign-Off Block

For formal school transcripts, semester evaluation books (`học bạ`), and academic syllabi:
- **Giáo viên chủ nhiệm / Giảng viên phụ trách:** Họ và tên, Ngày ký, Xác nhận tính trung thực và khách quan của các nhận xét.
- **Tổ trưởng chuyên môn:** Họ và tên, Ngày duyệt, Xác nhận tiêu chuẩn học thuật.
- **Ban Giám hiệu / Trưởng khoa duyệt:** Họ và tên, Ngày ký số, Đóng dấu xác nhận của cơ sở giáo dục.
