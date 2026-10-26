---
id: "register-and-pragmatics"
title: "Vietnamese 18-Register Pragmatic Matrix, Kinship Pronouns, and Calque Elimination"
domain: "vietnamese-pragmatics-and-ux"
description: "Verified specification of the 18-register DESIGN:OS Vietnamese pronoun matrix, compound-morpheme exemption rules, adversity/beneficiary passive voice (bị/được), and Sino-Vietnamese lexical balance."
when:
  - "Selecting self/reader pronouns across UI microcopy, SaaS landing pages, B2B proposals, finance, or government documents"
  - "Eliminating English-to-Vietnamese translation calques (CAL001) and passive-voice misuse (SYN001)"
  - "Configuring PRO001 and PRO002 pronoun drift detectors without false positives on compound words"
trust_tier: "verified"
version: "3.0.0"
source_attribution:
  - uri: "_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md"
    sha256: "863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d"
  - uri: "_evidence/vn-design-os-261026/sources/04-engine-execution-verification-log.txt"
    sha256: "4149a4846143aa45aec3a7089226ddf8f8e791c97c437acb311b2d9910bdf4ef"
---

# Vietnamese 18-Register Pragmatic Matrix, Kinship Pronouns, and Calque Elimination

## Purpose

Establishes the linguistic rules for pronoun consistency, register selection, compound-morpheme disambiguation, passive-voice polarity (`bị` vs `được`), and English calque elimination across all 6 DESIGN:OS Vietnamese skills.

## When to Use / When NOT

- **When to Use:**
  - Choosing the speaker/listener pronoun pair before drafting or reviewing any Vietnamese UI, marketing, technical, B2B, financial, or educational copy.
  - Debugging `PRO001`, `PRO002`, `CAL001`, and `SYN001` diagnostics emitted by `validate_copy.py`.
- **When NOT to Use:**
  - Literary fiction or multi-character dialogue where characters intentionally switch pronouns to reflect shifting emotional states.

## Core Knowledge Content

### 1. The 18-Register Kinship and Pronoun System (`PRO001`, `PRO002`)

Vietnamese lacks a neutral universal second-person pronoun equivalent to English `you`; every speaker-addressee pair encodes age, social distance, institutional authority, and transactional context.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Vietnamese lacks a neutral universal second-person pronoun equivalent to English 'you'; every speaker-addressee pair encodes age, social distance, institutional authority, and transactional context." -->

The DESIGN:OS Vietnamese Register Matrix defines 18 distinct registers across digital product UI (`ux-microcopy`), SaaS/consumer landing pages, enterprise B2B, banking/wealth management, administrative/government (Nghị định 30/2020/NĐ-CP), and healthcare.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="The DESIGN:OS Vietnamese Register Matrix defines 18 distinct registers across digital product UI (ux-microcopy), SaaS/consumer landing pages, enterprise B2B, banking/wealth management, administrative/government (Nghị định 30/2020/NĐ-CP), and healthcare." -->

In `ux-microcopy` (buttons, menus, toasts, form validation, empty states), the optimal register drops pronouns entirely in action labels (`Lưu thay đổi`, `Tạo dự án`) and uses `bạn` / `của bạn` only in conversational feedback, avoiding the pompous `Quý khách` inside compact UI controls.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="In ux-microcopy (buttons, menus, toasts, form validation, empty states), the optimal register drops pronouns entirely in action labels ('Lưu thay đổi', 'Tạo dự án') and uses 'bạn' / 'của bạn' only in conversational feedback, avoiding the pompous 'Quý khách' inside compact UI controls." -->

### 2. Bound Compound-Morpheme Exemption Rules

Automated pronoun validators (`PRO001`, `PRO002`) must exempt Sino-Vietnamese and native compound words where `bạn` or `quý` is a bound morpheme rather than a second-person pronoun, including `bạn bè`, `bạn đọc`, `bạn hàng`, `bạn đời`, `kết bạn`, `tình bạn`, `quý giá`, `quý hiếm`, `quý báu`, `quý trọng`, `quý mến`, and fiscal quarters `Quý I`, `Quý II`, `Quý III`, `Quý IV`, `Quý 1`–`Quý 4`.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Automated pronoun validators (PRO001, PRO002) must exempt Sino-Vietnamese and native compound words where 'bạn' or 'quý' is a bound morpheme rather than a second-person pronoun, including 'bạn bè', 'bạn đọc', 'bạn hàng', 'bạn đời', 'kết bạn', 'tình bạn', 'quý giá', 'quý hiếm', 'quý báu', 'quý trọng', 'quý mến', and fiscal quarters 'Quý I', 'Quý II', 'Quý III', 'Quý IV', 'Quý 1'–'Quý 4'." -->

### 3. English-to-Vietnamese Calques (`CAL001`) and Passive Voice Polarity (`SYN001`)

English-to-Vietnamese calques degrade natural cadence: `Làm ơn` in UI prompts (`Làm ơn nhập email`) carries a begging connotation and must be replaced with `Vui lòng nhập email` or direct imperative `Nhập email`; `Của bạn` at the start of a noun phrase (`Của bạn đơn hàng`) violates Vietnamese head-first noun phrase syntax.
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="English-to-Vietnamese calques degrade natural cadence: 'Làm ơn' in UI prompts ('Làm ơn nhập email') carries a begging connotation and must be replaced with 'Vui lòng nhập email' or direct imperative 'Nhập email'; 'Của bạn' at the start of a noun phrase ('Của bạn đơn hàng') violates Vietnamese head-first noun phrase syntax." -->

Vietnamese distinguishes adversity passive `bị` (negative outcome: `Tài khoản bị khóa`, `Thanh toán bị từ chối`) from beneficiary passive `được` (positive/neutral outcome: `Đơn hàng đã được xác nhận`) and active/state `đã` (`Hệ thống đã lưu thay đổi`); writing `Đơn hàng bị hủy thành công` or `Tệp của bạn đã bị tải lên` is a high-severity pragmatic error (`SYN001`).
<!-- ease:source uri="_evidence/vn-design-os-261026/sources/02-pragmatics-typography-icu-corpus.md" sha256="863e0f0c9ad2317f3b3fe74a7d33084247b23139ebc8ef7fb05d4da1c471788d" quote="Vietnamese distinguishes adversity passive 'bị' (negative outcome: 'Tài khoản bị khóa', 'Thanh toán bị từ chối') from beneficiary passive 'được' (positive/neutral outcome: 'Đơn hàng đã được xác nhận') and active/state 'đã' ('Hệ thống đã lưu thay đổi'); writing 'Đơn hàng bị hủy thành công' or 'Tệp của bạn đã bị tải lên' is a high-severity pragmatic error (SYN001)." -->

## Failure Modes (Mandatory)

1. **Pronoun Drift Within a Single Flow (`PRO001`):** Addressing the user as `Quý khách` in the hero headline and switching to `bạn` in the pricing card or checkout button destroys voice consistency.
2. **Compound Morpheme False Positives (`PRO001-COMPOUND-MORPHEME`):** Flagging `Báo cáo tài chính Quý II` or `tài sản quý giá` as an informal/formal pronoun collision when naive regexes match `\bquý\b` without compound-word pre-masking.
3. **Adversity Passive on Positive Action (`SYN001`):** Translating "Your order was successfully cancelled" as `Đơn hàng của bạn đã bị hủy thành công` instead of `Đã hủy đơn hàng` or `Đơn hàng đã được hủy theo yêu cầu`.
