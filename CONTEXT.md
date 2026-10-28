# Domain Glossary & Context (`CONTEXT.md`)

## Canonical Terms

| Term | Definition | _Avoid_ |
|---|---|---|
| **Source-Available** | Licensing model under **PolyForm Shield License 1.0.0** where source code is publicly readable and modifiable for non-competing use. | `open-source`, `MIT License` (when describing `design-os-vietnamese` or `DESIGN:OS`) |
| **Universal Rule** | One of the 18 baseline rules (`NFC001`, `ENC001`, `CAL001`, `SYN001`, `LAW001`, `DIA001`, `TONE001`, `NUM001`–`NUM004`, `DATE001`, `PHONE001`, `ICU001`–`ICU002`, `PRO001`–`PRO002`) in `shared/scripts/validate_copy.py`. | `global heuristic` |
| **Writing context** | The relationship and situation of one person writing to a specific person (chat with friends, email to the boss, job application, document for executives), described by five facets: `relation`, `closeness`, `channel`, `purpose`, `reader`. Declared with `--context`; never applied on a guess. Complements the organisation-to-customer **register**. | `register` (for person-to-person writing), `tone` |
| **Context preset** | A named bundle over the writing-context facets in `shared/references/context-matrix.md` (10 in v1), with forbidden address terms, the rules it disables, and the `CTX001`–`CTX005` rules it enables. Marked `proposed`: a convention, not statute. | `profile`, `persona` |
| **Domain Rule Engine** | Domain-specific AST/regex module `skills/<skill>/scripts/rules_<domain>.py` dynamically loaded via `--domain <domain>` or from the skill's own `scripts/` directory. | `plugin script` |
| **Span Deduplication** | Rule that at most one `CAL001` finding is emitted per winning `(start, end)` character span on a line, merging distinct suggestions in deterministic order. | `duplicate calque emission` |
| **UKMC.v1 Module** | Markdown knowledge file in `knowledge/*.md` with YAML frontmatter (`contract: ukmc.v1`, `trust_tier: "verified"`) and `<!-- ease:source uri="..." sha256="..." quote="..." -->` provenance anchors. | `unverified notes` |
