<!-- vlc-disable: all -->

# Labor Code & Offer Letter Compliance Standards (`design-os-vietnamese`)

This reference document establishes the statutory and legal compliance standards for employment contracts, job offer letters, probation agreements, and workplace policies under the Labor Code 2019 (**Bộ luật Lao động số 45/2019/QH14**) and the Law on Social Insurance (**Luật Bảo hiểm xã hội số 41/2024/QH15**).

---

## 1. Statutory Foundations of the Labor Code 2019

Vietnam's labor legal framework provides strict employee protections. Drafting employment copy without adhering to these statutes creates civil invalidity and administrative sanctions.

### 1.1 Prohibition of Discrimination in Employment (Điều 8 Khoản 1)
- Nghiêm cấm phân biệt đối xử trong lao động dựa trên giới tính, dân tộc, màu da, thành phần xã hội, tình trạng hôn nhân, tín ngưỡng, tôn giáo, nhiễm HIV, khuyết tật hoặc vì lý do thành lập, gia nhập và hoạt động công đoàn.
- Tuyển dụng nhân sự (`job-description`) không được đưa ra các tiêu chí giới hạn giới tính (*"chỉ tuyển nam/nữ"*), tình trạng hôn nhân (*"yêu cầu chưa kết hôn"*), tình trạng thai sản (*"cam kết không mang thai"*), hoặc ngoại hình (*"ngoại hình ưa nhìn"*) trừ trường hợp công việc đặc thù được pháp luật cho phép.

### 1.2 Prohibition of Document Retention & Security Deposits (Điều 17)
Người sử dụng lao động tuyệt đối không được thực hiện các hành vi sau khi giao kết, thực hiện hợp đồng lao động (`HR004`):
1. **Giữ bản chính giấy tờ tùy thân, văn bằng, chứng chỉ của người lao động:** Doanh nghiệp chỉ có quyền kiểm tra, đối chiếu bản chính và lưu giữ bản sao có chứng thực hoặc bản chụp.
2. **Yêu cầu người lao động phải thực hiện biện pháp bảo đảm bằng tiền hoặc tài sản khác:** Nghiêm cấm mọi hình thức thu tiền đặt cọc, giữ tiền ký quỹ đi làm, hoặc đe dọa tịch thu tiền cọc nếu nghỉ việc sớm.

---

## 2. Probation Duration & Compensation Floor (Điều 25 & 26)

Hợp đồng thử việc hoặc điều khoản thử việc trong Thư mời nhận việc (Offer Letter) phải tuân thủ nghiêm ngặt hai giới hạn luật định:

### 2.1 Statutory Ceilings on Probation Duration (Điều 25)
Thời gian thử việc do hai bên thỏa thuận căn cứ vào tính chất và mức độ phức tạp của công việc, nhưng **chỉ được thử việc một lần đối với một công việc** và bảo đảm các điều kiện sau:
- **Tối đa 180 ngày:** Đối với công việc của **người quản lý doanh nghiệp** theo quy định của Luật Doanh nghiệp, Luật Quản lý, sử dụng vốn nhà nước đầu tư vào sản xuất, kinh doanh tại doanh nghiệp.
- **Tối đa 60 ngày:** Đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật từ **cao đẳng trở lên** (kỹ sư phần mềm, chuyên viên tài chính, quản lý dự án, thiết kế UI/UX).
- **Tối đa 30 ngày:** Đối với công việc có chức danh nghề nghiệp cần trình độ chuyên môn, kỹ thuật trung cấp, công nhân kỹ thuật, nhân viên nghiệp vụ.
- **Tối đa 06 ngày làm việc:** Đối với các công việc giản đơn khác.
- *Lưu ý vi phạm:* Mọi thỏa thuận thử việc kéo dài 3 tháng (90 ngày) cho nhân viên văn phòng hoặc kỹ sư là hành vi vi phạm pháp luật lao động nghiêm trọng (`HR002`).

### 2.2 Statutory Floor on Probation Salary (Điều 26)
- Tiền lương của người lao động trong thời gian thử việc do hai bên thỏa thuận nhưng **ít nhất phải bằng 85% mức lương chính thức** của công việc đó (`HR002`).
- Nghiêm cấm các điều khoản chi trả 70%, 75% hoặc 80% lương chính thức trong thời gian thử việc.

---

## 3. Offer Letter Drafting Architecture (`offer-letter`)

Thư mời nhận việc (Offer Letter) chuyên nghiệp gửi tới ứng viên (`--register hr-candidate`) phải có cấu trúc chuẩn mực gồm 8 phần thiết yếu:

### 3.1 Cấu trúc chuẩn của một Offer Letter
1. **Tiêu đề văn bản & Lời chào trân trọng:** *"Kính gửi Anh/Chị [Họ và tên Ứng viên]"*
2. **Vị trí chức danh & Bộ phận công tác:** Nêu rõ chức danh công việc, bộ phận trực thuộc và người quản lý trực tiếp.
3. **Thời gian bắt đầu làm việc & Địa điểm:** Ngày nhận việc chính thức, địa chỉ trụ sở làm việc hoặc hình thức làm việc kết hợp (Hybrid/Remote).
4. **Thời gian thử việc & Đánh giá:** Ghi rõ thời hạn thử việc (ví dụ: 60 ngày hoặc 02 tháng, từ ngày ... đến ngày ...).
5. **Chế độ đãi ngộ & Thu nhập:** Nêu rõ mức lương Gross hoặc Net (`HR003`), phụ cấp, thưởng KPI, và chính sách đóng bảo hiểm.
6. **Thời giờ làm việc & Nghỉ ngơi:** Số giờ làm việc tiêu chuẩn (không quá 48 giờ/tuần; đối với văn phòng thường là 40 giờ/tuần từ thứ Hai đến thứ Sáu).
7. **Hồ sơ tiếp nhận nhân sự:** Danh mục giấy tờ sao y công chứng cần nộp trong ngày đầu tiên làm việc.
8. **Thời hạn phản hồi & Xác nhận:** Hạn chót để ứng viên ký tên đồng ý tiếp nhận thư mời.

### 3.2 Gross vs Net Salary Transparency Principle (`HR003`)
- Khi nêu mức lương trong Offer Letter, bắt buộc phải nêu rõ là **Gross (trước thuế và các khoản trích nộp bảo hiểm)** hoặc **Net (thực lĩnh)**:
  - ❌ `Mức lương của anh/chị là 25.000.000 ₫/tháng.`
  - ✅ `Mức lương chính thức: 25.000.000 ₫ Gross/tháng (trước thuế TNCN và 10,5% các khoản bảo hiểm bắt buộc).`
  - ✅ `Mức lương thực lĩnh: 22.000.000 ₫ Net/tháng (Công ty chịu trách nhiệm kê khai và đóng toàn bộ thuế TNCN, BHXH, BHYT, BHTN thay cho nhân viên).`

---

## 4. Unilateral Termination & Notice Periods (Điều 35 & 36)

Quy định thời hạn báo trước khi người lao động hoặc người sử dụng lao động đơn phương chấm dứt hợp đồng lao động:

| Loại hợp đồng lao động | Thời hạn báo trước của NLĐ (Điều 35) | Thời hạn báo trước của NSDLĐ (Điều 36) |
|---|---|---|
| **HĐLĐ không xác định thời hạn** | Ít nhất **45 ngày** | Ít nhất **45 ngày** |
| **HĐLĐ xác định thời hạn (12–36 tháng)** | Ít nhất **30 ngày** | Ít nhất **30 ngày** |
| **HĐLĐ theo mùa vụ hoặc dưới 12 tháng** | Ít nhất **03 ngày làm việc** | Ít nhất **03 ngày làm việc** |
| **Trong thời gian thử việc** | **Báo trước bất kỳ lúc nào**, không cần nêu lý do và không phải bồi thường | **Báo trước bất kỳ lúc nào**, không cần nêu lý do và không phải bồi thường |

---

## 5. Compulsory Social Insurance Framework (Luật BHXH 41/2024/QH15)

Tỷ lệ trích nộp các khoản bảo hiểm bắt buộc trên quỹ tiền lương đóng bảo hiểm của người lao động Việt Nam hiện hành:

1. **Phần người sử dụng lao động (doanh nghiệp) đóng:** Tổng cộng **21,5%**
   - Hưu trí & tử tuất: 14%
   - Ốm đau & thai sản: 3%
   - Tai nạn lao động, bệnh nghề nghiệp (BHTNLĐ-BNN): 0,5%
   - Bảo hiểm y tế (BHYT): 3%
   - Bảo hiểm thất nghiệp (BHTN): 1%
2. **Phần người lao động trích trừ từ lương Gross:** Tổng cộng **10,5%**
   - Hưu trí & tử tuất: 8%
   - Bảo hiểm y tế (BHYT): 1,5%
   - Bảo hiểm thất nghiệp (BHTN): 1%
3. **Kinh phí công đoàn (doanh nghiệp chịu toàn bộ):** **2%** trên quỹ tiền lương đóng BHXH.

---

## 6. Prohibited Disciplinary Measures (Điều 128)

Khi soạn thảo nội quy lao động (`internal-policy`) hoặc văn bản kỷ luật nhân sự, doanh nghiệp tuyệt đối không được quy định các hình thức sau:
1. **Phạt tiền, cắt lương thay việc xử lý kỷ luật lao động (`HR004`):** Hành vi trừ lương 10%, 20% hay 50% vì nhân viên phạm lỗi nghiệp vụ là trái pháp luật.
2. **Xử lý kỷ luật lao động đối với người lao động có hành vi vi phạm không được quy định trong nội quy lao động:** Nội quy phải được đăng ký hợp lệ với cơ quan quản lý nhà nước về lao động cấp tỉnh.
3. **Áp dụng nhiều hình thức kỷ luật lao động cho một hành vi vi phạm:** Khi một người lao động có nhiều hành vi vi phạm kỷ luật cùng một lúc thì chỉ áp dụng hình thức kỷ luật cao nhất tương ứng với hành vi vi phạm nặng nhất.

---

## 7. Working Hours & Overtime Compensation (Điều 98 & Điều 105–107)

Thời giờ làm việc và chế độ tiền lương làm thêm giờ bảo đảm quyền nghỉ ngơi của người lao động:
- **Thời giờ làm việc bình thường:** Không quá 08 giờ trong 01 ngày và không quá 48 giờ trong 01 tuần. Nhà nước khuyến khích doanh nghiệp thực hiện tuần làm việc 40 giờ (5 ngày/tuần).
- **Tiền lương làm thêm giờ (Overtime - OT):**
  - Làm thêm vào ngày làm việc thường: Ít nhất bằng **150%** đơn giá tiền lương hoặc tiền lương thực trả của công việc đang làm.
  - Làm thêm vào ngày nghỉ hằng tuần (thứ Bảy/Chủ nhật): Ít nhất bằng **200%**.
  - Làm thêm vào ngày nghỉ lễ, tết, ngày nghỉ có hưởng lương: Ít nhất bằng **300%** (chưa kể tiền lương ngày lễ, tết đối với người lao động hưởng lương ngày).
- **Làm thêm giờ vào ban đêm (từ 22:00 đến 06:00 sáng hôm sau):** Được trả thêm ít nhất 30% tiền lương của ngày làm việc bình thường và thêm 20% tiền lương làm thêm giờ ban ngày của ngày tương ứng.

---

## 8. Annual Leave & Seniority Entitlements (Điều 113 & 114)

Chế độ nghỉ hằng năm có hưởng lương của người lao động:
1. **Số ngày nghỉ phép năm tiêu chuẩn:**
   - 12 ngày làm việc: Đối với người làm công việc trong điều kiện bình thường.
   - 14 ngày làm việc: Đối với người lao động chưa thành niên, lao động là người khuyết tật, người làm nghề, công việc nặng nhọc, độc hại, nguy hiểm.
   - 16 ngày làm việc: Đối với người làm nghề, công việc đặc biệt nặng nhọc, độc hại, nguy hiểm.
2. **Phép năm thâm niên (Điều 114):** Cứ đủ **05 năm làm việc** cho một người sử dụng lao động thì số ngày nghỉ hằng năm của người lao động được tăng thêm tương ứng **01 ngày**.
3. **Thanh toán tiền phép năm chưa nghỉ:** Trường hợp do thôi việc, mất việc làm mà chưa nghỉ hằng năm hoặc chưa nghỉ hết số ngày nghỉ hằng năm thì được người sử dụng lao động thanh toán tiền lương cho những ngày chưa nghỉ.

---

## 9. Parental Leave & Family Support Protections (Luật BHXH)

- **Lao động nữ sinh con:** Được nghỉ việc hưởng chế độ thai sản trước và sau khi sinh con là **06 tháng** (thời gian nghỉ trước khi sinh không quá 02 tháng).
- **Lao động nam có vợ sinh con:** Được nghỉ việc hưởng chế độ thai sản từ 05 đến 14 ngày làm việc tùy thuộc vào sinh thường, sinh mổ hoặc sinh đôi trở lên trong vòng 30 ngày đầu kể từ ngày vợ sinh con.
