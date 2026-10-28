<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Vietnamese InfoSec & Cybersecurity (`vietnamese-cybersecurity-infosec`)

In cybersecurity incident management, regulatory breach reporting under Law 91/2025/QH15 and Decree 356/2025/NĐ-CP (PDPD), and system classification under Decree 85/2016/NĐ-CP and Circular 12/2022/TT-BTTTT, using fabricated security levels, soliciting user credentials, or promising impossible absolute security carries statutory administrative liabilities.

---

## 1. Regulated Superlatives & Absolute Security Claims (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11** and cybersecurity scientific principles, claiming absolute invulnerability or uncertified rankings is prohibited:

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:bảo\s+mật\|an\s+toàn\|mạnh\|nhanh\|tối\s+tân\|hiện\s+đại\|uy\s+tín\|chuẩn)\s+nhất` | "most secure / safest / strongest / fastest" | Common violation in InfoSec vendor promotions |
| `duy\s+nhất` | "the only" | Specifically prohibited by advertising statutes |
| `số\s*(?:một\|1)\b` | "number one" | Prohibited ranking claim |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without official award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign numeral superlative symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |
| `an\s+toàn\s+tuyệt\s+đối\s+100\s*%` | "100% absolute security" | Scientifically unfounded claim in cybersecurity |
| `miễn\s+nhiễm\s+100\s*%\s+với\s+mọi\s+mã\s+độc` | "100% immune to all malware" | Prohibited absolute security claim |
| `chống\s+tấn\s+công\s+bất\s+khả\s+xâm\s+phạm` | "impenetrable / invulnerable" | Misleading marketing claim |
| `hệ\s+thống\s+bảo\s+mật\s+số\s*1` | "number 1 security system" | Unverified superlative ranking |

---

## 2. Prohibited Phrases & Compliance Violations (`SEC001`–`SEC006`)

The following phrases are strictly prohibited across incident reports, breach notifications to Department A05, CVE advisories, and SOC alerts:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale | Severity |
|---|---|---|---|
| `an toàn thông tin cấp độ 6` | `hệ thống thông tin cấp độ 5 (cấp độ cao nhất theo luật định)` | Nghị định 85/2016/NĐ-CP & TT 12/2022/TT-BTTTT chỉ có Cấp độ 1–5 | error |
| `attt cấp độ 6` | `an toàn hệ thống thông tin cấp độ 5` | Không tồn tại cấp độ 6 trong quy định pháp luật Việt Nam | error |
| `tiêu chuẩn bảo mật cấp độ 6` | `tiêu chuẩn an toàn thông tin cấp độ 5` | Vi phạm quy chuẩn thẩm định an toàn hệ thống thông tin | error |
| `tiêu chuẩn bảo mật cấp độ 7` | `an toàn hệ thống thông tin cấp độ 5` | Khống chế tối đa theo luật là Cấp độ 5 | error |
| `báo cáo sự cố dữ liệu sau 5 ngày` | `thông báo vi phạm tới cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) chậm nhất 72 giờ` | Vi phạm Điều 23 Luật 91/2025/QH15 | error |
| `thời hạn thông báo sự cố là 7 ngày` | `thời hạn thông báo tới cơ quan quản lý là trong vòng 72 giờ` | Vi phạm Điều 23 Luật 91/2025/QH15 | error |
| `thời hạn báo cáo vi phạm là 5 ngày` | `thời hạn gửi thông báo theo Mẫu số 08 (NĐ 356/2025) là chậm nhất 72 giờ` | Vi phạm Điều 23 Luật 91/2025/QH15 | error |
| `vui lòng gửi mật khẩu cho quản trị viên` | `quản trị viên không bao giờ yêu cầu người dùng cung cấp mật khẩu` | Vi phạm nguyên tắc bảo mật thông tin xác thực | error |
| `gửi mã otp để xác minh sự cố` | `tuyệt đối không chia sẻ mã OTP với bất kỳ ai, kể cả nhân viên an ninh mạng` | Cảnh báo giả mạo, phòng ngừa tấn công phi kỹ thuật | error |
| `cung cấp mã pin để hỗ trợ kỹ thuật` | `ngân hàng/hệ thống không bao giờ yêu cầu cung cấp mã PIN` | Quy tắc an toàn định danh người dùng | error |
| `gửi số bảo mật cvv để mở khóa tài khoản` | `tuyệt đối không nhập số CVV trên các kênh không bảo mật` | Bảo vệ thông tin tài chính cá nhân nhạy cảm | error |
| `dữ liệu sức khỏe là dữ liệu cá nhân cơ bản` | `dữ liệu sức khỏe là dữ liệu cá nhân nhạy cảm theo Điều 4 Nghị định 356/2025/NĐ-CP` | Phân loại sai cấp độ bảo vệ dữ liệu nhạy cảm | error |
| `thông tin tài khoản ngân hàng là dữ liệu cơ bản` | `thông tin tài khoản và số dư ngân hàng là dữ liệu cá nhân nhạy cảm` | Vi phạm phân loại dữ liệu theo Điều 4 Nghị định 356/2025/NĐ-CP | error |
| `dữ liệu sinh trắc học là dữ liệu cơ bản` | `dữ liệu sinh trắc học là dữ liệu cá nhân nhạy cảm bắt buộc áp dụng biện pháp bảo vệ tăng cường` | Vi phạm Điều 4 Nghị định 356/2025/NĐ-CP | error |
| `hệ thống miễn nhiễm 100% với hacker` | `áp dụng mô hình phòng thủ theo chiều sâu để giảm thiểu tối đa rủi ro an ninh mạng` | Cấm cam kết bảo mật tuyệt đối phản khoa học | error |
| `không bao giờ bị tấn công mạng` | `chủ động giám sát, phát hiện và sẵn sàng phương án ứng cứu sự cố 24/7` | Tuyên bố phi thực tế trong an ninh mạng | error |
| `không cần vá lỗ hổng vì đã có tường lửa` | `kịp thời cập nhật bản vá bảo mật theo khuyến nghị của nhà sản xuất` | Nguy cơ khai thác lỗ hổng nghiêm trọng | error |
| `giấu kín sự cố để tránh ảnh hưởng uy tín` | `thực hiện quy trình báo cáo sự cố theo Điều 23 Luật 91/2025/QH15 và Luật ATTT mạng` | Hành vi che giấu sự cố an ninh mạng bị nghiêm cấm | error |

---

## 3. Mandatory Statutory Disclaimers in InfoSec

1. **Thông báo vi phạm dữ liệu cá nhân gửi cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Luật 91/2025/QH15 Điều 23; Mẫu số 08 NĐ 356/2025/NĐ-CP):**
   - Thông báo vi phạm bắt buộc phải được gửi theo Mẫu số 08 (Nghị định 356/2025/NĐ-CP Điều 28 khoản 2) tới:
     `Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (A05) - Bộ Công an trong thời hạn 72 giờ kể từ khi phát hiện vi phạm.`
2. **Cảnh báo an toàn thông tin & khuyến nghị bản vá (CVE Advisories):**
   - Mọi cảnh báo bảo mật phải ghi rõ:
     `Mức độ nghiêm trọng (Điểm CVSS) và Biện pháp khắc phục / Hướng dẫn áp dụng bản vá từ nhà cung cấp.`
3. **Chống lừa đảo và bảo vệ thông tin xác thực (Anti-Phishing Baseline):**
   - Bắt buộc ghi nhận khuyến cáo:
     `"Hệ thống và cán bộ quản trị không bao giờ yêu cầu người dùng cung cấp mật khẩu, mã OTP, mã PIN hay số bảo mật CVV qua điện thoại, email hoặc tin nhắn."`
