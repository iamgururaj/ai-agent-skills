"""Validate this repository's skill metadata and inline local Markdown links."""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    errors = []
    skills = sorted((root / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills/*/SKILL.md files found")
    for path in skills:
        content = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---(?:\n|$)", content, re.S)
        label = path.relative_to(root)
        if not match:
            errors.append(f"{label}: missing YAML frontmatter")
            continue
        try:
            metadata = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{label}: invalid YAML: {exc}")
            continue
        if not isinstance(metadata, dict):
            errors.append(f"{label}: frontmatter must be a mapping")
            continue
        name = metadata.get("name")
        if (not isinstance(name, str) or len(name) > 64
                or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                or name != path.parent.name):
            errors.append(f"{label}: name must match its lowercase hyphenated folder")
        description = metadata.get("description")
        if (not isinstance(description, str) or not description.strip()
                or len(description) > 1024):
            errors.append(f"{label}: description must be 1-1024 characters")
        if not content[match.end():].strip():
            errors.append(f"{label}: empty instructions")
        if "[TODO:" in content:
            errors.append(f"{label}: unfinished scaffold placeholder")
    # This repository uses inline Markdown links; validate file targets, not anchors.
    for path in [root / "README.md", *root.glob("evals/*.md"), *skills]:
        if not path.is_file():
            errors.append(f"Missing {path.relative_to(root)}")
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
            target = target.strip().strip("<>")
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            resolved = (path.parent / unquote(parts.path)).resolve()
            if not resolved.is_relative_to(root) or not resolved.is_file():
                errors.append(f"{path.relative_to(root)}: missing/unsafe link {target}")
    return skills, errors


if __name__ == "__main__":
    repo = Path(__file__).resolve().parents[1]
    files, failures = validate(repo)
    for failure in failures:
        print(f"ERROR: {failure}")
    if not failures:
        print(f"Validated {len(files)} skill(s) and local Markdown file links.")
    sys.exit(bool(failures))
