You are an independent reviewer (read-only). Do not modify any file. Read review-packet-final2.md in the current directory; it is self-contained and reflects the committed state of a Vietnamese statutory knowledge base.

Part A (50 ledger atoms): judge each ENTAILED, OVERREACH or WRONG against its quote and the shown source article. Check article/clause/point numbers, dates, amounts and every negative claim (mechanical counts in the context may support whole-article or whole-file negatives). Statements of the form "Second publisher / Official vbpl.vn text reproduces the same statutory wording: X" are judged on X.
Part B (variant table): every row with class "statutory" or "attested-in-statute" must be supported by its evidence quote in the needed sense; no unsourced row may be labelled statutory.
Part C (module paragraphs): every sentence must be supported by that paragraph's own anchors. Sentences the paragraph labels as an inference, as the linter's own reading, or as Historical are judged as labelled.

Output ONLY a JSON object, no prose:
{"reviewed_atoms": <int>, "entailed": <int>, "overreach": [{"id": "...", "minor": <bool>, "why": "..."}], "wrong": [{"id": "...", "why": "..."}], "variant_table_issues": [{"rule": "...", "form": "...", "why": "..."}], "paragraphs_reviewed": <int>, "unsupported_paragraphs": [{"paragraph_start": "<first 60 chars>", "why": "..."}], "passed": <true only if wrong, variant_table_issues and unsupported_paragraphs are empty and every overreach is minor>, "notes": "<=60 words"}
