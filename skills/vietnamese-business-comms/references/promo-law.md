<!-- vlc-disable: all -->

# Cẩm Nang Pháp Lý Khuyến Mại, Tiếp Thị & Quảng Cáo Việt Nam

> Căn cứ pháp luật thực định về trần khuyến mại (NĐ 81/2018 & NĐ 128/2024), nghĩa vụ công bố
> của KOL/KOC (Luật 75/2025/QH15), phòng chống thư rác (NĐ 91/2020) và quảng cáo so sánh.

---

## 1. Mức Trần Khuyến Mại & Cơ Chế Giảm Giá Sâu (NĐ 81/2018/NĐ-CP & NĐ 128/2024/NĐ-CP)

Hoạt động xúc tiến thương mại tại Việt Nam chịu sự quản lý chặt chẽ của Bộ Công Thương và Sở Công Thương các tỉnh, thành phố.

<!-- machine-readable: promo-discount-limits -->

| Hình thức xúc tiến | Mức giảm tối đa cho phép | Điều kiện pháp lý bắt buộc | Căn cứ pháp luật |
|---|---|---|---|
| Khuyến mại thương mại thông thường | **Tối đa 50%** giá trị hàng hóa, dịch vụ | Đăng ký hoặc thông báo chương trình khuyến mại với Sở Công Thương | Điều 6 & 7 Nghị định 81/2018/NĐ-CP |
| Chương trình khuyến mại tập trung | **Lên đến 100%** | Do cơ quan nhà nước cấp Trung ương (Bộ Công Thương) hoặc cấp tỉnh (UBND) ban hành quyết định tổ chức | Nghị định 128/2024/NĐ-CP (hiệu lực 01/12/2024) |
| Hàng hóa thực phẩm tươi sống | **Lên đến 100%** | Nhằm giải quyết hàng cận date hoặc tránh hư hỏng nông sản | Khoản 3 Điều 7 Nghị định 81/2018/NĐ-CP |
| Hàng thanh lý do phá sản / giải thể | **Lên đến 100%** | Phải có quyết định giải thể, phá sản hoặc chấm dứt địa điểm kinh doanh | Khoản 4 Điều 7 Nghị định 81/2018/NĐ-CP |

### Quy tắc kiểm duyệt linter (`MKT002`)
Khi copy quảng cáo thể hiện mức giảm giá vượt quá 50% (ví dụ: `giảm giá 70%`, `sale 80%`, `ưu đãi 90%`), người viết bắt buộc phải đính kèm chú thích căn cứ chương trình khuyến mại tập trung theo cú pháp:
```markdown
Ưu đãi siêu hội mua sắm giảm giá lên đến 70% toàn bộ phụ kiện công nghệ
<!-- khuyen-mai-tap-trung: Quyết định số 1820/QĐ-BCT Tháng khuyến mại tập trung quốc gia 2026 -->
```
Nếu không có chú thích này, linter `validate_copy.py` sẽ chặn xuất bản và báo lỗi `MKT002`.

---

## 2. Nghĩa Vụ Công Bố Tài Trợ Đối Với KOL / KOC (Luật 75/2025/QH15)

Luật sửa đổi, bổ sung một số điều của Luật Quảng cáo (Luật số 75/2025/QH15, chính thức có hiệu lực từ ngày **01/01/2026**) bổ sung quy định nghiêm ngặt đối với cá nhân có tầm ảnh hưởng trên mạng xã hội (KOL, KOC, Influencer).

### A. Nghĩa vụ minh bạch thông tin tài trợ (`MKT003`)
1. Bất kỳ bài viết, hình ảnh, video clip, story hoặc phiên phát trực tiếp (livestream) có nhận thù lao, hoa hồng liên kết (affiliate), hoặc tài trợ sản phẩm/dịch vụ từ nhãn hàng **đều phải gắn nhãn công bố rõ ràng**.
2. **Các từ khóa công bố hợp pháp:**
   - `#QuảngCáo`, `#QuangCao`
   - `#Ad`, `#Sponsored`
   - `Nội dung được tài trợ bởi [Tên Thương hiệu]`
   - `Hợp tác cùng [Tên Thương hiệu]`
   - `Sản phẩm do [Tên Thương hiệu] tài trợ`
3. Nhãn công bố phải xuất hiện ở vị trí dễ nhìn thấy nhất (đầu bài viết, đầu phần mô tả video, hoặc ghim cố định trên khung hình livestream), không được giấu sau nút *"Xem thêm"* hoặc dùng font chữ trùng màu nền.

### B. Trách nhiệm kiểm chứng sản phẩm
- Người có ảnh hưởng bắt buộc phải **trực tiếp sử dụng hoặc kiểm chứng thực tế** sản phẩm, dịch vụ trước khi đưa ra nhận xét, đánh giá trên mạng xã hội.
- Không được quảng cáo thực phẩm chức năng, mỹ phẩm, dịch vụ tài chính, bảo hiểm nếu nhãn hàng chưa được cấp Giấy xác nhận nội dung quảng cáo từ Bộ Y tế hoặc cơ quan quản lý chuyên ngành.
- Người có ảnh hưởng chịu trách nhiệm liên đới theo pháp luật nếu truyền bá thông tin sai lệch về tính năng, công dụng sản phẩm.

---

## 3. Quy Định Chống Thư Rác, Tin Nhắn Rác (Nghị Định 91/2020/NĐ-CP)

Nghị định 91/2020/NĐ-CP quy định chi tiết trách nhiệm của doanh nghiệp khi triển khai các chiến dịch tiếp thị qua tin nhắn (SMS, ZNS/ZBS, OTT), thư điện tử (Email) và cuộc gọi viễn thông.

### A. Khung giờ tiếp thị được phép
- **Tin nhắn tiếp thị (SMS / ZBS / OTT):** Chỉ được phép gửi trong khoảng thời gian từ **07:00 đến 22:00** hàng ngày.
- **Cuộc gọi tiếp thị (Telemarketing):** Chỉ được phép gọi trong khoảng thời gian từ **08:00 đến 17:00** hàng ngày.
- Mọi hành vi nhắn tin hoặc gọi điện quảng cáo ngoài khung giờ nêu trên đều cấu thành hành vi vi phạm pháp luật với mức phạt hành chính từ 20 đến 80 triệu đồng.

### B. Giới hạn tần suất tiếp thị (Frequency Capping)
Trừ trường hợp khách hàng có thỏa thuận khác bằng văn bản:
- Tối đa **03 tin nhắn quảng cáo** gửi tới 1 thuê bao trong vòng 24 giờ.
- Tối đa **03 thư điện tử quảng cáo** gửi tới 1 địa chỉ email trong vòng 24 giờ.
- Tối đa **01 cuộc gọi quảng cáo** tới 1 thuê bao trong vòng 24 giờ.

### C. Cơ chế từ chối nhận tin bắt buộc (`SPAM001`)
Mọi thông điệp quảng cáo qua tin nhắn hoặc email bắt buộc phải chứa hướng dẫn từ chối rõ ràng, dễ thao tác và không thu phí của người nhận:
- **SMS / Zalo:** `Soạn TC gửi [Đầu số]` hoặc `De tu choi, soan TC gui [Dau so]`.
- **Email:** Nút hoặc đường link `Hủy nhận tin` (Unsubscribe) đặt ở chân trang với cơ chế 1-click.

### D. Danh sách không quảng cáo quốc gia (DoNotCall List - DNC)
Hệ thống tổng đài và phần mềm tiếp thị tự động phải đồng bộ dữ liệu thời gian thực với Cục An toàn thông tin (Bộ Thông tin và Truyền thông). Nghiêm cấm tuyệt đối mọi hành vi gửi tin nhắn hoặc gọi điện quảng cáo tới các số thuê bao nằm trong danh sách DNC.

---

## 4. Quy Định Về Quảng Cáo So Sánh (Comparative Advertising)

Căn cứ **Điều 45 Luật Cạnh tranh số 23/2018/QH14** và **Điều 8 Khoản 10 Luật Quảng cáo số 16/2012/QH13**:

1. **Hành vi cấm tuyệt đối:** So sánh trực tiếp chất lượng, giá cả, dịch vụ của mình với một đối thủ cạnh tranh cụ thể được nêu đích danh hoặc chỉ rõ dấu hiệu nhận biết nhãn hiệu đối thủ.
2. **Trường hợp so sánh gián tiếp hợp pháp:**
   - So sánh dựa trên kết quả kiểm nghiệm của phòng thí nghiệm độc lập được nhà nước công nhận (ví dụ: *"Tiết kiệm 30% điện năng so với tiêu chuẩn máy lạnh thông thường"*).
   - So sánh với thế hệ sản phẩm trước đó của chính doanh nghiệp mình (ví dụ: *"Tốc độ xử lý nhanh gấp 2 lần so với phiên bản V1"*).
   - Tuyệt đối không dùng các từ ngữ miệt thị, hạ thấp uy tín của các thương hiệu cùng ngành.


---

## 5. Chế Tài Xử Phạt Vi Phạm Hành Chính (Sanctions & Penalties)

Căn cứ **Nghị định 38/2021/NĐ-CP** (xử phạt trong lĩnh vực văn hóa, quảng cáo) và **Nghị định 15/2020/NĐ-CP** (xử phạt trong lĩnh vực bưu chính, viễn thông, tần số vô tuyến điện, công nghệ thông tin):

<!-- machine-readable: promo-penalties -->

| Hành vi vi phạm | Khung tiền phạt (Cá nhân / Doanh nghiệp) | Biện pháp khắc phục hậu quả | Căn cứ điều khoản |
|---|---|---|---|
| Khuyến mại giảm giá vượt quá 50% trái phép | 10.000.000 – 40.000.000 VND | Buộc thu hồi số tiền khuyến mại vượt quy định, tịch thu tang vật | Điều 33 Nghị định 98/2020/NĐ-CP |
| Sử dụng từ ngữ "số 1", "nhất" không có tài liệu chứng minh (`LAW001`) | 10.000.000 – 60.000.000 VND | Buộc tháo dỡ, cải chính thông tin công khai trên phương tiện truyền thông | Điều 34 Nghị định 38/2021/NĐ-CP |
| KOL/KOC không công bố nội dung tài trợ quảng cáo (`MKT003`) | 20.000.000 – 80.000.000 VND | Buộc xóa bỏ bài đăng, tạm đình chỉ hoạt động quảng cáo trên mạng xã hội | Điều 34 Luật 75/2025 & NĐ 38/2021 |
| Gửi tin nhắn quảng cáo ngoài khung giờ 07:00–22:00 | 20.000.000 – 60.000.000 VND | Tạm đình chỉ hoặc thu hồi tên định danh (Brandname) | Điều 94 Nghị định 15/2020/NĐ-CP |
| Gửi tin nhắn quảng cáo không có cơ chế từ chối (`SPAM001`) | 10.000.000 – 40.000.000 VND | Buộc dừng gửi tin nhắn tới danh sách thuê bao vi phạm | Điều 94 Nghị định 15/2020/NĐ-CP |
| Gửi tin nhắn/gọi điện quảng cáo tới số điện thoại trong danh sách DNC | 60.000.000 – 100.000.000 VND | Thu hồi đầu số viễn thông, cấm cấp Brandname mới | Điều 94 Nghị định 15/2020/NĐ-CP |

---

## 6. Danh Mục Kiểm Tra Tuân Thủ Trước Khi Chạy Chiến Dịch (Campaign Pre-Flight Checklist)

1. [ ] **Mức chiết khấu:** Có vượt quá 50% không? Nếu có, đã đính kèm quyết định phê duyệt chương trình khuyến mại tập trung của Sở/Bộ Công Thương chưa?
2. [ ] **Từ ngữ khẳng định:** Có sử dụng các từ "số 1", "nhất", "hàng đầu", "duy nhất" không? Đã lưu trữ chứng nhận Euromonitor/Nielsen/Bộ ngành trong hồ sơ chiến dịch chưa?
3. [ ] **Hợp đồng KOL/KOC:** Đã ràng buộc điều khoản bắt buộc gắn hashtag `#QuảngCáo` hoặc nhãn tài trợ chưa? KOL đã trực tiếp trải nghiệm sản phẩm chưa?
4. [ ] **Cấu hình thời gian gửi:** Hệ thống tự động gửi tin nhắn/email đã cài đặt chặn ngoài khung giờ 07:00–22:00 chưa?
5. [ ] **Cú pháp từ chối (Opt-Out):** Toàn bộ SMS/ZBS/Email đã có câu hướng dẫn từ chối nhận tin rõ ràng ở cuối thông điệp chưa?

6. [ ] **Đồng bộ danh sách DNC:** Cơ sở dữ liệu khách hàng mục tiêu đã được lọc loại trừ toàn bộ thuê bao thuộc Danh sách Không quảng cáo Quốc gia trong vòng 24 giờ qua chưa?
7. [ ] **Quảng cáo so sánh:** Copy chiến dịch có nhắc tên nhãn hiệu của đối thủ cạnh tranh không? Đã loại bỏ mọi hình thức so sánh trực tiếp mang tính công kích chưa?
