<!-- vlc-disable: all -->

# HR, Recruitment, & Labor Compliance QA Checklist (`design-os-vietnamese`)

This QA checklist provides a comprehensive, systematic review protocol for Job Descriptions (JD), Thư mời nhận việc (Offer Letter), Nội quy lao động (Internal Labor Regulations), and Periodic Performance Appraisals.

---

## 1. Statutory & Regulatory Gates (Bộ luật Lao động 2019)

| Gate | Check Item | Pass Criteria | Severity if Failed |
|---|---|---|---|
| **GATE-HR-01** | **Anti-Discrimination (`HR001`)** | Tuyệt đối không có tiêu chí phân biệt đối xử về giới tính, hôn nhân, thai sản, ngoại hình hoặc độ tuổi tùy tiện (BLLĐ 2019 Điều 8 khoản 1). | `ERROR` |
| **GATE-HR-02** | **Probation Ceiling & Floor (`HR002`)** | Thời gian thử việc không quá 60 ngày đối với trình độ từ cao đẳng trở lên (chỉ người quản lý doanh nghiệp mới được tối đa 180 ngày theo Điều 25). Tiền lương thử việc ít nhất bằng 85% lương chính thức (Điều 26). | `ERROR` |
| **GATE-HR-03** | **Gross vs Net Transparency (`HR003`)** | Mọi Offer Letter nêu số tiền lương phải ghi rõ ràng là Gross (trước thuế và đóng bảo hiểm) hay Net (thực lĩnh). | `WARN` |
| **GATE-HR-04** | **No Document Retention / Deposits (`HR004`)** | Tuyệt đối không yêu cầu giữ bản chính bằng đại học, căn cước công dân hoặc thu tiền đặt cọc (BLLĐ 2019 Điều 17). | `ERROR` |
| **GATE-HR-05** | **No Punitive Salary Deductions (`HR004`)** | Tuyệt đối không quy định hình thức phạt tiền hoặc trừ lương thay xử lý kỷ luật lao động (BLLĐ 2019 Điều 128). | `ERROR` |
| **GATE-HR-06** | **Elimination of Toxic Clichés (`HR005`)** | Không sử dụng khẩu hiệu 'coi công ty là nhà 24/7', 'áp lực cực cao không giới hạn giờ giấc' hoặc 'lương hấp dẫn theo năng lực'. Nêu rõ dải lương minh bạch. | `WARN` |
| **GATE-HR-07** | **SBI Feedback in Reviews (`HR006`)** | Mọi nhận xét đánh giá hiệu suất nhân sự phải dựa trên hành vi cụ thể và số liệu đo lường theo mô hình SBI. Tuyệt đối không công kích cá nhân ('thái độ kém cỏi', 'lười biếng'). | `WARN` |

---

## 2. Register & Sociolinguistic Etiquette (`hr-candidate`)

- **Chế độ xưng hô chuẩn trong tuyển dụng:**
  - Ứng viên / Người lao động: `Anh/Chị` (hoặc Third-person `Ứng viên`, `Người lao động`).
  - Doanh nghiệp tự xưng: `Công ty`, `Chúng tôi`, hoặc tên thương hiệu.
  - Cấm tuyệt đối: các đại từ suồng sã hoặc xưng hô gia đình không chuẩn mực như `mày`, `cậu`, `con`, `cả nhà` trong thư mời nhận việc hoặc thông báo tuyển dụng chính thức.
- **Tính chuyên nghiệp & Trải nghiệm ứng viên:**
  - Văn phong tôn trọng, minh bạch, tạo cảm giác an tâm về môi trường làm việc chuẩn mực pháp lý.
  - Thư từ chối phỏng vấn vẫn phải duy trì sự trang trọng và động viên thiện chí.

---

## 3. Doctype-Specific Deep Audit Protocols

### 3.1 Job Descriptions (`job-description`)
- [ ] Chức danh công việc rõ ràng, phản ánh đúng chuyên môn và cấp bậc.
- [ ] Mục tiêu vai trò (Role Purpose) giải thích rõ đóng góp của vị trí.
- [ ] Trách nhiệm mô tả theo kết quả đầu ra và chỉ số đo lường.
- [ ] Không có tiêu chí phân biệt đối xử về giới tính, độ tuổi, ngoại hình hoặc tình trạng hôn nhân.
- [ ] Công khai dải thu nhập minh bạch (Gross hoặc Net) kèm quyền lợi phúc lợi.
- [ ] Nêu rõ quy trình tuyển dụng và các mốc thời gian phản hồi.

### 3.2 Offer Letters (`offer-letter`)
- [ ] Ghi rõ họ và tên ứng viên, vị trí chức danh và ngày bắt đầu làm việc.
- [ ] Thời gian thử việc tuân thủ trần luật định (tối đa 60 ngày đối với chuyên môn cao đẳng/đại học).
- [ ] Mức lương thử việc bảo đảm tối thiểu 85% mức lương chính thức.
- [ ] Mức lương nêu rõ ràng là Gross (trước thuế/bảo hiểm) hay Net (thực lĩnh).
- [ ] Danh mục hồ sơ tiếp nhận chỉ yêu cầu bản sao chứng thực, không giữ bản chính văn bằng/CCCD.
- [ ] Có thời hạn xác nhận tiếp nhận thư mời và chữ ký của đại diện có thẩm quyền của công ty.

### 3.3 Performance Appraisals (`performance-review`)
- [ ] Đánh giá dựa trên tiêu chí đo lường rõ ràng của bản cam kết OKR/KPI từ đầu kỳ.
- [ ] Mọi nhận xét phản hồi tuân thủ mô hình SBI (Situation – Behavior – Impact).
- [ ] Không có bất kỳ từ ngữ công kích tính cách cá nhân, xúc phạm danh dự người lao động.
- [ ] Có kế hoạch hành động cụ thể để phát triển kỹ năng hoặc cải thiện hiệu suất kỳ tiếp theo.
- [ ] Có biên bản làm việc và chữ ký đồng thuận của cả nhân viên và người quản lý trực tiếp.

### 3.4 Internal Labor Regulations (`internal-policy`)
- [ ] Thời giờ làm việc tiêu chuẩn không vượt quá 48 giờ/tuần (khuyến khích 40 giờ/tuần).
- [ ] Quy định mức trả lương làm thêm giờ (OT) đúng luật (150%, 200%, 300%).
- [ ] Quy định số ngày phép năm tiêu chuẩn từ 12 ngày trở lên, tăng theo thâm niên 5 năm.
- [ ] Danh mục hành vi vi phạm kỷ luật và hình thức xử lý rõ ràng, không có hình thức phạt tiền trừ lương.
- [ ] Đã hoàn tất thủ tục đăng ký Nội quy lao động với Sở Lao động – Thương binh và Xã hội địa phương.

---

## 4. Social Insurance & Payroll Compliance Checklist

- [ ] Tiền lương đóng BHXH bắt buộc tuân thủ đúng quy định của Luật Bảo hiểm xã hội số 41/2024/QH15.
- [ ] Tỷ lệ trích đóng bảo hiểm chính xác: 21,5% phía người sử dụng lao động và 10,5% trích từ lương người lao động.
- [ ] Khấu trừ thuế thu nhập cá nhân (thuế TNCN) theo biểu lũy tiến từng phần, áp dụng đầy đủ giảm trừ gia cảnh (bản thân 11.000.000 ₫/tháng và người phụ thuộc 4.400.000 ₫/tháng).
- [ ] Phiếu lương chi tiết (Payslip) được gửi riêng tư, bảo mật cho từng nhân viên trước ngày thanh toán tiền lương.

---

## 5. Probation Evaluation & Contract Conversion Workflow

- [ ] Thông báo kết quả thử việc cho người lao động trước khi kết thúc thời gian thử việc tối thiểu 03 ngày làm việc.
- [ ] Nếu thử việc đạt yêu cầu: Ký kết hợp đồng lao động chính thức ngay khi kết thúc thời gian thử việc.
- [ ] Nếu thử việc không đạt: Nêu rõ lý do đánh giá khách quan dựa trên bản cam kết mục tiêu thử việc đã ký ban đầu.

---

## 6. Foreign Employee Compliance (Lao động người nước ngoài)

- [ ] Kiểm tra điều kiện cấp Giấy phép lao động (Work Permit) hoặc văn bản xác nhận không thuộc diện cấp giấy phép lao động trước khi người lao động nước ngoài bắt đầu làm việc tại Việt Nam.
- [ ] Thời hạn hợp đồng lao động đối với người lao động nước ngoài không được vượt quá thời hạn của Giấy phép lao động.
- [ ] Thực hiện đầy đủ nghĩa vụ đóng BHXH bắt buộc và BHYT cho lao động nước ngoài theo quy định hiện hành.
