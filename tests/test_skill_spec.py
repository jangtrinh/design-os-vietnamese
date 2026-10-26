#!/usr/bin/env python3
"""Structural, metadata, link-resolution, and sovereignty verification for all 6 skills."""

from __future__ import annotations

import re
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS = (
    "vn-design-system-ux",
    "vietnamese-landing-copy",
    "vietnamese-tech-writing",
    "vietnamese-business-comms",
    "vietnamese-finance-copy",
    "vietnamese-education-copy",
)
# Constructed dynamically so even the test file never contains the literal vendor token.
FORBIDDEN_TOKEN = "".join(("trus", "sary"))
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)#]+)(?:#[^)]*)?\)")


class SkillSpecificationAndSovereigntyTests(unittest.TestCase):
    def test_zero_external_vendor_references_across_entire_repository(self) -> None:
        offenders: list[str] = []
        for path in REPO_ROOT.rglob("*"):
            if not path.is_file():
                continue
            if ".git" in path.parts or "__pycache__" in path.parts:
                continue
            try:
                content = path.read_text(encoding="utf-8")
            except UnicodeDecodeError:
                continue
            if FORBIDDEN_TOKEN in content.lower():
                offenders.append(str(path.relative_to(REPO_ROOT)))
        self.assertEqual(
            offenders,
            [],
            f"Found forbidden external vendor token in files: {offenders}",
        )

    def test_all_six_skills_have_valid_frontmatter_and_resolved_links(self) -> None:
        for skill in SKILLS:
            skill_dir = REPO_ROOT / "skills" / skill
            skill_md = skill_dir / "SKILL.md"
            self.assertTrue(skill_md.is_file(), f"Missing {skill_md}")
            text = skill_md.read_text(encoding="utf-8")
            self.assertTrue(text.startswith("---\n"), f"{skill}/SKILL.md missing YAML frontmatter")
            end_idx = text.find("\n---\n", 4)
            self.assertGreater(end_idx, 0, f"{skill}/SKILL.md unclosed YAML frontmatter")
            fm = text[4:end_idx]
            self.assertIn(f"name: {skill}", fm)
            self.assertIn("description:", fm)
            self.assertIn("https://github.com/jangtrinh/design-os-vietnamese", fm)

            # Check relative markdown links in SKILL.md resolve inside skill_dir
            body = text[end_idx + 5 :]
            for match in MD_LINK_RE.finditer(body):
                target = match.group(1).strip()
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                resolved = (skill_dir / target).resolve()
                self.assertTrue(
                    resolved.exists(),
                    f"{skill}/SKILL.md has broken relative link '{target}' -> {resolved}",
                )


if __name__ == "__main__":
    unittest.main()
