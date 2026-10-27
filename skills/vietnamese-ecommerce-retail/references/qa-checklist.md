<!-- vlc-disable: all -->

# E-Commerce & Retail Pre-Publish QA Checklist (`design-os-vietnamese`)

This checklist is an authoritative quality gate for e-commerce merchandisers, digital marketing specialists, checkout UX designers, platform operations teams, and compliance officers prior to publishing product listings, running promotional campaigns, or launching checkout flows in Vietnam.

---

## Tier 1: Regulatory & Statutory Compliance Gate (P0 - Blocking)

- [ ] **1. Tính chuẩn xác biểu tượng Bộ Công Thương (`ECOM001`):**
  - Website bán hàng gắn đúng biểu tượng `Đã thông báo Bộ Công Thương` (màu xanh dương); Sàn giao dịch TMĐT gắn đúng biểu tượng `Đã đăng ký Bộ Công Thương` (màu đỏ) per Nghị định 52/2013/NĐ-CP và Nghị định 85/2021/NĐ-CP.
  - Tuyệt đối không xuất hiện các thông điệp gây nhầm lẫn: `Bộ Công Thương bảo chứng chất lượng 100%`, `Bộ Công Thương chứng nhận hàng chính hãng`.
- [ ] **2. Hạn mức giảm giá khuyến mại & giá trung thực (`ECOM002`):**
  - Tỷ lệ giảm giá khuyến mại **không vượt quá 50%** giá hàng hóa trước khuyến mại theo Nghị định 81/2018/NĐ-CP và Nghị định 128/2024/NĐ-CP (trừ chương trình khuyến mại tập trung quốc gia được cơ quan nhà nước phê duyệt).
  - Giá niêm yết trước khuyến mại là giá bán thực tế, không nâng khống giá gốc để tạo mức giảm giá ảo lừa dối khách hàng.
- [ ] **3. Chính sách đổi trả hợp pháp per Luật Bảo vệ quyền lợi người tiêu dùng 2023 (Luật BVQLNTD 2023) (`ECOM003`):**
  - Đã loại bỏ 100% các điều khoản vô hiệu tước đoạt quyền lợi người tiêu dùng: `Hàng mua rồi miễn đổi trả trong mọi trường hợp`, `Từ chối giải quyết đổi trả dưới mọi hình thức`.
  - Quy định rõ điều kiện đổi trả: Thời hạn (ví dụ: trong vòng 07 ngày), tình trạng sản phẩm (nguyên vẹn bao bì, lỗi do nhà sản xuất hoặc giao sai mẫu), và phương thức hoàn tiền.
- [ ] **4. Thông tin ghi nhãn hàng hóa bắt buộc trên PDP (`ECOM004`):**
  - Trang chi tiết sản phẩm (PDP) hiển thị đầy đủ các trường thông tin bắt buộc per Nghị định 43/2017/NĐ-CP và Nghị định 111/2021/NĐ-CP:
    - Tên hàng hóa
    - Xuất xứ hàng hóa (`Xuất xứ: [Tên quốc gia/vùng lãnh thổ]`)
    - Tên và địa chỉ của tổ chức, cá nhân chịu trách nhiệm về hàng hóa
    - Hạn sử dụng, định lượng, thành phần và thông tin cảnh báo (nếu có).
- [ ] **5. Loại bỏ hoàn toàn Dark Patterns & Coercive Messaging (`ECOM006`):**
  - Không có thông báo đe dọa trừ lương nhân viên giao hàng hoặc bắt shipper đền tiền nếu hủy đơn.
  - Không đe dọa khóa tài khoản trong 5 phút để ép người mua thanh toán vội.
  - Không tự động tích chọn đăng ký ngầm các gói hội viên trả phí tự động gia hạn (Forced Continuity / Sneak into basket).

---

## Tier 2: E-Commerce Fulfillment, Logistics & Payment Safety Gate (P1 - High)

- [ ] **6. Chuẩn hóa vòng đời trạng thái vận đơn (`ECOM005`):**
  - Trạng thái đơn hàng sử dụng từ ngữ chuẩn mực tiếng Việt: `Chờ xác nhận`, `Đang đóng gói`, `Đã bàn giao vận chuyển`, `Đang giao hàng`, `Giao hàng thành công / Hoàn tất đơn hàng`.
  - Thay thế hoàn toàn các calque dịch máy: `Ra ngoài để giao hàng` ➔ `Đang giao hàng`, `Sự hoàn thành đơn hàng` ➔ `Hoàn tất đơn hàng`.
- [ ] **7. Minh bạch điều kiện giao hàng & thanh toán COD:**
  - Quy định rõ quyền đồng kiểm ngoại quan (mở hộp kiểm tra tình trạng đóng gói bên ngoài) khi nhận hàng COD.
  - Biểu phí giao hàng hiển thị rõ ràng trước bước xác nhận đơn hàng, không phát sinh phụ phí ẩn khi giao nhận.
- [ ] **8. Cổng thanh toán & bảo mật thông tin thẻ:**
  - Tích hợp cổng thanh toán trực tuyến được Ngân hàng Nhà nước cấp phép, tuân thủ tiêu chuẩn bảo mật PCI-DSS.
  - Hiển thị đầy đủ thông tin hóa đơn điện tử (VAT) cho người mua doanh nghiệp có nhu cầu.

---

## Tier 3: Sociolinguistic & Microcopy Integrity Gate (P2 - Medium)

- [ ] **9. Loại bỏ 100% calque dịch thô tiếng Anh (`ECOM005`):**
  - Thay thế `thêm vào xe đẩy` / `bỏ vào giỏ xe` bằng `Thêm vào giỏ hàng`.
  - Thay thế `tiền mặt trên giao hàng` bằng `Thanh toán khi nhận hàng (COD)`.
  - Thay thế `chính sách trở lại` bằng `Chính sách đổi trả`.
  - Thay thế `người vận chuyển cuối cùng` bằng `Đơn vị vận chuyển chặng cuối`.
  - Thay thế `mua bây giờ, trả sau này` bằng `Mua trước trả sau (BNPL)`.
- [ ] **10. Tuân thủ luật quảng cáo & cấm tuyên bố siêu thực (`LAW001`):**
  - Không sử dụng các từ ngữ khẳng định tuyệt đối không có chứng nhận: `rẻ nhất thị trường`, `sàn TMĐT số 1`, `hàng đầu Việt Nam`, `chính hãng 100%`, `giá rẻ vô địch`.
  - Khẳng định chất lượng dựa trên chứng từ pháp lý: phiếu công bố sản phẩm, tem phụ tiếng Việt, hóa đơn chứng từ hợp lệ.
- [ ] **11. Chuẩn hóa cặp đại từ xưng hô register `ecommerce-shopper`:**
  - Giao diện xưng hô thân thiện, trang trọng: Sử dụng `Quý khách` hoặc `Bạn`, hệ thống xưng `Chúng tôi` hoặc `[Tên gian hàng]`.
  - Tránh các đại từ cộc lốc hoặc suồng sã thiếu chuyên nghiệp.

---

## Tier 4: Technical & Orthographic Standards (P3 - Polish)

- [ ] **12. Định dạng giá tiền Đồng Việt Nam (`NUM001`–`NUM003`):**
  - Ký hiệu tiền tệ `₫` đặt sau số tiền kèm khoảng trắng: `250.000 ₫` hoặc `250.000 VNĐ` (không viết kiểu Anh `₫250,000`).
  - Dấu chấm phân cách hàng nghìn: `1.500.000 ₫` (không dùng dấu phẩy kiểu Anh `1,500,000 ₫`).
- [ ] **13. Chuẩn hóa Unicode NFC & Dấu thanh tiếng Việt (`NFC001`, `TONE001`):**
  - Toàn bộ nội dung mô tả sản phẩm, danh mục, thông báo toast được chuẩn hóa Unicode dựng sẵn (NFC).
  - Quy tắc đặt dấu thanh nhất quán trong toàn bộ storefront (kiểu mới: `hòa, thủy`).
- [ ] **14. Định dạng ngày giờ và thời hạn giao hàng (`DATE001`):**
  - Ngày tháng năm viết chuẩn `dd/MM/yyyy` (ví dụ: `28/10/2026`, không viết kiểu Mỹ `10/28/2026`).
