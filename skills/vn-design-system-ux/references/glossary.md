<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese UI/UX & Design System Glossary

> Canonical terminology mapping for software interfaces, design tokens, design systems, and developer platforms in Vietnamese (`vi-VN`).
> Used by `validate_copy.py` to flag machine translation calques, unidiomatic literalisms, and English loanword mishandling.

---

## 1. Principles of Natural UI Vietnamese

1. **Verb-First Action Labels:** UI controls are imperative and action-driven. Prefer direct transitive verbs (`Lưu thay đổi`, `Tạo dự án`, `Xóa`) over passive nominalizations (`Tiến hành việc lưu`, `Thực hiện tạo`).
2. **Standard Developer & System Terms:** Well-established engineering loanwords (`token`, `webhook`, `API`, `cache`, `cookie`) should remain in their standard lowercase or uppercase ASCII forms instead of clumsy literal calques (`mã thông báo`, `móc nối web`).
3. **No Sino-Vietnamese Translationese Overload:** Avoid awkward Sino-Vietnamese calques imported from desktop software of the 1990s (`bảng táp-lô` for dashboard, `người giữ chỗ` for placeholder, `hộp kiểm tra` for checkbox).

---

## 2. Machine-Readable UI/UX Glossary

<!-- machine-readable: glossary -->
| English | ❌ Calque / Literal | ✅ Natural UI Vietnamese | Severity |
|---|---|---|---|
| Dashboard | bảng táp-lô | Tổng quan / Bảng điều khiển | error |
| Workspace | vùng làm việc | Không gian làm việc | warn |
| Token | mã thông báo | token / Khóa token | warn |
| Save changes | tiết kiệm thay đổi | Lưu thay đổi | error |
| Dark mode | chế độ bóng tối | Chế độ tối | error |
| Light mode | chế độ sáng đèn | Chế độ sáng | error |
| Reset password | cài lại mật khẩu | Đặt lại mật khẩu | error |
| Revoke access | hủy bỏ truy cập | Thu hồi quyền truy cập | error |
| Undo | làm lại ngược | Hoàn tác | error |
| Redo | làm lại lại | Làm lại | error |
| Log in | đi vào hệ thống | Đăng nhập | error |
| Log out | đi ra hệ thống | Đăng xuất | error |
| Sign up | ký tên lên | Đăng ký | error |
| Checkout | kiểm tra ra | Thanh toán | error |
| Submit | nộp lên | Gửi / Xác nhận | error |
| Apply | ứng tuyển vào | Áp dụng | error |
| Cancel | bãi bỏ | Hủy | error |
| Delete | bôi xóa | Xóa | error |
| Remove | di dời đi | Gỡ bỏ / Xóa | error |
| Upload | tải lên trên | Tải lên | error |
| Download | tải xuống dưới | Tải xuống | error |
| Export | xuất cảng | Xuất / Xuất tệp | error |
| Import | nhập cảng | Nhập / Nhập tệp | error |
| Default | mặc định sẵn | Mặc định | warn |
| Custom | tùy biến hóa | Tùy chỉnh | error |
| Settings | các thiết lập hóa | Cài đặt | error |
| Preferences | sở thích người dùng | Tùy chọn | error |
| Notifications | các sự thông báo | Thông báo | error |
| Billing | hóa đơn hóa | Thanh toán / Gói cước | error |
| Subscription | đăng ký theo dõi | Gói đăng ký / Gói hội viên | error |
| Upgrade | nâng cấp lên | Nâng cấp | error |
| Downgrade | hạ cấp xuống | Hạ cấp gói | error |
| Credentials | giấy ủy nhiệm | Thông tin xác thực | error |
| Two-factor authentication | xác thực hai nhân tố | Xác thực hai lớp (2FA) | warn |
| Passkey | chìa khóa vượt qua | Khóa truy cập (Passkey) | error |
| Biometrics | sinh trắc học đo đạc | Sinh trắc học | error |
| Permissions | sự cho phép | Quyền truy cập | error |
| Roles | các vai diễn | Vai trò / Phân quyền | error |
| Member | thành phần viên | Thành viên | error |
| Invite | mời mọc | Mời | error |
| Empty state | trạng thái trống rỗng | Trạng thái trống | warn |
| Placeholder | người giữ chỗ | Văn bản gợi ý / Nội dung giữ chỗ | error |
| Tooltip | mẹo công cụ | Chú giải công cụ | error |
| Breadcrumbs | mẩu bánh mì | Đường dẫn điều hướng | error |
| Dropdown | thả rơi xuống | Menu thả xuống | error |
| Toggle | bật tắt qua lại | Nút gạt | error |
| Checkbox | hộp kiểm tra | Hộp kiểm | error |
| Radio button | nút đài radio | Nút chọn một (Radio) | error |
| Carousel | vòng quay ngựa gỗ | Băng chuyền hình ảnh | error |
| Skeleton loader | bộ xương tải | Khung tải dạng xương | error |
| Spinner | con quay tải | Biểu tượng xoay tải | error |
| Badge | huy hiệu đeo | Huy hiệu / Thẻ trạng thái | error |
| Avatar | hình đại diện hóa thân | Ảnh đại diện | error |
| Drawer | ngăn kéo kéo ra | Ngăn kéo điều hướng | error |
| Modal | hộp thoại phương thức | Hộp thoại / Cửa sổ bật lên | error |
| Popover | bật lên trên | Khung bật lên (Popover) | error |
| Tag | thẻ treo | Thẻ phân loại / Nhãn | error |
| Overview | nhìn bao quát | Tổng quan | error |
| Analytics | thuật phân tích | Phân tích dữ liệu | error |
| Audit log | nhật ký kiểm toán | Nhật ký hoạt động | error |
| API key | chìa khóa API | Khóa API | error |
| Webhook | móc nối web | Webhook | warn |
