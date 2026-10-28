<!-- vlc-disable: all -->

# Danh Mục Kiểm Tra Chất Lượng Thư Tín & Truyền Thông Doanh Nghiệp (Business Comms QA Checklist)

> Bộ tiêu chuẩn kiểm soát chất lượng (QA Checklist) áp dụng cho mọi tài liệu truyền thông,
> tiếp thị đa kênh, bán hàng B2B và văn bản hành chính trước khi xuất bản hoặc gửi khách hàng.

---

## 1. Đại Từ Xưng Hô & Quan Hệ Giao Tiếp (Pragmatics & Registers)

- [ ] **Khớp Register đã khai báo:** Đại từ nhân xưng có tuân thủ nghiêm ngặt `--register` không?
  - `b2b`: Xưng `em`/`tôi`/`chúng tôi`, hô `anh/chị` hoặc `Quý Công ty`. Tuyệt đối không dùng `bạn`, `mình`, `cậu` (`SALES001`).
  - `zns`: Luôn hô `Quý khách`, không dùng `bạn` hay `cả nhà`.
  - `press`: Khách quan, ngôi thứ ba hoặc `chúng tôi` – `Quý vị`.
  - `livestream`: Xưng `em`/`mình`, hô `cả nhà`, `mọi người`. Không dùng `quý khách`.
  - `gov-admin`: Văn phong hành chính công vụ, không dùng đại từ nhân xưng tùy tiện.
- [ ] **Nhất quán đại từ trong toàn văn bản (`PRO001`):** Không lẫn lộn giữa đại từ trang trọng (`quý khách`) và đại từ thân mật (`bạn`) trong cùng một tài liệu hoặc giao diện.
- [ ] **Xưng hô đối ngoại B2B:** Thư chào hàng và báo giá gửi cấp lãnh đạo đối tác đã có lời mở đầu trang trọng (`Kính gửi`, `Kính chào`) chưa? (`SALES003`).

---

## 2. Zalo Official Account (ZNS & ZBS)

- [ ] **Phân định ranh giới kênh ZNS (`ZNS001`):** Mẫu ZNS giao dịch (transactional) có bị lẫn từ ngữ khuyến mại, giảm giá, voucher, quà tặng không?
- [ ] **Ngân sách ký tự ZNS (`ZNS002`):** Tổng độ dài toàn bộ nội dung template (kể cả giá trị tham số động) có đảm bảo **dưới 400 ký tự NFC** không?
- [ ] **Dự phòng tham số động:** Template tĩnh đã để dành ít nhất 100–120 ký tự cho tên khách hàng, mã đơn hàng và địa chỉ giao hàng chưa?

---

## 3. Tin Nhắn Viễn Thông (SMS Brandname)

- [ ] **Tính toán bảng mã ký tự:** Đã xác định rõ nội dung gửi theo chuẩn ASCII (không dấu, 160 ký tự) hay UCS-2 (có dấu chuẩn, 70 ký tự) chưa?
- [ ] **Kiểm soát dung lượng tin nhắn:** Nội dung có dấu đã được căn chỉnh dưới 70 ký tự để tránh phát sinh cước tin nhắn kép (2x/3x) chưa?
- [ ] **Thương hiệu định danh (Brandname):** Tên thương hiệu hiển thị đã được đăng ký và phê duyệt bởi Cục An toàn thông tin chưa?

---

## 4. Sàn Thương Mại Điện Tử (Shopee, Lazada, TikTok Shop)

- [ ] **Công thức tiêu đề chuẩn SEO:** Đã áp dụng công thức: `[Thương hiệu] + [Tên sản phẩm] + [Đặc tính/Model] + [Quy cách/Màu sắc]` chưa?
- [ ] **Không viết hoa toàn bộ từ (`MKT001`):** Đã loại bỏ các từ viết hoa 4 chữ cái trở lên (như `GIẢM GIÁ`, `CHÍNH HÃNG`), chỉ giữ lại viết hoa đối với tên thương hiệu và tiêu chuẩn kỹ thuật (`USB`, `OLED`, `HDMI`) chưa?
- [ ] **Không chèn emoji rác (`MKT001`):** Tiêu đề đã được làm sạch toàn bộ các biểu tượng cảm xúc spam (`🔥`, `💥`, `⚡`, `❌`, `🎁`, `💯`) chưa?

---

## 5. Luật Quảng Cáo, Khuyến Mại & Người Có Ảnh Hưởng

- [ ] **Trần khuyến mại 50% (`MKT002`):** Nếu mức giảm giá vượt quá 50%, đã có văn bản phê duyệt chương trình khuyến mại tập trung và gắn chú thích `<!-- khuyen-mai-tap-trung: ... -->` chưa?
- [ ] **Công bố tài trợ KOL/KOC (`MKT003`):** Bài viết hoặc video của người có ảnh hưởng đã gắn hashtag `#QuảngCáo`, `#Ad`, hoặc nhãn `Tài trợ bởi` rõ ràng theo Luật 75/2025/QH15 chưa?
- [ ] **Từ ngữ khẳng định tuyệt đối (`LAW001`):** Đã loại bỏ các từ "số 1", "tốt nhất", "hàng đầu", "duy nhất", hoặc đã có tài liệu chứng minh hợp pháp kèm theo chưa?
- [ ] **Không quảng cáo so sánh:** Đã loại trừ mọi nội dung so sánh trực tiếp nhằm hạ thấp sản phẩm, dịch vụ của đối thủ cạnh tranh chưa?

---

## 6. Báo Giá Thương Mại & Thu Hồi Công Nợ (B2B Sales & Dunning)

- [ ] **Quy chuẩn Báo giá (`SALES004`):** Bảng báo giá đã nêu rõ điều khoản thuế GTGT (đã bao gồm hay chưa bao gồm VAT) và thời hạn hiệu lực của báo giá chưa?
- [ ] **Điều khoản thanh toán:** Đã quy định rõ phương thức thanh toán, số tài khoản thụ hưởng, và thời hạn thanh toán (Net 15 / Net 30) chưa?
- [ ] **Quy trình nhắc nợ leo thang:** Thư nhắc nợ đã tuân thủ đúng thang bậc thời gian (T-3 nhắc nhẹ -> T+7 thiện chí -> T+15 đôn đốc -> T+30 công văn chế tài) chưa?

---

## 7. Thể Thức Văn Bản Hành Chính (Nghị Định 30/2020/NĐ-CP)

- [ ] **Quốc hiệu & Tiêu ngữ chuẩn mực (`ADMIN001`):**
  - Dòng 1: `CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM` (in hoa, đậm).
  - Dòng 2: `Độc lập - Tự do - Hạnh phúc` (in thường, đậm, gạch nối có dấu cách).
- [ ] **Số và ký hiệu công văn:** Có đúng định dạng `Số: .../CV-[Tên viết tắt đơn vị]` chưa?
- [ ] **Thẩm quyền ký văn bản:** Đã sử dụng đúng chữ viết tắt thẩm quyền (`TM.`, `KT.`, `TL.`, `TUQ.`) chưa?
- [ ] **Khung nơi nhận:** Dòng cuối cùng của nơi nhận đã có `- Lưu: VT, [Đơn vị soạn thảo]` chưa?

---

## 8. Chống Thư Rác & Quyền Riêng Tư (Nghị Định 91/2020 & Luật 91/2025/QH15)

- [ ] **Cơ chế từ chối nhận tin (`SPAM001`):** Mọi tin nhắn SMS/Zalo/Email tiếp thị hàng loạt đã có hướng dẫn từ chối (ví dụ: `Soạn TC gửi 1324` hoặc nút `Hủy nhận tin`) chưa?
- [ ] **Khung giờ gửi tin:** Đã lên lịch gửi trong khung giờ quy định: SMS/Zalo từ 07:00 đến 22:00; Telemarketing từ 08:00 đến 17:00 chưa?
- [ ] **Bảo vệ dữ liệu cá nhân:** Form thu thập thông tin khách hàng đã có đường dẫn đến Chính sách bảo vệ dữ liệu cá nhân và hộp kiểm đồng ý minh bạch chưa?

---

## 9. Kỹ Thuật Ngôn Ngữ & Trình Bày Số Liệu

- [ ] **Chuẩn hóa Unicode NFC (`NFC001`):** Toàn bộ văn bản đã được chuẩn hóa Unicode dạng dựng sẵn (NFC), không bị lỗi NFD (tổ hợp)?
- [ ] **Tính nhất quán đặt dấu thanh (`TONE001`):** Văn bản tuân thủ một quy chuẩn đặt dấu thanh duy nhất (kiểu mới `hoà, thuỷ` hoặc kiểu cũ `hòa, thủy`)?
- [ ] **Định dạng số và tiền tệ:**
  - Dùng dấu chấm phân tách hàng nghìn: `1.500.000 VND` hoặc `1.500.000 đồng` (`NUM001`, `NUM002`).
  - Dùng dấu phẩy cho số thập phân: `99,5%` (`NUM003`).
  - Dùng ký hiệu số mũ chuẩn: `m²`, `m³`, không viết `m2`, `m3` (`NUM004`).
- [ ] **Định dạng ngày tháng:** Tuân thủ thứ tự Việt Nam: `ngày DD/MM/YYYY` hoặc `ngày DD tháng MM năm YYYY` (`DATE001`).
