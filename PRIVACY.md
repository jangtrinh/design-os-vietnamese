# Privacy Policy (`PRIVACY.md`)

`design-os-vietnamese` is a 100% local-first, zero-telemetry toolchain and AI agent skill suite.

## Core Privacy Guarantees

1. **Zero Telemetry & Zero Analytics**: Neither `validate_copy.py`, `check_i18n_parity.py`, `check_font_coverage.py`, `tools/verify_ukmc.py`, nor `scripts/self_check.py` makes any outbound network requests, collects usage analytics, or transmits telemetry.
2. **Local Execution Only**: All Vietnamese linguistic checks, statutory compliance validations, and `UKMC.v1` cryptographic verifications run strictly on your local machine using the Python 3.9+ standard library.
3. **Zero Third-Party Pip Dependencies**: The runtime requires zero third-party packages, eliminating supply-chain data exfiltration vectors.
4. **Data Sovereignty**: Your source code, contracts, medical notes, student evaluations, and localization catalogs (`en.json` / `vi.json`) never leave your workstation.
