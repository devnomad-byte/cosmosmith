#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "cosmosmith"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "README.zh-CN.md",
    ROOT / "LICENSE",
    ROOT / "package.json",
    ROOT / "bin" / "cosmosmith.mjs",
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


def check_text(path: Path, needle: str) -> None:
    text = path.read_text(encoding="utf-8")
    if needle not in text:
        fail(f"missing `{needle}` in {path.relative_to(ROOT)}")
    print(f"PASS text: {path.relative_to(ROOT)} contains {needle}")


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

    package = check_json(ROOT / "package.json")
    if package.get("name") != "cosmosmith":
        fail("package name must be cosmosmith")
    bin_field = package.get("bin")
    if not isinstance(bin_field, dict) or bin_field.get("cosmosmith") != "./bin/cosmosmith.mjs":
        fail("package bin must expose ./bin/cosmosmith.mjs")

    check_text(ROOT / "README.md", "npx cosmosmith init")
    check_text(ROOT / "README.zh-CN.md", "npx cosmosmith init")

    for skill in SKILLS:
        check_skill(skill)

    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml"}:
            text = path.read_text(encoding="utf-8")
            if "TODO" in text or "[TODO" in text:
                fail(f"placeholder remains in {path.relative_to(ROOT)}")

    smoke_dir = ROOT / ".tmp" / "validate-init"
    if smoke_dir.exists():
        shutil.rmtree(smoke_dir)
    result = subprocess.run(
        [
            "node",
            str(ROOT / "bin" / "cosmosmith.mjs"),
            "init",
            "--all",
            "--dir",
            str(smoke_dir),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    if result.returncode != 0:
        fail(f"cosmosmith init smoke test failed:\n{result.stdout}")
    for relative in [
        "AGENTS.md",
        "CLAUDE.md",
        "task.md",
        "proposal.md",
        "design.md",
        "docs/cosmosmith/idea-brief.md",
        "docs/cosmosmith/research-brief.md",
        ".cursor/rules/cosmosmith.mdc",
        ".github/copilot-instructions.md",
        ".opencode/AGENTS.md",
        ".trae/rules/cosmosmith.md",
    ]:
        if not (smoke_dir / relative).is_file():
            fail(f"init smoke test missing {relative}")
    print("PASS smoke: cosmosmith init --all generated expected files")

    print("Cosmosmith release validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
