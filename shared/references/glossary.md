<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese Universal Cross-Domain Glossary

> Canonical English-to-Vietnamese terminology and anti-calque mappings loaded by `shared/scripts/validate_copy.py`.
> Individual skills under `skills/*/references/glossary.md` extend this baseline with domain-specific vocabulary.

<!-- machine-readable: glossary -->
| English Term | ❌ Dịch máy / Calque | ✅ Thuật ngữ chuẩn (`vi-VN`) | Ghi chú ngữ cảnh | Severity |
|---|---|---|---|---|
| Please enter your password | làm ơn nhập của bạn mật khẩu | Vui lòng nhập mật khẩu của bạn / Nhập mật khẩu | Lỗi trật tự từ sở hữu cách tiếng Anh + dịch máy "Please" | error |
| your password | của bạn mật khẩu | mật khẩu của bạn | Sở hữu cách tiếng Việt đặt sau danh từ trung tâm | error |
| your account | của bạn tài khoản | tài khoản của bạn | Sở hữu cách tiếng Việt đặt sau danh từ trung tâm | error |
| your information | của bạn thông tin | thông tin của bạn | Sở hữu cách tiếng Việt đặt sau danh từ trung tâm | error |
| Please enter | làm ơn nhập | Vui lòng nhập / Nhập | Không dùng "Làm ơn" trong giao diện phần mềm | error |
| Dashboard | bảng điều khiển xe | Trang tổng quan / Bảng điều khiển | Tránh dịch nghĩa đen cơ khí | warn |
| Authentication | sự chứng thực | Xác thực | Phân biệt Authentication (Xác thực) và Authorization (Phân quyền) | error |
| Authorization | sự ủy quyền | Phân quyền / Cấp quyền | Trong ngữ cảnh IAM / RBAC | error |
| Token | đồng xu / thẻ bài | Mã xác thực / Token | Giữ nguyên Token hoặc dùng Mã xác thực | error |
| Webhook | móc web | Webhook | Giữ nguyên thuật ngữ kỹ thuật quốc tế | error |
| Deployment | sự dàn quân | Triển khai | Ngữ cảnh CI/CD và vận hành hệ thống | error |
| Repository | kho chứa hàng | Kho mã nguồn / Repo | Ngữ cảnh quản lý mã nguồn Git | error |
| Session | phiên họp | Phiên làm việc / Phiên đăng nhập | Ngữ cảnh xác thực người dùng | warn |
| Cache | bộ nhớ ẩn | Bộ nhớ đệm / Cache | Ngữ cảnh tối ưu hiệu năng | error |
| Cloud computing | tính toán đám mây | Điện toán đám mây | Thuật ngữ chuẩn CNTT Việt Nam | error |
