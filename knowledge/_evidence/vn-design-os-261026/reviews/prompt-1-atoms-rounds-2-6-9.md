You are an independent reviewer (read-only). Do not modify any file. Read the single file review-packet.md in the current directory; it is self-contained. It holds 43 knowledge-ledger atoms about Vietnamese statutes (each: statement, exact quote, and the full source article around the quote), the rule variant tables, and one module paragraph about a government agency.

A. For each atom judge: ENTAILED (the statement follows from the quote plus the shown article), OVERREACH (adds a fact the text does not say), or WRONG. Check article/clause/point numbers against the headings in the shown context, dates, fine amounts, and every negative claim ("no upper bound", "does not name", "none of ... amends", "only defines"). Statements of the form "Second publisher / Official vbpl.vn text reproduces the same statutory wording: X" are judged on X.
B. In the variant tables, check every row with class "statutory" or "attested-in-statute" is supported by its evidence quote, and no unsourced row is labelled statutory.
C. Check the agency paragraph against NĐ 356 Điều 39 and the NĐ 330 Điều 55 atom.

Output ONLY a JSON object, no prose:
{"reviewed_atoms": <int>, "entailed": <int>, "overreach": [{"id": "...", "why": "..."}], "wrong": [{"id": "...", "why": "..."}], "variant_table_issues": [{"rule": "...", "form": "...", "why": "..."}], "agency_paragraph_ok": <bool>, "agency_note": "...", "passed": <true only if wrong is empty, every overreach is minor, and agency_paragraph_ok>, "notes": "<=60 words"}
