<!-- vlc-disable: all -->

# Technical QA Checklist & Peer Review Rubric (`vietnamese-tech-writing`)

Technical documentation, developer quickstarts, and product UI strings require systematic quality gates. A defect in technical copy can cause developer integration failures, erroneous on-call incident responses, or silent data corruption in user research.

Every technical document, API reference, or localized UI catalog must score at least **4 out of 5** across all seven criteria before code merge.

---

## 1. Register & Impersonal Discipline (`ENG003`)

- [ ] **RFCs, ADRs, Specs & Postmortems:** Zero second-person address (`bạn`, `quý khách`, `anh/chị`). Sentences describe system states, component interactions, and requirements objectively (*"Hệ thống sẽ..."*, *"Cần cấu hình..."*).
- [ ] **Operational Runbooks (`ENG007`):** Instructions use bare imperatives (*"Chạy migration"*, *"Khởi động lại service"*); zero hedged language (*"bạn nên"*, *"bạn có thể"*, *"bạn hãy"*).
- [ ] **Developer Guides & READMEs:** Direct, approachable `bạn` address. Zero commercial or servile language (*"quý khách"*).
- [ ] **Customer Status Pages:** Formal, respectful `Quý khách` address for service downtime and maintenance notices.
- [ ] **PR Descriptions & Code Reviews:** Peer-level tone (`mình` / `bạn`); respectful, technically precise, focusing on diff logic.

---

## 2. Code-Switching & Technical Terminology (`CAL001`)

- [ ] **Git & Version Control Primitives:** `commit`, `merge`, `rebase`, `pull request`, `cherry-pick`, `branch` stay in English. Never `cam kết`, `hợp nhất chi nhánh`, or `yêu cầu kéo`.
- [ ] **Environment Names:** `production`, `staging`, `dev` stay in English. Never `sản xuất` or `dàn dựng`.
- [ ] **Cloud & Architecture Concepts:** `middleware`, `webhook`, `endpoint`, `pipeline`, `cluster`, `message queue` remain in English in engineering prose.
- [ ] **User-Facing Nouns:** Appropriately translated in product UI (`tài khoản`, `mật khẩu`, `thông báo`, `báo cáo`, `cài đặt`).
- [ ] **Identifiers & Code Literals:** Variables, functions, and configuration keys remain ASCII (`user_id`, `apiKey`, `MAX_RETRIES`).

---

## 3. Error Microcopy & User Blame (`ENG008`)

- [ ] **Non-Blaming Voice:** Zero direct accusations (*"Bạn đã nhập sai"*, *"Lỗi của bạn"*). The error describes the input requirement or system condition objectively (*"Email không đúng định dạng. Vui lòng kiểm tra lại."*).
- [ ] **Actionable Remediation:** Every error message states both what occurred and the next observable step to resolve it.
- [ ] **Zero Technical Jargon Leakage:** System stack traces, raw HTTP status codes, and database error strings are suppressed in user-facing UI.
- [ ] **Toast & Banner Brevity:** Mobile error banners fit on two lines maximum without pushing primary action controls offscreen.

---

## 4. App Store & Platform Character Limits (`PROD003`)

- [ ] **Apple App Store Name:** Maximum 30 NFC characters.
- [ ] **Apple App Store Subtitle:** Maximum 30 NFC characters.
- [ ] **Apple App Store Promotional Text:** Maximum 170 NFC characters.
- [ ] **Google Play Short Description:** Maximum 80 NFC characters.
- [ ] **Google Play Full Description:** Maximum 4.000 NFC characters.
- [ ] **Mobile Push Notifications:** Body text under 90 characters to prevent lock-screen truncation.
- [ ] **Pre-release Verification:** Character count evaluated strictly after precomposed NFC normalization.

---

## 5. Survey & Research Psychometrics (`PROD002`)

- [ ] **Zero Agree/Disagree Scales:** Questionnaires avoid `Bạn có đồng ý...` with `Đồng ý / Không đồng ý` to prevent acquiescence bias.
- [ ] **Item-Specific Construct Scales:** Questions measure the underlying attribute directly (e.g. *Rất khó → Rất dễ*).
- [ ] **NPS Preservation:** The 0–10 scale is preserved in full without collapsing into binary Yes/No or 1–5.
- [ ] **Labeled Scale Points:** Every scale option is distinctly labeled to prevent subjective numeric interpretation drift.
- [ ] **Zero Double-Barreled Questions:** Avoid compound evaluation queries (*"Ứng dụng có nhanh và tiện lợi không?"*).

---

## 6. Locale, ICU & Encoding Hazards

- [ ] **ASCII-Only Identifiers (`ENG001`):** Commit subjects, branch names, code variables, and JSON i18n resource keys contain strictly ASCII characters (no diacritics).
- [ ] **ICU Plural Compliance (`ICU001`):** Resource catalogs (`messages.vi.json`) contain strictly `other` branches (plus optional `=0`). Zero `one`, `few`, or `many` branches.
- [ ] **Precomposed NFC Normalization (`NFC001`):** All output verified as canonical NFC Unicode.
- [ ] **Tone Mark Consistency (`TONE001`):** Consistent tone mark placement (*kiểu mới* `hoà, thuỷ` or *kiểu cũ* `hòa, thủy`) maintained throughout the file.
- [ ] **SMS Segment Optimization:** SMS notifications kept under 70 characters when accented, avoiding unintended segment doubling costs.
- [ ] **React IME Handling:** Search inputs handle `isComposing` to avoid premature search execution during Telex typing.
- [ ] **Vietnamese Collation:** List sorting uses `Intl.Collator('vi')` to properly order `Đ` after `D` and sort tone marks hierarchically.
- [ ] **Font Subsetting:** Typography includes Latin Extended-B glyphs; `line-height >= 1.4` prevents stacked diacritic clipping (`ễ, ệ, ộ, ữ, ỹ`).

---

## 7. Reviewer Sign-Off Matrix

| Evaluation Milestone | Target Score | Reviewer Role | Status & Comments |
|---|:---:|---|---|
| 1. Document Register & Tone | 5 / 5 | Technical Writer / Lead Architect | |
| 2. Code-Switching Hygiene | 5 / 5 | Senior Software Engineer | |
| 3. Error Microcopy Clarity | 5 / 5 | Product Designer / UX Writer | |
| 4. Platform Limit Conformance | 5 / 5 | Mobile Release Engineer | |
| 5. Survey Psychometrics | 5 / 5 | User Researcher (UXR) | |
| 6. Locale & ICU Compliance | 5 / 5 | Automated Linter (`validate_copy.py`) | |
| 7. Final Security / PII Check | 5 / 5 | Security / Privacy Champion | |

---

> *Note: For PR approvals, any finding of severe level blocks deployment immediately.*
