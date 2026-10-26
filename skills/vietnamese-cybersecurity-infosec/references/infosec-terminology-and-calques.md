<!-- vlc-disable: all -->

# Vietnamese InfoSec & Cybersecurity Terminology, Glossaries, and Calque Blocklist

> Authoritative linguistic and technical baseline aligned with the National Cyber Security Centre (NCSC Việt Nam), VNCERT/CC, and Ministry of Information and Communications standard practice.

---

## 1. Machine-Readable Calque & Translationese Blocklist

<!-- machine-readable: calques -->
| ❌ Thuật ngữ dịch thô / Lạm dụng | ✅ Thuật ngữ InfoSec chuẩn | Thuật ngữ tiếng Anh gốc | Ghi chú & Căn cứ kỹ thuật |
|---|---|---|---|
| cuộc tấn công câu cá | tấn công giả mạo / lừa đảo trực tuyến | Phishing attack | Dịch máy thô từ "fishing/phishing"; chuẩn VNCERT dùng "tấn công giả mạo" |
| phần mềm đòi tiền chuộc / mã độc chuộc lỗi | mã độc tống tiền | Ransomware | Chuẩn Cục An toàn thông tin và A05 Bộ Công an dùng "mã độc tống tiền" |
| kỹ thuật xã hội | tấn công phi kỹ thuật / thao túng tâm lý | Social engineering | Dịch vụng nghĩa chữ "social"; bản chất là phi kỹ thuật, nhắm vào yếu tố con người |
| bề mặt cuộc tấn công | bề mặt tấn công | Attack surface | Bỏ từ nối "cuộc"; chuẩn công nghệ là "bề mặt tấn công" |
| tường lửa thế hệ tiếp theo | tường lửa thế hệ mới | Next-Generation Firewall (NGFW) | Dịch sát nghĩa chữ "next"; ngữ pháp chuẩn tiếng Việt là "thế hệ mới" |
| kiểm toán cây bút | kiểm thử xâm nhập / đánh giá thâm nhập | Penetration testing (Pentest) | Lỗi dịch thô từ "pen/pencil" thay vì chữ viết tắt của penetration |
| tấn công từ chối dịch vụ phân tán thô sơ | tấn công từ chối dịch vụ phân tán | Distributed Denial of Service (DDoS) | Giữ nguyên cấu trúc thuật ngữ chuẩn ATTT mạng |
| tiêm nhiễm mã độc | lây nhiễm mã độc | Malware infection | Tránh dùng từ "tiêm nhiễm" mang sắc thái ẩn dụ văn học |
| cửa hậu | cửa sau / backdoor | Backdoor | Trong văn cảnh kỹ thuật dùng "cửa sau" hoặc giữ thuật ngữ quốc tế backdoor |

---

## 2. Authoritative Cybersecurity Terminology Glossary

| Khái niệm tiếng Anh | Thuật ngữ tiếng Việt chuẩn | Định nghĩa & Ngữ cảnh sử dụng |
|---|---|---|
| **Vulnerability** | Lỗ hổng bảo mật | Điểm yếu trong hệ thống cho phép kẻ tấn công khai thác trái phép |
| **Exploit** | Khai thác lỗ hổng | Đoạn mã hoặc kỹ thuật lợi dụng lỗ hổng bảo mật để thực thi hành vi xâm nhập |
| **Zero-day** | Lỗ hổng chưa có bản vá / Lỗ hổng zero-day | Lỗ hổng chưa được nhà sản xuất công bố hoặc phát hành bản vá chính thức |
| **Patch / Workaround** | Bản vá / Biện pháp giảm thiểu | Mã cập nhật phần mềm khắc phục lỗ hổng hoặc cấu hình thay thế tạm thời |
| **Multi-Factor Authentication (MFA)** | Xác thực đa yếu tố | Biện pháp bảo vệ danh tính yêu cầu từ 2 yếu tố xác thực trở lên |
| **Brute-Force Attack** | Tấn công vét cạn / Dò quét mật khẩu | Phương pháp thử toàn bộ các hoán vị mật khẩu khả dĩ |
| **Credential Stuffing** | Tấn công nhồi thông tin xác thực | Sử dụng danh sách tài khoản lộ lọt từ hệ thống khác để đăng nhập tự động |
| **Man-in-the-Middle (MitM)** | Tấn công kẻ đứng giữa | Can thiệp, nghe lén hoặc sửa đổi gói tin trên đường truyền mạng |
| **Data Loss Prevention (DLP)** | Ngăn chặn thất thoát dữ liệu | Giải pháp giám sát và ngăn chặn truyền dữ liệu nhạy cảm ra ngoài |
| **Security Operations Center (SOC)** | Trung tâm điều hành an toàn thông tin | Bộ phận chuyên trách giám sát, phát hiện và phản ứng sự cố an ninh mạng 24/7 |
| **Threat Intelligence** | Thông tin tình báo mối đe dọa | Dữ liệu về các chiến dịch, tác nhân và chỉ số xâm hại (IoC) |
| **Security Advisory** | Cảnh báo an toàn thông tin | Văn bản thông báo chính thức về lỗ hổng, nguy cơ và giải pháp xử lý |
