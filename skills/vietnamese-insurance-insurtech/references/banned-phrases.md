<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Vietnamese Insurance & Bancassurance (`vietnamese-insurance-insurtech`)

In insurance, InsurTech, and bancassurance distribution channels in Vietnam, misleading advertising, failure to disclose investment risks, concealing exclusion clauses, and coercive cross-selling carry severe statutory penalties under the Law on Insurance Business 2022 (Luật Kinh doanh bảo hiểm số 08/2022/QH15), Ministry of Finance Circular 67/2023/TT-BTC, Law on Advertising 2012, and the Law on Credit Institutions 2024.

---

## 1. Regulated Superlatives (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, insurance advertisements and sales illustrations cannot use superlatives without documented, accredited certification:

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|nhanh\|uy\s+tín\|bảo\s+vệ\|an\s+toàn\|lãi\s+suất\s+cao\|rẻ\|đáng\s+tin\s+cậy)\s+nhất` | "best / fastest / safest / cheapest / highest return" | Common violation in insurance marketing slogans |
| `duy\s+nhất` | "the only" | Specifically prohibited by advertising statutes |
| `số\s*(?:một\|1)\b` | "number one" | Prohibited ranking claim |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without official award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited market ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign numeral superlative symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |
| `công\s+ty\s+bảo\s+hiểm\s+tốt\s+nhất` | "best insurance company" | Unverified superlative marketing slogan |
| `bảo\s+hiểm\s+nhân\s+thọ\s+số\s*1` | "number 1 life insurance" | Prohibited ranking claim in financial promotion |
| `quyền\s+lợi\s+cao\s+nhất\s+thị\s+trường` | "highest benefit on the market" | Unverified competitive comparison |
| `cam\s+kết\s+sinh\s+lời\s+tuyệt\s+đối` | "absolute return guarantee" | Unlawful guarantee in investment-linked insurance |

---

## 2. Prohibited Phrases & Deceptive Slogans (`INS001`–`INS006`)

The following phrases are strictly prohibited across insurance illustrations, customer onboarding journeys, bancassurance sales scripts, and policy certificates:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale | Severity |
|---|---|---|---|
| `tiết kiệm ngân hàng cam kết lãi suất` | `sản phẩm bảo hiểm nhân thọ liên kết đầu tư` | Vi phạm TT 67/2023/TT-BTC & Luật KDBH 2022 (cấm mạo danh tiết kiệm) | error |
| `lợi nhuận cố định 100% không rủi ro` | `kết quả đầu tư phụ thuộc vào hiệu quả của quỹ liên kết đơn vị` | Cấm cam kết lợi nhuận cố định trong bảo hiểm liên kết đầu tư (TT 67/2023) | error |
| `tiết kiệm đầu tư cam kết lợi nhuận cố định` | `sản phẩm bảo hiểm liên kết chung tích lũy tài khoản theo lãi suất công bố thực tế` | Cấm đánh tráo khái niệm bảo hiểm với tiền gửi tiết kiệm ngân hàng | error |
| `tiết kiệm ngân hàng lãi suất cam kết` | `hợp đồng bảo hiểm nhân thọ kết hợp đầu tư` | Vi phạm quy định tư vấn bảo hiểm qua ngân hàng (Bancassurance) | error |
| `bắt buộc mua bảo hiểm nhân thọ mới được giải ngân` | `việc tham gia bảo hiểm là hoàn toàn tự nguyện theo nhu cầu của khách hàng` | Vi phạm Thông tư 67/2023/TT-BTC và Luật Các tổ chức tín dụng 2024 | error |
| `ép buộc mua bảo hiểm để duyệt vay` | `thẩm định khoản vay độc lập với việc tham gia bảo hiểm tự nguyện` | Hành vi nghiêm cấm trong hoạt động đại lý bảo hiểm của tổ chức tín dụng | error |
| `không mua bảo hiểm thì không giải ngân` | `khoản vay được giải ngân khi đáp ứng đủ điều kiện tín dụng theo luật` | Vi phạm điều cấm về liên kết bắt buộc gói vay tín dụng | error |
| `không cần đọc điều khoản loại trừ` | `đại lý có nghĩa vụ giải thích rõ ràng, đầy đủ các trường hợp loại trừ trách nhiệm bảo hiểm` | Vi phạm Điều 19 Luật Kinh doanh bảo hiểm 2022 | error |
| `chi trả mọi rủi ro không loại trừ` | `quyền lợi bảo hiểm được chi trả theo quy tắc và điều khoản đã thỏa thuận` | Quảng cáo sai sự thật, che giấu điều khoản loại trừ luật định | error |
| `cam kết chi trả 100% không loại trừ` | `chi trả bồi thường theo hạn mức và phạm vi hợp đồng bảo hiểm` | Vi phạm quy định về nghĩa vụ minh bạch thông tin hợp đồng | error |
| `thời gian cân nhắc 7 ngày` | `thời gian cân nhắc tham gia bảo hiểm là 21 ngày` | Vi phạm Điều 35 Luật Kinh doanh bảo hiểm 2022 (tối thiểu 21 ngày) | error |
| `thời gian cân nhắc 14 ngày` | `thời gian cân nhắc tham gia bảo hiểm 21 ngày` | Vi phạm Điều 35 Luật Kinh doanh bảo hiểm 2022 | error |
| `không được hủy hợp đồng sau khi ký` | `bên mua bảo hiểm có quyền từ chối tiếp tục tham gia trong thời gian cân nhắc 21 ngày` | Xâm phạm quyền từ chối tham gia của bên mua bảo hiểm | error |
| `thời hạn bồi thường 60 ngày` | `thời hạn giải quyết bồi thường là 15 ngày kể từ ngày nhận đủ hồ sơ hợp lệ` | Vi phạm thời hạn giải quyết quyền lợi theo Điều 31 Luật KDBH 2022 | error |
| `thời hạn bồi thường 90 ngày` | `thời hạn chi trả quyền lợi tối đa không quá 30 ngày trong trường hợp cần xác minh` | Trái với quy định khống chế thời gian bồi thường tối đa tại Điều 31 | error |
| `tự động trích nợ mua bảo hiểm khi giải ngân` | `chỉ trích thu phí khi có văn bản ủy quyền hợp pháp của khách hàng` | Vi phạm quy chế quản lý tài khoản thanh toán và TT 67/2023 | error |
| `bảo hiểm lãi suất gấp đôi ngân hàng` | `sản phẩm bảo hiểm kết hợp đầu tư với quyền lợi bảo vệ và tích lũy` | Truyền thông thổi phồng, lừa dối người tham gia bảo hiểm | error |
| `rút vốn linh hoạt như sổ tiết kiệm` | `rút một phần giá trị tài khoản theo quy định của hợp đồng bảo hiểm liên kết chung` | Gây nhầm lẫn nghiêm trọng giữa giá trị tài khoản bảo hiểm và tiền gửi tiết kiệm | error |

---

## 3. Mandatory Statutory Disclaimers in Insurance

1. **Bảo hiểm liên kết đầu tư (Thông tư 67/2023/TT-BTC Điều 16):**
   - Tài liệu minh họa và sản phẩm trên ứng dụng số phải hiển thị rõ thông báo:
     `"Sản phẩm bảo hiểm liên kết đầu tư không phải là sản phẩm tiền gửi tiết kiệm của ngân hàng. Kết quả đầu tư của các quỹ liên kết đơn vị không được bảo đảm và bên mua bảo hiểm tự chịu toàn bộ rủi ro đầu tư."`
2. **Thời gian cân nhắc 21 ngày (Luật KDBH 2022 Điều 35):**
   - Hợp đồng bảo hiểm nhân thọ thời hạn trên 01 năm bắt buộc phải ghi rõ:
     `"Bên mua bảo hiểm có thời gian cân nhắc tham gia bảo hiểm là 21 ngày kể từ ngày nhận được hợp đồng bảo hiểm."`
3. **Nghĩa vụ giải thích điều khoản loại trừ (Luật KDBH 2022 Điều 19):**
   - Mọi giấy chứng nhận và tóm tắt hợp đồng phải có phần:
     `"Điều khoản loại trừ trách nhiệm bảo hiểm: Doanh nghiệp bảo hiểm không chịu trách nhiệm bồi thường trong các trường hợp được quy định chi tiết tại Quy tắc bảo hiểm đính kèm."`
