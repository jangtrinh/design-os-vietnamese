<!-- vlc-disable: all -->

# Cẩm Nang Tối Ưu Copywriting Đa Kênh Thương Mại Việt Nam (Omnichannel Guide)

> Hướng dẫn kỹ thuật và ngôn ngữ cho Zalo OA (ZNS/ZBS), SMS Brandname, Sàn Thương mại Điện tử
> (Shopee, Lazada, TikTok Shop), Kịch bản Livestream và Thông cáo Báo chí.

---

## 1. Zalo Official Account (OA): Phân Biệt ZNS và ZBS

Hệ sinh thái Zalo OA quy định ranh giới pháp lý và kiểm duyệt khắt khe giữa thông báo chăm sóc khách hàng và thông điệp tiếp thị.

<!-- machine-readable: zalo-channels -->

| Tiêu chí | Zalo Notification Service (ZNS) | Zalo Broadcast Service (ZBS) |
|---|---|---|
| **Mục đích** | Thông báo biến động tài khoản, xác nhận giao dịch, cập nhật đơn hàng, OTP, lịch hẹn | Chiến dịch khuyến mại, giới thiệu sản phẩm mới, tri ân khách hàng |
| **Kiểm duyệt** | Kiểm duyệt mẫu (template) nghiêm ngặt bởi Zalo Cloud Team trước khi kích hoạt | Gửi broadcast chủ động tới người quan tâm Zalo OA |
| **Quy định từ ngữ** | **Nghiêm cấm từ ngữ quảng cáo** (`giảm giá`, `khuyến mãi`, `voucher`, `ưu đãi`, `deal`, `mua ngay`) (`ZNS001`) | Được phép truyền thông ưu đãi, giảm giá và khuyến mại hợp pháp |
| **Ngân sách ký tự** | **Tối đa 400 ký tự chuẩn NFC** (`ZNS002`) bao gồm toàn bộ tham số động | Tối đa 2.000 ký tự (kèm banner hình ảnh, video, CTA đa dạng) |
| **Đại từ quy chuẩn** | Xưng: `[Tên Doanh nghiệp]` – Hô: `Quý khách` (`--register zns`) | Xưng: `[Tên Doanh nghiệp]` – Hô: `Quý khách` hoặc `Bạn` |

### Quy tắc tính toán tham số ZNS (Parameter Sizing)
Khi thiết kế template ZNS, các biến số `<customer_name>`, `<order_id>`, `<amount>`, `<address>` sẽ được thay thế bằng dữ liệu thực tế tại thời điểm gửi (runtime). 
- Dự phòng an toàn: Độ dài template tĩnh không được vượt quá **280 ký tự**, dành ít nhất **120 ký tự** cho các biến dữ liệu thực tế nhằm đảm bảo tổng độ dài luôn dưới trần 400 ký tự NFC.
- Ví dụ template ZNS hợp chuẩn:
  ```text
  Kính gửi Quý khách <customer_name>,
  Đơn hàng <order_id> của Quý khách đã được bàn giao cho đơn vị vận chuyển vào lúc <time>. 
  Mã vận đơn: <tracking_code>. 
  Dự kiến giao hàng vào ngày <delivery_date>. 
  Tổng thanh toán khi nhận hàng: <amount> VND.
  Mọi thắc mắc xin vui lòng liên hệ hotline 1900 xxxx. Trân trọng cảm ơn Quý khách!
  ```

---

## 2. Bài Toán Mã Hóa SMS Brandname: UCS-2 vs ASCII

Nhà mạng viễn thông Việt Nam (Viettel, VNPT, MobiFone) áp dụng cơ chế tính cước tin nhắn dựa trên bảng mã ký tự (Character Encoding).

<!-- machine-readable: sms-math -->

| Chuẩn mã hóa | Ký tự tiếng Việt | Dung lượng 1 tin (Single SMS) | Dung lượng tin ghép (Multipart SMS) | Rủi ro chi phí |
|---|---|---|---|---|
| **GSM 7-bit (ASCII)** | Không dấu (`Don hang da giao`) | **160 ký tự** | **153 ký tự / đoạn** (dành 7 ký tự cho UDH header) | Thấp, tối ưu ngân sách |
| **UCS-2 (Unicode)** | Có dấu chuẩn (`Đơn hàng đã giao`) | **70 ký tự** | **67 ký tự / đoạn** (dành 3 ký tự cho UDH header) | Tăng 2.3x nếu copy vượt 70 ký tự |

### Quy tắc tính cước SMS Brandname thực chiến
1. Một thông điệp có dấu dài 71 ký tự sẽ tự động bị chia thành **2 tin nhắn (134 ký tự)** và tính phí gấp đôi.
2. Một thông điệp dài 135 ký tự sẽ bị chia thành **3 tin nhắn** và tính phí gấp ba.
3. Kỹ thuật viên copywriting phải đếm chính xác số ký tự UTF-16 code units trước khi chốt kịch bản gửi tin hàng loạt.

---

## 3. Công Thức Đặt Tiêu Đề Sàn Thương Mại Điện Tử (Shopee, Lazada, TikTok Shop)

Thuật toán tìm kiếm (Search Algorithm) và xếp hạng hiển thị của các sàn TMĐT tại Việt Nam ưu tiên các tiêu đề giàu thông tin, chuẩn SEO và không chứa từ ngữ lừa dối người dùng.

### A. Công thức tiêu đề chuẩn mực (Listing Title Formula)
```
[Thương hiệu] + [Tên sản phẩm chính] + [Đặc tính cốt lõi / Model] + [Quy cách / Dung tích / Màu sắc]
```
- **Ví dụ chuẩn:**
  - `Baseus Cáp sạc nhanh 100W USB Type-C sang Type-C dài 1.2m bọc dù chống đứt màu xám`
  - `Anker Tai nghe không dây chống ồn chủ động Soundcore Space One Bluetooth 5.3 màu đen`

### B. Các điều cấm kỵ hàng đầu trên sàn TMĐT (`MKT001`)
1. **Cấm viết hoa toàn bộ từ (ALL-CAPS):** Viết hoa toàn bộ các từ từ 4 chữ cái trở lên (như `GIẢM GIÁ`, `CHÍNH HÃNG`, `SIÊU RẺ`) bị thuật toán sàn quét và giảm 30–50% lượt hiển thị tự nhiên. Ngoại lệ duy nhất là tên thương hiệu và tiêu chuẩn kỹ thuật (`HDMI`, `USB`, `OLED`, `WIFI`, `APPLE`, `SAMSUNG`).
2. **Cấm chèn biểu tượng cảm xúc (Spam Emoji):** Chèn các biểu tượng `🔥`, `💥`, `⚡`, `❌`, `⚠️`, `🚀`, `🎁`, `💯` ở đầu hoặc trong tiêu đề khiến sản phẩm bị hệ thống phân loại là tin rác.
3. **Cấm nhồi nhét từ khóa sai sự thật (Keyword Stuffing):** Không đưa các từ khóa không liên quan vào tiêu đề (ví dụ: bán ốp lưng nhưng chèn *"iPhone 15 Pro Max Samsung Galaxy S24"*).

---

## 4. Kịch Bản Bán Hàng Trực Tiếp (Livestream Spoken Script)

Phiên phát trực tiếp trên TikTok Shop và Shopee Live đòi hỏi ngôn ngữ khẩu ngữ tự nhiên, nhịp điệu dồn dập, tạo cảm xúc và thúc đẩy chuyển đổi tức thì.

### A. Quy chuẩn xưng hô phiên Live (`--register livestream`)
- **Đại từ kỳ vọng:** Xưng `Em` / `Mình` / `[Tên Host]` – Hô `Cả nhà`, `Mọi người`, `Các bác`, `Mấy bà`.
- **Cấm ngặt nghèo:** Tuyệt đối không dùng `Quý vị`, `Quý khách` (tạo cảm giác như bản tin truyền hình thời sự, triệt tiêu sự tương tác gần gũi).

### B. Cấu trúc nhịp điệu chốt Deal (Urgency & Scarcity Ladder)
1. **Hook giữ chân người xem (0–5 giây đầu mỗi mã hàng):** Nêu bật nỗi đau hoặc mức giá gây sốc.
2. **Thị phạm sản phẩm trực quan:** Cầm, thử, test độ bền hoặc hiệu năng thực tế trước ống kính.
3. **Call-to-Action ghim giỏ hàng:** 
   - *"Em vừa ghim deal số 1 ở góc trái màn hình, cả nhà chạm tay vào mua ngay kẻo hết mã voucher!"*
   - *"Chỉ còn đúng 15 suất trợ giá từ nhãn hàng, ai chưa thanh toán trong giỏ hàng bấm ngay giúp em nhé!"*

---

## 5. Quy Chuẩn Thông Cáo Báo Chí Doanh Nghiệp (Press Release)

Thông cáo báo chí gửi các cơ quan thông tấn báo chí tại Việt Nam (VnExpress, Tuổi Trẻ, Dân Trí, Forbes VN) phải tuân thủ nghiêm ngặt văn phong báo chí khách quan (`--register press`).

### A. Cấu trúc 6 phần kinh điển
1. **Tiêu đề báo chí (Press Headline):** Ngắn gọn, nêu bật sự kiện hoặc giá trị mới, không giật tít câu view.
2. **Dòng ngày tháng địa điểm (Dateline):** Bắt buộc in hoa và viết đúng quy chuẩn:
   `HÀ NỘI / TP. HỒ CHÍ MINH, ngày DD tháng MM năm YYYY`
3. **Đoạn dẫn nhập (Lead Paragraph):** Trả lời trọn vẹn mô hình 5W1H (Ai, Cái gì, Ở đâu, Khi nào, Vì sao, Như thế nào).
4. **Nội dung thân bài (Body):** Cung cấp dữ liệu định lượng, bối cảnh thị trường và tác động kinh tế - xã hội.
5. **Trích dẫn lãnh đạo (Executive Quote):** Thể hiện tầm nhìn chiến lược, xưng danh rõ ràng:
   *Ông [Họ và tên], Tổng Giám đốc [Tên Doanh nghiệp] cho biết: "..."*
6. **Thông tin về doanh nghiệp (Boilerplate) & Đầu mối báo chí (Media Contact):** Tóm tắt quy mô công ty, email, số điện thoại của người phụ trách truyền thông.


---

## 6. Mẫu Thông Cáo Báo Chí Chuẩn Mực Doanh Nghiệp (Sample Press Release)

```markdown
# DOANH NGHIỆP CÔNG NGHỆ [TÊN] RA MẮT NỀN TẢNG THƯƠNG MẠI B2B ĐẦU TIÊN TẠI VIỆT NAM

**TP. HỒ CHÍ MINH, ngày 15 tháng 03 năm 2026** — Hôm nay, Công ty Cổ phần Công nghệ [Tên] 
chính thức công bố ra mắt nền tảng thương mại số chuyên biệt cho khối doanh nghiệp vừa 
và nhỏ (SMEs). Giải pháp giúp rút ngắn 60% thời gian xử lý đơn đặt hàng và tự động hóa 
quy trình đối chiếu công nợ giữa các pháp nhân.

Nền tảng được phát triển trên kiến trúc điện toán đám mây bảo mật cao, kết nối trực tiếp 
với hệ thống hóa đơn điện tử của Tổng cục Thuế và hơn 25 ngân hàng thương mại tại Việt Nam. 
Trong giai đoạn thử nghiệm kéo dài 6 tháng vừa qua, nền tảng đã hỗ trợ xử lý thành công hơn 
150.000 giao dịch thương mại với tổng giá trị thanh toán đạt hơn 500 tỷ đồng.

Ông Nguyễn Văn Nam, Tổng Giám đốc Công ty Cổ phần Công nghệ [Tên] chia sẻ:
> "Sứ mệnh của chúng tôi là xóa bỏ mọi rào cản hành chính và chứng từ thủ công trong 
> giao dịch kinh tế giữa các doanh nghiệp Việt Nam. Với việc ứng dụng công nghệ tự động 
> hóa quy trình thanh toán, chúng tôi kỳ vọng sẽ mang lại giải pháp quản trị dòng tiền 
> minh bạch và tối ưu chi phí vận hành cho cộng đồng doanh nghiệp."

**Về Công ty Cổ phần Công nghệ [Tên]**
Được thành lập vào năm 2020, Công ty Cổ phần Công nghệ [Tên] là đơn vị tiên phong trong 
lĩnh vực cung cấp giải pháp chuyển đổi số cho doanh nghiệp tại Đông Nam Á, hiện phục vụ 
hơn 10.000 khách hàng tổ chức trên toàn quốc.

**Đầu mối liên hệ truyền thông:**
- Bà Lê Thu Trang — Trưởng phòng Truyền thông & Đối ngoại
- Email: media@domain.vn | Điện thoại: 028 3822 xxxx
```

---

## 7. Bảng Đối Soát Thông Điệp Đa Kênh Nhanh (Channel Matrix Quick Reference)

<!-- machine-readable: channel-matrix-summary -->

| Kênh | Giới hạn ký tự | Đại từ xưng hô | Rủi ro pháp lý hàng đầu | Kiểm duyệt tự động |
|---|---|---|---|---|
| **Zalo ZNS** | 400 NFC chars | `Quý khách` | Lẫn lộn nội dung quảng cáo vào thông báo giao dịch | Bắt buộc duyệt template |
| **SMS Brandname** | 70 UCS-2 / 160 ASCII | `Quý khách` | Nhảy số lượng tin phát sinh chi phí gấp đôi | Viettel / MobiFone / VinaPhone |
| **Shopee / Lazada** | 120–255 chars | Khách hàng (ngôi 3) | ALL-CAPS, chèn emoji spam, vi phạm bản quyền | Thuật toán sàn TMĐT |
| **TikTok Live** | Không giới hạn | `Cả nhà` / `Mọi người` | Dùng từ ngữ trang trọng gây chán, vi phạm chính sách cộng đồng | AI quét âm thanh thời gian thực |
| **Email B2B** | 150–300 từ | `Anh/Chị` | Xưng hô suồng sã (`bạn - mình`), thiếu thông tin liên hệ | Bộ lọc spam Outlook / Gmail |
| **Thông cáo báo chí**| 500–800 từ | `Quý vị` / Khách quan | Thiếu trích dẫn lãnh đạo, quảng cáo lộ liễu, thiếu dateline | Ban biên tập báo chí |
