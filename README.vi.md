# DESIGN:OS Vietnamese (`vi-VN`) — Phiên bản v5.0 Đa Ngành Nghề (16 Kỹ Năng)

> **Hệ sinh thái 16 Kỹ năng Ngôn ngữ, Hệ thống Thiết kế Giao diện (Design System), Copywriting Đa Ngành, Sư phạm 7 Bậc học (Mầm non → Tiến sĩ) & Kiểm định Pháp lý Tự động cho AI Agent**
> Xây dựng độc lập trên nền tảng **DESIGN:OS** và chuẩn tri thức **Universal Knowledge Master Contract (`UKMC.v1`)** với 16 kỹ năng chuyên sâu, 31 thanh điệu đối tượng (`registers`), 126 quy tắc kiểm định tĩnh, 489 cặp kiểm thử chuẩn (`golden pairs`) và 18 mô-đun tri thức xác thực mã hóa SHA-256.

[English Documentation (`README.md`)](README.md) · [Trang chủ GitHub Pages](https://jangtrinh.github.io/design-os-vietnamese/) · [Cookbook (`docs/cookbook.md`)](docs/cookbook.md) · [`llms.txt`](llms.txt)

![DESIGN:OS Vietnamese v5.0 Multi-Industry Architecture](assets/design-os-vietnamese-architecture.svg)

---

## Kiến trúc 16 Kỹ năng Chuyên sâu (`skills/`)

1. **[`vn-design-system-ux`](skills/vn-design-system-ux/SKILL.md)**: Design Tokens tiếng Việt, tỉ lệ `line-height` chống cắt dấu tầng (`Ấ, Ệ, Ữ, Ợ`), giới hạn ký tự UI (Button <= 24 [tối đa 28], Tab <= 18, Badge <= 16, Toast <= 90), kiểm định `en.json` ↔ `vi.json`, gắn kết từ ghép cuối câu bằng `U+00A0` (`UX001`–`UX007`).
2. **[`vietnamese-landing-copy`](skills/vietnamese-landing-copy/SKILL.md)**: Copywriting trang đích SaaS, Thương mại điện tử, Bất động sản, Giáo dục; tuân thủ Luật Quảng cáo sửa đổi 2025 (`Luật số 75/2025/QH15`) và Nghị định 98/2020/NĐ-CP (`LND001`–`LND004`).
3. **[`vietnamese-tech-writing`](skills/vietnamese-tech-writing/SKILL.md)**: Tài liệu kỹ thuật, API Reference, Runbook vận hành, Postmortem, ADR và khảo sát sản phẩm (`ENG001`–`ENG008`, `PROD002`–`PROD004`).
4. **[`vietnamese-business-comms`](skills/vietnamese-business-comms/SKILL.md)**: Giao tiếp B2B, Email doanh nghiệp, Zalo OA/ZNS, Tờ trình, Quyết định và Công văn hành chính theo **Nghị định 30/2020/NĐ-CP** & bảo vệ dữ liệu cá nhân **Nghị định 13/2023/NĐ-CP** (`ADMIN001`, `ZNS001`–`ZNS002`, `SALES001`–`SALES004`, `MKT001`–`MKT003`, `SPAM001`).
5. **[`vietnamese-finance-copy`](skills/vietnamese-finance-copy/SKILL.md)**: Ngân hàng số, Fintech, VietQR, Sao kê, Hóa đơn điện tử (**Nghị định 70/2025/NĐ-CP**) và Báo cáo tài chính theo **Thông tư 99/2025/TT-BTC** thay thế Thông tư 200 (`FIN001`–`FIN009`).
6. **[`vietnamese-education-copy`](skills/vietnamese-education-copy/SKILL.md)**: Hệ thống Sư phạm xuyên suốt **7 bậc học từ Mầm non đến Sau đại học (`EDU001`–`EDU012`)**:
   - **Bậc 1 — Giáo dục Mầm non (Nhà trẻ 3–36 tháng & Mẫu giáo 3–6 tuổi — VBHN 01/VBHN-BGDĐT)**: Nhận xét định tính theo 4–5 lĩnh vực phát triển (*Thể chất, Nhận thức, Ngôn ngữ, Tình cảm - Kỹ năng xã hội, Thẩm mỹ*); nghiêm cấm chấm điểm số (`9/10`) hoặc xếp loại học lực (`EDU011`).
   - **Bậc 2 — Giáo dục Tiểu học (Thông tư 27/2020/TT-BGDĐT)**: 3 mức môn học (*Hoàn thành tốt, Hoàn thành, Chưa hoàn thành*), 3 mức phẩm chất/năng lực (*Tốt, Đạt, Cần cố gắng*), 2 danh hiệu (*Học sinh Xuất sắc*, *Học sinh Tiêu biểu*) (`EDU002`).
   - **Bậc 3 — Giáo dục THCS & THPT (Thông tư 22/2021/TT-BGDĐT)**: 4 mức rèn luyện và học tập (*Tốt, Khá, Đạt, Chưa đạt*), bãi bỏ danh hiệu *Học sinh Tiên tiến* (`EDU001`).
   - **Bậc 4 — Giáo dục Nghề nghiệp / TVET (Luật GDNN & Thông tư 04/2022/TT-BLĐTBXH)**: Mô-đun đào tạo nghề, kỹ năng nghề quốc gia bậc 1–5, danh hiệu *Kỹ sư thực hành / Cử nhân thực hành*.
   - **Bậc 5 — Giáo dục Đại học (Thông tư 08/2021/TT-BGDĐT — VQF Bậc 6)**: Đào tạo tín chỉ, chuẩn đầu ra PLO/CLO theo thang Bloom cải tiến, *Khóa luận tốt nghiệp / Đồ án tốt nghiệp*.
   - **Bậc 6 — Sau đại học: Thạc sĩ (Thông tư 23/2021/TT-BGDĐT — VQF Bậc 7)**: Phân biệt định hướng nghiên cứu (*Luận văn thạc sĩ*) và định hướng ứng dụng (*Đề án thạc sĩ*).
   - **Bậc 7 — Sau đại học: Tiến sĩ & Học hàm GS/PGS (Thông tư 18/2021/TT-BGDĐT & QĐ 37/2018/QĐ-TTg — VQF Bậc 8)**: Danh xưng *Nghiên cứu sinh (NCS)*, *Luận án tiến sĩ*, chuẩn công bố quốc tế Web of Science/Scopus, phân biệt nghiêm ngặt *Học vị* (`CN., KS., ThS., TS.`) và *Học hàm / Chức danh* (`GS., PGS.`) (`EDU004`, `EDU008`, `EDU012`).
7. **[`vietnamese-healthcare-copy`](skills/vietnamese-healthcare-copy/SKILL.md)**: Y tế lâm sàng, Bệnh án điện tử EMR (**Luật Khám bệnh, chữa bệnh 2023**, **Thông tư 32/2023/TT-BYT**), Đơn thuốc ngoại trú, Hướng dẫn xuất viện và tuân thủ pháp lý Dược/Thực phẩm bảo vệ sức khỏe (**Nghị định 15/2018/NĐ-CP**) (`MED001`–`MED007`).
8. **[`vietnamese-legal-contracts`](skills/vietnamese-legal-contracts/SKILL.md)**: Soạn thảo Hợp đồng Dân sự (**BLDS 2015**), Hợp đồng Thương mại (**Luật Thương mại 2005** — trần phạt vi phạm 8% theo Điều 301), Thỏa thuận bảo mật NDA, Điều khoản dịch vụ ToS (**Luật Bảo vệ quyền lợi người tiêu dùng 2023**) (`LEG001`–`LEG007`).
9. **[`vietnamese-hospitality-travel`](skills/vietnamese-hospitality-travel/SKILL.md)**: Khách sạn – Resort 5 sao (**Luật Du lịch 2017** Điều 50), minh bạch giá `++` (5% phí phục vụ + 8%/10% thuế GTGT), Hàng không (**Thông tư 14/2015 & 19/2023/TT-BGTVT**), Lữ hành & Ẩm thực cao cấp (`HOS001`–`HOS006`).
10. **[`vietnamese-hr-recruitment`](skills/vietnamese-hr-recruitment/SKILL.md)**: Tuyển dụng nhân sự (JD không phân biệt đối xử theo **Điều 8 Bộ luật Lao động 2019**), Thư mời nhận việc, Hợp đồng lao động (2 loại theo **Điều 20 BLLĐ 2019**), Thử việc (**Điều 25, 26 BLLĐ 2019** — lương >= 85%) và BHXH (**Luật BHXH 41/2024/QH15**) (`HR001`–`HR006`).
11. **[`vietnamese-real-estate-construction`](skills/vietnamese-real-estate-construction/SKILL.md)**: Bất động sản & Xây dựng (**Luật Kinh doanh BĐS 2023** — trần đặt cọc <= 5% Điều 23, tiến độ thanh toán BĐS hình thành trong tương lai <= 30%/70%/95% Điều 25; **Luật Đất đai 2024** — tên chuẩn Giấy chứng nhận & pháp lý condotel/officetel; **Luật Nhà ở 2023** — tách bạch *diện tích thông thủy* vs *tim tường* & 2% kinh phí bảo trì; Hồ sơ mời thầu BOQ **Nghị định 37/2015/NĐ-CP**) (`REA001`–`REA006`).
12. **[`vietnamese-ecommerce-retail`](skills/vietnamese-ecommerce-retail/SKILL.md)**: Thương mại điện tử & Bán lẻ Đa kênh (**Nghị định 52/2013 & 85/2021/NĐ-CP** — phân biệt *Đã thông báo BCT* vs *Đã đăng ký BCT*; **Nghị định 81/2018 & 128/2024/NĐ-CP** — trần khuyến mại 50%; **Luật Bảo vệ quyền lợi người tiêu dùng 2023** — quyền đổi trả/đồng kiểm COD; Nhãn hàng hóa **Nghị định 43/2017 & 111/2021/NĐ-CP**) (`ECOM001`–`ECOM006`).
13. **[`vietnamese-government-public-service`](skills/vietnamese-government-public-service/SKILL.md)**: Dịch vụ công Trực tuyến, Hành chính công & VNeID (**Nghị định 42/2022/NĐ-CP** — 2 mức *DVC trực tuyến toàn trình* và *một phần*; **Luật Căn cước 2023** — danh xưng chuẩn *Thẻ căn cước* & hết hiệu lực CMND 9 số; **Nghị định 69/2024/NĐ-CP** — *VNeID Mức độ 1 / Mức độ 2*; **Luật Cư trú 2020** — nghiêm cấm yêu cầu nộp *Sổ hộ khẩu giấy*) (`GOV001`–`GOV006`).
14. **[`vietnamese-insurance-insurtech`](skills/vietnamese-insurance-insurtech/SKILL.md)**: Bảo hiểm Nhân thọ, Phi nhân thọ, Bancassurance & InsurTech (**Luật Kinh doanh bảo hiểm 2022** & **Thông tư 67/2023/TT-BTC** — cấm đánh tráo bảo hiểm liên kết đầu tư thành tiết kiệm ngân hàng cam kết lãi suất, thời gian cân nhắc 21 ngày Điều 35, giải thích rõ điều khoản loại trừ Điều 19, thời hạn bồi thường 15 ngày Điều 31) (`INS001`–`INS006`).
15. **[`vietnamese-cybersecurity-infosec`](skills/vietnamese-cybersecurity-infosec/SKILL.md)**: An toàn thông tin, An ninh mạng (SOC/VNCERT) & Ứng cứu sự cố dữ liệu cá nhân (**Nghị định 13/2023/NĐ-CP** Điều 23 — thông báo vi phạm dữ liệu cá nhân <= 72 giờ gửi Cục A05 Bộ Công an; **Nghị định 85/2016 & Thông tư 12/2022/TT-BTTTT** — *An toàn hệ thống thông tin Cấp độ 1–5*; chuẩn thuật ngữ CVE/Pentest) (`SEC001`–`SEC006`).
16. **[`vietnamese-media-journalism-pr`](skills/vietnamese-media-journalism-pr/SKILL.md)**: Báo chí, Truyền thông, Thông cáo báo chí & Xử lý khủng hoảng PR (**Luật Báo chí 2016** & **Nghị định 147/2024/NĐ-CP** — phân biệt Cơ quan báo chí vs Trang TTĐT tổng hợp ICP, chuẩn cải chính xin lỗi Điều 42, nguyên tắc suy đoán vô tội *nghi phạm / bị can / bị cáo* Điều 9, bảo vệ trẻ em < 16 tuổi theo **Luật Trẻ em 2016**) (`MEDJ001`–`MEDJ006`).

---

## Kiểm định Tự động & UKMC.v1

```bash
# Kiểm định văn bản tiếng Việt với bộ quy tắc chuyên ngành (hỗ trợ ghép đa ngành --domain finance,legal hoặc --domain all)
python3 shared/scripts/validate_copy.py path/to/file.md --domain edu --register edu-postgrad
python3 shared/scripts/validate_copy.py contract.md --domain finance,insurance,legal,cybersecurity --strict

# Kiểm định danh mục đa nền tảng: JSON, Apple Xcode (.xcstrings) và Android (strings.xml)
python3 shared/scripts/check_i18n_parity.py ios/Localizable.xcstrings --json
python3 shared/scripts/check_i18n_parity.py android/values/strings.xml android/values-vi/strings.xml --json

# Kiểm định tính toàn vẹn tri thức UKMC.v1 (18 module, 65+ neo bằng chứng SHA-256)
python3 tools/verify_ukmc.py

# Chạy toàn bộ kiểm thử tự động (Unit Tests + 489 cặp Golden Evals + Skill Spec + UKMC Gate)
python3 -m unittest discover -s tests -v
```

### Cài đặt dạng lệnh (pip / uvx) và hook pre-commit

Ba công cụ kiểm định cũng cài được như lệnh console, chỉ dùng thư viện chuẩn Python; cờ và mã thoát giống hệt các script ở trên.

| Lệnh | Tương ứng với |
| :--- | :--- |
| `vi-validate-copy` | `shared/scripts/validate_copy.py` |
| `vi-i18n-parity` | `shared/scripts/check_i18n_parity.py` |
| `vi-font-coverage` | `shared/scripts/check_font_coverage.py` |

```bash
pip install git+https://github.com/jangtrinh/design-os-vietnamese
vi-validate-copy path/to/copy.md --domain finance --strict

# hoặc chạy một lần, không cần cài
uvx --from git+https://github.com/jangtrinh/design-os-vietnamese vi-validate-copy path/to/copy.md --domain all
```

Dùng cùng bộ kiểm định dưới dạng hook [pre-commit](https://pre-commit.com) trong repo của bạn (`.pre-commit-config.yaml`); pre-commit tự dựng môi trường cho hook:

```yaml
repos:
  - repo: https://github.com/jangtrinh/design-os-vietnamese
    rev: main   # ghim theo tag phát hành có lệnh vi-* khi tag đó được công bố
    hooks:
      - id: validate-copy
        args: [--domain, ux, --register, ux-microcopy]
      - id: check-i18n-parity
        files: ^locales/(en|vi)\.json$
        pass_filenames: false
        args: [locales/en.json, locales/vi.json]
      - id: check-font-coverage
```

`check-i18n-parity` cần danh mục nguồn đứng trước, đích đứng sau, nhưng pre-commit chỉ truyền các tệp đã staged theo thứ tự đường dẫn; vì vậy `files:` chỉ là điều kiện kích hoạt còn `args:` chỉ rõ cặp nguồn/đích (nguồn trước, ví dụ `values/strings.xml` trước `values-vi/strings.xml` với Android). Mã hook: `validate-copy`, `check-i18n-parity`, `check-font-coverage`.

### Ngữ cảnh viết (`--context`)

`--register` mô hình hóa giọng **tổ chức → khách hàng**. `--context <preset>` mô hình hóa **một người viết cho một người cụ thể**: nhắn tin với bạn bè, email gửi sếp, thư xin việc, tài liệu cho lãnh đạo hoặc cho kỹ sư. Mỗi preset là một bộ năm trục (`relation`, `closeness`, `channel`, `purpose`, `reader`) khai báo trong [`shared/references/context-matrix.md`](shared/references/context-matrix.md). Preset bật các quy tắc `CTX001`–`CTX005` và **tắt** các quy tắc không hợp tình huống; lỗi thật (`NFC001`, `ENC001`, trộn `quý khách`/`bạn` theo `PRO001`) luôn được giữ. Danh sách từ và preset là quy ước, không phải luật (nhóm bằng chứng `proposed`).

| Preset | Tình huống | Quy tắc bật (`CTX`) | Nới lỏng (tắt) |
| :--- | :--- | :--- | :--- |
| `chat-close-friend` | Chat bạn thân | `CTX001` | `DIA001` `CAL001` `LAW001` `SYN001` `NUM002` `NUM004` `TONE001` `CTX003` |
| `chat-colleague` | Chat đồng nghiệp (Slack/Zalo nhóm) | `CTX001` | như trên |
| `chat-to-manager` | Nhắn sếp | `CTX001` `CTX002` `CTX003` | — |
| `email-to-manager` | Email gửi sếp/cấp trên | `CTX001` `CTX002` `CTX003` `CTX004` | — |
| `email-to-colleague` | Email đồng nghiệp | `CTX001` `CTX003` `CTX004` | — |
| `email-to-team` | Email/thông báo cho cấp dưới, cả team | `CTX001` `CTX003` `CTX004` | — |
| `email-to-client` | Email khách hàng/đối tác do cá nhân viết | `CTX001` `CTX003` `CTX004` | — |
| `job-application` | Thư xin việc, email ứng tuyển, CV | `CTX001` `CTX003` `CTX004` | — |
| `doc-for-executives` | Tài liệu/báo cáo cho lãnh đạo | `CTX001` `CTX003` `CTX005` | — |
| `doc-for-engineers` | Tài liệu kỹ thuật cho dev | `CTX001` `CTX003` | — |

| Quy tắc | Kích hoạt khi |
| :--- | :--- |
| `CTX001` | Có từ xưng/hô bị cấm trong ngữ cảnh (`mày/tao/mình/bạn` với cấp trên, `quý khách` trong chat bạn bè). `error` với cấp trên, còn lại `warning`. |
| `CTX002` | Tin nhắn gửi cấp trên có xưng hô trực tiếp (`anh/chị`, `sếp`) nhưng không có từ lễ phép (`ạ`, `dạ`, `vâng`). |
| `CTX003` | Có viết tắt kiểu chat (`ko`, `dc`, `đc`, `mn`, `ae`, `r`, …) ngoài chat bạn thân. `error` trong email/tài liệu gửi cấp trên, còn lại `warning`. |
| `CTX004` | Email không có dòng chào đầu hoặc không có lời kết. |
| `CTX005` | Tài liệu cho lãnh đạo không có dấu hiệu tóm tắt/kết luận (`Tóm tắt`, `Kết luận`, `Đề xuất`, `TL;DR`, …) trong 15 dòng không trống đầu tiên. |

Ba ví dụ (rút gọn từ kết quả thật; `exit` là mã thoát):

```text
$ printf 'Chào sếp,\n\nMình gửi sếp báo cáo tuần này, mai sếp rảnh ko?\n' | vi-validate-copy --context email-to-manager -
<stdin>:3:1: error CTX001  “Mình” does not fit the email-to-manager context (Email gửi sếp/cấp trên)
<stdin>:3:45: error CTX003  chat abbreviation “ko” (không) in the email-to-manager context
(cộng CTX002 thiếu từ lễ phép và CTX004 thiếu lời kết)        # exit 1

$ printf 'Tôi muốn ứng tuyển vị trí Kế toán tổng hợp, bạn xem CV giúp mình.\n' | vi-validate-copy --context job-application -
<stdin>:1:45: error CTX001  “bạn” does not fit the job-application context (Thư xin việc / email ứng tuyển / CV)
<stdin>:1:61: error CTX001  “mình” does not fit the job-application context (Thư xin việc / email ứng tuyển / CV)
(cộng 2 CTX004: thiếu lời chào và lời kết)                    # exit 1

$ printf 'ko biết nha mn, tối nay ae đi ăn ko, mai tao dc nghỉ r\ncam on nha, quán này rẻ nhất Sài Gòn, số 1 luôn\n' | vi-validate-copy --context chat-close-friend -
1 file(s) checked · 0 error(s) · 0 warning(s)                 # exit 0, sạch
# cùng đoạn văn không có --context: DIA001 "cam on", LAW001 "rẻ nhất" và "số 1"
```

Kết hợp: `--context` dùng chung với `--register`, `--domain`, `--doctype`; phần nới lỏng của ngữ cảnh áp dụng sau khi nạp quy tắc theo miền, ngữ nghĩa `--strict` và định dạng JSON không đổi. Preset lạ trả mã thoát `2` kèm danh sách id hợp lệ. Tệp CV đứng riêng không có lời chào/lời kết: thêm `<!-- vlc-disable: CTX004 -->`.

**Gợi ý, không đoán mò.** Khi không có `--context`, công cụ có thể in một dòng gợi ý ra **stderr** nếu có tín hiệu mạnh (ví dụ `Kính gửi anh/chị` cùng `Em xin…` gợi ý `email-to-manager`). Gợi ý không đổi kết quả, JSON trên stdout hay mã thoát, và không bao giờ áp dụng quy tắc theo phỏng đoán.

---

## Giấy phép (License)

Phát hành theo giấy phép [PolyForm Shield License 1.0.0](LICENSE). Bản quyền © 2026 DESIGN:OS (Jang Trinh).
