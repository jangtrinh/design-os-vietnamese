<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese Universal Banned Phrases & Superlatives

> Universal anti-patterns, literal English calques, and regulated advertising superlatives loaded by `shared/scripts/validate_copy.py`.
> Individual skills under `skills/*/references/banned-phrases.md` extend this baseline with domain-specific patterns.

<!-- machine-readable: calques -->
| ❌ Cụm từ cấm / Lạm dụng | ✅ Cách diễn đạt tự nhiên | Gợi ý thay thế / Ngữ cảnh | Severity |
|---|---|---|---|
| làm ơn nhập của bạn mật khẩu | Vui lòng nhập mật khẩu của bạn | Sửa cả lỗi dịch máy "Please" và đảo ngược sở hữu cách "your password" | error |
| của bạn mật khẩu | mật khẩu của bạn | Đặt cụm sở hữu "của bạn" sau danh từ | error |
| của bạn tài khoản | tài khoản của bạn | Đặt cụm sở hữu "của bạn" sau danh từ | error |
| của bạn thông tin | thông tin của bạn | Đặt cụm sở hữu "của bạn" sau danh từ | error |
| làm ơn nhập | Vui lòng nhập | Dùng "Vui lòng" hoặc động từ mệnh lệnh trực tiếp | error |
| xin quý khách vui lòng tiến hành | Vui lòng | Cắt bỏ kính ngữ thừa và động từ phụ trợ | error |
| yêu cầu đã được tiến hành gửi thành công | Đã gửi yêu cầu | Bỏ thể bị động và từ phụ trợ tiến hành | error |
| bạn hãy nhấn vào nút | Chọn / Nhấn | Không mô tả thao tác vật lý hiển nhiên | error |
| oops đã có lỗi | Không thể xử lý yêu cầu | Tránh tiếng lóng dịch cẩu thả từ tiếng Anh | error |
| xin lỗi vì sự bất tiện này | Thử lại sau ít phút | Thay câu xin lỗi sáo rỗng bằng hướng dẫn khắc phục | error |
| tiến hành đăng nhập | Đăng nhập | Rút gọn nhãn nút hành động | error |
| tiến hành thanh toán | Thanh toán | Nút bấm phải ngắn gọn, trực diện | error |
| đã được lưu thành công | Đã lưu | Rút gọn thông báo toast | error |
| đã được xóa thành công | Đã xóa | Rút gọn thông báo toast | error |
| nhấn vào đây để xem chi tiết | Xem chi tiết | Tránh anti-pattern liên kết click here | error |
| viết ra giấy | ghi lại thành file / ghi thành luật | Calque “write it on paper” cho việc ghi quy tắc; nói rõ ghi vào đâu | warn |
| nằm trên đường đi | gắn vào quy trình / gắn vào bước … | Calque “sits on the path”; nói bước hoặc quy trình cụ thể | error |
| đặt lên đường đi | gắn vào quy trình / gắn vào bước … | Calque “place on the path”; nói bước hoặc quy trình cụ thể | error |
| giết process | kill process | Giữ nguyên thuật ngữ kỹ thuật “kill process” | error |
| giết tiến trình | kill process / dừng tiến trình | Giữ nguyên thuật ngữ kỹ thuật “kill process” | error |
| lần thử mù | thử mò | Calque “blind attempt” | error |
| khớp với danh tính | đúng chất | Calque “match the identity” | error |
| onboard được lên | mang sang / chuyển sang | Calque “get onboarded onto” | warn |
| onboard vào | mang sang / chuyển sang | Calque “onboard into” | warn |
| được giấu khỏi | phải giấu, … không được thấy | Calque “is hidden from”; dùng chủ động | warn |

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
