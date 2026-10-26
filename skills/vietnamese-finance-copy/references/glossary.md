<!-- vlc-disable: all -->

# Financial & Accounting Glossary (`design-os-vietnamese`)

This glossary provides standardized Vietnamese finance, accounting, banking, tax, and FinTech terminology.
The first table is parsed by `validate_copy.py` at runtime; every row acts as a linting rule firing `CAL001` with the declared severity.

## 1. Machine-Readable Accounting, Tax, & Banking Terms

<!-- machine-readable: glossary -->

| EN | ❌ Wrong or stale | ✅ Correct | Severity |
|---|---|---|---|
| balance sheet | `Bảng cân đối kế toán` | `Báo cáo tình hình tài chính` | error |
| personal income tax | `thuế thu nhập cá nhân (PIT)` | `thuế TNCN` | warn |
| corporate income tax | `thuế thu nhập doanh nghiệp (CIT)` | `thuế TNDN` | warn |
| value added tax | `thuế giá trị gia tăng (VAT)` | `thuế GTGT` | warn |
| tax identification number | `mã số thuế (TIN)` | `mã số thuế (MST)` | warn |
| deposit (bank) | `tiền ký gửi` | `tiền gửi` | error |
| deposit (sales / escrow) | `tiền gửi đặt trước` | `đặt cọc` | error |
| revenue | `thu nhập bán hàng` | `doanh thu` | error |
| net profit | `lợi nhuận ròng sạch` | `lợi nhuận sau thuế` | error |
| gross profit | `lợi nhuận thô ráp` | `lợi nhuận gộp` | error |
| cash flow | `dòng chảy tiền mặt` | `lưu chuyển tiền tệ` | error |
| accounts receivable | `tài khoản phải thu` | `phải thu khách hàng` | error |
| accounts payable | `tài khoản phải trả` | `phải trả người bán` | error |
| retained earnings | `thu nhập giữ lại` | `lợi nhuận sau thuế chưa phân phối` | error |
| equity | `sự công bằng` | `vốn chủ sở hữu` | error |
| interest rate | `tỷ lệ quan tâm` | `lãi suất` | error |
| principal (loan) | `hiệu trưởng` | `tiền gốc` | error |
| security (financial) | `sự an toàn` | `chứng khoán` | error |
| bond | `trái phiếu liên kết` | `trái phiếu` | warn |
| return on investment | `sự trở lại của đầu tư` | `tỷ suất lợi nhuận / tỷ suất sinh lời` | error |
| fiscal year | `năm tài khóa tài chính` | `năm tài chính` | warn |
| audit | `kiểm tra sổ sách` | `kiểm toán` | error |
| invoice | `phiếu tính tiền` | `hóa đơn` | error |
| bank statement | `tuyên bố ngân hàng` | `sao kê tài khoản` | error |
| overdue | `quá thời hạn cuối` | `quá hạn` | warn |
| collateral | `tài sản bảo lãnh` | `tài sản bảo đảm` | error |
| maturity date | `ngày hết hạn vay` | `ngày đáo hạn` | error |
| installment payment | `trả dần` | `trả góp` | warn |
| credit limit | `giới hạn tín dụng` | `hạn mức tín dụng` | error |
| disbursement | `phân phối tiền` | `giải ngân` | error |
| amortisation | `sự trừ dần` | `khấu hao vô hình / phân bổ chi phí` | error |
| depreciation | `giảm giá trị` | `khấu hao tài sản cố định` | error |
| current assets | `tài sản hiện tại` | `tài sản ngắn hạn` | error |
| non-current assets | `tài sản không hiện tại` | `tài sản dài hạn` | error |
| liabilities | `trách nhiệm pháp lý` | `nợ phải trả` | error |
| gross margin | `lề gộp` | `biên lợi nhuận gộp` | error |
| operating expense | `chi phí hoạt động chung` | `chi phí quản lý doanh nghiệp / chi phí bán hàng` | warn |
| solvency | `khả năng thanh toán nợ` | `khả năng thanh toán` | warn |
| liquidity | `tính lỏng` | `tính thanh khoản` | error |
| portfolio | `danh mục đầu tư cặp tài liệu` | `danh mục đầu tư` | error |
| dividend | `tiền chia lãi` | `cổ tức` | error |
| share capital | `vốn cổ phần chia sẻ` | `vốn cổ phần` | error |
| market capitalization | `vốn hóa thị trường vốn` | `vốn hóa thị trường` | warn |
| underwrite | `ký dưới` | `bảo lãnh phát hành` | error |
| prospectus | `tờ rơi thông tin` | `bản cáo bạch` | error |
| beneficiary | `người hưởng lợi cá nhân` | `người thụ hưởng` | error |
| interbank wire transfer | `chuyển khoản dây cáp` | `chuyển khoản liên ngân hàng` | error |
| recurring payment | `thanh toán tái diễn` | `thanh toán định kỳ` | error |
| conversion fee | `phí biến đổi` | `phí chuyển đổi` | error |
| early repayment penalty | `tiền phạt trả trước` | `phí trả nợ trước hạn` | error |
| grace period | `giai đoạn ân cần` | `thời gian ân hạn` | error |
| biometric authentication | `xác thực đo lường sinh học` | `xác thực sinh trắc học` | error |
| facial recognition | `công nhận khuôn mặt` | `nhận diện khuôn mặt` | error |
| unit-linked insurance | `bảo hiểm nối kết đơn vị` | `bảo hiểm liên kết đơn vị` | error |
| universal life insurance | `bảo hiểm đời sống toàn cầu` | `bảo hiểm liên kết chung` | error |
| digital asset | `tài sản kỹ thuật con số` | `tài sản số` | error |
| legal tender | `tiền tệ đấu thầu hợp pháp` | `phương tiện thanh toán hợp pháp` | error |
| final tax settlement | `giải quyết thuế cuối cùng` | `quyết toán thuế` | error |
| non-performing loan | `nợ xấu xa` | `nợ xấu` | error |
| debt recovery | `phục hồi nợ` | `thu hồi nợ` | error |
| charter capital | `vốn điều lệ công ty hiến chương` | `vốn điều lệ` | error |

---

## 2. Machine-Readable Guaranteed-Return Patterns (`FIN001`)

The patterns below trigger `FIN001` across all document types. Prohibited in investment solicitation under Luật Chứng khoán 2019 Điều 12 and Nghị định 38/2018/NĐ-CP Điều 2 khoản 4.

<!-- machine-readable: guaranteed-return -->

| Pattern | Description |
|---|---|
| `cam\s+kết\s+(?:lợi\s+nhuận\|lãi\s+suất\|sinh\s+lời\|hoàn\s+vốn)` | Guaranteed return, profit, or interest |
| `đảm\s+bảo\s+(?:sinh\s+lời\|lợi\s+nhuận\|có\s+lãi)` | Assured return or profitability |
| `bảo\s+toàn\s+vốn` | Capital preservation guarantee |
| `đầu\s+tư\s+không\s+(?:có\s+)?rủi\s+ro` | Zero-risk investment claim |
| `chắc\s+chắn\s+có\s+lãi` | Guaranteed profit statement |
| `sinh\s+lời\s+chắc\s+chắn` | Definite yield claim |
| `không\s+bao\s+giờ\s+lỗ` | Never-loss claim |
| `an\s+toàn\s+100\s*%\s+vốn` | 100% capital safety guarantee |
