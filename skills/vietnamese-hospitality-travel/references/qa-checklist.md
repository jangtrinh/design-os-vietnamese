<!-- vlc-disable: all -->

# Hospitality, Aviation, & Travel QA Checklist (`design-os-vietnamese`)

This QA checklist provides a comprehensive, systematic review protocol for hotel booking confirmations, resort marketing copy, civil aviation delay notices, luxury fine dining menus, and travel itineraries.

---

## 1. Statutory & Regulatory Gates (Luật Du lịch 2017 & TT 19/2023/TT-BGTVT)

| Gate | Check Item | Pass Criteria | Severity if Failed |
|---|---|---|---|
| **GATE-HOS-01** | **Star Rating Validation (`HOS002`)** | Khách sạn/resort chỉ được gắn xếp hạng từ 1 sao đến 5 sao theo Quyết định của Cục Du lịch Quốc gia Việt Nam hoặc Sở Du lịch. Không sử dụng '6 sao', '7 sao'. | `ERROR` |
| **GATE-HOS-02** | **Pricing Transparency (`HOS001`)** | Không dùng viết tắt `++` mập mờ. Nêu rõ giá Net hoặc ghi chú đầy đủ: *"chưa bao gồm 5% phí phục vụ và 8% (hoặc 10%) thuế GTGT"*. | `ERROR` |
| **GATE-HOS-03** | **Check-in / Check-out Times (`HOS003`)** | Mọi xác nhận đặt phòng (`hotel-booking`) phải ghi rõ giờ nhận phòng (Check-in), giờ trả phòng (Check-out) và chính sách phụ thu nhận sớm/trả muộn. | `ERROR` |
| **GATE-HOS-04** | **Cancellation & Refund Policy (`HOS003`)** | Quy định rõ khung thời gian hủy miễn phí, mức phí phạt hủy phòng (50% hay 100%) và chính sách khách vắng mặt (No-show). | `ERROR` |
| **GATE-HOS-05** | **Flight Disruption Notice (`HOS004`)** | Khi thông báo chậm chuyến hoặc hủy chuyến (`flight-notice`), bắt buộc phải có lời xin lỗi chân thành và nêu rõ quyền lợi hỗ trợ ăn nghỉ, chuyển chuyến hoặc hoàn vé theo Thông tư 19/2023/TT-BGTVT. | `ERROR` |
| **GATE-HOS-06** | **F&B Allergen & Tax Disclosures (`HOS005`)** | Mọi thực đơn F&B (`fnb-menu`) phải có dòng lưu ý thực khách về dị ứng thực phẩm và thông tin tình trạng thuế GTGT / phí phục vụ. | `WARN` |
| **GATE-HOS-07** | **Courteous Hospitality Tone (`HOS006`)** | Tuyệt đối không dùng mệnh lệnh cộc lốc, đe dọa phạt tiền hoặc thoái thác trách nhiệm đối với tài sản của khách. Dùng *"Quý khách vui lòng..."*. | `WARN` |

---

## 2. Register & Sociolinguistic Etiquette

- **Chế độ xưng hô chuẩn (`hospitality-luxury`):**
  - Người đọc / Khách hàng: `Quý khách` (viết hoa chữ Q để thể hiện sự trọng thị tối cao).
  - Khách sạn / Doanh nghiệp tự xưng: `khu nghỉ dưỡng`, `khách sạn`, `chúng tôi`, hoặc tên thương hiệu.
  - Tuyệt đối cấm dùng các đại từ suồng sã: `bạn`, `mình`, `cả nhà`, `cậu`, `mày` trong các tài liệu đặt phòng, thông báo chuyến bay hoặc dịch vụ cao cấp.
- **Tính nhất quán trong toàn bộ tài liệu (`PRO001`):**
  - Không mở đầu bằng `Quý khách` rồi kết thúc bằng câu kêu gọi hành động `bạn hãy...`.
  - Giữ vững âm sắc hiếu khách (hospitality mindset) xuyên suốt từ tiêu đề, nội dung chính đến phần chữ ký xác nhận.

---

## 3. Typographic, Formatting, & Numerical Standards

1. **Định dạng tiền tệ Việt Nam Đồng:**
   - Dùng dấu chấm `.` phân cách hàng nghìn và ký hiệu `₫` đặt sau số tiền: `2.500.000 ₫`.
   - Tránh viết: `2,500,000 VND`, `2.500k`, `2tr5`.
2. **Định dạng ngày tháng và thời gian:**
   - Ngày tháng theo thứ tự ngày/tháng/năm: `dd/MM/yyyy` (ví dụ: `15/03/2026`).
   - Thời gian sử dụng định dạng 24 giờ: `14:00`, `18:30` (tránh `2:00 PM` trong văn bản tiếng Việt chuẩn).
3. **Quy chuẩn tên phòng và món ăn:**
   - Viết hoa chữ cái đầu của các danh từ riêng và tên phân hạng phòng: `Phòng Deluxe Hướng biển`, `Biệt thự Biển có Hồ bơi`.
   - Giữ nguyên thuật ngữ chuyên ngành ẩm thực quốc tế kèm chú thích tiếng Việt rõ ràng.

---

## 4. Pre-Publication Verification Workflow

Trước khi phát hành văn bản đặt phòng, thực đơn hay thông báo chuyến bay:

1. [ ] **Kiểm tra cú pháp & mã hóa:** Văn bản đã được chuẩn hóa Unicode NFC, không có ký tự mojibake hay lỗi dấu thanh.
2. [ ] **Kiểm tra từ cấm & calque:** Chạy công cụ kiểm tra `validate_copy.py` với cờ `--strict`.
3. [ ] **Xác thực hạng sao & quảng cáo:** Không có tuyên bố 'số 1', 'duy nhất' hoặc '6 sao/7 sao' khi chưa có chứng nhận nhà nước.
4. [ ] **Xác thực pháp lý vận chuyển & lưu trú:** Minh bạch điều khoản hoàn đổi vé máy bay hoặc phụ thu lưu trú.
5. [ ] **Duyệt văn phong hiếu khách:** Mọi thông báo hướng dẫn nội quy đều bắt đầu bằng lời mời lịch thiệp, tôn trọng trải nghiệm của khách hàng.

---

## 5. Doctype-Specific Deep Audit Protocols

### 5.1 Hotel & Resort Booking Confirmations (`hotel-booking`)
- [ ] Đã có thông tin mã đặt phòng (Booking Reference), tên khách lưu trú chính xác.
- [ ] Thời gian nhận phòng (Check-in) ghi rõ từ mấy giờ (ví dụ: `14:00`).
- [ ] Thời gian trả phòng (Check-out) ghi rõ trước mấy giờ (ví dụ: `12:00`).
- [ ] Có điều khoản phụ thu rõ ràng đối với trường hợp nhận phòng sớm hoặc trả phòng muộn.
- [ ] Nêu rõ chính sách hoàn hủy phòng (miễn phí trước bao nhiêu ngày, mức phí phạt khi hủy muộn hoặc không đến).
- [ ] Ghi rõ tổng chi phí và tình trạng thanh toán: đã thanh toán đủ hay thu tiền tại quầy khi nhận phòng.

### 5.2 Flight Disruption & Schedule Change Notices (`flight-notice`)
- [ ] Đầy đủ mã hiệu chuyến bay, chặng bay và giờ khởi hành cũ / mới.
- [ ] Nguyên nhân kỹ thuật hoặc thời tiết được giải thích ngắn gọn, trung thực.
- [ ] Có câu xin lỗi lịch thiệp: *"chân thành cáo lỗi và mong Quý khách thông cảm"*.
- [ ] Cung cấp đường dẫn hoặc hướng dẫn chuyển chuyến miễn phí, hoàn vé tự động hoặc nhận voucher dịch vụ ăn uống.

### 5.3 F&B & Fine Dining Menus (`fnb-menu`)
- [ ] Có ghi chú cảnh báo dị ứng thực phẩm (các loại hạt, hải sản, gluten, bơ sữa).
- [ ] Có dòng ghi chú tình trạng thuế giá trị gia tăng (thuế GTGT) và phí phục vụ (giá Net hay ++).
- [ ] Mô tả món ăn tinh tế, nêu bật nguyên liệu bản địa và phương pháp chế biến thủ công.
- [ ] Tên các loại rượu vang có đầy đủ niên vụ, giống nho và xuất xứ địa lý.

### 5.4 Tour Itineraries (`tour-itinerary`)
- [ ] Lịch trình chi tiết từng ngày, từng buổi (sáng, trưa, chiều, tối).
- [ ] Mục bao gồm (Inclusions) và không bao gồm (Exclusions) phân định rành mạch.
- [ ] Thông tin mức trách nhiệm bảo hiểm du lịch trọn gói được công bố cụ thể.
- [ ] Điều khoản hoàn hủy tour theo thang thời gian rõ ràng, minh bạch.
