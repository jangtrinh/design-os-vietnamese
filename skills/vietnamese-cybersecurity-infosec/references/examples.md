<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-cybersecurity-infosec`

> Auto-generated from `evals/vietnamese-cybersecurity-infosec/pairs.jsonl` (25 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Breach Notification

### sec-breach-01 (Rules: `SEC001` · Doctype: `breach-notification`)

```diff
- Báo cáo sự cố an ninh dữ liệu.
- Doanh nghiệp phát hiện rò rỉ dữ liệu cá nhân của khách hàng vào ngày 10/10/2026. Công ty dự kiến thông báo trong vòng 15 ngày sau khi hoàn tất kiểm tra nội bộ.
- Thông báo này được gửi tới cơ quan chức năng có liên quan.
+ Báo cáo sự cố an ninh dữ liệu cá nhân.
+ Doanh nghiệp phát hiện rò rỉ dữ liệu cá nhân vào ngày 10/10/2026 và đã gửi thông báo bằng văn bản theo Mẫu số 08 Nghị định 356/2025/NĐ-CP tới cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) trong thời hạn 72 giờ theo đúng quy định tại Điều 23 khoản 1 Luật 91/2025/QH15.
+ Đơn vị tiếp tục phối hợp chặt chẽ để khắc phục hậu quả.
```

### sec-breach-02 (Rules: `SEC001` · Doctype: `breach-notification`)

```diff
- Kế hoạch ứng phó vi phạm dữ liệu cá nhân.
- Quy trình nội bộ quy định thời hạn báo cáo sự cố vi phạm dữ liệu là 7 ngày kể từ khi phát hiện.
- Báo cáo sẽ được lưu tại hồ sơ công ty.
+ Kế hoạch ứng phó vi phạm dữ liệu cá nhân.
+ Quy trình nội bộ quy định thời hạn thông báo tới cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) là trong vòng 72 giờ kể từ khi phát hiện theo Điều 23 khoản 1 Luật 91/2025/QH15.
+ Hồ sơ sự cố được lưu trữ đầy đủ để phục vụ thanh tra.
```

### sec-breach-03 (Rules: `SEC001` · Doctype: `breach-notification`)

```diff
- Thông báo vi phạm quy định bảo vệ dữ liệu cá nhân.
- Công ty TNHH Dịch vụ Số đã phát hiện sự cố rò rỉ dữ liệu tài khoản.
- Đơn vị dự kiến gửi báo cáo sau 30 ngày sau khi phát hiện rò rỉ dữ liệu cá nhân.
+ Thông báo vi phạm quy định bảo vệ dữ liệu cá nhân.
+ Công ty TNHH Dịch vụ Số đã phát hiện sự cố rò rỉ dữ liệu tài khoản.
+ Đơn vị gửi báo cáo sự cố tới cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) trong vòng 72 giờ theo luật định.
```

### sec-breach-04 (Rules: `SEC001` · Doctype: `breach-notification`)

```diff
- Thông báo gửi cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) về sự cố dữ liệu.
- Doanh nghiệp báo cáo sau 96 giờ kể từ thời điểm phát hiện dấu hiệu xâm nhập trái phép vào cơ sở dữ liệu.
+ Thông báo gửi cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an) về sự cố dữ liệu.
+ Doanh nghiệp báo cáo trong vòng 72 giờ kể từ thời điểm phát hiện dấu hiệu xâm nhập trái phép vào cơ sở dữ liệu theo Điều 23 khoản 1 Luật 91/2025/QH15.
```

## System Security Level

### sec-level-01 (Rules: `SEC002`)

```diff
- Nền tảng điện toán đám mây của chúng tôi đã được thẩm định an toàn hệ thống thông tin cấp độ 6 bởi cơ quan quản lý chuyên ngành.
+ Nền tảng điện toán đám mây của chúng tôi đã được thẩm định an toàn hệ thống thông tin cấp độ 4 bởi cơ quan quản lý chuyên ngành theo Nghị định 85/2016/NĐ-CP.
```

### sec-level-02 (Rules: `SEC002`)

```diff
- Hệ thống thanh toán trực tuyến đạt tiêu chuẩn ATTT cấp 7 theo quy định mới nhất.
+ Hệ thống thanh toán trực tuyến đạt tiêu chuẩn an toàn hệ thống thông tin cấp độ 5 theo quy định của Nghị định 85/2016/NĐ-CP.
```

### sec-level-03 (Rules: `SEC002`)

```diff
- Trung tâm dữ liệu đạt tiêu chuẩn bảo mật cấp độ 8 Bộ TT&TT về an toàn vận hành.
+ Trung tâm dữ liệu đạt tiêu chuẩn bảo mật cấp độ 5 theo quy định của Bộ Thông tin và Truyền thông và Thông tư 12/2022/TT-BTTTT.
```

### sec-level-04 (Rules: `SEC002`)

```diff
- Báo cáo kiểm thử xác nhận ứng dụng ngân hàng đạt an toàn hệ thống thông tin cấp độ 9 theo tiêu chuẩn đánh giá.
+ Báo cáo kiểm thử xác nhận ứng dụng ngân hàng đạt an toàn hệ thống thông tin cấp độ 4 theo đúng hồ sơ phê duyệt.
```

## Infosec Calques

### sec-calque-01 (Rules: `SEC003`)

```diff
- Hệ thống tường lửa ghi nhận một cuộc tấn công câu cá quy mô lớn nhắm vào hòm thư điện tử của cán bộ nhân viên.
+ Hệ thống tường lửa ghi nhận một đợt tấn công giả mạo (phishing) quy mô lớn nhắm vào hòm thư điện tử của cán bộ nhân viên.
```

### sec-calque-02 (Rules: `SEC003`)

```diff
- Máy chủ lưu trữ tập tin kế toán đã bị lây nhiễm phần mềm đòi tiền chuộc và bị khóa toàn bộ dữ liệu.
+ Máy chủ lưu trữ tập tin kế toán đã bị lây nhiễm mã độc tống tiền (ransomware) và bị mã hóa toàn bộ dữ liệu.
```

### sec-calque-03 (Rules: `SEC003`)

```diff
- Kẻ tấn công đã sử dụng mã độc chuộc lỗi nguy hiểm để tống tiền doanh nghiệp.
+ Kẻ tấn công đã sử dụng mã độc tống tiền nguy hiểm để đe dọa doanh nghiệp.
```

### sec-calque-04 (Rules: `SEC003`)

```diff
- Chuyên gia an ninh mạng khuyến cáo nhân viên đề phòng các đòn kỹ thuật xã hội qua điện thoại.
+ Chuyên gia an ninh mạng khuyến cáo nhân viên đề phòng các hình thức tấn công phi kỹ thuật và thao túng tâm lý qua điện thoại.
```

### sec-calque-05 (Rules: `SEC003`)

```diff
- Doanh nghiệp cần rà soát lại toàn bộ bề mặt cuộc tấn công của các cổng thông tin điện tử.
+ Doanh nghiệp cần rà soát lại toàn bộ bề mặt tấn công của các cổng thông tin điện tử.
```

### sec-calque-06 (Rules: `SEC003`)

```diff
- Công ty vừa hoàn thành hợp đồng kiểm toán cây bút cho cổng thanh toán quốc tế và đã triển khai tường lửa thế hệ tiếp theo.
+ Công ty vừa hoàn thành hợp đồng kiểm thử xâm nhập (pentest) cho cổng thanh toán quốc tế và đã triển khai tường lửa thế hệ mới (NGFW).
```

## Credential Safety

### sec-cred-01 (Rules: `SEC004`)

```diff
- Cảnh báo khẩn cấp: Để bảo vệ tài khoản, vui lòng gửi lại mật khẩu hiện tại và mã OTP qua email này để xác minh quyền sở hữu.
+ Cảnh báo an toàn: Quản trị viên không bao giờ yêu cầu cung cấp thông tin bí mật; người dùng tuyệt đối không chia sẻ mật khẩu hay mã OTP cho bất kỳ ai.
```

### sec-cred-02 (Rules: `SEC004`)

```diff
- Thông báo hỗ trợ kỹ thuật: Quý khách hãy cung cấp mã PIN và số CVV cho nhân viên hỗ trợ qua tin nhắn để hoàn tất kiểm tra bảo mật.
+ Thông báo hỗ trợ kỹ thuật: Ngân hàng không bao giờ yêu cầu khách hàng cung cấp mã PIN hoặc số bảo mật CVV dưới bất kỳ hình thức nào.
```

### sec-cred-03 (Rules: `SEC004`)

```diff
- Yêu cầu bảo mật: Nhân viên quản trị vui lòng nhập mật khẩu gốc vào biểu mẫu đính kèm để mở khóa tài khoản máy chủ.
+ Yêu cầu bảo mật: Nhân viên quản trị thực hiện đặt lại mật khẩu trực tiếp trên cổng xác thực nội bộ SSO thông qua mạng riêng ảo VPN.
```

## Vulnerability Advisory

### sec-advisory-01 (Rules: `SEC005` · Doctype: `security-advisory`)

```diff
- Cảnh báo an toàn thông tin CVE-2026-1026.
- Phát hiện lỗ hổng nghiêm trọng cho phép thực thi mã từ xa trên máy chủ web.
- Lỗ hổng ảnh hưởng đến các phiên bản từ 2.0 đến 3.5.
+ Cảnh báo an toàn thông tin CVE-2026-1026.
+ Phát hiện lỗ hổng thực thi mã từ xa trên máy chủ web.
+ Mức độ nghiêm trọng: Nghiêm trọng (Điểm CVSS v3.1: 9.8).
+ Biện pháp khắc phục: Khuyến nghị cập nhật bản vá phiên bản 3.6 ngay lập tức theo hướng dẫn của nhà sản xuất.
```

### sec-advisory-02 (Rules: `SEC005` · Doctype: `security-advisory`)

```diff
- Cảnh báo an toàn thông tin: Lỗ hổng tràn bộ đệm.
- Mức độ nghiêm trọng: Cao (CVSS 8.5).
- Hiện tại hệ thống đang được theo dõi chặt chẽ.
+ Cảnh báo an toàn thông tin: Lỗ hổng tràn bộ đệm.
+ Mức độ nghiêm trọng: Cao (Điểm CVSS: 8.5).
+ Biện pháp khắc phục: Quản trị viên tiến hành áp dụng bản vá bảo mật và tạm thời giới hạn quyền truy cập từ mạng Internet.
```

### sec-advisory-03 (Rules: `SEC005` · Doctype: `security-advisory`)

```diff
- Khuyến nghị an toàn thông tin định kỳ.
- Biện pháp khắc phục: Quản trị viên cần cập nhật bản vá hệ điều hành cho toàn bộ máy trạm trong tuần này.
+ Khuyến nghị an toàn thông tin định kỳ.
+ Mức độ nghiêm trọng: Trung bình (CVSS 5.3).
+ Biện pháp khắc phục: Quản trị viên cần cập nhật bản vá hệ điều hành cho toàn bộ máy trạm trong tuần này.
```

## Pdpd Classification

### sec-sensitive-01 (Rules: `SEC006`)

```diff
- Chính sách quản trị phân loại dữ liệu sức khỏe và sinh trắc học là dữ liệu cá nhân cơ bản trong hệ thống nội bộ.
+ Chính sách quản trị xác định dữ liệu sức khỏe và sinh trắc học là dữ liệu cá nhân nhạy cảm cần được mã hóa theo Điều 4 Nghị định 356/2025/NĐ-CP.
```

### sec-sensitive-02 (Rules: `SEC006`)

```diff
- Tổ chức quy định số dư tài khoản ngân hàng thuộc nhóm dữ liệu cá nhân cơ bản không cần biện pháp bảo vệ đặc biệt.
+ Tổ chức quy định thông tin tài khoản và số dư ngân hàng là dữ liệu cá nhân nhạy cảm phải áp dụng biện pháp bảo vệ nghiêm ngặt theo luật định.
```

## Shared Advertising

### sec-shared-law-01 (Rules: `LAW001`)

```diff
- Giải pháp an ninh mạng của chúng tôi đảm bảo an toàn tuyệt đối và giúp tổ chức không thể bị hack dưới mọi hình thức.
+ Giải pháp an ninh mạng của chúng tôi cung cấp nhiều lớp phòng thủ chuyên sâu giúp giảm thiểu tối đa rủi ro xâm nhập cho tổ chức.
```

## Shared Locale

### sec-shared-date-01 (Rules: `DATE001`)

```diff
- Báo cáo rà quét lỗ hổng được lập và phê duyệt vào ngày 11/25/2026 bởi trưởng nhóm bảo mật.
+ Báo cáo rà quét lỗ hổng được lập và phê duyệt vào ngày 25/11/2026 bởi trưởng nhóm bảo mật.
```

## Shared Calque Pronoun

### sec-shared-calque-pro-01 (Rules: `CAL001`, `PRO001`)

```diff
- Hệ thống bảo mật gửi thông báo: Bạn vui lòng làm ơn nhập của bạn mật khẩu để tiếp tục. Kính chúc quý khách một ngày làm việc an toàn.
+ Hệ thống bảo mật gửi thông báo: Vui lòng nhập mật khẩu của bạn để tiếp tục. Chúc bạn một ngày làm việc hiệu quả và an toàn.
```
