<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese Banned Phrases & UI Anti-Patterns

> Anti-patterns, translationese, bureaucratic filler, and prohibited claims in Vietnamese software interfaces (`vi-VN`).
> Loaded directly by `validate_copy.py` into the active linter ruleset.

---

## 1. UI Translationese & Bureaucratic Padding

Modern software interfaces demand concise, immediate, and high-clarity copy. Translationese typically introduces:
1. **Unnecessary honorifics and auxiliary verbs** (`tiến hành`, `thực hiện`, `vui lòng`, `xin quý khách`).
2. **Clumsy passive constructions** (`đã được gửi thành công bởi hệ thống`).
3. **Dead-end apologetic filler** (`Oops!`, `Rất tiếc vì sự bất tiện này`) without an actionable recovery path.

---

## 2. Machine-Readable Calques & Banned UI Phrases

<!-- machine-readable: calques -->
| ❌ Cụm từ cấm / Lạm dụng | ✅ Cách diễn đạt tự nhiên | Gợi ý thay thế / Ngữ cảnh | Severity |
|---|---|---|---|
| xin quý khách vui lòng tiến hành | Vui lòng | Cắt bỏ kính ngữ thừa và động từ phụ trợ | error |
| yêu cầu đã được tiến hành gửi thành công | Đã gửi yêu cầu | Bỏ thể bị động và từ phụ trợ tiến hành | error |
| bạn hãy nhấn vào nút | Chọn / Nhấn | Không mô tả thao tác vật lý hiển nhiên | error |
| oops đã có lỗi | Không thể xử lý yêu cầu | Tránh tiếng lóng dịch cẩu thả từ tiếng Anh | error |
| xin lỗi vì sự bất tiện này | Thử lại sau ít phút | Thay câu xin lỗi sáo rỗng bằng hướng dẫn khắc phục | error |
| vui lòng chờ trong giây lát | Đang tải... / Đang xử lý... | Dùng trạng thái tiến trình rõ ràng | warn |
| tiến hành đăng nhập | Đăng nhập | Rút gọn nhãn nút hành động | error |
| tiến hành thanh toán | Thanh toán | Nút bấm phải ngắn gọn, trực diện | error |
| tiến hành xóa | Xóa | Động từ trực tiếp | error |
| thực hiện cập nhật | Cập nhật | Bỏ từ đệm thực hiện | error |
| thực hiện việc lưu | Lưu | Bỏ từ đệm thực hiện việc | error |
| đã được lưu thành công | Đã lưu | Rút gọn thông báo toast | error |
| đã được xóa thành công | Đã xóa | Rút gọn thông báo toast | error |
| đã được tạo thành công | Đã tạo | Rút gọn thông báo toast | error |
| bạn có chắc chắn muốn | Bạn có muốn / Xác nhận | Giảm độ dài tiêu đề hộp thoại xác nhận | warn |
| hãy chắc chắn rằng bạn | Đảm bảo bạn | Diễn đạt tự nhiên, trực diện | warn |
| vui lòng kiểm tra lại thông tin của bạn | Kiểm tra lại thông tin | Tránh lặp đại từ sở hữu | warn |
| thao tác của bạn đã hoàn tất | Đã hoàn tất | Tránh đại từ và danh từ hóa | error |
| nhấn vào đây để xem chi tiết | Xem chi tiết | Tránh anti-pattern liên kết click here | error |
| bấm vào liên kết dưới đây | Mở liên kết | Tránh anti-pattern liên kết click here | error |
| dữ liệu đang được tải xin vui lòng chờ | Đang tải dữ liệu... | Tránh câu rườm rà trong spinner | error |
| không có bất kỳ kết quả nào | Không tìm thấy kết quả | Tránh dịch máy bất kỳ | warn |
| rất tiếc nhưng hệ thống gặp lỗi | Không thể kết nối máy chủ | Nêu rõ nguyên nhân kỹ thuật thay vì xin lỗi | error |
| chúc mừng bạn đã đăng ký thành công | Đăng ký thành công | Cắt bỏ chúc mừng thừa thãi trong onboarding SaaS | warn |
| cảm ơn bạn đã sử dụng dịch vụ của chúng tôi | Cảm ơn bạn | Giảm bớt khách sáo rườm rà | warn |
| vui lòng không tắt trình duyệt trong quá trình này | Không đóng trình duyệt khi đang xử lý | Cảnh báo tiến trình rõ ràng | warn |
| hệ thống đang tiến hành bảo trì | Hệ thống đang bảo trì | Bỏ từ phụ trợ tiến hành | error |
| yêu cầu của quý khách đang được xử lý | Đang xử lý yêu cầu | Tránh kính ngữ hành chính rườm rà | error |
| quý khách vui lòng điền đầy đủ | Vui lòng điền đầy đủ thông tin | Ngữ cảnh web SaaS | error |
| bạn không có quyền truy cập vào trang này | Bạn không có quyền truy cập | Rút gọn thông báo lỗi 403 | warn |

---

## 3. Superlatives & Regulated Advertising Claims

Vietnamese advertising law (Luật Quảng cáo Đ8 K11 và Luật 75/2025/QH15) strictly prohibits unsubstantiated absolute claims (`số 1`, `hàng đầu`, `tốt nhất`, `duy nhất`, `rẻ nhất`, `an toàn tuyệt đối`) without verifiable legal documentation.

<!-- machine-readable: superlatives -->
| Regex Pattern | Mô tả | Ghi chú pháp lý / Căn cứ |
|---|---|---|
| `(?<!\w)(số\s+1\|hàng\s+đầu\|tốt\s+nhất\|duy\s+nhất\|rẻ\s+nhất\|hoàn\s+hảo\s+nhất)(?!\w)` | Từ ngữ khẳng định vị thế tuyệt đối không có chứng nhận | Luật Quảng cáo Đ8 K11 |
| `(?<!\w)(chính\s+xác\s+tuyệt\s+đối\|an\s+toàn\s+tuyệt\s+đối\|100%\s+bảo\s+mật)(?!\w)` | Cam kết an toàn hoặc bảo mật tuyệt đối không thể chứng minh | Luật 75/2025/QH15 |
| `(?<!\w)(độc\s+quyền\s+duy\s+nhất\|không\s+thể\s+bị\s+hack)(?!\w)` | Khẳng định độc quyền hoặc miễn nhiễm bảo mật | Luật An ninh mạng & Bảo vệ NTD |
| `(?<!\w)(vô\s+địch\|vượt\s+trội\s+nhất\|tối\s+ưu\s+nhất)(?!\w)` | Tính từ so sánh bậc nhất không có căn cứ kiểm định | Nghị định 38/2021/NĐ-CP |
| `(?<!\w)(nhanh\s+nhất\s+thị\s+trường\|rẻ\s+nhất\s+việt\s+nam)(?!\w)` | So sánh giá hoặc hiệu năng thị trường thiếu số liệu độc lập | Luật Cạnh tranh & Quảng cáo |
| `(?<!\w)(cam\s+kết\s+100%\|đảm\s+bảo\s+tuyệt\s+đối)(?!\w)` | Cam kết tuyệt đối hóa trong dịch vụ tài chính hoặc công nghệ | Luật Các TCTD & Bảo vệ NTD |
| `(?<!\w)(chuẩn\s+xác\s+nhất\|uy\s+tín\s+nhất)(?!\w)` | So sánh phẩm cấp dịch vụ mang tính tự xưng | Nghị định xử phạt quảng cáo |
| `(?<!\w)(hiện\s+đại\s+nhất\|tiên\s+tiến\s+nhất\s+thế\s+giới)(?!\w)` | Khẳng định công nghệ đỉnh cao thiếu kiểm chứng quốc tế | Luật Khoa học và Công nghệ |
