<!-- synced from shared/references/plain-vietnamese.md (c47b022113080aff) — edit shared/ source, not this copy -->
<!-- vlc-disable: all -->

# Plain Vietnamese — Viết ngắn, viết thẳng (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. A text can pass every mechanical check (number format, calques, banned phrases, register, superlatives) and still read as long-winded and machine-written. This page describes the rule family `PLAIN001`–`PLAIN007`, which checks the habits behind that impression, and ends with a short reading check for what no rule can see (section 6). The rules live in `plain_tone.py`; the phrase list is the machine-readable table below, so a team can extend it without touching Python.

> **Evidence class: `proposed`.** These are writing conventions, not statute. The thresholds are defaults you can change (`--max-sentence-words`), and every rule can be silenced with `<!-- vlc-disable: PLAINxxx -->`.

## 1. Why

A reader with limited time looks for the decision, the number and the next step. Four habits push those out of sight:

- **Long sentences.** Past about twenty-five words the reader loses the subject before the verb arrives.
- **Announcing instead of saying.** "Bản đánh giá này cho thấy…" spends five words before the point.
- **Filler.** "Điều này", "một cách", "thực hiện" and "tiến hành" add length and no information.
- **Audit scaffolding.** Labels such as `FACT` or `ASSUMPTION` belong in working notes. In a finished text, say how sure you are in a plain clause ("chưa kiểm tra", "đã đo").

## 2. The rules

A "word" is a space-separated token, which in Vietnamese is one syllable. Text inside backticks, fenced code blocks and URLs is ignored. Headings, table rows, quoted lines (`>`) and front matter are not prose and are skipped, and so is any sentence with no Vietnamese letter (an English paragraph). A sentence that wraps over several lines is measured as one sentence.

| Rule | Checks | Default |
|---|---|---|
| `PLAIN001` | A sentence longer than 25 words (`--max-sentence-words N` changes the limit). | warning |
| `PLAIN002` | An audit label (`FACT`, `INFERENCE`, `ASSUMPTION`, `UNKNOWN`, upper case, whole word) in prose. | warning |
| `PLAIN003` | A meta opener at the start of a sentence, list item or bold lead-in (table below). | warning |
| `PLAIN004` | A filler phrase anywhere in a sentence (table below). | warning |
| `PLAIN005` | `không chỉ … mà còn` (or `không những … mà còn`) inside one sentence. | warning |
| `PLAIN006` | A spaced dash (`—` or `–`) used as an aside. One finding per sentence. Number ranges such as `10 – 20` are skipped. | warning |
| `PLAIN007` | More than two parentheses in one sentence. | warning |

**Severity.** All seven rules are warnings. They become errors when you declare an executive reader with `--context doc-for-executives`, and the casual chat presets switch them off. The existing `--strict` flag makes any warning exit non-zero, `PLAIN` rules included. The rules run on prose files only (`.md`, `.mdx`, `.markdown`, `.txt` and stdin), not on string literals in code or JSON.

```bash
python3 shared/scripts/validate_copy.py report.md
python3 shared/scripts/validate_copy.py report.md --context doc-for-executives
python3 shared/scripts/validate_copy.py report.md --strict --max-sentence-words 25
```

## 3. Phrase list (machine-readable)

`validate_copy.py` reads this table at runtime. `Loại` is one of `label` (rule `PLAIN002`, matched case-sensitively as a whole word), `opener` (rule `PLAIN003`, matched only at the start of a sentence) or `filler` (rule `PLAIN004`, matched anywhere, any case). Add a row to extend the list.

<!-- machine-readable: plain-phrases -->
| Cụm từ | Loại | Gợi ý viết lại |
|---|---|---|
| FACT | label | bỏ nhãn; nói thẳng điều đã đo hoặc đã kiểm tra |
| INFERENCE | label | bỏ nhãn; viết “có thể”, “nhiều khả năng” kèm lý do |
| ASSUMPTION | label | bỏ nhãn; viết “giả sử …” hoặc “chưa kiểm tra” |
| UNKNOWN | label | bỏ nhãn; viết “chưa rõ” và nói cần kiểm tra gì |
| Bản đánh giá này | opener | vào thẳng kết quả |
| Bản rà soát này | opener | vào thẳng kết quả |
| Phần mới: | opener | bỏ tiêu đề dẫn; viết nội dung mới luôn |
| Lưu ý: | opener | đưa điều cần lưu ý vào câu chính |
| Hệ quả: | opener | nói hệ quả như một câu thường |
| Điểm chính: | opener | viết điểm chính luôn |
| Cần lưu ý rằng | opener | bỏ cụm dẫn; viết điều cần lưu ý |
| điều này | filler | nêu rõ “điều này” là gì, hoặc bỏ |
| nhìn chung | filler | bỏ |
| đáng chú ý | filler | bỏ; để con số tự nói |
| một cách | filler | dùng tính từ hoặc trạng từ trực tiếp (“nhanh”, thay vì “một cách nhanh chóng”) |
| thực hiện | filler | dùng động từ cụ thể (“gửi”, “kiểm tra”, “chạy”) |
| tiến hành | filler | dùng động từ cụ thể hoặc bỏ |

`tiến hành` and `thực hiện` also appear in the calque tables (`CAL001`) for button labels; both rules can fire on the same words and are independent.

## 4. Before and after

Examples use a generic delivery app and a dashboard. This table is executed by the test suite: every `Trước` must trigger its rule and every `Sau` must be clean.

<!-- machine-readable: plain-examples -->
| Trước | Sau | Quy tắc |
|---|---|---|
| Ứng dụng giao hàng cho phép người dùng theo dõi trạng thái đơn hàng của mình trong thời gian thực, đồng thời nhận thông báo khi tài xế đến gần điểm giao, và cũng có thể liên hệ trực tiếp với tài xế để thay đổi địa chỉ nhận hàng nếu cần. | Bạn theo dõi đơn theo thời gian thực. Khi tài xế đến gần, ứng dụng báo cho bạn. Cần đổi địa chỉ thì gọi thẳng tài xế. | `PLAIN001` |
| FACT: thời gian giao trung bình giảm từ 42 xuống 35 phút. | Thời gian giao trung bình giảm từ 42 xuống 35 phút. | `PLAIN002` |
| Bản đánh giá này cho thấy tỷ lệ giao trễ giảm còn 4%. | Tỷ lệ giao trễ giảm còn 4%. | `PLAIN003` |
| Nhìn chung, nhóm vận hành tiến hành kiểm tra đơn trễ mỗi sáng. | Nhóm vận hành kiểm tra đơn trễ mỗi sáng. | `PLAIN004` |
| Bảng điều khiển không chỉ hiện doanh thu theo ngày mà còn hiện doanh thu theo giờ. | Bảng điều khiển hiện doanh thu theo ngày và theo giờ. | `PLAIN005` |
| Bảng điều khiển cập nhật mỗi phút — kể cả giờ cao điểm — và lưu lịch sử 30 ngày. | Bảng điều khiển cập nhật mỗi phút, kể cả giờ cao điểm. Lịch sử lưu 30 ngày. | `PLAIN006` |
| Đơn (loại A) giao trong 30 phút (nội thành) hoặc 60 phút (ngoại thành) tùy khu vực (xem bảng phí). | Đơn loại A giao trong 30 phút ở nội thành, 60 phút ở ngoại thành. Phí theo khu vực nằm trong bảng phí. | `PLAIN007` |

## 5. When to silence a rule

- A quoted source, a legal clause or a contract term must keep its wording. Use `<!-- vlc-disable-line: PLAIN001 -->` on that line.
- A document that explains the audit labels themselves (such as this page) uses `<!-- vlc-disable: PLAIN002 -->` at the top.
- The casual chat presets (`--context chat-close-friend`, `--context chat-colleague`) switch all seven rules off. Every other context keeps them.

## 6. Reading check: what a clean report cannot tell you

`0 errors · 0 warnings` means the words follow the rules. It does not mean a reader understands them. Headings, captions and spoken lines are skipped or barely touched by the rules above, and they are where readers get lost. Before you publish one, read it once against the four questions below.

> **Evidence class: `proposed`.** Taken from a human editor's corrections on a published Vietnamese data article (2026-11): clipped headings, captions that described the picture, and a voice-over that re-read the article all passed every validator with zero findings.

| Check | Question to ask | Trước | Sau |
|---|---|---|---|
| Heading is a claim | Does the heading say who did what and what changed, in one full clause? A slogan built from parallel verbs or nouns makes the reader guess the link. | Đơn tăng, tài xế giảm, khách chờ | Số đơn tăng 20% nhưng tài xế ít đi, nên khách chờ lâu hơn |
| Caption informs | Does the caption add a fact the picture alone cannot give, and point to where the text explains it? Describing what is visible adds nothing. | Một tài xế đứng chờ bên xe máy. | Giờ cao điểm, mỗi tài xế chờ món trung bình 12 phút. Phần 2 giải thích vì sao. |
| Terms explained at first use | Would a reader outside the team know each term? Say what it means in plain words the first time, then keep the term. | Tỷ lệ SLA breach tăng. | Tỷ lệ đơn giao trễ so với cam kết (SLA) tăng. |
| Spoken text is said, not read | Read the voice-over aloud. Does each sentence sound like a person explaining, with linking words, and no more than two numbers in a one-minute script, rounded the way people say them? | Số đơn tăng 18,7%, tài xế giảm 6,2%, thời gian chờ tăng 3,4 phút. | Đơn thì tăng gần một phần năm, mà tài xế lại ít đi, nên khách phải chờ lâu hơn. |

**How to run it.** Read the text aloud, or give it to a second reader who has not seen the draft and ask them to say in one sentence what it means. If their sentence differs from what you meant, rewrite the line, then run `validate_copy.py` again.
