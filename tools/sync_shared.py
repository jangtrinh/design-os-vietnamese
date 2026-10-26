#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Synchronize shared/references/*.md and shared/scripts/*.py into every skills/*/ folder.

Usage:
    python3 tools/sync_shared.py          # copy shared/* into skills/*/
    python3 tools/sync_shared.py --check  # verify all skills/*/ copies match shared/*
"""
from __future__ import annotations

import argparse
import hashlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SHARED_REFS = ROOT / "shared" / "references"
SHARED_SCRIPTS = ROOT / "shared" / "scripts"
SKILLS_DIR = ROOT / "skills"


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def render_synced_content(src: pathlib.Path) -> bytes:
    raw = src.read_text(encoding="utf-8")
    rel = src.relative_to(ROOT).as_posix()
    digest = _sha256_bytes(raw.encode("utf-8"))
    if src.suffix == ".md":
        stamp = f"<!-- synced from {rel} ({digest}) — edit shared/ source, not this copy -->\n"
        return (stamp + raw).encode("utf-8")
    if src.suffix == ".py":
        lines = raw.splitlines(keepends=True)
        stamp = f"# synced from {rel} ({digest}) — edit shared/ source, not this copy\n"
        # Insert after shebang and encoding comment
        insert_at = 0
        while insert_at < len(lines) and insert_at < 2 and lines[insert_at].startswith("#"):
            insert_at += 1
        out = "".join(lines[:insert_at]) + stamp + "".join(lines[insert_at:])
        return out.encode("utf-8")
    return raw.encode("utf-8")


def sync_all(check_only: bool = False) -> int:
    drifted = []
    skill_dirs = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())
    sources = [
        *(( src, "references" ) for src in sorted(SHARED_REFS.glob("*.md"))),
        *(( src, "scripts" ) for src in sorted(SHARED_SCRIPTS.glob("*.py"))),
    ]

    for skill in skill_dirs:
        for src, subdir in sources:
            dest = skill / subdir / src.name
            expected = render_synced_content(src)
            if check_only:
                if not dest.is_file() or dest.read_bytes() != expected:
                    drifted.append((dest.relative_to(ROOT).as_posix(), src.relative_to(ROOT).as_posix()))
            else:
                dest.parent.mkdir(parents=True, exist_ok=True)
                dest.write_bytes(expected)
                if src.suffix == ".py":
                    dest.chmod(0o755)

    if check_only:
        if drifted:
            for dest_rel, src_rel in drifted:
                print(f"drift: {dest_rel} does not match {src_rel} (run: python3 tools/sync_shared.py)", file=sys.stderr)
            return 1
        print(f"sync_shared: {len(skill_dirs)} skills verified byte-identical to shared/")
    else:
        print(f"sync_shared: synced {len(sources)} shared files across {len(skill_dirs)} skills")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true", help="verify without modifying files")
    args = ap.parse_args()
    return sync_all(check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
