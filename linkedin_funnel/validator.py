"""Verification and integrity validator for the LinkedIn Funnel template."""

import hashlib
import json
from pathlib import Path
import re
from typing import List, Tuple
from urllib.parse import unquote, urlsplit


def verify_repository(root_dir: Path) -> Tuple[bool, List[str]]:
    """Runs all integrity checks: catalog, skills, frontmatter, symlinks, links, and assets."""
    errors: List[str] = []

    def require(condition: bool, message: str):
        if not condition:
            errors.append(message)

    catalog_path = root_dir / "skills" / "catalog.json"
    if not catalog_path.exists():
        return False, ["Missing skills/catalog.json"]

    catalog = json.loads(catalog_path.read_text())["skills"]
    names = [s["name"] for s in catalog]
    require(len(names) == len(set(names)), "Duplicate skill names in catalog")

    actual = {p.parent.name for p in (root_dir / "skills").glob("*/SKILL.md")}
    require(set(names) == actual, "Catalog does not match bundled skills")

    for skill in catalog:
        path = root_dir / skill["path"]
        require(path == root_dir / "skills" / skill["name"] / "SKILL.md", f"Unexpected skill path: {skill['path']}")
        if not path.exists():
            errors.append(f"Missing skill file: {path}")
            continue

        fm = re.match(r"\A---\n(.*?)\n---(?:\n|$)", path.read_text(), re.S)
        require(fm is not None, f"Missing skill frontmatter: {path}")
        if fm:
            for key in ("name", "description"):
                m = re.search(rf"^{key}: (.+)$", fm.group(1), re.M)
                require(m is not None and m.group(1).strip() == skill[key].strip(), f"Catalog {key} mismatch: {path}")

    for alias in (".agents/skills", ".claude/skills"):
        link_path = root_dir / alias
        require(link_path.is_symlink(), f"Missing discovery symlink: {alias}")
        require(link_path.resolve() == (root_dir / "skills").resolve(), f"Wrong skill target: {alias}")

    for folder in (root_dir, root_dir / "context"):
        ag = folder / "AGENTS.md"
        cl = folder / "CLAUDE.md"
        if ag.exists() and cl.exists():
            require(ag.read_text() == cl.read_text(), f"Agent instructions diverge in {folder}")

    for path in root_dir.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = re.sub(r"^```.*?^```[^\n]*$", "", path.read_text(), flags=re.M | re.S)
        for target in re.findall(r"\]\(([^\s)]+)(?:\s+\"[^\"]*\")?\)", text):
            target = target.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            linked = (path.parent / unquote(parsed.path)).resolve()
            require(linked.is_relative_to(root_dir), f"Link escapes template: {path}: {target}")
            require(linked.exists(), f"Broken local link: {path.relative_to(root_dir)}: {target}")

    for path in root_dir.rglob("*.json"):
        if ".git" in path.parts:
            continue
        try:
            json.loads(path.read_text())
        except (ValueError, UnicodeError) as error:
            errors.append(f"Invalid JSON {path.relative_to(root_dir)}: {error}")

    manifest_path = root_dir / "assets" / "manifest.json"
    if manifest_path.exists():
        manifest = json.loads(manifest_path.read_text())
        for asset in manifest["assets"]:
            asset_path = root_dir / "assets" / asset["file"]
            require(asset_path.exists(), f"Missing asset: {asset_path.name}")
            if asset_path.exists():
                h = hashlib.sha256(asset_path.read_bytes()).hexdigest()
                require(h == asset["sha256"], f"Asset hash differs: {asset['file']}")

    return (len(errors) == 0), errors
