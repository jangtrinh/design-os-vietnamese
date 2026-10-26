# Use Cases & Gherkin Acceptance Criteria (`v5-16-skill-expansion`)

## UC-01: Six New Domain Rule Engines Load & Validate Accurately
```gherkin
Scenario: Invoking validate_copy.py with any of the 16 domains loads its specific rule prefix
  Given "shared/scripts/validate_copy.py" and all 16 "skills/*/scripts/validate_copy.py" copies
  When invoked with "--domain <d> --list-rules" for each of the 16 domains (ux, landing, tech, biz, finance, edu, healthcare, legal, hospitality, hr, realestate, ecommerce, gov, insurance, cybersecurity, media)
  Then the process exits with code 0 and zero Traceback in stderr
  And stdout contains the expected domain rule IDs (REA001..006, ECOM001..006, GOV001..006, INS001..006, SEC001..006, MEDJ001..006)
  And cross-domain rules never leak across --domain switches
```

## UC-02: 489 Golden Evaluation Pairs Pass 100%
```gherkin
Scenario: Every golden evaluation pair across all 16 skills triggers expected rules on bad copy and zero rules on good copy
  Given 16 evaluation suites in "evals/*/pairs.jsonl" totaling >= 489 pairs
  When "python3 -m unittest tests.test_validate_copy.GoldenEvalPairsBenchmarkTests -v" runs
  Then every "bad" string triggers all of its "expected_rules"
  And every "good" string triggers zero rules from "expected_rules" and zero universal errors
```

## UC-03: 18 UKMC.v1 Knowledge Modules Pass Epistemic Gate
```gherkin
Scenario: Portable UKMC.v1 verifier validates all 18 knowledge modules
  Given 18 Markdown files in "knowledge/*.md" (excluding README.md)
  When "python3 tools/verify_ukmc.py" is executed
  Then exit code is 0, failures is 0, and Decision is "STOP_SUFFICIENT"
```

## UC-04: All Self-QA, Repo Delivery & SEO/AEO/GEO Harnesses Pass
```gherkin
Scenario: Documentation, plugin manifests, and GitHub Pages reflect all 16 skills with zero drift
  Given "README.md", "README.vi.md", "docs/index.html", "docs/cookbook.md", "llms.txt", and plugin manifests
  When "scripts/self_check.py", "verify-repo-delivery.py", "seo-aeo-geo-harness.py", and "unittest discover -s tests -v" run
  Then all checks exit 0 with zero missing reference files, zero phantom rule IDs, and zero personal paths
```
