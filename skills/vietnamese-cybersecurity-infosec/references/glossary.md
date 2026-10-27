<!-- vlc-disable: all -->

# Vietnamese InfoSec & Cybersecurity Terminology Glossary (`vietnamese-cybersecurity-infosec`)

This glossary provides standardized Vietnamese cybersecurity, SOC operations, threat intelligence, and vulnerability disclosure terminology aligned with the National Cyber Security Centre (NCSC Việt Nam), VNCERT/CC, and Ministry of Public Security Department A05.

The table below is parsed by `validate_copy.py` at runtime; each row acts as an active linting rule firing `CAL001` with the declared severity.

---

## 1. Machine-Readable Cybersecurity, SOC & Vulnerability Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| phishing attack | `cuộc tấn công câu cá` | `tấn công giả mạo` / `lừa đảo trực tuyến` | Chuẩn thuật ngữ VNCERT/CC & NCSC | error |
| phishing attack | `tấn công câu cá` | `tấn công giả mạo` / `lừa đảo trực tuyến` | Dịch máy thô ráp từ fishing/phishing | error |
| ransomware | `phần mềm đòi tiền chuộc` | `mã độc tống tiền` | Chuẩn Cục ATTT & A05 Bộ Công an | error |
| ransomware | `mã độc chuộc lỗi` | `mã độc tống tiền` | Dịch sai lệch bản chất tống tiền của ransomware | error |
| ransomware | `phần mềm chuộc tiền` | `mã độc tống tiền` | Tránh dịch từ vụng về | error |
| social engineering | `kỹ thuật xã hội` | `tấn công phi kỹ thuật` / `thao túng tâm lý` | Chuẩn thuật ngữ an toàn thông tin chuyên ngành | error |
| attack surface | `bề mặt cuộc tấn công` | `bề mặt tấn công` | Bỏ từ nối 'cuộc' theo quy chuẩn công nghệ | error |
| next-generation firewall | `tường lửa thế hệ tiếp theo` | `tường lửa thế hệ mới` | Ngữ pháp chuẩn công nghệ tiếng Việt (NGFW) | error |
| penetration testing | `kiểm toán cây bút` | `kiểm thử xâm nhập` / `đánh giá thâm nhập` | Lỗi dịch thô từ pen/pencil thay vì penetration | error |
| penetration testing | `thử nghiệm bút` | `kiểm thử xâm nhập` | Dịch máy thô ngô nghê | error |
| brute force attack | `tấn công vũ lực tàn bạo` | `tấn công vét cạn` / `dò quét mật khẩu` | Kỹ thuật mật mã học và an toàn hệ thống | error |
| credential stuffing | `nhồi nhét thông tin đăng nhập thô` | `tấn công nhồi thông tin xác thực` | Khai thác danh sách tài khoản rò rỉ | error |
| man-in-the-middle attack | `tấn công người đàn ông ở giữa` | `tấn công kẻ đứng giữa` | Dịch thô cụm Man-in-the-Middle (MitM) | error |
| denial of service | `từ chối cung cấp dịch vụ máy tính` | `tấn công từ chối dịch vụ` / `DoS` | Thuật ngữ chuẩn Luật ATTT mạng 2015 | error |
| distributed denial of service | `tấn công từ chối dịch vụ phân tán thô sơ` | `tấn công từ chối dịch vụ phân tán` / `DDoS` | Quy chuẩn thuật ngữ kỹ thuật NCSC | error |
| zero-day vulnerability | `lỗ hổng ngày số không` | `lỗ hổng zero-day` / `lỗ hổng chưa có bản vá` | Lỗ hổng bảo mật chưa được công bố bản vá | error |
| data breach | `vi phạm dữ liệu đổ vỡ` | `sự cố lộ lọt dữ liệu` / `vi phạm dữ liệu cá nhân` | Nghị định 13/2023/NĐ-CP | error |
| data exfiltration | `lọc dữ liệu bất hợp pháp` | `trích xuất dữ liệu trái phép` / `thất thoát dữ liệu` | Hành vi đánh cắp dữ liệu ra ngoài mạng nội bộ | error |
| privilege escalation | `leo thang đặc quyền chính trị` | `leo thang đặc quyền` / `nâng quyền trái phép` | Kỹ thuật chiếm quyền root/administrator | error |
| security operations center | `trung tâm hoạt động bảo an` | `trung tâm điều hành an toàn thông tin` / `SOC` | Tổ chức giám sát an ninh mạng 24/7 | error |
| multi-factor authentication | `xác thực nhiều nhân tố cá nhân` | `xác thực đa yếu tố` / `MFA` | Biện pháp bảo vệ danh tính nhiều lớp | error |
| threat intelligence | `tình báo đe dọa quân sự` | `thông tin tình báo mối đe dọa` / `CTI` | Thuật ngữ chuyên sâu trong SOC/CSIRT | error |
| malware infection | `tiêm nhiễm mã độc` | `lây nhiễm mã độc` | Tránh dùng ẩn dụ văn học không chuẩn xác | warn |
| air gap | `khoảng cách không khí mạng` | `mạng cách ly vật lý` / `air-gap` | Bảo vệ hệ thống điều khiển công nghiệp ICS/SCADA | warn |
| honeypot | `nồi mật ong kỹ thuật số` | `hệ thống bẫy tấn công` / `honeypot` | Hệ thống mồi nhử kẻ tấn công | warn |
| lateral movement | `chuyển động bên hông mạng` | `di chuyển ngang trong mạng` | Kỹ thuật di chuyển nội bộ sau khi xâm nhập | warn |
| supply chain attack | `tấn công chuỗi cung cấp hàng hóa` | `tấn công chuỗi cung ứng` | Tấn công qua nhà cung cấp phần mềm bên thứ ba | warn |
| command and control | `chỉ huy và kiểm soát quân sự` | `máy chủ điều khiển` / `C2 server` | Hạ tầng kiểm soát botnet/malware | warn |
| incident response | `phản hồi sự cố bị động` | `ứng cứu sự cố an toàn thông tin mạng` | Thuật ngữ chuẩn Thông tư 20/2017/TT-BTTTT | error |
| digital forensics | `pháp y kỹ thuật số tử thi` | `điều tra số` / `giám định kỹ thuật số` | Giám định và trích xuất chứng cứ số | warn |
| security posture | `tư thế an ninh mạng` | `trạng thái an toàn thông tin` / `mức độ sẵn sàng bảo mật` | Đánh giá tổng thể an ninh hệ thống | warn |
| endpoint detection and response | `phát hiện điểm cuối và trả lời` | `phát hiện và phản ứng điểm cuối` / `EDR` | Giải pháp an toàn máy trạm | warn |
