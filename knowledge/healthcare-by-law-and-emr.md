---
id: "healthcare-by-law-and-emr"
title: "Vietnamese Healthcare & Medical Compliance: Law on Medical Examination 15/2023/QH15, EMR Circular 32/2023/TT-BYT, and Supplement Decree 15/2018/NĐ-CP"
domain: "vietnamese-healthcare-and-pharma"
description: "Verified specification for Vietnamese clinical and healthcare communications under Law 15/2023/QH15, Electronic Medical Records (TT 32/2023/TT-BYT), outpatient prescriptions (TT 52/2017/TT-BYT), and dietary supplement disclaimers (NĐ 15/2018/NĐ-CP)."
when:
  - "Authoring or auditing hospital/clinic patient instructions, EMR notes, prescriptions, or dietary supplement (TPCN) copy"
  - "Enforcing MED001–MED007 rules in validate_copy.py for vietnamese-healthcare-copy"
  - "Verifying medical licensing terminology under the Law on Medical Examination and Treatment 2023"
trust_tier: "verified"
version: "4.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md"
    sha256: "a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed"
---

# Vietnamese Healthcare & Medical Compliance: Law on Medical Examination 15/2023/QH15, EMR Circular 32/2023/TT-BYT, and Supplement Decree 15/2018/NĐ-CP

## Purpose

Defines the statutory and clinical communication standards for Vietnamese hospitals, clinics, telemedicine apps, pharmaceutical disclosures, dietary supplements (`Thực phẩm bảo vệ sức khỏe` — TPCN), and Electronic Medical Records (`Bệnh án điện tử` — EMR).

## When to Use / When NOT

- **When to Use:**
  - Drafting or validating patient discharge instructions (`Giấy ra viện`), outpatient prescriptions (`Đơn thuốc`), EMR clinical notes, clinic landing pages, and dietary supplement product descriptions in Vietnam.
- **When NOT to Use:**
  - Non-medical lifestyle or fitness blog posts that make no diagnostic, therapeutic, or supplement claims.

## Core Knowledge Content

### 1. Law on Medical Examination and Treatment 2023 (`MED003`, `MED006`)

The Law on Medical Examination and Treatment 2023 (Luật Khám bệnh, chữa bệnh số 15/2023/QH15, effective 01/01/2024) officially replaces `Chứng chỉ hành nghề khám bệnh, chữa bệnh` with `Giấy phép hành nghề khám bệnh, chữa bệnh` (valid for 5 years per renewal cycle) and mandates strict patient health data confidentiality under Article 10.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="The Law on Medical Examination and Treatment 2023 (Luật Khám bệnh, chữa bệnh số 15/2023/QH15, effective 01/01/2024) officially replaces 'Chứng chỉ hành nghề khám bệnh, chữa bệnh' with 'Giấy phép hành nghề khám bệnh, chữa bệnh' (valid for 5 years per renewal cycle) and mandates strict patient health data confidentiality under Article 10." -->

### 2. Dietary Supplement (TPCN) Statutory Disclaimers and Prohibitions (`MED001`, `MED002`, `MED005`)

Under Decree 15/2018/NĐ-CP (Article 27) and Circular 05/2018/TT-BYT, all health supplement (`Thực phẩm bảo vệ sức khỏe` — TPCN) advertising and product copy must include the verbatim disclaimer `Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh`, and must never claim therapeutic cure (`điều trị dứt điểm`, `chữa khỏi hoàn toàn`) or use patient thank-you letters or physician/medical-facility imagery for promotional endorsement.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Under Decree 15/2018/NĐ-CP (Article 27) and Circular 05/2018/TT-BYT, all health supplement (Thực phẩm bảo vệ sức khỏe — TPCN) advertising and product copy must include the verbatim disclaimer 'Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh', and must never claim therapeutic cure ('điều trị dứt điểm', 'chữa khỏi hoàn toàn') or use patient thank-you letters or physician/medical-facility imagery for promotional endorsement." -->

### 3. Electronic Medical Records (EMR) and Outpatient Prescriptions (`MED004`, `MED007`)

Circular 32/2023/TT-BYT on Electronic Medical Records (`Bệnh án điện tử` — EMR) and Circular 52/2017/TT-BYT on outpatient prescriptions require explicit drug active ingredient (INN), concentration, dosage per intake, frequency per day, administration route, meal timing (`trước ăn` / `sau ăn`), and emergency red-flag return criteria (`Dấu hiệu cần tái khám ngay`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Circular 32/2023/TT-BYT on Electronic Medical Records (Bệnh án điện tử — EMR) and Circular 52/2017/TT-BYT on outpatient prescriptions require explicit drug active ingredient (INN), concentration, dosage per intake, frequency per day, administration route, meal timing ('trước ăn' / 'sau ăn'), and emergency red-flag return criteria ('Dấu hiệu cần tái khám ngay')." -->

## Failure Modes (Mandatory)

1. **Missing TPCN Statutory Disclaimer (`MED001`):** Publishing a dietary supplement landing page or e-commerce listing without `Thực phẩm này không phải là thuốc và không có tác dụng thay thế thuốc chữa bệnh`.
2. **Curative Claims or Patient Testimonials on TPCN (`MED002`, `MED005`):** Claiming a supplement `chữa khỏi hoàn toàn tiểu đường / xương khớp 100%` or citing `Thư cảm ơn của bệnh nhân Nguyễn Văn A`.
3. **Outdated Medical License Terminology (`MED003`):** Referring to a physician's post-2024 license as `Chứng chỉ hành nghề khám bệnh, chữa bệnh` instead of `Giấy phép hành nghề khám bệnh, chữa bệnh` under Law 15/2023/QH15.
