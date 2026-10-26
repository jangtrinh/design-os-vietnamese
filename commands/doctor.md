---
description: Diagnose DESIGN:OS Vietnamese installation, plugin manifests, 10 skill packs, and local verification gates
allowed-tools: Bash, Read, Glob
---

# `design-os-vietnamese` `/doctor` Diagnostics

Run a read-only diagnostic check of the `design-os-vietnamese` installation and repository health. Do **not** modify, create, or delete any files during this check.

## Steps

1. **Run the deterministic self-check script** when inside a `design-os-vietnamese` checkout:
   ```bash
   python3 scripts/self_check.py
   ```
2. **Run the UKMC.v1 knowledge base verifier**:
   ```bash
   python3 tools/verify_ukmc.py
   ```
3. **Check installed skill locations** across active agent harnesses:
   - Claude Code: `~/.claude/skills/vn-design-system-ux/SKILL.md` or `.claude-plugin/marketplace.json`
   - OpenAI Codex: `~/.codex/skills/vn-design-system-ux/SKILL.md` or `.codex-plugin/plugin.json`
   - Gemini CLI / Antigravity: `~/.gemini/config/skills/vn-design-system-ux/SKILL.md`
   - Cross-agent `.agents`: `~/.agents/skills/vn-design-system-ux/SKILL.md`
4. **Report a concise health table** covering:
   - Manifest integrity (`.claude-plugin`, `.codex-plugin`, `.agents/plugins`, `.factory-plugin`)
   - All 10 production skills (`skills/*/SKILL.md`)
   - Trust & privacy governance (`PRIVACY.md`, `SECURITY.md`, `LICENSE`)
   - Deterministic linter readiness (`python3 shared/scripts/validate_copy.py --list-rules`)
