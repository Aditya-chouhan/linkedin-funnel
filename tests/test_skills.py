"""Unit tests for Agent Skills discovery, frontmatter, and catalog synchronization."""

import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class TestSkills(unittest.TestCase):
    def setUp(self):
        self.skills_dir = ROOT / "skills"
        self.catalog_path = self.skills_dir / "catalog.json"
        self.assertTrue(self.catalog_path.exists(), "catalog.json must exist")
        self.catalog = json.loads(self.catalog_path.read_text())["skills"]

    def test_catalog_skill_count(self):
        """Verify that all 50 skills are registered in catalog.json."""
        self.assertEqual(len(self.catalog), 50, "Expected exactly 50 registered skills")

    def test_no_duplicate_skill_names(self):
        """Ensure all skill names in catalog are strictly unique."""
        names = [s["name"] for s in self.catalog]
        self.assertEqual(len(names), len(set(names)), "Duplicate skill name found in catalog")

    def test_all_catalog_skills_exist_on_disk(self):
        """Ensure every skill in catalog has a corresponding SKILL.md file."""
        for skill in self.catalog:
            skill_md = ROOT / skill["path"]
            self.assertTrue(skill_md.exists(), f"Skill file does not exist: {skill_md}")

    def test_skill_frontmatter_integrity(self):
        """Verify that every SKILL.md has valid YAML frontmatter matching the catalog."""
        for skill in self.catalog:
            skill_md = ROOT / skill["path"]
            content = skill_md.read_text()
            fm_match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.DOTALL)
            self.assertIsNotNone(fm_match, f"Missing YAML frontmatter in {skill_md}")

            fm = fm_match.group(1)
            name_match = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
            desc_match = re.search(r"^description:\s*(.+)$", fm, re.MULTILINE)

            self.assertIsNotNone(name_match, f"Missing 'name' field in {skill_md}")
            self.assertIsNotNone(desc_match, f"Missing 'description' field in {skill_md}")

            self.assertEqual(
                name_match.group(1).strip(),
                skill["name"],
                f"Catalog name mismatch for {skill['name']}"
            )
            self.assertEqual(
                desc_match.group(1).strip(),
                skill["description"],
                f"Catalog description mismatch for {skill['name']}"
            )

    def test_discovery_symlinks(self):
        """Verify that .agents/skills and .claude/skills symlinks are correctly configured."""
        for alias in [".agents/skills", ".claude/skills"]:
            link_path = ROOT / alias
            self.assertTrue(link_path.is_symlink(), f"Discovery link {alias} is not a symlink")
            self.assertEqual(link_path.resolve(), self.skills_dir.resolve(), f"Wrong symlink target for {alias}")


if __name__ == "__main__":
    unittest.main()
