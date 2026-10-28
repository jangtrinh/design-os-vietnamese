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

`Ambiguous = yes` means the token is also a normal English word, unit or code (`vs`, `ns`, `ko-KR`); it is skipped when the context's `reader` is `technical`. Tokens are matched as whole words (lowercase, or capitalised for tokens of two or more letters; single-letter tokens are lowercase only), never after a digit (`5 ns`, `5k`) and never inside identifiers, paths or locale codes (`ko-KR`, `k8s`).

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

## 5. Từng preset trong thực tế

Các ví dụ dưới đây là tài liệu giải thích, không phải fixture kiểm thử. **Sai** là đoạn bị quy tắc của preset bắt (kèm danh sách quy tắc chạy thật); **Đúng** là cách sửa, không còn lỗi nào. Mã quy tắc nằm trong ngoặc.

### `chat-close-friend` — Chat bạn thân

Chỉ cần chữ không hỏng và không nói bằng giọng chăm sóc khách hàng. Teencode, bỏ dấu, `tao/mày`, "ngon nhất" đều chấp nhận được.

- Sai: `Quý khách vui lòng đợi mình một chút nhé, mình ra liền.` (`CTX001`: giọng chăm sóc khách hàng trong chat bạn bè)
- Đúng: `Đợi tao tí nha, tao ra liền.`

### `chat-colleague` — Chat đồng nghiệp (Slack/Zalo nhóm)

Thân thiện và nhanh, nhưng không dùng `mày/tao`. Viết tắt được bỏ qua.

- Sai: `Mày gửi tao file với.` (`CTX001` hai lần: `Mày`, `tao`; mức cảnh báo)
- Đúng: `Bạn gửi mình file với nha, cảm ơn nhiều.`

### `chat-to-manager` — Nhắn sếp

Ngắn gọn, xưng `em`, có từ lễ phép `ạ`. Không dùng `bạn/mình`, không teencode.

- Sai: `Anh ơi mai em xin nghỉ ko?` (`CTX002`: có `Anh` nhưng không có `ạ/dạ/vâng`; `CTX003`: `ko`)
- Đúng: `Anh ơi, mai em xin nghỉ một buổi được không ạ?`

### `email-to-manager` — Email gửi sếp/cấp trên

Có lời chào đầu, xưng `em`, hô `anh/chị`, có `ạ` và lời kết. Nêu kết quả trước.

- Sai: `Bạn xem giúp em báo cáo này.` (`CTX001`: `Bạn` với cấp trên; `CTX004` hai lần: thiếu lời chào và thiếu lời kết)
- Đúng:

  ```text
  Kính gửi anh Nam,

  Em gửi anh báo cáo tuần này ạ. Anh xem giúp em nhé.

  Trân trọng,
  Lan
  ```

### `email-to-colleague` — Email đồng nghiệp

Thân thiện nhưng đủ khung: lời chào, một yêu cầu rõ, lời kết.

- Sai: `Tao cần danh sách khách hàng, gửi đc ko?` (`CTX001`: `Tao`; `CTX003` hai lần: `đc`, `ko`; `CTX004` hai lần)
- Đúng: `Chào An, / Bạn gửi mình danh sách khách hàng trước thứ Sáu nhé. / Cảm ơn bạn, Bình`

### `email-to-team` — Email/thông báo cho cấp dưới, cả team

Người dẫn dắt nói thẳng, không dùng giọng chăm sóc khách hàng và không `mày/tao`.

- Sai: `Quý vị lưu ý họp lúc 9h.` (`CTX001`: `Quý vị`; `CTX004` hai lần)
- Đúng: `Chào cả team, / Họp sprint 9h sáng thứ Hai ở phòng Mây nhé. / Thân, Hà`

### `email-to-client` — Email khách hàng/đối tác (cá nhân viết)

Một người viết thay mặt công việc: hô `anh/chị`, xưng `tôi/em`, đủ khung thư.

- Sai: `Mình gửi bạn báo giá ko?` (`CTX001` hai lần: `Mình`, `bạn`; `CTX003`: `ko`; `CTX004` hai lần)
- Đúng: `Kính gửi anh Hùng, / Tôi gửi anh báo giá đính kèm. / Trân trọng, Mai`

### `job-application` — Thư xin việc / email ứng tuyển / CV

Tôn trọng, cụ thể, đủ khung thư; không dùng đại từ ngang hàng với nhà tuyển dụng. Tệp CV đứng riêng vốn không có lời chào hay lời kết: thêm `<!-- vlc-disable: CTX004 -->` vào tệp đó, hoặc chỉ kiểm thư xin việc.

- Sai: `Mình muốn ứng tuyển, bạn xem CV giúp mình.` (`CTX001` hai lần: `Mình`, `bạn`; `CTX004` hai lần)
- Đúng: `Kính gửi anh/chị, / Tôi xin ứng tuyển vị trí Kế toán tổng hợp. CV của tôi đính kèm thư này. / Trân trọng, Lan`

### `doc-for-executives` — Tài liệu/báo cáo cho lãnh đạo

Kết luận đứng đầu: người đọc bận nên dừng được sau một màn hình.

- Sai: báo cáo mở đầu bằng bối cảnh và không có mục tóm tắt hay đề xuất trong 15 dòng đầu (`CTX005`)
- Đúng: `## Tóm tắt` ngay sau tiêu đề, ví dụ `Nên chọn nhà cung cấp B: rẻ hơn 12% so với A.`

### `doc-for-engineers` — Tài liệu kỹ thuật cho dev

Trực tiếp và chính xác. `bạn` và `chúng ta` đều ổn; giọng chăm sóc khách hàng thì không. Các token vừa là viết tắt chat vừa là từ tiếng Anh hay mã (`vs`, `ns`, `ko-KR`) không bị bắt trong tài liệu kỹ thuật.

- Sai: `Quý khách chạy lệnh sau để cài đặt.` (`CTX001`; mức cảnh báo)
- Đúng: `Chạy lệnh sau để cài đặt.`

### Giới hạn đã biết

- Lời chào chỉ được nhận diện theo từ mở đầu dòng đầu tiên, nên `Gửi` (như trong `Gửi tao danh sách…`) cũng bị tính là lời chào và `Chúc` (như trong `Chúc mừng …`) cũng bị tính là lời kết: bỏ sót chứ không báo nhầm.
- `CTX002` coi `anh`, `chị`, `sếp` là xưng hô trực tiếp; `anh ấy`, `anh em`, `nước Anh` được loại trừ nhưng một cái tên đi sau (`anh Nam`) vẫn tính là xưng hô.
- Danh sách từ chưa qua rà soát của người bản ngữ (xem phần Follow-ups của kế hoạch).

## 6. Gợi ý (không bao giờ là một finding)

Khi không có `--context`, `validate_copy.py` có thể in **một dòng gợi ý ra stderr** nếu có tín hiệu mạnh: `Kính gửi anh/chị` cùng `Em xin …` gợi ý `email-to-manager`; `Kính gửi` cùng `ứng tuyển` gợi ý `job-application`; `mày` cùng `tao` gợi ý `chat-close-friend`. Gợi ý không đổi finding, JSON trên stdout hay mã thoát, và công cụ không bao giờ áp dụng quy tắc ngữ cảnh theo phỏng đoán.
