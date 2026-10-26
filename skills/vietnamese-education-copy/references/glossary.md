<!-- vlc-disable: all -->

# Educational, Academic, & EdTech Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese educational, pedagogical, university administrative, and EdTech terminology across the 7-tier continuum (Mầm non $\rightarrow$ Tiểu học $\rightarrow$ THCS/THPT $\rightarrow$ GDNN $\rightarrow$ Đại học $\rightarrow$ Thạc sĩ $\rightarrow$ Tiến sĩ & GS/PGS).
The table below is parsed by `validate_copy.py` at runtime; every row acts as an automated lint rule firing `CAL001` with declared severity.

## 1. Machine-Readable Educational & EdTech Terms

<!-- machine-readable: glossary -->

| EN | ❌ Wrong or stale | ✅ Correct | Severity |
|---|---|---|---|
| homeroom teacher | `giáo viên phòng nhà` | `giáo viên chủ nhiệm` | error |
| report card (K-12) | `thẻ báo cáo` | `học bạ` | error |
| home communication notebook | `sách liên lạc` | `sổ liên lạc` | error |
| university syllabus | `giáo trình học phần` | `đề cương chi tiết học phần` | error |
| academic credit | `tín dụng học tập` | `tín chỉ` | error |
| official transcript | `bản dịch điểm` | `bảng điểm` | error |
| diploma reissuance | `cấp lại bằng tốt nghiệp gốc` | `cấp bản sao văn bằng từ sổ gốc` | error |
| university student | `học sinh đại học` | `sinh viên` | error |
| K-12 pupil | `sinh viên nhỏ` | `học sinh` | error |
| submit assignment | `đệ trình bài tập` | `nộp bài` | warn |
| LMS dashboard | `bảng táp-lô học tập` | `bảng tổng quan` | error |
| track progress | `theo dấu sự tiến bộ` | `theo dõi tiến độ học tập` | error |
| leaderboard | `bảng lãnh đạo` | `bảng xếp hạng` | error |
| mastery learning | `học tập làm chủ` | `học tập thông hiểu` | error |
| formative assessment | `đánh giá định hình` | `đánh giá quá trình` | error |
| summative assessment | `đánh giá tóm tắt` | `đánh giá định kỳ` | error |
| learning streak | `vệt học tập` | `chuỗi ngày học tập` | error |
| pedagogical scaffolding | `giàn giáo học tập` | `hỗ trợ từng bước` | error |
| spaced repetition | `lặp lại có khoảng cách xa` | `lặp lại ngắt quãng` | error |
| active recall | `nhớ lại tích cực` | `chủ động gợi nhớ` | error |
| lesson plan | `kế hoạch bài học tây` | `kế hoạch bài dạy / giáo án` | error |
| extracurricular activity | `ngoài chương trình học` | `hoạt động ngoại khóa` | error |
| curriculum framework | `dòng chảy giáo dục` | `chương trình đào tạo / khung chương trình` | error |
| midterm examination | `kiểm tra giữa kỳ hạn` | `kiểm tra giữa kỳ` | error |
| final examination | `kiểm tra kết thúc cuối cùng` | `thi kết thúc học phần / kiểm tra cuối kỳ` | error |
| tuition fee | `tiền thù lao học` | `học phí` | error |
| scholarship | `tàu học bổng` | `học bổng` | error |
| prerequisite course | `khóa học điều kiện tiên quyết` | `học phần tiên quyết` | error |
| elective course | `khóa học tùy chọn bầu cử` | `học phần tự chọn` | error |
| compulsory course | `khóa học bắt buộc cưỡng chế` | `học phần bắt buộc` | error |
| undergraduate thesis | `luận văn tốt nghiệp kết thúc` | `khóa luận tốt nghiệp / đồ án tốt nghiệp` | error |
| master thesis | `luận văn bậc thầy` | `luận văn thạc sĩ` | error |
| doctoral dissertation | `bài luận bác sĩ` | `luận án tiến sĩ` | error |
| academic department / chair | `phòng ban học thuật` | `bộ môn` | error |
| academic advisor | `cố vấn học viện` | `cố vấn học tập` | error |
| course enrollment | `ghi danh khóa học` | `đăng ký học phần` | error |
| drop course | `đánh rơi khóa học` | `hủy đăng ký học phần` | error |
| audit a course | `kiểm toán một môn học` | `dự thính học phần` | error |
| pass / fail grade | `đậu và rớt` | `đạt / chưa đạt` | error |
| credit hour | `giờ tín dụng` | `giờ tín chỉ` | error |
| academic semester | `học kỳ nửa năm` | `học kỳ` | warn |
| student attendance check | `sự có mặt tham dự` | `điểm danh` | error |
| truancy | `trốn việc học` | `trốn học` | error |
| parent-teacher conference | `cuộc họp cha mẹ thầy giáo` | `họp phụ huynh` | error |
| parents association | `hiệp hội phụ huynh học sinh` | `ban đại diện cha mẹ học sinh` | error |
| school principal | `người đứng đầu trường` | `hiệu trưởng` | error |
| vice principal | `người phụ tá hiệu trưởng` | `phó hiệu trưởng` | error |
| student union / council | `hội đồng sinh viên chính trị` | `đoàn thanh niên / hội sinh viên` | error |
| peer assessment | `bạn đồng trang lứa đánh giá` | `đánh giá đồng đẳng` | error |
| self-assessment | `tự kiểm tra bản thân` | `tự đánh giá` | error |
| scoring rubric | `quy tắc chấm điểm rubric` | `tiêu chí đánh giá / thang điểm chi tiết` | error |
| expected learning outcome | `đầu ra học tập` | `chuẩn đầu ra` | error |
| blended learning | `học tập pha trộn` | `học tập kết hợp` | error |
| microlearning | `học tập siêu nhỏ` | `học tập vi mô / bài học ngắn` | error |
| gamification | `trò chơi hóa giải trí` | `trò chơi hóa` | warn |
| diagnostic assessment | `xét nghiệm chẩn đoán học vấn` | `đánh giá chẩn đoán` | error |
| placement exam | `bài thi vị trí xếp lớp` | `bài thi xếp lớp` | error |
| pronunciation scoring | `điểm số phát biểu` | `điểm phát âm` | error |
| tonal recognition | `công nhận cao độ` | `nhận diện thanh điệu` | error |
| phonemic unit | `đơn vị âm vị học` | `âm vị` | error |
| lexical stress | `áp lực giọng nói` | `trọng âm` | error |
| sentence intonation | `giọng điệu bài hát` | `ngữ điệu` | error |
| double consent (child & parent) | `đồng ý kép hai bên` | `sự đồng ý kép của trẻ em và phụ huynh` | error |
| parental consent | `sự cho phép của cha mẹ đơn giản` | `sự đồng ý của phụ huynh` | error |
| student identity card | `chứng minh nhân dân sinh viên` | `thẻ sinh viên / thẻ học sinh` | error |
| student conduct evaluation | `hành vi cư xử cá nhân` | `đánh giá rèn luyện / xếp loại hạnh kiểm` | error |
| academic rank professor | `học vị giáo sư` | `chức danh giáo sư / học hàm giáo sư` | error |
| academic rank associate professor | `học vị phó giáo sư` | `chức danh phó giáo sư / học hàm phó giáo sư` | error |
| doctoral academic degree | `học hàm tiến sĩ` | `học vị tiến sĩ` | error |
| master academic degree | `học hàm thạc sĩ` | `học vị thạc sĩ` | error |
| bachelor academic degree | `học hàm cử nhân` | `học vị cử nhân / bằng cử nhân` | error |
| engineer academic degree | `học hàm kỹ sư` | `học vị kỹ sư / bằng kỹ sư` | error |
| undergraduate thesis mismatch | `luận án cử nhân` | `khóa luận tốt nghiệp / đồ án tốt nghiệp` | error |
| undergraduate university thesis mismatch | `luận án đại học` | `khóa luận tốt nghiệp` | error |
| undergraduate degree dissertation mismatch | `luận án tốt nghiệp đại học` | `khóa luận tốt nghiệp / đồ án tốt nghiệp` | error |
| master thesis mismatch | `luận án thạc sĩ` | `luận văn thạc sĩ / đề án thạc sĩ` | error |
| doctoral thesis mismatch | `khóa luận tiến sĩ` | `luận án tiến sĩ` | error |
| doctoral project mismatch | `đồ án tiến sĩ` | `luận án tiến sĩ` | error |
| postgraduate coursework thesis | `khóa luận thạc sĩ` | `luận văn thạc sĩ / đề án thạc sĩ` | error |
| vocational module | `học phần thợ` | `mô-đun đào tạo nghề` | error |
| vocational credit | `tín dụng tay nghề` | `tín chỉ nghề nghiệp` | error |
| national occupational skill standards | `chuẩn tay nghề quốc tế thô` | `chuẩn kỹ năng nghề quốc gia` | error |
| enterprise internship | `đi làm việc ngoài` | `thực tập tại doanh nghiệp` | error |
| intermediate vocational degree | `bằng thợ trung học` | `bằng tốt nghiệp trung cấp` | error |
| vocational college diploma | `bằng đại học thực hành cấp 2` | `bằng tốt nghiệp cao đẳng` | error |
| practice bachelor title | `cử nhân thực tập` | `cử nhân thực hành` | error |
| practice engineer title | `kỹ sư thực tập nghề` | `kỹ sư thực hành` | error |
| preschool developmental milestone | `cột mốc trưởng thành trẻ` | `chỉ số phát triển của trẻ` | error |
| preschool routine health record | `sách y tế mẫu giáo` | `sổ theo dõi sức khỏe trẻ` | error |
| early childhood physical domain | `lĩnh vực thể xác` | `lĩnh vực phát triển thể chất` | error |
| early childhood cognitive domain` | `lĩnh vực nhận biết trí khôn` | `lĩnh vực phát triển nhận thức` | error |
| early childhood language domain | `lĩnh vực ăn nói` | `lĩnh vực phát triển ngôn ngữ` | error |
| early childhood socio-emotional domain | `lĩnh vực cảm xúc xã hội thô` | `lĩnh vực phát triển tình cảm và kỹ năng xã hội` | error |
| early childhood aesthetic domain | `lĩnh vực làm đẹp nghệ thuật` | `lĩnh vực phát triển thẩm mỹ` | error |
| doctoral candidate | `thí sinh bác sĩ` | `nghiên cứu sinh` | error |
| master student | `học sinh cao học` | `học viên cao học` | error |
| doctoral thesis advisor | `người dạy tiến sĩ` | `người hướng dẫn khoa học` | error |
| doctoral literature review | `bài tiểu luận nhỏ` | `tiểu luận tổng quan` | error |
| doctoral thematic topic | `chủ đề nghiên cứu nhỏ` | `chuyên đề tiến sĩ` | error |
| thesis defense council | `hội đồng bảo hộ luận văn` | `hội đồng đánh giá luận văn / luận án` | error |
| institutional defense | `bảo vệ trường lớp` | `bảo vệ cấp cơ sở` | error |
