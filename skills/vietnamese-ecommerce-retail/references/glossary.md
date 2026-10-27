<!-- vlc-disable: all -->

# E-Commerce, Retail & Logistics Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese e-commerce, digital retail, fulfillment lifecycle, and multi-channel logistics terminology.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable E-Commerce, Retail & Logistics Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| out for delivery | `ra ngoài để giao hàng` | `đang giao hàng` | Trạng thái bưu tá đang đi phát kiện hàng | error |
| order fulfillment | `sự hoàn thành đơn hàng` | `xử lý đơn hàng` / `hoàn tất đơn hàng` | Quy trình tiếp nhận, đóng gói và xử lý đơn | error |
| add to cart | `thêm vào xe đẩy` / `bỏ vào giỏ xe` | `thêm vào giỏ hàng` | Nút hành động chuẩn trên sàn TMĐT | error |
| cash on delivery (COD) | `tiền mặt trên giao hàng` | `thanh toán khi nhận hàng (COD)` | Hình thức thanh toán trực tiếp cho bưu tá | error |
| return policy | `chính sách trở lại` | `chính sách đổi trả` / `chính sách hoàn trả` | Quy định đổi trả hàng per Luật BVQLNTD 2023 | error |
| last-mile carrier | `người vận chuyển cuối cùng` | `đơn vị vận chuyển chặng cuối` | Doanh nghiệp logistics giao chặng cuối | error |
| estimated delivery time (EDT) | `thời gian giao hàng ước tính` | `dự kiến giao hàng` / `thời gian giao dự kiến` | Thời gian dự kiến kiện hàng đến nơi | warn |
| buy now, pay later (BNPL) | `mua bây giờ, trả sau này` | `mua trước trả sau (BNPL)` | Dịch vụ tín dụng tiêu dùng số | error |
| flash sale | `bán hàng đèn flash` | `khuyến mại chớp nhoáng` / `flash sale` | Chương trình giảm giá có giới hạn thời gian | warn |
| stock keeping unit (SKU) | `đơn vị giữ cổ phiếu` | `mã phân loại hàng hóa (SKU)` / `mã sản phẩm` | Mã quản lý hàng tồn kho | error |
| drop-shipping | `thả hàng vận chuyển` | `bán hàng bỏ qua khâu vận chuyển (dropshipping)` | Mô hình chuyển giao đơn hàng trực tiếp | warn |
| payment gateway | `cổng vào thanh toán` | `cổng thanh toán trực tuyến` | Hạ tầng trung gian thanh toán ngân hàng | warn |
| cart abandonment | `từ bỏ xe đẩy mua sắm` | `bỏ quên giỏ hàng` | Tỷ lệ khách hàng không hoàn tất thanh toán | warn |
| cross-border e-commerce | `thương mại điện tử qua biên giới` | `thương mại điện tử xuyên biên giới` | Hoạt động xuất nhập khẩu trực tuyến | warn |
| consumer protection | `bảo vệ khách hàng ăn uống` | `bảo vệ quyền lợi người tiêu dùng` | Luật Bảo vệ quyền lợi người tiêu dùng 2023 | error |
| co-inspection / unboxing inspection | `kiểm tra mở hộp chung` | `đồng kiểm khi nhận hàng` | Quyền kiểm tra ngoại quan gói hàng | error |
| electronic VAT invoice | `hóa đơn đỏ giá trị` | `hóa đơn điện tử (hóa đơn VAT)` | Nghị định 123/2020/NĐ-CP | warn |
| country of origin | `gốc rễ sản phẩm` | `xuất xứ hàng hóa` / `xuất xứ` | Nghị định 43/2017/NĐ-CP về nhãn hàng hóa | error |
| return merchandise authorization (RMA) | `giấy ủy quyền hàng hóa trả lại` | `mã xác nhận trả hàng` / `yêu cầu đổi trả` | Quy trình quản lý hàng trả lại | warn |
| supply chain logistics | `chuỗi dây xích cung ứng` | `chuỗi cung ứng` / `dịch vụ logistics` | Quản trị vận hành chuỗi cung ứng | error |
| warehouse inventory check | `kiểm kê nhà kho chứa hàng` | `kiểm kê hàng tồn kho` | Hoạt động đối soát kho hàng | warn |
| omnichannel commerce | `bán lẻ tất cả các kênh` | `bán lẻ đa kênh (omnichannel)` | Trải nghiệm mua sắm liền mạch | warn |
| customer lifetime value (CLV) | `giá trị cuộc đời khách hàng` | `giá trị vòng đời khách hàng` | Chỉ số phân tích khách hàng | warn |
| affiliate marketing | `tiếp thị liên kết chi nhánh` | `tiếp thị liên kết (affiliate)` | Kênh tiếp thị hoa hồng | warn |
| product detail page (PDP) | `trang giấy chi tiết vật phẩm` | `trang chi tiết sản phẩm (PDP)` | Giao diện hiển thị thông tin sản phẩm | error |
| order tracking | `theo vết dấu vết đơn hàng` | `tra cứu đơn hàng` / `theo dõi vận đơn` | Chức năng kiểm tra hành trình đơn hàng | warn |
| point of sale (POS) | `điểm bán hàng kết thúc` | `hệ thống điểm bán lẻ (POS)` | Thiết bị / phần mềm thanh toán tại quầy | warn |
| counterfeit goods | `hàng giả mạo lừa đảo` | `hàng giả` / `hàng xâm phạm quyền sở hữu trí tuệ` | Hàng hóa vi phạm pháp luật | error |
| loyalty rewards program | `chương trình lòng trung thành` | `chương trình khách hàng thân thiết` | Chính sách tích điểm đổi quà | warn |
| freight forwarder | `người chuyển tiếp cước phí` | `đơn vị giao nhận vận tải` / `công ty forwarder` | Doanh nghiệp logistics giao nhận hàng | warn |

---

## 2. Terminology Guidelines & Statutory References

1. **Nghị định 52/2013/NĐ-CP & Nghị định 85/2021/NĐ-CP:**
   - Phân biệt tuyệt đối giữa thủ tục "Thông báo" (website bán hàng của chính thương nhân) và thủ tục "Đăng ký" (sàn TMĐT cho bên thứ ba mở gian hàng).
   - Biểu tượng của Bộ Công Thương là căn cứ xác thực về mặt quản lý nhà nước về hoạt động TMĐT, không phải chứng chỉ chất lượng sản phẩm hay chứng nhận hàng chính hãng 100%.
2. **Nghị định 81/2018/NĐ-CP & Nghị định 128/2024/NĐ-CP:**
   - Khống chế trần giảm giá khuyến mại không vượt quá 50% giá bán trước đó, trừ các chương trình khuyến mại tập trung quốc gia do cơ quan nhà nước tổ chức.
   - Nghiêm cấm nâng giá niêm yết rồi quảng cáo giảm giá sâu (giá neo ảo lừa dối người tiêu dùng).
3. **Luật Bảo vệ quyền lợi người tiêu dùng 2023 (số 19/2023/QH15):**
   - Vô hiệu hoàn toàn điều khoản "Hàng mua rồi miễn đổi trả trong mọi trường hợp" (Điều 25).
   - Nghiêm cấm dark pattern, đe dọa người tiêu dùng hoặc tạo cảm giác tội lỗi giả tạo (Điều 10).
4. **Nghị định 43/2017/NĐ-CP & Nghị định 111/2021/NĐ-CP:**
   - Trang chi tiết sản phẩm (PDP) bắt buộc hiển thị nhãn hàng hóa tiếng Việt: Tên hàng hóa, Tên và địa chỉ thương nhân chịu trách nhiệm, Xuất xứ hàng hóa.
