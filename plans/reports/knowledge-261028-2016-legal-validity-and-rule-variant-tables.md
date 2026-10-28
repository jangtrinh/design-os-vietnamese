# Knowledge refresh 2026-10-28: legal validity + rule variant tables

Run: `knowledge/_evidence/vn-design-os-261026`, extended through rounds 2–10. Researcher: claude-opus-5-5. Independent review is in §7.

**Status after round 5 (see §14): independent review passed; builder gate still DEEPEN.** grok-4.7 run 10, full scope, on frozen commit c9fa997 returned **passed=true**: 50/51 atoms entailed, 0 wrong, 1 minor overreach, 0 unsupported paragraphs, 0 variant-table issues. `verify_ukmc.py` now returns **STOP_SUFFICIENT** (exit 0). `kb gate` still returns **DEEPEN** (exit 2): hard gates pass, but saturation is 1/3 and real probes remain open. No rounds were manufactured, and no pass was set by hand.

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
| Builder gate (`kb gate`) | STOP_SUFFICIENT, resting on a stale review | **DEEPEN**: hard gates pass; saturation 0/3; probes open; final review passed=false |

- **"Independent sources" counts files.** Two files from one publisher count twice, so the publisher row is the honest measure of independence.
- **`tools/verify_ukmc.py` returns CONTINUE_GAP (exit 1).** Its only failure is `review.json did not pass independent review`. It does not check saturation or open probes, so the builder gate is the stricter result.

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

**Cost split (owner instruction, received mid-run).** The research, writing and rulings ran on Opus (claude-opus-5-5) before the instruction arrived. Independent grading ran on grok-4.7, not a Claude model. The first full gate rerun ran on Haiku and caught a stale test count. Opus ran the final rerun after the last edit.

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

Reviewer: **grok-4.7**, read-only (`grok-run.mjs ask --lean`, no write tools). It is a different runtime from the researcher (claude-opus-5-5). `codex exec` was tried first and could not authenticate (expired refresh token), so it gave no verdict. **The owner needs to re-login to Codex.** Raw verdicts, packets and prompts are in `knowledge/_evidence/vn-design-os-261026/reviews/`, with personal paths scrubbed.

| Run | Scope | Result |
|---|---|---|
| 1 | 43 atoms (rounds 2, 6–9), variant tables, agency paragraph | passed=false: 2 wrong, 7 overreach, 2 variant-row issues |
| 2 | 11 revised or disputed items, 2 relabelled rows, 2 module sections | 0 wrong, 2 minor overreach, rows OK, module text not OK |
| 3–4 | module paragraphs with their anchors | 3, then 1, sentences beyond their anchors |
| 5 | rewritten cybersecurity §1 | passed=true, 3 wording nits |
| **6 (recorded)** | **committed state bd52a14: 45 atoms, all variant rows, both module sections** | **passed=false**: 40/45 entailed, 0 wrong |

**Fixed after runs 1–5:**
- MED "cure claims fall outside any declaration": NĐ 15 Đ27 k4 đ allows content beyond the declaration when it has scientific documentation.
- Điều 39 transition: ongoing processing only. Fixed in the ledger, the module, `shared/compliance.md` (synced) and this report.
- Banner gloss; Mẫu 03a now has its own claim; the organization scope of fines.
- `lãi` → proposed.
- The Cục = specialised agency equation is labelled as an inference.
- Status dates anchored in place.

**Rejected with evidence:** "default-consent quote not in Điều 6". It is NĐ 356 Đ6 k3; run 1's packet showed the wrong heading, and runs 2 and 6 accept it.

**Still open from run 6** (not fixed in this run, so that `review.json` matches the reviewed state):
- **`claim-ads-law-75-repeals` (non-minor).** The statement that Luật 75 Đ1 k4 rewrites Đ8 k3 and k10 and leaves k11 unchanged was not shown: the packet cut the long article. Re-review with the full article.
- **`claim-fin-law56-register-status` (non-minor).** The packet showed 4 header lines, which end before the vbpl record line holding the quote. The quote does exist in the file. "Does not name a replacement" is a negative the reviewer could not see.
- **MED002 `thay thế thuốc chữa bệnh` as attested-in-statute.** Run 2 accepted it; run 6 rejects it. The reviewer disagrees with itself, so the owner decides the class.
- **NĐ 330 paragraph.** Its "text search finds no A05" sentence has no anchor of its own (a whole-file count, not a quote).
- Minor: the Điều 7 organization rider sits outside Điều 43; "tính năng" was dropped from the k4 đ statement.

`review.json` holds run 6 verbatim (`passed: false`) plus `author_notes_on_findings` and `previous_reviews`.

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
- Haiku ran the suite first and caught one stale count in `test_ukmc_knowledge.py` (59/59 instead of 61/61). After that fix and the final review, Opus reran the full suite; the output below is that last run.
- The builder check in `tests/test_ukmc_knowledge.py` resolves the builder as a sibling of the repo, so it is skipped inside a `.claude/worktrees/` checkout. It was also run against `~/Products/design-os-knowledge-builder`: 2 tests OK.

```text
$ python3 tools/sync_shared.py --check
sync_shared: 16 skills verified byte-identical to shared/
[exit 0]

$ python3 tools/build_examples.py --check
build_examples: 16 skills verified up-to-date
[exit 0]

$ python3 tools/verify_ukmc.py
FAIL: review.json did not pass independent review
files: 18 · anchors: 114 · failures: 1 · exempt blocks: 0
verified_claims: 61/61 · independent_sources: 26
Decision: CONTINUE_GAP
[exit 1]

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
Reason:   Deficiencies detected: Saturation not yet reached (low-delta rounds 0/3, delta 2.5%), A viable probe remains, Independent review has not passed. Probing further.
Hard Gates Passed: True
Saturation Passed: False
--------------------------------------------------
[exit 2]

$ python3 -m unittest discover -s tests
..................................................................
----------------------------------------------------------------------
Ran 66 tests in 5.488s

OK
[exit 0]

$ python3 scripts/self_check.py
ok: design-os-vietnamese self-check passed (16 skills, 18 UKMC.v1 modules)
[exit 0]
```

| Gate | Result |
|---|---|
| sync_shared, build_examples, self_check | pass |
| `verify_ukmc.py` | 61/61 claims, 26 sources; 1 failure = review not passed → CONTINUE_GAP (exit 1, expected) |
| `kb verify --claims` | 114 anchors, 0 failures |
| `kb gate` | **DEEPEN** (exit 2). Hard gates pass; saturation 0/3; a probe remains; review not passed |
| unittest | 66 tests OK |
| protected files (`rules_*.py`, `evals/`, `pyproject.toml`, `.pre-commit-hooks.yaml`, `.github/`, `README*`, `CHANGELOG.md`) | untouched |

## 10. Open questions for the owner

1. **Retire the two NĐ 13-era claims?** `claim-statutory-compliance` and `claim-cybersecurity-law` are still in `required_claim_ids`.
2. **Apply the protected-file replacements in §4?** These are the `rules_*.py` and `evals/` files; LEG007's logic can stay as is.
3. **Make `tools/verify_ukmc.py` read saturation and open probes?** It reports STOP_SUFFICIENT while the builder reports DEEPEN.
4. **Re-login to Codex** so a second, non-Grok reviewer can check this run.
5. **The next run must replace `review.json` before any STOP.** The gate does not check that a review covers atoms added after it.
6. **`tests/test_ukmc_knowledge.py` pins today's state** (`CONTINUE_GAP`/exit 1, `DEEPEN`/exit 2). It will fail by design once review and saturation pass; update it then.

## 11. Round 2 (owner rulings, 2026-10-28)

The owner ruled, via the parent session:
- run round 2;
- fix the stale citations in the protected `rules_*.py` and `evals/` now;
- retire the two NĐ 13-era claims and replace them.

**Work split:**

| Leg | Tier | Note |
|---|---|---|
| `rules_*.py` / `evals/` citation edits | Sonnet | test-first |
| Probe, rulings, knowledge edits, review of the Sonnet diff | Opus | |
| Knowledge grading | grok-4.7 | read-only; grades nothing it wrote |
| Gate rerun | Haiku | Opus reran the gates after the last edit |

| Measure | After round 1 | After round 2 |
|---|---|---|
| Verified claims (`verify_ukmc`) | 61/61 | **64/64** |
| Frozen source files | 26 | **28** |
| Anchors | 114 | **119** |
| Ledger atoms | 81 | **86** |
| `rules_*.py` / `evals/` / generator lines citing NĐ 13/2023 as current law, "03a", "A05" or "NĐ 38/2018" | 48 + 17 (guard test, before) | **0** (guard test, after; one detection pattern exempt) |
| Tests | 66 | **69** |
| Builder gate | DEEPEN | DEEPEN |
| Latest review | run 6 passed=false | run 7 passed=false |

### 11.1 The four open review items

| Item | Outcome | Evidence |
|---|---|---|
| `claim-ads-law-75-repeals` | **Resolved.** Split into the k25 repeal atom plus a new atom for Điều 1 k4. Run 7 accepted the split, but found "keeps its 2012 wording" overreaching, since earlier amending laws exist; that phrase was removed after the review (disclosed in `review.json`) | full Điều 1: k4 rewrites only k3 and k10; "khoản 11" occurs 0 times |
| `claim-fin-law56-register-status` | **Resolved.** Narrowed to the dates; the "no replacement" part is now its own atom on frozen relation record 28. Not flagged in run 7 | source 25 header; source 28 |
| MED002 `thay thế thuốc chữa bệnh` class | **Owner-decided (2026-10-28): `statutory`** (see §12). Earlier status: rejected with evidence, owner decision needed. Run 6 rejected `attested-in-statute` and run 7 rejected `statutory`. By the file's definitions, attested needs a text that does not regulate the subject (NĐ 15 does), and proposed needs no frozen source (one exists). Set to `statutory` with the note "mandated in negated form; only the affirmative fires" | `evidence_classes` in `rule-variant-tables.json` |
| NĐ 330 "no A05 in the texts" sentence | **Resolved: removed.** The guidance keeps only the statutory term | — |

### 11.2 Probe: what replaced Luật 56/2024?

**Nothing the register names.** vbpl.vn's relation record ("Lược đồ") for Luật 56/2024 gives the end date 01/01/2026 but lists **0** acts that end it in full. The record for Luật Chứng khoán 54/2019 lists exactly two amending acts, Luật 56/2024 and NĐ 200/2026 (private corporate bonds), and none that ends the Law. Both records are frozen as sources 27–28 (round 11). So on the register, Điều 91 k1 still stands as the FIN001 basis. Run 7 notes that the records do not mention Điều 91 itself; that sentence is open (§11.4).

### 11.3 Claims replaced (owner ruling)

`claim-statutory-compliance` and `claim-cybersecurity-law` were removed from `required_claim_ids` and recorded under `retired_claim_ids` with the reason. They are replaced by:
- `claim-pdpd-nd356-scope` (NĐ 356 Điều 1);
- `claim-pdpd-breach-notice-content` (NĐ 356 Điều 28 k1 a–d), alongside the existing `claim-pdpd-breach-72h` (Luật 91 Đ23 k1).

The retired atoms stay in the ledger. The modules cite them only under "Historical".

### 11.4 Rules and evals (commit 121042d)

- **Coverage:** SEC001/SEC006, EDU010, LND002, PROD004, LEG007 and FIN001 messages and hints, 10 eval pairs, 4 trigger-query lines, and 2 generators. Examples were regenerated.
- **Unchanged:** `expected_rules` and LEG007/FIN001 detection.
- **One detection change, accepted by Opus:** SEC001 also accepts the statutory phrase "cơ quan chuyên trách bảo vệ dữ liệu cá nhân". The updated good copy uses it.
- **Guard test:** the new `tests/test_current_pdpd_citations.py` failed before the edits (48 + 17 offenders) and passes after.
- **`A0[5]` rejected.** The Sonnet draft got around the test with an `A0[5]` regex, and Opus rejected that as obfuscation. The literal legacy pattern `Cục\s+A05|A05` is back, with an explicit, commented exemption in the test.
- **Open from run 7:** 8 module sentences need their own anchors:
  - finance §3: Điều 12 has no guarantee clause; the variant words; "FIN001 cites"; Điều 91 still the basis;
  - statutory §1: a non-historical paragraph anchored only to a corpus file; the Luật 75 paragraph;
  - statutory §2: the transition date; "NĐ 330 sets the fines".
  - Plus minor overreaches: the Điều 7 rider, "must match", "FIN001 cites".

### 11.5 Still red, and why

- **`kb gate` DEEPEN / `verify_ukmc` CONTINUE_GAP.** Saturation is 0/3, because rounds 11–12 added new material. Probes remain (KDBĐS lost provisions, the NĐ 15 replacement, dictionaries). Review run 7 is passed=false.
- **No second reviewer: Codex login expired.** Owner-manual.
- **Next run:** fix the 8 unanchored sentences, get the owner's call on the MED002 class, then a fresh full-scope review on a frozen state (the gate does not notice a review older than the atoms).

### 11.6 Verification after the last edit (round 2)

Haiku ran the suite and Opus checked the raw file. Screenshot: [knowledge-261028-2016-gates-terminal-r2.png](knowledge-261028-2016-gates-terminal-r2.png).

```text
$ python3 tools/sync_shared.py --check
sync_shared: 16 skills verified byte-identical to shared/
[exit 0]

$ python3 tools/build_examples.py --check
build_examples: 16 skills verified up-to-date
[exit 0]

$ python3 tools/verify_ukmc.py
FAIL: review.json did not pass independent review
files: 18 · anchors: 119 · failures: 1 · exempt blocks: 0
verified_claims: 64/64 · independent_sources: 28
Decision: CONTINUE_GAP
[exit 1]

$ env PYTHONPATH=$HOME/Products/design-os-knowledge-builder/src python3 -m knowledge_builder.cli verify ./knowledge --claims
[WARN] no ontology.yaml: legacy mode, UKMC.v1 checks only
files: 18
anchors: 119
failures: 0
exempt blocks: 0
[exit 0]

$ env PYTHONPATH=$HOME/Products/design-os-knowledge-builder/src python3 -m knowledge_builder.cli gate --root ./knowledge --run-id vn-design-os-261026
[*] Evaluating Stopping Gate for run: vn-design-os-261026
--------------------------------------------------
Decision: DEEPEN
Reason:   Deficiencies detected: Saturation not yet reached (low-delta rounds 0/3, delta 3.6%), A viable probe remains, Independent review has not passed. Probing further.
Hard Gates Passed: True
Saturation Passed: False
--------------------------------------------------
[exit 2]

$ python3 -m unittest discover -s tests
.....................................................................
----------------------------------------------------------------------
Ran 69 tests in 5.927s

OK
[exit 0]

$ python3 scripts/self_check.py
ok: design-os-vietnamese self-check passed (16 skills, 18 UKMC.v1 modules)
[exit 0]
```

Protected packaging files, untouched: `pyproject.toml`, `.pre-commit-hooks.yaml`, `.github/`, `README*`, `CHANGELOG.md`, `vi_design_os/`, `tests/test_pip_packaging_and_precommit.py`.

## 12. Round 3 (owner rulings, 2026-10-28)

**MED002 ruling.** The owner ruled `thay thế thuốc chữa bệnh` stays `statutory`, with this note: NĐ 15 Đ27 k3 a mandates the wording in negated form, and only the affirmative form fires. The ruling is recorded in the row as `owner_ruling`. A reviewer who disagrees with this class is a known, owner-decided item, not an open finding.

**The 8 run-7 sentences:**

| Sentence | Change |
|---|---|
| Finance: "Điều 12 … contains no guarantee clause" | Moved to its own paragraph with a new anchor, `claim-fin-luatck-d12-no-guarantee` (Luật CK Đ12 heading). The frozen article contains none of "bảo đảm", "đảm bảo", "cam kết" or "lợi nhuận" |
| Finance: "variants … express the same meaning" | Reworded: these are this module's proposed variants, not statutory wording |
| Finance: "NĐ 38/2018, the second basis FIN001 cites" | Repository claim removed from the sentence |
| Finance: "Điều 91 khoản 1 is still the basis" | Labelled as this module's inference |
| Statutory: corpus paragraph on Điều 8 k11 | Labelled "Historical (project corpus summary of 2026-10-26, superseded by the primary text below)" |
| Statutory: Luật 75 paragraph | Already narrowed after run 7 ("leaves khoản 11 untouched") |
| Statutory: Transition (date) | Luật 91 effective-date anchor added |
| Statutory: "NĐ 330 sets the fines" | Cut to the anchored fact: in force from 19/08/2026 (Điều 80) |

**Minor overreaches fixed in the ledger:**
- the A05 negatives now state the mechanical count (0 occurrences);
- "must match" → "must conform to (phải phù hợp với)", noting khoản 4 điểm đ;
- the Điều 7 rider removed from both fine atoms (Điều 7 has its own atom);
- "which FIN001 cites" removed;
- "together they are the current PDPD basis" removed.

**Saturation note.** Round 13 (one anchor atom, delta 1.2%) is a review correction, not a probe. It counts as low-delta in `run measure`, but it is not evidence of saturation.

### 12.1 Review run 8 (grok-4.7, read-only, frozen commit 88a89ff)

The verdict is recorded verbatim in `review.json`. The full record is `reviews/grok-8-round3-full-scope.json`, with packet and prompt alongside. Scope: 51 atoms, all variant rows, 31 module paragraphs.

| | Run 7 | **Run 8** |
|---|---|---|
| Atoms entailed | 42/50 | **50/51** |
| Wrong | 0 | **0** |
| Overreach | 8 (1 non-minor) | **1 (minor)** |
| Variant-table issues | 1 (MED002) | **0** (MED002 owner-decided; reviewer note only) |
| Unsupported module paragraphs/sentences | 8 sentences | **1 paragraph** |
| passed | false | **false** |

**Findings, both accepted and left for the next run.** The state was not edited after the review, so `review.json` describes exactly the committed state.
1. **Child-consent paragraph (cybersecurity).** Its anchor, Luật 91/2025 Điều 24 khoản 2, has the legal representative exercise the child's rights, except in the cases of Điều 19 khoản 1, which is not anchored. Fix: anchor Điều 19 khoản 1, or narrow the sentence to what khoản 2 says.
2. **`claim-med-ad-matches-declaration` (minor).** Khoản 4 điểm đ covers content beyond the declared *công dụng và tính năng*, not beyond khoản 2's *công dụng và tác dụng*. Fix: reword the khoản 4 rider.

### 12.2 Numbers, round 3 (before → after)

| | After round 2 | **After round 3** |
|---|---|---|
| Verified claims (`verify_ukmc`) | 64/64 | **65/65** |
| Independent sources | 28 | 28 |
| Anchors | 119 | **121** |
| Atoms | 86 | **87** |
| Review: unsupported module items | 8 sentences | **1 paragraph** |
| Tests | 69 | 69 |

### 12.3 Still red, and why

- **`kb gate` DEEPEN (exit 2).** Saturation is 1/3, and the one low-delta round is a review correction, not a probe. Probes remain open: KDBĐS lost provisions, the NĐ 15 replacement, lexicographic sources. Review run 8 is passed=false.
- **`verify_ukmc` CONTINUE_GAP (exit 1).** Its only failure is review run 8.
- The tests stay at the honest state (verify exit 1, gate exit 2). Nothing passed, so `tests/test_ukmc_knowledge.py` is unchanged.
- **Owner-manual:** Codex re-login, so that a second, non-Grok reviewer can run.

### 12.4 Verification after the last edit (round 3)

All 7 commands ran from the worktree after the `review.json` update. Exit codes:

| Command | Exit | Result |
|---|---|---|
| `sync_shared --check` | 0 | 16 skills byte-identical |
| `build_examples --check` | 0 | 16 skills up to date |
| `verify_ukmc.py` | 1 (expected) | 65/65 claims, 28 sources, 121 anchors; 1 failure = review → CONTINUE_GAP |
| `kb verify --claims` | 0 | 121 anchors, 0 failures |
| `kb gate` | 2 (expected) | DEEPEN; Hard Gates Passed: True; saturation 1/3 (delta 1.2%) |
| unittest | 0 | 69 tests OK |
| `self_check.py` | 0 | 16 skills, 18 UKMC.v1 modules |

Screenshot: `knowledge-261028-2016-gates-terminal-r3.png`.

## 13. Round 4 (last round of this run, 2026-10-28)

**Rebase.** The branch is rebased onto `origin/main` (24d0146: PR #4 rules fix plus PR #3 packaging). `121042d` dropped out as already applied (d89ea60), with no conflicts. Commit hashes before the rebase changed: the round-3 freeze 88a89ff is now e5c40e3, and the run-8 record is 643ffb1. Their trees are unchanged. After the rebase all gates held: 87 tests (5 skipped), DEEPEN, CONTINUE_GAP.

**The two run-8 fixes, nothing else** (freeze commit 0520afa):
1. **Child-consent paragraph** (`statutory-compliance-vi.md` 3.4.1). The unsupported tail was cut. The representative sentence now has its own anchor, the first sentence of Luật 91/2025 Điều 24 khoản 2, including its Điều 19 khoản 1 exception.
2. **`claim-med-ad-matches-declaration`** (2 atoms). The khoản 4 điểm đ rider now reads "content beyond the uses and features (công dụng, tính năng) recorded in the declaration needs scientific documentation".

No new probes or material were added. Anchors went from 121 to 122; claims stay at 65/65 and sources at 28.

### 13.1 Review run 9 (grok-4.7, read-only, frozen commit 0520afa)

The verdict is recorded verbatim in `review.json`. The record is `reviews/grok-9-round4-full-scope.json`, with packet and prompt alongside.

| | Run 8 | **Run 9** |
|---|---|---|
| Atoms entailed | 50/51 | **50/51** |
| Wrong | 0 | 0 |
| Overreach | 1 minor (med-ad) | **1 minor (med-endorsement, new)** |
| Variant-table issues | 0 | 0 |
| Unsupported paragraphs | 1 (child consent) | **1 (finance Luật 56, new)** |
| passed | false | **false** |

Both run-8 findings are gone. Run 9 raised two items that run 8 had passed on the same text. This reviewer's findings vary from run to run, so a single run is not a stable pass/fail signal.

1. **Finance: Luật 56 and Điều 12. This is a real conflict, not only a missing anchor.** The module says Luật 56's "only change to Điều 12 is khoản 3". The FIN001 `citation_note` in `data/rule-variant-tables.json` says Luật 56 amends Điều 12 **khoản 3 and khoản 4**, checked on vbpl.vn but not frozen. One of them is wrong. Next run: read item 20 of Luật 56 Điều 1 in the frozen text (source 25), then correct the module or the note.
2. **`claim-med-no-medical-endorsement` (minor).** Điều 27 khoản 2 bans the *instruments*: images, equipment, attire, names, letters, thank-you letters and articles. "May not use doctors" reads wider than the clause. Next run: name the instruments.

### 13.2 Still red, and why

- **`kb gate` DEEPEN (exit 2).** Saturation is 1/3 (delta 1.2%). Probes remain open: KDBĐS lost provisions, the NĐ 15 replacement, dictionaries. Review run 9 did not pass.
- **`verify_ukmc` CONTINUE_GAP (exit 1).** Its only failure is review run 9.
- **`tests/test_ukmc_knowledge.py` unchanged**, because nothing passed.
- **Owner-manual:** Codex re-login. A second, non-Grok reviewer would also help with the run-to-run variance above.

### 13.3 Verification after the last edit (round 4)

The 7 commands were rerun by Haiku after the `review.json` update; Opus checked the raw output. Exit codes:

| Command | Exit | Result |
|---|---|---|
| `sync_shared --check` | 0 | 16 skills byte-identical |
| `build_examples --check` | 0 | 16 skills up to date |
| `verify_ukmc.py` | 1 (expected) | 65/65 claims, 28 sources, 122 anchors; 1 failure = review → CONTINUE_GAP |
| `kb verify --claims` | 0 | 122 anchors, 0 failures |
| `kb gate` | 2 (expected) | DEEPEN; Hard Gates Passed: True; saturation 1/3 (delta 1.2%) |
| unittest | 0 | 87 tests OK (5 skipped) |
| `self_check.py` | 0 | 16 skills, 18 UKMC.v1 modules |

Screenshot: `knowledge-261028-2016-gates-terminal-r4.png`.

## 14. Round 5 (owner ruling 2026-10-29: Grok as the only reviewer)

**Rebase.** Nothing to do: `origin/main` is still 24d0146 (PR #5 not merged), and the branch was 0 behind.

**The two run-9 fixes, nothing else** (freeze commit c9fa997):
1. **Luật 56 / Điều 12.** Frozen source 25 settles it. Within Luật 56 Điều 1 (the Securities Law items), "Điều 12" occurs exactly once, at item 5 (khoản 3, market manipulation). Item 20 repeals Điều 23, khoản 3 Điều 48 and khoản 4–5 Điều 135, and inserts a phrase into Điều 7, 52 and 68. The "khoản 4 Điều 12" rewrite is item 4 of Luật 56 **Điều 2**, which amends the Accounting Law.
   - The **FIN001 `citation_note` was the wrong side** and is corrected.
   - Its stale "NĐ 38 not checked" sentence is also replaced with the frozen-source-24 finding the module already carries.
   - The finance module paragraph (3.4.1) now anchors item 20 and adds one anchored sentence on the Điều 2 item.
2. **`claim-med-no-medical-endorsement`.** The atom now names the instruments of Điều 27 khoản 2: images, equipment, attire, names, letters, thank-you letters and articles. The matching `MED005` sentence in the healthcare module (4.2.1) uses the same wording.

No new probes or material were added. Anchors went from 122 to 126; claims stay at 65/65 and sources at 28.

**Packet builder (mechanical, scratch tool).** Source 25's context now cuts at the amending law's own article headers. Before, a quoted inserted article ("Điều 31b.") truncated it. The context also prints a mechanical count of "Điều 12" next to "Điều 91". The healthcare section ends at the reworded `MED005` line, as before.

### 14.1 Review run 10 (grok-4.7, read-only, frozen commit c9fa997)

The verdict is recorded verbatim in `review.json` (`passed: true`, `post_review_edits: []`). The record is `reviews/grok-10-round5-full-scope.json`, with packet and prompt alongside.

| | Run 9 | **Run 10** |
|---|---|---|
| Atoms entailed | 50/51 | **50/51** |
| Wrong | 0 | 0 |
| Overreach | 1 minor (med-endorsement) | **1 minor (`claim-pdpd-nd356-scope`, new)** |
| Variant-table issues | 0 | 0 |
| Unsupported paragraphs | 1 (finance Luật 56) | **0** (33 reviewed) |
| passed | false | **true** |

New minor item: `claim-pdpd-nd356-scope` adds the law number 91/2025/QH15, which NĐ 356 Điều 1 does not print. Run 9 passed that same atom. It is left unedited so the frozen review stays valid; the next ledger edit should narrow it.

### 14.2 What changed in the tests

`tests/test_ukmc_knowledge.py` now asserts the real state: `verify_ukmc` exit 0, no `FAIL:` lines, `failures: 0`, `Decision: STOP_SUFFICIENT`. The builder-gate expectation stays at DEEPEN (exit 2); only its comment was updated.

### 14.3 Verification after the last edit (round 5)

The 7 commands were rerun by Haiku after the `review.json` and test update; Opus checked the raw output. Exit codes:

| Command | Exit | Result |
|---|---|---|
| `sync_shared --check` | 0 | 16 skills byte-identical |
| `build_examples --check` | 0 | 16 skills up to date |
| `verify_ukmc.py` | 0 | 65/65 claims, 28 sources, 126 anchors, 0 failures → **STOP_SUFFICIENT** |
| `kb verify --claims` | 0 | 126 anchors, 0 failures |
| `kb gate` | 2 (expected) | DEEPEN; Hard Gates Passed: True; saturation 1/3 (delta 1.2%); a viable probe remains |
| unittest | 0 | 87 tests OK (5 skipped) |
| `self_check.py` | 0 | 16 skills, 18 UKMC.v1 modules |

Screenshot: `knowledge-261028-2016-gates-terminal-r5.png`.

### 14.4 Still open
- **`kb gate` DEEPEN.** It needs 2 more low-delta rounds plus the open probes: KDBĐS lost provisions, the NĐ 15 replacement, dictionaries. These are real research rounds, not reruns.
- **Narrow `claim-pdpd-nd356-scope`**, then re-review.
- **Owner-manual:** Codex re-login, for a second reviewer.
