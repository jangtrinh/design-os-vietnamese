# DESIGN:OS Vietnamese Prompt Cookbook (`docs/cookbook.md`)

Copy-paste prompt recipes for Claude Code, OpenAI Codex, Gemini CLI, and Google Antigravity across all 16 Vietnamese production skills.

---

## 1. UI/UX Microcopy, Design Tokens & i18n (`vn-design-system-ux`)

```text
"Audit our Vietnamese localization catalog (vi.json against en.json) using check_i18n_parity.py and validate_copy.py --domain ux --register ux-microcopy. Fix any decomposed NFD characters, ICU 'one' plural branches, and button labels exceeding 24 characters (hard cap 28)."
```

## 2. Landing Pages & Advertising Law 75/2025 (`vietnamese-landing-copy`)

```text
"Write a high-converting Vietnamese SaaS landing page in register marketing-b2b. Ensure zero unverified superlatives under Advertising Law 75/2025/QH15 and verify with validate_copy.py --domain landing --doctype landing-page --strict."
```

## 3. Developer Docs, Runbooks & ADRs (`vietnamese-tech-writing`)

```text
"Draft a Vietnamese incident postmortem and production runbook in register tech-docs. Keep technical tokens (Webhook, OAuth 2.0, Idempotency Key) intact and verify with validate_copy.py --domain tech --doctype runbook."
```

## 4. B2B Emails, Zalo ZNS & Decree 30/2020 *Công văn* (`vietnamese-business-comms`)

```text
"Draft a formal administrative Công văn under Decree 30/2020/NĐ-CP in register admin-cong-van and verify all mandatory structural blocks with validate_copy.py --domain biz --doctype cong-van --strict."
```

## 5. Banking, VietQR & Circular 99/2025 Financial Reports (`vietnamese-finance-copy`)

```text
"Write a Vietnamese financial statement summary compliant with Circular 99/2025/TT-BTC and Decree 70/2025/NĐ-CP e-invoicing rules. Verify with validate_copy.py --domain finance --doctype financial-report."
```

## 6. 7-Tier Vietnamese Pedagogy Continuum: Mầm non → Tiến sĩ (`vietnamese-education-copy`)

```text
"Draft a Preschool developmental evaluation report (Mẫu giáo 3–6 tuổi, VBHN 01/VBHN-BGDĐT) using register edu-preschool and doctype preschool-report, AND a Doctoral dissertation proposal (VQF Level 8, TT 18/2021/TT-BGDĐT) using register edu-postgrad and doctype doctoral-dissertation. Validate both with validate_copy.py --strict."
```

## 7. Clinical EMR, E-Prescriptions & TPCN Compliance (`vietnamese-healthcare-copy`)

```text
"Audit this Vietnamese dietary supplement (TPCN) description and hospital discharge summary under Healthcare Law 2023 and Decree 15/2018/NĐ-CP using validate_copy.py --domain healthcare --doctype tpcn-ad."
```

## 8. Civil & Commercial Contracts (`vietnamese-legal-contracts`)

```text
"Draft a Vietnamese B2B software service contract under Civil Code 2015 and Commercial Law 2005 (enforcing the 8% breach penalty cap under Article 301). Verify with validate_copy.py --domain legal --doctype commercial-contract --register legal-contract."
```

## 9. 5-Star Hospitality, Aviation & Culinary Copy (`vietnamese-hospitality-travel`)

```text
"Write a 5-star resort booking confirmation and flight delay notification compliant with Tourism Law 2017 (Article 50) and Circular 19/2023/TT-BGTVT, explicitly disclosing ++ service charge and VAT. Verify with validate_copy.py --domain hospitality."
```

## 10. HR, Non-Discriminatory JDs & Labor Code 2019 (`vietnamese-hr-recruitment`)

```text
"Write a Vietnamese Senior Engineer Job Description and Offer Letter compliant with Articles 8, 17, 20, 25, and 26 of Labor Code 2019 (>=85% probation salary, clear Gross/Net disclosure). Verify with validate_copy.py --domain hr --doctype offer-letter --register hr-candidate."
```

## 11. Real Estate, Property & Construction BOQ (`vietnamese-real-estate-construction`)

```text
"Draft an off-plan apartment sales summary compliant with Real Estate Business Law 2023 (<=5% deposit cap Art. 23, <=30%/70%/95% installment caps Art. 25), Land Law 2024, and Housing Law 2023 (explicitly separating diện tích thông thủy vs tim tường and 2% maintenance fund). Verify with validate_copy.py --domain realestate --doctype off-plan-contract --register realestate-luxury."
```

## 12. E-Commerce, Omnichannel Retail & Consumer Protection (`vietnamese-ecommerce-retail`)

```text
"Audit an e-commerce product detail page (PDP) and Flash Sale campaign under Decrees 52/2013 & 85/2021 (Đã thông báo vs Đã đăng ký Bộ Công Thương), Decree 128/2024 (<=50% regular discount cap), and Consumer Protection Law 2023. Verify with validate_copy.py --domain ecommerce --doctype product-pdp --register ecommerce-shopper."
```

## 13. E-Government, Public Services (DVC) & VNeID (`vietnamese-government-public-service`)

```text
"Draft an online administrative procedure (TTHC) guide for the National Public Service Portal using Decree 42/2022/NĐ-CP (Dịch vụ công trực tuyến toàn trình / một phần), Law on Identification 2023 (Thẻ căn cước), Decree 69/2024 (VNeID Mức độ 2), and Law on Residence 2020 (zero paper Sổ hộ khẩu demands). Verify with validate_copy.py --domain gov --doctype dvc-guide --register public-citizen."
```

## 14. Insurance, Bancassurance & InsurTech (`vietnamese-insurance-insurtech`)

```text
"Audit a life insurance product illustration and claim guide under Insurance Business Law 2022 and Circular 67/2023/TT-BTC (21-day free-look period Art. 35, explicit liability exclusions Art. 19, 15-day payout Art. 31, zero bank-deposit misrepresentation). Verify with validate_copy.py --domain insurance --doctype policy-illustration --register insurance-policyholder."
```

## 15. Cybersecurity, ATTT Level 1–5 & 72h Breach Notice (`vietnamese-cybersecurity-infosec`)

```text
"Write a Personal Data Protection breach notification to A05 Ministry of Public Security (<=72 hours under Decree 13/2023/NĐ-CP Art. 23) and a CVE security advisory compliant with Decree 85/2016 & Circular 12/2022 (ATTT Cấp độ 1–5). Verify with validate_copy.py --domain cybersecurity --doctype breach-notification --register infosec-advisory."
```

## 16. Media, Journalism, Press Releases & Crisis PR (`vietnamese-media-journalism-pr`)

```text
"Draft an official corporate Press Release and Crisis Communications Statement compliant with Press Law 2016, Decree 147/2024/NĐ-CP, Article 42 press correction rules, presumption of innocence (nghi phạm / bị can / bị cáo), and Law on Children 2016 (<16 anonymization). Verify with validate_copy.py --domain media --doctype press-release --register crisis-comms."
```

## 17. Hybrid Multi-Domain Audit, Apple `.xcstrings` / Android `strings.xml` & Inline Suppression

```text
"Audit our Bancassurance & FinTech privacy agreement across Finance, Insurance, Legal, and Cybersecurity simultaneously using:
  python3 shared/scripts/validate_copy.py contract.md --domain finance,insurance,legal,cybersecurity --strict
Check our iOS String Catalog and Android XML parity using:
  python3 shared/scripts/check_i18n_parity.py ios/Localizable.xcstrings --json
  python3 shared/scripts/check_i18n_parity.py android/values/strings.xml android/values-vi/strings.xml --json
Use <!-- vncopy-disable: LAW001 --> or <!-- vncopy-disable-line --> only for legally verified third-party awards."
```
