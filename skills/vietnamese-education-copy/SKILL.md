---
name: vietnamese-education-copy
description: Writes, evaluates, and pedagogically audits native-quality Vietnamese (vi-VN) educational, academic, and EdTech communications across the full 7-tier Vietnamese Pedagogy Continuum (Mầm non -> Tiểu học -> THCS/THPT -> GDNN -> Đại học -> Thạc sĩ -> Tiến sĩ & GS/PGS). Enforces statutory Ministry of Education and Training (Bộ GD&ĐT) and Ministry of Labour, Invalids and Social Affairs (Bộ LĐ-TB&XH) circulars, including VBHN 01/VBHN-BGDĐT for preschool developmental milestones across 5 domains (forbidding numeric scores and K-12 grades), Thông tư 27/2020/TT-BGDĐT for primary education (mandating cần cố gắng over cần cải thiện), Thông tư 22/2021/TT-BGDĐT for secondary and high schools (THCS/THPT scale of Tốt/Khá/Đạt/Chưa đạt and abolition of học sinh tiên tiến), Thông tư 04/2022/TT-BLĐTBXH for TVET vocational modules and credits, Thông tư 08/2021/TT-BGDĐT for higher education (tín chỉ and decimal comma GPA notation), Thông tư 23/2021/TT-BGDĐT for Master's theses (luận văn / đề án thạc sĩ), Thông tư 18/2021/TT-BGDĐT & QĐ 37/2018/QĐ-TTg for Doctoral dissertations (luận án tiến sĩ) and academic rank (GS/PGS) vs academic degree (TS/ThS/Cử nhân) distinctions, and Thông tư 21/2019/TT-BGDĐT for diploma issuance (bản sao từ sổ gốc). Embeds modern learning science and EdTech AI tutoring frameworks (Spaced Repetition, 3PL IRT adaptive difficulty scaling, ZPD 3-tier scaffolding, Goodness of Pronunciation [GOP] Sandwich feedback for all 6 Vietnamese tones, and Self-Determination Theory to prevent overjustification), statutory child data protection compliance under Luật 91/2025/QH15 Điều 24 (minor double consent requiring verified approval from phụ huynh or người giám hộ), and sociolinguistic register discipline across edu-preschool, edu-k12-primary, edu-k12, edu-parent, edu-uni, and edu-postgrad.
license: PolyForm-Shield-1.0.0
metadata:
  version: "2.1.0"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Educational Copywriting & Learning Science (`vietnamese-education-copy`)

Writing for education in Vietnam fails when it flattens a deeply hierarchical, pedagogically codified, and legally regulated ecosystem into a generic Western tone. In Vietnam, a preschool teacher observing a 4-year-old (`cô` $\rightarrow$ `con`), a primary teacher evaluating qualities (`cô` $\rightarrow$ `con`, `cần cố gắng`), an AI agent tutoring high-school pronunciation (`thầy/cô` $\rightarrow$ `em`), a school broadcasting to parents (`nhà trường` $\rightarrow$ `Quý phụ huynh`), a university publishing a syllabus (`edu-uni`, impersonal `sinh viên`), and a doctoral researcher writing a dissertation (`edu-postgrad`, impersonal `nghiên cứu sinh` / `tác giả`) inhabit distinct sociolinguistic registers. Addressing a secondary student as `bạn` immediately reveals careless translation; applying numeric grades to a preschooler violates developmental regulations (`EDU011`); confusing academic rank (*học hàm Giáo sư*) with an academic degree (*học hàm Tiến sĩ* — `EDU004`) destroys scholarly credibility; while outputting abolished grading terms (`học sinh tiên tiến`, `xếp loại giỏi`) invalidates formal student transcripts (`học bạ`).

This skill provides educators, researchers, instructional designers, and EdTech product developers with authoritative guidelines, statutory MoET/MOLISA compliance checks, and pedagogical feedback frameworks across all 7 tiers of Vietnamese education.

---

## 1. Register Architecture & Persona Mapping

Vietnamese educational address (`xưng – hô`) encodes age group, institutional authority, and emotional warmth:

| Context / Surface | Register | Reader (`Hô`) | Speaker (`Xưng`) | Pedagogical Function & Guidelines |
|---|---|---|---|---|
| Early Childhood / Preschool (Mầm non: 3 tháng – 6 tuổi) | `edu-preschool` | `con` / `bạn nhỏ` | `cô` | Nurturing pastoral care. Qualitative observation of 5 domains. Forbids `bạn`, `quý khách`, `em`. |
| Primary School (Lớp 1–5, Tiểu học) | `edu-k12-primary` | `con` | `thầy` / `cô` | Nurturing mentor dynamic. Forbids `bạn`, `quý khách`, `em`. Uses `cần cố gắng`. |
| Secondary & High School (Lớp 6–12, THCS/THPT) | `edu-k12` | `em` | `thầy` / `cô` | Traditional Vietnamese classroom register. Respectful mentor dynamic. Forbids `bạn`, `quý khách`. |
| School / App $\rightarrow$ Parents | `edu-parent` | `Quý phụ huynh` | `Nhà trường` / `Hệ thống` | Formal school-to-home partnership (`sổ liên lạc`). Forbids casual `bạn`, `mình`, `cả nhà`. |
| TVET & Undergraduate (GDNN & Đại học) | `edu-uni` | *(impersonal)* | *(impersonal)* | Syllabi, transcripts, course regulations. Refers to learner as `sinh viên` / `học viên`. |
| Postgraduate (Thạc sĩ, Tiến sĩ & GS/PGS) | `edu-postgrad` | *(impersonal)* | *(impersonal)* | Scholarly dissertations, defense councils. Refers to researcher as `nghiên cứu sinh` (`NCS`) / `học viên` / `tác giả`. Forbids casual/K-12 pronouns. |
| EdTech AI Tutor / Mascot | `edu-k12` / `edu-preschool` | `em` / `con` / `bạn nhỏ` | `thầy` / `cô` / `[Linh vật]` | Growth Mindset mentor. Forbids harsh or discouraging evaluation tags. |

---

## 2. Statutory Regulations Across the 7 Pedagogy Tiers

### A. Mầm non (Nhà trẻ 3–36 tháng & Mẫu giáo 3–6 tuổi — VBHN 01/VBHN-BGDĐT)
- **Cốt lõi sư phạm (`EDU011`):** Tuyệt đối **không chấm điểm số** (`điểm 10`, `9/10 điểm`), không xếp loại học lực kiểu phổ thông (`Giỏi/Khá/Trung bình/Yếu/Kém`), không phân loại A/B/C.
- **5 Lĩnh vực phát triển:** Thể chất, Nhận thức, Ngôn ngữ, Tình cảm và Kỹ năng xã hội, Thẩm mỹ (đánh giá định tính: `Đạt` / `Chưa đạt` theo chỉ số độ tuổi).
- **Sức khỏe & Thể lực:** Biểu đồ tăng trưởng WHO (chiều cao, cân nặng định kỳ: `Bình thường - Kênh A`, `Suy dinh dưỡng`, `Thừa cân`).

### B. Tiểu học (Lớp 1–5 — Thông tư 27/2020/TT-BGDĐT)
- **Đánh giá kết quả học tập:** `Hoàn thành tốt (HTT)`, `Hoàn thành (HT)`, `Chưa hoàn thành (CHT)`.
- **Đánh giá phẩm chất & năng lực:** `Tốt`, `Đạt`, `Cần cố gắng` (`EDU003`: cấm dùng từ calque `cần cải thiện`).
- **Danh hiệu thi đua:** `Học sinh Xuất sắc`, `Học sinh Tiêu biểu hoàn thành tốt trong học tập và rèn luyện` (không dùng "Học sinh Giỏi/Tiên tiến").

### C. THCS & THPT (Lớp 6–12 — Thông tư 22/2021/TT-BGDĐT)
- **Thang đánh giá 4 mức tổng thể:** `Tốt`, `Khá`, `Đạt`, `Chưa đạt`.
- **Bài trừ thuật ngữ cũ (`EDU001`):**
  - ❌ `Học sinh Tiên tiến` *(đã bãi bỏ hoàn toàn)*.
  - ❌ `Xếp loại Giỏi / Trung bình / Yếu / Kém` *(đã bãi bỏ làm phân loại tổng thể học bạ)*.
- **Chương trình GDPT 2018:** Môn học bắt buộc và cụm 4 môn lựa chọn định hướng nghề nghiệp.

### D. Giáo dục Nghề nghiệp (Trung cấp & Cao đẳng — Luật GDNN & TT 04/2022/TT-BLĐTBXH)
- Cơ quan quản lý nhà nước: Bộ Lao động - Thương binh và Xã hội (Tổng cục GDNN).
- Thuật ngữ đơn vị học tập: `Mô-đun đào tạo nghề`, `Tín chỉ nghề nghiệp`, `Chuẩn kỹ năng nghề quốc gia` Bậc 1–5.
- Thực tập doanh nghiệp chiếm 50%–70% thời lượng. Văn bằng: `Bằng tốt nghiệp Trung cấp`, `Bằng tốt nghiệp Cao đẳng` (kèm danh hiệu *Cử nhân thực hành* / *Kỹ sư thực hành*).

### E. Đại học (Cử nhân, Kỹ sư, Bác sĩ, Dược sĩ — TT 08/2021/TT-BGDĐT)
- **Tín chỉ học tập (`EDU005`):** Bắt buộc dùng `tín chỉ` (credit); cấm dùng `tín dụng`.
- **Đề cương chi tiết học phần (`Course Syllabus`):** CLO gắn với PLO theo thang Bloom cải tiến.
- **Thang điểm & GPA (`EDU006`):** Điểm chữ A–F; GPA hệ 4,0 viết bằng **dấu phẩy thập phân** (ví dụ: `3,65/4,00`).
- **Sản phẩm tốt nghiệp (`EDU008`):** `Khóa luận tốt nghiệp` hoặc `Đồ án tốt nghiệp` (cấm gọi "luận án cử nhân/đại học").

### F. Sau đại học — Thạc sĩ (VQF Bậc 7 — Thông tư 23/2021/TT-BGDĐT)
- Danh xưng người học: `Học viên cao học` (hoặc `Học viên`).
- Hai định hướng đào tạo (`EDU008`):
  - Định hướng nghiên cứu: `Luận văn thạc sĩ` (Master's Thesis).
  - Định hướng ứng dụng: `Đề án thạc sĩ` (Master's Capstone Project).
- Hội đồng đánh giá luận văn: 05 thành viên (Chủ tịch, Thư ký, 02 Phản biện, Ủy viên).

### G. Sau đại học — Tiến sĩ & Chức danh GS/PGS (VQF Bậc 8 — TT 18/2021 & QĐ 37/2018)
- Danh xưng: `Nghiên cứu sinh` (`NCS`), `Người hướng dẫn khoa học`.
- Sản phẩm tốt nghiệp (`EDU008`): `Tiểu luận tổng quan`, 03 `Chuyên đề tiến sĩ`, và `Luận án tiến sĩ` (Doctoral Dissertation). Tuyệt đối không dùng "khóa luận tiến sĩ", "đồ án tiến sĩ".
- **Phân biệt Học hàm (Chức danh) và Học vị (`EDU004`):**
  - **Học vị (Academic Degree):** Do trường đại học/viện cấp: `Cử nhân`, `Kỹ sư`, `Thạc sĩ`, `Tiến sĩ`.
  - **Học hàm / Chức danh (Academic Rank):** Do HĐGSNN công nhận, cơ sở GDĐH bổ nhiệm: `Giáo sư (GS)`, `Phó Giáo sư (PGS)`.
  - ❌ Cấm: `học hàm Tiến sĩ`, `học hàm Thạc sĩ`, `học vị Giáo sư`, `bằng Giáo sư`.
  - Quy cách viết tắt chuẩn: `GS.TS.`, `PGS.TS.`, `TS.`, `ThS.`.
- **Văn phong khoa học (`EDU012`):** Cấm ngôi xưng thân mật/K-12 (`cô khen con`, `thầy nhắc các em`, `bạn hãy`, `mình sẽ`) và cấm thổi phồng khoa học (`chứng minh tuyệt đối 100% không có sai số`).

---

## 3. Learning Science & EdTech Pedagogical Frameworks

### A. The Sandwich Feedback Model for Pronunciation (`EDU009`)
Khi phản hồi chấm điểm phát âm (GOP - Goodness of Pronunciation qua 6 thanh điệu tiếng Việt: *ngang, huyền, sắc, hỏi, ngã, nặng*):
- ❌ **Tiêu cực / Phi sư phạm:** `Sai rồi! Bạn đã phát âm sai thanh ngã.`
- ✅ **Mô hình Sandwich:**
  1. *Khen ngợi nỗ lực:* `"Em đã phát âm phụ âm đầu rất rõ ràng!"`
  2. *Hướng dẫn ngữ âm cụ thể:* `"Ở thanh ngã (~), em hãy thử nâng cao cao độ và ngắt nhẹ hơi ở giữa âm tiết nhé."`
  3. *Khích lệ tư duy phát triển:* `"Hãy bấm nút và thử lại lần nữa nào, em sắp làm chủ được từ này rồi!"`

### B. Adaptive Assessment (3PL IRT & ZPD Scaffolding)
- Mô hình Item Response Theory (3PL: độ phân biệt $a$, độ khó $b$, đoán mò $c$).
- Giàn giáo hỗ trợ ZPD qua 3 mức gợi ý mờ dần (Khái niệm $\rightarrow$ Chiến lược $\rightarrow$ Thao tác).

### C. Actionable Empty States (`EDU007`)
- ❌ `Trạng thái trống` / `Không có dữ liệu` *(dịch thô kỹ thuật)*
- ✅ `"Chưa có bài tập nào cần nộp hôm nay! Em có muốn ôn lại bài kiểm tra tuần trước không?"` *(gợi ý hành động)*

---

## 4. Child Data Protection & Privacy (Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 Điều 24 — `EDU010`)

Xử lý dữ liệu cá nhân của trẻ em ($\ge 7$ tuổi) bắt buộc có **sự đồng ý kép**:
1. Sự đồng ý của trẻ em.
2. Sự đồng ý được xác thực của cha mẹ hoặc người giám hộ (`phụ huynh` hoặc `người giám hộ`).

---

## 5. Validation & CLI Usage

Kiểm tra tính chuẩn xác của tài liệu giáo dục, học bạ, đề cương hoặc microcopy ứng dụng:

```bash
# Mầm non: Sổ theo dõi sức khỏe và phát triển của trẻ
python skills/vietnamese-education-copy/scripts/validate_copy.py so-theo-doi-mam-non.md --doctype preschool-report --register edu-preschool --strict

# Tiểu học: Sổ liên lạc / Nhận xét học sinh
python skills/vietnamese-education-copy/scripts/validate_copy.py so-lien-lac.md --doctype primary-report-card --register edu-parent --strict

# THCS / THPT: Học bạ điện tử
python skills/vietnamese-education-copy/scripts/validate_copy.py hoc-ba.md --doctype secondary-report-card --register edu-k12 --strict

# TVET: Đề cương mô-đun nghề nghiệp
python skills/vietnamese-education-copy/scripts/validate_copy.py tvet.md --doctype tvet-syllabus --register edu-uni --strict

# Đại học: Đề cương chi tiết học phần / Bảng điểm
python skills/vietnamese-education-copy/scripts/validate_copy.py syllabus.md --doctype higher-ed --register edu-uni --strict
python skills/vietnamese-education-copy/scripts/validate_copy.py transcript.md --doctype transcript --register edu-uni --strict

# Sau đại học: Đề cương luận văn Thạc sĩ / Luận án Tiến sĩ
python skills/vietnamese-education-copy/scripts/validate_copy.py luan-van.md --doctype master-thesis --register edu-postgrad --strict
python skills/vietnamese-education-copy/scripts/validate_copy.py luan-an.md --doctype doctoral-dissertation --register edu-postgrad --strict

# EdTech App & Thu thập dữ liệu trẻ em
python skills/vietnamese-education-copy/scripts/validate_copy.py app.md --doctype edtech-microcopy --strict
python skills/vietnamese-education-copy/scripts/validate_copy.py consent.md --doctype child-consent --strict
```

### Danh mục quy tắc kiểm định (Rule Reference)
- `EDU001`: Danh hiệu/xếp loại THCS-THPT đã bị bãi bỏ (`học sinh tiên tiến`, `xếp loại giỏi`).
- `EDU002`: Giáo viên xưng hô gọi học sinh là `bạn`.
- `EDU003`: Đánh giá tiểu học dùng `cần cải thiện` thay vì thuật ngữ luật định `cần cố gắng`.
- `EDU004`: Nhầm lẫn Học hàm / Chức danh (`Giáo sư`, `Phó Giáo sư`) và Học vị (`Tiến sĩ`, `Thạc sĩ`, `Cử nhân`).
- `EDU005`: Tín chỉ học tập viết nhầm thành `tín dụng`.
- `EDU006`: GPA dùng dấu chấm thập phân (`3.8/4.0`) thay vì dấu phẩy (`3,8/4,0`).
- `EDU007`: Trạng thái trống khô cứng trên giao diện EdTech thiếu lời kêu gọi hành động.
- `EDU008`: Sai lệch tên gọi công trình tốt nghiệp giữa các bậc học (`luận án cử nhân`, `khóa luận tiến sĩ`, v.v.).
- `EDU009`: Phản hồi âm thanh/phát âm tiêu cực vi phạm mô hình Sandwich.
- `EDU010`: Thu thập dữ liệu trẻ em thiếu sự đồng ý của phụ huynh/người giám hộ (Luật 91/2025/QH15 Điều 24; NĐ 13/2023 hết hiệu lực từ 01/01/2026).
- `EDU011`: Chấm điểm số hoặc xếp loại học lực K-12 đối với trẻ mầm non (VBHN 01/VBHN-BGDĐT).
- `EDU012`: Xưng hô thân mật/K-12 hoặc thổi phồng khẳng định khoa học trong nghiên cứu Sau đại học.

---

## 6. Reference Guides & Asset Templates

- [references/preschool-to-postgrad-continuum.md](references/preschool-to-postgrad-continuum.md) — Cẩm nang toàn diện 7 bậc học (Mầm non $\rightarrow$ Tiến sĩ & GS/PGS).
- [references/glossary.md](references/glossary.md) — 100+ thuật ngữ chuẩn mực giáo dục, sư phạm, và quản lý học thuật.
- [references/banned-phrases.md](references/banned-phrases.md) — Bảng từ vựng dịch thô, calque, và biệt ngữ quảng cáo tuyển sinh trái luật.
- [references/grading-terminology.md](references/grading-terminology.md) — Chi tiết các thông tư đánh giá TT 22/2021, TT 27/2020, TT 08/2021.
- [references/doc-registers.md](references/doc-registers.md) — Ma trận xưng hô và phong cách giao tiếp sư phạm.
- [references/edtech-pedagogy.md](references/edtech-pedagogy.md) — Khoa học học tập: 3PL IRT, ZPD, GOP 6 thanh điệu, SDT và bảo vệ dữ liệu trẻ em.
- [references/qa-checklist.md](references/qa-checklist.md) — Danh sách kiểm tra chất lượng trước khi ban hành nội dung giáo dục.
- [assets/phieu-nhan-xet-hoc-ba.md.template](assets/phieu-nhan-xet-hoc-ba.md.template) — Mẫu học bạ điện tử THCS/THPT chuẩn Thông tư 22/2021.
- [assets/so-theo-doi-mam-non.md.template](assets/so-theo-doi-mam-non.md.template) — Mẫu sổ theo dõi phát triển mầm non chuẩn VBHN 01/VBHN-BGDĐT.
- [assets/de-cuong-luan-an-tien-si.md.template](assets/de-cuong-luan-an-tien-si.md.template) — Mẫu đề cương luận án tiến sĩ chuẩn Thông tư 18/2021.
