<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Real Estate & Construction (`design-os-vietnamese`)

In Vietnamese real estate marketing, project brochures, off-plan sales contracts, and construction bidding documents, deceptive claims, prohibited superlatives, and illegal contract clauses trigger statutory liabilities under the Law on Real Estate Business 2023, Land Law 2024, Housing Law 2023, and Law on Advertising 2012.

---

## 1. Regulated Superlatives & Absolute Claims (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, using superlatives without valid documentary certification from a competent state agency or accredited independent authority is strictly prohibited.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:đẹp\|rẻ\|đắc\s+địa\|sang\s+trọng\|đẳng\s+cấp\|lớn\|quy\s+mô)\s+nhất` | "most beautiful / prime / luxurious / largest" | Common violation in property project marketing |
| `duy\s+nhất` | "the only" | Specifically named in statute |
| `số\s*(?:một\|1)\b` | "number one / No. 1" | Regulated ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Regulated ranking symbol |
| `\bno\.?\s*1\b` | "No. 1" | Regulated ranking text |
| `hàng\s+đầu` | "leading / top" | Prohibited ranking claim without award verification |
| `đứng\s+đầu` | "ranks first" | Prohibited market rank claim |
| `cam\s+kết\s+sinh\s+lời\s+100\s*%` | "guaranteed 100% profit" | Unsubstantiated profit guarantee |
| `vị\s+trí\s+kim\s+cương\s+duy\s+nhất` | "the only diamond location" | Unverified superlative claim |
| `đô\s+thị\s+đẳng\s+cấp\s+nhất` | "most classy urban area" | Unverified quality superlative |
| `sinh\s+lời\s+cao\s+nhất` | "highest return" | Prohibited superlative claim |
| `dự\s+án\s+đáng\s+sống\s+nhất` | "most livable project" | Regulated superlative claim |

---

## 2. Prohibited Statements, Statutory Breaches & Calques (`REA001`–`REA006`)

The following phrases are prohibited across off-plan residential contracts, booking agreements, condominium brochures, and construction BOQ specifications:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale | Severity |
|---|---|---|---|
| `sổ đỏ lâu dài cho condotel` | `thời hạn sở hữu theo thời hạn giao đất của dự án là 50 năm` | Đất thương mại dịch vụ có thời hạn theo dự án tối đa 50 năm (Luật Đất đai 2024 Điều 134) | error |
| `sổ hồng vĩnh viễn cho officetel` | `thời hạn sở hữu 50 năm theo quy hoạch đất thương mại dịch vụ` | Căn hộ văn phòng lưu trú không được cấp quyền sử dụng đất ở lâu dài | error |
| `sở hữu lâu dài vĩnh viễn shophouse thương mại dịch vụ` | `thời hạn sử dụng đất 50 năm theo quy định của Luật Đất đai 2024` | Phân biệt shophouse thương mại dịch vụ với nhà phố thương mại đất ở | error |
| `cam kết lợi nhuận trọn đời condotel` | `chương trình hợp tác khai thác cho thuê theo thỏa thuận thương mại` | Nghiêm cấm cam kết bảo đảm lợi nhuận vô căn cứ gây rủi ro | error |
| `thu tiền đặt cọc 20% giá bán` | `thu tiền đặt cọc tối đa 5% giá bán` | Vi phạm trần đặt cọc 5% tại Điều 23 Khoản 5 Luật Kinh doanh BĐS 2023 | error |
| `thu tiền đặt cọc 15% giá bán` | `thu tiền đặt cọc tối đa 5% giá bán` | Vi phạm trần đặt cọc 5% tại Điều 23 Khoản 5 Luật Kinh doanh BĐS 2023 | error |
| `thu tiền đặt cọc 10% giá bán` | `thu tiền đặt cọc tối đa 5% giá bán` | Vi phạm trần đặt cọc 5% tại Điều 23 Khoản 5 Luật Kinh doanh BĐS 2023 | error |
| `thỏa thuận đặt cọc 15% giá bán` | `thỏa thuận đặt cọc tối đa 5% giá bán` | Đặt cọc off-plan không được vượt quá 5% giá bán | error |
| `đặt cọc giữ chỗ 10% tổng giá trị` | `ký thỏa thuận đặt cọc tối đa 5% khi dự án đủ điều kiện` | Nghiêm cấm huy động vốn trái luật khi chưa đủ điều kiện mở bán | error |
| `thanh toán đợt 1 là 40% giá trị hợp đồng` | `thanh toán đợt 1 không quá 30% giá trị hợp đồng` | Điều 25 Luật Kinh doanh BĐS 2023 khống chế đợt 1 tối đa 30% | error |
| `thanh toán đợt 1 là 50% giá trị hợp đồng` | `thanh toán đợt 1 không quá 30% giá trị hợp đồng` | Vượt trần thanh toán lần đầu 30% per Điều 25 Luật Kinh doanh BĐS 2023 | error |
| `thanh toán 80% trước khi bàn giao nhà` | `thanh toán tối đa 70% trước khi bàn giao nhà` | Thu trước bàn giao tối đa 70% (50% đối với FDI) per Điều 25 | error |
| `thu 100% trước khi bàn giao sổ hồng` | `thu tối đa 95% trước khi bàn giao Giấy chứng nhận` | 5% còn lại chỉ thanh toán khi nhận Giấy chứng nhận per Điều 25 | error |
| `kinh phí bảo trì 3% giá trị căn hộ` | `kinh phí bảo trì 2% giá trị căn hộ trước thuế` | Điều 152 Luật Nhà ở 2023 quy định tỷ lệ cố định 2% | error |
| `kinh phí bảo trì 5% giá trị căn hộ` | `kinh phí bảo trì 2% giá trị căn hộ trước thuế` | Thu sai tỷ lệ luật định 2% per Luật Nhà ở 2023 | error |
| `nộp kinh phí bảo trì ngay khi ký hợp đồng đặt cọc` | `nộp kinh phí bảo trì 2% khi nhận bàn giao căn hộ` | Kinh phí bảo trì chỉ thu khi bàn giao nhà ở per Điều 152 | error |
| `nộp kinh phí bảo trì ngay đợt 1` | `nộp kinh phí bảo trì 2% khi nhận bàn giao nhà` | Thu sớm trái quy định Điều 152 Luật Nhà ở 2023 | error |
| `vùng xanh lá cây` | `mảng xanh` / `công viên cây xanh` | Dịch máy thô từ green area trong quy hoạch kiến trúc | warn |
| `tài sản thực` | `bất động sản` | Dịch máy thô từ real property / real estate | warn |
| `danh sách số lượng` | `bảng tiên lượng mời thầu (BOQ)` | Dịch máy thô từ Bill of Quantities trong hồ sơ mời thầu | warn |
| `căn hộ trên kế hoạch` | `nhà ở hình thành trong tương lai` | Dịch máy thô từ off-plan apartment | warn |
| `tài sản ngoài kế hoạch` | `bất động sản hình thành trong tương lai` | Dịch máy thô từ off-plan property | warn |
| `bàn giao thô ráp` | `bàn giao thô` | Dịch máy thô từ rough / shell handover | warn |
| `chứng chỉ hoàn thành thực chất` | `biên bản nghiệm thu hoàn thành công trình đưa vào sử dụng` | Dịch máy thô từ substantial completion certificate | warn |

---

## 3. Mandatory Statutory Disclosures in Real Estate Marketing

1. **Điều kiện mở bán nhà ở hình thành trong tương lai:**
   - Dự án phải có văn bản thông báo đủ điều kiện bán, cho thuê mua nhà ở hình thành trong tương lai của Sở Xây dựng cấp tỉnh.
   - Phải công khai thông tin về giấy phép xây dựng, quy hoạch 1/500, biên bản nghiệm thu phần móng và hợp đồng bảo lãnh ngân hàng.
2. **Minh bạch loại hình và thời hạn sử dụng đất:**
   - Quảng cáo căn hộ nghỉ dưỡng condotel, căn hộ văn phòng officetel hoặc shophouse xây dựng trên đất thương mại dịch vụ phải nêu rõ thời hạn sử dụng đất (ví dụ: *Thời hạn sở hữu: 50 năm theo thời hạn giao đất của dự án*).
   - Tuyệt đối không mập mờ giữa đất ở ổn định lâu dài và đất kinh doanh thương mại dịch vụ có thời hạn.
