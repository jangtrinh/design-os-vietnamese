<!-- vlc-disable: all -->

# Technical & Product Glossary — Engineering Calques (EN → VI)

Vietnamese engineering and product prose is natively bilingual. Software engineers in Vietnam keep core tooling, cloud commands, and Git operations in English (`commit`, `deploy`, `merge`, `cache`, `pipeline`). Translating these terms literally produces laughable calques (`cam kết` for commit, `triển khai đến sản xuất` for deploy to production) that instantly signal unvetted machine translation.

**Format Contract:** The table below is parsed at runtime by `validate_copy.py`.
- Adding a row adds a linting rule across all technical documentation.
- Do not make a blocked calque a substring of any recommended alternative.

## 1. Machine-Readable Engineering Glossary

<!-- machine-readable: glossary -->

| EN | ❌ Calque | ✅ Native | Register |
|---|---|---|---|
| Commit changes | `Cam kết các thay đổi` | `Commit các thay đổi` | eng-readme |
| Deploy to production | `Triển khai đến sản xuất` | `Deploy lên production` / `Phát hành lên production` | eng-readme |
| Deploy to staging | `Triển khai đến dàn dựng` | `Deploy lên staging` | eng-readme |
| Pull request | `Yêu cầu kéo` | `Pull request` / `Tạo PR` | eng-readme |
| Merge branch | `Hợp nhất chi nhánh` | `Merge nhánh` / `Merge branch` | eng-readme |
| Code review | `Ôn tập mã nguồn` | `Review code` / `Đánh giá mã nguồn` | eng-readme |
| Rebase branch | `Tái căn cứ chi nhánh` | `Rebase nhánh` | eng-readme |
| Checkout branch | `Kiểm tra chi nhánh` | `Chuyển nhánh` / `Checkout branch` | eng-readme |
| Cherry-pick commit | `Hái quả anh đào` | `Cherry-pick commit` | eng-readme |
| Fix bug | `Sửa con bọ` | `Sửa lỗi` / `Fix bug` | eng-readme |
| Bug report | `Báo cáo con bọ` | `Báo cáo lỗi` / `Bug report` | eng-readme |
| Cache memory | `Bộ nhớ giấu giếm` | `Bộ nhớ đệm` / `Cache` | universal |
| Database | `Căn cứ dữ liệu` | `Cơ sở dữ liệu` / `Database` | universal |
| Message queue | `Hàng đợi thông điệp` | `Hàng đợi tin nhắn` / `Message queue` | universal |
| Load balancer | `Cân bằng tải trọng` | `Bộ cân bằng tải` / `Load balancer` | universal |
| Health check | `Kiểm tra sức khỏe hệ thống` | `Kiểm tra trạng thái hoạt động` / `Health check` | universal |
| Rate limit | `Giới hạn tỷ lệ` | `Giới hạn tần suất yêu cầu` / `Rate limit` | universal |
| Circuit breaker | `Cầu dao điện` | `Cơ chế ngắt mạch` / `Circuit breaker` | universal |
| Deadlock | `Khoá chết chóc` | `Khoá chết` / `Deadlock` | universal |
| Dead letter queue | `Hàng đợi thư chết` | `Hàng đợi xử lý lỗi` / `Dead-letter queue` | universal |
| Middleware | `Phần mềm ở giữa` | `Lớp trung gian` / `Middleware` | universal |
| Webhook | `Cái móc mạng` | `Điểm nhận sự kiện` / `Webhook` | universal |
| Endpoint | `Điểm kết thúc` | `Điểm cuối API` / `Endpoint` | universal |
| Payload | `Tải trọng hàng hoá` | `Dữ liệu truyền tải` / `Payload` | universal |
| Access token | `Mã thông báo truy cập` | `Khóa truy cập` / `Access token` | universal |
| Refresh token | `Mã làm tươi` | `Mã gia hạn phiên` / `Refresh token` | universal |
| Single sign-on | `Đăng nhập đơn lẻ` | `Đăng nhập một lần` / `SSO` | universal |
| Multi-factor authentication | `Xác thực nhiều nhân tố` | `Xác thực đa yếu tố` / `MFA` | universal |
| Sprint backlog | `Tồn đọng chạy nước rút` | `Danh sách công việc sprint` / `Sprint backlog` | product |
| Product backlog | `Tồn đọng sản phẩm` | `Danh mục tính năng sản phẩm` / `Product backlog` | product |
| User story | `Như một người dùng` | `Là người dùng` | product |
| Acceptance criteria | `Tiêu chuẩn chấp nhận được` | `Tiêu chí nghiệm thu` | product |
| Standup meeting | `Cuộc họp đứng dậy` | `Họp đồng bộ ngắn` / `Daily standup` | product |
| Retrospective | `Cuộc họp nhìn lại quá khứ` | `Họp rút kinh nghiệm` / `Sprint retrospective` | product |
| Feature roadmap | `Bản đồ đường tính năng` | `Lộ trình phát triển tính năng` / `Roadmap` | product |
| User onboarding | `Lên tàu người dùng` | `Hướng dẫn làm quen` / `Onboarding người dùng` | product |
| Empty state | `Trạng thái trống trải` | `Chưa có dữ liệu` | ux-microcopy |
| Refresh page | `Làm tươi trang` | `Tải lại trang` | ux-microcopy |
| Dropdown menu | `Thực đơn thả xuống` | `Menu lựa chọn` / `Danh sách chọn` | ux-microcopy |
| Breadcrumbs | `Những mẩu bánh mì` | `Thanh điều hướng phân cấp` / `Đường dẫn trang` | ux-microcopy |
| Tooltip | `Mẹo công cụ` | `Chú giải công cụ` / `Gợi ý thao tác` | ux-microcopy |
| Placeholder | `Người giữ chỗ` | `Văn bản gợi ý` / `Gợi ý nhập liệu` | ux-microcopy |
| Toggle switch | `Công tắc lật qua lật lại` | `Nút bật tắt` | ux-microcopy |
| Something went wrong | `Cái gì đó đã đi sai` | `Đã có lỗi xảy ra. Vui lòng thử lại.` | ux-microcopy |
| Invalid credentials | `Giấy ủy nhiệm không hợp lệ` | `Email hoặc mật khẩu chưa chính xác` | ux-microcopy |
| Session expired | `Phiên làm việc đã hết hạn sử dụng` | `Phiên đăng nhập đã hết hạn` | ux-microcopy |
| Bad request | `Yêu cầu tồi tệ` | `Yêu cầu không hợp lệ` | ux-microcopy |
| Internal server error | `Lỗi máy chủ nội bộ bên trong` | `Lỗi hệ thống máy chủ` | ux-microcopy |
| Deprecated API | `Giao diện lập trình bị phản đối` | `API sắp ngừng hỗ trợ` / `API không còn khuyến nghị` | universal |
| Backward compatibility | `Tương thích lùi lại` | `Tương thích ngược` | universal |
| Benchmark | `Điểm chuẩn của chiếc ghế` | `Đo kiểm hiệu năng` / `Benchmark` | universal |
| Latency | `Độ trễ nảy sinh` | `Độ trễ mạng` / `Thời gian phản hồi` | universal |
| Throughput | `Thông lượng đi qua` | `Lưu lượng xử lý` / `Throughput` | universal |
| Garbage collection | `Thu gom rác rưởi` | `Thu dọn vùng nhớ` / `Garbage collection` | universal |
| Out of memory | `Hết sạch trí nhớ` | `Tràn bộ nhớ RAM` / `Lỗi thiếu bộ nhớ` | universal |
| Thread pool | `Hồ bơi chủ đề` | `Nhóm luồng xử lý` / `Thread pool` | universal |
| Dark mode | `Chế độ tối tăm` | `Giao diện tối` / `Chế độ nền tối` | ux-microcopy |
| Cloud migration | `Di cư lên đám mây` | `Chuyển đổi dữ liệu lên đám mây` / `Cloud migration` | universal |

---

## 2. High-Severity Technical False Friends

1. **`Cam kết` vs `Commit`:**
   - English "commit" in Git means recording a revision to the repository history.
   - Vietnamese `cam kết` is a legal/moral pledge (*"cam kết bảo mật"*, *"cam kết chất lượng"*).
   - Writing *"cam kết các thay đổi"* makes an engineering document look like an amateur translation machine hallucination. Keep `commit`.

2. **`Triển khai đến sản xuất` vs `Deploy lên production`:**
   - `Sản xuất` means industrial manufacturing or factory fabrication (*"nhà máy sản xuất linh kiện"*).
   - Runtime deployment environments are never translated: use `production`, `staging`, `dev`.

3. **`Hái quả anh đào` vs `Cherry-pick`:**
   - Literal rendering of git command `cherry-pick`. Keep the command ASCII in documentation.

4. **`Như một người dùng, tôi muốn...` vs `Là người dùng, tôi muốn...`:**
   - `Như một` translates comparative "as/like".
   - Standard Agile User Story syntax in Vietnamese is strictly `Là [vai trò], tôi muốn [hành động] để [lợi ích]`.
