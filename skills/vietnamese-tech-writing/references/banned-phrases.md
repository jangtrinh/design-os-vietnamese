<!-- vlc-disable: all -->

# Banned Phrases & Superlatives in Engineering Copy (`vietnamese-tech-writing`)

Technical documentation, developer portals, release notes, and product microcopy require precise, objective, non-emotional language. This file catalogues:
1. **Engineering Translation Calques:** Literal phrases that destroy credibility with developers.
2. **Product Superlatives & Overclaims:** Marketing adjectives that should never leak into technical docs or release notes.

---

## 1. Machine-Readable Engineering Calques

<!-- machine-readable: calques -->

| ❌ Calque | ✅ Use instead | Why |
|---|---|---|
| `cam kết các thay đổi` | `commit các thay đổi` | `cam kết` means to pledge; Git operations stay English |
| `triển khai đến sản xuất` | `deploy lên production` | `sản xuất` means factory manufacturing, not an execution environment |
| `triển khai đến dàn dựng` | `deploy lên staging` | Literal calque of theatrical staging environment |
| `yêu cầu kéo` | `pull request` | Standard engineering vocabulary is PR or pull request |
| `hợp nhất chi nhánh` | `merge nhánh` | Git command calque |
| `ôn tập mã nguồn` | `review code` | `ôn tập` is studying for school examinations |
| `sửa con bọ` | `fix bug` | `con bọ` is an insect; software defects are `bug` or `lỗi` |
| `hàng đợi thông điệp` | `message queue` | Textbook calque; engineers use message queue |
| `tồn đọng chạy nước rút` | `sprint backlog` | `chạy nước rút` is an athletic 100m sprint race |
| `tồn đọng sản phẩm` | `product backlog` | Stilted literal calque of agile backlog |
| `như một người dùng` | `là người dùng` | User story syntax calque |
| `tiêu chuẩn chấp nhận được` | `tiêu chí nghiệm thu` | Agile acceptance criteria is `tiêu chí nghiệm thu` |
| `lên tàu người dùng` | `onboarding người dùng` | Literal nautical calque of user onboarding |
| `trạng thái trống trải` | `chưa có dữ liệu` | Empty state is an internal UX design concept |
| `làm tươi trang` | `tải lại trang` | Food freshness adjective used for browser refresh |
| `cái gì đó đã đi sai` | `đã có lỗi xảy ra` | Literal calque of English idiom "something went wrong" |
| `thay đổi trò chơi` | `bước tiến công nghệ đột phá` | Marketing cliché in engineering release notes |
| `nói chuyện với API` | `gọi API` | Calque of English "talk to the API" |
| `ném một ngoại lệ` | `bắn ngoại lệ` | Literal calque of "throw an exception" (use `ném ngoại lệ` or `phát sinh ngoại lệ`) |
| `giết tiến trình` | `dừng tiến trình` | Literal calque of Unix command "kill process" |
| `chúng tôi đã sửa các con bọ` | `đã khắc phục một số lỗi` | Unprofessional tone in public release notes |
| `nó là cần thiết để cấu hình` | `cần cấu hình` | English dummy-subject calque in runbooks |
| `bạn đã nhập sai` | `thông tin nhập chưa đúng` | Blaming the user in form validation microcopy |
| `lỗi của bạn` | `yêu cầu không hợp lệ` | Directly blaming the user |
| `do bạn nhập sai` | `vui lòng kiểm tra lại thông tin` | Blaming the user |

---

## 2. Superlatives in Technical Specs & Release Notes

Engineering specifications, API references, architecture decision records, and release notes must rely on quantified benchmarks rather than marketing hype.

### Prohibited Patterns in Technical Docs
1. **Unsubstantiated Performance Claims:** *"API nhanh nhất thị trường"* → write *"Độ trễ trung bình p99 dưới 15ms"*.
2. **Absolute Reliability Claims:** *"Hệ thống không bao giờ gặp lỗi"* → write *"SLA 99,95% thời gian hoạt động"*.
3. **Hyperbolic Security Claims:** *"Bảo mật an toàn nhất"* → write *"Mã hóa AES-256 và xác thực hai lớp (2FA)"*.

### Machine-Readable Superlatives Table

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:nhanh\|mạnh\|tốt\|nhẹ\|ổn\s+định\|bảo\s+mật\|thông\s+minh\|tối\s+ưu)\s+nhất` | "nhanh nhất, nhẹ nhất, tốt nhất..." | Regulated superlative modifier |
| `duy\s+nhất` | "duy nhất" | Absolute exclusivity claim |
| `số\s*(?:một\|1)\b` | "số 1, số một" | Regulated ranking claim |
| `hàng\s+đầu` | "hàng đầu" | Vague superiority claim |
| `top\s*1\b` | "top 1" | Unverified ranking claim |
| `\bno\.?\s*1\b` | "No.1" | English ranking claim |
| `không\s+thể\s+phá\s+vỡ` | "không thể phá vỡ" | Unprovable security claim |
| `vô\s+địch` | "vô địch" | Tacky superlative claim |
| `hoàn\s+hảo\s+100%` | "hoàn hảo 100%" | Unrealistic engineering claim |
| `không\s+thể\s+bị\s+tấn\s+công` | "không thể bị tấn công" | Prohibited absolute security claim |
