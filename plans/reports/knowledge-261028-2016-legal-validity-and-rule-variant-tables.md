# Knowledge refresh 2026-10-28: legal validity + rule variant tables

Run: `knowledge/_evidence/vn-design-os-261026` (extended, rounds 2–5). Researcher: claude-opus-5-5. Independent review: see §7.

## 1. Numbers (before → after)

| Measure | Before | After |
|---|---|---|
| `verify_ukmc.py` verified claims | 19/19 | **49/49** |
| `verify_ukmc.py` independent sources (distinct frozen files) | 6 | **22** |
| External publishers behind those files | 0 (all 6 are project-written corpora) | **3** (vbpl.vn / Bộ Tư pháp ×8, hethongphapluat.com ×7, hoatieu.vn ×1) |
| Issuing bodies of frozen primary texts | 0 | 3 (Quốc hội, Chính phủ, Bộ GDĐT) |
| ease:source anchors in modules | 66 | 98 |
| Ledger atoms | 21 | 66 (30 novel in round 2, 15 corroborating in rounds 3–5) |
| Saturation (`run measure --material`) | not measured | rounds 3, 4, 5 delta 0.0000 → 3/3 low-delta |
| Builder gate | STOP_SUFFICIENT | STOP_SUFFICIENT |

The tool's "independent sources" counts files. Two files from one publisher count twice, so the publisher row is the honest independence figure.

## 2. Legal validity verdicts (checked 2026-10-28)

Status source: the schema.org `legislationLegalForce` field on each vbpl.vn page (Cơ sở dữ liệu quốc gia về pháp luật). It is frozen as line 1 of each `07–14` source file.

| Document | Status | Evidence |
|---|---|---|
| Luật BVDLCN 91/2025/QH15 | InForce from 01/01/2026 | Điều 38 k1; vbpl JSON-LD |
| NĐ 356/2025/NĐ-CP (detailing Law 91) | InForce from 01/01/2026 | Điều 42 k1 |
| **NĐ 13/2023/NĐ-CP** | **NotInForce from 01/01/2026** | NĐ 356 Điều 42 k2, plus vbpl JSON-LD `NotInForce` |
| Luật Quảng cáo 16/2012/QH13 | PartiallyInForce | vbpl JSON-LD; Điều 8 k11 is unchanged by Law 75/2025 |
| Luật 75/2025/QH15 (amends Ads Law) | InForce from 01/01/2026 | Điều 3 k1; Điều 1 k25 repeals Điều 8 k13, Điều 1 k4 rewrites k3/k10 only |
| Luật Chứng khoán 54/2019/QH14 | PartiallyInForce | vbpl JSON-LD; Luật 56/2024 amends Đ12 k3, k4, not Đ91 (read on vbpl, not frozen) |
| NĐ 15/2018/NĐ-CP | InForce | vbpl JSON-LD; replacement decree still in draft per July 2026 press (not frozen) |
| Luật KCB 15/2023/QH15 | InForce | vbpl JSON-LD |
| Luật KDBĐS 29/2023/QH15 | not read from register | mirror text only; vbpl ItemID not found |
| QĐ 1989/QĐ-BGDĐT (25/5/2018) | number, date and title confirmed | mirror text; scope is textbooks only |

Answer to the open UNKNOWN: yes. Law 91/2025 plus Decree 356/2025 replaced Decree 13/2023 from 01/01/2026. Consents obtained under Decree 13 stay valid (Law 91 Điều 39 k1).

## 3. Substantive changes behind the citation fix

This was not a number swap. Four statements in the repo were wrong under the new regime, not just stale:

| Old statement (NĐ 13/2023) | Current rule | Basis |
|---|---|---|
| Breach notice on **Mẫu 03a** | **Mẫu số 08**; in NĐ 356, Mẫu 03a/03b is the DPIA *update* form | NĐ 356 Đ28 k2 |
| Children **7 to under 16** need dual consent for any processing | Dual consent (child + legal rep) applies to **publishing/disclosing private-life data from age 7**, with no upper bound; otherwise the legal representative acts for the child | Luật 91 Đ24 k2 |
| **11 rights** of the data subject (NĐ 13 Đ9) | Law 91 Đ4 k1 groups the rights into points a–e | Luật 91 Đ4 |
| Agency = **Cục A05** | Decree 356 says only "đơn vị trực thuộc Bộ Công an"; A05 is not a statutory term | NĐ 356 Đ39 k1 |

Mapping used for every edit: consent → Luật 91 Đ9 + NĐ 356 Đ6 (k3 bans default consent); breach 72h → Luật 91 Đ23 k1; content and form → NĐ 356 Đ28; sensitive data → Luật 91 Đ2 k3 + NĐ 356 Đ4; no-consent cases → Luật 91 Đ19; DPIA → Luật 91 Đ21 + NĐ 356 Đ19; cross-border → Luật 91 Đ20 + NĐ 356 Đ17–18; health data → Luật 91 Đ26.

## 4. Stale citations fixed

- `knowledge/`: `statutory-compliance-vi.md`, `cybersecurity-attt-and-pdpd.md` (PDPD sections rewritten on the new texts; the old corpus anchors are kept and labelled "Historical").
- `shared/references/compliance.md` and `register-matrix.md`, synced to all 16 skills (`tools/sync_shared.py --check` passes).
- 25 skill files, 67 lines, plus 4 stale `Mẫu 03a` lines. Files touched: SKILL.md of education, legal, healthcare, landing and cybersecurity, and references and assets of legal (pdpd-and-consumer-protection, qa-checklist, glossary, chinh-sach-bao-mat-pdpd template), cybersecurity (banned-phrases, ung-cuu-su-co-pdpd-72h-a05, qa-checklist, glossary), healthcare, education, landing, tech-writing, insurance and business-comms. Every remaining mention of NĐ 13/2023 in these files is labelled as history.

**Not fixed: these are protected files, left for the owner to decide.**

| File | Lines | Proposed replacement |
|---|---|---|
| `rules_cybersecurity.py` | 9, 25, 31, 36, 163–164, 180–181, 229, 262–263 | "Điều 23 Luật 91/2025/QH15; Mẫu số 08 NĐ 356/2025"; SEC006 → "Điều 4 NĐ 356/2025"; drop "A05" |
| `rules_education.py` | 21, 41, 57, 365, 377 | "Luật 91/2025/QH15 Điều 24" (dual consent only for publishing private-life data, age ≥ 7) |
| `rules_landing.py` | 17, 43, 118 | "Luật 91/2025/QH15 Điều 9; NĐ 356/2025 Điều 6" |
| `rules_legal.py` | 10, 30, 40, 284–285 | "Điều 4 Luật 91/2025/QH15". The **LEG007 11-right check no longer matches the law** (logic change, not only text) |
| `rules_tech.py` | 23, 219 | "Luật 91/2025/QH15 Điều 9" |
| `rules_finance.py` | 30, 193–194 | FIN001 basis: "Luật Chứng khoán 2019 **Điều 91 khoản 1**" (Đ12 has no guarantee clause) |
| `evals/` | trigger-queries.md ×4, 5 pairs.jsonl files (9 rows) | same mapping |
| `skills/*/references/examples.md` ×4 | generated from `evals/` by `tools/build_examples.py` | regenerate after evals change |
| `tools/generate_tech_pairs.py`, `generate_landing_pairs.py` | 2 each | same mapping |

## 5. New sources (frozen, `knowledge/_evidence/vn-design-os-261026/sources/`)

Legal texts are not protected by copyright (Luật SHTT Điều 15), so full copies are frozen. Each one is cut to the statutory span, with site navigation and paid commentary removed.

- 07 Luật 91/2025/QH15 · 08 NĐ 356/2025/NĐ-CP · 09 NĐ 13/2023/NĐ-CP (status record) · 10 Luật 75/2025/QH15 · 11 Luật 16/2012/QH13 · 12 Luật 54/2019/QH14 · 13 NĐ 15/2018/NĐ-CP · 14 Luật 15/2023/QH15. All from vbpl.vn.
- 15 Luật 29/2023/QH15 (from hethongphapluat.com) · 16 QĐ 1989/QĐ-BGDĐT (from hoatieu.vn). Both are mirrors with no register status.
- 17–22: second-publisher copies (hethongphapluat.com) of 07, 12, 11, 10, 13 and 14. All 15 claim quotes reproduce verbatim. These files are corroboration rounds 3–5 and contain no new claims.

## 6. Machine-usable output: `knowledge/data/`

- `rule-variant-tables.json`: tables for FIN001, MED002, REA001 and REA002. Each row carries an evidence class:
  - `statutory`: the clause is a frozen quote;
  - `attested-in-statute`: the form appears in an official text, e.g. `đảm bảo` in NĐ 356 and `tiền lãi` in Luật CK;
  - `proposed`: no source.
  Each table also has word-order patterns, statutory exceptions (fixed-income coupons; the TPCN disclaimer itself), proposed regexes, and a proposed negation guard.
- `rule-negation-cases.jsonl`: 10 valid sentences that must not fire.
- `heldout-candidates.jsonl`: 12 paraphrases that should fire.
- `tests/test_knowledge_rule_variant_tables.py` re-checks every quote and sha256 against the frozen files, and checks that evidence classes are consistent.

Measured with the unchanged linter (read-only run of `validate_copy.py`):

| | Current rules | Proposed patterns + negation guard |
|---|---|---|
| Held-out candidates flagged (want 12/12) | **2/12** | 11/12 |
| Valid negations flagged (want 0/10) | 2/10 | 1/10 |

Caveats:
- The proposed numbers are **in-sample**. The patterns were written with these sentences in view, so the candidates must be frozen and new sentences written before any of this counts as a held-out score.
- The current negation guard (`META_NEGATION_RE`) only skips meta wording such as "không được cam kết". A plain "Sản phẩm này không cam kết lợi nhuận" is flagged today, and so is "Không có khoản đầu tư nào được đảm bảo sinh lời".

## 7. Independent review

REVIEW_PLACEHOLDER

## 8. Still UNKNOWN

- Dictionary and grammar layer: no copies of Hoàng Phê, Diệp Quang Ban or Cao Xuân Hạo were available. Every colloquial variant (`bao lời`, `khỏi hẳn`, `booking`) stays `proposed`, and the negation cue list has no source.
- Whether "Cục A05" is still the unit's name after the 2025 Bộ Công an restructuring.
- Status of the NĐ 15/2018 replacement decree after July 2026.
- The vbpl.vn register entry for Luật KDBĐS 29/2023 (only the mirror text is frozen), and Law 43/2024 amendments to it.
- What NĐ 38/2018 (cited by FIN001) actually says on guarantees. Not checked.
- QĐ 1989 binds textbooks only. Whether product UI should follow it is a style decision for the owner.
- `has_viable_probe_remaining=false` covers the statutory claims only. The lexicographic probes are still open.

## 9. Verification (rerun after the last edit)

VERIFY_PLACEHOLDER
