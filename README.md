# Cosmosmith

**Give your AI coding agents a product team, an architecture desk, a task board, and a release gate in one command.**

Cosmosmith helps you turn a rough product idea into a governed multi-agent workflow. It initializes project rules, spec templates, task ledgers, editor adapters, and Codex role skills so agents can move from discovery to implementation with verification evidence instead of drifting through prompts.

[中文文档](README.zh-CN.md) | [npm](https://www.npmjs.com/package/cosmosmith) | [GitHub](https://github.com/devnomad-byte/cosmosmith)

## Start In 10 Seconds

```bash
npx cosmosmith@latest init --all
```

You get a project workspace for AI-assisted building:

```text
AGENTS.md                         project constitution for agents
task.md                           claimable task ledger with evidence fields
proposal.md                       product proposal template
design.md                         technical and UX design template
docs/cosmosmith/idea-brief.md      product discovery notes
docs/cosmosmith/research-brief.md  research notes
CLAUDE.md                         Claude Code adapter
.cursor/rules/cosmosmith.mdc       Cursor adapter
.github/copilot-instructions.md    GitHub Copilot adapter
.opencode/AGENTS.md                OpenCode adapter
.trae/rules/cosmosmith.md          Trae adapter
```

## Why Developers Use It

AI agents are fast, but fast code is not the same as a finished product. Cosmosmith gives the work a spine:

- **Clarify the idea** before implementation starts.
- **Split responsibilities** across product, research, architecture, UX, frontend, backend, QA, DevOps, and governance roles.
- **Publish tasks** into `task.md` so agents claim small pieces instead of wandering.
- **Require evidence** before a task can be marked done.
- **Share one rule source** across Codex, Claude Code, Cursor, Copilot, OpenCode, and Trae.

The core model is:

```text
Prompt -> Context -> Harness -> Loop
```

- Prompt: what the agent is being asked to do.
- Context: the files, research, constraints, and decisions that matter.
- Harness: tests, scripts, checks, and release gates.
- Loop: review, verification, feedback, and rule updates.

## CLI Or Plugin

Cosmosmith has two useful layers.

| Layer | What it does | When to use |
| --- | --- | --- |
| CLI initializer | Generates `AGENTS.md`, `task.md`, spec templates, and editor adapters. | Use this in any project. |
| Codex plugin | Adds `$cosmosmith-*` role skills to Codex. | Use this when you want Codex to load the role workflows directly. |

The CLI works everywhere:

```bash
npx cosmosmith init
npx cosmosmith@latest init
npx cosmosmith@latest init --all
npx cosmosmith@latest init --dir ./my-project --all
```

Useful options:

```bash
npx cosmosmith@latest init --claude --cursor --copilot
npx cosmosmith@latest init --opencode --trae
npx cosmosmith@latest init --all --dry-run
npx cosmosmith@latest init --all --force
```

Existing files are skipped by default. Use `--force` only when you intentionally want to overwrite generated files.

## Codex Plugin Install

Codex users can install the role skills as a native plugin:

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
codex plugin add cosmosmith@cosmosmith
```

Start a new Codex thread after installation so the new skills are loaded.

## Role Mesh

Cosmosmith is not just one prompt. It is a working set of roles that hand off artifacts to each other.

| Skill | What it helps the agent do |
| --- | --- |
| `cosmosmith-product-discovery` | Turn a vague idea into users, jobs, first slice, and acceptance criteria. |
| `cosmosmith-market-research` | Research competitors, analogues, standards, risks, and current external facts. |
| `cosmosmith-spec-governor` | Convert discovery into `proposal.md`, `design.md`, and claimable tasks. |
| `cosmosmith-architect` | Define boundaries, data flow, reliability, security, and integrations. |
| `cosmosmith-ui-ux-designer` | Design flows, screens, interaction states, accessibility, and visual direction. |
| `cosmosmith-frontend-engineer` | Implement frontend task slices and record verification evidence. |
| `cosmosmith-backend-engineer` | Implement APIs, domain logic, persistence, permissions, and contracts. |
| `cosmosmith-qa-verifier` | Turn acceptance criteria into reproducible tests and QA evidence. |
| `cosmosmith-devops-release` | Check build, CI, deployment, monitoring, rollback, and release readiness. |
| `cosmosmith-governance-review` | Find rule drift, missing evidence, weak handoffs, and incomplete tasks. |
| `cosmosmith-project-rules` | Generate or update project instruction files and editor adapters. |

## Typical Workflow

```text
rough idea
  -> product discovery
  -> market research when facts may be current
  -> proposal and design
  -> task.md
  -> frontend/backend slices
  -> QA evidence
  -> release readiness
  -> governance review
```

Example instruction to your agent:

```text
Use Cosmosmith. I want to build a quiet personal CRM for independent consultants.
Start with product discovery, then publish the first task ledger.
```

## Verify Your Install

Create a temporary workspace:

```bash
npx cosmosmith@latest init --all --dir .tmp/cosmosmith-check
```

Check the output:

```bash
ls .tmp/cosmosmith-check
```

You should see `AGENTS.md`, `task.md`, `proposal.md`, `design.md`, `CLAUDE.md`, and `docs/cosmosmith/`.

## Development

```bash
npm run validate
npm run smoke:init
```

Validate the Codex plugin manifest:

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

Preview the npm package:

```bash
npm pack --dry-run
```

## Roadmap

- `cosmosmith init --sample` for a tiny verified demo workflow.
- Task ledger consistency validator.
- Better post-init guidance for CLI vs runtime skills.
- More adapters as agent rule conventions stabilize.

## License

MIT
