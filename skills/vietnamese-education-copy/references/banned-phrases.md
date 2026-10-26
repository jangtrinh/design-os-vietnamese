<!-- vlc-disable: all -->

# Banned Phrases & Educational Calques (`design-os-vietnamese`)

This document lists prohibited translationese, harsh unpedagogical feedback phrases, and regulated school admissions superlatives.

---

## 1. Regulated Superlatives in Education & Admissions (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, schools, universities, language centers, and EdTech platforms cannot claim to be "best", "number one", or "only" without licensed verification.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|cao\|nhanh\|uy\s+tín\|lớn\|hiệu\s+quả\|chuẩn)\s+nhất` | "best school / highest pass rate / most reputable" | Standard violation in admissions marketing |
| `duy\s+nhất` | "the only" | Explicitly banned by statute without proof |
| `số\s*(?:một\|1)\b` | "number one" | Specifically prohibited claim |
| `hàng\s+đầu` | "leading" | Prohibited comparative boast |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |

**Compliant Rewrite Principle:**
State empirical, verified metrics instead of empty boast words:
- ❌ `Trung tâm Anh ngữ luyện thi IELTS tốt nhất Việt Nam`
- ✅ `Trung tâm đào tạo hơn 5.000 học viên đạt band điểm 7.0+ từ năm 2020 đến nay`

---

## 2. Educational Translationese & Machine-Translation Tells

The following phrases are unidiomatic, calqued expressions that destroy pedagogical warmth and credibility:

<!-- machine-readable: calques -->

| ❌ Calque / Bad Phrasing | ✅ Idiomatic Pedagogical Phrasing | Why |
|---|---|---|
| `thân gửi các cha mẹ` | `Kính gửi Quý phụ huynh` | Cold literal translation of 'Dear parents' |
| `giáo viên phòng nhà` | `giáo viên chủ nhiệm` | Literal calque of 'homeroom teacher' |
| `thẻ báo cáo` | `học bạ` | Report card is 'học bạ' in Vietnamese |
| `sách liên lạc` | `sổ liên lạc` | Contact notebook is 'sổ liên lạc' |
| `bảng táp-lô` | `bảng tổng quan` | Technical jargon out of place in school apps |
| `theo dấu sự tiến bộ` | `theo dõi tiến độ học tập` | Word-for-word calque of 'track progress' |
| `học tập làm chủ` | `học tập thông hiểu` | Clumsy rendering of 'Mastery Learning' |
| `đánh giá định hình` | `đánh giá quá trình` | Inaccurate rendering of 'Formative Assessment' |
| `giàn giáo học tập` | `hỗ trợ từng bước` | Unidiomatic technical translation of 'Scaffolding' |
| `vệt học tập` | `chuỗi ngày học tập` | Literal calque of 'Learning Streak' |
| `bảng lãnh đạo` | `bảng xếp hạng` | Absurd literal translation of 'Leaderboard' |
| `đệ trình bài tập` | `nộp bài` | Over-formal translation of 'Submit assignment' |
| `tín dụng học tập` | `tín chỉ` | 'Tín dụng' is financial debt/credit |
| `đậu và rớt` | `đạt và chưa đạt` | Non-statutory casual slang in formal contexts |
| `học bạ điện thoại` | `sổ liên lạc điện tử` | Incorrect compound noun |
| `chuyên gia dạy học` | `nhà giáo dục / giảng viên chuyên môn` | Artificial phrasing |

---

## 3. Harsh & Demotivating Phrasing to Avoid in Pedagogical Copy

Words that induce anxiety, trigger shame, or stifle a Growth Mindset in children and adult learners:

| ❌ Demotivating / Blunt Phrasing | ✅ Constructive Growth Mindset Formulation |
|---|---|
| `Sai rồi!` | `Chưa chính xác, em hãy thử lại một lần nữa nhé!` |
| `Bạn đã phát âm sai hoàn toàn.` | `Âm này hơi khó một chút, em chú ý lắng nghe lại ngữ điệu mẫu nhé.` |
| `Điểm của bạn quá thấp.` | `Em đã hoàn thành bài tập, hãy cùng ôn lại một số câu để nâng cao điểm số nhé!` |
| `Bạn không chú ý nghe giảng.` | `Em hãy tập trung hơn trong phần này để nắm chắc kiến thức trọng tâm nhé.` |
| `Học sinh lười biếng.` | `Em cần chủ động và phân bổ thời gian tự học hợp lý hơn.` |
