# Tiêu Chuẩn Thuật Ngữ TMĐT, Chuỗi Cung Ứng & Danh Mục Calque Giao Nhận (`vi-VN`)

Tài liệu chuẩn hóa ngôn ngữ giao diện (UI/UX microcopy), trạng thái vận hành đơn hàng, phương thức thanh toán và danh mục lỗi dịch thô (calques) trong lĩnh vực thương mại điện tử và bán lẻ đa kênh tại Việt Nam.

---

## 1. Vòng Đời Trạng Thái Đơn Hàng Chuẩn Ngành

Giao diện ứng dụng và website thương mại điện tử cần sử dụng hệ thống trạng thái nhất quán, dễ hiểu đối với người tiêu dùng Việt Nam:

1. **Chờ xác nhận:** Đơn hàng đã được tạo thành công trên hệ thống và đang chờ người bán xác nhận tình trạng còn hàng.
2. **Đang xử lý / Đang đóng gói:** Người bán đang đóng gói sản phẩm và chuẩn bị bàn giao cho bưu cục vận chuyển.
3. **Đã bàn giao vận chuyển:** Kiện hàng đã được quét mã tiếp nhận tại trung tâm chia chọn của đơn vị vận chuyển.
4. **Đang giao hàng:** Bưu tá (shipper) đang trên lộ trình phát hàng tới địa chỉ nhận của khách hàng trong ngày.
5. **Giao hàng thành công / Hoàn tất đơn hàng:** Khách hàng đã nhận hàng và hoàn tất thanh toán (nếu áp dụng COD).
6. **Đã hủy đơn:** Đơn hàng bị hủy bởi người mua hoặc người bán trước khi giao nhận.
7. **Yêu cầu trả hàng / Hoàn tiền:** Quy trình khiếu nại hoặc đổi trả đang được xử lý theo chính sách bảo vệ khách hàng.

---

## 2. Bảng Đối Chiếu Thuật Ngữ Chuẩn vs. Calque Dịch Thô (`ECOM005`)

Tuyệt đối loại bỏ các bản dịch máy nguyên từ (word-by-word) làm méo mó tiếng Việt và suy giảm uy tín của sàn thương mại điện tử:

| Thuật ngữ tiếng Anh gốc | Bản dịch máy thô (BỊ CẤM ❌) | Thuật ngữ tiếng Việt tự nhiên (BẮT BUỘC ✅) | Ghi chú ngữ nghĩa |
|---|---|---|---|
| Out for delivery | `Ra ngoài để giao hàng` | `Đang giao hàng` | "Out for delivery" có nghĩa là bưu tá đang trên đường đi giao kiện hàng. |
| Order fulfillment | `Sự hoàn thành đơn hàng` | `Hoàn tất đơn hàng` / `Xử lý đơn hàng` | Quá trình tiếp nhận, đóng gói và xử lý trọn gói đơn hàng. |
| Add to cart | `Thêm vào xe đẩy` / `Bỏ vào giỏ xe` | `Thêm vào giỏ hàng` | Trong mua sắm trực tuyến, người Việt Nam gọi là "giỏ hàng", không dùng từ "xe đẩy" hay "giỏ xe". |
| Cash on delivery (COD) | `Tiền mặt trên giao hàng` | `Thanh toán khi nhận hàng (COD)` | Phương thức thanh toán tiền mặt trực tiếp cho bưu tá khi nhận kiện hàng. |
| Return policy | `Chính sách trở lại` | `Chính sách đổi trả` / `Chính sách hoàn trả` | Quy định về điều kiện và thủ tục đổi/trả sản phẩm của cửa hàng. |
| Last-mile carrier | `Người vận chuyển cuối cùng` | `Đơn vị vận chuyển chặng cuối` | Doanh nghiệp logistics thực hiện khâu giao nhận chặng cuối đến tay khách hàng. |
| Estimated delivery time | `Thời gian giao hàng ước tính` | `Dự kiến giao hàng` / `Thời gian giao dự kiến` | Ngày/giờ dự kiến bưu phẩm đến địa chỉ người nhận. |
| Buy now, pay later | `Mua bây giờ, trả sau này` | `Mua trước trả sau (BNPL)` | Giải pháp tín dụng tiêu dùng số. |

---

## 3. Quy Chuẩn Giá Cả & Định Dạng Số Tiền (`NUM001`, `NUM002`)

- **Ký hiệu tiền tệ Đồng Việt Nam:**
  - Viết sau số tiền kèm khoảng trắng hoặc khoảng trắng không ngắt: `250.000 ₫` hoặc `250.000 VNĐ`.
  - Không đặt ký hiệu trước số tiền như tiếng Anh (tránh `₫250,000`).
- **Dấu phân cách hàng nghìn:**
  - Luôn dùng dấu chấm `.` để phân tách các nhóm 3 chữ số: `1.500.000 ₫`.
  - Không dùng dấu phẩy `,` như kiểu định dạng của các nước nói tiếng Anh (tránh `1,500,000 ₫` vi phạm quy tắc `NUM001`).
