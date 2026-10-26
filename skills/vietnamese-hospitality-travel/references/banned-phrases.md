<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Hospitality, Aviation, & Travel (`design-os-vietnamese`)

In hospitality, resort management, civil aviation, and culinary F&B copy, prohibited language breaches Vietnamese advertising laws (Luật Quảng cáo 2012), consumer rights protection, or statutory tourism regulations (Luật Du lịch 2017).

---

## 1. Regulated Superlatives (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, using superlatives without valid documentary certification from a competent state agency or accredited inspection body is illegal.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|đẹp\|sang\s+trọng\|đẳng\s+cấp\|ngon\|rẻ\|độc\s+đáo\|hấp\s+dẫn\|uy\s+tín\|hiện\s+đại)\s+nhất` | "most luxurious / best / cheapest / most reputable" | Common violation in resort & hotel advertisements |
| `duy\s+nhất` | "the only" | Specifically named in statute |
| `số\s*(?:một\|1)\b` | "number one" | Specifically named in statute |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |
| `thiên\s+đường\s+nghỉ\s+dưỡng\s+số\s+1` | "number one resort paradise" | Prohibited advertising claim |
| `khách\s+sạn\s+đẹp\s+nhất\s+Việt\s+Nam` | "most beautiful hotel in Vietnam" | Prohibited superlative without state award |
| `dịch\s+vụ\s+hoàn\s+hảo\s+nhất` | "most perfect service" | Unsubstantiated quality claim |
| `ẩm\s+thực\s+đỉnh\s+cao\s+nhất` | "highest culinary pinnacle" | Unsubstantiated superlative |

**Compliant Rewrite Principle:**
Never use unsubstantiated superlatives (`resort đẹp nhất đảo ngọc`). State verified factual amenities, official star ratings, or accredited awards:
- ❌ `Khu nghỉ dưỡng 5 sao có bãi biển đẹp nhất Phú Quốc`
- ✅ `Khu nghỉ dưỡng 5 sao tọa lạc tại Bãi Kem với đường bờ biển dài 800 m`

---

## 2. Prohibited Claims & Hostile Guest Phrasing

The following phrases are prohibited across hotel confirmations, flight notices, menus, and tour itineraries:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale |
|---|---|---|
| `resort 7 sao` | `khu nghỉ dưỡng 5 sao cao cấp` | Luật Du lịch 2017 Điều 50 chỉ xếp hạng từ 1 đến 5 sao |
| `tiêu chuẩn 6 sao` | `tiêu chuẩn 5 sao quốc tế` | Luật Du lịch 2017 Điều 50 không công nhận hạng 6 sao |
| `dịch vụ 6 sao` | `dịch vụ chuẩn 5 sao quốc tế` | Không tồn tại phân hạng 6 sao theo pháp luật du lịch |
| `giá rẻ như cho` | `mức giá ưu đãi đặc quyền` | Quảng cáo phi chuẩn mực thương mại |
| `tour du lịch 0 đồng` | `tour du lịch trọn gói tiết kiệm` | Nghị định 45/2019/NĐ-CP cấm tour 0 đồng biến tướng |
| `cấm mang đồ ăn vào phòng` | `Quý khách vui lòng không sử dụng thực phẩm mang từ ngoài vào phòng` | Giữ văn phong hiếu khách, tránh mệnh lệnh cộc lốc |
| `khách tự bảo quản đồ đạc mất không chịu trách nhiệm` | `Để đảm bảo an toàn tài sản, Quý khách vui lòng gửi tư trang tại két sắt` | Khách sạn có trách nhiệm bảo quản tài sản khách lưu trú |
| `phạt 100% tiền cọc` | `áp dụng phí hủy phòng tương đương 100% tiền đặt cọc` | Dùng thuật ngữ phí dịch vụ / phí hủy phòng theo thỏa thuận |
| `không hoàn vé dưới mọi hình thức` | `vé áp dụng điều kiện không hoàn hủy theo quy định giá vé` | Thông tư 19/2023/TT-BGTVT quy định hoàn vé khi chuyến bay bị hủy do lỗi hãng |
| `chuyến bay bị hủy khách tự tìm chỗ ở` | `hãng hàng không hỗ trợ bố trí nơi lưu trú cho hành khách` | Thông tư 14/2015/TT-BGTVT quy định nghĩa vụ phục vụ lưu trú |
| `chậm chuyến do lỗi kỹ thuật không đền bù` | `hãng hàng không thực hiện bồi thường ứng trước không hoàn lại` | Thông tư 19/2023/TT-BGTVT bắt buộc bồi thường chậm chuyến kéo dài |
| `bao ăn bao ở bao vé` | `chương trình tour đã bao gồm chi phí lưu trú, ăn uống và vé tham quan` | Văn phong lữ hành chuyên nghiệp, chuẩn mực |
| `đi tour thả ga không lo về giá` | `chương trình du lịch với chi phí minh bạch và trọn gói` | Loại bỏ khẩu hiệu giật gân, thiếu chuyên nghiệp |
| `khách hàng tự chịu mọi rủi ro khi bay` | `hành khách được bảo hiểm hàng không theo quy định pháp luật` | Luật Hàng không Dân dụng Việt Nam quy định trách nhiệm bồi thường |
| `hủy tour mất sạch tiền` | `phí hủy tour tính theo thời điểm thông báo hủy trong hợp đồng lữ hành` | Hợp đồng lữ hành phải quy định khung thời gian hoàn hủy rõ ràng |
| `check-in tự túc` | `thủ tục nhận phòng tự động` | Tránh dùng từ lóng nửa nạc nửa mỡ |
| `check-out trễ tính tiền gấp đôi` | `trả phòng muộn sau thời gian quy định sẽ áp dụng mức phụ thu tương ứng` | Diễn đạt chính sách phụ thu minh bạch, lịch sự |
| `menu đồ ăn không đổi trả` | `các món ăn đã chuẩn bị theo yêu cầu xin phép không hoàn đổi` | Văn phong ẩm thực cao cấp, tôn trọng thực khách |
| `phí tip bắt buộc` | `tiền bồi dưỡng tùy tâm / phí dịch vụ đã bao gồm` | Tiền tip không được ép buộc nếu không có thỏa thuận trước |
| `chặt chém du khách` | *(loại bỏ hoàn toàn)* | Hành vi vi phạm Luật Giá và hình ảnh du lịch quốc gia |
| `bán phòng chui` | `phân phối phòng qua kênh không chính thức` | Dùng thuật ngữ nghiệp vụ kinh doanh khách sạn |
| `cháy phòng toàn bộ` | `khách sạn đã kín phòng trong giai đoạn này` | Thuật ngữ nghiệp vụ đặt phòng chuyên nghiệp |
| `bay đúng giờ 100%` | `chỉ số bay đúng giờ (OTP) duy trì ở mức cao` | Không thể cam kết tuyệt đối trong khai thác hàng không |
| `bao đậu visa 100%` | `hỗ trợ tối đa quy trình chuẩn bị hồ sơ xin thị thực` | Thẩm quyền cấp thị thực thuộc cơ quan ngoại giao nước sở tại |
| `resort đẳng cấp hoàng gia` | `khu nghỉ dưỡng cao cấp chuẩn quốc tế` | Lạm dụng từ ngữ phong kiến, phô trương |
| `tour giá sốc tận óc` | `chương trình tour ưu đãi mùa lễ hội` | Khẩu hiệu phản cảm, vi phạm văn hóa quảng cáo |
| `khách phải chịu phạt nếu làm bẩn khăn` | `trường hợp làm hỏng hoặc ố bẩn tài sản, khách sạn xin phép áp dụng phí giặt tẩy` | Ngôn từ hiếu khách lịch thiệp, tôn trọng khách hàng |
| `miễn trách nhiệm hoàn toàn` | `giới hạn trách nhiệm theo hợp đồng vận chuyển` | Hãng vận chuyển không thể tự ý miễn trừ mọi trách nhiệm pháp lý |
| `đồ ăn thức uống tươi sống 100%` | `nguyên liệu tươi ngon được tuyển chọn mỗi ngày` | Quy định an toàn thực phẩm và tính xác thực |
| `khách sạn không phục vụ người địa phương` | *(phân biệt đối xử trái pháp luật - loại bỏ)* | Vi phạm Luật Du lịch về quyền bình đẳng của khách du lịch |
| `dồn tour ghép khách tùy tiện` | `kết hợp đoàn du lịch theo thỏa thuận bằng văn bản với khách hàng` | Vi phạm Điều 40 Luật Du lịch 2017 về quản lý tour |
| `resort sang chảnh nhất vịnh` | `khu nghỉ dưỡng sang trọng bên bờ vịnh` | Tránh từ lóng 'sang chảnh' và từ ngữ tâng bốc |
| `ăn buffet tẹt ga không giới hạn` | `tiệc tự chọn buffet không giới hạn món ăn` | Thay thế từ lóng khẩu ngữ bằng phong cách ẩm thực chuẩn |
