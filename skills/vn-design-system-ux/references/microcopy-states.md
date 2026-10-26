<!-- vlc-disable: all -->

# DESIGN:OS Vietnamese Microcopy & Interface States (`microcopy-states.md`)

> Production playbook for designing, writing, and structuring Vietnamese user interface microcopy across all operational states.
> Covers empty states, skeletons, optimistic UI, partial failures, destructive modals, permission primers, biometrics/passkeys, and AI streaming.

---

## 1. State-First Interface Design Philosophy

In modern software systems, an interface is rarely static. Interfaces cycle through dynamic states: empty, pending, optimistic, partially degraded, failed, or awaiting destructive confirmation.
Vietnamese microcopy requires careful engineering across these states because:
1. **Syllabic Expansion (+25% to +35%):** Explanatory text that fits on two lines in English often breaks into three lines in Vietnamese, shifting modal layouts and pushing primary CTAs below the fold.
2. **Context-Rich Recovery:** Vietnamese users respond poorly to generic machine-translated error prompts ("Đã xảy ra lỗi"). Error and empty states must communicate *why* the state occurred and provide an *immediate, observable next step*.
3. **Tone Consistency (Register Contract):** Maintain the `ux-microcopy` register (`bạn` / implicit subject) throughout every transient state without reverting to robotic translationese (`xin quý khách vui lòng`).

---

## 2. Empty States: The 3 Operational Archetypes (`UX003`)

Never present a dead-end placeholder like `Không có dữ liệu` or `Trạng thái trống`. An empty state must always guide the user forward.

### Archetype A: First-Use / Onboarding (Zero Data Created)
- **Mental Model:** The user is new or hasn't activated this module yet.
- **Pattern:** Clear Benefit Headline + Context Explanation (1–2 sentences) + Primary Creation CTA.
- **Example:**
  - ❌ *Bad:* `Trạng thái trống. Chưa có dự án nào trong hệ thống.`
  - ✅ *Good:*
    - **Tiêu đề:** `Tạo dự án đầu tiên của bạn`
    - **Nội dung:** `Tổ chức công việc, theo dõi tiến độ và cộng tác cùng nhóm trên một không gian tập trung.`
    - **CTA:** `+ Tạo dự án mới` (Button <= 24 chars)

### Archetype B: Zero-Results (Filter / Search Miss)
- **Mental Model:** The user applied search queries or filters that returned 0 matches.
- **Pattern:** Acknowledge Query + Suggest Scope Broadening + Clear Filter Action.
- **Example:**
  - ❌ *Bad:* `Không có kết quả. Vui lòng thử lại.`
  - ✅ *Good:*
    - **Tiêu đề:** `Không tìm thấy kết quả phù hợp`
    - **Nội dung:** `Không có giao dịch nào khớp với bộ lọc "Tháng này". Hãy kiểm tra lại chính tả hoặc đặt lại bộ lọc.`
    - **CTA:** `Đặt lại bộ lọc` / `Xóa từ khóa tìm kiếm`

### Archetype C: Cleared Queue (Productive Zero / All Caught Up)
- **Mental Model:** Inbox zero, all review items processed, or all invoices paid.
- **Pattern:** Positive Reinforcement + Timestamp / Status Confirmation.
- **Example:**
  - ❌ *Bad:* `Không có nhiệm vụ nào cần làm.`
  - ✅ *Good:*
    - **Tiêu đề:** `Bạn đã xử lý hết công việc!`
    - **Nội dung:** `Không còn yêu cầu nào đang chờ duyệt. Hệ thống sẽ thông báo khi có nhiệm vụ mới.`
    - **Hành động phụ:** `Xem lịch sử duyệt`

---

## 3. Loading, Skeleton, & Progressive Hydration States

1. **Skeleton Loaders:**
   - Mirror actual Vietnamese content density: skeletons for cards and list items must account for the taller vertical bounding box (`line-height >= 1.25` on headings, `>= 1.50` on body) of Vietnamese stacked diacritics.
   - Do not display text labels inside shimmering skeleton blocks.
2. **Deterministic Spinners:**
   - Single-step quick loading (`< 2s`): Use animated spinner icon without verbose text.
   - Multi-step loading (`> 2s`): Use present-continuous progressive text (`Đang xuất báo cáo...`, `Đang đồng bộ hóa dữ liệu...`). Never use passive translationese (`Dữ liệu đang được tiến hành xử lý xin vui lòng chờ`).
3. **Progress Bar Microcopy:**
   - Include progress percentage and remaining metric: `Đang tải lên 14/20 tệp (70%)`.

---

## 4. Optimistic UI & Undo Toast Notifications (`UX001`)

Optimistic updates immediately reflect user action in the UI before server confirmation, pairing with a transient Toast notification with an actionable `Hoàn tác` (Undo) trigger.

### Microcopy Pattern:
`[Hành động đã hoàn tất]. [Hành động khôi phục ngắn]`

| Action Type | ❌ Bad / Calque Microcopy | ✅ Natural Vietnamese Toast (<= 90 chars) |
|---|---|---|
| **Archive Project** | `Dự án đã được lưu trữ thành công vào hệ thống.` | `Đã lưu trữ dự án. Hoàn tác` |
| **Delete File** | `Tệp của bạn đã được xóa bỏ hoàn toàn.` | `Đã xóa 3 tệp. Hoàn tác (5s)` |
| **Send Message** | `Tin nhắn của bạn đã được tiến hành gửi đi.` | `Đã gửi tin nhắn.` |
| **Copy Link** | `Đã sao chép liên kết vào bộ nhớ tạm thành công.` | `Đã sao chép liên kết vào khay nhớ tạm.` |

- **Toast Duration:** 4,000ms – 6,000ms for actions with `Hoàn tác`.
- **Character Cap:** Max 90 characters NFC. Never wrap to more than 2 lines on mobile screens (375px width).

---

## 5. Partial Failure & Network Retry States (`UX004`)

When network requests fail or batch operations partially succeed, dead-end alerts (`Đã xảy ra lỗi hệ thống`) cause user abandonment. Every error state must state the cause, impact, and recovery path.

### Structure of Actionable Error Messages:
1. **What happened:** Clear, non-technical explanation (`Không thể tải danh sách giao dịch`).
2. **Why it happened (if known):** (`Kết nối mạng bị gián đoạn` / `Phiên đăng nhập đã hết hạn`).
3. **Recovery CTA:** Specific actionable verb button (`Thử lại`, `Đăng nhập lại`, `Kiểm tra kết nối`).

```text
❌ Dead-End Error (UX004):
Đã xảy ra lỗi. Thao tác không thành công. Vui lòng liên hệ quản trị viên.

✅ Actionable Recovery State:
Không thể kết nối với máy chủ thanh toán do kết nối mạng không ổn định.
Các giao dịch trước đó vẫn được bảo toàn.
[Kiểm tra kết nối và thử lại]  [Về trang tổng quan]
```

---

## 6. Destructive Confirmation Modals (`UX005`)

Destructive actions (deleting databases, revoking access, cancelling active plans) require high friction, explicit consequences, and unequivocal button labels.

### The 3 Mandatory Elements of Destructive Modals:
1. **Title:** Specific action naming the entity (`Xóa dự án "Alpha"` instead of `Xóa`).
2. **Consequence Statement:** Explicit mention of permanence and irreversibility (`Hành động này không thể hoàn tác`, `Dữ liệu sẽ bị xóa vĩnh viễn`).
3. **Action Button:** Exact verb phrase matching the destruction (`Xóa vĩnh viễn`, `Hủy tài khoản`) instead of vague `OK`, `Đồng ý`, `Có`, `Xác nhận`.

```text
❌ Dangerous Modal (UX005):
Tiêu đề: Cảnh báo
Nội dung: Bạn có chắc chắn muốn xóa không?
Nút: [Hủy] [Đồng ý]

✅ High-Safety Destructive Modal:
Tiêu đề: Xóa vĩnh viễn dự án "Alpha"?
Nội dung: Toàn bộ mã nguồn, tài liệu và lịch sử hoạt động liên quan sẽ bị xóa vĩnh viễn. Hành động này không thể hoàn tác.
Nút phụ: [Hủy bỏ]
Nút chính nguy hiểm: [Xóa dự án vĩnh viễn]
```

---

## 7. System Permission Primers (Pre-Permission UX)

Never trigger the native OS permission prompt (Camera, Microphone, Location, Push Notifications) raw without an educational primer card explaining the exact product value.

| Permission | Context / Value Proposition | Primary CTA | Secondary CTA |
|---|---|---|---|
| **Camera** | `Quét mã QR và xác thực danh tính nhanh chóng qua camera thiết bị.` | `Bật quyền camera` | `Để sau` |
| **Push Notifications** | `Nhận thông báo tức thì khi có biến động số dư hoặc tin nhắn công việc quan trọng.` | `Bật thông báo` | `Không phải lúc này` |
| **Location** | `Tự động tìm kiếm chi nhánh và đối tác giao hàng gần vị trí của bạn nhất.` | `Chia sẻ vị trí` | `Nhập địa chỉ thủ công` |
| **Microphone** | `Ghi âm ghi chú cuộc họp và chuyển thành văn bản bằng giọng nói.` | `Cho phép dùng mic` | `Hủy` |

---

## 8. Biometric & Passkey Authentication Microcopy

Standardize Vietnamese terminology for device-native authentication mechanisms:
- **`Face ID` / `Touch ID` / `Windows Hello`:** Keep official brand names intact as proper nouns.
- **Passkey:** Translate as `Khóa truy cập (Passkey)` or `Khóa truy cập`.
- **Two-Factor Authentication:** `Xác thực hai lớp (2FA)`.

### Authentication Prompt Strings:
- **Biometric Request Prompt:** `Xác thực bằng Face ID để xác nhận giao dịch` / `Quét vân tay Touch ID để mở khóa ví`.
- **Passkey Creation Prompt:** `Tạo Khóa truy cập cho thiết bị này để đăng nhập an toàn mà không cần mật khẩu.`
- **Fallback Trigger:** `Sử dụng mật khẩu thiết bị` / `Đăng nhập bằng mã PIN`.

---

## 9. AI Streaming & Generative UI Microcopy

For LLM streaming responses, generative widgets, and agentic workflows:
1. **Streaming Placeholder / Thinking State:**
   - `Đang phân tích yêu cầu...`
   - `Đang tra cứu dữ liệu...`
   - `Đang tạo phản hồi...`
   - *Never display mechanical logs as microcopy unless explicitly in developer debug mode.*
2. **Interrupt / Stop Generation:**
   - Label: `Dừng tạo` (Button <= 12 chars).
3. **Regenerate / Variant Generation:**
   - Label: `Tạo lại` / `Tạo phương án khác`.
4. **Citation / Source Transparency:**
   - Label: `Nguồn trích dẫn` / `Căn cứ dữ liệu`.
5. **Hallucination / Disclaimer Microcopy:**
   - Microcopy: `Trí tuệ nhân tạo có thể tạo thông tin chưa chính xác. Vui lòng kiểm tra lại các dữ kiện quan trọng.` (Keep <= 110 chars).
