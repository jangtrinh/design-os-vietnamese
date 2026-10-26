<!-- vlc-disable: all -->

# HR, Recruitment, & Labor Compliance Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese terminology for human resources, talent acquisition, recruitment marketing, statutory labor contracts (Bộ luật Lao động 2019), payroll, social insurance, and performance evaluations.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable HR & Labor Law Terms

<!-- machine-readable: glossary -->

| EN | ❌ Wrong or stale | ✅ Correct | Severity |
|---|---|---|---|
| job description | `bản mô tả công ăn việc làm` | `bản mô tả công việc (JD)` | error |
| offer letter | `lá thư mời làm việc` | `thư mời nhận việc (Offer Letter)` | error |
| probation | `thời kỳ thử thách làm` | `thời gian thử việc` | error |
| probation salary | `tiền công thử thách` | `tiền lương thử việc` | error |
| official salary | `tiền lương chính thức thức` | `tiền lương chính thức` | error |
| gross salary | `tiền lương tổng gộp thô` | `lương Gross (trước thuế và bảo hiểm)` | error |
| net salary | `tiền lương mạng lưới sạch` | `lương Net (thực lĩnh)` | error |
| basic salary | `tiền lương nền móng` | `lương căn bản / lương cơ bản` | warn |
| severance pay | `tiền bồi thường thôi làm` | `trợ cấp thôi việc` | error |
| redundancy allowance | `tiền trợ cấp dư thừa người` | `trợ cấp mất việc làm` | error |
| unemployment insurance | `bảo hiểm không có việc làm` | `bảo hiểm thất nghiệp` | error |
| social insurance | `bảo hiểm xã hội hội` | `bảo hiểm xã hội (BHXH)` | error |
| health insurance | `bảo hiểm y tế sức khỏe` | `bảo hiểm y tế (BHYT)` | error |
| labor contract | `hợp đồng lao động việc làm` | `hợp đồng lao động (HĐLĐ)` | error |
| definite-term contract | `hợp đồng có kỳ hạn nhất định` | `hợp đồng lao động xác định thời hạn` | error |
| indefinite-term contract | `hợp đồng vô thời hạn mãi` | `hợp đồng lao động không xác định thời hạn` | error |
| notice period | `khoảng thời gian báo tin trước` | `thời hạn báo trước` | error |
| unilateral termination | `đơn phương hủy bỏ ngang` | `đơn phương chấm dứt hợp đồng lao động` | error |
| internal labor regulations | `quy tắc lao động nội bộ` | `nội quy lao động` | error |
| collective bargaining agreement | `thỏa thuận thương lượng tập thể` | `thỏa ước lao động tập thể (TƯLĐTT)` | error |
| performance appraisal | `sự đánh giá biểu hiện làm` | `đánh giá hiệu suất / đánh giá hoàn thành công việc` | warn |
| key performance indicator | `chỉ số thể hiện chính` | `chỉ số hiệu suất cốt lõi (KPI)` | warn |
| objectives and key results | `mục tiêu và kết quả then chốt chốt` | `mục tiêu và kết quả then chốt (OKR)` | warn |
| 360-degree feedback | `phản hồi vòng tròn 360 độ` | `phản hồi đa chiều 360 độ` | warn |
| employer branding | `sự xây dựng nhãn hiệu chủ` | `thương hiệu nhà tuyển dụng` | warn |
| employee value proposition | `đề xuất giá trị công nhân` | `đề xuất giá trị nhân viên (EVP)` | warn |
| talent acquisition | `sự đoạt lấy tài năng` | `thu hút nhân tài / tuyển dụng nhân tài` | warn |
| headhunter | `người săn đầu người` | `chuyên viên săn đầu người / dịch vụ tuyển dụng cấp cao` | warn |
| candidate experience | `kinh nghiệm của ứng viên` | `trải nghiệm ứng viên` | warn |
| onboarding | `quá trình lên tàu làm việc` | `quy trình hội nhập nhân viên mới (Onboarding)` | warn |
| offboarding | `quá trình xuống tàu rời đi` | `quy trình bàn giao và nghỉ việc (Offboarding)` | warn |
| background check | `kiểm tra lý lịch phía sau` | `xác minh lý lịch / thẩm tra thông tin ứng viên` | warn |
| reference check | `kiểm tra tham chiếu người quen` | `thẩm định thông tin người tham chiếu` | warn |
| resume / CV | `bản tóm tắt cuộc đời` | `sơ yếu lý lịch / hồ sơ xin việc (CV)` | error |
| cover letter | `bức thư che phủ` | `thư ứng tuyển (Cover Letter)` | error |
| job vacancy | `khoảng trống công việc` | `vị trí tuyển dụng / vị trí còn trống` | warn |
| talent pool | `hồ bơi tài năng` | `nguồn nhân tài dự phòng (Talent Pool)` | warn |
| overtime | `làm việc vượt giờ giấc` | `làm thêm giờ (OT)` | error |
| night shift | `ca làm đêm hôm` | `làm việc vào ban đêm` | warn |
| annual leave | `ngày nghỉ hàng năm năm` | `nghỉ hằng năm / phép năm` | error |
| maternity leave | `nghỉ đẻ sinh con` | `nghỉ thai sản` | error |
| paternity leave | `nghỉ làm cha chăm con` | `chế độ thai sản dành cho lao động nam` | warn |
| sick leave | `nghỉ ốm đau bệnh tật` | `nghỉ ốm đau hưởng chế độ BHXH` | warn |
| work from home | `làm việc từ căn nhà` | `làm việc từ xa (Work from Home / Remote)` | warn |
| hybrid working | `làm việc lai tạp ghép nối` | `mô hình làm việc kết hợp (Hybrid)` | warn |
| core hours | `giờ làm việc cốt lõi lõi` | `khung giờ làm việc linh hoạt / giờ làm việc cốt lõi` | warn |
| timesheet | `tờ giấy ghi thời gian` | `bảng chấm công` | error |
| payslip | `mẩu giấy báo tiền lương` | `phiếu lương / bảng kê lương chi tiết` | error |
| payroll | `danh sách cuộn trả lương` | `bảng thanh toán tiền lương` | error |
| trade union | `công đoàn thương mại` | `tổ chức công đoàn cơ sở` | warn |
| labor dispute | `tranh cãi bất đồng lao động` | `tranh chấp lao động` | error |
| labor discipline | `kỷ luật trừng phạt công nhân` | `kỷ luật lao động` | error |
| dismissal | `đuổi việc sa thải ngay` | `xử lý kỷ luật sa thải` | error |
| wage deduction | `trừ bớt tiền lương phạt` | `khấu trừ tiền lương` | error |
| shift allowance | `tiền trợ cấp ca kíp` | `phụ cấp ca làm việc` | warn |
| seniority allowance | `tiền thâm niên lâu năm` | `phụ cấp thâm niên` | warn |
| job orientation | `sự định hướng công việc làm` | `định hướng công việc cho nhân viên mới` | warn |
| exit interview | `cuộc phỏng vấn tại cửa thoát` | `phỏng vấn thôi việc (Exit Interview)` | warn |
