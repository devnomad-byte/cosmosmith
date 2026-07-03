# Cosmosmith

Cosmosmith is a Codex plugin for turning rough ideas into researched specs, task ledgers, implementation slices, verification evidence, and release readiness.

It is designed as a short, connected skill chain rather than one giant prompt.

## What It Adds

- `cosmosmith-product-discovery`: clarify a rough idea into an idea brief.
- `cosmosmith-spec-governor`: convert briefs into `proposal.md`, `design.md`, and `task.md`.
- `cosmosmith-governance-review`: review artifacts for rule drift, missing evidence, and task completeness.
- `cosmosmith-project-rules`: generate `AGENTS.md` and optional editor adapters such as `CLAUDE.md`.

## Install

Add this repository as a Codex plugin marketplace:

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
```

Then install the plugin:

```bash
codex plugin add cosmosmith@cosmosmith
```

Start a new Codex thread after installation so the new skills are loaded.

## Typical Flow

1. Ask Cosmosmith to clarify a rough idea.
2. Use the generated idea brief to create a proposal, design, and task ledger.
3. Generate project rules with `cosmosmith-project-rules`.
4. Implement tasks in small slices.
5. Run governance review before marking tasks done.

Example prompts:

```text
Use cosmosmith-product-discovery to turn this idea into a brief: ...
```

```text
Use cosmosmith-spec-governor to create proposal.md, design.md, and task.md.
```

```text
Use cosmosmith-project-rules to create AGENTS.md and CLAUDE.md for this repo.
```

## Project Rule Files

Cosmosmith treats `AGENTS.md` as the canonical cross-agent project constitution.

Optional adapters can be generated when the user asks:

- `CLAUDE.md`
- `.cursor/rules/cosmosmith.mdc`
- `.github/copilot-instructions.md`

Adapters should stay short and point back to `AGENTS.md` whenever possible.

## Repository Layout

```text
.agents/plugins/marketplace.json
plugins/cosmosmith/
  .codex-plugin/plugin.json
  skills/
  templates/
```

The plugin lives under `plugins/cosmosmith/` so this repository can act as a Codex marketplace.

## Development

Validate the plugin:

```bash
python scripts/validate_release.py
```

The validator checks plugin manifest shape, skill frontmatter, required templates, and placeholder leakage.

## License

MIT

