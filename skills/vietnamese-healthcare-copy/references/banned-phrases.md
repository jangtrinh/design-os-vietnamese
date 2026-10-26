<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Healthcare & Medical Communication (`design-os-vietnamese`)

In healthcare, hospital, clinic, pharmacy, and dietary supplement (TPCN) communications, prohibited language carries severe statutory penalties under the Law on Advertising 2012, Law on Medical Examination and Treatment 2023, Law on Pharmacy 2016, and Decree 15/2018/NĐ-CP.

---

## 1. Regulated Superlatives (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, using superlatives without valid documentary certification from a competent state agency or accredited independent authority is illegal.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|nhanh\|uy\s+tín\|hiệu\s+quả\|an\s+toàn\|hiện\s+đại\|chuyên\s+nghiệp\|chuẩn\|rẻ)\s+nhất` | "best / safest / most modern / most effective / cheapest" | Common violation in clinic and hospital promotions |
| `duy\s+nhất` | "the only" | Specifically named in statute |
| `số\s*(?:một\|1)\b` | "number one" | Specifically named in statute |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without official award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |
| `hàng\s+đầu\s+việt\s+nam` | "leading in Vietnam" | Common unverified hospital marketing claim |
| `chuẩn\s+quốc\s+tế\s+duy\s+nhất` | "the only international standard" | Unverified monopoly claim |
| `tuyệt\s+đối\s+100\s*%` | "absolute 100%" | Unfounded perfection claim in medicine |
| `bệnh\s+viện\s+số\s*1` | "number 1 hospital" | Prohibited advertising slogan |
| `phòng\s+khám\s+tốt\s+nhất` | "best clinic" | Unverified superlative claim |

**Compliant Rewrite Principle:**
Never use empty superlatives (`phòng khám tốt nhất Hà Nội`, `bác sĩ uy tín nhất`). State verified credentials, accreditations, and factual metrics:
- ❌ `Bệnh viện đa khoa tốt nhất khu vực phía Nam`
- ✅ `Bệnh viện đa khoa đạt chuẩn chất lượng quốc tế JCI với 24 chuyên khoa lâm sàng`

---

## 2. Prohibited Slogans & Curative Claims (`MED002`, `MED005`, `MED006`)

The following phrases are strictly prohibited across hospital landing pages, clinic ads, social media posts, and health supplement descriptions:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale |
|---|---|---|
| `thần dược trị bách bệnh` | `sản phẩm hỗ trợ sức khỏe` | Nghiêm cấm quảng cáo mê tín, sai sự thật (Luật Dược 2016) |
| `chữa khỏi hoàn toàn 100%` | `hỗ trợ cải thiện triệu chứng và kiểm soát bệnh` | Nghiêm cấm cam kết khỏi bệnh 100% trong y khoa (Luật KCB 2023) |
| `điều trị dứt điểm vĩnh viễn` | `phác đồ điều trị và dự phòng tái phát` | Nghiêm cấm cam kết vĩnh viễn không có cơ sở khoa học |
| `cam kết khỏi bệnh 100%` | `tư vấn phác đồ theo dõi điều trị cá thể hóa` | Vi phạm Luật Khám bệnh, chữa bệnh số 15/2023/QH15 |
| `thay thế hoàn toàn thuốc đặc trị` | `sản phẩm hỗ trợ nâng cao thể trạng` | Vi phạm Nghị định 15/2018/NĐ-CP (TPCN không thay thế thuốc) |
| `thổi bay bệnh tật` | `hỗ trợ làm giảm các triệu chứng khó chịu` | Ngôn từ quảng cáo thổi phồng, lừa dối người tiêu dùng |
| `uống là khỏi ngay` | `sử dụng theo chỉ định và hướng dẫn của bác sĩ` | Vi phạm quy chế thông tin thuốc và cảnh báo an toàn |
| `trị tận gốc không tái phát` | `quản lý bệnh mạn tính và dự phòng biến chứng` | Không có cơ sở lâm sàng cho các bệnh lý mạn tính |
| `thần dược phòng the` | `sản phẩm hỗ trợ sức khỏe sinh lý nam/nữ` | Cấm dùng từ 'thần dược' trong quảng cáo TPCN |
| `thuốc tiên cứu người` | `dược phẩm kê đơn theo phác đồ của Bộ Y tế` | Ngôn từ phản khoa học, truyền thông sai lệch |
| `chữa bách bệnh` | `hỗ trợ điều trị theo đúng chỉ định chuyên môn` | Cấm quảng cáo sai sự thật bản chất sản phẩm |
| `bí quyết gia truyền chữa dứt điểm ung thư` | `phác đồ điều trị ung bướu đa mô thức tại cơ sở y tế` | Hành vi lừa dối nguy hiểm đến tính mạng người bệnh |
| `xua tan nỗi lo ung thư` | `chương trình tầm soát và phát hiện sớm ung bướu` | Tránh gây ảo tưởng chủ quan cho người bệnh |
| `cam kết không đau 100%` | `áp dụng các phương pháp kiểm soát đau đa mô thức` | Không thể cam kết mức độ đau tuyệt đối cho mọi cơ địa |
| `bác sĩ bàn tay vàng số 1` | `bác sĩ chuyên khoa giàu kinh nghiệm phẫu thuật` | Danh xưng tự phong vi phạm Luật Quảng cáo Điều 8 |
| `bệnh nhân không chịu hợp tác` | `người bệnh chưa phối hợp tuân thủ điều trị` | Ngôn từ đổ lỗi cho người bệnh, thiếu tính nhân văn |
| `bệnh nan y vô phương cứu chữa` | `tiên lượng dè dặt / bệnh ở giai đoạn tiến triển` | Tránh gây tuyệt vọng, tuân thủ đạo đức giao tiếp y khoa |
| `con nghiện` | `người điều trị nghiện chất` / `người bệnh rối loạn sử dụng chất` | Ngôn từ kỳ thị, vi phạm quyền con người và Luật KCB |
| `kẻ tâm thần` | `người bệnh rối loạn tâm thần` | Xóa bỏ định kiến và kỳ thị người có vấn đề sức khỏe tâm thần |
| `bệnh nhân tâm thần quậy phá` | `người bệnh kích động do rối loạn hành vi` | Ngôn từ không đạt chuẩn y khoa lâm sàng |
| `uống thuốc tùy ý` | `dùng thuốc đúng liều lượng và thời gian theo đơn` | Vi phạm quy chế kê đơn và an toàn sử dụng thuốc |
| `uống khi cần không hạn chế` | `dùng tối đa không vượt quá liều quy định` | Nguy cơ quá liều, ngộ độc thuốc cấp tính |
| `ngày uống vài lần` | `ngày uống [số] lần, mỗi lần [số] viên` | Hướng dẫn mơ hồ vi phạm Thông tư 52/2017/TT-BYT |
| `chứng chỉ hành nghề y tế` | `giấy phép hành nghề khám bệnh, chữa bệnh` | Thuật ngữ cũ bãi bỏ từ 01/01/2024 theo Luật KCB 2023 |
| `chứng chỉ hành nghề khám chữa bệnh` | `giấy phép hành nghề khám bệnh, chữa bệnh` | Cập nhật theo Luật Khám bệnh, chữa bệnh 15/2023/QH15 |
| `bác sĩ khuyên dùng để chữa bệnh` | `tham khảo ý kiến bác sĩ chuyên khoa trước khi dùng` | Cấm dùng hình ảnh/lời khuyên bác sĩ quảng cáo TPCN |
| `thư cảm ơn của bệnh nhân` | *(bỏ hoàn toàn trong tài liệu quảng cáo TPCN/cơ sở y tế)* | Nghị định 15/2018/NĐ-CP Điều 27 khoản 2 nghiêm cấm |
| `chia sẻ của bệnh nhân đã khỏi bệnh` | *(bỏ hoàn toàn trong tài liệu quảng cáo)* | Nghiêm cấm dùng phản hồi bệnh nhân để quảng cáo TPCN |
| `dùng hình ảnh bác sĩ để quảng cáo` | *(bỏ hoàn toàn)* | Nghị định 15/2018/NĐ-CP Điều 27 khoản 2 nghiêm cấm |
| `không tác dụng phụ 100%` | `đã được kiểm nghiệm lâm sàng về tính dung nạp` | Không có sản phẩm y dược nào an toàn tuyệt đối 100% |
| `an toàn tuyệt đối cho mọi người` | `sản phẩm phù hợp với các đối tượng theo khuyến cáo` | Mọi hoạt chất đều có nguy cơ dị ứng hoặc chống chỉ định |
| `thay thế bữa ăn hoàn toàn` | `bổ sung dinh dưỡng thiết yếu bên cạnh chế độ ăn` | Tránh suy dinh dưỡng hoặc mất cân đối vi chất |
| `khỏi dứt điểm không cần bác sĩ` | `cần thăm khám bác sĩ chuyên khoa để được chẩn đoán` | Khuyến khích tự điều trị nguy hiểm |
| `cứu tinh của bệnh nhân tiểu đường` | `giải pháp hỗ trợ kiểm soát đường huyết` | Ngôn từ giật gân, phóng đại hiệu quả sản phẩm |

---

## 3. Mandatory Statutory Disclaimers in Healthcare

1. **Thực phẩm bảo vệ sức khỏe (TPCN) — Nghị định 15/2018/NĐ-CP Điều 27:**
   - Bắt buộc phải có dòng chữ:
     `"Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh."`
   - Kích thước chữ phải đủ lớn, dễ đọc, tương phản rõ rệt với màu nền; trên video/audio phải đọc rõ ràng, tốc độ vừa phải.
2. **Quảng cáo thuốc kê đơn (Prescription-only medicine):**
   - **Nghiêm cấm tuyệt đối** quảng cáo thuốc kê đơn đến công chúng trên mọi phương tiện thông tin đại chúng (truyền hình, báo chí, mạng xã hội, bảng biển ngoài trời).
   - Chỉ được phép phát hành thông tin thuốc cho cán bộ y tế thông qua hội thảo chuyên ngành, tài liệu y khoa được Bộ Y tế phê duyệt.
