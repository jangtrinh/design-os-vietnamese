# Knowledge refresh 2026-10-28: legal validity + rule variant tables

Run: `knowledge/_evidence/vn-design-os-261026`, extended through rounds 2–10. Researcher: claude-opus-5-5. Independent review is in §7.

## 1. Numbers (before → after)

| Measure | Before | After |
|---|---|---|
| `verify_ukmc.py`: verified claims | 19/19 | **61/61** |
| `verify_ukmc.py`: independent sources (distinct frozen files) | 6 | **26** |
| External publishers behind those files | 0 (all 6 are corpora the project wrote) | **3**: vbpl.vn / Bộ Tư pháp ×12, hethongphapluat.com ×7, hoatieu.vn ×1 |
| Issuing bodies of the frozen primary texts | 0 | 3 (Quốc hội, Chính phủ, Bộ GDĐT) |
| `ease:source` anchors in modules | 66 | 114 |
| Ledger atoms | 21 | 81 (rounds in §1a) |
| Saturation (`run measure --material`) | not measured | **0/3 low-delta rounds** (round 10 delta 0.0253) |
| Builder gate (`kb gate`) | STOP_SUFFICIENT, resting on a stale review | **DEEPEN**: hard gates pass, independent review recorded, saturation does not pass, probes remain open |

- **"Independent sources" counts files.** Two files from one publisher count twice, so the publisher row is the honest measure of independence.
- **`tools/verify_ukmc.py` still prints STOP_SUFFICIENT.** It checks hashes and claim counts but not saturation or open probes. The builder gate is the stricter result, and it is the one that counts.

### 1a. Rounds: what each one was

| Round | Type | Atoms | Novel | Delta |
|---|---|---|---|---|
| 1 | baseline (2026-10-26, gemini worker) | 21 | — | — |
| 2 | primary-text research: 10 statutory texts frozen from vbpl.vn and mirrors | 30 | 30 | 1.43 |
| 3–5 | **corroboration only**: second-publisher copies (17–22) of the same texts, no new claims | 15 | 0 | 0.0 |
| 6 | **probe**: penalty decree NĐ 330/2026 | 5 | 5 | 0.076 |
| 7 | **probe**: NĐ 38/2018, the decree FIN001 cites | 2 | 2 | 0.028 |
| 8 | **probe**: Luật 56/2024, the 2024 amendment to the Securities Law | 2 | 2 | 0.027 |
| 9 | **probe**: vbpl register entry for Luật KDBĐS 29/2023 (1 new claim + 3 official-text corroborations) | 4 | 1 | 0.013 |
| 10 | **review correction, not a probe**: two anchors the independent review asked for (NĐ 356 Đ20 k3 on Mẫu 03a/03b; NĐ 15 Đ27 k4 đ) | 2 | 2 | 0.025 |

Rounds 3–5 had zero delta, but they were corroboration, not saturation. The real probes in rounds 6–8 each found new material, so the low-delta counter reset. Round 9 was low-delta, and round 10's review corrections reset the counter again. No round was made up and no claim was trimmed to get back under 2%. The run is therefore DEEPEN, and `has_viable_probe_remaining=true`, with the open probes listed in `state.json` → `open_probes`.

## 2. Legal validity verdicts (checked 2026-10-28)

Status comes from the schema.org `legislationLegalForce` field on each vbpl.vn page, the national legal database (Cơ sở dữ liệu quốc gia về pháp luật). It is frozen as line 1 of each vbpl source file.

| Document | Status | Evidence |
|---|---|---|
| Luật BVDLCN 91/2025/QH15 | InForce from 01/01/2026 | Điều 38 k1; vbpl JSON-LD |
| NĐ 356/2025/NĐ-CP (detailing Law 91) | InForce from 01/01/2026 | Điều 42 k1 |
| **NĐ 13/2023/NĐ-CP** | **NotInForce from 01/01/2026** | NĐ 356 Điều 42 k2; vbpl JSON-LD `NotInForce` |
| **NĐ 330/2026/NĐ-CP** (fines for cybersecurity + PDP) | InForce from 19/08/2026 | Điều 80; vbpl JSON-LD |
| Luật Quảng cáo 16/2012/QH13 | PartiallyInForce | vbpl JSON-LD; Law 75/2025 leaves Điều 8 k11 unchanged |
| Luật 75/2025/QH15 (amends the Advertising Law) | InForce from 01/01/2026 | Điều 3 k1. Điều 1 k25 repeals Điều 8 k13; Điều 1 k4 rewrites only k3 and k10 |
| Luật Chứng khoán 54/2019/QH14 | PartiallyInForce | vbpl JSON-LD |
| Luật 56/2024/QH15 (amends the Securities Law) | in force 01/01/2025 → **fully out of force from 01/01/2026** | vbpl record. Its only change to Điều 12 is k3 (market manipulation); none of its 20 securities items touches **Điều 91** |
| NĐ 38/2018/NĐ-CP | InForce | vbpl JSON-LD. Scope: investment in innovative SME start-ups (Điều 1 k1) |
| NĐ 15/2018/NĐ-CP | InForce | vbpl JSON-LD. Press reports a draft replacement (not frozen) |
| Luật KCB 15/2023/QH15 | InForce | vbpl JSON-LD |
| Luật KDBĐS 29/2023/QH15 | **PartiallyInForce** (effective 01/08/2024) | vbpl JSON-LD, read in round 9. The official text reproduces the 3 REA quotes word for word |
| QĐ 1989/QĐ-BGDĐT (25/5/2018) | number, date and title confirmed | mirror text. Scope: textbooks only |

The open UNKNOWN is answered: yes. Law 91/2025 plus Decree 356/2025 replaced Decree 13/2023 from 01/01/2026. Processing already under way that was consented or agreed under Decree 13 continues without new consent (Law 91 Điều 39 k1).

## 3. Substantive changes behind the citation fix

This was more than a number swap. Five statements in the repo were wrong under the new regime, not merely out of date:

| Old statement (NĐ 13/2023 era) | Current rule | Basis |
|---|---|---|
| Breach notice on **Mẫu 03a** | **Mẫu số 08**. In NĐ 356, Mẫu 03a/03b is the DPIA *update* form | NĐ 356 Đ28 k2 |
| Children **7 to under 16** need dual consent for any processing | Dual consent (child + legal representative) applies to **publishing or disclosing private-life data from age 7**, with no upper bound. Otherwise the legal representative acts for the child | Luật 91 Đ24 k2 |
| **11 rights** of the data subject (NĐ 13 Đ9) | Law 91 Đ4 k1 groups them into points a–e. "Self-protection" is now a duty (Đ4 k2 a) | Luật 91 Đ4 |
| Agency = **"Cục A05"** | Law 91 and NĐ 356 name only the **"cơ quan chuyên trách bảo vệ dữ liệu cá nhân"**, a unit under Bộ Công an. NĐ 330/2026 Đ55 k1 b names **Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao (Bộ Công an)** as the DPIA-dossier recipient, so the Cục is very likely that agency, but no frozen text says so outright (inference). The code "A05" appears in none of the three texts | NĐ 356 Đ39 k1; NĐ 330 Đ55 |
| FIN001 basis "Luật CK **Đ12**; **NĐ 38/2018** Đ2 k4" | The ban is Luật CK **Điều 91 k1**. NĐ 38/2018 governs start-up investment; its Đ2 k4 only defines the start-up fund manager | Luật CK Đ91; NĐ 38 Đ1, Đ2 |

New, now cited: under NĐ 330/2026, default-on consent costs **30–50 M đồng** (Đ43 k1 c) and treating silence as consent **50–70 M đồng** (Đ43 k2 b). Both amounts are for organizations; individuals pay half (Đ7 k1).

Mapping used for every edit:
- consent → Luật 91 Đ9 + NĐ 356 Đ6 (k3 bans default consent)
- breach within 72h → Luật 91 Đ23 k1
- breach-notice content and form → NĐ 356 Đ28
- sensitive data → Luật 91 Đ2 k3 + NĐ 356 Đ4
- cases needing no consent → Luật 91 Đ19
- DPIA → Luật 91 Đ21 + NĐ 356 Đ19
- cross-border transfer → Luật 91 Đ20 + NĐ 356 Đ17–18
- health data → Luật 91 Đ26

## 4. Stale citations fixed

- **`knowledge/`**: `statutory-compliance-vi.md` (3.2.0), `cybersecurity-attt-and-pdpd.md` (5.2.0), `finance-tt99-and-fintech.md` (3.2.0), `real-estate-and-construction-law.md` (5.2.0), `healthcare-by-law-and-emr.md`, `unicode-and-phonology.md`. The old corpus anchors are kept and labelled "Historical".
- **`shared/references/compliance.md` and `register-matrix.md`**, synced to all 16 skills (`tools/sync_shared.py --check` passes).
- **25 skill files, 67 lines, plus 4 stale `Mẫu 03a` lines.**
  - Substance fixes, not just citation swaps:
    - PDPD policy template (`chinh-sach-bao-mat-pdpd.md.template`): legal basis, definition (Luật 91 Đ2 k1), and the 6-item rights list from Luật 91 Đ4 k1 a–e, replacing the old 11-item list.
    - `pdpd-and-consumer-protection.md`: definitions table (Đ2 k5/7/8/9), DPIA and transfer duties (Đ20–21 + NĐ 356 Đ18–19), and the rights list.
    - `ung-cuu-su-co-pdpd-72h-a05.md`: Mẫu 08 contents (NĐ 356 Đ28 k1 a–d), with the basic and sensitive data lists quoted from NĐ 356 Đ3 and Đ4.
    - Education `edtech-pedagogy.md` §6 and `qa-checklist.md` item 12: the child-consent rule.
  - Every remaining mention of NĐ 13/2023 in these files is labelled as history. The template lints clean, as the original did.
  - Left as is: the shorthand "Cục A05" in about 8 cybersecurity and legal skill files, including headings and the `ung-cuu-su-co-pdpd-72h-a05.md` filename. It points at a real unit (NĐ 330 Đ55), but user-facing copy should use the full name. That is a style pass, not a legal fix.

**Not fixed: these files are protected and left for the owner to decide.**

| File | Lines | Proposed replacement |
|---|---|---|
| `rules_cybersecurity.py` | 9, 25, 31, 36, 163–164, 180–181, 229, 262–263 | "Điều 23 Luật 91/2025/QH15; Mẫu số 08 NĐ 356/2025". SEC006 → "Điều 4 NĐ 356/2025". Replace the code "A05" with the statutory term "cơ quan chuyên trách bảo vệ dữ liệu cá nhân (Bộ Công an)"; the full Cục name (NĐ 330 Đ55) only as an inference |
| `rules_education.py` | 21, 41, 57, 365, 377 | "Luật 91/2025/QH15 Điều 24" (dual consent only for publishing private-life data, age ≥ 7) |
| `rules_landing.py` | 17, 43, 118 | "Luật 91/2025/QH15 Điều 9; NĐ 356/2025 Điều 6". Optionally add the NĐ 330 Đ43 fine to the message |
| `rules_legal.py` | 10, 30, 40, 284–285 | "Điều 4 Luật 91/2025/QH15". LEG007 checks only for a rights heading, "rút lại sự đồng ý" and "xóa dữ liệu", all still valid under Đ4 k1 b and d. **Only the message text is stale; the logic does not need to change** |
| `rules_tech.py` | 23, 219 | "Luật 91/2025/QH15 Điều 9" |
| `rules_finance.py` | 11, 30, 193–194 | FIN001 basis: "Luật Chứng khoán 2019 **Điều 91 khoản 1**". Drop "Đ12" and "NĐ 38/2018 Đ2 kh.4" (neither has a guarantee clause). Scope note: Đ91 binds securities firms and fund managers; for other issuers the rule is a style rule, not a statutory one |
| `evals/` | trigger-queries.md ×4; 5 pairs.jsonl files (9 rows) | same mapping |
| `skills/*/references/examples.md` ×4 | generated from `evals/` by `tools/build_examples.py` | regenerate after `evals/` changes |
| `tools/generate_tech_pairs.py`, `generate_landing_pairs.py` | 2 each | same mapping |

**Cost split (owner instruction, received mid-run).** The research, writing and rulings ran on Opus (claude-opus-5-5) before the instruction arrived. Independent grading ran on grok-4.7, not a Claude model. The final mechanical gate rerun ran on Haiku, and Opus checked it.

**Ledger disclosure.** Two old round-1 required claims, `claim-statutory-compliance` and `claim-cybersecurity-law`, still describe Decree 13/2023, now expired. Their quotes are true of the old corpus, so they still verify. The modules cite them only under "Historical" labels. The owner should decide whether to retire them from `required_claim_ids`.

## 5. New sources (frozen in `knowledge/_evidence/vn-design-os-261026/sources/`)

Legal texts are not protected by copyright (Luật SHTT Điều 15), so full copies are frozen. Each one is cut to the statutory span, with site navigation and paid commentary removed. Mirror diffs against the official copies show statutory-text differences only.

- **07–14, from vbpl.vn**: Luật 91/2025/QH15 · NĐ 356/2025/NĐ-CP · NĐ 13/2023/NĐ-CP (status record) · Luật 75/2025/QH15 · Luật 16/2012/QH13 · Luật 54/2019/QH14 · NĐ 15/2018/NĐ-CP · Luật 15/2023/QH15.
- **15–16, mirrors with no register status**: Luật 29/2023/QH15 (hethongphapluat.com) · QĐ 1989/QĐ-BGDĐT (hoatieu.vn).
- **17–22, second-publisher copies** (hethongphapluat.com) of 07, 12, 11, 10, 13 and 14. All 15 claim quotes reproduce verbatim.
- **23–26, from vbpl.vn**: NĐ 330/2026/NĐ-CP · NĐ 38/2018/NĐ-CP · Luật 56/2024/QH15 (with its register fields) · Luật 29/2023/QH15 (the official text of 15).

## 6. Machine-usable output: `knowledge/data/`

- `rule-variant-tables.json`: tables for FIN001, MED002, REA001 and REA002. Each row carries an evidence class:
  - `statutory`: the clause is a frozen quote;
  - `attested-in-statute`: the form appears in a frozen official text with the needed sense, e.g. the MED002 disclaimer words in NĐ 15 Đ27 k3 a;
  - `proposed`: no source.
  - `đảm bảo` and `lãi` are `proposed`: the frozen texts use them only in other senses ("ensure"; accounting interest on assets).
  - Each table also has word-order patterns, statutory exceptions (fixed-income coupons; the TPCN disclaimer itself), proposed regexes, and a proposed negation guard.
  - FIN001 carries a `scope_note` on Đ91's addressees.
- `rule-negation-cases.jsonl`: 10 valid sentences that must not fire.
- `heldout-candidates.jsonl`: 12 paraphrases that should fire.
- `tests/test_knowledge_rule_variant_tables.py`: re-checks every quote and sha256 against the frozen files, and checks that evidence classes are consistent.

Measured with the unchanged linter (read-only run of `validate_copy.py`):

| | Current rules | Proposed patterns + negation guard |
|---|---|---|
| Held-out candidates flagged (want 12/12) | **2/12** | 11/12 |
| Valid negations flagged (want 0/10) | 2/10 | 1/10 |

Caveats:
- **The proposed numbers are in-sample.** The patterns were written with these sentences in view. Freeze the candidates and write new sentences before any of this counts as a held-out score.
- **The current negation guard (`META_NEGATION_RE`) skips only meta wording** such as "không được cam kết". A plain "Sản phẩm này không cam kết lợi nhuận" is flagged today, and so is "Không có khoản đầu tư nào được đảm bảo sinh lời".

## 7. Independent review

Reviewer: **grok-4.7**, read-only (`grok-run.mjs ask --lean`, no write tools). It is a different runtime from the researcher (claude-opus-5-5).
- `codex exec` was tried first and could not authenticate (expired refresh token), so it gave no verdict. **Re-login to Codex is needed (owner-manual).**
- Raw verdicts, packets and prompts are in `knowledge/_evidence/vn-design-os-261026/reviews/`, with personal paths scrubbed. The verdicts are summarised in `review.json`.

| Run | Scope | Result |
|---|---|---|
| 1 | 43 atoms (rounds 2, 6–9), variant tables, agency paragraph | passed=false: 2 wrong, 7 overreach, 2 variant-row issues |
| 2 | 11 revised or disputed items, 2 relabelled rows, 2 module sections | 0 wrong, 2 minor overreach, rows OK; module text not OK |
| 3–4 | module paragraphs with their anchors | 3, then 1, sentences beyond their anchors |
| 5 | rewritten cybersecurity §1 | **passed=true**, 3 wording nits |

**Accepted and fixed:**
- MED "cure claims fall outside any declaration": NĐ 15 Đ27 k4 đ allows content beyond the declared uses when it has scientific documentation. Statement narrowed, k4 đ cited, and the MED002 reading labelled as the rule's.
- Điều 39 transition: covers ongoing processing only. Fixed in the ledger, the module, `shared/compliance.md` (synced to 16 skills) and this report.
- Banner gloss, the Mẫu 03a fact, and the organization scope of fines: each now rests on its own cited clause.
- `lãi` → proposed; the MED002 disclaimer words → attested-in-statute.
- The Cục = specialised agency equation is labelled as an inference.
- Status dates now anchored in place.

**Rejected, with evidence:**
- "default-consent quote not in Điều 6": it is NĐ 356 Đ6 k3. The packet showed the wrong heading.
- "Luật 56 negative not shown": the full list of 20 item headers has zero mentions of Đ91. Run 2 agreed.

`review.json` `passed=true` is a composite, set by the researcher from the reviewer's last verdict on each scope; no single reviewer run passed every scope. The basis is written into the file (`passed_basis`). It does not change the gate, which stays DEEPEN on saturation.

## 8. Still UNKNOWN (open probes)

**Resolved in this run:**
- "Is Cục A05 still the unit's name?" Partly: NĐ 330 Đ55 (2026) still names the Cục in full, as the DPIA-dossier recipient. No frozen text uses the code, and none says outright that the Cục is the specialised agency.
- "What does NĐ 38/2018 say on guarantees?" Nothing: it is a start-up investment decree.

**Still open:**
- Which law replaced Luật 56/2024/QH15 from 01/01/2026, and whether it amends Luật CK Điều 91. This is the next probe.
- Which provisions of Luật KDBĐS 29/2023 lost force (Luật 43/2024 and later), and whether Điều 23 k5 or Điều 25 are among them.
- Status of the NĐ 15/2018 replacement decree after July 2026.
- Dictionary and grammar layer: no copies of Hoàng Phê, Diệp Quang Ban or Cao Xuân Hạo were available. Every colloquial variant (`bao lời`, `khỏi hẳn`, `booking`) stays `proposed`, and the negation cue list has no source.
- QĐ 1989 binds textbooks only. Whether product UI should follow it is a style decision for the owner.

## 9. Verification (rerun after the last edit)

Rerun after the last edit on 2026-10-28. Screenshot: [knowledge-261028-2016-gates-terminal.png](knowledge-261028-2016-gates-terminal.png).
- Haiku ran the suite first and caught one stale count in `test_ukmc_knowledge.py` (59/59 instead of 61/61). After the fix, Opus reran the full suite.
- The builder check in `tests/test_ukmc_knowledge.py` resolves the builder as a sibling of the repo, so it is skipped inside a `.claude/worktrees/` checkout. It was also run against `~/Products/design-os-knowledge-builder`: 2 tests OK.

```text
$ python3 tools/sync_shared.py --check
sync_shared: 16 skills verified byte-identical to shared/
[exit 0]

$ python3 tools/build_examples.py --check
build_examples: 16 skills verified up-to-date
[exit 0]

$ python3 tools/verify_ukmc.py
files: 18 · anchors: 114 · failures: 0 · exempt blocks: 0
verified_claims: 61/61 · independent_sources: 26
Decision: STOP_SUFFICIENT
[exit 0]

$ env PYTHONPATH=$HOME/Products/design-os-knowledge-builder/src python3 -m knowledge_builder.cli verify ./knowledge --claims
[WARN] no ontology.yaml: legacy mode, UKMC.v1 checks only
files: 18
anchors: 114
failures: 0
exempt blocks: 0
[exit 0]

$ env PYTHONPATH=$HOME/Products/design-os-knowledge-builder/src python3 -m knowledge_builder.cli gate --root ./knowledge --run-id vn-design-os-261026
[*] Evaluating Stopping Gate for run: vn-design-os-261026
--------------------------------------------------
Decision: DEEPEN
Reason:   Deficiencies detected: Saturation not yet reached (low-delta rounds 0/3, delta 2.5%), A viable probe remains. Probing further.
Hard Gates Passed: True
Saturation Passed: False
--------------------------------------------------
[exit 2]

$ python3 -m unittest discover -s tests
..................................................................
----------------------------------------------------------------------
Ran 66 tests in 5.525s

OK
[exit 0]

$ python3 scripts/self_check.py
ok: design-os-vietnamese self-check passed (16 skills, 18 UKMC.v1 modules)
[exit 0]
```

| Gate | Result |
|---|---|
| sync_shared, build_examples, self_check | pass |
| `verify_ukmc.py` | 61/61 claims, 26 sources, 0 failures (STOP_SUFFICIENT under its own looser gate) |
| `kb verify --claims` | 114 anchors, 0 failures |
| `kb gate` | **DEEPEN** (exit 2). Hard gates pass; saturation 0/3; a probe remains |
| unittest | 66 tests OK |
| protected files (`rules_*.py`, `evals/`, `pyproject.toml`, `.pre-commit-hooks.yaml`, `.github/`, `README*`, `CHANGELOG.md`) | untouched |

## 10. Open questions for the owner

1. **Retire the two NĐ 13-era claims?** `claim-statutory-compliance` and `claim-cybersecurity-law` are still in `required_claim_ids`.
2. **Apply the protected-file replacements in §4?** These are the `rules_*.py` and `evals/` files; LEG007's logic can stay as is.
3. **Make `tools/verify_ukmc.py` read saturation and open probes?** It reports STOP_SUFFICIENT while the builder reports DEEPEN.
4. **Re-login to Codex** so a second, non-Grok reviewer can check this run.
