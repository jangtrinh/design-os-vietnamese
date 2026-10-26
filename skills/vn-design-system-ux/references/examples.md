<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vn-design-system-ux`

> Auto-generated from `evals/vn-design-system-ux/pairs.jsonl` (29 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Button Caps

### ux-001 (Rules: `UX001` · Doctype: `ui-button`)

```diff
- Tiến hành đăng ký nhận bảng giá căn hộ mẫu ngay hôm nay
+ Đăng ký nhận bảng giá
```
- **Why:** Button labels must not exceed 24 characters.

## Tab Caps

### ux-002 (Rules: `UX001` · Doctype: `ui-tab`)

```diff
- Báo cáo doanh thu và tài chính
+ Doanh thu
```
- **Why:** Navigation tab labels must not exceed 18 characters.

## Badge Caps

### ux-003 (Rules: `UX001` · Doctype: `ui-badge`)

```diff
- Đang chờ thanh toán tiền
+ Chờ thanh toán
```
- **Why:** Badge labels must not exceed 16 characters.

## Toast Caps

### ux-004 (Rules: `UX001` · Doctype: `ui-toast`)

```diff
- Yêu cầu cập nhật hồ sơ thông tin doanh nghiệp của bạn đã được gửi thành công đến bộ phận hỗ trợ kỹ thuật và đang được xử lý
+ Đã gửi yêu cầu cập nhật hồ sơ. Hệ thống sẽ phản hồi trong 24 giờ.
```
- **Why:** Toast messages must not exceed 90 characters.

## Button Pronouns

### ux-005 (Rules: `UX002` · Doctype: `ui-button`)

```diff
- Bạn nhấn vào đây
+ Tiếp tục
```
- **Why:** Compact button labels should not include conversational pronouns.

## Button Padding

### ux-006 (Rules: `UX002` · Doctype: `ui-button`)

```diff
- Vui lòng lưu thay đổi
+ Lưu thay đổi
```
- **Why:** Compact buttons should omit polite filler like vui lòng.

## Tab Pronouns

### ux-007 (Rules: `UX002` · Doctype: `ui-tab`)

```diff
- Hồ sơ của tôi
+ Hồ sơ cá nhân
```
- **Why:** Tab labels should be concise nouns without possessive pronouns.

## Empty Raw Placeholder

### ux-008 (Rules: `UX003` · Doctype: `ui-empty`)

```diff
- Không có dữ liệu
+ Chưa có dự án nào. Bắt đầu bằng cách tạo dự án đầu tiên của bạn.
```
- **Why:** Empty state must not be a raw placeholder; it needs an actionable creation CTA.

## Empty State Placeholder

### ux-009 (Rules: `UX003` · Doctype: `ui-empty`)

```diff
- Trạng thái trống
+ Chưa có tài liệu nào. Tải lên tệp để bắt đầu phân tích.
```
- **Why:** Empty state should explain context and provide an upload CTA.

## Empty List Placeholder

### ux-010 (Rules: `UX003` · Doctype: `ui-empty`)

```diff
- Danh sách trống
+ Chưa có thành viên nào. Mời đồng nghiệp tham gia nhóm để bắt đầu cộng tác.
```
- **Why:** Empty list should guide user to invite team members.

## Error Dead End

### ux-011 (Rules: `UX004` · Doctype: `ui-error`)

```diff
- Đã xảy ra lỗi
+ Không thể tải dữ liệu do mất kết nối. Kiểm tra mạng và thử lại.
```
- **Why:** Error messages must state cause and provide actionable recovery step.

## Error System

### ux-012 (Rules: `UX004` · Doctype: `ui-error`)

```diff
- Lỗi hệ thống
+ Máy chủ tạm thời bận. Vui lòng tải lại trang hoặc thử lại sau ít phút.
```
- **Why:** System errors should explain status and offer reload/retry.

## Error Unsuccessful

### ux-013 (Rules: `UX004` · Doctype: `ui-error`)

```diff
- Thao tác không thành công
+ Thao tác chưa hoàn tất do gián đoạn đường truyền. Vui lòng thử lại.
```
- **Why:** Avoid generic unsuccessful alerts without recovery CTA.

## Destructive Vague Ok

### ux-014 (Rules: `UX005` · Doctype: `ui-destructive-modal`)

```diff
- Xóa tài khoản vĩnh viễn? Dữ liệu sẽ bị xóa hoàn toàn. [Hủy] [OK]
+ Xóa tài khoản vĩnh viễn? Dữ liệu sẽ bị xóa vĩnh viễn. Hành động này không thể hoàn tác. [Hủy] [Xóa vĩnh viễn]
```
- **Why:** Destructive modals must not use vague OK button.

## Destructive Vague Agree

### ux-015 (Rules: `UX005` · Doctype: `ui-destructive-modal`)

```diff
- Xóa dự án này? Dữ liệu không thể khôi phục. [Hủy] [Đồng ý]
+ Xóa dự án này? Dữ liệu sẽ bị xóa vĩnh viễn và không thể hoàn tác. [Hủy] [Xóa dự án]
```
- **Why:** Destructive modals must not use vague Đồng ý button.

## Destructive Missing Consequence

### ux-016 (Rules: `UX005` · Doctype: `ui-destructive-modal`)

```diff
- Xóa toàn bộ cơ sở dữ liệu? [Hủy] [Xóa ngay]
+ Xóa toàn bộ cơ sở dữ liệu? Toàn bộ bảng và bản ghi sẽ bị xóa vĩnh viễn. Hành động này không thể hoàn tác. [Hủy] [Xóa ngay]
```
- **Why:** Destructive modals must explicitly warn that action cannot be undone.

## Css Heading Line Height

### ux-017 (Rules: `UX006` · Doctype: `css-tokens`)

```diff
- h1 { font-size: 36px; line-height: 1.1; }
+ h1 { font-size: 36px; line-height: 1.25; }
```
- **Why:** Heading line-height below 1.18 clips stacked diacritics.

## Css Body Line Height

### ux-018 (Rules: `UX006` · Doctype: `css-tokens`)

```diff
- p { font-size: 16px; line-height: 1.25; }
+ p { font-size: 16px; line-height: 1.5; }
```
- **Why:** Body prose line-height below 1.35 clips diacritics.

## Css Token Line Height

### ux-019 (Rules: `UX006` · Doctype: `css-tokens`)

```diff
- --lh-display: 1.05;
+ --lh-display: 1.20;
```
- **Why:** Display leading tokens below 1.18 clip uppercase diacritics.

## Nextjs Font Subsets

### ux-020 (Rules: `UX007` · Doctype: `nextjs-font`)

```diff
- export const font = Inter({ subsets: ['latin'] });
+ export const font = Inter({ subsets: ['latin', 'vietnamese'] });
```
- **Why:** next/font/google must declare vietnamese subset alongside latin.

## Calque Dashboard

### ux-021 (Rules: `CAL001`)

```diff
- Xem thông tin trên bảng táp-lô của hệ thống.
+ Xem thông tin trên bảng điều khiển của hệ thống.
```
- **Why:** Do not use calque bảng táp-lô for dashboard.

## Calque Save Changes

### ux-022 (Rules: `CAL001`)

```diff
- Nhấn để tiết kiệm thay đổi vào hồ sơ.
+ Nhấn để lưu thay đổi vào hồ sơ.
```
- **Why:** Do not use calque tiết kiệm thay đổi for save changes.

## Calque Reset Password

### ux-023 (Rules: `CAL001`)

```diff
- Gửi liên kết cài lại mật khẩu qua email.
+ Gửi liên kết đặt lại mật khẩu qua email.
```
- **Why:** Use đặt lại mật khẩu instead of cài lại mật khẩu.

## Translationese Sent

### ux-024 (Rules: `CAL001`)

```diff
- Yêu cầu đã được tiến hành gửi thành công.
+ Đã gửi yêu cầu thành công.
```
- **Why:** Remove bureaucratic filler like đã được tiến hành gửi thành công.

## Syntactic Calque Story

### ux-025 (Rules: `SYN001`)

```diff
- Như một quản trị viên, tôi muốn quản lý quyền thành viên.
+ Là quản trị viên, tôi muốn quản lý quyền thành viên.
```
- **Why:** User story calque Như một ..., tôi muốn should be Là ..., tôi muốn.

## Unicode Nfc

### ux-026 (Rules: `NFC001`)

```diff
- Tài liệu dự án
+ Tài liệu dự án
```
- **Why:** Emit precomposed NFC Unicode.

## Icu Plural Branch

### ux-027 (Rules: `ICU001`)

```diff
- {count, plural, one {# dự án} other {# dự án}}
+ {count, plural, other {# dự án}}
```
- **Why:** Vietnamese uses only other plural category.

## Icu Placeholder Diacritics

### ux-028 (Rules: `ICU002`)

```diff
- Xin chào {tên}, bạn có thông báo mới.
+ Xin chào {name}, bạn có thông báo mới.
```
- **Why:** Placeholder variables must remain ASCII.

## Register Mismatch

### ux-029 (Rules: `PRO002` · Register: `ux-microcopy`)

```diff
- Chào mừng quý khách đến với ứng dụng.
+ Chào mừng bạn đến với ứng dụng.
```
- **Why:** ux-microcopy register expects bạn and forbids quý khách.
