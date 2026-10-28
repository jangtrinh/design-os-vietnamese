<!-- vlc-disable: all -->

# Vietnamese Legal & Contract Terminology Glossary (`vietnamese-legal-contracts`)

This glossary provides standardized Vietnamese civil-law terminology, contract drafting phrasing, intellectual property nomenclature, labor law classifications, and personal data protection terms (Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15 & Nghị định 356/2025/NĐ-CP; Nghị định 13/2023/NĐ-CP no longer in force from 01/01/2026).

The machine-readable table below is loaded by `validate_copy.py` at runtime; each row acts as an active linting rule firing `CAL001` with the declared severity.

---

## 1. Machine-Readable Contract & Legal Terms (`CAL001`)

<!-- machine-readable: glossary -->

| EN | ❌ Wrong or stale | ✅ Correct | Severity |
|---|---|---|---|
| indemnification | `bồi thường vô hại` | `bồi thường thiệt hại` | error |
| hold harmless | `giữ vô hại` | `miễn trừ trách nhiệm bồi thường` | error |
| liquidated damages | `tiền thiệt hại thanh lý` | `phạt vi phạm / bồi thường thiệt hại ước tính` | error |
| force majeure | `lực lượng cao cấp` | `sự kiện bất khả kháng` | error |
| severability | `tính có thể cắt đứt` | `tính hiệu lực từng phần / hiệu lực độc lập của các điều khoản` | error |
| governing law | `luật chi phối` | `luật áp dụng` | error |
| dispute resolution | `giải tán tranh chấp` | `giải quyết tranh chấp` | error |
| arbitration | `trọng tài phán xét` | `trọng tài thương mại` | error |
| jurisdiction | `khu vực tài phán xét xử` | `thẩm quyền tài phán / thẩm quyền xét xử của tòa án` | error |
| representations and warranties | `đại diện và bảo hành` | `cam đoan và bảo đảm` | error |
| covenants | `giao ước tôn giáo` | `nghĩa vụ cam kết` | error |
| non-disclosure agreement | `hợp đồng không tiết lộ` | `thỏa thuận bảo mật thông tin` | error |
| non-compete agreement | `thỏa thuận không ganh đua` | `cam kết hạn chế cạnh tranh / thỏa thuận không cạnh tranh` | error |
| non-solicitation | `không chèo kéo nhân viên` | `cam kết không lôi kéo nhân sự và khách hàng` | error |
| intellectual property | `tài sản trí tuệ trừu tượng` | `quyền sở hữu trí tuệ` | error |
| copyright | `quyền sao chép chép lại` | `quyền tác giả` | error |
| moral rights | `quyền đạo đức` | `quyền nhân thân` | error |
| economic rights | `quyền kinh tế tài chính` | `quyền tài sản` | error |
| assignment of IP | `chuyển nhượng tài sản trí tuệ phân công` | `chuyển nhượng quyền sở hữu trí tuệ` | error |
| licensing | `cấp giấy phép sử dụng` | `chuyển quyền sử dụng đối tượng sở hữu trí tuệ / cấp phép sử dụng` | warn |
| breach of contract | `phá vỡ hợp đồng` | `vi phạm hợp đồng` | error |
| termination | `hủy diệt hợp đồng` | `chấm dứt hợp đồng` | error |
| rescission | `hủy bỏ hiệu lực từ đầu` | `hủy bỏ hợp đồng` | error |
| material breach | `vi phạm vật chất` | `vi phạm cơ bản nghĩa vụ hợp đồng` | error |
| condition precedent | `điều kiện tiền nhiệm` | `điều kiện tiên quyết` | error |
| entire agreement | `toàn bộ sự đồng ý hợp nhất` | `tính toàn vẹn của hợp đồng / thỏa thuận toàn bộ` | error |
| waiver of rights | `từ bỏ quyền hạn từ chối` | `từ bỏ quyền` | error |
| remedies | `phương thuốc cứu chữa pháp lý` | `biện pháp chế tài / biện pháp khắc phục vi phạm` | error |
| specific performance | `thực hiện cụ thể` | `buộc thực hiện đúng hợp đồng` | error |
| statutory penalty | `tiền phạt theo luật định hình` | `phạt vi phạm theo luật định` | error |
| consequential damages | `thiệt hại hậu quả tiếp theo` | `thiệt hại gián tiếp` | error |
| direct damages | `thiệt hại trực diện` | `thiệt hại trực tiếp thực tế` | error |
| loss of profit | `mất mát lợi nhuận` | `khoản lợi nhuận bị bỏ lỡ / lợi nhuận đáng lẽ được hưởng` | error |
| limitation of liability | `giới hạn bổn phận pháp lý` | `giới hạn trách nhiệm bồi thường` | error |
| exclusion of liability | `loại trừ bổn phận` | `miễn trừ trách nhiệm` | error |
| data subject | `chủ đề dữ liệu` | `chủ thể dữ liệu` | error |
| data controller | `người điều khiển dữ liệu` | `bên kiểm soát dữ liệu cá nhân` | error |
| data processor | `bên chế biến dữ liệu` | `bên xử lý dữ liệu cá nhân` | error |
| personal data | `dữ liệu riêng tư` | `dữ liệu cá nhân` | error |
| sensitive personal data | `dữ liệu nhạy cảm mềm` | `dữ liệu cá nhân nhạy cảm` | error |
| cross-border transfer | `chuyển giao xuyên biên thùy` | `chuyển dữ liệu cá nhân ra nước ngoài` | error |
| terms of service | `điều kiện phục vụ` | `điều khoản sử dụng dịch vụ` | error |
| standard form contract | `hợp đồng hình thức tiêu chuẩn` | `hợp đồng theo mẫu` | error |
| general trading conditions | `điều kiện buôn bán tổng hợp` | `điều kiện giao dịch chung` | error |
| unconscionable clause | `điều khoản vô lương tâm` | `điều khoản không công bằng / điều khoản vô hiệu` | error |
| unfair terms | `điều khoản bất công` | `điều khoản không lành mạnh / điều khoản xâm phạm quyền lợi người tiêu dùng` | error |
| dispute | `cuộc cãi vã pháp lý` | `tranh chấp hợp đồng` | error |
| venue | `địa điểm gặp mặt xét xử` | `tòa án có thẩm quyền / nơi giải quyết tranh chấp` | error |
| counterpart | `bản sao đối tác` | `bản chính có giá trị pháp lý như nhau` | error |
| execute a contract | `hành quyết hợp đồng` | `giao kết hợp đồng / ký kết hợp đồng` | error |
| valid and binding | `hợp lệ và trói buộc` | `có hiệu lực pháp lý và ràng buộc các bên` | error |
| in witness whereof | `để làm nhân chứng cho điều đó` | `để làm bằng chứng, các bên ký tên dưới đây` | error |
| without prejudice to | `không có thành kiến với` | `không làm phương hại đến quyền` | error |
| notwithstanding | `không đứng vững trước` | `mặc dù có quy định / trừ trường hợp có thỏa thuận khác` | error |
| recitals | `phần mở đầu diễn giải` | `căn cứ giao kết hợp đồng / giải thích bối cảnh` | error |
| formal notice | `thông báo chú ý` | `thông báo bằng văn bản` | error |
| legal entity | `thực thể pháp nhân tính` | `pháp nhân` | error |
| legal capacity | `sức chứa ký hợp đồng` | `năng lực hành vi dân sự để giao kết hợp đồng` | error |
| power of attorney | `sức mạnh của luật sư` | `giấy ủy quyền / hợp đồng ủy quyền` | error |
| authorized representative | `đại diện được ủy quyền có sức mạnh` | `người đại diện theo ủy quyền` | error |
| legal representative | `đại diện theo pháp luật bắt buộc` | `người đại diện theo pháp luật` | error |
| security deposit | `tiền cọc giữ chỗ` | `đặt cọc` | error |
| escrow account | `tài khoản ký thác bí mật` | `tài khoản ký quỹ` | error |
| pledge of assets | `lời thề cầm đồ` | `cầm cố tài sản` | error |
| mortgage of assets | `thế chấp ngân hàng nợ` | `thế chấp tài sản` | error |
| joint and several liability | `trách nhiệm kết hợp và chia rẽ` | `trách nhiệm liên đới` | error |
| trade secret | `bí quyết thương nghiệp giấu kín` | `bí mật kinh doanh` | error |

---

## 2. Vietnamese Civil Law vs. Common Law Doctrinal Equivalents

Drafting cross-border agreements into Vietnamese requires recognizing doctrinal divergence between Anglo-American Common Law and Vietnamese Civil Law (dựa trên hệ thống Dân luật chịu ảnh hưởng từ Bộ luật Dân sự Pháp và Đức):

1. **Indemnity (`Bồi thường thiệt hại`):**
   - In Common Law, an indemnity creates a primary, standalone obligation to hold the indemnified party harmless from costs, regardless of fault or breach.
   - Under **Bộ luật Dân sự 2015 Điều 360 & Điều 419** and **Luật Thương mại 2005 Điều 302–307**, compensation for damage (`bồi thường thiệt hại`) requires establishing: (i) an act of breach, (ii) actual and direct loss or lost profit, and (iii) a direct causal link between breach and damage.
2. **Liquidated Damages (`Phạt vi phạm` vs. `Bồi thường thiệt hại ước tính`):**
   - Vietnamese Commercial Law (Điều 300 & Điều 301) strictly caps agreed penalties for breach (`phạt vi phạm`) at **8% of the breached contract obligation value**.
   - Liquidated damages clauses imported from English common law that set arbitrary pre-estimated amounts exceeding 8% are partially void as penalty clauses. They must be drafted either within the 8% cap or structured under Civil Code 2015 Điều 418 (for non-commercial contracts) or as genuine damages calculation mechanisms.
3. **Representations & Warranties (`Cam đoan và bảo đảm`):**
   - Vietnamese law does not distinguish between common-law equitable representations (remedied by rescission) and legal warranties (remedied by damages).
   - Both are subsumed under the general civil obligation of truthfulness, information disclosure, and contractual warranty (`bảo đảm chất lượng`, `cam đoan quyền sở hữu`).
