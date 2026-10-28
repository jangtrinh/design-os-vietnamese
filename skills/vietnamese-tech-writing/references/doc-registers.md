<!-- vlc-disable: all -->

# Engineering Documentation Registers & Voice Hierarchy (`vietnamese-tech-writing`)

Technical documents serve different audiences with conflicting communication expectations. Addressing a developer as `quý khách` in an API reference reads as absurd parody; addressing a reader as `bạn` in an Architectural Decision Record (ADR) or Postmortem compromises institutional rigor and blamelessness.

---

## 1. Document Type to Register Mapping

| Document Type | Doctype Flag | Audience | Register | Reader Address | Self-Reference |
|---|---|---|---|---|---|
| **RFC / Technical Spec** | `--doctype rfc` | Senior Engineers, Architects | `eng-impersonal` | *None* (Impersonal) | `chúng tôi` / *Omitted* |
| **Architecture Decision Record** | `--doctype adr` | Tech Leads, Future Maintainers| `eng-impersonal` | *None* (Impersonal) | *Omitted* |
| **Blameless Postmortem** | `--doctype postmortem`| Engineering Org, Execs | `eng-impersonal` | *None* (No names/pronouns)| *Omitted* |
| **Operational Runbook** | `--doctype runbook` | DevOps, On-call Engineers | `eng-impersonal` | *None* (Bare Imperative)| *Omitted* |
| **Developer README / Quickstart**| `--doctype identifier`| External Developers, SDK Users| `eng-readme` | `bạn` | `chúng tôi` / `mình` |
| **API Reference & Tutorials** | *Standard* | Developers, Integrators | `eng-readme` | `bạn` | `chúng tôi` |
| **Pull Request & Code Review** | *Standard* | Internal Engineering Peers | `saas` / *Peer* | `bạn` / `mình` | `mình` / `tôi` |
| **System Status Page** | *Standard* | End Users, Customers | `formal` / `re` | `Quý khách` | `chúng tôi` |
| **UI Error Messages** | `--doctype error-message`| Product End Users | `ux-microcopy` | *None* (Objective fact) | *Omitted* |

---

## 2. The Impersonal Construction in RFCs & ADRs (`ENG003`)

English technical docs frequently use dummy "you" (*"In this section, you will define the database schema"* or *"You must pass the bearer token"*). Translating this directly into Vietnamese imports unwanted personal pronouns (*"Trong phần này, bạn sẽ định nghĩa..."*).

Vietnamese possesses rich, natural impersonal grammatical frames that make `bạn` completely unnecessary.

### Impersonal Rewrite Blueprints

| English Translationese (❌ Calque) | Production Impersonal Vietnamese (✅ Compliant) |
|---|---|
| *Bạn cần cấu hình Redis trước khi khởi động.* | **Cần cấu hình Redis trước khi khởi động dịch vụ.** |
| *Bạn sẽ gửi request đến endpoint này.* | **Client gửi HTTP POST request đến endpoint `/v1/payments`.** |
| *Bạn có thể xem dữ liệu trong bảng users.* | **Dữ liệu được lưu trữ và truy vấn tại bảng `users`.** |
| *Nếu bạn gặp lỗi timeout, bạn nên retry.* | **Khi phát sinh lỗi timeout, hệ thống tự động retry tối đa 3 lần.** |
| *Trong tài liệu này, chúng tôi sẽ hướng dẫn bạn.* | **Tài liệu này mô tả kiến trúc phân tán của hệ thống thanh toán.** |
| *Bạn hãy truyền bearer token vào header.* | **Yêu cầu truyền Bearer token hợp lệ trong header Authorization.** |

### Worked Impersonal RFC Specification Example

```markdown
# RFC-028: Phân vùng và mã hóa dữ liệu người dùng tại tầng lưu trữ

## 1. Mục tiêu (Objective)
Đặc tả giải pháp phân vùng cơ sở dữ liệu PostgreSQL cho bảng `user_events` và triển khai
mã hóa ở trạng thái nghỉ (encryption-at-rest) nhằm đáp ứng yêu cầu của Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15.

## 2. Thiết kế chi tiết (Detailed Design)
1. Bảng `user_events` được phân vùng theo phạm vi thời gian (Range Partitioning) theo từng tháng.
2. Dữ liệu định danh cá nhân (PII) được mã hóa tại tầng ứng dụng bằng thuật toán AES-256-GCM
   trước khi ghi xuống bộ nhớ đệm hoặc cơ sở dữ liệu.
3. Khóa giải mã được quản lý tập trung thông qua dịch vụ AWS KMS / HashiCorp Vault.
4. Mọi truy vấn phân tích bắt buộc đi qua lớp View ẩn danh, không cấp quyền truy cập bảng gốc trực tiếp.

## 3. Rủi ro và kế hoạch dự phòng (Risks & Mitigations)
- **Rủi ro:** Gia tăng 5ms độ trễ khi thực hiện mã hóa trên mỗi giao dịch ghi.
- **Phương án:** Sử dụng worker pool bất đồng bộ để tách luồng xử lý mã hóa ra khỏi luồng phản hồi HTTP chính.
```

---

## 3. Architecture Decision Record (ADR) Standards

An ADR records an architectural decision alongside its rationale and trade-offs. It must remain timeless and impersonal:

```markdown
# ADR-004: Chuyển đổi kiến trúc sang Event-Driven với Apache Kafka

## Trạng thái: Đã chấp thuận (Accepted)
## Ngày quyết định: 25/10/2026
## Phạm vi ảnh hưởng: Core Banking Service, Notification Gateway

### Ngữ cảnh (Context)
Hệ thống xử lý giao dịch hiện tại giao tiếp đồng bộ qua REST API. Khi lưu lượng vượt ngưỡng
10.000 TPS trong các đợt flash sale, dịch vụ thanh toán bị nghẽn do thời gian phản hồi của
các bên thứ ba. Cần giải pháp xử lý bất đồng bộ, đảm bảo tính bền bỉ của thông điệp.

### Quyết định (Decision)
Triển khai cụm Apache Kafka làm bus truyền thông điệp trung tâm:
1. Mọi sự kiện phát sinh giao dịch (`TransactionCreated`) được đẩy vào Kafka topic có phân vùng.
2. Dịch vụ thông báo và tích điểm tiêu thụ sự kiện bất đồng bộ qua Consumer Group riêng biệt.
3. Không thực hiện gọi đồng bộ giữa các microservices ngoài luồng xác thực bắt buộc.

### Hệ quả (Consequences)
- **Tích cực:** Tách rời hoàn toàn các dịch vụ phụ trợ, tăng khả năng chịu tải lên 50.000 TPS.
- **Tiêu cực:** Tăng độ phức tạp vận hành cơ sở hạ tầng và đòi hỏi cơ chế xử lý idempotent.
```

---

## 4. Operational Runbooks & Bare Imperative Discipline (`ENG007`)

When an engineer is woken up at 3:00 AM during a Severity-1 outage, hedged instructions like *"Bạn nên chạy migration"* or *"Bạn có thể restart server nếu muốn"* sound optional, causing fatal hesitation.

Runbook steps must be **bare imperatives**:
- ❌ Defective: *"Bạn nên kiểm tra log trước rồi bạn có thể restart service."*
- ✅ Correct: *"Kiểm tra log tại `/var/log/app.log`. Thực hiện restart service bằng lệnh `systemctl restart app`."*
- ❌ Defective: *"Bạn hãy chạy migration cơ sở dữ liệu."*
- ✅ Correct: *"Chạy database migration: `npm run db:migrate`."*
- ❌ Defective: *"Bạn có thể xả cache Redis nếu thấy CPU quá tải."*
- ✅ Correct: *"Xả cache Redis: `redis-cli FLUSHDB ASYNC` nếu CPU Redis vượt quá 85%."*

---

## 5. Blameless Postmortems: Name Systems, Never People

A postmortem that contains personal pronouns (`bạn`, `anh ấy`, `kỹ sư A`) ceases to be blameless and creates a culture of fear and cover-up. Postmortems analyze systemic root causes, configuration failures, and timing race conditions.

### Blameless Postmortem Principles
1. **Zero Personal Accusations:**
   - ❌ *"Bạn Nam đã deploy nhầm script khiến database bị drop."*
   - ✅ *"Quy trình CI/CD thiếu bước kiểm tra môi trường, khiến lệnh migration chạy nhầm vào database production."*
2. **Focus on Timeline & Automated Recovery:**
   - Describe system state changes in chronological order.
3. **Action Items with Ticket Identifiers:**
   - Frame corrective actions as concrete systemic safeguards: *"Thêm bước xác thực hai lớp (2-man rule) trước khi thực thi script DDL trên production (TICKET-4029)."*

---

## 6. Customer-Facing Status Pages & Outage Notices

Unlike internal RFCs or developer READMEs, public status pages address paying customers and business users during high-stress operational incidents.

- **Register:** `formal` / `re` (Address as `Quý khách`; Self-reference: `chúng tôi`).
- **Tone:** Empathetic, transparent, reassuring, non-defensive.
- **Template:**
  > *"Kính gửi Quý khách, Hệ thống cổng thanh toán hiện đang ghi nhận tình trạng gián đoạn dịch vụ tạm thời từ 14:15. Đội ngũ kỹ sư của chúng tôi đang tích cực phối hợp cùng đối tác ngân hàng để khắc phục sự cố. Dự kiến dịch vụ sẽ được khôi phục hoàn toàn trước 15:30. Chúng tôi thành thật xin lỗi vì sự bất tiện này."*

---

## 7. UI Error Messages: Objective, Never Blaming (`ENG008`)

Error microcopy must inform the user what occurred and provide a concrete path to resolution. Never blame the user directly:
- ❌ *"Bạn đã nhập sai định dạng email."* → ✅ *"Email không đúng định dạng. Vui lòng kiểm tra lại."*
- ❌ *"Lỗi của bạn: mật khẩu quá ngắn."* → ✅ *"Mật khẩu cần tối thiểu 8 ký tự bao gồm chữ và số."*
- ❌ *"Do bạn thao tác sai nên giao dịch thất bại."* → ✅ *"Giao dịch chưa hoàn tất. Vui lòng thử lại sau vài phút."*
