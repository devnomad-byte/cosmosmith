# Cosmosmith

Cosmosmith is a universal initializer and Codex plugin for turning rough ideas into researched specs, task ledgers, implementation slices, verification evidence, and release readiness.

It is designed for multi-agent work across Codex, Claude Code, Cursor, GitHub Copilot, OpenCode, Trae, and similar AI coding tools.

Chinese documentation: [README.zh-CN.md](README.zh-CN.md)

## Quick Start

Run this in any project:

```bash
npx cosmosmith init
```

This creates:

- `AGENTS.md`
- `task.md`
- `proposal.md`
- `design.md`
- `docs/cosmosmith/idea-brief.md`
- `docs/cosmosmith/research-brief.md`

Generate adapters for every supported tool:

```bash
npx cosmosmith init --all
```

Or choose specific adapters:

```bash
npx cosmosmith init --claude --cursor --copilot
```

Useful options:

```bash
npx cosmosmith init --dir ./my-project
npx cosmosmith init --all --force
npx cosmosmith init --all --dry-run
```

## Editor / Agent Support

| Tool | Command |
| --- | --- |
| Generic agents | `npx cosmosmith init` |
| Claude Code | `npx cosmosmith init --claude` |
| Cursor | `npx cosmosmith init --cursor` |
| GitHub Copilot | `npx cosmosmith init --copilot` |
| OpenCode | `npx cosmosmith init --opencode` |
| Trae | `npx cosmosmith init --trae` |
| Everything | `npx cosmosmith init --all` |

Cosmosmith treats `AGENTS.md` as the canonical project constitution. Tool-specific files are adapters.

## Codex Plugin

Codex users can also install Cosmosmith as a native plugin:

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
codex plugin add cosmosmith@cosmosmith
```

Start a new Codex thread after installation so the new skills are loaded.

## Skills

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
- `cosmosmith-project-rules`: generate project instruction adapters.

## Typical Flow

1. Clarify a rough idea with `cosmosmith-product-discovery`.
2. Research competitors and current constraints with `cosmosmith-market-research`.
3. Create `proposal.md`, `design.md`, and `task.md` with `cosmosmith-spec-governor`.
4. Review architecture and UX with `cosmosmith-architect` and `cosmosmith-ui-ux-designer`.
5. Implement frontend/backend tasks in small slices.
6. Verify with `cosmosmith-qa-verifier`.
7. Prepare release readiness with `cosmosmith-devops-release`.
8. Run `cosmosmith-governance-review` before marking tasks done.

## What `init` Writes

Default:

```text
AGENTS.md
task.md
proposal.md
design.md
docs/cosmosmith/idea-brief.md
docs/cosmosmith/research-brief.md
```

With `--all`:

```text
CLAUDE.md
.cursor/rules/cosmosmith.mdc
.github/copilot-instructions.md
.opencode/AGENTS.md
.trae/rules/cosmosmith.md
```

Existing files are skipped by default. Use `--force` to overwrite generated files.

## Repository Layout

```text
bin/cosmosmith.mjs
package.json
.agents/plugins/marketplace.json
plugins/cosmosmith/
  .codex-plugin/plugin.json
  skills/
  templates/
scripts/validate_release.py
```

## Development

Validate the release package:

```bash
npm run validate
```

Smoke-test the initializer:

```bash
npm run smoke:init
```

Validate the Codex plugin:

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

## License

MIT

