<!-- vlc-disable: all -->

# Educational Register Matrix & Pragmatics (`design-os-vietnamese`)

In Vietnamese society, educational interactions reflect revered cultural principles: *Tôn sư trọng đạo* (respecting teachers and honoring morality) and *Tiên học lễ, hậu học văn* (learning etiquette before academic knowledge). Picking the wrong pronoun or register in an educational app, report card, or portal does not merely look unnatural—it breaks cultural decorum and undermines parental trust.

---

## 1. Register Profiles & Boundaries

### A. Secondary & High School (`edu-k12`)
- **Primary Audience:** Students aged 11–18 (Lớp 6–12, THCS & THPT).
- **Teacher Address (`Xưng – Hô`):** `thầy/cô` – `em`.
- **Statutory & Pragmatic Rules:**
  - The teacher or AI tutor refers to itself as `thầy` or `cô`, never `tôi` or `mình`.
  - The student is addressed as `em`, never `bạn`, `cậu`, or `mày`.
  - In student peer interactions (forums, collaborative homework), students use `mình` – `bạn` or `cậu` – `tớ`.
- **Sample Teacher Report-Card Remark:**
  `"Em có tinh thần tự giác cao trong học tập, tích cực phát biểu xây dựng bài. Cần chú ý rèn thêm kỹ năng làm việc nhóm để đạt kết quả xuất sắc hơn trong học kỳ II."`

### B. Primary School (`edu-k12-primary`)
- **Primary Audience:** Young pupils aged 6–10 (Lớp 1–5, Tiểu học).
- **Teacher Address (`Xưng – Hô`):** `thầy/cô` – `con`.
- **Statutory & Pragmatic Rules:**
  - Vietnamese primary school pedagogy adopts a family-like, pastoral relationship. Teachers address young pupils as `con` (or `bạn nhỏ` in playful EdTech mascot interfaces).
  - Addressing a 7-year-old pupil as `em` feels overly formal and distant; addressing them as `bạn` sounds like an American corporate machine translation.
- **Sample Teacher Sổ Liên Lạc Remark:**
  `"Con chăm ngoan, tiếp thu bài nhanh và biết giúp đỡ bạn bè trong lớp. Cô khen ngợi sự tiến bộ vượt bậc của con ở môn Toán tuần này."`

### C. School-to-Parent Communication (`edu-parent`)
- **Primary Audience:** Parents and legal guardians (`phụ huynh học sinh`).
- **School Address (`Xưng – Hô`):** `Nhà trường / Giáo viên chủ nhiệm` – `Quý phụ huynh`.
- **Statutory & Pragmatic Rules:**
  - The universal, respectful vocative is **`Kính gửi Quý phụ huynh`**.
  - Never address parents as `Quý khách` (commercial retail register) or `các cha mẹ` (literal translationese).
  - When a teacher speaks 1:1 with an individual parent in private consultation, they use kinship terms based on age seniority: `Em chào anh/chị` (if teacher is younger) or `Chào anh/chị` (if peer). In automated systems and collective broadcasts, strictly use `Quý phụ huynh`.
- **Sample Parent Broadcast Notice:**
  `"Kính gửi Quý phụ huynh, nhà trường xin thông báo lịch họp phụ huynh cuối học kỳ I vào lúc 08:00 sáng Chủ nhật, ngày 10/01/2026. Kính mong Quý phụ huynh sắp xếp thời gian tham dự đầy đủ."`

### D. University & Higher Education (`edu-uni`)
- **Primary Audience:** Undergraduate and postgraduate adult students (`sinh viên`, `học viên`).
- **Institutional Address (`Xưng – Hô`):** *(Impersonal third person)*.
- **Statutory & Pragmatic Rules:**
  - University syllabi, transcripts, academic policies, and course registration systems do not use direct second-person address (`bạn`, `em`, `quý khách`).
  - Refer to the learner in the third person as `sinh viên` (undergraduate) or `học viên cao học` (graduate student).
  - Lecturers use `giảng viên`, never `giáo viên`.
- **Sample University Course Syllabus Notice:**
  `"Sinh viên vắng quá 20% tổng số tiết học phần sẽ không đủ điều kiện dự thi kết thúc học phần. Điểm đánh giá quá trình chiếm trọng số 40% trong điểm tổng kết."`

---

## 2. EdTech AI Tutor Persona Guidelines

Modern EdTech applications (Duolingo-style gamified learning, AI speaking tutors, homework assistants) must adopt calibrated pedagogical personas:

### A. The Inspiring Mentor Persona (AI Coach)
- **Voice Attributes:** Encouraging, patient, constructive, celebrating effort and resilience over raw intellect (Growth Mindset).
- **Tone Rules:**
  - When a student makes a mistake, avoid punitive or dismissive words (`Sai rồi`, `Không đúng`, `Kém`).
  - Use scaffolding encouragement: `"Gần đúng rồi!", "Em hãy xem lại gợi ý ở bước 2 nhé!", "Một thử thách rất thú vị, chúng ta cùng giải quyết nào!"`
- **Avoid Overjustification Effect:**
  - Transition learners from extrinsic XP/points to intrinsic joy of mastery: praise their specific strategy rather than giving shallow rewards.

### B. Machine Address Pitfalls to Avoid in Educational UI

| English Source | ❌ Machine Translation Slip | ✅ Authentic Educational UI | Context |
|---|---|---|---|
| "You earned 50 XP!" | `Bạn đã kiếm được 50 XP!` | `Em nhận được 50 điểm kinh nghiệm!` | K-12 Student UI |
| "Your progress" | `Sự tiến bộ của bạn` | `Tiến độ học tập của em` | Dashboard tab |
| "Submit homework" | `Đệ trình bài tập về nhà của bạn` | `Nộp bài tập` | Action button |
| "Dear parents" | `Thân gửi các cha mẹ` | `Kính gửi Quý phụ huynh` | Zalo notification |
| "Empty state" | `Trạng thái trống` | `Chưa có bài tập nào hôm nay` | List container |
| "Good job!" | `Công việc tốt!` | `Em làm tốt lắm!` | Achievement toast |
| "Try again" | `Hãy thử lại lần nữa bạn nhé` | `Thử lại nào!` | Quiz action |

---

## 3. Kinship Address Nuances & Classroom Speech Etiquette

Vietnamese classroom discourse is deeply interpersonal. Teachers and students adhere to established conventions:

### A. The Polite Particle "Dạ" & "Thưa"
- When a student responds to a teacher, polite discourse markers are expected:
  - `"Dạ thưa thầy/cô, em đã hiểu bài rồi ạ."`
  - In educational software prompts designed for speaking practice, teaching students to open responses with `"Dạ"` or `"Dạ thưa cô"` models authentic cultural etiquette.

### B. Parental Consultation & Zalo Group Communication
- Class Zalo groups (`Nhóm Zalo lớp`) are the primary school-to-home bridge in modern Vietnam.
- Teachers managing class groups must balance warmth and statutory authority:
  - Opening: `"Kính gửi Quý phụ huynh học sinh lớp [X]"`
  - Body: Specific updates regarding schedule, uniform, health checks, or tuition notices.
  - Closing: `"Trân trọng cảm ơn sự phối hợp chặt chẽ của Quý phụ huynh."`
  - Self-reference: `"Giáo viên chủ nhiệm: [Họ và tên cô giáo]"`

### C. Addressing Multi-Age Learning Communities
- In lifelong learning platforms, adult education, or community coding bootcamps:
  - When the learners are working adults, shift from `thầy/cô – em` to consultative professional address: `Giảng viên / Huấn luyện viên` – `anh/chị` (`consult` or `b2b` register), or use friendly inclusive `mình – bạn` in peer learning circles.

---

## 4. EdTech In-App Notification & Microcopy Taxonomy

System notifications in Vietnamese educational platforms must adhere to calibrated emotional registers:

| Notification Type | Trigger Event | Recommended Vietnamese Microcopy | Voice Calibration |
|---|---|---|---|
| **Homework Due Reminder** | 2 hours before deadline | `"Bài tập môn Toán sắp đến hạn nộp. Em hãy kiểm tra lại và nộp bài trước 21:00 nhé!"` | Gentle accountability |
| **Streak Milestone** | 7-day study streak | `"Chúc mừng em đã hoàn thành chuỗi 7 ngày học tập liên tục! Tiếp tục phát huy nhé!"` | Competence praise |
| **New Assignment Posted** | Teacher releases quiz | `"Thầy/Cô vừa giao bài luyện tập mới: 'Hình học không gian'. Hãy bắt đầu làm bài nào!"` | Actionable call to action |
| **System Maintenance** | LMS planned downtime | `"Hệ thống sẽ bảo trì từ 23:00 đến 02:00 sáng mai. Chúc các em nghỉ ngơi thật tốt!"` | Consideration & care |
| **Grade Published** | Exam scores released | `"Điểm kiểm tra giữa kỳ môn Ngữ văn đã có. Em hãy vào mục Kết quả để xem chi tiết nhé."` | Neutral, respectful update |
