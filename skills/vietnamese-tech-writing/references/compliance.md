<!-- synced from shared/references/compliance.md (5fcb218b6711e039) — edit shared/ source, not this copy -->
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

- **Statute:** **Nghị định 13/2023/NĐ-CP về Bảo vệ dữ liệu cá nhân (PDPD)** & **Luật Bảo vệ dữ liệu cá nhân**.
- **Mandatory Lead-Form & Onboarding Requirements:**
  1. **Express, Purpose-Bound Consent (Điều 11):** Consent copy must explicitly state **what data** is collected and **for what specific purpose** (`nhằm mục đích...` / `để phục vụ...`), and link to the full `Chính sách bảo mật` / `Chính sách bảo vệ dữ liệu cá nhân`.
  2. **No Pre-Ticked Boxes or Silence:** Silence or non-response is **not** valid consent. Checkboxes must render unchecked by default.
  3. **Unbundled Marketing Consent:** Transactional/service processing consent must be separated from promotional/marketing consent (use two independent checkboxes when both apply).
  4. **Children's Personal Data (Điều 20):** For children aged **7 to under 16**, processing personal data requires **Double Consent (Sự đồng ý kép)**: verified consent from the child **AND** verified consent from a parent or legal guardian (`cha, mẹ hoặc người giám hộ hợp pháp`), plus age verification prior to collection.

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
