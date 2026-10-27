<!-- vlc-disable: all -->

# Vietnamese Media, Journalism & PR Terminology Glossary (`vietnamese-media-journalism-pr`)

This glossary provides standardized Vietnamese journalism, newsroom editorial, press release architecture, and crisis PR terminology under the Press Law 2016 (Luật Báo chí số 103/2016/QH13) and Decree 147/2024/NĐ-CP on Internet services and online information.

The table below is parsed by `validate_copy.py` at runtime; each row acts as an active linting rule firing `CAL001` with the declared severity.

---

## 1. Machine-Readable Journalism, Press & PR Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| for immediate release | `để phát hành ngay lập tức` | `thông cáo báo chí phát hành ngay` / `phát hành ngay` | Tiêu ngữ thông cáo báo chí chuẩn | error |
| for immediate release | `cho sự phát hành ngay` | `thông cáo báo chí phát hành ngay` | Dịch máy thô từ For Immediate Release | error |
| on the record | `trên hồ sơ` | `phát ngôn chính thức` / `thông tin có dẫn nguồn` | Thuật ngữ phỏng vấn báo chí chuẩn | error |
| off the record | `ngoài hồ sơ` | `thông tin hậu trường không trích dẫn` / `thông tin ngoài lề` | Thuật ngữ tác nghiệp báo chí quốc tế | error |
| lead story | `câu chuyện dẫn đầu` | `đoạn mở đầu` / `sapo` / `tin tiêu điểm` | Dịch vụng nghĩa chữ lead | error |
| gatekeeper | `người giữ cổng thông tin` | `biên tập viên kiểm duyệt` / `ban biên tập` | Chuẩn nghề nghiệp cơ quan báo chí | error |
| byline | `dòng chữ ký của tác giả` | `bút danh` / `tên tác giả` | Lỗi dịch thô từ byline | error |
| press release | `phát hành báo chí` | `thông cáo báo chí` | Tên văn kiện truyền thông đối ngoại chính thức | error |
| boilerplate | `tấm kim loại nồi hơi` | `phần giới thiệu doanh nghiệp` / `thông tin tổ chức` | Đoạn tóm tắt giới thiệu cuối thông cáo | error |
| dateline | `dòng thời gian hạn chót` | `địa điểm và thời gian phát hành` / `dateline` | Dòng ghi rõ địa danh, ngày tháng | error |
| media contact | `tiếp xúc phương tiện truyền thông` | `thông tin liên hệ báo chí` / `đầu mối truyền thông` | Thông tin người phụ trách truyền thông | error |
| spin doctor | `bác sĩ quay cuồng` | `chuyên viên xử lý khủng hoảng` / `cố vấn truyền thông` | Dịch máy thô cụm spin doctor | error |
| scoop | `cái xẻng xúc tin tức` | `tin độc quyền` / `phóng sự độc quyền` | Thuật ngữ báo chí điều tra | error |
| op-ed / opinion editorial | `ý kiến biên tập đối diện` | `bài xã luận chuyên gia` / `chuyên mục bình luận` | Thể loại báo chí bình luận chuyên sâu | error |
| embargo / press embargo | `cấm vận tin tức toàn diện` | `thời điểm dỡ bỏ hạn chế xuất bản` / `lệnh phong tỏa thông tin` | Quy định mốc thời gian xuất bản | warn |
| fact check | `kiểm tra sự kiện thô` | `xác minh tính xác thực của thông tin` / `kiểm chứng sự thật` | Quy trình biên tập cốt lõi của tòa soạn | error |
| sound bite | `miếng cắn âm thanh` | `đoạn trích phát biểu` / `phát biểu ngắn gọn` | Trích đoạn phát biểu trên phát thanh/truyền hình | error |
| talking points | `các điểm nói chuyện` | `thông điệp then chốt` / `tài liệu hướng dẫn phát ngôn` | Tài liệu chuẩn bị cho người phát ngôn | warn |
| photo caption | `chú thích hình ảnh máy bay` | `chú thích ảnh` / `chú thích hình` | Phần giải thích nội dung bức ảnh báo chí | error |
| citizen journalism | `báo chí công dân đường phố` | `báo chí công dân` | Hiện tượng truyền thông mạng xã hội | warn |
| press conference | `hội nghị báo chí đông đúc` | `họp báo` / `cuộc họp báo` | Sự kiện truyền thông chính thức | error |
| crisis communication | `giao tiếp khủng hoảng` | `truyền thông xử lý khủng hoảng` | Hoạt động ứng phó rủi ro dư luận | warn |
| retraction | `rút lại bài báo im lặng` | `thông báo cải chính và xin lỗi` / `rút bài có cải chính` | Bắt buộc theo Điều 42 Luật Báo chí 2016 | error |
| defamation | `nói xấu làm hoen ố` | `hành vi xúc phạm danh dự, nhân phẩm` / `bôi nhọ uy tín` | Thuật ngữ pháp lý dân sự và hình sự | error |
| source confidentiality | `sự giữ bí mật nguồn gốc` | `bảo mật nguồn tin báo chí` | Quyền và nghĩa vụ nhà báo Luật Báo chí 2016 | error |
| investigative journalism | `báo chí theo dõi điều tra ngầm` | `báo chí điều tra` | Thể loại báo chí chuyên môn cao | warn |
| wire service | `dịch vụ dây cáp báo chí` | `hãng thông tấn` | TTXVN, Reuters, AP, AFP | error |
| syndication | `liên kết tài chính báo chí` | `chia sẻ bản quyền nội dung báo chí` | Thỏa thuận phân phối lại bài viết | warn |
| news anchor | `mỏ neo tin tức` | `người dẫn chương trình thời sự` / `BTV dẫn sóng` | Thuật ngữ truyền hình chuyên ngành | error |
| media kit | `bộ công cụ phương tiện` | `hồ sơ truyền thông` / `bộ tài liệu báo chí` | Tài liệu phục vụ phóng viên tại sự kiện | warn |
| press agency | `đại lý báo chí` | `cơ quan báo chí` | Luật Báo chí 2016 phân định rõ với đại lý phát hành | error |
| advertorial | `quảng cáo bài báo ngụy trang` | `bài viết truyền thông` / `bài PR` | Bài viết giới thiệu sản phẩm có tài trợ | warn |
