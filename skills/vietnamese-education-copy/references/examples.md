<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-education-copy`

> Auto-generated from `evals/vietnamese-education-copy/pairs.jsonl` (46 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## K12

### edu-legacy-overall-01 (Rules: `EDU001` · Doctype: `secondary-report-card`)

```diff
- Học kỳ này em đạt xếp loại Giỏi trong học bạ.
+ Học kỳ này em đạt kết quả học tập mức Tốt trong học bạ.
```

### edu-legacy-overall-02 (Rules: `EDU001` · Doctype: `secondary-report-card`)

```diff
- Kết quả học tập cuối năm của học sinh xếp loại trung bình.
+ Kết quả học tập cuối năm của học sinh đạt mức Đạt.
```

### edu-legacy-title-01 (Rules: `EDU001` · Doctype: `secondary-report-card`)

```diff
- Khen tặng em vì đã đạt danh hiệu học sinh tiên tiến học kỳ I.
+ Khen tặng em vì đã đạt danh hiệu Học sinh Giỏi học kỳ I.
```

### edu-legacy-title-02 (Rules: `EDU001` · Doctype: `secondary-report-card`)

```diff
- Học sinh đạt danh hiệu học sinh tiên tiến của khối lớp 8.
+ Học sinh đạt danh hiệu học sinh giỏi của khối lớp 8.
```

## Pedagogy

### edu-address-ban-01 (Rules: `EDU002` · Doctype: `teacher-to-student`)

```diff
- Bạn hãy nộp lại bài tập làm văn trước giờ học ngày mai.
+ Em hãy nộp lại bài tập làm văn trước giờ học ngày mai nhé.
```

### edu-address-ban-02 (Rules: `EDU002` · Doctype: `teacher-to-student`)

```diff
- Thầy yêu cầu bạn phải giữ trật tự và chú ý nghe giảng.
+ Thầy yêu cầu em phải giữ trật tự và chú ý nghe giảng trong lớp.
```

## Primary

### edu-primary-calque-01 (Rules: `EDU003` · Doctype: `primary-report-card`)

```diff
- Môn Tiếng Việt: Con cần cải thiện thêm kỹ năng viết chính tả.
+ Môn Tiếng Việt: Con cần cố gắng thêm ở phần viết chính tả.
```

### edu-primary-calque-02 (Rules: `EDU003` · Doctype: `primary-report-card`)

```diff
- Năng lực giải quyết vấn đề toán học của con cần cải thiện.
+ Năng lực giải quyết vấn đề toán học của con cần cố gắng hơn.
```

## Higher Ed

### edu-credit-calque-01 (Rules: `EDU005` · Doctype: `higher-ed`)

```diff
- Sinh viên phải hoàn thành tối thiểu 130 tín dụng để đủ điều kiện xét tốt nghiệp.
+ Sinh viên phải hoàn thành tối thiểu 130 tín chỉ để đủ điều kiện xét tốt nghiệp.
```

### edu-credit-calque-02 (Rules: `EDU005` · Doctype: `transcript`)

```diff
- Tổng số tín dụng tích lũy của sinh viên trong chương trình đào tạo là 120.
+ Tổng số tín chỉ tích lũy của sinh viên trong chương trình đào tạo là 120.
```

### edu-gpa-dot-01 (Rules: `EDU006` · Doctype: `transcript`)

```diff
- Điểm trung bình chung tích lũy toàn khóa học: 3.65/4.0.
+ Điểm trung bình chung tích lũy toàn khóa học: 3,65/4,0.
```

### edu-gpa-dot-02 (Rules: `EDU006` · Doctype: `transcript`)

```diff
- Kết quả tốt nghiệp đạt điểm GPA 3.8/4.0 xếp loại Xuất sắc.
+ Kết quả tốt nghiệp đạt điểm GPA 3,8/4,0 xếp loại Xuất sắc.
```

## Edtech

### edu-empty-state-01 (Rules: `EDU007` · Doctype: `edtech-microcopy`)

```diff
- Danh sách bài tập: Trạng thái trống.
+ Chưa có bài tập nào cần nộp hôm nay. Em hãy dành thời gian ôn lại bài cũ nhé!
```

### edu-empty-state-02 (Rules: `EDU007` · Doctype: `edtech-microcopy`)

```diff
- Bảng tổng quan học tập: Không có dữ liệu.
+ Chưa có nội dung hiển thị tuần này. Hãy bắt đầu bài học đầu tiên ngay bây giờ!
```

## Pronunciation

### edu-pronounce-harsh-01 (Rules: `EDU009` · Doctype: `pronunciation-feedback`)

```diff
- Sai rồi! Em đã phát âm sai thanh hỏi ở từ này.
+ Em phát âm phụ âm đầu rất tốt. Ở thanh hỏi, em hãy hạ thấp giọng một chút rồi nâng cao lên nhé!
```

### edu-pronounce-harsh-02 (Rules: `EDU009` · Doctype: `pronunciation-feedback`)

```diff
- Điểm của bạn là 35. Bạn đã phát âm sai phụ âm đầu.
+ Em đã cố gắng rất nhiều! Em chú ý bật hơi rõ hơn ở phụ âm đầu để phát âm chuẩn xác nhé.
```

## Privacy

### edu-child-consent-01 (Rules: `EDU010` · Doctype: `child-consent`)

```diff
- Ứng dụng bắt đầu thu thập dữ liệu của trẻ em để phân tích hành vi học tập.
+ Hệ thống thu thập dữ liệu học tập của học sinh dưới sự xác nhận đồng ý của phụ huynh hoặc người giám hộ.
```

### edu-child-consent-02 (Rules: `EDU010` · Doctype: `child-consent`)

```diff
- Đăng ký tài khoản cho trẻ em dưới 16 tuổi tham gia khóa học trực tuyến.
+ Đăng ký tài khoản học tập cho học sinh có sự xác nhận đồng ý từ cha mẹ hoặc người giám hộ hợp pháp.
```

## Terminology

### edu-calque-homeroom (Rules: `CAL001`)

```diff
- Giáo viên phòng nhà đã gửi bảng đánh giá tuần cho gia đình.
+ Giáo viên chủ nhiệm đã gửi bảng đánh giá tuần cho gia đình.
```

### edu-calque-report-card (Rules: `CAL001`)

```diff
- Phụ huynh vui lòng kiểm tra thẻ báo cáo cuối kỳ của học sinh.
+ Phụ huynh vui lòng kiểm tra học bạ cuối kỳ của học sinh.
```

### edu-calque-syllabus (Rules: `CAL001`)

```diff
- Khoa vừa ban hành giáo trình học phần cho các lớp khóa mới.
+ Khoa vừa ban hành đề cương chi tiết học phần cho các lớp khóa mới.
```

### edu-calque-diploma-reissuance (Rules: `CAL001`)

```diff
- Thủ tục nộp hồ sơ cấp lại bằng tốt nghiệp gốc tại phòng đào tạo.
+ Thủ tục nộp hồ sơ cấp bản sao văn bằng từ sổ gốc tại phòng đào tạo.
```

### edu-calque-leaderboard (Rules: `CAL001`)

```diff
- Em hãy cố gắng làm bài tập để thăng hạng trên bảng lãnh đạo tuần này.
+ Em hãy cố gắng làm bài tập để thăng hạng trên bảng xếp hạng tuần này.
```

### edu-calque-learning-streak (Rules: `CAL001`)

```diff
- Chúc mừng em đã duy trì vệt học tập liên tục suốt 7 ngày qua.
+ Chúc mừng em đã duy trì chuỗi ngày học tập liên tục suốt 7 ngày qua.
```

## Compliance

### edu-superlative-best (Rules: `LAW001`)

```diff
- Hệ thống trường liên cấp song ngữ chất lượng tốt nhất Việt Nam.
+ Hệ thống trường liên cấp song ngữ đạt chuẩn kiểm định chất lượng quốc tế.
```

### edu-superlative-number-one (Rules: `LAW001`)

```diff
- Trung tâm luyện thi đại học số 1 với tỷ lệ đỗ thủ khoa cao.
+ Trung tâm luyện thi đại học với hơn mười năm kinh nghiệm giảng dạy.
```

## Formatting

### edu-number-dot-decimal (Rules: `NUM003`)

```diff
- Điểm kiểm tra định kỳ của học sinh đạt 8.5 điểm môn Toán.
+ Điểm kiểm tra định kỳ của học sinh đạt 8,5 điểm môn Toán.
```

## Pragmatics

### edu-register-mixed (Rules: `PRO001`)

```diff
- Kính gửi Quý phụ huynh, bạn hãy nhắc nhở con chuẩn bị bài kỹ trước khi đến lớp.
+ Kính gửi Quý phụ huynh, xin quý phụ huynh vui lòng nhắc nhở con chuẩn bị bài kỹ trước khi đến lớp.
```

### edu-register-pronoun (Rules: `PRO002` · Register: `edu-k12`)

```diff
- Bạn hãy chú ý ghi chép bài đầy đủ vào vở học tập.
+ Em hãy chú ý ghi chép bài đầy đủ vào vở học tập.
```

## Encoding

### edu-nfc-decomposed (Rules: `NFC001`)

```diff
- Kết quả học tập và rèn luyện của học sinh trong năm học.
+ Kết quả học tập và rèn luyện của học sinh trong năm học.
```

## Academic Rank

### edu-rank-degree-ts (Rules: `EDU004` · Register: `edu-uni` · Doctype: `higher-ed`)

```diff
- Thầy hướng dẫn có học hàm Tiến sĩ chuyên ngành Khoa học Máy tính.
+ Thầy hướng dẫn có học vị Tiến sĩ chuyên ngành Khoa học Máy tính.
```

### edu-rank-degree-gs (Rules: `EDU004` · Register: `edu-uni` · Doctype: `higher-ed`)

```diff
- Hội đồng vừa trao học vị Giáo sư danh dự cho giảng viên cao cấp.
+ Hội đồng vừa trao chức danh Giáo sư danh dự cho giảng viên cao cấp.
```

### edu-rank-degree-ths (Rules: `EDU004` · Register: `edu-uni` · Doctype: `higher-ed`)

```diff
- Yêu cầu ứng viên dự tuyển có học hàm Thạc sĩ trở lên.
+ Yêu cầu ứng viên dự tuyển có học vị Thạc sĩ trở lên.
```

### edu-rank-degree-pgs (Rules: `EDU004` · Register: `edu-uni` · Doctype: `higher-ed`)

```diff
- Nhà trường tổ chức lễ công nhận học vị Phó Giáo sư cho các nhà khoa học trẻ.
+ Nhà trường tổ chức lễ công nhận chức danh Phó Giáo sư cho các nhà khoa học trẻ.
```

## Graduation Work

### edu-grad-work-bachelor (Rules: `EDU008` · Register: `edu-uni` · Doctype: `higher-ed`)

```diff
- Sinh viên năm cuối chuẩn bị bảo vệ luận án cử nhân trước hội đồng khoa.
+ Sinh viên năm cuối chuẩn bị bảo vệ khóa luận tốt nghiệp trước hội đồng khoa.
```

### edu-grad-work-master (Rules: `EDU008` · Register: `edu-postgrad` · Doctype: `master-thesis`)

```diff
- Học viên cao học đã hoàn thành bản thảo luận án thạc sĩ chuyên ngành Quản lý kinh tế.
+ Học viên cao học đã hoàn thành bản thảo luận văn thạc sĩ chuyên ngành Quản lý kinh tế.
```

### edu-grad-work-phd-khoa-luan (Rules: `EDU008` · Register: `edu-postgrad` · Doctype: `doctoral-dissertation`)

```diff
- Nghiên cứu sinh nộp hồ sơ bảo vệ khóa luận tiến sĩ cấp đơn vị chuyên môn.
+ Nghiên cứu sinh nộp hồ sơ bảo vệ luận án tiến sĩ cấp đơn vị chuyên môn.
```

### edu-grad-work-phd-do-an (Rules: `EDU008` · Register: `edu-postgrad` · Doctype: `doctoral-dissertation`)

```diff
- Khoa thông báo lịch nghiệm thu đồ án tiến sĩ của các nghiên cứu sinh.
+ Khoa thông báo lịch nghiệm thu luận án tiến sĩ của các nghiên cứu sinh.
```

## Preschool

### edu-preschool-numeric-score (Rules: `EDU011` · Register: `edu-preschool` · Doctype: `preschool-report`)

```diff
- Bé rất tích cực phát biểu và đạt điểm 10 môn Nhận thức trong tuần qua.
+ Bé rất tích cực phát biểu và đạt chuẩn mốc phát triển nhận thức trong tuần qua.
```

### edu-preschool-overall-gioi (Rules: `EDU011` · Register: `edu-preschool` · Doctype: `preschool-report`)

```diff
- Cuối học kỳ I, bé được giáo viên chủ nhiệm xếp loại học lực Giỏi.
+ Cuối học kỳ I, bé được giáo viên chủ nhiệm đánh giá Đạt tất cả các chỉ số phát triển theo độ tuổi.
```

### edu-preschool-letter-grade (Rules: `EDU011` · Register: `edu-preschool` · Doctype: `preschool-report`)

```diff
- Bé chăm ngoan và được nhà trường xếp loại A trong học kỳ vừa qua.
+ Bé chăm ngoan và hoàn thành tốt các hoạt động sinh hoạt và học tập trong học kỳ vừa qua.
```

### edu-preschool-ten-point-scale (Rules: `EDU011` · Register: `edu-preschool` · Doctype: `preschool-report`)

```diff
- Khả năng phát âm tiếng Việt của bé đạt 9/10 điểm theo bài kiểm tra định kỳ.
+ Khả năng phát âm tiếng Việt của bé đạt chuẩn chỉ số phát triển ngôn ngữ theo độ tuổi.
```

## Postgrad

### edu-postgrad-pronoun-minh-se (Rules: `EDU012` · Register: `edu-postgrad` · Doctype: `doctoral-dissertation`)

```diff
- Trong chương 3, mình sẽ trình bày thuật toán phân cụm dữ liệu phân tán.
+ Trong chương 3, nghiên cứu sinh trình bày thuật toán phân cụm dữ liệu phân tán.
```

### edu-postgrad-pronoun-teacher-student (Rules: `EDU012` · Register: `edu-postgrad` · Doctype: `master-thesis`)

```diff
- Cán bộ hướng dẫn ghi nhận tiến độ và cô khen con đã nộp đề cương đúng hạn.
+ Cán bộ hướng dẫn ghi nhận tiến độ và đánh giá cao học viên đã nộp đề cương đúng hạn.
```

### edu-postgrad-claim-inflation (Rules: `EDU012` · Register: `edu-postgrad` · Doctype: `doctoral-dissertation`)

```diff
- Mô hình đề xuất chứng minh tuyệt đối 100% không có sai số trong quá trình nhận dạng.
+ Mô hình đề xuất đạt độ chính xác 98,5% trên tập dữ liệu kiểm thử với khoảng tin cậy 95,0%.
```

### edu-postgrad-casual-ban-hay (Rules: `EDU012` · Register: `edu-postgrad` · Doctype: `master-thesis`)

```diff
- Để đánh giá hiệu quả giải pháp, bạn hãy đối chiếu biểu đồ tăng trưởng doanh thu.
+ Để đánh giá hiệu quả giải pháp, tác giả đối chiếu biểu đồ tăng trưởng doanh thu.
```
