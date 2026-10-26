# DESIGN:OS Vietnamese Prompt Cookbook (`docs/cookbook.md`)

Copy-paste prompt recipes for Claude Code, OpenAI Codex, Gemini CLI, and Google Antigravity across all 10 Vietnamese production skills.

---

## 1. UI/UX Microcopy, Design Tokens & i18n (`vn-design-system-ux`)

```text
"Audit our Vietnamese localization catalog (vi.json against en.json) using check_i18n_parity.py and validate_copy.py --domain ux --register ux-microcopy. Fix any decomposed NFD characters, ICU 'one' plural branches, and button labels exceeding 28 characters."
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
