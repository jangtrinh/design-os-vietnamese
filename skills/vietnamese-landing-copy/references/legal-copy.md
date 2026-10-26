<!-- vlc-disable: all -->

# Statutory Copy, Disclaimers & Regulatory Compliance (`vietnamese-landing-copy`)

*Disclaimer: This guide synthesizes current Vietnamese statutory requirements for digital marketing surfaces and landing pages. It does not substitute for licensed legal counsel.*

---

## 1. Personal Data Protection: Nghị định 13/2023/NĐ-CP

Enacted by the Government of Vietnam on 17/04/2023 and effective from **01/07/2023**, Nghị định 13/2023/NĐ-CP establishes comprehensive data privacy obligations across all digital surfaces collecting personal information from Vietnamese citizens.

### Core Legal Principles (Điều 11 & Điều 12)
1. **Consent Must Be Voluntary & Explicit:** Pre-ticked checkboxes (`ô đánh dấu sẵn`) are strictly void. The user must perform an affirmative act (tick an unchecked box or click a dedicated confirmation button).
2. **Specific Purpose Requirement:** Generic claims like *"để nâng cao chất lượng dịch vụ"* without naming the specific business purpose fail statutory standards.
3. **Right to Withdraw:** The data subject must be explicitly informed of their right to withdraw consent and request data deletion at any time.
4. **The Dual-Checkbox Mandate:** Consent to process data for an enquiry or transaction **cannot be bundled** with consent to receive promotional marketing or third-party advertising.

### Production Lead-Form Templates

#### Template 1: SaaS / Tech Platform (Register `saas`)
```html
<div class="lead-form-consent">
  <!-- Checkbox 1: Mandatory Service Processing -->
  <label class="consent-item">
    <input type="checkbox" required name="consent_service" />
    <span>
      Tôi đồng ý để [Tên Công Ty] thu thập và xử lý thông tin cá nhân của tôi
      theo <a href="/chinh-sach-bao-mat">Chính sách bảo mật</a> nhằm mục đích
      tạo tài khoản và tư vấn giải pháp.
    </span>
  </label>

  <!-- Checkbox 2: Optional Marketing Communications -->
  <label class="consent-item">
    <input type="checkbox" name="consent_marketing" />
    <span>
      Tôi đồng ý nhận thông tin cập nhật tính năng, bài viết chuyên môn và ưu đãi
      từ [Tên Công Ty] qua email hoặc điện thoại (tùy chọn, có thể hủy bất kỳ lúc nào).
    </span>
  </label>
</div>
```

#### Template 2: Real Estate & Luxury Hospitality (Register `re`)
```html
<div class="lead-form-consent">
  <label class="consent-item">
    <input type="checkbox" required name="consent_re_advisory" />
    <span>
      Tôi xác nhận đồng ý để Chủ đầu tư và Đơn vị phân phối chính thức liên hệ tư vấn
      thông tin dự án [Tên Dự Án], đồng thời xử lý dữ liệu cá nhân của tôi theo
      <a href="/chinh-sach-bao-mat">Chính sách bảo mật</a>. Tôi hiểu rằng tôi có quyền
      rút lại sự đồng ý bất cứ lúc nào bằng cách liên hệ hotline hoặc gửi yêu cầu qua email.
    </span>
  </label>
</div>
```

#### Template 3: Consultative B2B Enterprise (Register `b2b`)
```html
<div class="lead-form-consent">
  <label class="consent-item">
    <input type="checkbox" required name="consent_b2b_proposal" />
    <span>
      Tôi đồng ý để [Tên Doanh Nghiệp] liên hệ trao đổi nhu cầu và gửi báo giá chi tiết,
      đồng thời lưu trữ thông tin liên hệ theo đúng
      <a href="/chinh-sach-bao-mat">Chính sách bảo mật dữ liệu doanh nghiệp</a>.
    </span>
  </label>
</div>
```

---

## 2. E-Commerce & Commercial Footer Disclosures

Under **Nghị định 52/2013/NĐ-CP** (amended by **Nghị định 85/2021/NĐ-CP**), commercial websites and e-commerce landing pages must display verified corporate credentials in the page footer.

### Mandatory Footer Elements Checklist
- [x] Full corporate legal name (`Tên doanh nghiệp / Tên tổ chức`).
- [x] Enterprise Registration Code / Tax Code (`Mã số doanh nghiệp` or `MST`).
- [x] Date and issuing authority of the business license (`Ngày cấp, Nơi cấp`).
- [x] Headquarters address (`Địa chỉ trụ sở chính`).
- [x] Official contact phone number (`Số điện thoại liên hệ`) and email.
- [x] Full name of the person responsible for content (`Người đại diện theo pháp luật` or `Người chịu trách nhiệm nội dung`).
- [x] Ministry of Industry and Trade badge (`Logo Đã thông báo Bộ Công Thương` for standard websites, or `Logo Đã đăng ký Bộ Công Thương` for trading floors/marketplaces) linked directly to the public profile at `online.gov.vn`.

### Production Footer Template
```html
<footer class="site-footer">
  <div class="footer-legal-container">
    <p class="company-name"><strong>CÔNG TY CỔ PHẦN CÔNG NGHỆ DESIGN:OS VIỆT NAM</strong></p>
    <p>Mã số doanh nghiệp: 0108912345 do Sở Kế hoạch và Đầu tư TP. Hồ Chí Minh cấp ngày 15/03/2021</p>
    <p>Địa chỉ trụ sở: Tầng 18, Toà nhà Landmark 81, số 720A Điện Biên Phủ, Phường 22, Quận Bình Thạnh, TP. Hồ Chí Minh</p>
    <p>Hotline: 1900 6868 | Email: contact@design-os.vn</p>
    <p>Người đại diện pháp luật: Ông Nguyễn Văn An</p>
    
    <div class="moit-badge">
      <a href="http://online.gov.vn/Home/WebDetails/12345" target="_blank" rel="noopener noreferrer">
        <img src="/assets/logo-da-thong-bao-bo-cong-thuong.png" alt="Đã thông báo Bộ Công Thương" width="160" height="60" />
      </a>
    </div>

    <p class="copyright">© 2026 DESIGN:OS. Toàn bộ bản quyền được bảo lưu.</p>
  </div>
</footer>
```

---

## 3. Real Estate Project Disclaimers (Bất Động Sản)

Under **Luật Kinh doanh Bất động sản 2023** (effective 01/08/2024) and **Luật Nhà ở 2023**, property promotional copy must distinguish architectural renders from delivered physical construction to prevent misrepresentation liability.

### Standard Statutory Disclaimers

| Disclaimer Intent | Production Vietnamese Text | Mandatory Position |
|---|---|---|
| **Render Disclaimer** | `*Hình ảnh mang tính chất minh họa. Các chi tiết thiết kế và cảnh quan có thể được điều chỉnh theo phê duyệt của cơ quan có thẩm quyền.` | Placed directly beneath Hero renders, 3D floor plans, or model unit galleries |
| **Contractual Offer Hedge** | `*Thông tin và thông số kỹ thuật trên website chỉ mang tính chất tham khảo, không cấu thành đề nghị giao kết hợp đồng hoặc cam kết pháp lý chính thức từ Chủ đầu tư.` | Placed in the project summary or pricing overview section |
| **Pricing Suffix Hedge** | `*Giá bán dự kiến chưa bao gồm thuế GTGT (VAT) và 2% kinh phí bảo trì. Chính sách bán hàng áp dụng theo văn bản chính thức của Chủ đầu tư tại từng thời điểm.` | Placed beside headline prices and payment schedules |
| **Handover Schedule Hedge** | `*Thời gian bàn giao dự kiến: Quý IV/2027. Tiến độ thực tế có thể thay đổi tùy theo điều kiện thi công khách quan.` | Placed adjacent to progress updates |
| **Zoning & Masterplan Hedge** | `*Quy hoạch hạ tầng giao thông và tiện ích ngoại khu căn cứ theo đồ án quy hoạch tổng thể đã được cơ quan nhà nước có thẩm quyền phê duyệt.` | Placed near regional connectivity maps |

---

## 4. Healthcare, Medical & Cosmetics Disclaimers

Under regulations enforced by the Ministry of Health (Cục An toàn thực phẩm & Cục Quản lý Khám, chữa bệnh):

1. **Functional Foods & Supplements (Thực phẩm chức năng):**
   Every banner, video, and landing page must carry the verbatim statutory disclaimer:
   > *"Sản phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."*
2. **Cosmetic & Dermatological Claims:**
   - Prohibited terms: `Điều trị triệt để`, `Trị tận gốc nám`, `Khỏi 100% vĩnh viễn`.
   - Compliant terms: `Hỗ trợ làm mờ đốm nâu`, `Cải thiện sắc tố da`, `Được kiểm nghiệm da liễu`.
3. **Medical Clinics & Aesthetic Centers:**
   - Must state the official medical operating license:
     > *"Giấy phép hoạt động khám bệnh, chữa bệnh số [X]/BYT-GPHĐ do Bộ Y tế (hoặc Sở Y tế) cấp ngày [Ngày]."*
