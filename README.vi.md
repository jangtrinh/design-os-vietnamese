# DESIGN:OS Vietnamese (`design-os-vietnamese`)

> **Hệ sinh thái Kỹ năng Ngôn ngữ, Typography, UX Writing, Tuân thủ Pháp lý Việt Nam & Cơ sở Tri thức chuẩn UKMC.v1 dành cho AI Agent và Design System.**
>
> Xây dựng và phát triển độc lập bởi **Jang Trinh / DESIGN:OS** (`https://github.com/jangtrinh/design-os-vietnamese`).

[English Documentation (`README.md`)](README.md)

---

## Tổng quan Kiến trúc

**DESIGN:OS Vietnamese** giải quyết triệt để các lỗi cố hữu khi AI sinh nội dung và giao diện tiếng Việt trong môi trường sản phẩm thực tế (Production):

1. **Loại bỏ văn phong dịch máy (Calque & Ngữ dụng học — `CAL001`, `SYN001`, `PRO001`):** Chặn các cấu trúc dịch từng từ từ tiếng Anh (*"Làm ơn nhập của bạn mật khẩu"*, *"Đơn hàng bị hủy thành công"*), chuẩn hóa 18 ngữ vực xưng hô (`register-matrix.md`) và bảo vệ các từ ghép Hán-Việt/thuần Việt (`bạn bè`, `bạn đọc`, `kết bạn`, `quý giá`, `Quý I/II/III/IV`) khỏi bị nhận diện nhầm là đại từ.
2. **Kỹ thuật Typography & Dấu chồng tầng (`Ẫ, Ễ, Ổ, Ữ, Ệ, Ộ`):** Thiết lập ngưỡng `line-height` tối thiểu (`1.5` cho văn bản thân, `1.28–1.35` cho tiêu đề lớn), kiểm tra bảng `cmap` nhị phân của file font `.ttf`/`.otf` đủ 134 nguyên âm tiếng Việt + `Đ/đ` + `₫` (`check_font_coverage.py`), và dự phòng độ giãn nở chiều ngang `+20%` đến `+35%`.
3. **Chuẩn hóa Unicode NFC, Bảng mã cũ & Bộ gõ Telex/VNI (`NFC001`, `ENC001`, `TONE001`):** Tự động chuẩn hóa chuỗi tổ hợp NFD từ macOS Finder/Google Docs về NFC dựng sẵn, phát hiện lỗimojibake UTF-8 kép (`Ã¡`, `á»‡`) và bảng mã TCVN3/VNI/CP1258, đồng bộ quy tắc đặt dấu thanh `oa/oe/uy` theo Quyết định 1989/QĐ-BGDĐT (`--fix-tone new|old`), và hướng dẫn xử lý `isComposing` cho bộ gõ Telex/VNI trên React/Web.
4. **Định dạng Bản địa `vi-VN` & Đa dòng ICU MessageFormat (`NUM001–NUM004`, `ICU001`, `ICU002`):** Kiểm tra phân tách hàng nghìn bằng dấu chấm (`.`), thập phân bằng dấu phẩy (`,`), phát hiện nhánh số nhiều `one`/`few`/`many` thừa trong khối ICU nhiều dòng, và phân biệt thông minh tên chip phần cứng (`Apple M2`, `MacBook Air M2`, `M3 Max`) với đơn vị diện tích/thể tích (`m²`, `m³`).
5. **Tuân thủ Pháp lý Việt Nam hiện hành (2025–2026):**
   - **Luật Quảng cáo 2012 & Luật sửa đổi số 75/2025/QH15** (hiệu lực `01/01/2026`): Cấm dùng từ so sánh tuyệt đối (`nhất`, `duy nhất`, `tốt nhất`, `số 1`) không có tài liệu chứng minh và bắt buộc gắn nhãn tài trợ đối với KOL/KOC.
   - **Nghị định 13/2023/NĐ-CP (PDPD):** Yêu cầu sự đồng ý tường minh đủ 6 yếu tố và xác thực đồng thời của cả cha mẹ lẫn trẻ em từ `7` đến dưới `16` tuổi (Điều 20).
   - **Thông tư 99/2025/TT-BTC** (thay thế Thông tư 200/2014/TT-BTC từ `01/01/2026`): Đổi tên *Bảng cân đối kế toán* thành **Báo cáo tình hình tài chính**, bổ sung TK `215` (Tài sản sinh học), TK `332` (Phải trả cổ tức, lợi nhuận) và TK `82112` (Thuế TNDN bổ sung theo thuế tối thiểu toàn cầu Pillar Two).
   - **Thông tư 22/2021/TT-BGDĐT (Chương trình GDPT 2018):** Chuẩn hóa 4 mức đánh giá học tập và rèn luyện **Tốt — Khá — Đạt — Chưa đạt** (thay thế *Học lực Giỏi/Tiên tiến/Yếu/Kém* cũ) và Khung năng lực ngoại ngữ 6 bậc dùng cho Việt Nam (Thông tư 01/2014/TT-BGDĐT).
   - **Nghị định 30/2020/NĐ-CP & Nghị định 91/2020/NĐ-CP:** Chuẩn hóa thể thức văn bản hành chính (`Công văn`, `Tờ trình`, `Quyết định`, `Biên bản`) và quy tắc chống tin nhắn rác trên Zalo ZNS / Brandname SMS.

---

## Danh mục 6 Kỹ năng Chuyên sâu (`skills/`)

1. **[`vn-design-system-ux`](skills/vn-design-system-ux/SKILL.md):** UX Writing, Microcopy cho mọi trạng thái giao diện, Design Tokens tiếng Việt (`Be Vietnam Pro`), kiểm tra độ phủ font và đối soát song ngữ `en.json` / `vi.json`.
2. **[`vietnamese-landing-copy`](skills/vietnamese-landing-copy/SKILL.md):** Landing page SaaS & Thương mại điện tử, công thức tiêu đề Hero/CTA, bảng giá VND, tuân thủ Luật Quảng cáo & Nghị định khuyến mại 81/2018 + 128/2024.
3. **[`vietnamese-tech-writing`](skills/vietnamese-tech-writing/SKILL.md):** Tài liệu kỹ thuật, API Reference, ADR, Runbook, Post-mortem/RCA, Changelog và quy tắc pha trộn thuật ngữ Anh–Việt (code-switching).
4. **[`vietnamese-business-comms`](skills/vietnamese-business-comms/SKILL.md):** Văn bản hành chính chuẩn Nghị định 30/2020/NĐ-CP (`Công văn`, `Tờ trình`, `Quyết định`, `Thông báo`, `Biên bản`), email B2B và mẫu tin nhắn Zalo ZNS.
5. **[`vietnamese-finance-copy`](skills/vietnamese-finance-copy/SKILL.md):** Ngân hàng số, chuyển tiền Napas 247 / VietQR, chứng khoán, bảo hiểm, kế toán doanh nghiệp theo Thông tư 99/2025/TT-BTC và quy tắc đọc số tiền bằng chữ.
6. **[`vietnamese-education-copy`](skills/vietnamese-education-copy/SKILL.md):** EdTech, hệ thống LMS, học bạ số phổ thông theo Thông tư 22/2021/TT-BGDĐT, đề cương đại học và chuẩn KNLNN 6 bậc (VSTEP).

---

## Hướng dẫn Sử dụng Nhanh

```bash
# 1. Kiểm tra văn bản với bộ máy validate_copy.py v3.0
python3 shared/scripts/validate_copy.py du-ong-dan/file.md --domain ux --register ux-microcopy

# 2. Tự động sửa lỗi Unicode NFD, ký hiệu m²/m³ và đồng bộ dấu thanh kiểu mới (hoà, thuỷ)
python3 shared/scripts/validate_copy.py du-ong-dan/file.md --fix --fix-tone new

# 3. Kiểm tra toàn bộ 8 học phần tri thức UKMC.v1 và cổng dừng epistemic
PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli verify knowledge --claims

PYTHONPATH=/Users/jangtrinh/Products/design-os-knowledge-builder/src \
  python3 -m knowledge_builder.cli gate --root knowledge --run-id vn-design-os-261026

# 4. Chạy toàn bộ bộ kiểm thử tự động
python3 -m unittest discover -s tests -v
```

## Bản quyền

Phát hành theo giấy phép [MIT License](LICENSE). Bản quyền (c) 2026 Jang Trinh / DESIGN:OS.
