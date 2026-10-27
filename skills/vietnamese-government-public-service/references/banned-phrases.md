<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Public Administration & Citizen Service (`design-os-vietnamese`)

In Vietnamese government portals, online public service guidelines, administrative procedure (TTHC) dossiers, and civil service communications, bureaucratic bullying, outdated identity terminology, obsolete public service levels, and abolished paper residency demands carry severe regulatory infractions under Decree 42/2022/NĐ-CP, the Law on Identification 2023, Decree 69/2024/NĐ-CP, the Law on Residence 2020, and Decree 30/2020/NĐ-CP.

---

## 1. Regulated Superlatives & Civic Claims (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11** and administrative governance rules, using unverified superlatives in public service communications and civic information portals is strictly prohibited.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:nhanh\|thuận\s+tiện\|hiện\s+đại\|chuyên\s+nghiệp\|minh\s+bạch)\s+nhất` | "fastest / most convenient / most modern / most transparent" | Inappropriate superlative in civic services |
| `duy\s+nhất` | "the only" | Specifically restricted superlative |
| `số\s*(?:một\|1)\b` | "number one / No. 1" | Regulated ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Regulated ranking symbol |
| `\bno\.?\s*1\b` | "No. 1" | Regulated ranking text |
| `hàng\s+đầu` | "leading / top" | Prohibited ranking claim without award verification |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `nhanh\s+nhất\s+thị\s+trường` | "fastest on the market" | Commercialized superlative inappropriate for public services |
| `cổng\s+dịch\s+vụ\s+công\s+số\s*1` | "number 1 public service portal" | Prohibited superlative ranking claim |
| `thủ\s+tục\s+đơn\s+giản\s+nhất` | "simplest procedure" | Subjective unverified claim |
| `giải\s+quyết\s+nhanh\s+gọn\s+nhất` | "quickest resolution" | Unverified superlative claim |

---

## 2. Prohibited Statements, Bureaucratic Scolding & Calques (`GOV001`–`GOV006`)

The following phrases are prohibited across public service guidelines, administrative notifications, citizen feedback channels, and civic software UI:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale | Severity |
|---|---|---|---|
| `công dân tự chịu hoàn toàn hậu quả nếu không biết thao tác` | `quý công dân cần hướng dẫn vui lòng liên hệ tổng đài để được hỗ trợ chu đáo` | Thái độ cửa quyền, vi phạm quy chế tiếp dân và văn hóa công sở (NĐ 30/2020) | error |
| `cấm hỏi nhiều tại quầy một cửa` | `cán bộ tiếp nhận có trách nhiệm lắng nghe, hướng dẫn đầy đủ, chu đáo` | Vi phạm quy tắc đạo đức công vụ và quy chế tiếp công dân | error |
| `cán bộ không có nghĩa vụ giải thích` | `cán bộ có trách nhiệm giải thích rõ ràng căn cứ pháp lý và hướng dẫn hoàn thiện` | Vi phạm trách nhiệm giải trình của cán bộ công chức | error |
| `dịch vụ công cộng trên đường dây` | `dịch vụ công trực tuyến` | Dịch máy thô từ online public service | error |
| `cửa hàng một điểm dừng` | `Bộ phận Một cửa / Trung tâm Phục vụ hành chính công` | Dịch máy thô từ one-stop shop | error |
| `bàn dịch vụ công dân` | `Bộ phận tiếp nhận và trả kết quả` | Dịch máy thô từ citizen service desk | error |
| `yêu cầu nộp sổ hộ khẩu giấy` | `tra cứu thông tin cư trú trên Cơ sở dữ liệu quốc gia về dân cư / VNeID` | Sổ hộ khẩu giấy đã bị bãi bỏ từ 01/01/2023 per Điều 38 Luật Cư trú 2020 | error |
| `bắt buộc xuất trình sổ hộ khẩu bản gốc` | `xuất trình Thẻ căn cước hoặc ứng dụng VNeID` | Hành vi vòi vĩnh giấy tờ đã hết giá trị per NĐ 104/2022/NĐ-CP | error |
| `nộp bản sao công chứng sổ hộ khẩu hoặc sổ tạm trú giấy` | `khai thác dữ liệu cư trú điện tử liên thông` | Bị nghiêm cấm theo Luật Cư trú 2020 và Nghị định 104/2022 | error |
| `bản sao sổ hộ khẩu công chứng` | `thông tin cư trú xác thực điện tử qua VNeID` | Sổ hộ khẩu giấy hết giá trị pháp lý | error |
| `dịch vụ công trực tuyến mức độ 3` | `dịch vụ công trực tuyến một phần` | Đã bãi bỏ 4 mức, chuyển sang 2 mức per Điều 11 Nghị định 42/2022/NĐ-CP | error |
| `dịch vụ công trực tuyến mức độ 4` | `dịch vụ công trực tuyến toàn trình` | Thay thế bằng toàn trình per Nghị định 42/2022/NĐ-CP | error |
| `dvc mức 3` | `dịch vụ công trực tuyến một phần` | Cách gọi cũ đã bãi bỏ per Nghị định 42/2022/NĐ-CP | error |
| `dvc mức 4` | `dịch vụ công trực tuyến toàn trình` | Cách gọi cũ đã bãi bỏ per Nghị định 42/2022/NĐ-CP | error |
| `chứng minh nhân dân 9 số còn hiệu lực` | `Thẻ căn cước` | Hết giá trị sử dụng từ ngày 31/12/2024 theo Điều 46 Luật Căn cước 2023 | error |
| `nộp bản sao cmnd 9 số` | `xuất trình Thẻ căn cước hoặc CCCD còn hạn sử dụng` | Không được yêu cầu nộp CMND 9 số đã hết hiệu lực | error |
| `cấp mới thẻ cccd gắn chip` | `cấp mới Thẻ căn cước` | Thuật ngữ mới chuẩn Luật Căn cước 2023 từ 01/07/2024 | error |
| `vneid mức độ 3` | `Tài khoản định danh điện tử mức độ 2` | Nghị định 69/2024/NĐ-CP chỉ quy định duy nhất Mức độ 1 và Mức độ 2 | error |
| `vneid mức độ 4` | `Tài khoản định danh điện tử mức độ 2` | Không tồn tại Mức độ 4 trong quy chuẩn định danh VNeID | error |
| `vneid hạng vàng` | `Tài khoản định danh điện tử mức độ 2` | Danh xưng sai trái, gây hiểu lầm cấp độ định danh nhà nước | error |
| `tài khoản định danh điện tử cấp 3` | `Tài khoản định danh điện tử mức độ 2` | Phân cấp không có căn cứ pháp lý per Nghị định 69/2024 | error |

---

## 3. Mandatory Administrative Clerical Standards (NĐ 30/2020/NĐ-CP)

1. **Văn hóa tiếp công dân & giải quyết TTHC:**
   - Cán bộ, công chức khi giao tiếp với người dân phải có thái độ lịch sự, tôn trọng, ngôn ngữ chuẩn mực, rõ ràng, dễ hiểu.
   - Nghiêm cấm mọi hành vi hách dịch, cửa quyền, gây khó khăn, phiền hà hoặc đùn đẩy trách nhiệm.
2. **Minh bạch hóa quy trình TTHC:**
   - Mọi thủ tục hành chính phải được công khai đầy đủ trên Cổng Dịch vụ công Quốc gia, Cổng thông tin điện tử của cơ quan và tại Bộ phận Một cửa.
   - Tài liệu hướng dẫn bắt buộc phải có đầy đủ: Trình tự thực hiện, Thành phần hồ sơ và Thời hạn giải quyết.
