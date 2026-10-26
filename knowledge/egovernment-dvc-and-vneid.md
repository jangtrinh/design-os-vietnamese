---
id: "egovernment-dvc-and-vneid"
title: "Vietnamese E-Government, Public Services (DVC), VNeID Digital Identity & Residence Administration"
domain: "vietnamese-government-and-public-service"
description: "Verified specification for Vietnamese digital public services under Decree 42/2022/NĐ-CP, VNeID electronic identification under Law on Identification 26/2023/QH15 and Decree 69/2024/NĐ-CP, and residence verification under Law on Residence 68/2020/QH14 and Decree 104/2022/NĐ-CP."
when:
  - "Authoring or auditing online public service (DVC) instructions, administrative procedures (TTHC), citizen portal notices, and VNeID integration copy"
  - "Enforcing GOV001–GOV006 rules in validate_copy.py for vietnamese-government-public-service"
  - "Verifying identity document and residence terminology under current Vietnamese administrative legislation"
trust_tier: "verified"
version: "5.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md"
    sha256: "a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4"
---

# Vietnamese E-Government, Public Services (DVC), VNeID Digital Identity & Residence Administration

## Purpose

Defines statutory standards and communication protocols for Vietnamese national and provincial digital public service portals (Cổng Dịch vụ công Quốc gia & Cổng Dịch vụ công cấp Bộ/Tỉnh), administrative procedure guides (TTHC), VNeID electronic identification, citizen identity card documentation, and residence verification.

## When to Use / When NOT

- **When to Use:**
  - Authoring or auditing procedural guides for administrative procedures (TTHC) published on the National Public Service Portal or ministerial/provincial information systems.
  - Composing citizen-facing notifications, SMS alerts, and email status updates regarding administrative dossier submission, processing, fee payment, and result delivery.
  - Designing UI/UX flows and copy for VNeID authentication (SSO, Level 1, Level 2) and identity verification across public and private sector systems.
  - Ensuring adherence to the complete abolition of paper household registration books (Sổ hộ khẩu giấy, Sổ tạm trú giấy) under Law on Residence 2020 and Decree 104/2022/NĐ-CP.
- **When NOT to Use:**
  - Pure internal government classified correspondence not accessible to citizens or businesses.
  - Commercial B2B contracts unrelated to public administrative procedures.

## Core Knowledge Content

### 1. Two Statutory Tiers of Online Public Services under Decree 42/2022/NĐ-CP (`GOV001`, `GOV005`)

Article 11 of Decree 42/2022/NĐ-CP replaces legacy 4-tier online public service classifications ('Dịch vụ công trực tuyến mức độ 1, 2, 3, 4') with exactly two statutory tiers: 'Dịch vụ công trực tuyến toàn trình' (full-process online public service) and 'Dịch vụ công trực tuyến một phần' (partial online public service).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Article 11 of Decree 42/2022/NĐ-CP replaces legacy 4-tier online public service classifications ('Dịch vụ công trực tuyến mức độ 1, 2, 3, 4') with exactly two statutory tiers: 'Dịch vụ công trực tuyến toàn trình' (full-process online public service) and 'Dịch vụ công trực tuyến một phần' (partial online public service)." -->

### 2. Identity Document Evolution, VNeID Classification, and Residence Verification (`GOV002`, `GOV003`, `GOV004`)

Under the Law on Identification 2023 (Luật Căn cước số 26/2023/QH15, effective 01/07/2024), newly issued cards are titled 'Thẻ căn cước' and legacy 9-digit 'Chứng minh nhân dân (CMND)' cards expired after 31/12/2024; under Decree 69/2024/NĐ-CP on electronic identification and authentication, VNeID accounts are classified into Level 1 ('Tài khoản định danh điện tử mức độ 1') and Level 2 ('Tài khoản định danh điện tử mức độ 2'), while the Law on Residence 2020 (Luật Cư trú số 68/2020/QH14) and Decree 104/2022/NĐ-CP prohibit requiring citizens to submit paper household registration books ('Sổ hộ khẩu giấy' or 'Sổ tạm trú giấy').
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/06-realestate-ecommerce-gov-insurance-cybersecurity-media-corpus.md" sha256="a5c5e96f885071c71a06f446536365f5cbf3b116d53006875351bbe6130598c4" quote="Under the Law on Identification 2023 (Luật Căn cước số 26/2023/QH15, effective 01/07/2024), newly issued cards are titled 'Thẻ căn cước' and legacy 9-digit 'Chứng minh nhân dân (CMND)' cards expired after 31/12/2024; under Decree 69/2024/NĐ-CP on electronic identification and authentication, VNeID accounts are classified into Level 1 ('Tài khoản định danh điện tử mức độ 1') and Level 2 ('Tài khoản định danh điện tử mức độ 2'), while the Law on Residence 2020 (Luật Cư trú số 68/2020/QH14) and Decree 104/2022/NĐ-CP prohibit requiring citizens to submit paper household registration books ('Sổ hộ khẩu giấy' or 'Sổ tạm trú giấy')." -->

## Failure Modes (Mandatory)

1. **Obsolete 4-Tier Public Service Classification (`GOV001`):** Citing `mức độ 3`, `mức độ 4`, `DVC mức 3`, or `DVC mức 4` instead of `toàn trình` or `một phần` under Decree 42/2022/NĐ-CP.
2. **Invalid Identity Card Currency (`GOV002`):** Demanding submission of 9-digit CMND cards after their statutory expiration date (31/12/2024), or referencing `cấp mới thẻ CCCD gắn chip` instead of `Thẻ căn cước` under Law 26/2023/QH15.
3. **Fabricated VNeID Levels (`GOV003`):** Promising or requiring `VNeID mức độ 3`, `cấp 3`, or `hạng vàng`.
4. **Demanding Paper Household Registration (`GOV004`):** Requiring `Sổ hộ khẩu giấy` or `Sổ tạm trú giấy` in violation of Law on Residence 2020 and Decree 104/2022/NĐ-CP.
5. **Incomplete TTHC Procedure Guide (`GOV005`):** Omitting `Trình tự thực hiện`, `Thành phần hồ sơ`, or `Thời hạn giải quyết` in `doctype == "dvc-guide"`.
6. **Bureaucratic Coercion and Administrative Calques (`GOV006`):** Scolding citizens or using unvetted English translationese on public service interfaces.
