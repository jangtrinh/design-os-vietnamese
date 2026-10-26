---
id: "education-moet-and-edtech"
title: "Vietnamese Education Standards: MOET Circular 22/2021/TT-BGDĐT (GDPT 2018) and KNLNN 6 Bậc"
domain: "vietnamese-education-and-edtech"
description: "Verified specification for K-12 student assessment terminology under MOET Circular 22/2021/TT-BGDĐT, Vietnam's 6-level Foreign Language Proficiency Framework (KNLNN 6 bậc), and EdTech advertising compliance."
when:
  - "Designing LMS dashboards, digital report cards (học bạ số), or EdTech course pages for Vietnam"
  - "Mapping language proficiency levels to KNLNN 6 bậc (Circular 01/2014/TT-BGDĐT) and CEFR"
  - "Auditing education copy with validate_copy.py --domain edu"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md"
    sha256: "c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290"
---

# Vietnamese Education Standards: MOET Circular 22/2021/TT-BGDĐT (GDPT 2018) and KNLNN 6 Bậc

## Purpose

Defines the statutory K-12 assessment terminology under MOET Circular 22/2021/TT-BGDĐT (`Chương trình GDPT 2018`), foreign language certification nomenclature under Circular 01/2014/TT-BGDĐT (`KNLNN 6 bậc`), and ethical EdTech claim standards.

## When to Use / When NOT

- **When to Use:**
  - Building or auditing K-12 school management systems (`học bạ số`), LMS interfaces, parent notifications, and EdTech course landing pages in Vietnam.
- **When NOT to Use:**
  - Archival transcripts from pre-2021 cohorts that preserve historical Circular 58/2011/TT-BGDĐT labels verbatim.

## Core Knowledge Content

### 1. K-12 Assessment Terminology Under Circular 22/2021/TT-BGDĐT (`EDU001`)

MOET Circular 22/2021/TT-BGDĐT governs K-12 student assessment under the 2018 General Education Curriculum (GDPT 2018), replacing legacy `Học lực: Giỏi / Tiên tiến / Yếu / Kém` labels with the 4-tier classification `Tốt — Khá — Đạt — Chưa đạt` for both conduct (`Kết quả rèn luyện`) and learning outcomes (`Kết quả học tập`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="MOET Circular 22/2021/TT-BGDĐT governs K-12 student assessment under the 2018 General Education Curriculum (GDPT 2018), replacing legacy 'Học lực: Giỏi / Tiên tiến / Yếu / Kém' labels with the 4-tier classification 'Tốt — Khá — Đạt — Chưa đạt' for both conduct ('Kết quả rèn luyện') and learning outcomes ('Kết quả học tập')." -->

### 2. Foreign Language Proficiency Framework (`KNLNN 6 Bậc`) and EdTech Claims (`EDU002`, `EDU003`)

Under Circular 01/2014/TT-BGDĐT, Vietnam's 6-level Foreign Language Proficiency Framework (`Khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam` — `KNLNN 6 bậc`, assessed via VSTEP) maps `Bậc 1–6` to CEFR `A1–C2`; EdTech platforms must neither equate non-accredited internal quiz scores with official VSTEP certificates nor promise `Cam kết 100% đỗ đại học / đạt IELTS 8.0`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/03-vietnam-statutory-regulatory-corpus.md" sha256="c367b62b33da872f4c4477b922d9e94c589012e98581cc33e7c042a0858b8290" quote="Under Circular 01/2014/TT-BGDĐT, Vietnam's 6-level Foreign Language Proficiency Framework (Khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam — KNLNN 6 bậc, assessed via VSTEP) maps Bậc 1–6 to CEFR A1–C2; EdTech platforms must neither equate non-accredited internal quiz scores with official VSTEP certificates nor promise 'Cam kết 100% đỗ đại học / đạt IELTS 8.0'." -->

## Failure Modes (Mandatory)

1. **Obsolete K-12 Grading Labels (`EDU001`):** Displaying `Xếp loại học lực: Học sinh Tiên tiến / Học sinh Yếu / Kém` in a modern GDPT 2018 school portal instead of `Kết quả học tập: Tốt / Khá / Đạt / Chưa đạt`.
2. **Unverified Exam Outcome Guarantees (`EDU002`):** Advertising `Cam kết 100% đỗ đại học nguyện vọng 1` or `Bảo đảm đạt IELTS 7.5 không cần học ngữ pháp` without contractual outcome conditions.
3. **Misrepresenting Internal Completion Badges as Statutory Degrees (`EDU003`):** Calling a short-course completion badge `Bằng cấp chuẩn Quốc gia Bậc 4 VSTEP` when the provider is not licensed by MOET to administer VSTEP exams.
