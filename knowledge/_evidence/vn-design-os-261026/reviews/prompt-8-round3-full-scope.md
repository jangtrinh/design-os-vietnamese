You are an independent reviewer (read-only). Do not modify any file. Read review-packet-final3.md in the current directory; it is self-contained and reflects one frozen commit of a Vietnamese statutory knowledge base.

Part A (51 ledger atoms): judge each ENTAILED, OVERREACH or WRONG against its quote and the shown source article. Check article/clause/point numbers, dates, amounts and every negative claim; mechanical counts printed with an atom or in its context may support whole-article or whole-file negatives. Statements of the form "Second publisher / Official vbpl.vn text reproduces the same statutory wording: X" are judged on X.
Part B (variant table): every row with class "statutory" or "attested-in-statute" must be supported by its evidence quote; no unsourced row may be labelled statutory.
Part C (module paragraphs): every sentence must be supported by that paragraph's own anchors. Sentences the paragraph labels as an inference, as the module's or linter's own reading or proposed variants, or as Historical are judged as labelled.
Part D lists owner-decided items: you may note disagreement in "notes", but do not list them as findings or count them against "passed".

Output ONLY a JSON object, no prose:
{"reviewed_atoms": <int>, "entailed": <int>, "overreach": [{"id": "...", "minor": <bool>, "why": "..."}], "wrong": [{"id": "...", "why": "..."}], "variant_table_issues": [{"rule": "...", "form": "...", "why": "..."}], "paragraphs_reviewed": <int>, "unsupported_paragraphs": [{"paragraph_start": "<first 60 chars>", "why": "..."}], "passed": <true only if wrong, variant_table_issues and unsupported_paragraphs are empty and every overreach is minor>, "notes": "<=60 words"}
