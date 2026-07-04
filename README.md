# Cosmosmith

**Turn a rough idea into a governed multi-agent software workflow.**

Cosmosmith is a universal project initializer and Codex plugin for teams and solo builders who want AI agents to move from imagination to implementation with evidence. It gives a project a constitution, a task ledger, spec templates, editor adapters, and a mesh of role skills for product, research, architecture, UX, engineering, QA, DevOps, and governance.

[中文文档](README.zh-CN.md) | [npm package](https://www.npmjs.com/package/cosmosmith) | [GitHub](https://github.com/devnomad-byte/cosmosmith)

## Why Cosmosmith

Most agent workflows fail in the same place: the first idea is vague, roles are implicit, context drifts, and "done" is declared without evidence.

Cosmosmith turns that into an operating loop:

- **Prompt**: what is being asked, which role is acting, and what output is expected.
- **Context**: the selected files, research, constraints, decisions, and task state that matter.
- **Harness**: tests, scripts, checks, review gates, and release criteria.
- **Loop**: the feedback cycle from discovery to proposal, implementation, verification, release, and learning.

The philosophy is simple: **build worlds, not fragments**. Let a user start with a rough thought, then let agents turn it into artifacts, tasks, implementation slices, and verification evidence.

## Install In Any Project

Run Cosmosmith from npm:

```bash
npx cosmosmith@latest init
```

This writes the default project governance files:

```text
AGENTS.md
task.md
proposal.md
design.md
docs/cosmosmith/idea-brief.md
docs/cosmosmith/research-brief.md
```

Generate every supported editor/agent adapter:

```bash
npx cosmosmith@latest init --all
```

Generate only the adapters you need:

```bash
npx cosmosmith@latest init --claude --cursor --copilot
npx cosmosmith@latest init --opencode --trae
```

Target another directory:

```bash
npx cosmosmith@latest init --dir ./my-project --all
```

Preview or overwrite:

```bash
npx cosmosmith@latest init --all --dry-run
npx cosmosmith@latest init --all --force
```

Existing files are skipped by default. Use `--force` only when you intentionally want to replace generated files.

## What Gets Installed

Cosmosmith treats `AGENTS.md` as the canonical project constitution. Tool-specific files are thin adapters that point agents back to the same source of truth.

| Surface | Generated file | Command |
| --- | --- | --- |
| Generic agents / Codex project rules | `AGENTS.md` | `npx cosmosmith init` |
| Task ledger | `task.md` | `npx cosmosmith init` |
| Proposal template | `proposal.md` | `npx cosmosmith init` |
| Design template | `design.md` | `npx cosmosmith init` |
| Discovery notes | `docs/cosmosmith/idea-brief.md` | `npx cosmosmith init` |
| Research notes | `docs/cosmosmith/research-brief.md` | `npx cosmosmith init` |
| Claude Code | `CLAUDE.md` | `npx cosmosmith init --claude` |
| Cursor | `.cursor/rules/cosmosmith.mdc` | `npx cosmosmith init --cursor` |
| GitHub Copilot | `.github/copilot-instructions.md` | `npx cosmosmith init --copilot` |
| OpenCode | `.opencode/AGENTS.md` | `npx cosmosmith init --opencode` |
| Trae | `.trae/rules/cosmosmith.md` | `npx cosmosmith init --trae` |

## CLI Or Plugin?

Cosmosmith has two layers:

- **CLI initializer**: `npx cosmosmith init` adds rules, templates, and editor adapters to a project. This works in any repository.
- **Codex plugin**: installs the actual `$cosmosmith-*` role skills into Codex so the agent can load them as reusable workflows.

If you only need project rules and templates, the CLI is enough. If you want Codex to expose Cosmosmith role skills directly, install the plugin too.

## Codex Plugin Install

After cloning or publishing the marketplace entry, Codex users can install Cosmosmith as a native plugin:

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
codex plugin add cosmosmith@cosmosmith
```

Start a new Codex thread after installation so the new skills are loaded.

## Role Skills

The Codex plugin provides a role mesh. Each skill has its own responsibility, handoff artifacts, web-research trigger, and verification expectations.

| Skill | Role |
| --- | --- |
| `cosmosmith-product-discovery` | Clarifies a vague idea through Socratic dialogue and writes the idea brief. |
| `cosmosmith-market-research` | Searches current competitors, analogues, pricing, standards, risks, and external evidence. |
| `cosmosmith-spec-governor` | Converts briefs into `proposal.md`, `design.md`, and claimable `task.md` work. |
| `cosmosmith-architect` | Defines boundaries, data flow, reliability, security, integrations, and trade-offs. |
| `cosmosmith-ui-ux-designer` | Designs flows, screens, states, accessibility, and domain-appropriate interaction patterns. |
| `cosmosmith-frontend-engineer` | Claims frontend tasks, implements slices, verifies browser behavior, and records evidence. |
| `cosmosmith-backend-engineer` | Claims backend tasks, implements APIs/domain logic/persistence, and verifies contracts. |
| `cosmosmith-qa-verifier` | Turns acceptance criteria into reproducible QA evidence and reopens failing tasks. |
| `cosmosmith-devops-release` | Checks build, CI, environment, deployment, monitoring, rollback, and release readiness. |
| `cosmosmith-governance-review` | Reviews rule drift, missing evidence, task completeness, and role handoff health. |
| `cosmosmith-project-rules` | Creates or updates `AGENTS.md` and editor-specific rule adapters. |

## Typical Workflow

1. **Seed**: the user gives a rough idea.
2. **Discover**: `cosmosmith-product-discovery` asks sparse Socratic questions and writes `docs/cosmosmith/idea-brief.md`.
3. **Research**: `cosmosmith-market-research` gathers current external facts when competitors, standards, laws, libraries, or product expectations may matter.
4. **Specify**: `cosmosmith-spec-governor` writes `proposal.md`, `design.md`, and publishes tasks into `task.md`.
5. **Review**: architect and UX roles challenge the plan before implementation gets large.
6. **Build**: frontend and backend roles claim small tasks and update status as they work.
7. **Verify**: QA maps acceptance criteria to tests, manual checks, screenshots, or API evidence.
8. **Release**: DevOps validates build, configuration, deployment, monitoring, and rollback.
9. **Govern**: governance review checks that the project rules, tasks, artifacts, and evidence still agree.

## Example

```bash
mkdir my-world
cd my-world
npx cosmosmith@latest init --all
```

Then tell your agent:

```text
Use Cosmosmith. I want to build a quiet personal CRM for independent consultants.
Start with product discovery, then publish the first task ledger.
```

The expected shape is:

```text
docs/cosmosmith/idea-brief.md  -> clarified intent
docs/cosmosmith/research-brief.md -> sources, facts, inferences
proposal.md -> proposed world and first slice
design.md -> buildable plan
task.md -> claimable tasks with harness and evidence
```

## Verify Your Install

Run a dry install into a temporary folder:

```bash
npx cosmosmith@latest init --all --dir .tmp/cosmosmith-check
```

Check the generated files:

```bash
ls .tmp/cosmosmith-check
```

You should see `AGENTS.md`, `task.md`, `proposal.md`, `design.md`, `CLAUDE.md`, and `docs/cosmosmith/`.

## Development

Clone the repository and run:

```bash
npm run validate
npm run smoke:init
```

Validate the Codex plugin manifest with the Codex plugin creator validator:

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

Package preview:

```bash
npm pack --dry-run
```

## Repository Layout

```text
bin/cosmosmith.mjs                 # zero-dependency CLI
plugins/cosmosmith/.codex-plugin/  # Codex plugin manifest
plugins/cosmosmith/skills/         # role skills
plugins/cosmosmith/templates/      # generated project files and adapters
plugins/cosmosmith/references/     # shared standards
scripts/validate_release.py        # release validation harness
```

## Roadmap

- `--sample`: generate a tiny verified example task after init.
- Stronger post-init guidance that distinguishes project rules from runtime plugin skills.
- More editor adapters as agent rule conventions stabilize.
- Optional validators for task ledger consistency and artifact freshness.

## License

MIT
