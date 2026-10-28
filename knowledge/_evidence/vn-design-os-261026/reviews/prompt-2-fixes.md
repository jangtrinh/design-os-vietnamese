You are an independent reviewer (read-only). Do not modify any file. Read the single file review-packet-2.md in the current directory; it is self-contained.

Context: an earlier review of a Vietnamese statutory knowledge ledger flagged items. The author revised some statements, added two atoms, relabelled two variant-table rows and rewrote two module paragraphs. For three earlier findings the author disputes the finding and supplies the full article or whole-file counts instead (items 7, 10, 11): the earlier packet showed truncated or wrong context.

For each of items 1-11 judge ENTAILED, OVERREACH or WRONG against the full article shown (and, for negative claims, the whole-file counts). Check the two relabelled rows against the class definitions. Check the two module texts against the atoms and articles in the packet: flag any sentence that states more than the texts show.

Output ONLY a JSON object, no prose:
{"reviewed_items": <int>, "entailed": <int>, "overreach": [{"id": "...", "why": "..."}], "wrong": [{"id": "...", "why": "..."}], "variant_rows_ok": <bool>, "variant_note": "...", "module_text_ok": <bool>, "module_note": "...", "passed": <true only if wrong is empty, every overreach is minor, variant_rows_ok and module_text_ok>, "notes": "<=60 words"}
