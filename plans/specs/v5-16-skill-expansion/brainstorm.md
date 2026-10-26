# Brainstorm — DESIGN:OS Vietnamese v5.0: 16-Skill Multi-Industry Expansion (`v5-16-skill-expansion`)

## 1. Press Release (Working Backwards)
**Headline**: **DESIGN:OS Vietnamese v5.0** expands from 10 to **16 Sovereign Production Skills**, **31 Audience Registers**, **126 Deterministic AST/Regex Rules**, **18 UKMC.v1 Cryptographic Knowledge Modules**, and **489 Golden Evaluation Pairs**, adding full statutory & linguistic coverage for **Real Estate & Construction**, **E-Commerce & Retail**, **Government & Public Services (DVC / VNeID)**, **Insurance & InsurTech**, **Cybersecurity & InfoSec (SOC / PDPD)**, and **Media, Journalism & Crisis PR**.

## 2. Six New Regulated Industry Skills

| # | Skill Slug | `--domain` Aliases | Rule IDs | Core Vietnamese Statutory & Technical Basis |
|---|---|---|---|---|
| 11 | `vietnamese-real-estate-construction` | `realestate`, `construction` | `REA001`–`REA006` | Luật Kinh doanh BĐS 2023 (Đặt cọc <= 5% Đ23, Thanh toán <= 30%/70%/95% Đ25), Luật Nhà ở 2023 (Diện tích thông thủy vs tim tường Đ141, Phí bảo trì 2% Đ152), Luật Đất đai 2024 (Giấy chứng nhận Đ134), NĐ 37/2015 Hợp đồng xây dựng / BOQ |
| 12 | `vietnamese-ecommerce-retail` | `ecommerce`, `retail` | `ECOM001`–`ECOM006` | NĐ 52/2013 & NĐ 85/2021 TMĐT (Đã thông báo vs Đã đăng ký BCT), NĐ 81/2018 & NĐ 128/2024 (Trần khuyến mại 50%), Luật BVQLNTD 2023 (Đổi trả / Đồng kiểm COD), NĐ 43/2017 & NĐ 111/2021 Nhãn hàng hóa |
| 13 | `vietnamese-government-public-service` | `gov`, `public-service` | `GOV001`–`GOV006` | NĐ 42/2022 (2 mức DVC: Toàn trình & Một phần, bỏ mức 1–4), Luật Căn cước 2023 (Thẻ căn cước từ 01/07/2024, CMND 9 số hết hiệu lực), NĐ 69/2024 (VNeID Mức 1/2), Luật Cư trú 2020 & NĐ 104/2022 (Bỏ Sổ hộ khẩu giấy / CT07) |
| 14 | `vietnamese-insurance-insurtech` | `insurance`, `insurtech` | `INS001`–`INS006` | Luật Kinh doanh bảo hiểm 2022 & TT 67/2023/TT-BTC (Cấm đánh tráo BH liên kết đầu tư thành tiết kiệm ngân hàng, Thời gian cân nhắc 21 ngày Đ35, Giải thích loại trừ trách nhiệm Đ19, Bồi thường 15 ngày Đ31, 4 chủ thể hợp đồng BH) |
| 15 | `vietnamese-cybersecurity-infosec` | `cybersecurity`, `infosec` | `SEC001`–`SEC006` | NĐ 13/2023/NĐ-CP (Báo cáo vi phạm dữ liệu cá nhân <= 72 giờ cho Cục A05 Đ23, Dữ liệu cơ bản vs nhạy cảm Đ2), NĐ 85/2016 & TT 12/2022/TT-BTTTT (An toàn HTTT Cấp độ 1–5), QĐ 05/2017/QĐ-TTg (VNCERT/CC), chuẩn thuật ngữ SOC/Pentest |
| 16 | `vietnamese-media-journalism-pr` | `media`, `journalism`, `pr` | `MEDJ001`–`MEDJ006` | Luật Báo chí 2016 (Cải chính & xin lỗi Đ42, Suy đoán vô tội: nghi phạm/bị can/bị cáo Đ9), Luật Trẻ em 2016 (Bảo vệ thông tin trẻ em < 16 tuổi), NĐ 147/2024/NĐ-CP (ICP vs Báo chí), chuẩn Thông cáo báo chí & Xử lý khủng hoảng |

## 3. MoSCoW Scope
- **Must Have**:
  - 6 new skill directories under `skills/<slug>/` with `SKILL.md`, `scripts/rules_<domain>.py`, `scripts/{validate_copy.py,check_font_coverage.py,check_i18n_parity.py}`, `references/{glossary.md,banned-phrases.md,register-matrix.md,unicode-and-tone.md,typography-and-layout.md,<domain-reference>.md}`, and `examples/good-vs-bad.md`.
  - 6 new evaluation suites under `evals/<slug>/pairs.jsonl` (25 golden pairs each = +150 pairs, 489 total).
  - 6 new `UKMC.v1` verified knowledge modules under `knowledge/<module>.md` (18 modules total, passing `tools/verify_ukmc.py` with `STOP_SUFFICIENT`).
  - Full integration into `shared/scripts/validate_copy.py`, `tools/sync_shared.py`, `tools/build_examples.py`, `scripts/self_check.py`, plugin manifests, `README.md`, `README.vi.md`, `docs/index.html`, `docs/cookbook.md`, `llms.txt`, and `docs/llms.txt`.
