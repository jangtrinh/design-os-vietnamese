# Use Cases & Gherkin Acceptance Criteria (`qa-issue-2-hardening`)

## UC-01: `--domain` CLI Flag Execution Across Shared and Skill Copies (Blocker)
```gherkin
Scenario: Running validate_copy.py with --domain loads domain rules without crashing
  Given the shared validator "shared/scripts/validate_copy.py" and all 10 skill validators "skills/*/scripts/validate_copy.py"
  When invoked with "--domain <domain>" for each of the 10 domains (ux, landing, tech, biz, finance, edu, healthcare, legal, hospitality, hr) and "--list-rules"
  Then the process exits with code 0
  And stderr contains no "Traceback" or "NameError"
  And stdout includes the domain-specific rule prefix (UX, LND, TECH, BIZ, FIN, EDU, MED, LEG, HOS, HR)

Scenario: Running README Quick Start command on calque fixture
  Given "tests/fixtures/qa/calque_readme_example.md"
  When "python3 shared/scripts/validate_copy.py tests/fixtures/qa/calque_readme_example.md --domain ux --register ux-microcopy" is executed
  Then the process exits with code 1 (because CAL001 error is found)
  And stderr contains no "Traceback" or "NameError"
  And stdout contains "1 error, 0 warnings"
```

## UC-02: `CAL001` Span Deduplication
```gherkin
Scenario: Overlapping or identical-span calques from builtin, glossary.md, and banned-phrases.md emit one finding
  Given "tests/fixtures/qa/calque_readme_example.md" containing "Làm ơn nhập của bạn mật khẩu"
  When validated by "shared/scripts/validate_copy.py"
  Then exactly 1 CAL001 finding is emitted at 1:1
  And the suggestion "Vui lòng nhập mật khẩu của bạn" appears once without duplicate repetition
  And the summary line reads "1 error, 0 warnings"
```

## UC-03: Source-Available Wording & License Consistency
```gherkin
Scenario: Repository documentation accurately reflects PolyForm Shield 1.0.0 source-available license
  Given "README.md", "README.vi.md", "docs/_config.yml", and "docs/QA-FINDINGS.md"
  When scanned for license terminology
  Then "README.md" describes the ecosystem as "source-available" (not "open-source")
  And "docs/_config.yml" links to "PolyForm Shield 1.0.0" (not "MIT")
  And "docs/QA-FINDINGS.md" states that the license is now PolyForm Shield 1.0.0 (resolved)
```

## UC-04: Repository-Wide Zero Personal Paths
```gherkin
Scenario: No file in the repository contains personal absolute paths
  Given all tracked files in the repository
  When scanned for "<personal-home-path>"
  Then only the negative-assertion string literals inside test files are allowed, and zero documentation, knowledge, or tool files contain "<personal-home-path>"
```
