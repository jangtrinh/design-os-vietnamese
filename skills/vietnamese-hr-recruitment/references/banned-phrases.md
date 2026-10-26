<!-- vlc-disable: all -->

# Banned & Regulated Phrases in HR, Recruitment, & Labor Compliance (`design-os-vietnamese`)

In recruitment advertising, job descriptions (JD), employment contracts, and workplace communications, prohibited language directly breaches the Labor Code 2019 (**Bộ luật Lao động 45/2019/QH14**), Law on Advertising 2012, or the Law on Gender Equality.

---

## 1. Regulated Superlatives (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, employer branding communications claiming to be "best", "leading", or "#1" workplace without accredited third-party certification are unlawful.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|cao\|hấp\s+dẫn\|lý\s+tưởng\|nổi\s+bật\|uy\s+tín\|hàng\s+đầu)\s+nhất` | "best workplace / highest salary / most ideal company" | Common violation in recruitment banners |
| `duy\s+nhất` | "the only" | Specifically named in statute |
| `số\s*(?:một\|1)\b` | "number one" | Specifically named in statute |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |
| `môi\s+trường\s+làm\s+việc\s+số\s+1` | "number one workplace" | Prohibited claim without certified certification |
| `chế\s+độ\s+đãi\s+ngộ\s+tốt\s+nhất` | "best compensation and benefits" | Unsubstantiated superlative |
| `doanh\s+nghiệp\s+tuyển\s+dụng\s+hàng\s+đầu` | "leading recruitment enterprise" | Uncertified leadership claim |
| `mức\s+lương\s+cao\s+nhất\s+thị\s+trường` | "highest salary in the market" | Deceptive salary superlative |

**Compliant Rewrite Principle:**
Never use empty superlatives (`chế độ đãi ngộ tốt nhất Việt Nam`). State verified facts or accredited awards:
- ❌ `Công ty có môi trường làm việc tốt nhất ngành công nghệ`
- ✅ `Doanh nghiệp đạt chứng nhận Nơi làm việc Xuất sắc (Great Place to Work) năm 2025`

---

## 2. Prohibited Discriminatory, Punitive, & Toxic Phrasing

The following phrases are prohibited across job descriptions, offer letters, internal labor policies, and performance evaluations:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale |
|---|---|---|
| `chỉ tuyển nam` | `ưu tiên ứng viên có sức khỏe phù hợp tính chất công việc` | Bộ luật Lao động 2019 Điều 8 cấm phân biệt giới tính |
| `chỉ tuyển nữ` | `chào đón tất cả ứng viên đáp ứng năng lực chuyên môn` | Bộ luật Lao động 2019 Điều 8 cấm phân biệt giới tính |
| `yêu cầu chưa kết hôn` | `không phân biệt tình trạng hôn nhân của ứng viên` | Bộ luật Lao động 2019 Điều 8 cấm phân biệt tình trạng hôn nhân |
| `cam kết không mang thai` | *(bỏ hoàn toàn - vi phạm pháp luật)* | Bộ luật Lao động 2019 Điều 137 bảo vệ lao động thai sản |
| `không vướng bận gia đình` | `chủ động sắp xếp thời gian làm việc theo tính chất dự án` | Xâm phạm đời sống riêng tư và phân biệt đối xử |
| `ngoại hình ưa nhìn` | `tác phong chuyên nghiệp, lịch sự khi tiếp xúc khách hàng` | Phân biệt đối xử về ngoại hình trái pháp luật |
| `giữ bằng đại học gốc` | `kiểm tra đối chiếu văn bằng gốc và lưu bản sao chứng thực` | Bộ luật Lao động 2019 Điều 17 cấm giữ bản chính văn bằng |
| `giữ căn cước công dân gốc` | `đối chiếu bản gốc CCCD và lưu trữ bản chụp giấy tờ` | Bộ luật Lao động 2019 Điều 17 cấm giữ bản chính giấy tờ tùy thân |
| `phạt trừ lương` | `áp dụng các hình thức xử lý kỷ luật lao động theo luật định` | Bộ luật Lao động 2019 Điều 128 cấm phạt tiền, trừ lương |
| `tịch thu tiền đặt cọc` | *(bỏ hoàn toàn - trái pháp luật)* | Bộ luật Lao động 2019 Điều 17 cấm yêu cầu đặt cọc tiền |
| `lương thử việc 70%` | `tiền lương thử việc tối thiểu bằng 85% lương chính thức` | Bộ luật Lao động 2019 Điều 26 quy định sàn lương thử việc 85% |
| `lương thử việc 75%` | `tiền lương thử việc ít nhất 85% mức lương chính thức` | Vi phạm Điều 26 Bộ luật Lao động 2019 |
| `thử việc 3 tháng` | `thời gian thử việc tối đa không quá 60 ngày` | Điều 25 Bộ luật Lao động giới hạn thử việc 60 ngày (trừ quản lý) |
| `thử việc 90 ngày` | `thời gian thử việc tối đa 60 ngày đối với trình độ đại học` | Vi phạm trần 60 ngày thử việc theo Điều 25 |
| `lương thỏa thuận theo năng lực` | `mức lương thỏa thuận trong dải từ 20.000.000 ₫ đến 30.000.000 ₫ Gross` | Tránh diễn đạt mù mờ, thiếu minh bạch dải thu nhập |
| `lương hấp dẫn theo năng lực` | `dải thu nhập cạnh tranh theo năng lực và kết quả thực hiện` | JD hiện đại yêu cầu công khai dải thu nhập rõ ràng |
| `chịu được áp lực cực cao không giới hạn giờ giấc` | `kỹ năng quản lý thời gian và ưu tiên đầu việc hiệu quả` | Khẩu hiệu bóc lột, vi phạm quy định thời giờ làm việc |
| `coi công ty là nhà làm việc 24/7` | `tinh thần hợp tác trách nhiệm và gắn kết tập thể` | Tránh bình thường hóa văn hóa làm việc kiệt sức |
| `thái độ kém cỏi` | `chưa hoàn thành mục tiêu giao tiếp và hợp tác theo thỏa thuận` | Đánh giá SBI dựa trên hành vi cụ thể, tránh mạt sát cá nhân |
| `lười biếng` | `tỷ lệ bàn giao công việc đúng hạn trong kỳ đạt 65% (chưa đạt KPI)` | Đánh giá hiệu suất phải dùng dữ liệu đo lường định lượng |
| `thiếu năng lực bẩm sinh` | `cần tham gia khóa đào tạo chuyên sâu về kỹ năng phân tích dữ liệu` | Xúc phạm phẩm giá người lao động, thiếu tính xây dựng |
| `sẵn sàng OT không tính lương` | `thực hiện làm thêm giờ theo đúng quy định hưởng lương tăng ca` | Điều 98 BLLĐ 2019 quy định trả lương làm thêm giờ bắt buộc |
| `đuổi việc ngay lập tức` | `chấm dứt hợp đồng lao động theo quy trình luật định` | Dùng ngôn từ hành chính chuẩn mực, bảo đảm thủ tục pháp lý |
| `tự nguyện từ bỏ BHXH` | *(thỏa thuận vô hiệu trước pháp luật)* | Luật BHXH quy định tham gia bảo hiểm bắt buộc theo luật định |
| `cam kết không nhảy việc trong 3 năm` | `điều khoản bảo lưu thời hạn cam kết sau đào tạo chuyên sâu` | Điều 40 BLLĐ 2019 quy định hợp đồng đào tạo nghề rõ ràng |
| `trừ tiền chuyên cần nếu đi muộn 5 phút` | `ghi nhận tuân thủ kỷ luật lao động và khung giờ làm việc` | Không được dùng hình thức phạt tiền trừ lương |
| `nhân viên phải sẵn sàng nghe điện thoại sếp lúc nửa đêm` | `chế độ trực ca khẩn cấp kèm phụ cấp theo thỏa ước lao động` | Tôn trọng thời giờ nghỉ ngơi của người lao động |
| `lương bao gồm tất cả các khoản không đóng bảo hiểm` | `cơ cấu lương minh bạch gồm lương cơ bản đóng bảo hiểm và phụ cấp` | Gian lận trốn đóng BHXH bắt buộc là hành vi vi phạm pháp luật |
| `không được phép mang thai trong 2 năm đầu` | *(điều khoản vô hiệu)* | Vi phạm quyền con người và quyền thai sản phụ nữ |
| `tuyển dụng gấp chỉ nhận người trẻ dưới 25 tuổi` | `ưu tiên ứng viên có tinh thần học hỏi và sẵn sàng hội nhập` | Phân biệt đối xử về độ tuổi trong tuyển dụng |
| `cắt phép năm nếu không đạt chỉ tiêu` | `chế độ nghỉ hằng năm theo đúng quy định của Bộ luật Lao động` | Phép năm là quyền luật định, không thể tùy tiện cắt giảm |
| `thử việc không trả lương` | `trả lương thử việc ít nhất 85% lương chính thức` | Hành vi bóc lột sức lao động, vi phạm Bộ luật Lao động 2019 |
