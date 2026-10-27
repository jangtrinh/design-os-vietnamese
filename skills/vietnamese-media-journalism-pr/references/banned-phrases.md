<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Vietnamese Media, Journalism & PR (`vietnamese-media-journalism-pr`)

In journalism, corporate public relations, press releases, and online news publication in Vietnam, violating the constitutional presumption of innocence, revealing child identity, self-proclaiming press status without a license under Decree 147/2024/NĐ-CP, or silently deleting inaccurate reports without formal correction breaches the Press Law 2016, Law on Children 2016, and the Constitution of Vietnam.

---

## 1. Regulated Superlatives & Sensationalism Claims (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11** and professional press conventions, unverified superlatives and sensational clickbait claims are strictly regulated:

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:uy\s+tín\|nhanh\|chính\s+xác\|nóng\|sốt\s+dẻo\|thu\s+hút\|lớn\|hấp\s+dẫn)\s+nhất` | "most reputable / fastest / hottest / most accurate" | Common violation in media self-promotion |
| `duy\s+nhất` | "the only" | Specifically prohibited by advertising statutes |
| `số\s*(?:một\|1)\b` | "number one" | Prohibited ranking claim |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without official award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited market ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign numeral superlative symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |
| `báo\s+điện\s+tử\s+số\s*1` | "number 1 online newspaper" | Prohibited ranking claim in media promotions |
| `kênh\s+thông\s+tin\s+uy\s+tín\s+nhất\s+việt\s+nam` | "most reputable news channel in Vietnam" | Unverified superlative ranking |
| `thương\s+hiệu\s+số\s*1\s+thị\s+trường` | "number 1 brand in market" | Superlative claim in corporate PR |
| `tin\s+tức\s+chính\s+xác\s+nhất` | "most accurate news" | Sensational media slogan |

---

## 2. Prohibited Phrases & Compliance Violations (`MEDJ001`–`MEDJ006`)

The following phrases are strictly prohibited across news articles, investigative reports, press corrections, and crisis PR statements:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale | Severity |
|---|---|---|---|
| `tên tội phạm vừa bị tạm giữ` | `nghi phạm vừa bị cơ quan công an tạm giữ để điều tra` | Vi phạm suy đoán vô tội (Hiến pháp 2013 Đ31 & BLTTHS 2015 Đ13) | error |
| `hung thủ vừa bị bắt giữ` | `nghi phạm vừa bị lực lượng chức năng bắt giữ` | Vi phạm suy đoán vô tội khi chưa có bản án kết tội của Tòa án | error |
| `kẻ giết người vừa bị khởi tố` | `bị can vừa bị khởi tố để điều tra về hành vi giết người` | Chưa có bản án kết tội có hiệu lực pháp luật của Tòa án | error |
| `bắt tạm giam tên tội phạm` | `bắt tạm giam bị can để phục vụ công tác điều tra` | Sử dụng danh xưng tội phạm trước khi xét xử vi phạm Hiến pháp | error |
| `kẻ lừa đảo vừa bị triệu tập` | `đối tượng liên quan vừa bị triệu tập để lấy lời khai` | Vi phạm nguyên tắc suy đoán vô tội trong tố tụng hình sự | error |
| `chỉ cần gỡ bài âm thầm không cần cải chính` | `đăng thông báo cải chính và xin lỗi công khai theo Điều 42 Luật Báo chí 2016` | Nghiêm cấm gỡ bài âm thầm không cải chính, xin lỗi | error |
| `gỡ bài khỏi hệ thống mà không cần đăng cải chính` | `thực hiện quy trình cải chính, xin lỗi và nêu rõ bài viết gốc theo luật` | Vi phạm Điều 42 Luật Báo chí 2016 | error |
| `âm thầm gỡ bỏ bài viết sai sự thật mà không xin lỗi` | `đăng thông báo cải chính và xin lỗi bạn đọc cùng đối tượng bị ảnh hưởng` | Vi phạm nghĩa vụ pháp lý của cơ quan báo chí | error |
| `trang thông tin điện tử tổng hợp tự sản xuất tin bài điều tra` | `dẫn lại nguyên văn tin bài từ cơ quan báo chí chính thống theo giấy phép ICP` | Vi phạm Nghị định 147/2024/NĐ-CP và Luật Báo chí 2016 | error |
| `tòa soạn báo điện tử thuộc giấy phép icp` | `ban quản trị trang thông tin điện tử tổng hợp` | Trang ICP không được mạo danh tòa soạn cơ quan báo chí | error |
| `tòa soạn chuyên trang trực thuộc trang thông tin điện tử tổng hợp` | `chuyên trang tổng hợp thông tin theo giấy phép ICP` | Cấm hành vi 'báo hóa' trang thông tin điện tử tổng hợp | error |
| `kiện đến cùng mà không cần xác minh` | `phối hợp với các bên liên quan để xác minh khách quan và giải quyết khiếu nại` | Phát ngôn xử lý khủng hoảng mang tính đe dọa, thiếu xây dựng | error |
| `khách hàng bịa đặt thông tin để phá hoại` | `công ty đang tiếp nhận thông tin phản ánh và tiến hành kiểm tra quy trình nội bộ` | Đổ lỗi và công kích khách hàng trong xử lý khủng hoảng PR | error |
| `sự cố do người tiêu dùng thiếu hiểu biết` | `doanh nghiệp xin nhận trách nhiệm và tăng cường hướng dẫn sử dụng sản phẩm an toàn` | Vi phạm đạo đức truyền thông và quan hệ công chúng | error |
| `công ty không có trách nhiệm giải thích cho khách hàng` | `công ty cam kết minh bạch thông tin và cung cấp văn bản giải trình chi tiết` | Trốn tránh trách nhiệm giải trình của doanh nghiệp | error |
| `đăng ảnh rõ mặt học sinh 12 tuổi` | `làm mờ khuôn mặt và bảo mật thông tin trẻ em dưới 16 tuổi theo Điều 21 Luật Trẻ em 2016` | Vi phạm quyền bí mật đời sống riêng tư của trẻ em | error |
| `tiết lộ địa chỉ nhà và lớp học của em bé` | `bảo mật tuyệt đối thông tin nhận dạng trẻ vị thành niên theo Nghị định 56/2017/NĐ-CP` | Hành vi nghiêm cấm trong thông tin truyền thông | error |
| `công bố danh tính nạn nhân dưới 16 tuổi` | `viết tắt họ tên và che mờ hình ảnh nhận diện của trẻ em` | Vi phạm Điều 21 Luật Trẻ em 2016 | error |

---

## 3. Mandatory Statutory Disclaimers & Formats in Media

1. **Thông báo Cải chính và Xin lỗi (Điều 42 Luật Báo chí 2016):**
   - Tiêu đề văn bản bắt buộc phải có đầy đủ cụm từ:
     `"Thông báo Cải chính và Xin lỗi"`
   - Bắt buộc phải nêu rõ: Tên bài viết gốc, ngày tháng xuất bản/phát sóng, nội dung thông tin sai sự thật, sự thật đã được kiểm chứng, và lời xin lỗi chân thành gửi tới bạn đọc, tổ chức, hoặc cá nhân có liên quan.
2. **Quy định đối với Trang thông tin điện tử tổng hợp ICP (Nghị định 147/2024/NĐ-CP):**
   - Phải ghi rõ nguồn tin gốc: `"Theo [Tên cơ quan báo chí cấp phép dẫn nguồn]"` kèm đường dẫn liên kết (hyperlink) trỏ trực tiếp đến bài viết gốc.
   - Bắt buộc ghi rõ số Giấy phép thiết lập trang thông tin điện tử tổng hợp và tên cơ quan cấp phép ở chân trang.
3. **Bảo vệ quyền bí mật đời sống riêng tư của trẻ em (Điều 21 Luật Trẻ em 2016):**
   - Mọi hình ảnh trẻ em dưới 16 tuổi trong các vụ việc tiêu cực, bạo lực, hoặc vi phạm pháp luật bắt buộc phải được che mờ toàn bộ khuôn mặt và thay đổi họ tên bằng chữ viết tắt (ví dụ: `cháu N.V.A (12 tuổi)`).
