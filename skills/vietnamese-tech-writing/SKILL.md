---
name: vietnamese-tech-writing
description: Writes, edits, and audits native-quality Vietnamese (vi-VN) engineering, cloud, and product documentation — including commit subjects, PR reviews, RFCs, ADRs, blameless postmortems, operational runbooks, READMEs, API docs, CLI/UI error microcopy, i18n message catalogs, release notes, user research surveys, and app-store metadata. Master of technical code-switching taxonomy (Keep-EN vs Translate-VI vs Context-Split), impersonal system registers (eliminating 'bạn' in specs), bare imperative runbooks, non-blaming error microcopy, acquiescence bias mitigation in surveys, platform character limits, and Telex/VNI IME composition hazards.
license: MIT
metadata:
  version: "2.0.0"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese Engineering & Technical Writing Craft (`vi-VN`)

Vietnamese technical and software engineering prose fails in ways that are inverted from marketing copy. Marketing copy fails by being too literal. Technical copy fails by being **too Vietnamese**—translating industry-standard English commands and tool names that Vietnamese engineers leave in English, while importing conversational pronouns into documents that describe system architecture.

A document that translates `commit` to `cam kết` or `deploy to production` to `triển khai đến sản xuất` is instantly recognized by software engineers as unreviewed machine translation. Similarly, writing *"Bạn nên restart service"* in an incident runbook or *"Bạn đã nhập sai"* in an error banner introduces ambiguity and unprofessional friction.

This skill equips DESIGN:OS engineers and agents with the exact lexical conventions, syntactic rules, register distinctions, and internationalization safeguards required for world-class Vietnamese software engineering.

---

## 1. The Core Engineering Rule: Three-Tier Code-Switching

Read **[references/code-switching.md](references/code-switching.md)** for the complete 100+ term taxonomy:

1. **Tier 1 — Keep-EN Always (100% English):**
   - **Git & CI/CD:** `commit`, `push`, `pull`, `merge`, `rebase`, `cherry-pick`, `branch`, `PR`, `pipeline`, `build`.
   - **Environments:** `production`, `staging`, `dev`, `local`.
   - **Infrastructure & Tools:** `cluster`, `pod`, `node`, `middleware`, `webhook`, `load balancer`, `cache`.
   - **Rule:** Never translate `commit` to `cam kết` (means *to pledge*), or `production` to `sản xuất` (means *industrial manufacturing*).
2. **Tier 2 — Translate-VI Always (100% Vietnamese):**
   - **User-Facing Product Nouns:** `lỗi`, `tệp tin`, `tài khoản`, `mật khẩu`, `thông báo`, `báo cáo`, `cài đặt`.
   - **Form Fields & Navigation:** `Đăng nhập`, `Đăng ký`, `Tìm kiếm`, `Trang chủ`, `Lưu thay đổi`.
3. **Tier 3 — Context-Split (Split by Document Formality):**
   - In informal team PRs, code reviews, and Slack: use English terms (`cache`, `database`, `server`).
   - In published formal architecture specs (RFCs, ADRs): formal Sino-Vietnamese is preferred (`bộ nhớ đệm`, `cơ sở dữ liệu`, `máy chủ`).

---

## 2. Document Hierarchy & Register Rules

Select the document register before writing. Read **[references/doc-registers.md](references/doc-registers.md)**:

| Document Type | Target Register | Address Rule | Pronoun Contract |
|---|---|---|---|
| **RFC, Architecture Spec, ADR** | `eng-impersonal` | *None* | **Zero `bạn`.** Systems are described objectively (`Hệ thống sẽ...`, `Cần cấu hình...`). |
| **Blameless Postmortem** | `eng-impersonal` | *None* | **Name systems, never people.** Describe state transitions and systemic root causes. |
| **Operational Runbook** | `eng-impersonal` | *None* | **Bare imperatives.** Zero hedged language (`bạn nên`, `có thể`, `hãy`). |
| **Developer README & API Docs** | `eng-readme` | `bạn` | Friendly, direct second-person. Zero servile `quý khách`. |
| **Customer-Facing Status Page** | `re` / `formal` | `Quý khách` | Formal institutional respect during service downtime. |
| **UI Error Messages** | `ux-microcopy` | *None* | Objective facts. **Never blame the user (`ENG008`).** |

---

## 3. Runbooks & Error Microcopy Standards

### Operational Runbooks (`ENG007`)
At 3:00 AM during an active incident, hedged phrases make mandatory procedures appear optional.
- ❌ **Hedged:** *"Bạn nên kiểm tra log rồi bạn có thể restart service nếu cần."*
- ✅ **Bare Imperative:** *"Kiểm tra log tại `/var/log/app.log`. Chạy lệnh `systemctl restart app` để khởi động lại dịch vụ."*

### UI Error Messages & Alerts (`ENG008`)
Never blame the user or accuse them of making mistakes. State the input condition and the remedy objectively:
- ❌ **Blaming User:** *"Bạn đã nhập sai định dạng email."* / *"Lỗi của bạn: mật khẩu quá ngắn."*
- ✅ **Objective Fact:** *"Email không đúng định dạng. Vui lòng kiểm tra lại."* / *"Mật khẩu cần tối thiểu 8 ký tự bao gồm chữ và số."*

---

## 4. Platform Character Limits (`PROD003`)

Vietnamese text expands by 25–35% compared to English. Character limits enforced by app stores and mobile platforms must be verified against precomposed NFC strings:

- **Apple App Store Title:** Maximum **30 characters**.
- **Apple App Store Subtitle:** Maximum **30 characters**.
- **Apple App Store Promotional Text:** Maximum **170 characters**.
- **Google Play Short Description:** Maximum **80 characters**.
- **Google Play Full Description:** Maximum **4.000 characters**.
- **Mobile Push Notifications:** Body text under **90 characters** to prevent lock-screen truncation.

---

## 5. Survey & User Research Psychometrics (`PROD002`)

Read **[references/survey-design.md](references/survey-design.md)**:
- **The Acquiescence Bias Trap:** Agree/Disagree questions (*"Bạn có đồng ý rằng..."*) inflate positive feedback by 10–15% due to Vietnamese politeness norms.
- **Mandatory Rule:** Always use **Item-Specific Construct Scales** measuring the exact property (e.g., *Rất khó → Rất dễ* for Customer Effort Score; *Rất không hài lòng → Rất hài lòng* for CSAT).
- **Preserve Net Promoter Score (NPS):** Strictly maintain the standard **0 to 10 scale**. Never compress to binary Yes/No or 1–5.

---

## 6. Internationalization & Technical Hazards

Read **[references/i18n-hazards.md](references/i18n-hazards.md)**:
- **The UCS-2 70-Char SMS Cliff:** A single Vietnamese diacritic flips SMS gateways from GSM 7-bit (160 chars) to UCS-2 (70 chars), doubling or tripling telecom costs. Keep accented OTP messages under 70 characters.
- **CLDR ICU Plural Rules (`ICU001`):** Vietnamese has **only the `other` plural branch** (plus optional `=0`). Any `one`, `few`, or `many` branch in `messages.vi.json` is a copy-paste error from English.
- **ASCII Identifiers (`ENG001`):** Commit subjects, git branch names, code variables, and JSON i18n keys must remain strictly ASCII (`[^\x00-\x7F]+` prohibited).
- **Telex/VNI React IME Composition:** Search inputs and form fields must monitor `onCompositionStart` and `onCompositionEnd` to prevent premature search triggers while vowels are combining.
- **Vietnamese Collation:** Standard JavaScript `array.sort()` breaks because `Đ` sorts after `Z`. Always use `new Intl.Collator("vi").compare`.

---

## 7. CLI Validation & Quality Gates

Run `validate_copy.py` with doctype flags across your engineering artifacts:

```bash
# Validate Git commit message
python scripts/validate_copy.py commit.txt --doctype commit

# Validate Git branch name
python scripts/validate_copy.py branch.txt --doctype branch

# Validate i18n resource file keys and ICU plurals
python scripts/validate_copy.py assets/messages.vi.json --doctype identifier --strict

# Validate RFC or ADR (flags forbidden 'bạn' and informalities)
python scripts/validate_copy.py docs/rfc-012.md --doctype rfc

# Validate incident runbook (flags hedged instructions)
python scripts/validate_copy.py runbooks/deploy.md --doctype runbook

# Validate error messages (flags blaming 'Bạn đã nhập sai')
python scripts/validate_copy.py errors.txt --doctype error-message

# Validate App Store metadata character limits
python scripts/validate_copy.py appstore-subtitle.txt --doctype app-store-subtitle

# Validate user survey questions (flags agree/disagree bias)
python scripts/validate_copy.py survey.md --doctype survey
```

### Reference Documentation Library
- **[references/code-switching.md](references/code-switching.md):** 100+ term engineering taxonomy across Git, Cloud, AI, and Product.
- **[references/doc-registers.md](references/doc-registers.md):** Impersonal RFCs/ADRs, bare imperative runbooks, and blameless postmortems.
- **[references/i18n-hazards.md](references/i18n-hazards.md):** String expansion, UCS-2 SMS cliff, ICU plurals, React IME bugs, and collation.
- **[references/survey-design.md](references/survey-design.md):** Psychometric scales, acquiescence bias prevention, and NPS design.
- **[references/glossary.md](references/glossary.md):** 55+ machine-readable engineering calques.
- **[references/banned-phrases.md](references/banned-phrases.md):** Blocked engineering calques and superlatives.
- **[references/qa-checklist.md](references/qa-checklist.md):** 7-milestone technical review rubric.
