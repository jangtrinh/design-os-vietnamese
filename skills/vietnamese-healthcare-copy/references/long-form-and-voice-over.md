<!-- synced from shared/references/long-form-and-voice-over.md (246582b4ecd37ed5) — edit shared/ source, not this copy -->
<!-- vlc-disable: all -->

# Long-form articles and voice-over scripts (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. Use this page when you write or edit a Vietnamese piece that people read from start to end, or listen to: an article, an explainer, a data story, a newsletter, a case study, or the script a voice reads over a video. It covers what the validator cannot see: whether the piece makes its point, whether each sentence reads like Vietnamese, and whether a spoken line sounds like a person talking.

It works together with three other pages:

- [plain-vietnamese.md](plain-vietnamese.md) checks the form of each sentence (`PLAIN001`–`PLAIN007`) and gives the four-question reading check in its section 6. This page does not repeat that check.
- The skill's `code-switching.md` or `glossary.md` decides which language a term is in. This page decides whether the sentence around the term can be understood.
- [register-matrix.md](register-matrix.md) and [context-matrix.md](context-matrix.md) decide the voice and how the reader is addressed.

> **Evidence class: `proposed`.** Taken from a human editor's corrections on published Vietnamese long-form pieces and a narrated video (2026-11). Every one of them passed `validate_copy.py --strict` with zero findings before the corrections. Sources for the sentence-rhythm rules are listed in section 6.

## 1. The rule above the others

`0 errors · 0 warnings` means the words follow the rules. It does not mean the text is clear. Before anyone else reads a draft, read every sentence once as a reader who has never seen the project, with the rules below. Then run the validator.

## 2. Shape of the piece

1. **The title carries the thesis, never the example.** A worked example (one Button, one order, one ward) may open a section, but the title, the deck and the closing sentence state the whole picture. Say once, early, that the example stands for a larger set. A title built around the example makes the piece look smaller than it is.
2. **A deck of one or two sentences sits under the title**, with one to three hard numbers.
3. **Open with something the reader can see**: a concrete scene, or one number made relatable, before any abstraction. Mark an invented scene as "ví dụ minh họa".
4. **Length serves the reader.** An explainer runs about 1.200 to 2.500 words, with a heading every 600 to 1.200 words. Cut repetition first. Never cut a caveat to save words.
5. **Caveats sit next to the number they qualify**, or in the methods note ("Về dữ liệu", "Cách làm"). Do not add a separate section that lists unfinished work and conditional numbers: it reads as an apology and pulls each caveat away from the claim it belongs to.
6. **Credit generated images and video with the exact tool and model**: "các hình minh họa tạo bằng AI trên <công cụ>, ảnh tĩnh bằng model <tên model> và clip bằng model <tên model>". A wrong or vague model name is a factual error.

## 3. Sentences

1. **Headings, table titles, chart titles, card labels and captions are full sentences** (or full questions), even when short. A reader should get them on the first read without the body.

   | Trước | Sau |
   |---|---|
   | Thư viện đủ, lựa chọn vẫn sai | Design system có đủ component, nhưng agent vẫn chọn sai Button |
   | Cần biết: Component, variant, size, state. | Cần biết: Button thuộc component nào, có những variant, size và state nào. |
   | Nó là gì? | Button này là gì? |

2. **Every sentence has someone doing something to something.** No sentence made only of nouns, no verb without a subject, no note-style "X: Y." in place of a sentence.

   | Trước | Sau |
   |---|---|
   | Rule icon: Export nhận một leading icon khớp hành động. | Nhờ rule icon, Export nhận một leading icon khớp với hành động. |
   | Một khối chữ lớn không kiểm tự động được độ phủ, độ mới. | Với một khối chữ lớn như vậy, không có cách tự động kiểm xem tài liệu đã phủ đủ chưa, còn mới không. |

3. **A colon only opens a list or a quote; it never replaces a verb.** At most one colon per sentence. Split a chain such as "A: B; C: D" into sentences.
4. **Link sentences with words that carry meaning, and keep the subject steady.** Use "vì", "nên", "nhưng", "còn", "vậy mà", "nhờ vậy", "vì vậy" so the reader sees how the next sentence stands to the last. Repeat the main noun of the previous sentence; repeating a key word is how Vietnamese prose links, not a fault.

   | Trước | Sau |
   |---|---|
   | Khoảng cách đó đo được. | Khoảng cách giữa một design system đầy đủ và một trang làm đúng có thể đo bằng số. |

5. **Do not carry English sentence frames over.** Drop "được" passives when the doer is clear, and the frames "việc … là …", "điều tương tự đúng với", "X thắng Y", a bare "lý do là". Do not use a private metaphor that only the writer understands; say the plain thing.

   | Trước | Sau |
   |---|---|
   | Nó được viết cho designer và dev đọc. | Người ta viết nó cho designer và dev đọc. |
   | Điều tương tự đúng với mọi component. | Chuyện xảy ra với Button cũng xảy ra với mọi component. |
   | Bản mới thắng bản cũ. | Khi hai bản cùng nói về một việc, bản mới được dùng. |

6. **Rhythm: a short sentence states the fact, then a longer one says what it means.** Never leave three clipped sentences in a row. Read aloud: a sentence that needs two breaths is split, a sentence that sounds cut off is joined to its neighbour.

   | Trước | Sau |
   |---|---|
   | Một Button nối với tài liệu, token, rule và slot. Dễ nhìn, dễ lần theo từng quan hệ. | Một Button chỉ nối với tài liệu, token, rule và slot, nên cụm này dễ nhìn và lần theo được từng quan hệ. |

7. **Name the thing instead of an empty pointer.** "Đây", "đó", "điều này" and "nó" at the start of a sentence only work when the previous sentence has exactly one noun they can point to. Otherwise name it.

   | Trước | Sau |
   |---|---|
   | Đây là câu design system trả lời được. | Design system trả lời được câu này. |
   | Vì gate này chưa được viết, nó vẽ nét đứt. | Gate này chưa được viết, nên sơ đồ vẽ nó bằng nét đứt. |

8. **Sharp numbers, calm words.** A sentence with a number says the number, its unit and what it counts, and at most two numbers per sentence. The meaning goes in the next sentence in ordinary words. Add no emotional adjective; the concrete detail carries the judgement.
9. **Explain every term where it first appears**, in the same sentence, in everyday words, including terms the glossary keeps in English: "gate, tức một bước kiểm tự động trong lúc build, sai thì build dừng". Put at most two English nouns in a row.
10. **Design, product and engineering terms that the trade uses in English stay in English** (Button, variant, slot, screen, rule, scope, token, workflow, agent, skills). The sentence around them stays Vietnamese, and so do ordinary words that have a natural Vietnamese form (câu hỏi, lý do, dự án, triệu chứng). Do not swap an everyday Vietnamese word for English: "tám câu hỏi", not "tám question".

## 4. Voice-over scripts

A voice-over is heard once, at the speaker's pace, with no way to re-read. The rules in section 3 still hold; these come on top.

1. **Explain; never telegraph.** Each line is a full conversational sentence with its reasoning in it, as if talking a colleague through the idea. A line that reads like a slide bullet sounds clipped.

   | Trước | Sau |
   |---|---|
   | Design system viết cho người đọc. AI cần thêm một layer ontology. | Có điều design system được viết cho người đọc, nên chỗ nào thiếu thì người tự hỏi đồng nghiệp hoặc nhớ lại lần review trước. Agent thì không làm vậy được. |

2. **Length follows the explanation, not a target duration.** If the script cannot explain the point in the time asked for, report the real length and let the requester choose. Do not cut the reasoning to hit a number of seconds.
3. **One idea per beat**: two to four sentences, about 10 to 25 seconds spoken. **Each beat opens by linking to the one before** ("Chuyện này dẫn tới…", "Cái fail này nằm ở chỗ…", "Thử nhìn lại…").
4. **No phrase is repeated across a beat boundary.** "…qua một ví dụ nhỏ." followed by "Lấy một ví dụ nhỏ." is heard as a stutter.
5. **Open on what the audience already hears, then ask the question.** A pattern that works: everyone talks about X, yet Y still fails; here is why. Then the worked example, then the thesis, then where to read the full piece.
6. **Numbers are rounded and spoken as words**: one or two in a one-minute script ("hơn một nghìn sáu trăm", "gần một phần năm"). They must match the article they introduce. Do not re-read the article.
7. **Slang in a brief is softened in the script; the meaning stays.** A brief that says "fail lòi" becomes "vẫn cứ fail" on air.
8. **Write for the text-to-speech engine.** Join English compounds without a hyphen ("anti flop skills", not "anti-flop", which makes the voice pause mid-word). Spell a domain the way it is said ("design os chấm vn"). Write numbers as words.
9. **Check what the voice actually said.** Run speech-to-text on the final mix and compare it word for word with the script. Regenerate any line that differs, has a pause in the wrong place or repeats a phrase.

## 5. How to run the pass

1. Extract every string a reader sees or hears: title, deck, headings, table headers and cells, list items, captions, body sentences, spoken lines.
2. Mark each one CLEAR or UNCLEAR with the reason: slogan, abstract, calque, unexplained term, stacked nouns, no subject, clipped, missing link word.
3. Rewrite every UNCLEAR string. Keep numbers, sources, caveats and quotes unchanged.
4. Report the before and after of every heading and table title, and of at least ten body sentences.
5. Run `validate_copy.py --strict`. A finding that conflicts with a plain, correct sentence is reported, not obeyed blindly.
6. Say plainly when no native reader other than the writer has read the text.
7. For a voice-over, read the script aloud before generating audio, and run step 9 of section 4 after.

## 6. Sources for the sentence-rhythm rules

Rules 2 to 8 of section 3 were drawn from how critics describe the prose of the writer Nguyễn Ngọc Tư, then turned into rules for non-fiction. No sentence, image or dialect of the writer is copied: the voice stays standard Vietnamese, because dialect works in a character's mouth and non-fiction has no characters speaking.

- Đào Duy Hiệp, "Chất thơ trong Cánh đồng bất tận", VnExpress: rhythm comes from repeating key words across layers. Used for rules 4 and 6. https://vnexpress.net/chat-tho-trong-canh-dong-bat-tan-1974018.html
- Nguyễn Thị Hoài Phương, "Biểu thức quy chiếu 'người phụ nữ' trong một số truyện ngắn của Nguyễn Ngọc Tư từ góc nhìn của phân tích diễn ngôn", Tạp chí Khoa học và Công nghệ, Trường Đại học Khoa học, Đại học Huế, 15(3), 2020: people and things are named by a noun with a concrete description, without judgement. Used for rules 7 and 8. https://jos.husc.edu.vn/UPLOADS/numbers/34/553_fulltext_1.Van%20-%20Phuong%20-%20Nguyen%20Thi%20Hoai%20Phuong.pdf
- Phạm Thị Lương, "Truyện ngắn đồng bằng sông Cửu Long mười năm đầu thế kỷ XXI", Tạp chí Khoa học Trường Đại học Cần Thơ, 57(1C), 2021: each sentence reads like someone telling the reader a story, not a note. Used for rules 2 and 6. https://ctujsvn.ctu.edu.vn/index.php/ctujsvn/article/download/3771/48/48
- Bình (2009), Ngôn ngữ & Đời sống: more than 200 regional words in the writer's short stories, mostly in characters' speech. This is why the rules take rhythm and leave dialect out. https://vjol.info.vn/NNDS/article/download/10189/9348/
