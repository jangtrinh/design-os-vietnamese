# -*- coding: utf-8 -*-
import json
import unicodedata
from pathlib import Path

pairs = [
    {
        "id": "eng-commit-cam-ket",
        "category": "engineering",
        "en": "Commit your code changes",
        "bad": "Cam kết các thay đổi của bạn trước khi tạo PR.",
        "good": "Commit các thay đổi trước khi tạo PR.",
        "diagnosis": "`Cam kết` means to pledge or promise legally. Git revision recording is strictly `commit`.",
        "why": "`Cam kết` is a legal/moral pledge; Git revision recording stays `commit`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-deploy-production",
        "category": "engineering",
        "en": "Deploy the build to production",
        "bad": "Triển khai đến sản xuất sau khi test xong.",
        "good": "Deploy lên production sau khi test xong.",
        "diagnosis": "`Sản xuất` is industrial factory manufacturing. Deployment environments stay English (`production`).",
        "why": "Environment names are never translated; `sản xuất` means factory manufacturing.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-pull-request",
        "category": "engineering",
        "en": "Open a pull request on GitHub",
        "bad": "Mở một yêu cầu kéo trên GitHub để team review.",
        "good": "Tạo một pull request trên GitHub để team review.",
        "diagnosis": "`Yêu cầu kéo` is a textbook dictionary calque. Vietnamese developers say `pull request` or `PR`.",
        "why": "`Yêu cầu kéo` is a literal calque; standard engineering prose uses `pull request` or `PR`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-merge-branch",
        "category": "engineering",
        "en": "Merge the feature branch into main",
        "bad": "Hợp nhất chi nhánh tính năng vào nhánh main.",
        "good": "Merge nhánh tính năng vào nhánh main.",
        "diagnosis": "`Hợp nhất chi nhánh` calques the Git merge command. Engineers say `merge nhánh`.",
        "why": "Git command operations stay English (`merge nhánh`).",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-fix-bug",
        "category": "engineering",
        "en": "Fix bug in payment cache",
        "bad": "Sửa con bọ trong bộ nhớ đệm thanh toán.",
        "good": "Fix bug trong bộ nhớ đệm thanh toán.",
        "diagnosis": "`Con bọ` is a biological insect. Software defects are `bug` or `lỗi`.",
        "why": "`Con bọ` is humorous/inappropriate for serious engineering docs; write `fix bug` or `sửa lỗi`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-message-queue",
        "category": "engineering",
        "en": "Message queue is overloaded",
        "bad": "Hàng đợi thông điệp đang bị quá tải request.",
        "good": "Message queue đang bị quá tải request.",
        "diagnosis": "`Hàng đợi thông điệp` is pedantic textbook translationese. Engineers write `message queue`.",
        "why": "`Hàng đợi thông điệp` is over-translated; Vietnamese developers use `message queue`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-something-wrong",
        "category": "engineering",
        "en": "Something went wrong. Please try again.",
        "bad": "Cái gì đó đã đi sai. Vui lòng thử lại.",
        "good": "Đã có lỗi xảy ra. Vui lòng thử lại.",
        "diagnosis": "Literal translation of the English idiom 'Something went wrong'.",
        "why": "Word-for-word calque of an English idiom; settled Vietnamese is `Đã có lỗi xảy ra`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-refresh-page",
        "category": "engineering",
        "en": "Refresh the page to see changes",
        "bad": "Làm tươi trang để xem các thay đổi mới.",
        "good": "Tải lại trang để xem các thay đổi mới.",
        "diagnosis": "`Làm tươi` translates food/botanical freshness. Browser reload is `tải lại trang`.",
        "why": "`Làm tươi` refers to food/flowers; refreshing a webpage is `tải lại trang`.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "eng-branch-diacritics",
        "category": "engineering",
        "en": "Feature branch name for auth",
        "bad": "feat/thêm-đăng-nhập",
        "good": "feat/add-login",
        "diagnosis": "Branch names must contain only ASCII characters. Diacritics break CLI tools and case folding.",
        "why": "Branch names must be ASCII to prevent shell and filesystem collation corruptions.",
        "expected_rules": ["ENG001"],
        "doctype": "branch"
    },
    {
        "id": "eng-commit-subject-diacritics",
        "category": "engineering",
        "en": "Git commit subject line",
        "bad": "sửa lỗi xác thực tài khoản",
        "good": "fix: resolve authentication validation error",
        "diagnosis": "The subject line of a git commit must be ASCII. The commit body may contain Vietnamese.",
        "why": "Commit subject lines must remain ASCII for compatibility with git log formatters and CI.",
        "expected_rules": ["ENG001"],
        "doctype": "commit"
    },
    {
        "id": "eng-identifier-ascii",
        "category": "i18n",
        "en": "i18n key in JSON resource file",
        "bad": '"auth.đăngNhập.tiêuĐề": "Đăng nhập"',
        "good": '"auth.signIn.title": "Đăng nhập"',
        "diagnosis": "Resource keys must be ASCII. Diacritics in keys break code generation and AST linters.",
        "why": "i18n resource keys must be ASCII; only values contain Vietnamese.",
        "expected_rules": ["ENG001"],
        "doctype": "identifier",
        "filename": "messages.vi.json"
    },
    {
        "id": "eng-rfc-direct-address",
        "category": "engineering",
        "en": "RFC specification describing retry policy",
        "bad": "Bạn sẽ thử lại request tối đa 3 lần khi gặp lỗi kết nối.",
        "good": "Hệ thống sẽ tự động thử lại request tối đa 3 lần khi gặp lỗi kết nối.",
        "diagnosis": "An RFC describes a system, not a reader. Direct address `bạn` is forbidden.",
        "why": "RFCs describe system architecture objectively; eliminate `bạn` with impersonal frames.",
        "expected_rules": ["ENG003"],
        "doctype": "rfc"
    },
    {
        "id": "eng-postmortem-address",
        "category": "engineering",
        "en": "Blameless postmortem incident description",
        "bad": "Bạn đã deploy nhầm script khiến dịch vụ thanh toán bị gián đoạn.",
        "good": "Dịch vụ thanh toán bị gián đoạn do script migration thực thi thiếu biến môi trường.",
        "diagnosis": "Postmortems must be blameless. Direct address `bạn` accuses individuals instead of analyzing systemic failure.",
        "why": "Postmortems must name system transitions, never individuals or direct second-person address.",
        "expected_rules": ["ENG003"],
        "doctype": "postmortem"
    },
    {
        "id": "eng-adr-direct-address",
        "category": "engineering",
        "en": "Architecture decision record",
        "bad": "Trong phần này, bạn sẽ tích hợp Apache Kafka làm message bus.",
        "good": "Hệ thống tích hợp Apache Kafka làm message bus trung tâm.",
        "diagnosis": "ADRs describe structural system decisions. Second-person address `bạn` is forbidden.",
        "why": "ADRs are impersonal records of architectural decisions; eliminate `bạn`.",
        "expected_rules": ["ENG003"],
        "doctype": "adr"
    },
    {
        "id": "eng-runbook-hedged-nen",
        "category": "engineering",
        "en": "Runbook step: run migration before restart",
        "bad": "Bạn nên chạy migration cơ sở dữ liệu trước khi restart dịch vụ.",
        "good": "Chạy migration cơ sở dữ liệu trước khi restart dịch vụ.",
        "diagnosis": "Hedged instruction `bạn nên` makes an essential procedure appear optional during an outage.",
        "why": "Runbook instructions must use bare imperatives without hedging (`bạn nên`).",
        "expected_rules": ["ENG007"],
        "doctype": "runbook"
    },
    {
        "id": "eng-runbook-hedged-co-the",
        "category": "engineering",
        "en": "Runbook step: clear cache if latency spikes",
        "bad": "Bạn có thể xoá cache Redis nếu độ trễ tăng cao.",
        "good": "Xoá cache Redis nếu độ trễ tăng cao.",
        "diagnosis": "Hedged instruction `bạn có thể` introduces hesitation during emergency response.",
        "why": "Runbooks require crisp bare imperatives without `bạn có thể`.",
        "expected_rules": ["ENG007"],
        "doctype": "runbook"
    },
    {
        "id": "eng-error-user-blame-nhap-sai",
        "category": "microcopy",
        "en": "Email validation error message",
        "bad": "Bạn đã nhập sai địa chỉ email.",
        "good": "Địa chỉ email không đúng định dạng. Vui lòng kiểm tra lại.",
        "diagnosis": "Directly blaming the user (`Bạn đã nhập sai`) in form validation microcopy.",
        "why": "Error messages must describe the objective state without accusing the user.",
        "expected_rules": ["ENG008"],
        "doctype": "error-message"
    },
    {
        "id": "eng-error-user-blame-loi-cua-ban",
        "category": "microcopy",
        "en": "Password length validation",
        "bad": "Lỗi của bạn: mật khẩu quá ngắn.",
        "good": "Mật khẩu cần tối thiểu 8 ký tự.",
        "diagnosis": "Accusing the user with `Lỗi của bạn` in an error message.",
        "why": "Never blame the user; state the system input requirement objectively.",
        "expected_rules": ["ENG008"],
        "doctype": "error-message"
    },
    {
        "id": "prd-sprint-backlog",
        "category": "product",
        "en": "Add tickets to sprint backlog",
        "bad": "Thêm các ticket vào tồn đọng chạy nước rút.",
        "good": "Thêm các ticket vào sprint backlog.",
        "diagnosis": "Comical calque of agile terminology: `tồn đọng chạy nước rút` instead of `sprint backlog`.",
        "why": "Agile ceremonies and artifacts stay English in professional product teams.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "prd-user-story-syntax",
        "category": "product",
        "en": "As a user, I want to reset my password",
        "bad": "Như một người dùng, tôi muốn đặt lại mật khẩu của mình.",
        "good": "Là người dùng, tôi muốn đặt lại mật khẩu.",
        "diagnosis": "`Như một` is a comparative calque. Vietnamese user stories start with `Là [vai trò]`.",
        "why": "Standard Vietnamese user story convention is `Là [vai trò]`, not comparative `Như một`.",
        "expected_rules": ["CAL001", "SYN001"]
    },
    {
        "id": "prd-empty-state-slop",
        "category": "microcopy",
        "en": "Empty state screen message",
        "bad": "Trạng thái trống trải",
        "good": "Chưa có dự án nào. Nhấn nút bên dưới để tạo mới.",
        "diagnosis": "Shipping internal UI jargon (`trạng thái trống`) to end users instead of actionable copy.",
        "why": "Never display internal design terminology; tell the user what is missing and how to add it.",
        "expected_rules": ["CAL001"]
    },
    {
        "id": "prd-agree-scale-question",
        "category": "survey",
        "en": "Survey question asking for agreement",
        "bad": "Bạn có đồng ý rằng nền tảng rất dễ sử dụng không?",
        "good": "Mức độ dễ dàng khi sử dụng nền tảng? (Rất khó – Rất dễ)",
        "diagnosis": "Agree/disagree question structure primes agreement and creates acquiescence bias.",
        "why": "Agree/disagree questions bias results by 10-15%; use an item-specific construct scale.",
        "expected_rules": ["PROD002"],
        "doctype": "survey"
    },
    {
        "id": "prd-agree-scale-endpoints",
        "category": "survey",
        "en": "Survey scale response options",
        "bad": "Lựa chọn: Rất đồng ý / Đồng ý / Không đồng ý",
        "good": "Lựa chọn: Rất không hài lòng / Hài lòng / Rất hài lòng",
        "diagnosis": "Agree/disagree response endpoints (`đồng ý / không đồng ý`) inflate feedback scores.",
        "why": "Replace agree/disagree options with item-specific satisfaction or difficulty endpoints.",
        "expected_rules": ["PROD002"],
        "doctype": "survey"
    },
    {
        "id": "prd-app-store-title-limit",
        "category": "app-store",
        "en": "App Store title exceeding 30 characters",
        "bad": "DESIGN:OS - Nền tảng thiết kế giao diện tự động hoá chuyên nghiệp",
        "good": "DESIGN:OS - Thiết kế giao diện",
        "diagnosis": "Title is 64 characters, exceeding the Apple App Store 30-character limit.",
        "why": "App Store titles are strictly limited to 30 NFC characters.",
        "expected_rules": ["PROD003"],
        "doctype": "app-store-title"
    },
    {
        "id": "prd-app-store-subtitle-limit",
        "category": "app-store",
        "en": "App Store subtitle exceeding 30 characters",
        "bad": "Ứng dụng quản trị tài chính doanh nghiệp toàn diện và tiện lợi",
        "good": "Quản trị tài chính thông minh",
        "diagnosis": "Subtitle exceeds the 30-character platform limit.",
        "why": "App Store subtitles are capped at 30 NFC characters.",
        "expected_rules": ["PROD003"],
        "doctype": "app-store-subtitle"
    },
    {
        "id": "prd-app-store-promo-limit",
        "category": "app-store",
        "en": "App Store promotional text exceeding 170 characters",
        "bad": "Chào mừng bạn đến với phiên bản nâng cấp toàn diện nhất từ trước đến nay của chúng tôi. Chúng tôi đã hoàn thiện toàn bộ tính năng và bổ sung thêm rất nhiều công cụ mới giúp doanh nghiệp tối ưu hoá mọi quy trình vận hành phức tạp.",
        "good": "Khám phá phiên bản mới với hiệu năng vượt trội và giao diện trực quan hơn.",
        "diagnosis": "Promotional text exceeds the 170-character platform limit.",
        "why": "App Store promotional text is strictly limited to 170 NFC characters.",
        "expected_rules": ["PROD003"],
        "doctype": "app-store-promo"
    },
    {
        "id": "prd-consent-without-purpose",
        "category": "legal",
        "en": "Consent copy without purpose statement",
        "bad": "Tôi đồng ý cho phép ứng dụng thu thập dữ liệu cá nhân của tôi.",
        "good": "Tôi đồng ý cho phép ứng dụng thu thập dữ liệu cá nhân nhằm mục đích xác thực tài khoản.",
        "diagnosis": "Consent copy collecting personal data without naming an explicit purpose (Nghị định 13/2023/NĐ-CP).",
        "why": "Nghị định 13/2023/NĐ-CP mandates express, informed consent naming the specific purpose.",
        "expected_rules": ["PROD004"],
        "doctype": "consent"
    },
    {
        "id": "eng-icu-plural-branches",
        "category": "i18n",
        "en": "1 commit / 5 commits",
        "bad": '{"commitCount": "{count, plural, one {# commit} other {# commit}}"}',
        "good": '{"commitCount": "{count, plural, other {# commit}}"}',
        "diagnosis": "ICU plural contains a `one` branch. Vietnamese has only the `other` branch in CLDR.",
        "why": "Vietnamese has no grammatical plural; ICU plural takes strictly `other`.",
        "expected_rules": ["ICU001"],
        "filename": "messages.vi.json"
    },
    {
        "id": "eng-readme-quy-khach",
        "category": "register",
        "en": "SDK installation guide addressing developer as quy khach",
        "bad": "Kính thưa Quý khách, vui lòng chạy lệnh npm install để cài đặt SDK.",
        "good": "Vui lòng chạy lệnh npm install để cài đặt SDK.",
        "diagnosis": "`Quý khách` is a commercial/luxury register, forbidden in developer README documentation.",
        "why": "`Quý khách` sounds servile and out of place in technical documentation; use `bạn` or omit pronoun.",
        "expected_rules": ["PRO002"],
        "register": "eng-readme"
    },
    {
        "id": "eng-unicode-nfd",
        "category": "unicode",
        "en": "Developer documentation encoded in NFD",
        "bad": unicodedata.normalize("NFD", "Hướng dẫn cài đặt công cụ phát triển phần mềm"),
        "good": unicodedata.normalize("NFC", "Hướng dẫn cài đặt công cụ phát triển phần mềm"),
        "diagnosis": "Decomposed Unicode (NFD) diacritics break string indexing and CLI search.",
        "why": "All documentation must be precomposed NFC Unicode.",
        "expected_rules": ["NFC001"]
    },
    {
        "id": "eng-num-dot-decimal",
        "category": "number",
        "en": "System latency reduced by 14.8%",
        "bad": "Độ trễ hệ thống đã giảm 14.8% sau khi tối ưu cache.",
        "good": "Độ trễ hệ thống đã giảm 14,8% sau khi tối ưu cache.",
        "diagnosis": "Period used as a decimal separator instead of comma in Vietnamese prose.",
        "why": "Vietnamese numbers use a comma for decimal fractions (`14,8%`).",
        "expected_rules": ["NUM003"]
    },
    {
        "id": "eng-app-store-superlative",
        "category": "legal",
        "en": "Best app subtitle claim",
        "bad": "Quản lý dự án tốt nhất",
        "good": "Quản lý dự án cho đội nhóm",
        "diagnosis": "Unproven superlative `tốt nhất` in App Store metadata violates Luật Quảng cáo.",
        "why": "Superlatives like `tốt nhất` require official proof documentation under Luật Quảng cáo.",
        "expected_rules": ["LAW001"],
        "doctype": "app-store-subtitle"
    }
]

out_path = Path(__file__).resolve().parent.parent / "evals" / "vietnamese-tech-writing" / "pairs.jsonl"
out_path.parent.mkdir(parents=True, exist_ok=True)
with out_path.open("w", encoding="utf-8") as f:
    for p in pairs:
        f.write(json.dumps(p, ensure_ascii=False) + "\n")

print(f"Generated {len(pairs)} pairs to {out_path}")
