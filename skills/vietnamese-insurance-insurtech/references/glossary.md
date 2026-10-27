<!-- vlc-disable: all -->

# Vietnamese Insurance & InsurTech Terminology Glossary (`vietnamese-insurance-insurtech`)

This glossary provides standardized Vietnamese insurance, actuarial, InsurTech digital product, and bancassurance terminology under the Law on Insurance Business 2022 (Luật Kinh doanh bảo hiểm số 08/2022/QH15) and Ministry of Finance Circular 67/2023/TT-BTC.

The table below is parsed by `validate_copy.py` at runtime; each row acts as an active linting rule firing `CAL001` with the declared severity.

---

## 1. Machine-Readable Insurance, Actuarial & InsurTech Terms

<!-- machine-readable: glossary -->

| English / Source | ❌ Dịch sai / Cũ | ✅ Thuật ngữ chuẩn | Ghi chú | Severity |
|---|---|---|---|---|
| insurance policy | `chính sách bảo hiểm` | `hợp đồng bảo hiểm` / `quy tắc và điều khoản bảo hiểm` | Thuật ngữ luật định bắt buộc theo Điều 4 & Điều 15 Luật KDBH 2022 | error |
| life policy | `chính sách bảo hiểm nhân thọ` | `hợp đồng bảo hiểm nhân thọ` | Định danh hợp đồng bảo hiểm con người theo Điều 4 | error |
| policyholder | `người giữ chính sách` | `bên mua bảo hiểm` | Chủ thể giao kết hợp đồng và đóng phí bảo hiểm Điều 4 | error |
| insured person | `người được bảo đảm` | `người được bảo hiểm` | Người có tính mạng, sức khỏe, tài sản được bảo hiểm | error |
| beneficiary | `người nhận tiền thưởng` | `người thụ hưởng` | Người được chỉ định nhận tiền bồi thường Điều 4 | error |
| insurance coverage | `câu chuyện bảo hiểm` | `phạm vi bảo hiểm` / `quyền lợi bảo hiểm` | Điều 16 Luật Kinh doanh bảo hiểm 2022 | error |
| insurance coverage | `độ bao phủ bảo hiểm` | `phạm vi bảo hiểm` | Tránh dùng calque 'độ bao phủ' trong hợp đồng | warn |
| insurance premium | `tiền thưởng bảo hiểm` | `phí bảo hiểm` / `phí bảo hiểm định kỳ` | Khoản tiền bên mua phải đóng cho DNBH Điều 4 | error |
| act of God | `sự kiện thiên Chúa` | `sự kiện bất khả kháng` / `thiên tai` | Bộ luật Dân sự 2015 & Luật KDBH 2022 | error |
| free-look period | `thời gian nhìn miễn phí` | `thời gian cân nhắc tham gia bảo hiểm` | 21 ngày theo Điều 35 Luật KDBH 2022 | error |
| free-look period | `thời gian dùng thử bảo hiểm` | `thời gian cân nhắc tham gia bảo hiểm` | Bảo hiểm không có chế định 'dùng thử' thương mại | error |
| claim payout / settlement | `chi trả khiếu nại` | `giải quyết bồi thường` / `chi trả quyền lợi bảo hiểm` | Điều 31 Luật Kinh doanh bảo hiểm 2022 | error |
| claim settlement | `giải quyết yêu sách` | `giải quyết bồi thường bảo hiểm` | Dịch thô chữ claim/settlement | error |
| cash value / surrender value | `giá trị tiền mặt sẵn có` | `giá trị hoàn lại` | Khoản tiền bên mua nhận lại khi chấm dứt HĐ trước hạn Điều 4 | error |
| exclusion clause | `khoản loại bỏ` | `điều khoản loại trừ trách nhiệm bảo hiểm` | Điều 19 Luật Kinh doanh bảo hiểm 2022 | error |
| exclusion clause | `điều khoản miễn trừ toàn bộ` | `điều khoản loại trừ trách nhiệm bảo hiểm` | Điều 19 Luật Kinh doanh bảo hiểm 2022 | warn |
| underwriting | `viết dưới bảo hiểm` | `thẩm định bảo hiểm` / `đánh giá rủi ro bảo hiểm` | Nghiệp vụ thẩm định điều kiện phát hành hợp đồng | error |
| underwriting | `ký dưới bảo hiểm` | `thẩm định phát hành hợp đồng bảo hiểm` | Nghiệp vụ thẩm định hồ sơ yêu cầu bảo hiểm | error |
| sum insured / face amount | `số tiền đã bảo hiểm` | `số tiền bảo hiểm` | Số tiền DNBH cam kết chi trả theo thỏa thuận Điều 4 | error |
| grace period | `giai đoạn duyên dáng` | `thời gian gia hạn đóng phí bảo hiểm` | Thời gian 60 ngày đóng phí bổ sung Điều 37 | error |
| deductible / excess | `tiền khấu trừ tự nguyện cắt bỏ` | `mức khấu trừ` / `mức miễn bồi thường có khấu trừ` | Áp dụng trong bảo hiểm thiệt hại phi nhân thọ | warn |
| supplementary rider | `người cưỡi bổ sung` | `sản phẩm bảo hiểm bổ trợ` / `quyền lợi bổ trợ` | Quyền lợi tăng cường gắn liền hợp đồng chính | error |
| universal life | `bảo hiểm cuộc sống phổ quát` | `bảo hiểm liên kết chung` | Dòng sản phẩm theo Thông tư 67/2023/TT-BTC | error |
| unit-linked insurance | `bảo hiểm liên kết đơn vị tiền` | `bảo hiểm liên kết đơn vị` | Dòng sản phẩm đầu tư rủi ro theo TT 67/2023/TT-BTC | error |
| investment-linked insurance | `tiết kiệm đầu tư cam kết` | `bảo hiểm liên kết đầu tư` | Cấm mạo danh tiền gửi tiết kiệm theo TT 67/2023/TT-BTC | error |
| annuity | `khoản niên kim hàng năm tự do` | `bảo hiểm hưu trí` / `bảo hiểm niên kim` | Nghiệp vụ bảo hiểm nhân thọ Điều 7 | warn |
| reinsurance | `bảo hiểm lại từ đầu` | `tái bảo hiểm` | Hoạt động phân tán rủi ro giữa các DNBH Điều 4 | error |
| insurable interest | `lợi ích có thể bảo hiểm được` | `quyền lợi có thể được bảo hiểm` | Điều kiện bắt buộc khi giao kết hợp đồng Điều 4 & 34 | warn |
| co-insurance | `đồng bảo hiểm chia đôi` | `đồng bảo hiểm` | Các DNBH cùng nhận bảo hiểm cho một đối tượng | warn |
| subrogation | `thế quyền thay thế chủ` | `chuyển quyền yêu cầu bồi hoàn` / `thế quyền` | Quyền đòi bên thứ ba bồi hoàn Điều 38 | warn |
| lapsed policy | `chính sách bị mất hiệu lực` | `hợp đồng bảo hiểm mất hiệu lực` | Do không đóng phí quá thời gian gia hạn | error |
| bancassurance | `bán chéo ép buộc bảo hiểm` | `phân phối bảo hiểm qua ngân hàng` / `bancassurance` | Kênh phân phối đại lý bảo hiểm qua tổ chức tín dụng | error |
