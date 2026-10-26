# DESIGN:OS Vietnamese — Skill Routing & Trigger Queries Benchmark (120 Queries)

This benchmark tests skill discovery, trigger accuracy, and boundary disambiguation across all 6 skills in **DESIGN:OS Vietnamese**. Each skill has 15 positive trigger queries (Vietnamese, English, and code-switched VI/EN) and 5 negative/boundary disambiguation queries (120 queries total).

---

## 1. `vn-design-system-ux` (Product UI, UX Writing, Microcopy, i18n, Typography Tokens)

### Positive Trigger Queries (Should Route to `vn-design-system-ux`)
1. "Viết lại hệ thống microcopy cho màn hình thanh toán, empty state và toast báo lỗi trên app SaaS."
2. "Kiểm tra file `vi.json` và `en.json` xem có bị lỗi ICU plural `one`/`other` hay lệch biến `{count}` không."
3. "Nút CTA trong modal xóa tài khoản nên viết là 'Xóa' hay 'Xóa tài khoản vĩnh viễn' để đúng chuẩn UX writing tiếng Việt?"
4. "Tại sao chữ `Ễ`, `Ẫ`, `Ộ` trên tiêu đề hero bị cắt mất dấu mũ và dấu nặng khi dùng `leading-tight` của Tailwind?"
5. "Thiết kế bộ design token font-size và line-height cho tiếng Việt với font Be Vietnam Pro."
6. "Review giúp mình các thông báo lỗi form đăng nhập (sai mật khẩu, tài khoản bị khóa, hết hạn OTP) sao cho tự nhiên, không bị dịch máy."
7. "Làm sao xử lý lỗi gõ tiếng Việt Telex/VNI bị nhảy chữ (`Tiênsg Viêjt`) trong React controlled input?"
8. "Audit file `.ttf` và CSS `@font-face` xem đã hỗ trợ đủ 134 ký tự tiếng Việt, chữ `Đ/đ` và ký hiệu `₫` chưa."
9. "Chuyển đổi danh sách nhãn menu điều hướng (Dashboard, Settings, Billing, Workspace, Members) sang tiếng Việt chuẩn SaaS."
10. "Kiểm tra độ dài ký tự tiếng Việt (+30% expansion) cho các nút bấm và tab bar trên mobile 375px."
11. "Viết thông báo loading state, optimistic UI state và offline banner cho ứng dụng quản lý công việc."
12. "Sửa câu dịch máy 'Làm ơn nhập của bạn địa chỉ thư điện tử để tiếp tục' thành microcopy tự nhiên."
13. "Chuẩn hóa cách dùng đại từ xưng hô trong app: khi nào bỏ chủ ngữ, khi nào dùng 'bạn'?"
14. "Kiểm tra lỗi NFD Unicode tiếng Việt khi copy-paste tên file từ macOS Finder vào ô tìm kiếm."
15. "Xây dựng bảng thuật ngữ (glossary) UI tiếng Việt thống nhất cho toàn bộ design system."

### Boundary / Negative Queries (Route Elsewhere)
16. "Viết landing page bán khóa học luyện thi IELTS cam kết đầu ra B2." -> Route to `vietnamese-education-copy` / `vietnamese-landing-copy`
17. "Soạn công văn gửi Sở Thông tin và Truyền thông theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
18. "Lập báo cáo tình hình tài chính theo Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Viết tài liệu hướng dẫn tích hợp Webhook và REST API bằng tiếng Việt." -> Route to `vietnamese-tech-writing`
20. "Tối ưu câu tiêu đề quảng cáo Facebook Ads và kịch bản livestream TikTok Shop." -> Route to `vietnamese-landing-copy`

---

## 2. `vietnamese-landing-copy` (Landing Pages, Marketing Copy, E-Commerce, Compliance)

### Positive Trigger Queries (Should Route to `vietnamese-landing-copy`)
1. "Viết toàn bộ nội dung landing page cho phần mềm quản lý bán hàng đa kênh tại Việt Nam (Hero, Pain points, Features, Pricing, FAQ)."
2. "Kiểm tra xem câu headline 'Giải pháp ERP số 1 Việt Nam, tốt nhất thị trường' có vi phạm Luật Quảng cáo không."
3. "Viết lại bảng giá SaaS 3 gói (Khởi đầu, Chuyên nghiệp, Doanh nghiệp) hiển thị giá VND và ưu đãi thanh toán theo năm."
4. "Tối ưu phần mô tả sản phẩm thương mại điện tử trên Shopee Mall và TikTok Shop cho ngành mỹ phẩm chính hãng."
5. "Soạn nội dung banner chương trình khuyến mại giảm giá 50% tuân thủ Nghị định 81/2018/NĐ-CP và Nghị định 128/2024/NĐ-CP."
6. "Viết mẫu checkbox xin sự đồng ý xử lý dữ liệu cá nhân (PDPD) trên form đăng ký nhận tư vấn theo Nghị định 13/2023/NĐ-CP."
7. "Viết 5 biến thể Hero section và nút CTA cho ứng dụng đặt lịch khám bệnh trực tuyến."
8. "Chỉnh sửa bài viết PR / KOL review có gắn nhãn tài trợ theo Luật Quảng cáo sửa đổi 75/2025/QH15."
9. "Viết nội dung chân trang (footer) website thương mại điện tử chuẩn thông báo Bộ Công Thương (Nghị định 52/2013 & 85/2021)."
10. "Chuyển đổi landing page tiếng Anh sang tiếng Việt sao cho không bị sượng kiểu dịch word-by-word ('Unlock your potential')."
11. "Viết chuỗi 3 email onboarding và giới thiệu tính năng mới cho người dùng dùng thử miễn phí 14 ngày."
12. "Soạn phần Social Proof và Case Study khách hàng doanh nghiệp với số liệu định lượng chuẩn tiếng Việt."
13. "Kiểm tra cách viết giá tiền '1.250.000 ₫/tháng' vs '1.5M VND' trên trang bảng giá."
14. "Viết câu cảnh báo bắt buộc 'Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh' cho landing page thực phẩm bảo vệ sức khỏe."
15. "Tối ưu khoảng trắng không ngắt dòng (`\u00A0`) cho các tiêu đề quảng cáo tiếng Việt để không bị rớt 1 âm tiết xuống dòng."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn biên bản nghiệm thu bàn giao hệ thống phần mềm giữa hai công ty." -> Route to `vietnamese-business-comms`
17. "Viết thông báo lỗi HTTP 429 Too Many Requests trong tài liệu SDK." -> Route to `vietnamese-tech-writing`
18. "Giải thích cách tính lãi suất trên dư nợ giảm dần cho khoản vay mua nhà." -> Route to `vietnamese-finance-copy`
19. "Viết nhận xét học bạ cuối kỳ cho học sinh lớp 6 theo Thông tư 22/2021/TT-BGDĐT." -> Route to `vietnamese-education-copy`
20. "Sửa lỗi ICU MessageFormat trong file `messages.vi.arb` của ứng dụng Flutter." -> Route to `vn-design-system-ux`

---

## 3. `vietnamese-tech-writing` (Developer Docs, API References, Architecture, Runbooks, Release Notes)

### Positive Trigger Queries (Should Route to `vietnamese-tech-writing`)
1. "Viết tài liệu hướng dẫn tích hợp cổng thanh toán (Authentication, Webhook signature HMAC-SHA256, Idempotency key) bằng tiếng Việt."
2. "Khi viết tài liệu kỹ thuật tiếng Việt, những thuật ngữ nào nên giữ nguyên tiếng Anh (như `webhook`, `payload`, `token`, `idempotent`) và thuật ngữ nào nên dịch?"
3. "Viết bài hướng dẫn Quickstart cài đặt CLI và cấu hình biến môi trường cho lập trình viên Việt Nam."
4. "Soạn bản ghi chú phát hành (Changelog / Release Notes) phiên bản v2.4.0 theo chuẩn Keep a Changelog bằng tiếng Việt."
5. "Viết báo cáo phân tích sự cố (Post-mortem / RCA) sau đợt gián đoạn cơ sở dữ liệu kéo dài 25 phút."
6. "Viết tài liệu Architecture Decision Record (ADR) về việc chuyển đổi từ REST sang gRPC cho dịch vụ thanh toán."
7. "Soạn quy trình vận hành chuẩn (Runbook / SOP) xử lý cảnh báo tràn bộ nhớ Redis trên cụm Kubernetes."
8. "Chuẩn hóa bảng mã lỗi API (Error Codes Reference) với cột mô tả nguyên nhân và cách khắc phục bằng tiếng Việt."
9. "Dịch bình luận mã nguồn (docstrings) và README kỹ thuật sang tiếng Việt mà không làm hỏng tên biến hoặc cú pháp lệnh."
10. "Kiểm tra tài liệu cấu hình phần cứng MacBook Pro chip Apple M2 Max xem có bị công cụ bắt nhầm `M2` thành mét vuông `m²` không."
11. "Viết tài liệu hướng dẫn bảo mật OAuth 2.0 PKCE và quản lý khóa API cho đối tác tích hợp."
12. "Cấu trúc lại tài liệu nội bộ theo mô hình Diátaxis (Tutorials, How-to Guides, Reference, Explanation) bằng tiếng Việt."
13. "Viết hướng dẫn khắc phục sự cố (Troubleshooting Guide) khi kết nối WebSocket bị ngắt quãng."
14. "Biên tập bài blog kỹ thuật chuyên sâu giải thích cơ chế chống ghi đè đồng thời (Optimistic Concurrency Control)."
15. "Kiểm tra các khối mã lệnh (fenced code blocks) trong tài liệu Markdown tiếng Việt để đảm bảo trình kiểm tra chính tả không sửa nhầm code."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn tờ trình xin phê duyệt ngân sách mua sắm máy chủ năm 2026." -> Route to `vietnamese-business-comms`
17. "Viết copy cho nút bấm và hộp thoại xác nhận trong trang cài đặt tài khoản." -> Route to `vn-design-system-ux`
18. "Viết nội dung quảng cáo khóa học lập trình Python cho người mới bắt đầu." -> Route to `vietnamese-education-copy`
19. "Soạn điều khoản biểu phí chuyển tiền nhanh Napas 247." -> Route to `vietnamese-finance-copy`
20. "Viết lời chào mừng khách hàng mới trên trang chủ thương mại điện tử." -> Route to `vietnamese-landing-copy`

---

## 4. `vietnamese-business-comms` (Administrative Docs NĐ 30/2020, B2B Emails, Zalo ZNS, Proposals)

### Positive Trigger Queries (Should Route to `vietnamese-business-comms`)
1. "Soạn công văn đề nghị phối hợp triển khai hóa đơn điện tử gửi Cục Thuế theo đúng thể thức Nghị định 30/2020/NĐ-CP."
2. "Viết tờ trình gửi Hội đồng Quản trị và Ban Tổng Giám đốc xin phê duyệt ngân sách dự án chuyển đổi số Quý III/2026."
3. "Soạn quyết định bổ nhiệm Giám đốc Khối Công nghệ thông tin chuẩn mẫu văn bản hành chính doanh nghiệp."
4. "Viết biên bản họp nghiệm thu giai đoạn 1 dự án triển khai ERP giữa bên A và bên B."
5. "Thiết kế bộ mẫu tin nhắn Zalo ZNS (Tag 1 xác nhận đơn hàng, Tag 2 cập nhật vận chuyển) không vi phạm quy định chống rác Nghị định 91/2020/NĐ-CP."
6. "Viết email B2B gửi Giám đốc Tài chính của đối tác để đề xuất lịch họp trình bày giải pháp tự động hóa đối soát."
7. "Soạn thông báo nghỉ lễ Quốc khánh 2/9 gửi toàn thể cán bộ nhân viên và Quý Đối tác, Khách hàng."
8. "Kiểm tra lỗi viết lời chào 'Gửi Anh Hùng,' trong email doanh nghiệp và sửa lại thành 'Kính gửi anh Hùng,'."
9. "Soạn thư xin lỗi chính thức gửi khách hàng doanh nghiệp về sự cố gián đoạn dịch vụ kèm phương án đền bù SLA."
10. "Viết thư mời thầu / hồ sơ yêu cầu (RFP) cung cấp dịch vụ kiểm toán bảo mật thông tin."
11. "Kiểm tra cách trình bày quốc hiệu, tiêu ngữ (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM / Độc lập - Tự do - Hạnh phúc`) và ký thay (`KT.`), thừa lệnh (`TL.`)."
12. "Soạn công văn giải trình chậm nộp hồ sơ bảo hiểm xã hội gửi cơ quan BHXH quận."
13. "Viết đề xuất hợp tác thương mại (B2B Partnership Proposal) gửi chuỗi bán lẻ toàn quốc."
14. "Soạn mẫu tin nhắn SMS thương hiệu (Brandname SMS) có tiền tố `[QC]` và cú pháp từ chối `Soạn TC gửi...` đúng chuẩn."
15. "Chỉnh sửa văn phong email催 thu công nợ quá hạn lần 1 và lần 2 sao cho lịch sự, chuyên nghiệp nhưng dứt khoát."

### Boundary / Negative Queries (Route Elsewhere)
16. "Viết tài liệu mô tả các trường JSON của API tạo hóa đơn." -> Route to `vietnamese-tech-writing`
17. "Thiết kế trạng thái trống (empty state) khi danh sách công văn chưa có dữ liệu." -> Route to `vn-design-system-ux`
18. "Định khoản nghiệp vụ phải trả cổ tức theo tài khoản 332 của Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Viết đề cương học phần (Syllabus) môn Quản trị Kinh doanh bậc đại học." -> Route to `vietnamese-education-copy`
20. "Viết tiêu đề quảng cáo Google Search Ads cho dịch vụ chữ ký số." -> Route to `vietnamese-landing-copy`

---

## 5. `vietnamese-finance-copy` (Banking, Fintech, E-Wallets, Securities, Accounting TT 99/2025/TT-BTC)

### Positive Trigger Queries (Should Route to `vietnamese-finance-copy`)
1. "Cập nhật thuật ngữ báo cáo tài chính trên phần mềm kế toán từ Thông tư 200/2014/TT-BTC sang Thông tư 99/2025/TT-BTC (Báo cáo tình hình tài chính, TK 215, TK 332, TK 82112)."
2. "Viết nội dung màn hình xác nhận chuyển tiền nhanh Napas 247 và quét mã VietQR trên ứng dụng ngân hàng số."
3. "Soạn bảng công bố thông tin lãi suất vay tiêu dùng, phân biệt rõ lãi suất theo dư nợ gốc ban đầu và lãi suất theo dư nợ giảm dần."
4. "Kiểm tra nội dung giới thiệu sản phẩm chứng chỉ quỹ và trái phiếu doanh nghiệp để đảm bảo không dùng từ 'tiết kiệm cam kết lợi nhuận không rủi ro'."
5. "Viết hướng dẫn xác thực sinh trắc học khuôn mặt (NFC CCCD gắn chip) cho giao dịch chuyển tiền trên 10 triệu đồng theo quy định NHNN."
6. "Chuẩn hóa cách đọc số tiền bằng chữ trên hóa đơn GTGT điện tử (ví dụ: `1.025.000 ₫` -> `Một triệu không trăm hai mươi lăm nghìn đồng chẵn`)."
7. "Viết thông báo biến động số dư tài khoản thanh toán và sao kê thẻ tín dụng hàng tháng."
8. "Soạn bảng tóm tắt quyền lợi và điểm loại trừ trách nhiệm cho sản phẩm bảo hiểm sức khỏe trực tuyến."
9. "Biên tập bản nhận định thị trường chứng khoán (VN-Index, thanh khoản khớp lệnh, khối ngoại mua ròng) đúng thuật ngữ UBCKNN."
10. "Viết thông báo nhắc lịch thanh toán dư nợ tối thiểu thẻ tín dụng và phí phạt chậm thanh toán."
11. "Kiểm tra định dạng số tiền VND, tỷ lệ phần trăm lãi suất (`6,5%/năm`) và mã giao dịch trên biên lai điện tử."
12. "Soạn điều khoản sử dụng dịch vụ ví điện tử và hạn mức giao dịch theo xác thực eKYC."
13. "Giải thích các chỉ số tài chính (ROE, ROA, P/E, P/B, biên lợi nhuận gộp) bằng tiếng Việt dễ hiểu cho nhà đầu tư cá nhân."
14. "Viết kịch bản thông báo xử lý giao dịch treo (tra soát, hoàn tiền về tài khoản nguồn trong 3–5 ngày làm việc)."
15. "Kiểm tra hệ thống danh mục tài khoản kế toán mới áp dụng từ ngày 01/01/2026 theo Thông tư 99/2025/TT-BTC."

### Boundary / Negative Queries (Route Elsewhere)
16. "Viết tài liệu kỹ thuật hướng dẫn kiểm tra chữ ký RSA của cổng thanh toán." -> Route to `vietnamese-tech-writing`
17. "Thiết kế line-height và bảng màu cho hệ thống nút bấm trong Figma." -> Route to `vn-design-system-ux`
18. "Soạn công văn gửi Ngân hàng Nhà nước chi nhánh TP.HCM theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
19. "Viết bài giảng môn Tài chính Doanh nghiệp cho sinh viên năm 3." -> Route to `vietnamese-education-copy`
20. "Viết bài quảng cáo chương trình khuyến mại mở thẻ tặng vali." -> Route to `vietnamese-landing-copy`

---

## 6. `vietnamese-education-copy` (EdTech, LMS, K-12 MOET TT 22/2021, University, KNLNN 6 Bậc)

### Positive Trigger Queries (Should Route to `vietnamese-education-copy`)
1. "Chuẩn hóa hệ thống thuật ngữ đánh giá học sinh THCS/THPT trên phần mềm học bạ số theo Thông tư 22/2021/TT-BGDĐT (`Tốt`, `Khá`, `Đạt`, `Chưa đạt`)."
2. "Viết mẫu nhận xét định kỳ của giáo viên chủ nhiệm gửi phụ huynh học sinh tiểu học và trung học cơ sở sao cho mang tính xây dựng, khích lệ."
3. "Kiểm tra nội dung tư vấn khóa học tiếng Anh để quy đổi đúng chuẩn Khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam (KNLNN 6 bậc / VSTEP) theo Thông tư 01/2014/TT-BGDĐT."
4. "Sửa lại các câu quảng cáo khóa học vi phạm kiểu 'Cam kết 100% đỗ đại học' hoặc 'Cấp bằng chuẩn Quốc gia chỉ sau 2 tuần'."
5. "Thiết kế đề cương học phần (Course Syllabus) và chuẩn đầu ra (Learning Outcomes theo thang Bloom) cho khóa học Phân tích Dữ liệu."
6. "Viết hệ thống câu hỏi trắc nghiệm khách quan 4 lựa chọn (MCQ) kèm giải thích chi tiết cho đúng và cho từng phương án nhiễu."
7. "Soạn thông báo kết quả học tập, lịch thi học kỳ và nhắc hoàn thành học phí gửi phụ huynh/sinh viên."
8. "Xây dựng rubric chấm điểm bài tập lớn (Tiêu chí, Trọng số, Mô tả mức Xuất sắc / Tốt / Đạt / Cần cải thiện)."
9. "Viết nội dung màn hình xin sự đồng ý của cả phụ huynh và học sinh từ 7 đến dưới 16 tuổi trên ứng dụng học tập trực tuyến theo Điều 20 Nghị định 13/2023/NĐ-CP."
10. "Soạn lời dẫn bài giảng video (Instructional Script) và tóm tắt kiến thức trọng tâm cuối bài cho học sinh lớp 10."
11. "Phân biệt chính xác cách dùng 'Chứng chỉ', 'Chứng nhận hoàn thành khóa học' và 'Văn bằng' trên trang giới thiệu chương trình đào tạo."
12. "Viết chuỗi thông báo khích lệ chuỗi ngày học liên tục (streak), nhắc bài tập về nhà và phản hồi khi học viên làm sai bài tập trên LMS."
13. "Chuyển đổi thuật ngữ cũ ('Học lực Yếu / Kém', 'Học sinh Tiên tiến') sang thuật ngữ chuẩn Chương trình GDPT 2018."
14. "Soạn cẩm nang hướng dẫn tân sinh viên đăng ký tín chỉ và quy chế đào tạo đại học."
15. "Viết thư mời phụ huynh tham dự buổi họp tổng kết học kỳ I và tư vấn định hướng chọn tổ hợp môn lớp 10."

### Boundary / Negative Queries (Route Elsewhere)
16. "Viết tài liệu hướng dẫn cấu hình máy chủ Moodle LMS trên Ubuntu 24.04." -> Route to `vietnamese-tech-writing`
17. "Kiểm tra độ phủ glyph tiếng Việt của file font chữ dùng trong app học tập." -> Route to `vn-design-system-ux`
18. "Hạch toán học phí nhận trước vào tài khoản doanh thu chưa thực hiện theo Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Soạn quyết định thành lập Hội đồng thi của trường theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
20. "Tối ưu tỷ lệ chuyển đổi (CRO) cho nút đăng ký nhận tư vấn trên landing page." -> Route to `vietnamese-landing-copy`
