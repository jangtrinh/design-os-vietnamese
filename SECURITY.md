# Security Policy (`SECURITY.md`)

## Supported Versions

| Version | Supported |
| :--- | :--- |
| `4.0.x` | Yes |
| `< 4.0` | No |

## Security Architecture

- **Zero External Dependencies**: All linters (`validate_copy.py`, `check_i18n_parity.py`, `check_font_coverage.py`) and verification tools (`tools/verify_ukmc.py`, `scripts/self_check.py`) use only the Python 3.9+ standard library.
- **No Network I/O**: No runtime script opens sockets or performs HTTP requests.
- **Cryptographic Provenance**: All 12 `UKMC.v1` knowledge modules in `knowledge/` are pinned to SHA-256 hashes of primary regulatory and linguistic corpora in `knowledge/_evidence/`.

## Reporting a Vulnerability

Please report security issues via [GitHub Security Advisories](https://github.com/jangtrinh/design-os-vietnamese/security/advisories/new) or directly via the author profile at [github.com/jangtrinh](https://github.com/jangtrinh).
