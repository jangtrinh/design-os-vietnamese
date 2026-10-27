<!-- vlc-disable: all -->

# Real Estate & Construction Engineering Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese real estate, property development, condominium management, and construction BOQ terminology.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable Real Estate, Land Tenure & Construction BOQ Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| green area / greenery | `vùng xanh lá cây` | `mảng xanh` / `công viên cây xanh` | Mật độ cây xanh trong quy hoạch đô thị | error |
| real estate / real property | `tài sản thực` | `bất động sản` | Thuật ngữ pháp lý per Luật Kinh doanh BĐS 2023 | error |
| bill of quantities (BOQ) | `danh sách số lượng` | `bảng tiên lượng mời thầu (BOQ)` / `bảng khối lượng mời thầu` | Hồ sơ mời thầu xây dựng per NĐ 37/2015/NĐ-CP | error |
| off-plan property | `căn hộ trên kế hoạch` / `tài sản ngoài kế hoạch` | `nhà ở hình thành trong tương lai` / `bất động sản hình thành trong tương lai` | Điều 3 Luật Kinh doanh BĐS 2023 | error |
| rough handover / shell handover | `bàn giao thô ráp` | `bàn giao thô` | Bàn giao kết cấu khung và tường ngăn thô | error |
| substantial completion certificate | `chứng chỉ hoàn thành thực chất` | `biên bản nghiệm thu hoàn thành công trình đưa vào sử dụng` | Văn bản pháp lý nghiệm thu Luật Xây dựng | error |
| usable carpet area | `diện tích thảm` | `diện tích thông thủy` | Điều 141 Luật Nhà ở 2023 | error |
| gross floor area (GFA) | `tổng diện tích sàn thô` | `tổng diện tích sàn xây dựng (GFA)` | Tiêu chuẩn đo vẽ kiến trúc công trình | warn |
| master plan 1/500 | `kế hoạch tổng thể 1/500` | `quy hoạch chi tiết xây dựng tỷ lệ 1/500` | Luật Quy hoạch đô thị | error |
| land use rights certificate | `giấy chứng nhận đất đai` | `Giấy chứng nhận quyền sử dụng đất, quyền sở hữu tài sản gắn liền với đất` | Tên gọi chuẩn mới Luật Đất đai 2024 | error |
| construction permit | `giấy phép cấu trúc` | `giấy phép xây dựng` | Luật Xây dựng 2014 sửa đổi 2020 | error |
| building density | `mật độ dày đặc của tòa nhà` | `mật độ xây dựng` | Quy chuẩn kỹ thuật quốc gia QCVN 01:2021/BXD | error |
| floor area ratio (FAR) | `tỷ lệ sàn trên khu đất` | `hệ số sử dụng đất` | Quy chuẩn kỹ thuật quốc gia QCVN 01:2021/BXD | error |
| building setback | `khoảng lùi lại của tòa nhà` | `khoảng lùi xây dựng` | Khoảng cách từ chỉ giới đường đỏ đến chỉ giới xây dựng | error |
| as-built drawings | `bản vẽ như đã xây dựng` | `bản vẽ hoàn công` | Nghị định 06/2021/NĐ-CP | error |
| MEP systems | `hệ thống ống nước và cơ điện tử` | `hệ thống cơ điện (MEP)` | Cơ điện lạnh, cấp thoát nước và PCCC | warn |
| foundation milestone | `cột mốc móng nhà` | `nghiệm thu phần móng` | Điều kiện mở bán off-plan per Luật KDBĐS | error |
| topping-out ceremony | `lễ đội đỉnh tòa nhà` | `lễ cất nóc` | Hoàn thành thi công kết cấu bê tông tầng mái | error |
| maintenance fund (sinking fund) | `quỹ chìm bảo trì` | `kinh phí bảo trì phần sở hữu chung nhà chung cư` | Điều 152 Luật Nhà ở 2023 (định mức 2%) | error |
| land allocation decision | `quyết định phân bổ đất` | `quyết định giao đất / cho thuê đất` | Quyết định hành chính per Luật Đất đai 2024 | error |
| fire safety acceptance | `sự phê chuẩn an toàn hỏa hoạn` | `nghiệm thu phòng cháy chữa cháy (PCCC)` | Cục Cảnh sát PCCC và CNCH | error |
| show flat / model home | `ngôi nhà mẫu giáo` | `nhà mẫu` / `căn hộ mẫu` | Căn hộ trưng bày phục vụ tiếp thị | error |
| commercial townhouse / shophouse | `nhà phố mua sắm` | `nhà phố thương mại (shophouse)` | Loại hình BĐS hỗn hợp | warn |
| compensation & site clearance | `đền bù xóa sổ mặt bằng` | `bồi thường, hỗ trợ và tái định cư` | Luật Đất đai 2024 Chương VII | error |
| structural safety inspection | `kiểm toán cấu trúc công trình` | `kiểm định an toàn chịu lực công trình` | NĐ 06/2021/NĐ-CP quản lý chất lượng công trình | error |
| concrete slump test | `kiểm tra sự sụt lún bê tông` | `thử độ sụt bê tông` | Tiêu chuẩn TCVN 3106:1993 | warn |
| geotechnical investigation report | `báo cáo đất đai địa chất` | `báo cáo khảo sát địa chất công trình` | Hồ sơ khảo sát xây dựng per Luật Xây dựng | error |
| general contractor | `nhà thầu chính yếu` | `tổng thầu thi công xây dựng` / `nhà thầu chính` | Phân loại nhà thầu per Luật Đấu thầu 2023 | warn |
| subcontractor | `nhà thầu phụ thuộc` | `nhà thầu phụ` | Đơn vị thi công chuyên ngành phụ trợ | warn |
| warranty retention money | `tiền giữ lại công trình` | `tiền bảo hành công trình xây dựng` | Nghị định 37/2015/NĐ-CP về hợp đồng xây dựng | warn |
| defect liability period (DLP) | `thời kỳ chịu trách nhiệm khiếm khuyết` | `thời hạn bảo hành công trình` | Thời hạn bảo hành công trình theo hợp đồng | error |
| handover protocol | `giao thức bàn giao căn hộ` | `biên bản bàn giao nhà ở` | Văn bản xác nhận bàn giao thực tế căn hộ | error |

---

## 2. Terminology Guidelines & Statutory References

1. **Luật Kinh doanh bất động sản 2023 (số 29/2023/QH15):**
   - Phân biệt chính xác giữa `nhà ở có sẵn` và `nhà ở hình thành trong tương lai`.
   - Tiền đặt cọc trong thỏa thuận đặt cọc nhà ở hình thành trong tương lai bị giới hạn ở mức không quá 5% giá bán per Điều 23 Khoản 5.
   - Tiến độ thanh toán phân kỳ được quy định chặt chẽ per Điều 25: đợt 1 tối đa 30%, trước bàn giao nhà tối đa 70% (50% đối với chủ đầu tư FDI), trước cấp Giấy chứng nhận tối đa 95%.
2. **Luật Đất đai 2024 (số 31/2024/QH15) & Luật Nhà ở 2023 (số 27/2023/QH15):**
   - Thời hạn sử dụng đất thương mại dịch vụ (Condotel, Officetel, Shophouse khối đế) theo dự án tối đa 50 năm (hoặc 70 năm). Nghiêm cấm cam kết sổ đỏ lâu dài vĩnh viễn trên đất thương mại dịch vụ.
   - Bắt buộc phân định rõ `diện tích thông thủy` (usable carpet area) và `diện tích tim tường` (wall-center area) per Điều 141 Luật Nhà ở 2023.
   - Kinh phí bảo trì 2% phần sở hữu chung nhà chung cư per Điều 152 Luật Nhà ở 2023 được thu vào thời điểm bàn giao căn hộ, không thu sớm ở giai đoạn đặt cọc.
3. **Nghị định 37/2015/NĐ-CP & Luật Xây dựng:**
   - Sử dụng các biểu mẫu chuẩn mực: Bảng tiên lượng mời thầu (BOQ), Biên bản nghiệm thu hoàn thành công trình đưa vào sử dụng, Bản vẽ hoàn công, Báo cáo khảo sát địa chất.
