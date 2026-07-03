#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "cosmosmith"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / ".agents" / "plugins" / "marketplace.json",
    PLUGIN / ".codex-plugin" / "plugin.json",
    PLUGIN / "templates" / "generated-project" / "AGENTS.md",
    PLUGIN / "templates" / "generated-project" / "CLAUDE.md",
    PLUGIN / "templates" / "artifacts" / "idea-brief.md",
    PLUGIN / "templates" / "artifacts" / "research-brief.md",
    PLUGIN / "templates" / "artifacts" / "proposal.md",
    PLUGIN / "templates" / "artifacts" / "design.md",
    PLUGIN / "templates" / "artifacts" / "task-ledger.md",
    PLUGIN / "templates" / "artifacts" / "qa-report.md",
    PLUGIN / "templates" / "artifacts" / "release-readiness.md",
    PLUGIN / "references" / "standards.md",
]

SKILLS = [
    "cosmosmith-product-discovery",
    "cosmosmith-market-research",
    "cosmosmith-spec-governor",
    "cosmosmith-architect",
    "cosmosmith-ui-ux-designer",
    "cosmosmith-frontend-engineer",
    "cosmosmith-backend-engineer",
    "cosmosmith-qa-verifier",
    "cosmosmith-devops-release",
    "cosmosmith-governance-review",
    "cosmosmith-project-rules",
]


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    raise SystemExit(1)


def check_file(path: Path) -> None:
    if not path.is_file():
        fail(f"missing required file: {path.relative_to(ROOT)}")
    print(f"PASS file: {path.relative_to(ROOT)}")


def check_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(data, dict):
        fail(f"JSON root must be object: {path.relative_to(ROOT)}")
    print(f"PASS json: {path.relative_to(ROOT)}")
    return data


def check_skill(skill: str) -> None:
    path = PLUGIN / "skills" / skill / "SKILL.md"
    check_file(path)
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"skill missing frontmatter: {skill}")
    if f"name: {skill}" not in text:
        fail(f"skill name mismatch: {skill}")
    if "description:" not in text:
        fail(f"skill missing description: {skill}")
    if "TODO" in text or "[TODO" in text:
        fail(f"skill contains TODO placeholder: {skill}")
    print(f"PASS skill: {skill}")


def main() -> int:
    for path in REQUIRED_FILES:
        check_file(path)

    marketplace = check_json(ROOT / ".agents" / "plugins" / "marketplace.json")
    if marketplace.get("name") != "cosmosmith":
        fail("marketplace name must be cosmosmith")
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("marketplace must list plugins")
    if plugins[0].get("name") != "cosmosmith":
        fail("first marketplace plugin must be cosmosmith")

    manifest = check_json(PLUGIN / ".codex-plugin" / "plugin.json")
    if manifest.get("name") != "cosmosmith":
        fail("plugin name must be cosmosmith")
    if not re.match(r"^\d+\.\d+\.\d+", str(manifest.get("version", ""))):
        fail("plugin version must be semver-like")
    if manifest.get("skills") != "./skills/":
        fail("plugin skills path must be ./skills/")

    for skill in SKILLS:
        check_skill(skill)

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8")
            if "TODO" in text or "[TODO" in text:
                fail(f"placeholder remains in {path.relative_to(ROOT)}")

    print("Cosmosmith release validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
