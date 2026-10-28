---
title: "DESIGN:OS Vietnamese — Skill Routing & Trigger Queries Benchmark (200 Queries Across 10 Skills)"
version: "4.0.0"
---

# DESIGN:OS Vietnamese — Skill Routing & Trigger Queries Benchmark (200 Queries)

This benchmark tests skill discovery, trigger accuracy, and boundary disambiguation across all **10 production skills** in **DESIGN:OS Vietnamese**. Each skill has 15 positive trigger queries (Vietnamese, English, and code-switched VI/EN) and 5 negative/boundary disambiguation queries (**200 queries total**).

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
16. "Viết phiếu nhận xét trẻ mẫu giáo 5 tuổi theo 5 lĩnh vực phát triển." -> Route to `vietnamese-education-copy`
17. "Soạn công văn gửi Sở Thông tin và Truyền thông theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
18. "Lập báo cáo tình hình tài chính theo Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Soạn hợp đồng cung ứng dịch vụ phần mềm có điều khoản phạt vi phạm 8%." -> Route to `vietnamese-legal-contracts`
20. "Viết hướng dẫn chăm sóc người bệnh sau xuất viện." -> Route to `vietnamese-healthcare-copy`

---

## 2. `vietnamese-landing-copy` (Landing Pages, Marketing Copy, E-Commerce, Compliance)

### Positive Trigger Queries (Should Route to `vietnamese-landing-copy`)
1. "Viết toàn bộ nội dung landing page cho phần mềm quản lý bán hàng đa kênh tại Việt Nam (Hero, Pain points, Features, Pricing, FAQ)."
2. "Kiểm tra xem câu headline 'Giải pháp ERP số 1 Việt Nam, tốt nhất thị trường' có vi phạm Luật Quảng cáo không."
3. "Viết lại bảng giá SaaS 3 gói (Khởi đầu, Chuyên nghiệp, Doanh nghiệp) hiển thị giá VND và ưu đãi thanh toán theo năm."
4. "Tối ưu phần mô tả sản phẩm thương mại điện tử trên Shopee Mall và TikTok Shop cho ngành mỹ phẩm chính hãng."
5. "Soạn nội dung banner chương trình khuyến mại giảm giá 50% tuân thủ Nghị định 81/2018/NĐ-CP và Nghị định 128/2024/NĐ-CP."
6. "Viết mẫu checkbox xin sự đồng ý xử lý dữ liệu cá nhân (PDPD) trên form đăng ký nhận tư vấn theo Luật 91/2025/QH15 Điều 9 và Nghị định 356/2025/NĐ-CP Điều 6."
7. "Viết 5 biến thể Hero section và nút CTA cho nền tảng quản lý chuỗi cửa hàng."
8. "Chỉnh sửa bài viết PR / KOL review có gắn nhãn tài trợ theo Luật Quảng cáo sửa đổi 75/2025/QH15."
9. "Viết nội dung chân trang (footer) website thương mại điện tử chuẩn thông báo Bộ Công Thương (Nghị định 52/2013 & 85/2021)."
10. "Chuyển đổi landing page tiếng Anh sang tiếng Việt sao cho không bị sượng kiểu dịch word-by-word ('Unlock your potential')."
11. "Viết chuỗi 3 email onboarding và giới thiệu tính năng mới cho người dùng dùng thử miễn phí 14 ngày."
12. "Soạn phần Social Proof và Case Study khách hàng doanh nghiệp với số liệu định lượng chuẩn tiếng Việt."
13. "Kiểm tra cách viết giá tiền '1.250.000 ₫/tháng' vs '1.5M VND' trên trang bảng giá."
14. "Viết bài giới thiệu dự án căn hộ chung cư cao cấp có diện tích 85 m² đúng chuẩn pháp lý bất động sản."
15. "Tối ưu khoảng trắng không ngắt dòng (`\u00A0`) cho các tiêu đề quảng cáo tiếng Việt để không bị rớt 1 âm tiết xuống dòng."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn biên bản nghiệm thu bàn giao hệ thống phần mềm giữa hai công ty." -> Route to `vietnamese-business-comms`
17. "Viết thông báo lỗi HTTP 429 Too Many Requests trong tài liệu SDK." -> Route to `vietnamese-tech-writing`
18. "Giải thích cách tính lãi suất trên dư nợ giảm dần cho khoản vay mua nhà." -> Route to `vietnamese-finance-copy`
19. "Soạn đề cương luận án tiến sĩ theo Thông tư 18/2021/TT-BGDĐT." -> Route to `vietnamese-education-copy`
20. "Soạn thư mời nhận việc (Offer Letter) có mức lương thử việc 85%." -> Route to `vietnamese-hr-recruitment`

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
18. "Viết chương trình đào tạo mô-đun nghề Quản trị mạng trình độ Cao đẳng." -> Route to `vietnamese-education-copy`
19. "Soạn hợp đồng chuyển giao quyền sở hữu trí tuệ mã nguồn phần mềm." -> Route to `vietnamese-legal-contracts`
20. "Viết JD tuyển dụng Kỹ sư DevOps Senior lương Gross 60–80 triệu." -> Route to `vietnamese-hr-recruitment`

---

## 4. `vietnamese-business-comms` (Administrative Docs NĐ 30/2020, B2B Emails, Zalo ZNS, Quotations)

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
10. "Viết bảng báo giá dịch vụ phần mềm B2B có đầy đủ điều khoản thuế GTGT và thời hạn hiệu lực báo giá."
11. "Kiểm tra cách trình bày quốc hiệu, tiêu ngữ (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM / Độc lập - Tự do - Hạnh phúc`) và ký thay (`KT.`), thừa lệnh (`TL.`)."
12. "Soạn công văn giải trình chậm nộp hồ sơ bảo hiểm xã hội gửi cơ quan BHXH quận."
13. "Viết đề xuất hợp tác thương mại (B2B Partnership Proposal) gửi chuỗi bán lẻ toàn quốc."
14. "Soạn mẫu tin nhắn SMS thương hiệu (Brandname SMS) có tiền tố `[QC]` và cú pháp từ chối `Soạn TC gửi...` đúng chuẩn."
15. "Chỉnh sửa văn phong email nhắc thanh toán công nợ quá hạn (dunning email) sao cho lịch sự, chuyên nghiệp nhưng dứt khoát."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn hợp đồng thương mại có điều khoản trọng tài VIAC và phạt vi phạm 8%." -> Route to `vietnamese-legal-contracts`
17. "Thiết kế trạng thái trống (empty state) khi danh sách công văn chưa có dữ liệu." -> Route to `vn-design-system-ux`
18. "Định khoản nghiệp vụ phải trả cổ tức theo tài khoản 332 của Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Soạn thông báo chậm chuyến bay gửi hành khách theo Thông tư 19/2023/TT-BGTVT." -> Route to `vietnamese-hospitality-travel`
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
12. "Soạn điều khoản biểu phí dịch vụ ví điện tử và hạn mức giao dịch theo xác thực eKYC."
13. "Giải thích các chỉ số tài chính (ROE, ROA, P/E, P/B, biên lợi nhuận gộp) bằng tiếng Việt dễ hiểu cho nhà đầu tư cá nhân."
14. "Viết kịch bản thông báo xử lý giao dịch treo (tra soát, hoàn tiền về tài khoản nguồn trong 3–5 ngày làm việc)."
15. "Kiểm tra hệ thống danh mục tài khoản kế toán mới áp dụng từ ngày 01/01/2026 theo Thông tư 99/2025/TT-BTC."

### Boundary / Negative Queries (Route Elsewhere)
16. "Viết tài liệu kỹ thuật hướng dẫn kiểm tra chữ ký RSA của cổng thanh toán." -> Route to `vietnamese-tech-writing`
17. "Soạn hợp đồng vay tài sản có thế chấp quyền sử dụng đất theo Bộ luật Dân sự 2015." -> Route to `vietnamese-legal-contracts`
18. "Soạn công văn gửi Ngân hàng Nhà nước chi nhánh TP.HCM theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
19. "Viết đề cương luận văn thạc sĩ chuyên ngành Tài chính - Ngân hàng." -> Route to `vietnamese-education-copy`
20. "Tính lương Gross sang Net và mức đóng BHXH trong thư mời nhận việc." -> Route to `vietnamese-hr-recruitment`

---

## 6. `vietnamese-education-copy` (7-Tier Pedagogy Continuum: Mầm Non -> Tiểu Học -> THCS/THPT -> GDNN -> Đại Học -> Thạc Sĩ -> Tiến Sĩ & GS/PGS)

### Positive Trigger Queries (Should Route to `vietnamese-education-copy`)
1. "Viết phiếu nhận xét trẻ mẫu giáo 4–5 tuổi trong Sổ theo dõi sức khỏe và đánh giá sự phát triển của trẻ theo 5 lĩnh vực (Thể chất, Nhận thức, Ngôn ngữ, Tình cảm - Kỹ năng xã hội, Thẩm mỹ) chuẩn VBHN 01/VBHN-BGDĐT."
2. "Kiểm tra sổ liên lạc mầm non nhà trẻ 24 tháng tuổi xem giáo viên có lỡ chấm điểm 9/10 hay xếp loại Học lực Giỏi trái quy định không (`EDU011`)."
3. "Viết nhận xét học bạ học sinh lớp 3 theo Thông tư 27/2020/TT-BGDĐT với 3 mức môn học (`Hoàn thành tốt`, `Hoàn thành`, `Chưa hoàn thành`) và 3 mức phẩm chất/năng lực (`Tốt`, `Đạt`, `Cần cố gắng`)."
4. "Chuẩn hóa hệ thống thuật ngữ đánh giá học sinh THCS/THPT trên phần mềm học bạ số theo Thông tư 22/2021/TT-BGDĐT (`Tốt`, `Khá`, `Đạt`, `Chưa đạt`)."
5. "Thiết kế chương trình mô-đun nghề Kỹ thuật chế biến món ăn trình độ Cao đẳng theo Thông tư 04/2022/TT-BLĐTBXH."
6. "Soạn đề cương chi tiết học phần (Course Syllabus) bậc Đại học theo Thông tư 08/2021/TT-BGDĐT gắn ma trận chuẩn đầu ra PLO/CLO và thang Bloom."
7. "Kiểm tra cách dùng thuật ngữ công trình tốt nghiệp: khi nào gọi là `Khóa luận tốt nghiệp / Đồ án tốt nghiệp` (Đại học), `Luận văn thạc sĩ / Đề án thạc sĩ` (Thạc sĩ TT 23/2021), và `Luận án tiến sĩ` (Tiến sĩ TT 18/2021) (`EDU008`)."
8. "Soạn đề cương nghiên cứu và tóm tắt Luận án Tiến sĩ cho Nghiên cứu sinh (NCS) kèm danh mục công bố quốc tế WoS (SCIE/SSCI) và Scopus Q1 theo Thông tư 18/2021/TT-BGDĐT."
9. "Kiểm tra lỗi nhầm lẫn giữa Học hàm/Chức danh (`GS.`, `PGS.`) và Học vị (`TS.`, `ThS.`, `CN.`) kiểu viết sai 'học hàm Tiến sĩ' hoặc 'học vị Giáo sư' (`EDU004`)."
10. "Phân biệt chương trình Thạc sĩ định hướng nghiên cứu (bảo vệ Luận văn thạc sĩ) và Thạc sĩ định hướng ứng dụng (bảo vệ Đề án thạc sĩ) theo Thông tư 23/2021/TT-BGDĐT."
11. "Kiểm tra nội dung tư vấn khóa học tiếng Anh để quy đổi đúng chuẩn Khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam (KNLNN 6 bậc / VSTEP) theo Thông tư 01/2014/TT-BGDĐT."
12. "Sửa lại các câu quảng cáo khóa học vi phạm kiểu 'Cam kết 100% đỗ đại học' hoặc 'Cấp bằng chuẩn Quốc gia chỉ sau 2 tuần'."
13. "Viết nội dung màn hình xin sự đồng ý kép của cả phụ huynh và học sinh từ 7 tuổi trở lên trên ứng dụng học tập trực tuyến theo Điều 24 Luật 91/2025/QH15."
14. "Viết hệ thống câu hỏi trắc nghiệm khách quan 4 lựa chọn (MCQ) kèm giải thích sư phạm cho từng phương án nhiễu."
15. "Soạn biên bản họp Hội đồng đánh giá Luận án Tiến sĩ cấp cơ sở đào tạo đúng chuẩn văn phong học thuật `edu-postgrad`."

### Boundary / Negative Queries (Route Elsewhere)
16. "Viết tài liệu hướng dẫn cấu hình máy chủ Moodle LMS trên Ubuntu 24.04." -> Route to `vietnamese-tech-writing`
17. "Kiểm tra độ phủ glyph tiếng Việt của file font chữ dùng trong app học tập." -> Route to `vn-design-system-ux`
18. "Hạch toán học phí nhận trước vào tài khoản doanh thu chưa thực hiện theo Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Soạn hợp đồng lao động cho giảng viên cơ hữu theo Bộ luật Lao động 2019." -> Route to `vietnamese-legal-contracts`
20. "Viết tin tuyển dụng Giáo viên Mầm non có mức lương thử việc 85%." -> Route to `vietnamese-hr-recruitment`

---

## 7. `vietnamese-healthcare-copy` (Y Tế, Bệnh Viện, Phòng Khám, Dược Phẩm, TPCN & Bệnh Án Điện Tử EMR)

### Positive Trigger Queries (Should Route to `vietnamese-healthcare-copy`)
1. "Kiểm tra bài giới thiệu Thực phẩm bảo vệ sức khỏe (TPCN) xem đã có câu bắt buộc 'Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh' theo Nghị định 15/2018/NĐ-CP chưa (`MED001`)."
2. "Sửa lại nội dung quảng cáo viên uống bổ khớp đang dùng từ vi phạm 'điều trị dứt điểm thoái hóa khớp 100%, cam kết khỏi bệnh vĩnh viễn' và 'thư cảm ơn của bệnh nhân' (`MED002`, `MED005`)."
3. "Cập nhật hồ sơ năng lực bác sĩ trên website bệnh viện từ 'Chứng chỉ hành nghề khám bệnh, chữa bệnh' sang 'Giấy phép hành nghề khám bệnh, chữa bệnh' theo Luật Khám bệnh, chữa bệnh 2023 (`MED003`)."
4. "Soạn mẫu Giấy ra viện và hướng dẫn theo dõi tại nhà sau phẫu thuật nội soi có đầy đủ mục 'Dấu hiệu cần tái khám ngay / cấp cứu' theo Thông tư 32/2023/TT-BYT (`MED007`)."
5. "Chuẩn hóa mẫu đơn thuốc ngoại trú điện tử theo Thông tư 52/2017/TT-BYT và TT 27/2021/TT-BYT (tên hoạt chất quốc tế INN, hàm lượng, liều dùng một lần, số lần/ngày, đường dùng, trước/sau ăn) (`MED004`)."
6. "Viết thông báo trả kết quả xét nghiệm máu và hướng dẫn đặt lịch khám chuyên khoa với văn phong điềm tĩnh, nhân văn, không gây hoang mang cho người bệnh (`MED006`)."
7. "Soạn quy trình hướng dẫn nhịn ăn và chuẩn bị đại tràng trước khi nội soi tiêu hóa gây mê cho Quý khách hàng."
8. "Thiết kế mẫu phiếu tóm tắt bệnh án điện tử (EMR) theo chuẩn Thông tư 32/2023/TT-BYT và mã bệnh ICD-10 tiếng Việt."
9. "Kiểm tra điều khoản bảo mật thông tin bệnh án và dữ liệu sức khỏe nhạy cảm theo Điều 10 Luật Khám bệnh, chữa bệnh 2023 và Luật 91/2025/QH15 Điều 26."
10. "Viết tờ hướng dẫn sử dụng thiết bị y tế gia đình (máy đo huyết áp bắp tay phân loại B theo Nghị định 98/2021/NĐ-CP)."
11. "Chỉnh sửa các cụm từ kỳ thị hoặc đổ lỗi trong ghi chú điều dưỡng ('bệnh nhân không chịu hợp tác', 'bệnh nan y vô phương cứu chữa') sang ngôn ngữ y khoa chuẩn mực (`MED006`)."
12. "Viết nội dung trang giới thiệu gói khám sức khỏe tổng quát định kỳ và tầm soát ung thư sớm tại bệnh viện đa khoa."
13. "Soạn tin nhắn nhắc lịch tiêm chủng vắc-xin định kỳ cho trẻ sơ sinh và hướng dẫn theo dõi phản ứng sau tiêm 24–48 giờ."
14. "Phân biệt rõ 'Thuốc kê đơn (Rx)', 'Thuốc không kê đơn (OTC)' và 'Thực phẩm bảo vệ sức khỏe' trên giao diện nhà thuốc trực tuyến."
15. "Kiểm tra bảng thuật ngữ chuyên khoa Tim mạch, Nội tiết, Chẩn đoán hình ảnh và Xét nghiệm trên ứng dụng đặt lịch khám."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn bảng tóm tắt quyền lợi bảo hiểm nhân thọ và điểm loại trừ bảo hiểm." -> Route to `vietnamese-finance-copy`
17. "Viết giáo trình đào tạo Bác sĩ Nội trú và Đề cương Luận văn Thạc sĩ Y khoa." -> Route to `vietnamese-education-copy`
18. "Soạn hợp đồng mua sắm trang thiết bị y tế giữa bệnh viện và nhà phân phối." -> Route to `vietnamese-legal-contracts`
19. "Viết JD tuyển dụng Điều dưỡng viên trưởng khoa Hồi sức cấp cứu." -> Route to `vietnamese-hr-recruitment`
20. "Tối ưu line-height cho các thẻ chỉ số nhịp tim trên Apple Watch app." -> Route to `vn-design-system-ux`

---

## 8. `vietnamese-legal-contracts` (Hợp Đồng Dân Sự/Thương Mại, Pháp Chế, Điều Khoản ToS, PDPD DPA & SHTT)

### Positive Trigger Queries (Should Route to `vietnamese-legal-contracts`)
1. "Kiểm tra hợp đồng cung ứng dịch vụ phần mềm B2B xem điều khoản 'phạt vi phạm 20% tổng giá trị hợp đồng' có vượt trần 8% theo Điều 301 Luật Thương mại 2005 không (`LEG001`)."
2. "Rà soát mẫu hợp đồng lao động xem có còn dùng thuật ngữ 'Hợp đồng lao động mùa vụ' đã bị bãi bỏ theo Điều 20 Bộ luật Lao động 2019 không (`LEG002`)."
3. "Sửa lại cách viện dẫn điều luật bị dịch theo kiểu Mỹ 'theo quy định tại Điều 15.2(a)' thành đúng chuẩn kỹ thuật lập pháp Việt Nam 'theo quy định tại Điểm a Khoản 2 Điều 15' (`LEG003`)."
4. "Kiểm tra Điều khoản sử dụng dịch vụ (ToS) xem có điều khoản miễn trừ trách nhiệm tuyệt đối trái Điều 25 Luật Bảo vệ quyền lợi người tiêu dùng 2023 không (`LEG004`)."
5. "Soạn Thỏa thuận xử lý dữ liệu cá nhân (DPA) và Chính sách bảo mật có đầy đủ quyền của chủ thể dữ liệu theo Điều 4 khoản 1 Luật 91/2025/QH15 (`LEG007`)."
6. "Loại bỏ các cấu trúc dịch máy từ hợp đồng tiếng Anh ('Bất kể các quy định trái ngược trong hợp đồng này', 'Thời gian là yếu tố cốt lõi của hợp đồng') sang văn phong pháp lý dân luật Việt Nam."
7. "Soạn Hợp đồng dịch vụ công nghệ thông tin có đầy đủ điều khoản Sự kiện bất khả kháng (Điều 156 BLDS 2015), Hoàn cảnh thay đổi cơ bản (Điều 420 BLDS 2015) và Giải quyết tranh chấp tại VIAC (`LEG006`)."
8. "Phân biệt rõ chế tài 'Phạt vi phạm' (Điều 301 Luật Thương mại / Điều 418 BLDS) và 'Bồi thường thiệt hại' (Điều 302 Luật Thương mại) trong hợp đồng thương mại."
9. "Kiểm tra các văn bản hợp đồng cũ còn viện dẫn 'Bộ luật Dân sự 2005', 'Bộ luật Lao động 2012' hoặc 'Luật Doanh nghiệp 2014' đã hết hiệu lực (`LEG005`)."
10. "Soạn điều khoản chuyển nhượng quyền sở hữu trí tuệ và quyền tác giả đối với phần mềm máy tính theo Luật Sở hữu trí tuệ sửa đổi 2022."
11. "Soạn Thỏa thuận bảo mật thông tin (NDA) song phương giữa hai doanh nghiệp trước khi đàm phán M&A."
12. "Soạn Hợp đồng thuê văn phòng thương mại theo Bộ luật Dân sự 2015 và Luật Kinh doanh bất động sản 2023 (đặt cọc Điều 328 BLDS, bàn giao mặt bằng, chấm dứt trước hạn)."
13. "Tư vấn cách soạn điều khoản giới hạn trách nhiệm (Limitation of Liability) hợp pháp theo pháp luật Việt Nam mà không bị vô hiệu."
14. "Soạn phụ lục hợp đồng điều chỉnh đơn giá và tiến độ nghiệm thu dịch vụ."
15. "Chuẩn hóa hệ thống định nghĩa ('Bên A', 'Bên B', 'Ngày Hiệu Lực', 'Thông Tin Mật', 'Sự Kiện Bất Khả Kháng') trong hợp đồng thương mại."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn công văn hành chính gửi Sở Kế hoạch và Đầu tư theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
17. "Viết thư mời nhận việc (Offer Letter) gửi ứng viên trúng tuyển." -> Route to `vietnamese-hr-recruitment`
18. "Viết câu ngắn dưới nút bấm 'Bằng việc nhấn Đăng ký, bạn đồng ý với Điều khoản'." -> Route to `vn-design-system-ux` / `vietnamese-landing-copy`
19. "Lập hóa đơn GTGT và hạch toán thuế TNDN theo Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
20. "Viết tài liệu mô tả luồng xác thực chữ ký số PKI/HSM." -> Route to `vietnamese-tech-writing`

---

## 9. `vietnamese-hospitality-travel` (Du Lịch, Khách Sạn, Resort, Hàng Không & Ẩm Thực F&B)

### Positive Trigger Queries (Should Route to `vietnamese-hospitality-travel`)
1. "Kiểm tra bảng giá phòng resort và thực đơn nhà hàng đang viết '3.500.000 ₫++' mà không giải thích rõ '5% phí phục vụ và 8% thuế GTGT' (`HOS001`)."
2. "Sửa bài quảng cáo khu nghỉ dưỡng và du thuyền tự nhận là 'đẳng cấp 6 sao / 7 sao quốc tế' trái Điều 50 Luật Du lịch 2017 (`HOS002`)."
3. "Soạn email xác nhận đặt phòng khách sạn 5 sao (Booking Confirmation) có đầy đủ giờ nhận phòng (14:00), giờ trả phòng (12:00), chính sách phụ thu nhận sớm/trả muộn và chính sách hoàn hủy (`HOS003`)."
4. "Soạn thông báo thay đổi giờ khởi hành / chậm chuyến bay gửi hành khách có lời xin lỗi chân thành, lý do cụ thể và quyền lợi phục vụ ăn uống/đổi chuyến theo Thông tư 14/2015 và TT 19/2023/TT-BGTVT (`HOS004`)."
5. "Viết thực đơn Fine Dining ẩm thực Việt Nam đương đại kèm ghi chú thành phần gây dị ứng (hải sản, đậu phộng, sữa, gluten) và ghi chú thuế/phí (`HOS005`)."
6. "Chuyển đổi các biển báo nội quy khách sạn khô cứng ('Cấm mang sầu riêng, phạt ngay 2 triệu', 'Khách tự giữ đồ, mất khách sạn không chịu trách nhiệm') sang ngôn ngữ hiếu khách sang trọng (`HOS006`)."
7. "Viết lịch trình tour du lịch nghỉ dưỡng Phú Quốc 4 ngày 3 đêm trọn gói chuẩn Luật Du lịch 2017 (bao gồm/không bao gồm, điều kiện hoàn hủy tour)."
8. "Soạn thư chào mừng Quý khách (Welcome Letter) đặt trong phòng Tổng thống (Presidential Suite) của khu nghỉ dưỡng biển."
9. "Viết quy định hành lý xách tay, hành lý ký gửi và điều kiện hoàn/đổi vé máy bay cho các hạng vé Economy, Deluxe và Business."
10. "Biên tập nội dung giới thiệu liệu trình Spa trị liệu thảo mộc truyền thống tại resort 5 sao."
11. "Soạn kịch bản phản hồi đánh giá của khách lưu trú trên Booking.com và TripAdvisor bằng tiếng Việt lịch thiệp, cầu thị."
12. "Viết thông báo mời Quý khách trải nghiệm tiệc trà chiều (Afternoon Tea) và thực đơn thực dưỡng."
13. "Chuẩn hóa thuật ngữ lưu trú tiếng Việt (hạng phòng tiêu chuẩn/hướng biển, giường đôi lớn/hai giường đơn, nâng hạng phòng miễn phí, bữa sáng tự chọn)."
14. "Soạn hướng dẫn an toàn hồ bơi vô cực và bãi biển riêng tại khu nghỉ dưỡng."
15. "Viết bản đề xuất gói dịch vụ hội nghị kết hợp nghỉ dưỡng (MICE) cho đoàn khách doanh nghiệp 200 người."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn hợp đồng thuê mặt bằng kinh doanh nhà hàng theo Bộ luật Dân sự 2015." -> Route to `vietnamese-legal-contracts`
17. "Viết JD tuyển dụng Quản lý Tiền sảnh (Front Office Manager) khách sạn." -> Route to `vietnamese-hr-recruitment`
18. "Hạch toán doanh thu dịch vụ lưu trú và ăn uống theo Thông tư 99/2025/TT-BTC." -> Route to `vietnamese-finance-copy`
19. "Thiết kế chương trình đào tạo Trung cấp/Cao đẳng nghề Quản trị Khách sạn." -> Route to `vietnamese-education-copy`
20. "Tối ưu giao diện bộ chọn ngày nhận/trả phòng (Date Range Picker) trên mobile." -> Route to `vn-design-system-ux`

---

## 10. `vietnamese-hr-recruitment` (Nhân Sự, Tuyển Dụng, JD, Bộ Luật Lao Động 2019, Offer Letter & OKR/KPI)

### Positive Trigger Queries (Should Route to `vietnamese-hr-recruitment`)
1. "Kiểm tra tin tuyển dụng (JD) xem có chứa các yêu cầu phân biệt đối xử vi phạm Điều 8 Bộ luật Lao động 2019 như 'Chỉ tuyển nữ 18–24 tuổi, ngoại hình ưa nhìn, chưa kết hôn, cam kết không mang thai' không (`HR001`)."
2. "Rà soát Thư mời nhận việc (Offer Letter) đang ghi 'Thời gian thử việc 90 ngày, hưởng 75% lương chính thức' cho vị trí chuyên viên — vi phạm trần 60 ngày và mức sàn 85% lương theo Điều 25 & 26 Bộ luật Lao động 2019 (`HR002`)."
3. "Kiểm tra Offer Letter xem mức lương đề xuất `25.000.000 ₫/tháng` đã ghi rõ là lương `Gross` (trước thuế TNCN và BHXH) hay lương `Net` (thực lĩnh) chưa (`HR003`)."
4. "Phát hiện và chặn các quy định nội bộ trái Điều 17 & 128 Bộ luật Lao động 2019 như 'Công ty giữ bằng đại học gốc khi nhận việc', 'Đặt cọc 5 triệu đồng' hoặc 'Đi muộn 15 phút phạt trừ nửa ngày lương' (`HR004`)."
5. "Viết lại bản Mô tả công việc (JD) đang dùng toàn sáo ngữ ('Lương hấp dẫn theo năng lực, môi trường năng động, chịu được áp lực cực cao 24/7') thành JD minh bạch dải lương, công cụ làm việc và mục tiêu 30-60-90 ngày (`HR005`)."
6. "Chuyển đổi nhận xét đánh giá hiệu suất cuối năm (Performance Review) mang tính công kích cá nhân ('Thái độ kém, lười biếng, thiếu trách nhiệm') sang mô hình phản hồi SBI (Tình huống – Hành vi – Tác động) khách quan (`HR006`)."
7. "Soạn Thư mời nhận việc (Offer Letter) chuẩn mực gửi ứng viên vị trí Kỹ sư Phần mềm Senior (lương Gross, phụ cấp ăn trưa/điện thoại, thời gian thử việc 60 ngày hưởng 85%–100% lương, đóng BHXH theo Luật BHXH 2024)."
8. "Soạn email mời phỏng vấn vòng chuyên môn và email thông báo kết quả chưa phù hợp (Rejection Email) ấm áp, tôn trọng ứng viên."
9. "Xây dựng bộ mục tiêu OKR và chỉ số KPI quý cho phòng Kinh doanh và phòng Sản phẩm bằng tiếng Việt rõ ràng, đo lường được."
10. "Viết thông báo nhân sự nội bộ về chính sách làm việc linh hoạt (Hybrid Working) và quy trình đăng ký nghỉ phép năm (12 ngày phép/năm theo Điều 113 BLLĐ 2019)."
11. "Giải thích bảng tính lương hàng tháng cho nhân viên mới: mức lương đóng BHXH bắt buộc (BHXH 8%, BHYT 1,5%, BHTN 1%), giảm trừ gia cảnh bản thân và người phụ thuộc."
12. "Soạn cẩm nang hội nhập (Onboarding Guide) ngày đầu tiên đi làm cho nhân viên mới."
13. "Viết quy trình đánh giá kết thúc thời gian thử việc và thông báo tiếp nhận chính thức."
14. "Chuẩn hóa thuật ngữ nhân sự tiếng Việt (Tổng thu nhập trước thuế, Thực lĩnh, Thử việc, Bàn giao công việc, Đánh giá năng lực 360 độ, Lộ trình thăng tiến)."
15. "Soạn thông báo điều chỉnh lương định kỳ và thưởng hiệu quả công việc cuối năm."

### Boundary / Negative Queries (Route Elsewhere)
16. "Soạn Hợp đồng lao động xác định thời hạn 24 tháng kèm Phụ lục bảo mật NDA đầy đủ điều khoản pháp lý." -> Route to `vietnamese-legal-contracts`
17. "Soạn Quyết định bổ nhiệm Giám đốc Nhân sự có Quốc hiệu Tiêu ngữ theo Nghị định 30/2020/NĐ-CP." -> Route to `vietnamese-business-comms`
18. "Hạch toán chi phí tiền lương vào TK 642 và thuế TNCN phải nộp vào TK 3335." -> Route to `vietnamese-finance-copy`
19. "Viết tài liệu hướng dẫn tích hợp API máy chấm công khuôn mặt." -> Route to `vietnamese-tech-writing`
20. "Thiết kế bài kiểm tra đánh giá năng lực ngoại ngữ đầu vào theo KNLNN 6 bậc." -> Route to `vietnamese-education-copy`
