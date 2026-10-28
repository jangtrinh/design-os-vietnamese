<!-- vlc-disable: TONE001, DIA001, LAW001, CAL001, PRO001, CTX001, CTX002, CTX003, CTX004, CTX005 -->

# Context Matrix — Who Writes to Whom (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. The [register matrix](register-matrix.md) models **organisation → customer** voices. This file models the other half: **one person writing to a specific person or group** — a chat with friends, an email to the boss, a job application, a document for executives or for engineers.

This file is the canonical source of truth. `validate_copy.py --context <id>` parses the machine-readable tables below at runtime and runs rules `CTX001`–`CTX005` (implemented in `writing_context.py`). Tone, warmth and rhythm stay in the skill guidance; only deterministic checks live here.

> **Evidence class: `proposed`.** Everything below is writing convention, not statute. No law dictates how to chat with a friend or to greet a manager. `Nghị định 30/2020/NĐ-CP` governs administrative documents only and is already covered by the `gov-admin` register. Word lists need native-speaker review before they are treated as stable.

## 1. Facets

A **context preset** is a named bundle over five independent facets. A rule reads facets, never the preset name.

| Facet | Values | Read by |
|---|---|---|
| `relation` | `up` (boss, recruiter, client, elder), `peer`, `down` (reports), `public` | `CTX001` and `CTX003` severity |
| `closeness` | `stranger`, `acquainted`, `close` | documentation; `close` presets disable `CTX003` |
| `channel` | `chat`, `email`, `document`, `post` | `CTX003` severity, `CTX004` |
| `purpose` | `inform`, `request`, `report`, `apply`, `decline`, `apologize` | guidance only; no rule reads it in v1 |
| `reader` | `general`, `executive`, `technical` | `CTX003` (ambiguous tokens are skipped for `technical`), `CTX005` |

## 2. Machine-Readable Context Presets

- **Self / Address** — the terms this context normally uses for the writer (`xưng`) and the reader (`hô`). Guidance shown in the `CTX001` hint; `—` means impersonal.
- **Forbids** — comma-separated address or self terms that trigger `CTX001`. Severity is `error` when `relation` is `up`, otherwise `warning`.
- **Disables** — rules switched off for this context. Applied after domain rules are collected, so they also silence `--domain` rules listed here. Real defects (`NFC001`, `ENC001`, `PRO001`) are never disabled.
- **Enables** — the `CTX` rules that run for this context.
- **Basis** — evidence class. `proposed` = convention, not statute.

<!-- machine-readable: contexts -->

| Context | Label | Relation | Closeness | Channel | Purpose | Reader | Self | Address | Forbids | Disables | Enables | Basis |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| `chat-close-friend` | Chat bạn thân | peer | close | chat | inform | general | `tao`, `mình`, `tớ` | `mày`, `cậu`, `bạn` | `quý khách`, `quý vị` | `DIA001`, `CAL001`, `LAW001`, `SYN001`, `NUM002`, `NUM004`, `TONE001`, `CTX003` | `CTX001` | `proposed` |
| `chat-colleague` | Chat đồng nghiệp (Slack/Zalo nhóm) | peer | acquainted | chat | inform | general | `mình`, `em`, `anh`, `chị` | `bạn`, `anh`, `chị`, `em` | `quý khách`, `quý vị`, `mày`, `tao` | `DIA001`, `CAL001`, `LAW001`, `SYN001`, `NUM002`, `NUM004`, `TONE001`, `CTX003` | `CTX001` | `proposed` |
| `chat-to-manager` | Nhắn sếp | up | acquainted | chat | request | general | `em`, `tôi` | `anh/chị`, `sếp` | `mày`, `tao`, `tớ`, `cậu`, `mình`, `bạn` | — | `CTX001`, `CTX002`, `CTX003` | `proposed` |
| `email-to-manager` | Email gửi sếp/cấp trên | up | acquainted | email | report | general | `em`, `tôi` | `anh/chị`, `sếp` | `mày`, `tao`, `tớ`, `cậu`, `mình`, `bạn` | — | `CTX001`, `CTX002`, `CTX003`, `CTX004` | `proposed` |
| `email-to-colleague` | Email đồng nghiệp | peer | acquainted | email | request | general | `mình`, `tôi`, `em`, `anh`, `chị` | `bạn`, `anh`, `chị`, `em` | `quý khách`, `quý vị`, `mày`, `tao`, `tớ`, `cậu` | — | `CTX001`, `CTX003`, `CTX004` | `proposed` |
| `email-to-team` | Email/thông báo cho cấp dưới, cả team | down | acquainted | email | inform | general | `anh`, `chị`, `mình`, `tôi` | `các bạn`, `các em`, `cả team` | `quý khách`, `quý vị`, `mày`, `tao` | — | `CTX001`, `CTX003`, `CTX004` | `proposed` |
| `email-to-client` | Email khách hàng/đối tác (cá nhân viết) | up | stranger | email | request | general | `tôi`, `em` | `anh/chị`, `quý công ty` | `mày`, `tao`, `tớ`, `cậu`, `mình`, `bạn` | — | `CTX001`, `CTX003`, `CTX004` | `proposed` |
| `job-application` | Thư xin việc / email ứng tuyển / CV | up | stranger | email | apply | general | `tôi`, `em` | `anh/chị`, `quý công ty` | `mày`, `tao`, `tớ`, `cậu`, `mình`, `bạn` | — | `CTX001`, `CTX003`, `CTX004` | `proposed` |
| `doc-for-executives` | Tài liệu/báo cáo cho lãnh đạo | up | acquainted | document | report | executive | — | — | `mày`, `tao`, `tớ`, `cậu`, `mình`, `bạn` | — | `CTX001`, `CTX003`, `CTX005` | `proposed` |
| `doc-for-engineers` | Tài liệu kỹ thuật cho dev | peer | acquainted | document | inform | technical | `chúng tôi`, `chúng ta` | `bạn` | `quý khách`, `quý vị`, `mày`, `tao` | — | `CTX001`, `CTX003` | `proposed` |

### Why these rules are on or off

- **Casual chats** disable `DIA001`, `CAL001`, `LAW001`, `SYN001`: unaccented typing, borrowed English words, superlatives and word-order slips are normal in a friend chat and are not advertising claims. `NUM002` (ungrouped amounts such as `500000đ`), `NUM004` (`m2`) and `TONE001` (mixed `hoà`/`hòa`) are disabled for the same reason. `CTX003` is disabled because abbreviations are the register. Left **on**: `NFC001`, `ENC001` (broken Unicode is broken everywhere), `PRO001` (mixing `quý khách` with `bạn` in one message), and the numeric/format checks that prevent real misreadings (`NUM001`, `NUM003`, `DATE001`, `PHONE001`, `ICU001`, `ICU002`).
- **Chat to the boss** keeps every universal rule: the message is informal in channel but not in relationship.
- **`CTX002` runs only for `chat-to-manager` and `email-to-manager`.** A formal letter to a recruiter or client signals respect with `Kính gửi` / `Trân trọng`, and forcing `ạ` into it reads as over-familiar.
- **`CTX004` runs for every email preset.** `CTX005` runs only for `doc-for-executives`.

## 3. Machine-Readable Word Lists

### Chat abbreviations and teencode (`CTX003`)

`Ambiguous = yes` means the token is also a normal English word, unit or code (`vs`, `ns`, `ko-KR`); it is skipped when the context's `reader` is `technical`. Tokens are matched as whole words, lowercase or capitalised, never after a digit (`5 ns`, `5k`) and never inside identifiers, paths or locale codes (`ko-KR`, `k8s`).

<!-- machine-readable: chat-abbreviations -->

| Token | Meaning | Ambiguous | Basis |
|---|---|---|---|
| `ko` | không | yes | `proposed` |
| `k` | không | yes | `proposed` |
| `hok` | không | no | `proposed` |
| `dc` | được | yes | `proposed` |
| `đc` | được | no | `proposed` |
| `j` | gì | yes | `proposed` |
| `bt` | bình thường | yes | `proposed` |
| `ns` | nói | yes | `proposed` |
| `mn` | mọi người | no | `proposed` |
| `ae` | anh em | no | `proposed` |
| `vs` | với | yes | `proposed` |
| `r` | rồi | yes | `proposed` |
| `oke` | ổn / được | no | `proposed` |
| `okie` | ổn / được | no | `proposed` |
| `thik` | thích | no | `proposed` |
| `iu` | yêu | no | `proposed` |
| `bik` | biết | no | `proposed` |
| `wá` | quá | no | `proposed` |
| `ntn` | như thế nào | no | `proposed` |
| `trc` | trước | no | `proposed` |
| `cx` | cũng | no | `proposed` |
| `lm` | làm | yes | `proposed` |
| `mk` | mình / mật khẩu | yes | `proposed` |
| `hnay` | hôm nay | no | `proposed` |
| `zậy` | vậy | no | `proposed` |
| `dzậy` | vậy | no | `proposed` |
| `pls` | vui lòng | no | `proposed` |

### Politeness particles (`CTX002`)

<!-- machine-readable: politeness-particles -->

| Particle | Basis |
|---|---|
| `ạ` | `proposed` |
| `dạ` | `proposed` |
| `vâng` | `proposed` |

### Email greetings (`CTX004`)

A greeting is any of these at the start of the first body line. Header fields such as `Subject:`, `Chủ đề:`, `To:`, `From:` and Markdown headings are skipped when looking for the first body line.

<!-- machine-readable: email-greetings -->

| Opener | Basis |
|---|---|
| `Kính gửi` | `proposed` |
| `Kính chào` | `proposed` |
| `Xin chào` | `proposed` |
| `Chào` | `proposed` |
| `Em chào` | `proposed` |
| `Con chào` | `proposed` |
| `Tôi chào` | `proposed` |
| `Thân gửi` | `proposed` |
| `Thân chào` | `proposed` |
| `Gửi` | `proposed` |
| `Dear` | `proposed` |
| `Hi` | `proposed` |
| `Hello` | `proposed` |
| `Các anh` | `proposed` |
| `Các chị` | `proposed` |
| `Các bạn` | `proposed` |
| `Các em` | `proposed` |
| `Mọi người` | `proposed` |
| `Cả team` | `proposed` |
| `Anh chị em` | `proposed` |

### Email sign-offs (`CTX004`)

A sign-off is any of these at the start of one of the last six non-empty lines.

<!-- machine-readable: email-signoffs -->

| Closer | Basis |
|---|---|
| `Trân trọng` | `proposed` |
| `Kính thư` | `proposed` |
| `Kính chào` | `proposed` |
| `Thân mến` | `proposed` |
| `Thân ái` | `proposed` |
| `Thân` | `proposed` |
| `Xin cảm ơn` | `proposed` |
| `Cảm ơn` | `proposed` |
| `Chúc` | `proposed` |
| `Best regards` | `proposed` |
| `Regards` | `proposed` |
| `Sincerely` | `proposed` |
| `Thanks` | `proposed` |
| `Cheers` | `proposed` |

### Executive summary markers (`CTX005`)

One of these must appear within the first 15 non-empty lines of a document written for executives.

<!-- machine-readable: summary-markers -->

| Marker | Basis |
|---|---|
| `Tóm tắt` | `proposed` |
| `Tóm lược` | `proposed` |
| `TL;DR` | `proposed` |
| `Kết luận` | `proposed` |
| `Đề xuất` | `proposed` |
| `Khuyến nghị` | `proposed` |
| `Điểm chính` | `proposed` |
| `Executive summary` | `proposed` |
| `Bottom line` | `proposed` |

## 4. Rules

| Rule | Fires when | Severity |
|---|---|---|
| `CTX001` | An address or self term in **Forbids** appears (first hit per term; compounds such as `bạn bè`, `một mình`, `tao nhã` are exempt) | `error` for `relation: up`, else `warning` |
| `CTX002` | A direct-address term from **Address** (`anh`, `chị`, `sếp`) appears and no politeness particle (`ạ`, `dạ`, `vâng`) appears anywhere in the message | `warning` |
| `CTX003` | A chat abbreviation from section 3 appears | `error` for `up` + `email`/`document`, else `warning` |
| `CTX004` | `email` channel: the first body line has no greeting, or the last six non-empty lines have no sign-off | `warning` |
| `CTX005` | `doc-for-executives`: no summary marker in the first 15 non-empty lines | `warning` |

All five accept `vlc-disable-line` / `vlc-disable` directives like every other rule.

## 5. Presets in Practice

Examples are teaching material, not test fixtures. **Bad** shows what the preset's rules catch; **good** shows the fix.

### `chat-close-friend` — Chat bạn thân

Anything goes except broken text and a corporate voice. Teencode, no tones, `tao/mày` and superlatives are fine.

- Bad: `Quý khách vui lòng đợi mình một chút nhé.` — a customer-service voice in a friend chat (`CTX001`).
- Good: `Đợi tao tí nha, tao ra liền.`

### `chat-colleague` — Chat đồng nghiệp

Friendly and fast, but not `mày/tao`. Abbreviations are tolerated.

- Bad: `Mày gửi tao file với.` (`CTX001`, warning).
- Good: `Bạn gửi mình file với nha, cảm ơn nhiều.`

### `chat-to-manager` — Nhắn sếp

Short, with `em … ạ`. No `bạn/mình`, no teencode, politeness particle present.

- Bad: `Anh ơi mai em xin nghỉ ko?` (`CTX002`, `CTX003`).
- Good: `Anh ơi, mai em xin nghỉ một buổi được không ạ?`

### `email-to-manager` — Email gửi sếp/cấp trên

Greeting, `em/anh`, `ạ`, sign-off. Report the result first.

- Bad: `Bạn xem giúp em báo cáo này.` with no greeting or closing (`CTX001`, `CTX002`, `CTX004`).
- Good: `Kính gửi anh Nam, / Em gửi anh báo cáo tuần này ạ. / Trân trọng, Lan`

### `email-to-colleague` — Email đồng nghiệp

Warm but complete: greeting, one ask, sign-off.

- Bad: `Gửi tao danh sách khách hàng đc ko?` (`CTX001`, `CTX003`, `CTX004`).
- Good: `Chào An, / Bạn gửi mình danh sách khách hàng trước thứ Sáu nhé. / Cảm ơn bạn, Bình`

### `email-to-team` — Email/thông báo cho cấp dưới, cả team

A lead speaks plainly, never as a customer-service voice or with `mày/tao`.

- Bad: `Quý vị lưu ý họp lúc 9h.` (`CTX001`, `CTX004`).
- Good: `Chào cả team, / Họp sprint 9h sáng thứ Hai ở phòng Mây nhé. / Thân, Hà`

### `email-to-client` — Email khách hàng/đối tác

One person writing for a business: `anh/chị`, `tôi/em`, complete frame.

- Bad: `Mình gửi bạn báo giá ko?` (`CTX001`, `CTX003`, `CTX004`).
- Good: `Kính gửi anh Hùng, / Tôi gửi anh báo giá đính kèm. / Trân trọng, Mai`

### `job-application` — Thư xin việc / email ứng tuyển / CV

Respectful, specific, complete frame; no peer pronouns toward the recruiter. A stand-alone CV file has no greeting or sign-off by nature: add `<!-- vlc-disable: CTX004 -->` to it, or check only the cover letter.

- Bad: `Mình muốn ứng tuyển, bạn xem CV giúp mình.` (`CTX001`, `CTX004`).
- Good: `Kính gửi anh/chị, / Tôi xin ứng tuyển vị trí Kế toán tổng hợp. / Trân trọng, Lan`

### `doc-for-executives` — Tài liệu/báo cáo cho lãnh đạo

The conclusion comes first; a busy reader should stop after one screen.

- Bad: a report that opens with background and never states a recommendation (`CTX005`).
- Good: `## Tóm tắt / Đề xuất chọn nhà cung cấp B, tiết kiệm 12% chi phí.`

### `doc-for-engineers` — Tài liệu kỹ thuật cho dev

Direct and precise. `bạn` and `chúng ta` are fine; a customer-service voice is not. `vs`, `ns`, `ko-KR` in technical prose are not flagged.

- Bad: `Quý khách chạy lệnh sau để cài đặt.` (`CTX001`, warning).
- Good: `Chạy lệnh sau để cài đặt.`

## 6. Suggestion (never a finding)

With no `--context`, `validate_copy.py` may print **one hint to stderr** when strong signals appear, for example `Kính gửi anh/chị` together with a self-reference `em` suggests `email-to-manager`, and `Kính gửi` together with `ứng tuyển` suggests `job-application`. The hint never changes findings, the JSON on stdout or the exit code, and the linter never applies context rules on a guess.
