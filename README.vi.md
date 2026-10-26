# DESIGN:OS Vietnamese (`vi-VN`) — Phiên bản v4.0 Đa Ngành Nghề

> **Hệ sinh thái Kỹ năng Ngôn ngữ, Hệ thống Thiết kế Giao diện (Design System), Copywriting Đa Ngành, Sư phạm 7 Bậc học (Mầm non → Tiến sĩ) & Kiểm định Pháp lý Tự động cho AI Agent**
> Xây dựng độc lập trên nền tảng **DESIGN:OS** và chuẩn tri thức **Universal Knowledge Master Contract (`UKMC.v1`)**.

[English Documentation (`README.md`)](README.md)

![DESIGN:OS Vietnamese v4.0 Multi-Industry Architecture](assets/design-os-vietnamese-architecture.svg)

---

## Kiến trúc 10 Kỹ năng Chuyên sâu (`skills/`)

1. **[`vn-design-system-ux`](skills/vn-design-system-ux/SKILL.md)**: Design Tokens tiếng Việt, tỉ lệ `line-height` chống cắt dấu tầng (`Ấ, Ệ, Ữ, Ợ`), giới hạn ký tự UI (Button <= 28, Tab <= 18, Badge <= 16, Toast <= 90), kiểm định `en.json` ↔ `vi.json`, gắn kết từ ghép cuối câu bằng `U+00A0` (`UX001`–`UX010`).
2. **[`vietnamese-landing-copy`](skills/vietnamese-landing-copy/SKILL.md)**: Copywriting trang đích SaaS, Thương mại điện tử, Bất động sản, Giáo dục; tuân thủ Luật Quảng cáo sửa đổi 2025 (`Luật số 75/2025/QH15`) và Nghị định 98/2020/NĐ-CP (`LND001`–`LND007`).
3. **[`vietnamese-tech-writing`](skills/vietnamese-tech-writing/SKILL.md)**: Tài liệu kỹ thuật, API Reference, Runbook vận hành, Postmortem, ADR và khảo sát sản phẩm (`TECH001`–`TECH006`).
4. **[`vietnamese-business-comms`](skills/vietnamese-business-comms/SKILL.md)**: Giao tiếp B2B, Email doanh nghiệp, Zalo OA/ZNS, Tờ trình, Quyết định và Công văn hành chính theo **Nghị định 30/2020/NĐ-CP** & bảo vệ dữ liệu cá nhân **Nghị định 13/2023/NĐ-CP** (`BIZ001`–`BIZ007`).
5. **[`vietnamese-finance-copy`](skills/vietnamese-finance-copy/SKILL.md)**: Ngân hàng số, Fintech, VietQR, Sao kê, Hóa đơn điện tử (**Nghị định 70/2025/NĐ-CP**) và Báo cáo tài chính theo **Thông tư 99/2025/TT-BTC** thay thế Thông tư 200 (`FIN001`–`FIN006`).
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

---

## Kiểm định Tự động & UKMC.v1

```bash
# Kiểm định văn bản tiếng Việt với bộ quy tắc chuyên ngành
python3 shared/scripts/validate_copy.py path/to/file.md --domain edu --register edu-postgrad

# Kiểm định tính toàn vẹn tri thức UKMC.v1 (12 module, 53 neo bằng chứng SHA-256)
python3 tools/verify_ukmc.py

# Chạy toàn bộ тест tự động (Unit Tests + 310+ cặp Golden Evals + Skill Spec + UKMC Gate)
python3 -m unittest discover -s tests -v
```

---

## Giấy phép (License)

Phát hành theo giấy phép [PolyForm Shield License 1.0.0](LICENSE). Bản quyền © 2026 DESIGN:OS (Jang Trinh).
