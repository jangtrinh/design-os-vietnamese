# -*- coding: utf-8 -*-
import json
import unicodedata
from pathlib import Path

pairs = [
    {
        "id": "cal-learn-more",
        "category": "calque",
        "en": "Learn more about the project",
        "bad": "Học thêm về dự án của chúng tôi",
        "good": "Tìm hiểu thêm về dự án",
        "diagnosis": "`Học thêm` means study more in an academic sense. Exploring information uses `Tìm hiểu thêm`.",
        "why": "`Học thêm` is academic tutoring/studying; commercial information discovery uses `Tìm hiểu thêm`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-get-started",
        "category": "calque",
        "en": "Get started with our software",
        "bad": "Bắt đầu được với phần mềm của chúng tôi",
        "good": "Bắt đầu ngay với phần mềm của chúng tôi",
        "diagnosis": "The English particle 'started' calqued as `được`. Action CTAs use `Bắt đầu ngay`.",
        "why": "`Bắt đầu được` imports an English particle into a modal capability sense; write `Bắt đầu ngay`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-see-details",
        "category": "calque",
        "en": "See details",
        "bad": "Nhìn chi tiết bảng giá",
        "good": "Xem chi tiết bảng giá",
        "diagnosis": "`Nhìn` is to look physically. Reviewing content or listings is always `xem`.",
        "why": "Physical looking (`nhìn`) is incorrect for examining documents or web listings (`xem`).",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-sign-up",
        "category": "calque",
        "en": "Sign up for newsletter",
        "bad": "Ký lên để nhận tin",
        "good": "Đăng ký nhận tin",
        "diagnosis": "Literal calque of 'sign up' as `ký lên`. The Vietnamese verb is `đăng ký`.",
        "why": "`Ký lên` is a word-for-word calque of 'sign up'; the standard term is `đăng ký`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-contact-us",
        "category": "calque",
        "en": "Contact us today",
        "bad": "Liên lạc chúng tôi ngay hôm nay",
        "good": "Liên hệ ngay với chúng tôi",
        "diagnosis": "`Liên lạc` means maintaining a telecommunication connection. Business inquiries use `liên hệ`.",
        "why": "`Liên lạc` refers to radio/phone transmission channels; inbound sales enquiries use `liên hệ`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-testimonials",
        "category": "calque",
        "en": "Testimonials from partners",
        "bad": "Lời chứng thực từ đối tác",
        "good": "Cảm nhận khách hàng từ đối tác",
        "diagnosis": "`Chứng thực` is notarial certification. Customer endorsements are `cảm nhận khách hàng`.",
        "why": "`Chứng thực` is legal notarial verification; marketing endorsements are `cảm nhận khách hàng`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-trusted-by",
        "category": "calque",
        "en": "Trusted by 500 enterprises",
        "bad": "Tin tưởng bởi 500 doanh nghiệp",
        "good": "Được 500 doanh nghiệp tin dùng",
        "diagnosis": "English passive-agent 'trusted by' calqued as `tin tưởng bởi`. Front the agent with `Được ... tin dùng`.",
        "why": "Passive 'by' calqued as `bởi`; Vietnamese uses `Được [agent] tin dùng`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-free-shipping",
        "category": "calque",
        "en": "Free shipping nationwide",
        "bad": "Vận chuyển tự do toàn quốc",
        "good": "Miễn phí giao hàng toàn quốc",
        "diagnosis": "`Tự do` translates free as in liberty. Free of charge logistics is `miễn phí giao hàng`.",
        "why": "`Tự do` means liberty/unconstrained, not zero monetary cost; use `miễn phí giao hàng`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-add-to-cart",
        "category": "calque",
        "en": "Add to cart now",
        "bad": "Thêm vào xe đẩy ngay",
        "good": "Thêm vào giỏ hàng ngay",
        "diagnosis": "Literal translation of shopping cart as `xe đẩy` (supermarket trolley). Online commerce uses `giỏ hàng`.",
        "why": "`Xe đẩy` is a physical supermarket trolley; web shopping uses `giỏ hàng`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-privacy-policy",
        "category": "calque",
        "en": "Privacy Policy",
        "bad": "Xem Chính sách riêng tư của chúng tôi",
        "good": "Xem Chính sách bảo mật của chúng tôi",
        "diagnosis": "`Riêng tư` is personal intimacy. The statutory legal term in Vietnam is `Chính sách bảo mật`.",
        "why": "`Riêng tư` refers to personal lifestyle privacy; statutory documents use `Chính sách bảo mật`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-one-stop",
        "category": "calque",
        "en": "A one-stop solution for offices",
        "bad": "Giải pháp một cửa cho văn phòng hiện đại",
        "good": "Giải pháp trọn gói cho văn phòng hiện đại",
        "diagnosis": "`Một cửa` refers strictly to state administrative single-window desks. Business offerings are `trọn gói`.",
        "why": "`Một cửa` is state public administration; commercial turnkey packages are `trọn gói`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-click-here",
        "category": "calque",
        "en": "Click here to receive offers",
        "bad": "Nhấp vào đây để nhận ưu đãi",
        "good": "Xem chi tiết để nhận ưu đãi",
        "diagnosis": "'Click here' is outdated UX microcopy and reads as amateur translation.",
        "why": "'Click here' (`nhấp vào đây`) is weak microcopy; state the user outcome directly.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-order-in-stock",
        "category": "calque",
        "en": "Products currently in stock",
        "bad": "Sản phẩm hiện đang trong cổ phiếu",
        "good": "Sản phẩm hiện đang còn hàng",
        "diagnosis": "`Cổ phiếu` translates stock as in equity shares. Inventory availability is `còn hàng`.",
        "why": "`Cổ phiếu` means financial equities; warehouse stock is `còn hàng`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-real-time",
        "category": "calque",
        "en": "Update data in real time",
        "bad": "Cập nhật dữ liệu trong thời gian thực",
        "good": "Cập nhật dữ liệu theo thời gian thực",
        "diagnosis": "Preposition `trong` is a calque of English 'in'. Vietnamese uses `theo thời gian thực`.",
        "why": "Vietnamese uses preposition `theo` for dynamic tracking, not static containment `trong`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-word-order",
        "category": "word-order",
        "en": "Premium apartments with river view",
        "bad": "Khám phá các cao cấp căn hộ ven sông",
        "good": "Khám phá các căn hộ cao cấp ven sông",
        "diagnosis": "English places adjectives before nouns; Vietnamese requires noun-modifier order.",
        "why": "Vietnamese places qualifying adjectives after nouns (`căn hộ cao cấp`).",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "cal-chung-ta",
        "category": "register",
        "en": "We provide warehouse management solutions",
        "bad": "Chúng ta cung cấp nền tảng quản trị kho",
        "good": "Chúng tôi cung cấp nền tảng quản trị kho",
        "diagnosis": "`Chúng ta` includes the reader as an employee. A company speaking to customers uses `chúng tôi`.",
        "why": "Inclusive `chúng ta` mistakenly claims the customer is part of the corporate entity.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "law-number-one",
        "category": "legal",
        "en": "No.1 massage chair brand in Vietnam",
        "bad": "Thương hiệu ghế massage số 1 Việt Nam",
        "good": "Thương hiệu ghế massage được hơn 50.000 gia đình tin dùng",
        "diagnosis": "Unproven superlative claim prohibited by Luật Quảng cáo Điều 8 khoản 11.",
        "why": "`số 1` without certified proof violates Điều 8 khoản 11 Luật Quảng cáo.",
        "expected_rules": ["LAW001"]
    },
    {
        "id": "law-best-market",
        "category": "legal",
        "en": "Best apartments on the market",
        "bad": "Dự án căn hộ tốt nhất thị trường",
        "good": "Dự án căn hộ chuẩn sinh thái ven sông",
        "diagnosis": "Unproven superlative claim `tốt nhất` prohibited by Luật Quảng cáo.",
        "why": "`tốt nhất` is an unproven absolute superlative; replace with an aspirational feature phrase.",
        "expected_rules": ["LAW001"]
    },
    {
        "id": "law-leading-developer",
        "category": "legal",
        "en": "Leading real estate developer in Vietnam",
        "bad": "Chủ đầu tư hàng đầu Việt Nam",
        "good": "Chủ đầu tư với hơn 20 năm kinh nghiệm tại Việt Nam",
        "diagnosis": "`Hàng đầu` is regulated wording of similar meaning under Luật Quảng cáo.",
        "why": "`hàng đầu` is a regulated superiority claim requiring licensed market survey proof.",
        "expected_rules": ["LAW001"]
    },
    {
        "id": "nfc-decomposed",
        "category": "unicode",
        "en": "Luxury apartments in new urban project",
        "bad": unicodedata.normalize("NFD", "Căn hộ cao cấp tại dự án mới"),
        "good": unicodedata.normalize("NFC", "Căn hộ cao cấp tại dự án mới"),
        "diagnosis": "Text is encoded in decomposed NFD Unicode instead of precomposed NFC.",
        "why": "NFD decomposed diacritics break web font layout and text length counting.",
        "expected_rules": ["NFC001"]
    },
    {
        "id": "dia-unaccented",
        "category": "diacritics",
        "en": "District 9 premium apartments",
        "bad": "Can ho cao cap quan 9 mo ban gia goc",
        "good": "Căn hộ cao cấp Quận 9 mở bán giá gốc",
        "diagnosis": "Vietnamese marketing copy written without tone marks and diacritics.",
        "why": "Unaccented Vietnamese belongs in search URLs and slugs, never in user-facing marketing copy.",
        "expected_rules": ["DIA001"]
    },
    {
        "id": "tone-mixed-style",
        "category": "tone",
        "en": "Peaceful and harmonious urban area",
        "bad": "Dự án khu đô thị hoà bình và hòa thuận.",
        "good": "Dự án khu đô thị hoà bình và hoà thuận.",
        "diagnosis": "Mixed tone mark placements: `hoà` (kiểu mới) and `hòa` (kiểu cũ) in the same text.",
        "why": "Inconsistent tone placement within a single document looks unproofread.",
        "expected_rules": ["TONE001"]
    },
    {
        "id": "num-comma-group",
        "category": "number",
        "en": "Booking deposit only 50,000 VND today",
        "bad": "Ưu đãi đặt cọc chỉ 50,000 ₫ hôm nay.",
        "good": "Ưu đãi đặt cọc chỉ 50.000 ₫ hôm nay.",
        "diagnosis": "American comma grouping used for Vietnamese Dong.",
        "why": "Vietnamese currency groups thousands with periods (`50.000 ₫`), not commas.",
        "expected_rules": ["NUM001"]
    },
    {
        "id": "num-ungrouped",
        "category": "number",
        "en": "Service fee starting from 50000 VND per day",
        "bad": "Giá thuê khởi điểm từ 50000 ₫ một ngày.",
        "good": "Giá thuê khởi điểm từ 50.000 ₫ một ngày.",
        "diagnosis": "Ungrouped currency amount of 5 or more digits without thousands separator.",
        "why": "Amounts of 5 digits or more must group thousands with periods.",
        "expected_rules": ["NUM002"]
    },
    {
        "id": "num-dot-decimal",
        "category": "number",
        "en": "Absorption rate reached 15.5% in first week",
        "bad": "Tỷ lệ hấp thụ sản phẩm đạt 15.5% trong tuần đầu.",
        "good": "Tỷ lệ hấp thụ sản phẩm đạt 15,5% trong tuần đầu.",
        "diagnosis": "Period used as a decimal separator instead of Vietnamese comma.",
        "why": "Vietnamese uses comma for decimal fractions (`15,5%`).",
        "expected_rules": ["NUM003"]
    },
    {
        "id": "num-ascii-sqm",
        "category": "number",
        "en": "Rental price from 350,000 VND/m2 per month",
        "bad": "Giá thuê mặt bằng chỉ từ 350.000 ₫/m2 một tháng.",
        "good": "Giá thuê mặt bằng chỉ từ 350.000 ₫/m² một tháng.",
        "diagnosis": "ASCII `m2` used instead of superscript `m²`.",
        "why": "Professional typography uses superscript `m²` for square meters.",
        "expected_rules": ["NUM004"]
    },
    {
        "id": "date-mm-dd",
        "category": "date",
        "en": "Registration deadline before 09/28/2026",
        "bad": "Thời hạn đăng ký trước ngày 09/28/2026.",
        "good": "Thời hạn đăng ký trước ngày 28/09/2026.",
        "diagnosis": "American MM/dd/yyyy date format used instead of Vietnamese dd/MM/yyyy.",
        "why": "Vietnamese locale formatting strictly requires dd/MM/yyyy date ordering.",
        "expected_rules": ["DATE001"]
    },
    {
        "id": "phone-trunk-zero",
        "category": "phone",
        "en": "Customer care hotline: +84 0912 345 678",
        "bad": "Tổng đài chăm sóc khách hàng: +84 0912 345 678.",
        "good": "Tổng đài chăm sóc khách hàng: +84 912 345 678.",
        "diagnosis": "Domestic trunk zero kept after international country code +84.",
        "why": "The leading 0 must be dropped when using country code +84.",
        "expected_rules": ["PHONE001"]
    },
    {
        "id": "icu-plural-branches",
        "category": "i18n",
        "en": "1 apartment / 5 apartments",
        "bad": '{"units": "{count, plural, one {# căn hộ} other {# căn hộ}}"}',
        "good": '{"units": "{count, plural, other {# căn hộ}}"}',
        "diagnosis": "ICU plural contains a `one` branch. Vietnamese has no grammatical plural categories besides `other`.",
        "why": "Vietnamese CLDR plural has only the `other` branch; `one` is a copy-paste error from English.",
        "expected_rules": ["ICU001"],
        "filename": "vi.json"
    },
    {
        "id": "pro-mixed-document",
        "category": "register",
        "en": "Welcome customers. Register to visit model unit.",
        "bad": "Kính chào Quý khách. Bạn hãy đăng ký tham quan nhà mẫu ngay.",
        "good": "Kính chào Quý khách. Quý khách vui lòng đăng ký tham quan nhà mẫu ngay.",
        "diagnosis": "Mixed registers: `Quý khách` and `bạn` in the same landing page document.",
        "why": "A document must maintain one consistent audience address register throughout.",
        "expected_rules": ["PRO001"]
    },
    {
        "id": "pro-register-mismatch",
        "category": "register",
        "en": "Welcome to our software platform",
        "bad": "Kính chào Quý khách đến với nền tảng của chúng tôi.",
        "good": "Chào mừng bạn đến với nền tảng của chúng tôi.",
        "diagnosis": "`Quý khách` is forbidden in the declared `saas` register, which expects `bạn`.",
        "why": "The `saas` register is approachable and peer-level (`bạn`); `Quý khách` signals corporate stiffness.",
        "expected_rules": ["PRO002"],
        "register": "saas"
    },
    {
        "id": "syn-dummy-subject",
        "category": "syntax",
        "en": "It is very important to optimize the sales process",
        "bad": "Nó là rất quan trọng để tối ưu hóa quy trình bán hàng.",
        "good": "Việc tối ưu hóa quy trình bán hàng là rất quan trọng.",
        "diagnosis": "English dummy-subject calque 'It is important to...'.",
        "why": "Vietnamese has no dummy 'it'; recast as a topicalized noun clause or direct verb.",
        "expected_rules": ["SYN001"]
    },
    {
        "id": "lnd-hero-passive",
        "category": "landing",
        "en": "Riverside villa designed by world leading architect",
        "bad": "Biệt thự ven sông được thiết kế bởi kiến trúc sư Foster.",
        "good": "Biệt thự ven sông do kiến trúc sư Foster thiết kế.",
        "diagnosis": "Passive English construction `được thiết kế bởi` in hero headline copy.",
        "why": "Hero headlines should front the actor active-voice (`Do [agent] thiết kế`).",
        "expected_rules": ["LND001"],
        "doctype": "hero"
    },
    {
        "id": "lnd-leadform-compliance",
        "category": "landing",
        "en": "Submit form with name and phone number",
        "bad": "Để lại thông tin gồm họ và tên và số điện thoại để nhận tư vấn ngay.",
        "good": "Để lại họ và tên và số điện thoại. Tôi đồng ý để công ty xử lý dữ liệu cá nhân theo Chính sách bảo mật nhằm mục đích tư vấn sản phẩm.",
        "diagnosis": "Lead form collecting personal data without purpose statement and privacy policy link (NĐ 13/2023).",
        "why": "Nghị định 13/2023/NĐ-CP requires stating the processing purpose and referencing Chính sách bảo mật.",
        "expected_rules": ["LND002"],
        "doctype": "lead-form"
    },
    {
        "id": "lnd-footer-compliance",
        "category": "landing",
        "en": "Fashion Retail Co. Ltd. Headquarters: 45 Le Duan, District 1.",
        "bad": "Công ty TNHH Bán Lẻ Thời Trang. Địa chỉ trụ sở: 45 Lê Duẩn, Quận 1. Hotline: 0912345678.",
        "good": "Công ty TNHH Bán Lẻ Thời Trang. MST: 0312345678. Địa chỉ trụ sở: 45 Lê Duẩn, Quận 1. Hotline: 0912345678. Đã thông báo Bộ Công Thương.",
        "diagnosis": "E-commerce footer missing mandatory statutory fields: Tax ID (MST) and Ministry of Industry and Trade notice.",
        "why": "Nghị định 52/2013/NĐ-CP & 85/2021/NĐ-CP mandate displaying MST and Bộ Công Thương registration.",
        "expected_rules": ["LND003"],
        "doctype": "ecommerce-footer"
    },
    {
        "id": "lnd-pricing-month",
        "category": "landing",
        "en": "Professional package: 499,000 VND/month",
        "bad": "Gói dịch vụ chuyên nghiệp giá 499.000 ₫/month dành cho đội nhóm.",
        "good": "Gói dịch vụ chuyên nghiệp giá 499.000 ₫/tháng dành cho đội nhóm.",
        "diagnosis": "English billing period `/month` in pricing table instead of `/tháng`.",
        "why": "Pricing tables on Vietnamese sites must use `/tháng` or `/năm`, not English `/month`.",
        "expected_rules": ["LND004"],
        "doctype": "pricing-table"
    },
    {
        "id": "lnd-pricing-mixed-scale",
        "category": "landing",
        "en": "Basic plan 500k/month, advanced plan 1,500,000 VND/month",
        "bad": "Gói cơ bản giá 500k một tháng, gói nâng cao giá 1.500.000 ₫ một tháng.",
        "good": "Gói cơ bản giá 500.000 ₫ một tháng, gói nâng cao giá 1.500.000 ₫ một tháng.",
        "diagnosis": "Mixing colloquial scale (500k) and full period-grouped digits (1.500.000 ₫) in the same pricing table.",
        "why": "Pricing tables must maintain uniform denomination formatting across tiers.",
        "expected_rules": ["LND004"],
        "doctype": "pricing-table"
    }
]

out_path = Path(__file__).resolve().parent.parent / "evals" / "vietnamese-landing-copy" / "pairs.jsonl"
out_path.parent.mkdir(parents=True, exist_ok=True)
with out_path.open("w", encoding="utf-8") as f:
    for p in pairs:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

print(f"Generated {len(pairs)} pairs to {out_path}")
