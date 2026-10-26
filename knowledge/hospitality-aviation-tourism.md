---
id: "hospitality-aviation-tourism"
title: "Vietnamese Hospitality, Tourism, Aviation & F&B Standards: Law on Tourism 2017 and Circular 19/2023/TT-BGTVT"
domain: "vietnamese-hospitality-and-travel"
description: "Verified specification for Vietnamese hotel/resort star ratings (Law on Tourism 2017 Article 50), ++ service charge and VAT pricing transparency, and aviation delay/cancellation notices (Circulars 14/2015 & 19/2023/TT-BGTVT)."
when:
  - "Writing or auditing hotel/resort booking confirmations, room descriptions, tour itineraries, flight notifications, or fine-dining F&B menus"
  - "Enforcing HOS001–HOS006 rules in validate_copy.py for vietnamese-hospitality-travel"
  - "Formatting Net vs ++ pricing with explicit 5% service charge and 8%/10% VAT disclosures"
trust_tier: "verified"
version: "4.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md"
    sha256: "a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed"
---

# Vietnamese Hospitality, Tourism, Aviation & F&B Standards: Law on Tourism 2017 and Circular 19/2023/TT-BGTVT

## Purpose

Defines the statutory and service-excellence standards for Vietnamese hotels, resorts, travel agencies, airlines, and fine-dining F&B establishments.

## When to Use / When NOT

- **When to Use:**
  - Auditing hotel booking confirmations, resort landing pages, tour itineraries, airline delay/cancellation messages, and F&B menus in Vietnam.
- **When NOT to Use:**
  - Internal back-of-house kitchen inventory spreadsheets not exposed to guests.

## Core Knowledge Content

### 1. Official 1–5 Star Accommodation Rating Cap (`HOS002`)

Article 50 of the Law on Tourism 2017 (Luật Du lịch số 09/2017/QH14) recognizes tourist accommodation ratings strictly from 1 star to 5 stars based on official appraisal decisions by the Vietnam National Authority of Tourism or provincial tourism departments, prohibiting self-proclaimed `6 sao` or `7 sao` classifications and unaccredited star claims.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Article 50 of the Law on Tourism 2017 (Luật Du lịch số 09/2017/QH14) recognizes tourist accommodation ratings strictly from 1 star to 5 stars based on official appraisal decisions by the Vietnam National Authority of Tourism or provincial tourism departments, prohibiting self-proclaimed '6 sao' or '7 sao' classifications and unaccredited star claims." -->

### 2. Net vs Plus-Plus (`++`) Pricing Transparency (`HOS001`, `HOS005`)

In Vietnamese hospitality and fine-dining F&B pricing, net prices (`Giá đã bao gồm phí phục vụ và thuế GTGT`) must be clearly distinguished from plus-plus (`++`) prices by explicitly disclosing the service charge percentage (typically `5% phí phục vụ`) and value-added tax percentage (`8%` or `10% thuế GTGT`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="In Vietnamese hospitality and fine-dining F&B pricing, net prices ('Giá đã bao gồm phí phục vụ và thuế GTGT') must be clearly distinguished from plus-plus ('++') prices by explicitly disclosing the service charge percentage (typically 5% phí phục vụ) and value-added tax percentage (8% or 10% thuế GTGT)." -->

### 3. Aviation Delay & Cancellation Passenger Rights (`HOS004`)

Under Ministry of Transport Circular 14/2015/TT-BGTVT and Circular 19/2023/TT-BGTVT on non-refundable advance compensation and passenger obligations in air transport, flight delay or cancellation notices must state an explicit apology, the verified operational or weather cause, updated departure schedule, and passenger meal/accommodation/refund/re-routing entitlements.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/05-multi-industry-pedagogy-healthcare-legal-hospitality-hr-corpus.md" sha256="a6bcddebf52a95595070264d5a290493e1885bc7ae548ec6c68e7eca3f42d2ed" quote="Under Ministry of Transport Circular 14/2015/TT-BGTVT and Circular 19/2023/TT-BGTVT on non-refundable advance compensation and passenger obligations in air transport, flight delay or cancellation notices must state an explicit apology, the verified operational or weather cause, updated departure schedule, and passenger meal/accommodation/refund/re-routing entitlements." -->

## Failure Modes (Mandatory)

1. **Opaque `++` Price Tags (`HOS001`):** Listing `Giá phòng: 3.500.000 ₫++ / đêm` without specifying `Giá chưa bao gồm 5% phí phục vụ và 8% thuế GTGT`.
2. **Self-Proclaimed `6 Sao` / `7 Sao` Claims (`HOS002`):** Advertising a resort or cruise as `Siêu nghỉ dưỡng đẳng cấp 6 sao đầu tiên tại Việt Nam` in violation of Article 50 of the Law on Tourism 2017.
3. **Abrupt Flight Delay Notifications (`HOS004`):** Sending `Chuyến bay VN123 đổi giờ bay sang 23:45` without an apology, cause explanation, or passenger service entitlements under Circular 19/2023/TT-BGTVT.
