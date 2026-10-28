<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-tech-writing`

> Auto-generated from `evals/vietnamese-tech-writing/pairs.jsonl` (32 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Engineering

### eng-commit-cam-ket (Rules: `CAL001`)

```diff
- Cam kết các thay đổi của bạn trước khi tạo PR.
+ Commit các thay đổi trước khi tạo PR.
```
- **Why:** `Cam kết` is a legal/moral pledge; Git revision recording stays `commit`.

### eng-deploy-production (Rules: `CAL001`)

```diff
- Triển khai đến sản xuất sau khi test xong.
+ Deploy lên production sau khi test xong.
```
- **Why:** Environment names are never translated; `sản xuất` means factory manufacturing.

### eng-pull-request (Rules: `CAL001`)

```diff
- Mở một yêu cầu kéo trên GitHub để team review.
+ Tạo một pull request trên GitHub để team review.
```
- **Why:** `Yêu cầu kéo` is a literal calque; standard engineering prose uses `pull request` or `PR`.

### eng-merge-branch (Rules: `CAL001`)

```diff
- Hợp nhất chi nhánh tính năng vào nhánh main.
+ Merge nhánh tính năng vào nhánh main.
```
- **Why:** Git command operations stay English (`merge nhánh`).

### eng-fix-bug (Rules: `CAL001`)

```diff
- Sửa con bọ trong bộ nhớ đệm thanh toán.
+ Fix bug trong bộ nhớ đệm thanh toán.
```
- **Why:** `Con bọ` is humorous/inappropriate for serious engineering docs; write `fix bug` or `sửa lỗi`.

### eng-message-queue (Rules: `CAL001`)

```diff
- Hàng đợi thông điệp đang bị quá tải request.
+ Message queue đang bị quá tải request.
```
- **Why:** `Hàng đợi thông điệp` is over-translated; Vietnamese developers use `message queue`.

### eng-something-wrong (Rules: `CAL001`)

```diff
- Cái gì đó đã đi sai. Vui lòng thử lại.
+ Đã có lỗi xảy ra. Vui lòng thử lại.
```
- **Why:** Word-for-word calque of an English idiom; settled Vietnamese is `Đã có lỗi xảy ra`.

### eng-refresh-page (Rules: `CAL001`)

```diff
- Làm tươi trang để xem các thay đổi mới.
+ Tải lại trang để xem các thay đổi mới.
```
- **Why:** `Làm tươi` refers to food/flowers; refreshing a webpage is `tải lại trang`.

### eng-branch-diacritics (Rules: `ENG001` · Doctype: `branch`)

```diff
- feat/thêm-đăng-nhập
+ feat/add-login
```
- **Why:** Branch names must be ASCII to prevent shell and filesystem collation corruptions.

### eng-commit-subject-diacritics (Rules: `ENG001` · Doctype: `commit`)

```diff
- sửa lỗi xác thực tài khoản
+ fix: resolve authentication validation error
```
- **Why:** Commit subject lines must remain ASCII for compatibility with git log formatters and CI.

### eng-rfc-direct-address (Rules: `ENG003` · Doctype: `rfc`)

```diff
- Bạn sẽ thử lại request tối đa 3 lần khi gặp lỗi kết nối.
+ Hệ thống sẽ tự động thử lại request tối đa 3 lần khi gặp lỗi kết nối.
```
- **Why:** RFCs describe system architecture objectively; eliminate `bạn` with impersonal frames.

### eng-postmortem-address (Rules: `ENG003` · Doctype: `postmortem`)

```diff
- Bạn đã deploy nhầm script khiến dịch vụ thanh toán bị gián đoạn.
+ Dịch vụ thanh toán bị gián đoạn do script migration thực thi thiếu biến môi trường.
```
- **Why:** Postmortems must name system transitions, never individuals or direct second-person address.

### eng-adr-direct-address (Rules: `ENG003` · Doctype: `adr`)

```diff
- Trong phần này, bạn sẽ tích hợp Apache Kafka làm message bus.
+ Hệ thống tích hợp Apache Kafka làm message bus trung tâm.
```
- **Why:** ADRs are impersonal records of architectural decisions; eliminate `bạn`.

### eng-runbook-hedged-nen (Rules: `ENG007` · Doctype: `runbook`)

```diff
- Bạn nên chạy migration cơ sở dữ liệu trước khi restart dịch vụ.
+ Chạy migration cơ sở dữ liệu trước khi restart dịch vụ.
```
- **Why:** Runbook instructions must use bare imperatives without hedging (`bạn nên`).

### eng-runbook-hedged-co-the (Rules: `ENG007` · Doctype: `runbook`)

```diff
- Bạn có thể xoá cache Redis nếu độ trễ tăng cao.
+ Xoá cache Redis nếu độ trễ tăng cao.
```
- **Why:** Runbooks require crisp bare imperatives without `bạn có thể`.

## I18N

### eng-identifier-ascii (Rules: `ENG001` · Doctype: `identifier`)

```diff
- "auth.đăngNhập.tiêuĐề": "Đăng nhập"
+ "auth.signIn.title": "Đăng nhập"
```
- **Why:** i18n resource keys must be ASCII; only values contain Vietnamese.

### eng-icu-plural-branches (Rules: `ICU001`)

```diff
- {"commitCount": "{count, plural, one {# commit} other {# commit}}"}
+ {"commitCount": "{count, plural, other {# commit}}"}
```
- **Why:** Vietnamese has no grammatical plural; ICU plural takes strictly `other`.

## Microcopy

### eng-error-user-blame-nhap-sai (Rules: `ENG008` · Doctype: `error-message`)

```diff
- Bạn đã nhập sai địa chỉ email.
+ Địa chỉ email không đúng định dạng. Vui lòng kiểm tra lại.
```
- **Why:** Error messages must describe the objective state without accusing the user.

### eng-error-user-blame-loi-cua-ban (Rules: `ENG008` · Doctype: `error-message`)

```diff
- Lỗi của bạn: mật khẩu quá ngắn.
+ Mật khẩu cần tối thiểu 8 ký tự.
```
- **Why:** Never blame the user; state the system input requirement objectively.

### prd-empty-state-slop (Rules: `CAL001`)

```diff
- Trạng thái trống trải
+ Chưa có dự án nào. Nhấn nút bên dưới để tạo mới.
```
- **Why:** Never display internal design terminology; tell the user what is missing and how to add it.

## Product

### prd-sprint-backlog (Rules: `CAL001`)

```diff
- Thêm các ticket vào tồn đọng chạy nước rút.
+ Thêm các ticket vào sprint backlog.
```
- **Why:** Agile ceremonies and artifacts stay English in professional product teams.

### prd-user-story-syntax (Rules: `CAL001`, `SYN001`)

```diff
- Như một người dùng, tôi muốn đặt lại mật khẩu của mình.
+ Là người dùng, tôi muốn đặt lại mật khẩu.
```
- **Why:** Standard Vietnamese user story convention is `Là [vai trò]`, not comparative `Như một`.

## Survey

### prd-agree-scale-question (Rules: `PROD002` · Doctype: `survey`)

```diff
- Bạn có đồng ý rằng nền tảng rất dễ sử dụng không?
+ Mức độ dễ dàng khi sử dụng nền tảng? (Rất khó – Rất dễ)
```
- **Why:** Agree/disagree questions bias results by 10-15%; use an item-specific construct scale.

### prd-agree-scale-endpoints (Rules: `PROD002` · Doctype: `survey`)

```diff
- Lựa chọn: Rất đồng ý / Đồng ý / Không đồng ý
+ Lựa chọn: Rất không hài lòng / Hài lòng / Rất hài lòng
```
- **Why:** Replace agree/disagree options with item-specific satisfaction or difficulty endpoints.

## App Store

### prd-app-store-title-limit (Rules: `PROD003` · Doctype: `app-store-title`)

```diff
- DESIGN:OS - Nền tảng thiết kế giao diện tự động hoá chuyên nghiệp
+ DESIGN:OS - Thiết kế giao diện
```
- **Why:** App Store titles are strictly limited to 30 NFC characters.

### prd-app-store-subtitle-limit (Rules: `PROD003` · Doctype: `app-store-subtitle`)

```diff
- Ứng dụng quản trị tài chính doanh nghiệp toàn diện và tiện lợi
+ Quản trị tài chính thông minh
```
- **Why:** App Store subtitles are capped at 30 NFC characters.

### prd-app-store-promo-limit (Rules: `PROD003` · Doctype: `app-store-promo`)

```diff
- Chào mừng bạn đến với phiên bản nâng cấp toàn diện nhất từ trước đến nay của chúng tôi. Chúng tôi đã hoàn thiện toàn bộ tính năng và bổ sung thêm rất nhiều công cụ mới giúp doanh nghiệp tối ưu hoá mọi quy trình vận hành phức tạp.
+ Khám phá phiên bản mới với hiệu năng vượt trội và giao diện trực quan hơn.
```
- **Why:** App Store promotional text is strictly limited to 170 NFC characters.

## Legal

### prd-consent-without-purpose (Rules: `PROD004` · Doctype: `consent`)

```diff
- Tôi đồng ý cho phép ứng dụng thu thập dữ liệu cá nhân của tôi.
+ Tôi đồng ý cho phép ứng dụng thu thập dữ liệu cá nhân nhằm mục đích xác thực tài khoản.
```
- **Why:** Luật 91/2025/QH15 Điều 9 and NĐ 356/2025/NĐ-CP Điều 6 mandate express, informed consent naming the specific purpose.

### eng-app-store-superlative (Rules: `LAW001` · Doctype: `app-store-subtitle`)

```diff
- Quản lý dự án tốt nhất
+ Quản lý dự án cho đội nhóm
```
- **Why:** Superlatives like `tốt nhất` require official proof documentation under Luật Quảng cáo.

## Register

### eng-readme-quy-khach (Rules: `PRO002` · Register: `eng-readme`)

```diff
- Kính thưa Quý khách, vui lòng chạy lệnh npm install để cài đặt SDK.
+ Vui lòng chạy lệnh npm install để cài đặt SDK.
```
- **Why:** `Quý khách` sounds servile and out of place in technical documentation; use `bạn` or omit pronoun.

## Unicode

### eng-unicode-nfd (Rules: `NFC001`)

```diff
- Hướng dẫn cài đặt công cụ phát triển phần mềm
+ Hướng dẫn cài đặt công cụ phát triển phần mềm
```
- **Why:** All documentation must be precomposed NFC Unicode.

## Number

### eng-num-dot-decimal (Rules: `NUM003`)

```diff
- Độ trễ hệ thống đã giảm 14.8% sau khi tối ưu cache.
+ Độ trễ hệ thống đã giảm 14,8% sau khi tối ưu cache.
```
- **Why:** Vietnamese numbers use a comma for decimal fractions (`14,8%`).
