<!-- vlc-disable: all -->

# Banned & Regulated Phrases in Financial Communication (`design-os-vietnamese`)

In financial, credit, banking, and wealth-management copy, prohibited language directly breaches Vietnamese advertising, consumer protection, and securities laws.

---

## 1. Regulated Superlatives (`LAW001`)

Under **Luật Quảng cáo 16/2012/QH13 Điều 8 khoản 11**, using superlatives without valid documentary certification from a competent state agency or accredited research firm is illegal.

<!-- machine-readable: superlatives -->

| Pattern | Matches | Note |
|---|---|---|
| `(?:tốt\|cao\|thấp\|nhanh\|an\s+toàn\|uy\s+tín\|lớn\|sinh\s+lời\|hiệu\s+quả\|minh\s+bạch)\s+nhất` | "highest interest / safest / lowest fee / most reputable" | Common violation in deposit & credit card ads |
| `duy\s+nhất` | "the only" | Specifically named in statute |
| `số\s*(?:một\|1)\b` | "number one" | Specifically named in statute |
| `hàng\s+đầu` | "leading / top" | Prohibited claim without award certification |
| `đứng\s+đầu` | "ranks first" | Prohibited ranking claim |
| `(?<!#)#\s*1\b` | "#1" | Foreign equivalent symbol |
| `\bno\.?\s*1\b` | "No.1" | Foreign equivalent text |

**Compliant Rewrite Principle:**
Never use empty superlatives (`lãi suất tốt nhất thị trường`). State verified numerical facts:
- ❌ `Lãi suất vay mua nhà tốt nhất thị trường`
- ✅ `Lãi suất vay mua nhà từ 6,5%/năm cố định trong 12 tháng đầu`

---

## 2. Prohibited Slogans & Marketing Claims

The following phrases are prohibited across financial promotions, landing pages, investment pitches, and social ads:

<!-- machine-readable: calques -->

| ❌ Prohibited Phrase | ✅ Compliant Phrasing | Statutory Rationale |
|---|---|---|
| `lợi nhuận khủng` | `lợi nhuận kỳ vọng` | Sensational solicitation banned under Luật Chứng khoán 2019 |
| `x2 tài khoản` | `tỷ suất sinh lời kỳ vọng` | Misleading profit promise |
| `làm giàu không khó` | *(bỏ hoàn toàn)* | Predatory financial marketing |
| `tiền đẻ ra tiền` | `tối ưu hóa hiệu quả nguồn vốn` | Misleading passive income implication |
| `cơ hội đổi đời` | `giải pháp đầu tư tài chính` | Speculative gambling framing |
| `ai cũng có thể đầu tư` | `sản phẩm phù hợp với nhà đầu tư có khẩu vị rủi ro phù hợp` | Violation of investor suitability requirements |
| `không cần kiến thức vẫn có lãi` | *(bỏ hoàn toàn)* | Unsuitable investor solicitation |
| `vốn ít lời nhiều` | `kỳ hạn đầu tư linh hoạt` | Unrealistic return promise |
| `rút vốn bất cứ lúc nào không mất phí` | `biểu phí rút vốn trước hạn quy định tại điều khoản hợp đồng` | Deceptive fee statement |
| `bảo hiểm sinh lời` | `sản phẩm bảo hiểm liên kết đầu tư` | Mis-selling insurance as a high-yield savings vehicle |
| `gửi tiết kiệm lãi cao hơn ngân hàng` | *(bỏ hoàn toàn)* | Misrepresenting corporate bonds or P2P lending as insured bank deposits |
| `sàn quốc tế uy tín` | `tổ chức được Bộ Tài chính cấp phép` | Unlicensed offshore securities/crypto solicitation |
| `đầu tư chắc thắng` | `kế hoạch phân bổ tài sản` | Prohibited outcome guarantee |
| `bí mật làm giàu` | `kiến thức quản lý tài chính cá nhân` | Slop marketing phrasing |

---

## 3. Mandatory Statutory Disclaimers That Must Never Be Softened

Financial marketers frequently attempt to soften or hide mandatory disclaimers. In Vietnamese law, removing or minimizing these statements triggers immediate administrative penalties:

1. **Investment Risk Disclaimer:**
   - Text: `"Đầu tư luôn tiềm ẩn rủi ro thị trường. Kết quả trong quá khứ không mang tính bảo đảm cho hiệu quả đầu tư trong tương lai."`
   - Location: Mandatory on any wealth management, fund, stock, or bond promotion displaying historical performance.
2. **Investment-Linked Insurance Disclaimer (Thông tư 67/2023/TT-BTC Điều 53):**
   - Text: `"Đây là sản phẩm bảo hiểm liên kết đầu tư, không phải là tiền gửi tiết kiệm ngân hàng. Kết quả đầu tư không được bảo đảm và do bên mua bảo hiểm chịu mọi rủi ro."`
   - Requirement: Font size must be equal to or greater than the standard body copy; never hidden in micro-footnotes.
3. **Promotional 0% Interest Rate Transparency (Thông tư 43/2016 & TT 18/2019):**
   - Text: `"Trả góp 0% lãi suất. Phí chuyển đổi giao dịch: [X]%. Tổng chi phí phải trả: [Y] ₫. Lãi suất thực tế áp dụng: [Z]%/năm."`
   - Requirement: All figures must be visible on the same screen or card as the 0% claim.
4. **Digital Asset Disclaimer (Nghị quyết 05/2025/NQ-CP & Luật 71/2025):**
   - Text: `"Tài sản số không phải là phương tiện thanh toán hợp pháp tại Việt Nam."`
