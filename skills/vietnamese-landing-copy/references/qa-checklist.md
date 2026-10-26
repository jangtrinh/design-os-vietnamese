<!-- vlc-disable: all -->

# QA Checklist & Peer Review Rubric (`vietnamese-landing-copy`)

Automated CLI linters (`validate_copy.py`) catch deterministic defects such as decomposed Unicode NFD, unaccented slang, period/comma numbering faults, and unannotated advertising superlatives. However, persuasive nuance, emotional resonance, and brand register alignment require human editorial evaluation.

Every production landing page must score at least **4 out of 5** across all six dimensions below prior to public deployment.

---

## 1. Register & Audience Pragmatics

- [ ] **Unified Pronoun Axis (`PRO001` / `PRO002`):** The entire landing page maintains exactly one consistent register. Hero, features, customer reviews, FAQs, forms, and footer never vacillate between `bạn`, `Quý khách`, and `Anh/Chị`.
- [ ] **Institutional Self-Reference:** The organization speaks consistently as `chúng tôi` (exclusive "we"), never inclusive `chúng ta`, unless inviting the user into a community manifesto.
- [ ] **Sino-Vietnamese (Hán-Việt) Density:**
  - Real Estate & Wealth Management: 65–75% Hán-Việt ratio (*kiến tạo, chốn an cư, đắc địa*).
  - SaaS & Developer Tools: 25–35% Hán-Việt ratio; predominantly active Thuần Việt verbs.
- [ ] **Zero Direct Address with Common Nouns:** The copy avoids talking to the visitor using third-person nouns like *"Khách hàng hãy bấm vào đây"* (rewrite as direct imperative or `Quý khách vui lòng...`).

---

## 2. Idiomaticity & Syntactic Naturalness

- [ ] **Noun-Modifier Order:** Modifiers follow nouns throughout (`căn hộ cao cấp`, `giải pháp toàn diện`, never `cao cấp căn hộ`).
- [ ] **Active Voice Recasting:** English passive frames (*"designed by"*, *"built by"*) are recast as active agent constructions (*"Do kiến trúc sư danh tiếng thiết kế"* or *"Công ty X kiến tạo"*).
- [ ] **Zero Calqued Idioms:** No verbatim translations of English clichés like `ở cuối ngày` (*at the end of the day*), `giải pháp một cửa` (*one-stop solution*), or `thay đổi trò chơi` (*game changer*).
- [ ] **Classifier Precision:** Tangible items carry natural Vietnamese classifiers (`căn hộ`, `toà tháp`, `nền đất`, `bản cập nhật`, `gói dịch vụ`).
- [ ] **Rhythmic Cadence:** Sentences flow naturally when read aloud; clauses use natural connective particles (*đồng thời, nhờ đó, qua đó*) rather than stacked English prepositions.

---

## 3. CTA & Conversion Architecture

- [ ] **Settled Conventional Vocabulary:** All CTAs adhere to the canonical conversion glossary ([glossary.md](glossary.md)):
  - SaaS: `Bắt đầu ngay`, `Dùng thử miễn phí`, `Đặt lịch demo`.
  - Real Estate: `Đăng ký nhận báo giá`, `Tải trọn bộ mặt bằng`, `Đặt hẹn tham quan nhà mẫu`.
  - E-Commerce: `Mua ngay`, `Thêm vào giỏ hàng`, `Khám phá ngay`.
- [ ] **Zero English Particles:** No calqued prepositions on verbs (e.g. `Đăng ký lên`, `Bắt đầu được`).
- [ ] **Mobile Touch Target & Expansion:** Button text accommodates 25–30% string expansion without wrapping awkwardly or truncating at 375px mobile viewport.

---

## 4. Legal & Regulatory Compliance

- [ ] **Superlative Substantiation (`LAW001`):** No unverified ranking claims (`số 1`, `tốt nhất`, `duy nhất`, `hàng đầu`) appear without a valid certified market survey (Luật Quảng cáo Điều 8 khoản 11).
- [ ] **Proof Annotations:** Valid claims carry `<!-- proof: ... -->` naming the survey authority and certificate date.
- [ ] **Comparative Advertising:** No competitor is disparaged or mentioned by name (Luật Cạnh tranh 2018).
- [ ] **PDPA Lead Form Consent (`LND002`):**
  - Unchecked checkbox for data processing.
  - Clear statement of purpose (*"nhằm mục đích tư vấn sản phẩm"*).
  - Visible link to `Chính sách bảo mật`.
  - Dual-checkbox architecture separating inquiry processing from marketing newsletters.
- [ ] **E-Commerce Statutory Footer (`LND003`):** Complete corporate name, Tax ID (MST), registered headquarters address, hotline, and MOIT registration status (Nghị định 52/2013/NĐ-CP & 85/2021/NĐ-CP).
- [ ] **Real Estate Disclaimers:** Visual renders marked with `Hình ảnh mang tính chất minh họa`; prices state VAT and maintenance fee conditions.

---

## 5. Locale Formatting & Number Discipline

- [ ] **Number Grouping (`NUM001` / `NUM002`):** Thousands grouped with periods (`50.000 ₫`, `1.200.000 ₫`); decimals separated by commas (`2,5 ha`, `12,5%`).
- [ ] **Pricing Scale Uniformity (`LND004`):** Pricing tables do not mix period-grouped numbers with colloquial word scales in the same table, and billing periods use `/tháng` or `/năm` (never `/month`).
- [ ] **Area Units (`NUM004`):** Superscript units used (`m²`, `m³`, `km²`), never plain ASCII `m2` or `m3`.
- [ ] **Dates & Times (`DATE001`):** Dates follow `dd/MM/yyyy` (e.g. `15/08/2026`); times follow 24-hour notation (`14:30`).
- [ ] **Phone Numbers (`PHONE001`):** Standard domestic format `0912 345 678` or international format `+84 912 345 678` (never `+84 0912...`).

---

## 6. Typography & Web Font Rendering

- [ ] **Precomposed NFC Unicode (`NFC001`):** All output verified as canonical NFC Unicode.
- [ ] **Consistent Tone Mark Placement (`TONE001`):** Entire document strictly adheres to either *kiểu mới* (`hoà`, `thuỷ`) or *kiểu cũ* (`hòa`, `thủy`).
- [ ] **Full Font Subsetting:** Web fonts include the complete Latin Extended-B set; no fallback glyph replacement or misaligned stacked diacritics (`ễ`, `ệ`, `ộ`, `ữ`, `ỹ`).
- [ ] **HTML Locale Tag:** Document root contains `<html lang="vi">`.

---

## Reviewer Sign-Off Matrix

| Evaluation Dimension | Passing Score | Assigned Reviewer | Status / Notes |
|---|:---:|---|---|
| 1. Register & Pragmatics | 4 / 5 | Lead Copywriter | |
| 2. Idiomaticity & Syntax | 5 / 5 | Native Vietnamese Editor | |
| 3. CTA & Conversion Flow | 4 / 5 | Growth / CRO Specialist | |
| 4. Legal & Regulatory | 5 / 5 | Legal / Compliance Officer | |
| 5. Locale & Number Rules | 5 / 5 | QA Automation (`validate_copy.py`) | |
| 6. Typography & Rendering | 5 / 5 | Frontend Engineer | |
