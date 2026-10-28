<!-- synced from shared/references/compliance.md (6c1e774e5aef3c8d) — edit shared/ source, not this copy -->
<!-- vlc-disable: TONE001, DIA001, LAW001 -->

# Statutory & Regulatory Compliance Reference (`design-os-vietnamese`)

Shared across every skill in `design-os-vietnamese`. In Vietnam, copywriting defects across marketing, e-commerce, data collection, finance, and education are governed by specific statutes and decrees with active administrative enforcement.

> **Disclaimer:** This reference is an engineering and copywriting quality-assurance guide, not formal legal counsel. Its purpose is to catch statutory defects before copy reaches legal/compliance sign-off.

---

## 1. Advertising Superlatives & Influencer Disclosure

### A. Superlative & Unproven Ranking Claims (`LAW001`)
- **Statute:** **Điều 8 Khoản 11, Luật Quảng cáo 16/2012/QH13** (as amended by **Luật số 75/2025/QH15**, effective **01/01/2026**).
- **Rule:** Prohibits advertising using the words `nhất`, `duy nhất`, `tốt nhất`, `số một` (`số 1`), `hàng đầu`, `đầu tiên`, `bán chạy nhất`, `rẻ nhất`, `uy tín nhất`, or words of equivalent meaning **without lawful documentary proof** (market survey from a licensed research organization, official competition award, or state certification).
- **Remediation:**
  1. Replace with a verifiable, countable metric: *"Được hơn 25.000 doanh nghiệp tin dùng"* instead of *"Giải pháp số 1 Việt Nam"*.
  2. If lawful documentary proof exists, attach an inline proof annotation so `validate_copy.py` records the citation:
     ```markdown
     Thương hiệu máy lọc nước bán chạy số 1 Việt Nam <!-- proof: Báo cáo Euromonitor International 2025, chứng nhận ngày 15/03/2026 -->
     ```
- **Negation Guard:** Negative phrases (*"không phải là số 1"*, *"chưa phải tốt nhất"*) are not superlative claims and are exempted by `validate_copy.py`.

### B. KOL / KOC & Sponsored Content Disclosure (New from 01/01/2026)
- **Statute:** **Luật sửa đổi, bổ sung một số điều của Luật Quảng cáo (Luật số 75/2025/QH15)**.
- **Rule:** Influencers (người chuyển tải sản phẩm quảng cáo) must:
  1. Explicitly disclose sponsored/advertising content before or during the post/video/livestream (`#QuảngCáo`, `#Ad`, `Nội dung được tài trợ bởi [Thương hiệu]`).
  2. Verify claims against official product documentation and **not endorse products/services they have not directly used or verified** (especially in healthcare, cosmetics, nutrition, and finance).

---

## 2. Personal Data Protection & Consent (`PROD004`)

- **Statute (from 01/01/2026):** **Luật Bảo vệ dữ liệu cá nhân số 91/2025/QH15** & **Nghị định 356/2025/NĐ-CP** (detailing the Law). **Nghị định 13/2023/NĐ-CP is no longer in force** from 01/01/2026 (NĐ 356/2025 Điều 42 khoản 2); cite it only as history. Processing already under way that was consented or agreed under NĐ 13/2023 before that date continues without new consent (Luật 91/2025 Điều 39 khoản 1).
- **Mandatory Lead-Form & Onboarding Requirements:**
  1. **Express, Purpose-Bound Consent (Luật 91/2025 Điều 9):** Consent copy must explicitly state **what data** is collected and **for what specific purpose** (`nhằm mục đích...` / `để phục vụ...`), and link to the full `Chính sách bảo mật` / `Chính sách bảo vệ dữ liệu cá nhân`.
  2. **No Pre-Ticked Boxes or Silence:** Silence or non-response is **not** valid consent (Luật 91/2025 Điều 9 khoản 4 điểm d). Default-on consent is banned (NĐ 356/2025 Điều 6 khoản 3). Checkboxes must render unchecked by default.
  3. **Unbundled Marketing Consent:** Transactional/service processing consent must be separated from promotional/marketing consent (use two independent checkboxes when both apply).
  4. **Children's Personal Data (Luật 91/2025 Điều 24):** The legal representative exercises the child's data rights. To **publish or disclose** private-life information of a child **aged 7 or older**, get **Double Consent (Sự đồng ý kép)**: the child **AND** the legal representative (`người đại diện theo pháp luật`). The Law sets no upper age bound in that clause (the former "7 to under 16" rule came from NĐ 13/2023 Điều 20). Verify age before collection.

---

## 3. Promotions, Discounts, and Anti-Spam

### A. Promotional Discount Ceiling (`MKT002`)
- **Statute:** **Nghị định 81/2018/NĐ-CP**, as amended by **Nghị định 128/2024/NĐ-CP** (effective 01/12/2024).
- **Rule:** Maximum promotional discount is **50%** of the price immediately preceding the promotion period.
- **Exemption (Up to 100%):** Allowed **only** within a state-organized or state-certified concentrated promotion program (`chương trình khuyến mại tập trung`, e.g., Vietnam Grand Sale, municipal promotional months) or stabilization programs. Annotate with:
  ```markdown
  Ưu đãi giảm giá lên đến 80% <!-- khuyen-mai-tap-trung: Quyết định số 1820/QĐ-BCT Tháng khuyến mại tập trung quốc gia 2026 -->
  ```

### B. Anti-Spam & Telemarketing Windows (`SPAM001`)
- **Statute:** **Nghị định 91/2020/NĐ-CP chống tin nhắn rác, thư điện tử rác, cuộc gọi rác**.
- **Rules:**
  - Prior opt-in required; zero messages/calls to numbers on the national `Danh sách không quảng cáo` (DoNotCall list).
  - **Time Windows:** Advertising SMS/ZBS only **07:00–22:00**; advertising voice calls only **08:00–17:00**.
  - **Frequency Caps:** Max **3 advertising SMS**, **3 advertising emails**, and **1 advertising call** per recipient per 24 hours.
  - **Mandatory Opt-Out (`SPAM001`):** Every promotional message must include a clear, functional refusal instruction (e.g., *"Soạn TC gửi [Đầu số]"* or *"Nhấn vào đây để hủy nhận tin"*).

---

## 4. E-Commerce Website & App Footer Disclosures (`LND004`)

- **Statute:** **Nghị định 52/2013/NĐ-CP** as amended by **Nghị định 85/2021/NĐ-CP** on E-Commerce.
- **Mandatory Footer Information on Any Commercial Landing Page or Web App:**
  1. Full legal entity name (`Tên doanh nghiệp / hộ kinh doanh`).
  2. Registered head-office address (`Địa chỉ trụ sở chính`).
  3. Business Registration Certificate number / Tax Code (`Mã số doanh nghiệp / MST`, date & place of issuance).
  4. Contact phone number and email (`Số điện thoại và email liên hệ`).
  5. Links to `Chính sách bảo mật`, `Điều khoản sử dụng`, `Chính sách vận chuyển / đổi trả / thanh toán`.
  6. Ministry of Industry and Trade badge: `Đã thông báo Bộ Công Thương` (for sales websites) or `Đã đăng ký Bộ Công Thương` (for e-commerce marketplaces/platforms).

---

## 5. Clerical & Administrative Document Standard (`ADMIN001`)

- **Statute:** **Nghị định 30/2020/NĐ-CP về công tác văn thư**.
- **Mandatory Header & Structural Rules for Official `Công văn`, `Tờ trình`, `Quyết định`, `Thông báo`:**
  1. **Quốc hiệu & Tiêu ngữ:**
     - Line 1 (ALL CAPS, bold): `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`
     - Line 2 (Title/Sentence case, bold, centered solid underline): `Độc lập - Tự do - Hạnh phúc` (with spaced hyphens `-`).
  2. **Date Line:** `..., ngày DD tháng MM năm YYYY` (zero-padded days `01`–`09` and months `01`, `02`).
  3. **Signing Authority Abbreviations:** `TM.` (Thay mặt tập thể), `KT.` (Ký thay người đứng đầu), `TL.` (Thừa lệnh), `TUQ.` (Thừa ủy quyền).
  4. **Recipient Block (`Nơi nhận`):** Must end with `- Lưu: VT, [Tên đơn vị soạn thảo].`

---

## 6. 7-Tier Education & Pedagogy Continuum (`EDU001`–`EDU012`)

- **Preschool (`Mầm non` — VBHN 01/VBHN-BGDĐT):** Nurseries (3–36 months, 4 domains) and Kindergartens (3–6 years, 5 domains: *Thể chất, Nhận thức, Ngôn ngữ, Tình cảm - Kỹ năng xã hội, Thẩm mỹ*). Strictly forbids numeric scores (`9/10`) or `Học lực Giỏi/Khá/Yếu/Kém` rankings; evaluates end-of-age developmental expectations (`Đạt` / `Chưa đạt`) and WHO growth charts.
- **Primary (`Tiểu học` — Thông tư 27/2020/TT-BGDĐT):** 3 subject levels (`Hoàn thành tốt — Hoàn thành — Chưa hoàn thành`), 3 competency/quality levels (`Tốt — Đạt — Cần cố gắng`), and 2 commendation titles (`Học sinh Xuất sắc`, `Học sinh Tiêu biểu`). Abolishes `Học sinh Tiên tiến` at primary level.
- **Secondary (`THCS & THPT` — Thông tư 22/2021/TT-BGDĐT):** 4 levels (`Tốt — Khá — Đạt — Chưa đạt`) for both learning and conduct.
- **Vocational (`GDNN` — Luật GDNN & Thông tư 04/2022/TT-BLĐTBXH) & Higher Education (VQF Bậc 6–8, QĐ 1982/QĐ-TTg):**
  - Undergraduate (`Đại học`, TT 08/2021/TT-BGDĐT): culminates in `Khóa luận tốt nghiệp` or `Đồ án tốt nghiệp`.
  - Master's (`Thạc sĩ`, TT 23/2021/TT-BGDĐT): culminates in research `Luận văn thạc sĩ` or applied `Đề án thạc sĩ`.
  - Doctoral (`Tiến sĩ`, TT 18/2021/TT-BGDĐT): `Nghiên cứu sinh (NCS)` completes `Chuyên đề tiến sĩ`, WoS/Scopus publications, and defends `Luận án tiến sĩ`.
  - State Academic Ranks (QĐ 37/2018/QĐ-TTg): `Giáo sư (GS.)` and `Phó Giáo sư (PGS.)` are academic ranks (`chức danh / học hàm`), whereas `TS.`, `ThS.`, `CN.` are academic degrees (`học vị`). Place rank before degree (`GS.TS.`, `PGS.TS.`).

---

## 7. Healthcare, Pharmaceuticals, TPCN & EMR (`MED001`–`MED007`)

- **Luật Khám bệnh, chữa bệnh 15/2023/QH15** (effective 01/01/2024): Replaces `Chứng chỉ hành nghề khám bệnh, chữa bệnh` with `Giấy phép hành nghề khám bệnh, chữa bệnh`.
- **Nghị định 15/2018/NĐ-CP & Thông tư 05/2018/TT-BYT (TPCN):** Dietary supplements (`Thực phẩm bảo vệ sức khỏe`) must carry the exact disclaimer: *"Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh"*, and must never claim therapeutic cure (`điều trị dứt điểm`, `chữa khỏi hoàn toàn`) or use patient thank-you letters / physician endorsements.
- **Thông tư 32/2023/TT-BYT (EMR) & Thông tư 52/2017/TT-BYT (Đơn thuốc):** Requires clear INN active ingredient, dosage, route, timing (`trước ăn` / `sau ăn`), and emergency red-flag return instructions (`Dấu hiệu cần tái khám ngay`).

---

## 8. Civil, Commercial & Consumer Contracts (`LEG001`–`LEG007`)

- **Luật Thương mại 2005 (Điều 301):** Caps contractual breach penalties (`phạt vi phạm`) in commercial contracts at **8%** of the value of the breached obligation (contrasting with civil contracts under Article 418 of `Bộ luật Dân sự 2015`).
- **Bộ luật Lao động 2019 (Điều 20):** Abolished seasonal labor contracts (`hợp đồng lao động mùa vụ`); recognizes only indefinite-term and fixed-term (`<= 36 months`) contracts.
- **Luật Bảo vệ quyền lợi người tiêu dùng 2023 (Điều 25):** Voids standard-form contract clauses that unconditionally waive statutory business liability.
- **Vietnamese Legislative Citation Hierarchy:** Cite from specific to general (`Điểm a Khoản 2 Điều 15`), never Anglo-American `Điều 15.2(a)`.

---

## 9. Hospitality, Tourism, Aviation & F&B (`HOS001`–`HOS006`)

- **Luật Du lịch 2017 (Điều 50):** Official tourist accommodation ratings span **1 to 5 stars** only (`1–5 sao`) by state appraisal decision; self-proclaimed `6 sao` or `7 sao` claims are prohibited.
- **Net vs `++` Pricing:** Any `++` price must explicitly disclose the service charge (`5% phí phục vụ`) and VAT (`8%` or `10% thuế GTGT`).
- **Thông tư 14/2015/TT-BGTVT & Thông tư 19/2023/TT-BGTVT (Aviation):** Flight delay/cancellation notices must include an explicit apology, reason, updated schedule, and passenger care/refund/rebooking rights.

---

## 10. HR, Recruitment & Labor Code (`HR001`–`HR006`)

- **Bộ luật Lao động 2019 (Điều 8 & Điều 17):** Prohibits gender, marital, pregnancy, or arbitrary age discrimination in JDs, and forbids retaining original identity cards/diplomas (`giữ bằng gốc`) or demanding cash deposits (`đặt cọc đi làm`).
- **Bộ luật Lao động 2019 (Điều 25 & Điều 26):** Probation duration capped at `180 ngày` (enterprise managers), `60 ngày` (college/university degrees), `30 ngày` (intermediate/technical), and `6 ngày làm việc` (other roles); probation salary must be at least **85%** of the official salary.
