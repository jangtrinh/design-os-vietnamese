<!-- vlc-disable: all -->

# Banned & Regulated Phrases in E-Commerce & Retail (`design-os-vietnamese`)

In Vietnamese e-commerce storefronts, digital retail campaigns, product description pages (PDP), and fulfillment communications, unlawful claims, deceptive discount promotions, and checkout dark patterns carry severe statutory penalties under Decree 52/2013/NĐ-CP, Decree 85/2021/NĐ-CP, Decree 81/2018/NĐ-CP, Decree 128/2024/NĐ-CP, and the Law on Protection of Consumers' Rights 2023.

---

## 1. Regulated Superlatives & Absolute Representations (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, using superlatives without valid documentary certification from a competent state agency or accredited independent authority is strictly prohibited.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:rẻ\|ưu\s+đãi\|hấp\s+dẫn\|tiết\s+kiệm\|uy\s+tín\|chất\s+lượng\|nhanh)\s+nhất` | "cheapest / most attractive / best saving / most reputable" | Common violation in online storefront promotions |
| `duy\s+nhất` | "the only" | Specifically named in statute |
| `số\s*(?:một\|1)\b` | "number one / No. 1" | Regulated ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Regulated ranking symbol |
| `\bno\.?\s*1\b` | "No. 1" | Regulated ranking text |
| `hàng\s+đầu` | "leading / top" | Prohibited ranking claim without award verification |
| `đứng\s+đầu` | "ranks first" | Prohibited market rank claim |
| `cam\s+kết\s+rẻ\s+nhất\s+thị\s+trường` | "guaranteed cheapest on the market" | Unverified superlative price claim |
| `giá\s+rẻ\s+vô\s+địch` | "unbeatable cheap price" | Hyperbolic marketing superlative |
| `sàn\s+thương\s+mại\s+điện\s+tử\s+số\s*1` | "number 1 e-commerce marketplace" | Prohibited ranking slogan |
| `chính\s+hãng\s+100\s*%` | "authentic 100%" | Absolute guarantee claim requiring certificate |
| `ưu\s+đãi\s+lớn\s+nhất\s+lịch\s+sử` | "biggest discount in history" | Exaggerated unverified claim |

---

## 2. Prohibited Statements, Checkout Coercion & Calques (`ECOM001`–`ECOM006`)

The following phrases are prohibited across online storefronts, flash sale landing pages, checkout funnels, and return policies:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale | Severity |
|---|---|---|---|
| `bộ công thương bảo chứng chất lượng 100%` | `website đã hoàn tất thủ tục thông báo/đăng ký với Bộ Công Thương` | Nghị định 52/2013 & NĐ 85/2021 cấm nhận vơ logo BCT kiểm định chất lượng | error |
| `logo bộ công thương chứng nhận hàng chính hãng tuyệt đối` | `thương nhân đã đăng ký hoạt động thương mại điện tử với Bộ Công Thương` | Thủ tục BCT là quản lý điều kiện hoạt động, không phải chứng chỉ chất lượng | error |
| `bộ công thương chứng nhận hàng chính hãng` | `sản phẩm có đầy đủ hóa đơn chứng từ và tem phụ chứng minh nguồn gốc` | Sai bản chất thủ tục thông báo/đăng ký website TMĐT | error |
| `bộ công thương cam kết chất lượng` | `người bán cam kết chịu trách nhiệm về chất lượng hàng hóa per pháp luật` | BCT không bảo đảm thay cho người bán | error |
| `hàng mua rồi miễn đổi trả trong mọi trường hợp` | `hỗ trợ đổi trả trong vòng 7 ngày đối với sản phẩm có lỗi từ nhà sản xuất` | Điều 25 Luật Bảo vệ quyền lợi người tiêu dùng 2023 vô hiệu điều khoản này | error |
| `từ chối giải quyết đổi trả dưới mọi hình thức` | `chính sách đổi trả minh bạch theo quy định pháp luật bảo vệ người tiêu dùng` | Tước đoạt quyền lợi người tiêu dùng là điều khoản vô hiệu | error |
| `miễn đổi trả hàng dưới mọi lý do` | `chính sách đổi trả áp dụng theo quy chế hoạt động của sàn TMĐT` | Vi phạm Điều 25 Luật BVQLNTD 2023 | error |
| `nhân viên giao hàng sẽ bị trừ lương nếu bạn hủy đơn` | `quý khách vui lòng kiểm tra kỹ đơn hàng trước khi bấm đặt hàng` | Dark pattern đe dọa cưỡng ép cảm xúc per Điều 10 Luật BVQLNTD 2023 | error |
| `shipper phải đền tiền nếu đơn hàng bị từ chối` | `quý khách có quyền kiểm tra ngoại quan gói hàng trước khi nhận` | Thủ thuật tâm lý cưỡng ép vi phạm chuẩn mực kinh doanh | error |
| `tự động khóa tài khoản vĩnh viễn nếu quý khách không thanh toán trong 5 phút` | `đơn hàng chưa thanh toán sẽ tự động hoàn về giỏ sau thời gian quy định` | Đe dọa thao túng thanh toán vô lý | error |
| `tự động khóa tài khoản vĩnh viễn nếu không thanh toán trong 5 phút` | `đơn hàng sẽ tự động hủy nếu quá hạn thanh toán 15 phút` | Cưỡng ép thanh toán vi phạm quyền tự chủ giao dịch | error |
| `giảm giá 70% toàn bộ sản phẩm` | `giảm giá tối đa 50% hoặc tham gia Tháng khuyến mại tập trung quốc gia` | Nghị định 81/2018 & NĐ 128/2024 khống chế trần giảm giá 50% | error |
| `giảm giá 80% toàn bộ sản phẩm` | `khuyến mại đến 50% theo quy định pháp luật thương mại` | Vượt hạn mức khuyến mại tối đa 50% | error |
| `ra ngoài để giao hàng` | `đang giao hàng` | Calque dịch máy thô từ out for delivery | error |
| `sự hoàn thành đơn hàng` | `hoàn tất đơn hàng` / `xử lý đơn hàng` | Calque dịch máy thô từ order fulfillment | error |
| `thêm vào xe đẩy` | `thêm vào giỏ hàng` | Calque dịch máy thô từ add to cart | error |
| `bỏ vào giỏ xe` | `thêm vào giỏ hàng` | Calque dịch máy thô | error |
| `tiền mặt trên giao hàng` | `thanh toán khi nhận hàng (COD)` | Calque dịch máy thô từ cash on delivery | error |
| `chính sách trở lại` | `chính sách đổi trả` | Calque dịch máy thô từ return policy | error |
| `người vận chuyển cuối cùng` | `đơn vị vận chuyển chặng cuối` | Calque dịch máy thô từ last-mile carrier | error |

---

## 3. Mandatory Statutory Storefront Disclosures

1. **Công bố thông tin chủ sở hữu website (Nghị định 52/2013/NĐ-CP Điều 29):**
   - Tên thương nhân, tổ chức hoặc cá nhân sở hữu website.
   - Địa chỉ trụ sở, số điện thoại liên hệ, địa chỉ email.
   - Số Giấy chứng nhận đăng ký kinh doanh hoặc Mã số doanh nghiệp.
2. **Công khai chính sách giao dịch chung:**
   - Chính sách vận chuyển và giao nhận, chính sách bảo hành, chính sách đổi trả hàng hóa, chính sách bảo vệ thông tin cá nhân của người tiêu dùng.
