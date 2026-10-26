---
name: vietnamese-government-public-service
description: Drafts, localizes, and audits Vietnamese e-government communications, online public service portals (DVC toàn trình & một phần), administrative procedure guides (TTHC), VNeID electronic identity notifications, and citizen status updates. Enforces Decree 42/2022/NĐ-CP public service classifications, Law on Identification 2023 (Luật Căn cước 26/2023/QH15) and Decree 69/2024/NĐ-CP (VNeID Level 1 and Level 2), abolition of paper household books under Law on Residence 2020 (Luật Cư trú 68/2020/QH14) and Decree 104/2022/NĐ-CP, and administrative clerical standards under Decree 30/2020/NĐ-CP.
version: "5.0.0"
license: PolyForm-Shield-1.0.0
metadata:
  author: "DESIGN:OS Vietnamese"
  repository: "https://github.com/jangtrinh/design-os-vietnamese"
---

# Vietnamese E-Government, Public Services (DVC) & VNeID Identity (`vietnamese-government-public-service`)

In Vietnamese digital governance, administrative instructions and citizen notifications carry **strict statutory mandates and administrative accountability**. Using obsolete 4-tier public service classifications violates Decree 42/2022/NĐ-CP; demanding paper household registration books violates Article 38 of the Law on Residence 2020 and Decree 104/2022/NĐ-CP; referencing 9-digit CMND cards or fabricated VNeID levels breaches the Law on Identification 2023 and Decree 69/2024/NĐ-CP; and bureaucratic scolding violates Decree 30/2020/NĐ-CP on clerical etiquette.

This skill equips digital government product owners, software engineers, civil servants, and technical writers with authoritative, statutory Vietnamese public administration phrasing, procedural structures, and linter automation aligned with current Vietnamese administrative legislation.

---

## 1. Register & Sociolinguistic Etiquette

Administrative documents, public service portals, and citizen notifications operate under formal public administration standards:

| Document / Surface | Register | Address (`Hô`) | Speaker (`Xưng`) | Notes |
|---|---|---|---|---|
| Public Service Guide (`dvc-guide`) | `public-admin` | `Công dân` / `Tổ chức` | `Cơ quan có thẩm quyền` / `Bộ phận Một cửa` | Objective, courteous administrative tone; no casual pronouns (`bạn`, `mình`) |
| VNeID & Identity Notice (`vneid-notice`) | `public-admin` | `Công dân` | `Cục Cảnh sát QLHC về TTXH` / `Hệ thống VNeID` | Precise statutory identity card and account level terminology |
| Citizen Notification (`citizen-notification`) | `formal-notice` | `Ông/Bà` / `Quý công dân` | `Bộ phận tiếp nhận và trả kết quả` | Transparent dossier progress, explicit deadlines, courteous administrative guidance |

---

## 2. Supported Document Types (`DOCTYPES`)

The linter dynamically configures domain-specific statutory checks based on declared `--doctype`:

| Doctype Slug | Vietnamese Title & Statutory Scope | Key Statutory Checks |
|---|---|---|
| `dvc-guide` | Hướng dẫn Thủ tục hành chính (TTHC) trên Cổng Dịch vụ công Quốc gia (Nghị định 42/2022/NĐ-CP) | `GOV001` (toàn trình vs một phần), `GOV005` (đủ Trình tự, Hồ sơ, Thời hạn) |
| `vneid-notice` | Thông báo định danh điện tử VNeID & Thẻ căn cước (Luật Căn cước 2023 & Nghị định 69/2024/NĐ-CP) | `GOV002` (Thẻ căn cước, hết hạn CMND 9 số), `GOV003` (chỉ có Mức độ 1 & 2) |
| `citizen-notification` | Thông báo giải quyết hồ sơ hành chính gửi công dân / tổ chức (Nghị định 30/2020/NĐ-CP) | `GOV004` (cấm đòi Sổ hộ khẩu giấy), `GOV006` (cấm quát nạt, chuẩn hóa thuật ngữ) |

---

## 3. End-to-End Workflow

To produce compliant administrative copy and public service guidelines under Vietnamese law, follow this 5-stage workflow:

1. **Stage 1: Doctype Classification & Statutory Scope Determination:**
   - Determine whether the copy is an administrative procedure guide (`dvc-guide`), an identity notice (`vneid-notice`), or an individual dossier notification (`citizen-notification`).
   - Reference the governing statute (Decree 42/2022/NĐ-CP for online public services, Law 26/2023/QH15 for identification, Law 68/2020/QH14 for residence).
2. **Stage 2: Register Enforcement & Civil Service Etiquette:**
   - Establish consistent formal administrative address (`Công dân`, `Ông/Bà`, `Tổ chức`).
   - Strictly prohibit bureaucratic scolding, condescending warnings, or coercive threats (`GOV006`).
3. **Stage 3: Terminology Currency Verification:**
   - Classify online services strictly as `toàn trình` or `một phần` under Article 11 Decree 42/2022/NĐ-CP (`GOV001`).
   - Standardize identity cards as `Thẻ căn cước`, eliminate 9-digit CMND references after 31/12/2024 (`GOV002`).
   - Standardize VNeID accounts to Level 1 and Level 2 (`GOV003`).
4. **Stage 4: Elimination of Paper Residence Dossiers:**
   - Eliminate all requirements for citizens to submit, notarize, or present `Sổ hộ khẩu giấy` or `Sổ tạm trú giấy` (`GOV004`).
   - Provide electronic verification alternatives: VNeID Level 2, National Population Database sync, or Form CT07.
5. **Stage 5: Automated Linter & Pre-Publication Gate:**
   - Run `validate_copy.py` with `--domain vietnamese-government-public-service` and `--doctype`.

---

## 4. Statutory Regulations & Transition Guidelines

Public service administrators and engineering teams must enforce modern Vietnamese administrative legislation:

1. **Abolition of Legacy 4-Tier Public Services (`GOV001`):**
   - Under **Điều 11 Nghị định 42/2022/NĐ-CP**, public services are classified into **Dịch vụ công trực tuyến toàn trình** (entire workflow online) and **Dịch vụ công trực tuyến một phần** (partial workflow online).
   - The former 4-tier model (mức độ 1, 2, 3, 4) is obsolete and legally replaced.
2. **Identity Document Currency (`GOV002`):**
   - Under **Luật Căn cước số 26/2023/QH15** (effective 01/07/2024), new cards are titled **Thẻ căn cước**.
   - Legacy 9-digit CMND cards officially expired on **31/12/2024**; administrative portals cannot accept 9-digit CMND as valid ID.
3. **VNeID Electronic Identification Levels (`GOV003`):**
   - Under **Nghị định 69/2024/NĐ-CP**, electronic identification consists of strictly **Tài khoản định danh điện tử mức độ 1** (self-registered via NFC/face) and **Tài khoản định danh điện tử mức độ 2** (registered at police station, biometric verified).
   - Fabricated tiers such as Level 3, Level 4, or "hạng vàng" are illegal.
4. **Paper Household Registration Abolition (`GOV004`):**
   - Under **Điều 38 Luật Cư trú 2020** and **Nghị định 104/2022/NĐ-CP**, paper household books (`Sổ hộ khẩu giấy`, `Sổ tạm trú giấy`) have been invalid since 01/01/2023.
   - Demanding citizens present or submit paper household registration is strictly prohibited.

---

## 5. Administrative Communication & Clerical Standards (NĐ 30/2020/NĐ-CP)

1. **Civic Service Etiquette (`GOV006`):**
   - Public service portals must eliminate bureaucratic bullying, coercive language, or scolding (e.g. `Công dân tự chịu hoàn toàn hậu quả nếu không biết thao tác`, `Cấm hỏi nhiều tại quầy một cửa`).
2. **Public Administration Terminology (`GOV006`):**
   - Replace literal translationese with standard Vietnamese terms:
     - `Dịch vụ công trực tuyến` (never `Dịch vụ công cộng trên đường dây`)
     - `Bộ phận Một cửa` / `Trung tâm Phục vụ hành chính công` (never `Cửa hàng một điểm dừng`)
     - `Bộ phận tiếp nhận và trả kết quả` (never `Bàn dịch vụ công dân`)

---

## 6. Deterministic Rule Reference

- `GOV001`: Obsolete 4-tier online public service terminology (`Dịch vụ công trực tuyến mức độ 1/2/3/4`, `DVC mức 3/4`) replaced under Decree 42/2022/NĐ-CP.
- `GOV002`: Outdated identity card terminology (`Chứng minh nhân dân 9 số còn hiệu lực`, `nộp bản sao CMND 9 số`, `cấp mới thẻ CCCD gắn chip`) without noting transition to `Thẻ căn cước`.
- `GOV003`: Invalid VNeID electronic identity level (`VNeID mức độ 3`, `VNeID mức độ 4`, `Tài khoản định danh điện tử cấp 3`, `VNeID hạng vàng`).
- `GOV004`: Unlawful requirement demanding paper household registration books (`Sổ hộ khẩu giấy`, `Sổ tạm trú giấy`) abolished under Law on Residence 2020.
- `GOV005`: Administrative procedure guide (`doctype == dvc-guide`) missing mandatory statutory TTHC fields (`Trình tự thực hiện`, `Thành phần hồ sơ`, `Thời hạn giải quyết`).
- `GOV006`: Bureaucratic scolding, coercive threats, or machine-translated administrative calques.

---

## 7. Bundled References

- [references/dvc-truc-tuyen-nd42-2022.md](references/dvc-truc-tuyen-nd42-2022.md) — Decree 42/2022/NĐ-CP 2-tier online public service classification and mandatory TTHC guide fields.
- [references/luat-can-cuoc-2023-va-vneid-nd69.md](references/luat-can-cuoc-2023-va-vneid-nd69.md) — Law on Identification 2023 card terminology and Decree 69/2024/NĐ-CP VNeID Level 1 & Level 2 standards.
- [references/luat-cu-tru-bo-so-ho-khau-giay.md](references/luat-cu-tru-bo-so-ho-khau-giay.md) — Law on Residence 2020 and Decree 104/2022/NĐ-CP abolition of paper household books and electronic verification channels.
