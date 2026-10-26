<!-- vlc-disable: TONE001, DIA001 -->

# Register Matrix — Vietnamese Pragmatics & Audience Address (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. Vietnamese has **no neutral "you."** English collapses every social relationship into one pronoun; Vietnamese encodes hierarchy, warmth, age, institutional authority, and channel context directly into the pronoun pair (**xưng – hô**). Picking the wrong pronoun does not read as slightly awkward—it reads as a completely different brand or as unedited machine translation.

This file is the canonical source of truth. `validate_copy.py` parses the `<!-- machine-readable: registers -->` table below at runtime.

## 1. Machine-Readable Register Profiles

- **Expects** — primary reader address (`hô`) for the register. An empty cell means the register is **impersonal** (zero direct second-person address).
- **Forbids** — comma-separated pronouns that trigger `PRO002` when found in a document declared with `--register <name>`.

<!-- machine-readable: registers -->

| Register | Expects | Forbids | Primary Surfaces & Domain Context |
|---|---|---|---|
| `ux-microcopy` | `bạn` | `quý khách`, `quý vị`, `mày`, `cậu` | DESIGN:OS product UI, SaaS dashboards, mobile apps, settings, modals, empty/error states (omit pronoun on buttons/labels; use `bạn` only when ownership or consequence needs disambiguation) |
| `saas` | `bạn` | `quý khách`, `quý vị` | SaaS landing pages, developer tools, consumer tech, e-commerce, digital creator products |
| `re` | `quý khách` | `bạn`, `mình`, `cả nhà` | Real estate (bất động sản), luxury retail, aviation, 5-star hospitality, private banking |
| `formal` | `quý vị` | `bạn`, `mình`, `cả nhà` | Institutional announcements, state events, keynotes, formal public broadcasts |
| `consult` | `anh/chị` | `bạn`, `quý vị` | Consultative sales, brokerage, high-ticket B2C services, 1:1 CRM follow-ups |
| `b2b` | `anh/chị` | `bạn`, `quý vị`, `cả nhà` | B2B cold outreach, enterprise proposals, quotations (`báo giá`), dunning notices |
| `zns` | `quý khách` | `bạn`, `mình`, `cả nhà` | Zalo OA ZNS/ZBS transactional & service notifications (channel-enforced formality floor) |
| `press` | `quý vị` | `bạn`, `mình`, `bọn mình`, `cả nhà` | Press releases (`thông cáo báo chí`), corporate investor relations, public statements |
| `livestream` | `cả nhà` | `quý vị`, `quý khách` | TikTok Shop / Shopee Live spoken scripts, social commerce flash-sale callouts |
| `eng-impersonal` | | `bạn`, `quý khách`, `quý vị`, `anh/chị`, `em`, `con` | RFCs, ADRs, architecture specs, postmortems, runbooks, system design docs |
| `eng-readme` | `bạn` | `quý khách`, `quý vị` | Open-source READMEs, SDK quickstarts, developer tutorials, API guides |
| `finance-formal` | `quý khách` | `bạn`, `mình`, `cả nhà` | Financial statements (`BCTC`), tax filings, e-invoices, credit/loan disclosures, insurance contracts |
| `edu-k12` | `em` | `bạn`, `quý khách`, `quý vị` | Secondary/High school (THCS/THPT) teacher-to-student remarks, `học bạ`, AI tutor for grades 6–12 |
| `edu-k12-primary` | `con` | `bạn`, `quý khách`, `quý vị`, `em` | Primary school (Tiểu học, grades 1–5) teacher-to-student remarks, pastoral feedback |
| `edu-preschool` | `con` | `bạn`, `quý khách`, `quý vị`, `em` | Early childhood / Preschool (Mầm non: Nhà trẻ 3–36 tháng & Mẫu giáo 3–6 tuổi) teacher-to-child interactions & developmental observation logs (`cô` – `con`) |
| `edu-parent` | `quý phụ huynh` | `bạn`, `mình`, `quý khách`, `em`, `con` | School-to-parent notices (`sổ liên lạc điện tử`, `sổ theo dõi trẻ mầm non`), tuition notices, parental learning analytics |
| `edu-uni` | | `bạn`, `con`, `em`, `quý khách` | Undergraduate university syllabi (`đề cương học phần`), transcripts, academic regulations (third-person `sinh viên`) |
| `edu-postgrad` | | `bạn`, `con`, `em`, `quý khách`, `mình`, `cả nhà` | Postgraduate Master's (`Thạc sĩ` TT 23/2021) & Doctoral (`Tiến sĩ` TT 18/2021) dissertations, defense councils, scholarly journals (third-person `học viên`, `nghiên cứu sinh`, `tác giả`) |
| `gov-admin` | | `bạn`, `mình`, `em`, `con`, `cả nhà` | Administrative & statutory documents under Nghị định 30/2020/NĐ-CP (`công văn`, `tờ trình`, `quyết định`) |
| `healthcare` | `quý khách` | `bạn`, `mình`, `cả nhà` | Hospital/clinic patient communications, appointment reminders, discharge instructions (`quý khách`) |
| `healthcare-clinical` | | `bạn`, `mình`, `cả nhà`, `cậu`, `mày` | Electronic Medical Records (EMR TT 32/2023/TT-BYT), prescriptions (`đơn thuốc`), lab reports (impersonal/third-person `người bệnh`, `bác sĩ`) |
| `legal-contract` | | `bạn`, `mình`, `cả nhà`, `em`, `con`, `cậu` | Civil/commercial/labor contracts, Terms of Service, PDPD Privacy Policies, DPAs (third-person `Bên A`, `Bên B`, `Khách hàng`, `Người lao động`) |
| `hospitality-luxury` | `quý khách` | `bạn`, `mình`, `cả nhà`, `cậu`, `mày` | 4–5 star hotels, resorts, airlines, cruise lines, fine dining F&B, concierge communications |
| `hr-candidate` | `anh/chị` | `mày`, `cậu`, `con`, `cả nhà` | Job descriptions (JD), offer letters (`thư mời nhận việc`), interview invitations, formal HR candidate communications |

---

## 2. Self-Reference Rules (`Xưng`)

1. **`chúng tôi` (Exclusive "We" — Organization/Brand):**
   - Standard self-reference across corporate landing pages, B2B proposals, terms of service, press releases, and finance disclosures.
2. **`chúng ta` (Inclusive "We" — Writer + Reader together):**
   - **High-frequency LLM error:** English `we` maps to both `chúng tôi` and `chúng ta`. LLMs routinely write *"Chúng ta cung cấp giải pháp..."* on a company page, which claims the customer works at the company.
   - Reserve `chúng ta` strictly for community manifestos, collaborative tutorials (*"Trong phần này, chúng ta sẽ cấu hình..."*), or internal all-hands memos.
3. **Zero-Pronoun Controls in UI (`ux-microcopy`):**
   - Buttons, menu items, tabs, and form labels **omit the speaker and listener entirely**: write `Đổi mật khẩu`, `Lưu thay đổi`, `Tạo khóa API`, never `Bạn hãy đổi mật khẩu của bạn`.
   - Use `bạn` in UI microcopy only when clarifying ownership or consequence (`Xóa không gian làm việc của bạn?`).
4. **Kinship & Seniority Self-Reference (`em` vs `tôi` vs `mình`):**
   - **B2B Sales (`b2b` / `consult`):** When addressing an older or senior buyer as `anh`/`chị`, a younger account executive naturally refers to themselves as `em` (*"Em gửi anh báo giá..."*). When seniority is equal or unknown in formal executive correspondence, use `tôi` or the company name.
   - **Engineering Peer Review:** In PR descriptions, code reviews, and internal Slack/Teams threads, Vietnamese engineers use `mình` + `bạn` or `anh/chị` + `em`. Never use `mình` in RFCs (`eng-impersonal`) or customer-facing enterprise docs.
   - **Education (`thầy` / `cô`):** A teacher or K-12 AI tutor refers to itself as `thầy` or `cô` (never `tôi` or `mình`) when addressing `em` or `con`.

---

## 3. Document-Level Consistency & Channel Overrides

- **One Register Per Document (`PRO001`):**
  Mixing formal pronouns (`quý khách`, `quý vị`) with casual pronouns (`bạn`, `mình`) in the same page or screen is a critical defect. If the Hero section addresses `Quý khách`, the FAQ and Footer CTA must not drop to `bạn`.
- **The Channel Override Law:**
  A SaaS or e-commerce brand whose web/app voice is `bạn` **must switch to `Quý khách`** inside a Zalo ZNS transactional template (`--register zns`) or an e-invoice (`--register finance-formal`). In Vietnam, the delivery channel and legal instrument override brand casualness.

---

## 4. Third-Person Nouns vs Direct Address

`khách hàng`, `người dùng`, `nhà đầu tư`, `sinh viên`, `học sinh`, `bệnh nhân`, and `cá nhân/tổ chức` are **third-person nouns**, not vocative pronouns.
- **Correct (Policy / Terms / University Regulation):** *"Người dùng có trách nhiệm bảo mật khóa cá nhân."* / *"Sinh viên đăng ký học phần trước ngày 15/08."*
- **Wrong (Direct UI Instruction):** *"Khách hàng hãy nhấn vào nút bên dưới."* → Write: *"Quý khách vui lòng nhấn vào nút bên dưới"* (`re`) or *"Nhấn vào nút bên dưới"* (`ux-microcopy`).

---

## 5. Compound-Word Disambiguation (Preventing False Positives)

The word `bạn` and the Sino-Vietnamese morpheme `quý` appear inside many compound nouns and adjectives where they are **not** pronouns:
- **Non-pronoun compounds with `bạn`:** `bạn bè`, `bạn đọc`, `bạn hàng`, `bạn đời`, `bạn học`, `bạn đồng hành`, `kết bạn`, `tình bạn`, `nhóm bạn`, `bạn hữu`.
- **Non-pronoun compounds with `quý`:** `quý giá`, `quý hiếm`, `quý báu`, `quý trọng`, `quý mến`, `Quý I`, `Quý II`, `Quý III`, `Quý IV`, `quý 1`, `quý 2`, `quý 3`, `quý 4`, `quý đầu năm`, `quý cuối năm`.

`validate_copy.py` explicitly guards these compound forms so `PRO001` and `PRO002` never emit false positives on legitimate Vietnamese vocabulary.
