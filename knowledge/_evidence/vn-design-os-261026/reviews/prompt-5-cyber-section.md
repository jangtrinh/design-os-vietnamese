You are an independent reviewer (read-only). Do not modify any file. Read review-packet-3.md in the current directory; it is self-contained.

It holds two sections of a Vietnamese statutory knowledge module. Each PARAGRAPH is followed by its ANCHORs (cited quote plus the full article it sits in). Anchors to project corpus files (01-06) support only sentences labelled Historical.

For each PARAGRAPH, judge whether every sentence is supported by its own anchors (quote plus the shown article). Flag any sentence that states more than they show. Sentences that the paragraph explicitly labels as the linter's own reading, or as Historical, are judged as labelled.

Output ONLY a JSON object, no prose:
{"paragraphs_reviewed": <int>, "supported": <int>, "unsupported": [{"paragraph_start": "<first 60 chars>", "why": "..."}], "minor": [{"paragraph_start": "...", "why": "..."}], "passed": <true only if unsupported is empty>, "notes": "<=50 words"}
