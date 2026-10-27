<!-- vlc-disable: all -->

# Public Administration & Online Public Services Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese public administration, online public service portals, citizen identity, and civil service terminology.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable Public Administration, VNeID & Civil Service Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| online public service | `dịch vụ công cộng trên đường dây` | `dịch vụ công trực tuyến` | Nghị định 42/2022/NĐ-CP | error |
| one-stop shop administrative division | `cửa hàng một điểm dừng` | `Bộ phận Một cửa` / `Trung tâm Phục vụ hành chính công` | Quyết định 468/QĐ-TTg & Nghị định 61/2018/NĐ-CP | error |
| reception and result delivery division | `bàn dịch vụ công dân` | `Bộ phận tiếp nhận và trả kết quả` | Cơ cấu tổ chức tiếp nhận TTHC | error |
| 9-digit citizen ID | `chứng minh nhân dân 9 số còn hiệu lực` | `Thẻ căn cước` | Hết hiệu lực từ 31/12/2024 per Điều 46 Luật Căn cước 2023 | error |
| national population database | `cơ sở dữ liệu dân số toàn quốc` | `Cơ sở dữ liệu quốc gia về dân cư` | Dữ liệu gốc quốc gia per Luật Căn cước 2023 | error |
| electronic identification & authentication | `nhận dạng điện tử cá nhân` | `định danh và xác thực điện tử` | Nghị định 69/2024/NĐ-CP | warn |
| paper household registration book | `sổ hộ khẩu giấy` | `thông tin cư trú trên Cơ sở dữ liệu quốc gia về dân cư / VNeID` | Bãi bỏ từ 01/01/2023 per Điều 38 Luật Cư trú 2020 | error |
| paper temporary residence book | `sổ tạm trú giấy` | `thông tin tạm trú điện tử` | Bãi bỏ từ 01/01/2023 per Luật Cư trú 2020 | error |
| digital public signature | `dấu hiệu kỹ thuật số` | `chữ ký số công vụ` / `chữ ký số chuyên dùng` | Nghị định 30/2020/NĐ-CP về công tác văn thư | error |
| administrative procedure | `thủ tục chính quyền hành chính` | `thủ tục hành chính (TTHC)` | Nghị định 63/2010/NĐ-CP kiểm soát TTHC | error |
| level 3 online public service | `dịch vụ công trực tuyến mức độ 3` | `dịch vụ công trực tuyến một phần` | Bãi bỏ cách chia 4 mức per Điều 11 NĐ 42/2022 | error |
| level 4 online public service | `dịch vụ công trực tuyến mức độ 4` | `dịch vụ công trực tuyến toàn trình` | Bãi bỏ per Điều 11 NĐ 42/2022/NĐ-CP | error |
| short level 3 DVC | `dvc mức 3` | `dịch vụ công trực tuyến một phần` | Bãi bỏ per NĐ 42/2022/NĐ-CP | error |
| short level 4 DVC | `dvc mức 4` | `dịch vụ công trực tuyến toàn trình` | Bãi bỏ per NĐ 42/2022/NĐ-CP | error |
| invalid VNeID level 3 | `vneid mức độ 3` | `Tài khoản định danh điện tử mức độ 2` | Nghị định 69/2024 chỉ có Mức 1 và Mức 2 | error |
| invalid VNeID level 4 | `vneid mức độ 4` | `Tài khoản định danh điện tử mức độ 2` | Nghị định 69/2024 chỉ có Mức 1 và Mức 2 | error |
| invalid VNeID gold tier | `vneid hạng vàng` | `Tài khoản định danh điện tử mức độ 2` | Danh xưng sai trái quy định pháp luật | error |
| invalid electronic identity cap 3 | `tài khoản định danh điện tử cấp 3` | `Tài khoản định danh điện tử mức độ 2` | Nghị định 69/2024/NĐ-CP | error |
| certified electronic true copy | `bản sao điện tử được chứng nhận` | `bản sao điện tử chứng thực từ bản chính` | Nghị định 45/2020/NĐ-CP về TTHC trên môi trường điện tử | warn |
| dossier receipt & appointment slip | `phiếu cuộc hẹn tiếp nhận` | `Giấy tiếp nhận hồ sơ và hẹn trả kết quả` | Mẫu số 01 Thông tư 01/2018/TT-VPCP | error |
| dossier submission slip | `biên nhận tài liệu nộp` | `Giấy tiếp nhận hồ sơ và hẹn trả kết quả` | Văn bản hành chính chuẩn một cửa | warn |
| cadres, civil servants & public employees | `người phục vụ công cộng` | `cán bộ, công chức, viên chức` | Luật Cán bộ, công chức & Luật Viên chức | warn |
| biometric verification | `xác thực số đo sinh học` | `xác thực sinh trắc học` | Thu nhận vân tay, ảnh mặt, mống mắt | warn |
| iris biometric enrollment | `quét mống mắt mắt nhìn` | `thu nhận sinh trắc học mống mắt` | Điều 16 Luật Căn cước 2023 | warn |
| citizen reception hall | `phòng chào đón công dân` | `Phòng Tiếp công dân` | Luật Tiếp công dân 2013 | warn |
| state administrative organ | `cơ quan quản trị nhà nước` | `cơ quan hành chính nhà nước` | Thuật ngữ Hiến pháp và Luật Tổ chức Chính phủ | warn |
| civil status extract | `trích xuất tình trạng dân sự` | `trích lục hộ tịch` / `bản sao trích lục hộ tịch` | Luật Hộ tịch 2014 | error |
| marital status certificate | `giấy chứng nhận độc thân tự do` | `Giấy xác nhận tình trạng hôn nhân` | Nghị định 123/2015/NĐ-CP hướng dẫn Luật Hộ tịch | error |
| authorization letter / power of attorney | `giấy trao quyền đại diện` | `Văn bản ủy quyền` / `Giấy ủy quyền` | Bộ luật Dân sự 2015 Điều 562 | warn |
| administrative enforcement decision | `quyết định của ban quản lý` | `quyết định hành chính` / `quyết định xử phạt vi phạm hành chính` | Luật Xử lý vi phạm hành chính | warn |

---

## 2. Terminology Guidelines & Statutory References

1. **Nghị định 42/2022/NĐ-CP về Cung cấp thông tin và dịch vụ công trực tuyến:**
   - Bãi bỏ hoàn toàn hệ thống phân loại 4 mức độ cũ (Mức độ 1, 2, 3, 4).
   - Chỉ sử dụng hai mức độ chính thức: `Dịch vụ công trực tuyến toàn trình` (toàn bộ quy trình từ nộp, giải quyết, nộp phí đến trả kết quả đều trên môi trường mạng) và `Dịch vụ công trực tuyến một phần` (công dân phải trực tiếp có mặt ở một số khâu).
2. **Luật Căn cước 2023 (số 26/2023/QH15) & Nghị định 69/2024/NĐ-CP:**
   - Từ ngày 01/07/2024, thống nhất tên gọi `Thẻ căn cước`. Chứng minh nhân dân (CMND) 9 số chính thức hết hạn sử dụng từ ngày 31/12/2024.
   - Tài khoản định danh điện tử VNeID chỉ có hai mức độ: `Mức độ 1` (đăng ký qua app) và `Mức độ 2` (thu nhận sinh trắc học tại cơ quan Công an). Không có các mức độ 3, 4 hay danh xưng tự phong như "hạng vàng".
3. **Luật Cư trú 2020 (số 68/2020/QH14) & Nghị định 104/2022/NĐ-CP:**
   - Bãi bỏ hoàn toàn giá trị sử dụng của Sổ hộ khẩu giấy và Sổ tạm trú giấy từ ngày 01/01/2023.
   - Cơ quan nhà nước có nghĩa vụ tra cứu dữ liệu cư trú qua Cơ sở dữ liệu quốc gia về dân cư hoặc ứng dụng VNeID, tuyệt đối không yêu cầu người dân xuất trình sổ hộ khẩu giấy.
4. **Nghị định 30/2020/NĐ-CP về Công tác văn thư:**
   - Chuẩn hóa thể thức văn bản hành chính, văn hóa giao tiếp công sở, loại bỏ thái độ hách dịch, cửa quyền, dọa dẫm công dân.
