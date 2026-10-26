<!-- vlc-disable: all -->
# Worked Diagnostic Pairs — `vietnamese-ecommerce-retail`

> Auto-generated from `evals/vietnamese-ecommerce-retail/pairs.jsonl` (25 verified pairs). Each pair contrasts a real LLM defect (❌) with the production Vietnamese fix (✅) and names the rule IDs it satisfies.

## Moit Badge

### ecom-badge-conflation-01 (Rules: `ECOM001`)

```diff
- Sàn giao dịch thương mại điện tử chỉ cần gắn logo Đã thông báo Bộ Công Thương là đủ điều kiện vận hành hợp pháp.
+ Sàn giao dịch thương mại điện tử phải hoàn tất thủ tục đăng ký và gắn logo Đã đăng ký Bộ Công Thương theo quy định pháp luật.
```

### ecom-badge-quality-01 (Rules: `ECOM001`)

```diff
- Toàn bộ mỹ phẩm bán trên website được Bộ Công Thương bảo chứng chất lượng 100% về độ an toàn.
+ Toàn bộ mỹ phẩm bán trên website có đầy đủ phiếu công bố sản phẩm và hóa đơn chứng từ hợp pháp.
```

### ecom-badge-quality-02 (Rules: `ECOM001`)

```diff
- Cửa hàng cam kết mọi đơn hàng đều có logo Bộ Công Thương chứng nhận hàng chính hãng tuyệt đối.
+ Cửa hàng cam kết cung cấp sản phẩm chính hãng với tem phụ tiếng Việt và hóa đơn VAT đầy đủ.
```

### ecom-badge-quality-03 (Rules: `ECOM001`)

```diff
- Khách hàng an tâm mua sắm vì sản phẩm đã được chứng nhận hàng chính hãng bởi Bộ Công Thương.
+ Khách hàng an tâm mua sắm vì sản phẩm được phân phối chính thức từ nhà sản xuất uy tín.
```

## Promotions

### ecom-discount-cap-01 (Rules: `ECOM002`)

```diff
- Chương trình sale sập sàn 80% áp dụng cho toàn bộ bộ sưu tập thời trang mùa thu.
+ Chương trình giảm giá 50% áp dụng cho toàn bộ bộ sưu tập thời trang mùa thu.
```

### ecom-discount-cap-02 (Rules: `ECOM002`)

```diff
- Khuyến mại 70% giá trị mọi sản phẩm gia dụng trong dịp cuối tuần này.
+ Khuyến mại 50% giá trị mọi sản phẩm gia dụng trong dịp cuối tuần này.
```

### ecom-discount-cap-03 (Rules: `ECOM002`)

```diff
- Cửa hàng áp dụng mức giảm giá 90% cho phụ kiện điện thoại khi mua kèm máy tính bảng.
+ Cửa hàng áp dụng mức giảm giá 90% trong Tháng khuyến mại tập trung quốc gia được cơ quan nhà nước phê duyệt.
```

### ecom-fake-anchor-01 (Rules: `ECOM002`)

```diff
- Gian hàng thực hiện chiêu trò nâng khống giá gốc để giảm giá ảo nhằm thu hút người mua.
+ Gian hàng niêm yết giá bán trung thực và giảm giá thực tế dựa trên giá bán công bố trước đó.
```

## Consumer Rights

### ecom-no-return-01 (Rules: `ECOM003`)

```diff
- Quy định của cửa hàng: hàng mua rồi miễn đổi trả trong mọi trường hợp kể cả lỗi kỹ thuật.
+ Khách hàng được quyền đổi trả sản phẩm miễn phí trong vòng 7 ngày nếu phát hiện lỗi từ nhà sản xuất.
```

### ecom-no-return-02 (Rules: `ECOM003`)

```diff
- Chúng tôi không áp dụng đổi trả với bất kỳ lý do gì kể cả lỗi nhà sản xuất.
+ Chúng tôi hỗ trợ đổi hàng mới hoặc hoàn tiền đầy đủ nếu sản phẩm có lỗi từ nhà sản xuất.
```

### ecom-no-return-03 (Rules: `ECOM003`)

```diff
- Đơn vị vận chuyển cấm đồng kiểm và từ chối hoàn tiền dưới mọi hình thức khi giao hàng.
+ Người mua có quyền đồng kiểm ngoại quan gói hàng và yêu cầu hoàn tiền nếu sản phẩm bị hư hỏng.
```

### ecom-no-return-04 (Rules: `ECOM003`)

```diff
- Cửa hàng từ chối hoàn tiền dưới mọi hình thức sau khi khách hàng đã thanh toán.
+ Cửa hàng thực hiện hoàn tiền vào tài khoản ngân hàng trong vòng 48 giờ đối với đơn hàng hoàn trả hợp lệ.
```

## Product Labeling

### ecom-pdp-label-01 (Rules: `ECOM004` · Doctype: `product-pdp`)

```diff
- Áo sơ mi nam công sở cao cấp chất liệu cotton thoáng mát, giá bán 450.000 ₫ mỗi chiếc.
+ Áo sơ mi nam công sở cotton. Xuất xứ: Việt Nam. Thương nhân chịu trách nhiệm: Công ty Dệt May An Phát.
```

### ecom-pdp-label-02 (Rules: `ECOM004` · Doctype: `product-pdp`)

```diff
- Bộ nồi inox 5 đáy dùng cho mọi loại bếp, tặng kèm muôi canh inox cao cấp khi mua hôm nay.
+ Bộ nồi inox 5 đáy. Nơi sản xuất: Thái Lan. Nhà phân phối: Công ty Gia Dụng Toàn Cầu.
```

### ecom-pdp-label-03 (Rules: `ECOM004` · Doctype: `product-pdp`)

```diff
- Bàn chải đánh răng điện công nghệ sóng âm, pin sạc không dây tiện lợi khi đi du lịch.
+ Bàn chải điện sóng âm. Nguồn gốc: Nhật Bản. Đơn vị nhập khẩu: Công ty Cổ phần Thiết Bị Y Tế Á Châu.
```

### ecom-pdp-label-04 (Rules: `ECOM004` · Doctype: `product-pdp`)

```diff
- Tai nghe không dây chống ồn chủ động với thời lượng pin 30 giờ và âm thanh chuẩn studio.
+ Tai nghe không dây. Sản xuất tại: Việt Nam. Nhà sản xuất: Công ty TNHH Điện Tử Nam Việt.
```

## Calque

### ecom-calque-delivery-01 (Rules: `ECOM005`)

```diff
- Kiện hàng của quý khách hiện đang ra ngoài để giao hàng tại khu vực quận 1.
+ Kiện hàng của quý khách hiện đang giao hàng tại khu vực quận 1.
```

### ecom-calque-cart-01 (Rules: `ECOM005`)

```diff
- Vui lòng nhấn nút thêm vào xe đẩy để lưu trữ sản phẩm cần thanh toán.
+ Vui lòng nhấn nút thêm vào giỏ hàng để lưu trữ sản phẩm cần thanh toán.
```

### ecom-calque-cod-01 (Rules: `ECOM005`)

```diff
- Khách hàng có thể chọn phương thức tiền mặt trên giao hàng khi nhận kiện bưu phẩm.
+ Khách hàng có thể chọn phương thức thanh toán khi nhận hàng (COD) khi nhận kiện bưu phẩm.
```

### ecom-calque-policy-01 (Rules: `ECOM005`)

```diff
- Quý khách vui lòng tham khảo chính sách trở lại để biết thêm chi tiết về thủ tục đổi hàng.
+ Quý khách vui lòng tham khảo chính sách đổi trả để biết thêm chi tiết về thủ tục đổi hàng.
```

## Dark Pattern

### ecom-dark-pattern-01 (Rules: `ECOM006`)

```diff
- Nhân viên sẽ bị trừ lương nếu quý khách hủy đơn hàng sau khi bưu tá đã xuất kho.
+ Quý khách có thể hủy đơn hàng miễn phí trước khi kiện hàng được bàn giao cho đơn vị vận chuyển.
```

### ecom-dark-pattern-02 (Rules: `ECOM006`)

```diff
- Hệ thống tự động khóa tài khoản vĩnh viễn nếu không thanh toán trong 5 phút nữa.
+ Đơn hàng chưa thanh toán sẽ tự động hết hạn sau 24 giờ để hoàn trả sản phẩm về kho.
```

### ecom-dark-pattern-03 (Rules: `ECOM006`)

```diff
- Ứng dụng tự động đăng ký gói hội viên trả phí gia hạn ngầm không cần đồng ý của người dùng.
+ Ứng dụng chỉ kích hoạt gói hội viên trả phí khi khách hàng chủ động xác nhận đồng ý đăng ký.
```

## Superlative

### ecom-superlative-01 (Rules: `LAW001`)

```diff
- Nền tảng mua sắm trực tuyến số 1 Việt Nam với dịch vụ giao hàng nhanh nhất cả nước.
+ Nền tảng mua sắm trực tuyến đa ngành với mạng lưới giao hàng phủ sóng toàn quốc.
```

## Typography Currency

### ecom-currency-thousands-01 (Rules: `NUM001`)

```diff
- Giá ưu đãi đặc biệt cho thành viên mới chỉ 350,000 ₫ kèm mã miễn phí vận chuyển.
+ Giá ưu đãi đặc biệt cho thành viên mới chỉ 350.000 ₫ kèm mã miễn phí vận chuyển.
```
