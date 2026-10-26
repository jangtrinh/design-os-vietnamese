# Contributing to DESIGN:OS Vietnamese (`CONTRIBUTING.md`)

Contributions to rules, domain glossaries, evaluation pairs (`evals/*/pairs.jsonl`), and `UKMC.v1` knowledge modules are welcome under the terms of the [PolyForm Shield License 1.0.0](LICENSE).

## Mandatory Pre-PR Verification Gates

Before opening a pull request, run the full deterministic verification suite locally:

```bash
# 1. Sync shared references & scripts across all 10 skills and rebuild examples.md
python3 tools/sync_shared.py
python3 tools/build_examples.py

# 2. Run the 33 unit, golden eval (339 pairs), QA regression, and UKMC.v1 tests
python3 -m unittest discover -s tests -v

# 3. Run the repository delivery and self-check gates
python3 scripts/self_check.py
python3 tools/verify_ukmc.py
```

All tests must exit `0` with zero warnings or drift before merging.
