# Cosmosmith

Cosmosmith is a multi-agent skill system for turning rough ideas into researched specs, task ledgers, implementation slices, verification evidence, and release readiness.

It ships as a native Codex plugin and as a portable rules/templates kit for other AI coding tools.

Chinese documentation: [README.zh-CN.md](README.zh-CN.md)

## What It Adds

- `cosmosmith-product-discovery`: clarify a rough idea into an idea brief.
- `cosmosmith-market-research`: research competitors, analogues, standards, and external evidence.
- `cosmosmith-spec-governor`: convert briefs into `proposal.md`, `design.md`, and `task.md`.
- `cosmosmith-architect`: design system boundaries, data flow, reliability, and integrations.
- `cosmosmith-ui-ux-designer`: design flows, screens, states, accessibility, and visual direction.
- `cosmosmith-frontend-engineer`: implement frontend task slices with verification evidence.
- `cosmosmith-backend-engineer`: implement backend task slices with contracts and tests.
- `cosmosmith-qa-verifier`: verify tasks against acceptance criteria and record evidence.
- `cosmosmith-devops-release`: prepare build, CI, deployment, monitoring, and rollback.
- `cosmosmith-governance-review`: review artifacts for rule drift, missing evidence, and task completeness.
- `cosmosmith-project-rules`: generate `AGENTS.md` and optional editor adapters such as `CLAUDE.md`, Cursor rules, and Copilot instructions.

## Installation Matrix

| Tool | Support level | How to use Cosmosmith |
| --- | --- | --- |
| Codex | Native plugin | Install the marketplace and plugin. |
| Claude Code | Rules adapter | Copy or generate `AGENTS.md` and `CLAUDE.md`; use the skills as reference workflows. |
| Cursor | Rules adapter | Copy or generate `AGENTS.md` and `.cursor/rules/cosmosmith.mdc`. |
| GitHub Copilot | Instructions adapter | Copy or generate `AGENTS.md` and `.github/copilot-instructions.md`. |
| OpenCode | Portable skills/rules | Copy `AGENTS.md` and use `plugins/cosmosmith/skills/*` as skill folders if supported by your setup. |
| Trae | Project rules adapter | Copy or generate `AGENTS.md` and adapt it into Trae project rules. |

Codex is the native plugin target. Other tools use Cosmosmith through project rule files, generated templates, and portable `SKILL.md` workflows.

## Install for Codex

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
```

Then install the plugin:

```bash
codex plugin add cosmosmith@cosmosmith
```

Start a new Codex thread after installation so the new skills are loaded.

## Use with Claude Code

Cosmosmith treats `AGENTS.md` as the canonical cross-agent project constitution and `CLAUDE.md` as a Claude-specific adapter.

In a target project, ask Codex with Cosmosmith installed:

```text
Use $cosmosmith-project-rules to create AGENTS.md and CLAUDE.md for this repo.
```

Manual fallback:

1. Copy `plugins/cosmosmith/templates/generated-project/AGENTS.md` to your project root.
2. Copy `plugins/cosmosmith/templates/generated-project/CLAUDE.md` to your project root.
3. Ask Claude Code to follow `CLAUDE.md`; it points back to `AGENTS.md` as canonical.

## Use with Cursor

In a target project, ask Cosmosmith:

```text
Use $cosmosmith-project-rules to create AGENTS.md and Cursor rules for this repo.
```

Manual fallback:

1. Copy `plugins/cosmosmith/templates/generated-project/AGENTS.md` to `AGENTS.md`.
2. Copy `plugins/cosmosmith/templates/adapters/cursor/cosmosmith.mdc` to `.cursor/rules/cosmosmith.mdc`.

The Cursor rule is intentionally short. `AGENTS.md` remains the canonical source.

## Use with GitHub Copilot

Manual setup:

1. Copy `plugins/cosmosmith/templates/generated-project/AGENTS.md` to `AGENTS.md`.
2. Copy `plugins/cosmosmith/templates/adapters/copilot/copilot-instructions.md` to `.github/copilot-instructions.md`.

Keep Copilot instructions short and point back to `AGENTS.md`.

## Use with OpenCode

OpenCode-compatible setups can use the repository instructions and portable skill folders:

1. Copy `plugins/cosmosmith/templates/generated-project/AGENTS.md` to your project root.
2. If your OpenCode setup supports skill folders, copy `plugins/cosmosmith/skills/` into the location your setup expects.
3. Use the skill names in prompts, for example `cosmosmith-spec-governor`.

If your setup does not support portable skills directly, use the `SKILL.md` files as workflow references.

## Use with Trae

Trae users can still use Cosmosmith through project rules:

1. Copy `plugins/cosmosmith/templates/generated-project/AGENTS.md` into your project.
2. Convert the relevant sections into Trae project rules if your Trae workspace uses a different rule file format.
3. Keep `AGENTS.md` as the canonical source when possible.

## Typical Flow

1. Clarify a rough idea with `cosmosmith-product-discovery`.
2. Research competitors and current constraints with `cosmosmith-market-research`.
3. Create `proposal.md`, `design.md`, and `task.md` with `cosmosmith-spec-governor`.
4. Review architecture and UX with `cosmosmith-architect` and `cosmosmith-ui-ux-designer`.
5. Implement frontend/backend tasks in small slices.
6. Verify with `cosmosmith-qa-verifier`.
7. Prepare release readiness with `cosmosmith-devops-release`.
8. Run `cosmosmith-governance-review` before marking tasks done.

Example prompts:

```text
Use $cosmosmith-product-discovery to turn this idea into a brief: ...
```

```text
Use $cosmosmith-spec-governor to create proposal.md, design.md, and task.md.
```

```text
Use $cosmosmith-project-rules to create AGENTS.md and CLAUDE.md for this repo.
```

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/cosmosmith/
  .codex-plugin/plugin.json
  skills/
  templates/
scripts/validate_release.py
```

The plugin lives under `plugins/cosmosmith/` so this repository can act as a Codex marketplace.

## Development

Validate the release package:

```bash
python scripts/validate_release.py
```

Validate the Codex plugin:

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

## License

MIT
