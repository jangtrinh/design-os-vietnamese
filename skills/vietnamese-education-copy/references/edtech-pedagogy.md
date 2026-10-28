<!-- vlc-disable: all -->

# Learning Science, Cognitive Psychology, & EdTech Architecture (`design-os-vietnamese`)

This guide bridges cognitive learning science and native Vietnamese EdTech copy design. It provides concrete specifications for Spaced Repetition systems, Item Response Theory (IRT) adaptive assessment, Zone of Proximal Development (ZPD) scaffolding, pediatric acoustic pronunciation scoring (GOP across Vietnamese 6 tones), Self-Determination Theory (SDT), and statutory child data protection under **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 Điều 24**.

---

## 1. Spaced Repetition & Habit-Loop Microcopy

Spaced Repetition Systems (SRS) model the Ebbinghaus forgetting curve through adaptive intervals (Leitner 5-box system, SuperMemo SM-2, and modern Free Spaced Repetition Scheduler - FSRS).

### A. Non-Shaming Retention Notifications
Push notifications and reminder nudges must inspire intrinsic motivation rather than induce guilt or anxiety:
- ❌ **Shame / Guilt Nudge:** `Bạn đã bỏ bê việc học 3 ngày rồi! Chuỗi học tập của bạn sắp bị mất!`
- ✅ **Constructive Growth Nudge:** `Hôm nay em có 5 từ vựng cần ôn lại để đưa vào trí nhớ dài hạn. Cùng dành 3 phút hoàn thành để giữ vững chuỗi ngày học tập nhé!`

### B. Memory Interval State Labels
| SRS Memory Stage | Recommended Vietnamese UI Label | Description |
|---|---|---|
| New Card / First Exposure | `Từ mới` | Initial cognitive encoding |
| Learning / Short-term | `Đang ghi nhớ` | Review interval: 10m $\rightarrow$ 1d |
| Review / Intermediate | `Ôn tập định kỳ` | Review interval: 3d $\rightarrow$ 7d $\rightarrow$ 14d |
| Mastered / Long-term | `Đã thông hiểu` | Consolidation into semantic long-term memory |

---

## 2. Adaptive Assessment & 3PL Item Response Theory (IRT)

Modern adaptive testing estimates a learner's latent ability ($\theta$) dynamically. In the 3-Parameter Logistic (3PL) model:

$$P_i(\theta) = c_i + \frac{1 - c_i}{1 + e^{-a_i(\theta - b_i)}}$$

Where:
- $b_i$: Item difficulty (Độ khó của câu hỏi).
- $a_i$: Item discrimination (Độ phân biệt của câu hỏi).
- $c_i$: Pseudo-guessing parameter (Xác suất đoán mò may rủi).

### UI Framing of Dynamic Difficulty Scaling
When an adaptive algorithm increases problem difficulty after a winning streak:
- Never say: `"Hệ thống đang tăng độ khó vì bạn làm quá nhanh."`
- Frame as an empowering milestone:
  `"Tuyệt vời! Em đã thành thạo mức độ cơ bản. Thầy/Cô có một thử thách nâng cao hơn để em thử sức đây!"`
When an algorithm lowers difficulty after consecutive errors:
- Frame as supportive consolidation:
  `"Hãy cùng ôn lại một ví dụ tương tự để nắm chắc phương pháp giải trước khi tiếp tục nhé!"`

---

## 3. ZPD Scaffolding & 3-Tier Fading Hints

Vygotsky's Zone of Proximal Development (ZPD) represents the cognitive space between what a student can do unassisted and what they can achieve with expert guidance. EdTech interfaces scaffold assistance through 3 fading tiers:

```
[Tier 1: Nhắc nhở quy tắc] ──> [Tier 2: Gợi ý chiến lược] ──> [Tier 3: Hướng dẫn chi tiết]
```

1. **Tier 1 — Rule Reminder (Nhắc nhở quy tắc):**
   - Directs attention to the underlying formula, theorem, or grammar rule without giving away the answer.
   - Example: `"Gợi ý 1: Trong câu điều kiện loại 2, mệnh đề If sử dụng thì quá khứ đơn. Em hãy kiểm tra lại động từ nhé."`
2. **Tier 2 — Strategic Clue (Gợi ý chiến lược):**
   - Eliminates distractors or breaks the problem into sub-goals.
   - Example: `"Gợi ý 2: Phương án A và C sử dụng thì hiện tại nên không phù hợp. Em hãy chọn giữa B và D."`
3. **Tier 3 — Step-by-Step Resolution (Hướng dẫn từng bước):**
   - Shows the full worked solution with an immediate follow-up practice problem.
   - Example: `"Lời giải chi tiết: Đáp án đúng là B vì động từ 'were' phù hợp với mệnh đề If loại 2. Bây giờ em hãy thử áp dụng với câu tương tự này nhé!"`

---

## 4. Pediatric ASR & GOP Pronunciation Feedback (The 6 Vietnamese Tones)

Evaluating spoken language through Goodness of Pronunciation (GOP) acoustic models requires sensitive pedagogical framing. In Vietnamese, word meaning depends entirely on 6 phonemic tones:

| Vietnamese Tone | Diacritic | Pitch Contour & Acoustic Description | Common Learner Defect |
|---|---|---|---|
| **Thanh Ngang** (Không dấu) | `a` | Mid-level, flat pitch (33) | Dropping pitch or adding glottal stop |
| **Thanh Huyền** | `à` | Low falling pitch (21) | Falling too steeply into heavy tone |
| **Thanh Sắc** | `á` | High rising pitch (35) | Insufficient rise in pitch |
| **Thanh Hỏi** | `ả` | Mid-low falling then rising (312/324) | Confusing with falling tone; omitting contour rise |
| **Thanh Ngã** | `ã` | High rising with creaky voice / glottal interruption | Failing to break vocal tract airflow |
| **Thanh Nặng** | `ạ` | Low abrupt drop with glottal closure (21?) | Prolonging tone instead of abrupt stop |

### The Compliant Sandwich Feedback Model (`EDU009`)
Acoustic algorithms must never output blunt failure tags (`Sai rồi`, `Bạn nói sai`). Apply the 3-layer Sandwich structure:
1. **Layer 1 (Praise Effort & Success):**
   `"Em đã phát âm phụ âm đầu và âm đệm rất chuẩn xác!"`
2. **Layer 2 (Targeted Acoustic/Tone Adjustment):**
   `"Ở từ này, em cần chú ý thanh Ngã (~). Hãy thử ngân cao giọng hơn một chút và ngắt hơi nhẹ ở giữa âm tiết nhé."`
3. **Layer 3 (Growth Mindset Encouragement):**
   `"Bấm nút micro và nói lại lần nữa nào, em sắp phát âm hoàn hảo rồi!"`

---

## 5. Self-Determination Theory (SDT) & Anti-Overjustification

Under Deci & Ryan's Self-Determination Theory, sustained learning depends on meeting three psychological needs:
- **Autonomy (Quyền tự chủ):** The feeling of being in control of one's learning path.
- **Competence (Cảm giác năng lực):** The feeling of mastery and effective problem resolution.
- **Relatedness (Sự kết nối):** Feeling connected to teachers, peers, and family.

### Preventing the Overjustification Effect
Overjustification occurs when an extrinsic reward (XP, badges, digital gems) replaces and diminishes intrinsic curiosity. When a child masters a complex mathematical concept:
- ❌ **Shallow Extrinsic Slop:** `"Chúc mừng bạn nhận được 100 kim cương vì đã làm xong bài!"`
- ✅ **Intrinsic Competence Feedback:** `"Chúc mừng em đã chinh phục thành công bài toán phân số nâng cao! Em đã vận dụng rất tốt phương pháp quy đồng mẫu số."`

---

## 6. Child Data Protection & Double Consent (Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 Điều 24 — `EDU010`)

Vietnam's Personal Data Protection Decree imposes strict legal obligations on EdTech platforms handling minor data:

### Double Consent Requirement
1. **Children from 7 to under 16 years old:**
   - Platform must obtain verified consent from **both the child AND the child's parent or legal guardian** (`phụ huynh` hoặc `người giám hộ`).
2. **Children under 7 years old:**
   - Platform must obtain verified consent from the parent or legal guardian.

### Statutory UX Onboarding Requirements (`EDU010`)
Any registration, profile setup, microphone audio access, or behavioral telemetry collection screen must explicitly include:
- A parental verification gate: `"Vui lòng có sự xác nhận của Quý phụ huynh hoặc người giám hộ trước khi bắt đầu."`
- Clear purpose statement: Data is strictly used for personalized learning analytics and never shared for behavioral advertising.
- Automatic deletion policy for pediatric voice recordings after GOP score computation.
