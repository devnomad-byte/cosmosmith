# Cosmosmith

Cosmosmith（造界匠）是一套多 Agent 技能系统，用来把一个粗略想法变成经过调研的规格、任务板、实现切片、验证证据和发布检查。

它既可以作为 Codex 原生插件安装，也可以作为其他 AI 编程工具的规则/模板兼容包使用。

English documentation: [README.md](README.md)

## 提供什么

- `cosmosmith-product-discovery`：把粗略想法澄清成 idea brief。
- `cosmosmith-market-research`：调研竞品、同类产品、标准和外部证据。
- `cosmosmith-spec-governor`：把 brief 转成 `proposal.md`、`design.md` 和 `task.md`。
- `cosmosmith-architect`：设计系统边界、数据流、可靠性和集成方案。
- `cosmosmith-ui-ux-designer`：设计流程、页面、状态、可访问性和视觉方向。
- `cosmosmith-frontend-engineer`：实现前端任务切片并记录验证证据。
- `cosmosmith-backend-engineer`：实现后端任务切片、接口契约和测试。
- `cosmosmith-qa-verifier`：按验收标准验证任务并记录证据。
- `cosmosmith-devops-release`：准备构建、CI、部署、监控和回滚。
- `cosmosmith-governance-review`：检查规则漂移、缺失证据和任务完整性。
- `cosmosmith-project-rules`：生成 `AGENTS.md`，以及可选的 `CLAUDE.md`、Cursor rules、Copilot instructions。

## 安装/使用矩阵

| 工具 | 支持方式 | 如何使用 Cosmosmith |
| --- | --- | --- |
| Codex | 原生插件 | 安装 marketplace 和 plugin。 |
| Claude Code | 规则适配 | 复制或生成 `AGENTS.md` 与 `CLAUDE.md`；skills 作为工作流参考。 |
| Cursor | 规则适配 | 复制或生成 `AGENTS.md` 与 `.cursor/rules/cosmosmith.mdc`。 |
| GitHub Copilot | instructions 适配 | 复制或生成 `AGENTS.md` 与 `.github/copilot-instructions.md`。 |
| OpenCode | 可移植 skills/rules | 复制 `AGENTS.md`，并按你的环境使用 `plugins/cosmosmith/skills/*`。 |
| Trae | 项目规则适配 | 复制或生成 `AGENTS.md`，再按 Trae 项目规则格式适配。 |

Codex 是原生插件目标。其他工具通过项目规则文件、模板和可移植 `SKILL.md` 工作流使用 Cosmosmith。

## Codex 安装

添加这个仓库作为 Codex plugin marketplace：

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
```

安装插件：

```bash
codex plugin add cosmosmith@cosmosmith
```

安装后开启一个新的 Codex 线程，让新 skills 被加载。

## Claude Code 使用

Cosmosmith 把 `AGENTS.md` 作为跨 Agent 的项目宪法，把 `CLAUDE.md` 作为 Claude Code 的适配文件。

如果已经在 Codex 中安装 Cosmosmith，可以在目标项目里说：

```text
Use $cosmosmith-project-rules to create AGENTS.md and CLAUDE.md for this repo.
```

手动方式：

1. 复制 `plugins/cosmosmith/templates/generated-project/AGENTS.md` 到项目根目录。
2. 复制 `plugins/cosmosmith/templates/generated-project/CLAUDE.md` 到项目根目录。
3. 让 Claude Code 遵守 `CLAUDE.md`；它会指向 canonical 的 `AGENTS.md`。

## Cursor 使用

如果已经安装 Cosmosmith，可以在目标项目里说：

```text
Use $cosmosmith-project-rules to create AGENTS.md and Cursor rules for this repo.
```

手动方式：

1. 复制 `plugins/cosmosmith/templates/generated-project/AGENTS.md` 为 `AGENTS.md`。
2. 复制 `plugins/cosmosmith/templates/adapters/cursor/cosmosmith.mdc` 为 `.cursor/rules/cosmosmith.mdc`。

Cursor rule 会保持很短，`AGENTS.md` 仍然是主规则。

## GitHub Copilot 使用

手动方式：

1. 复制 `plugins/cosmosmith/templates/generated-project/AGENTS.md` 为 `AGENTS.md`。
2. 复制 `plugins/cosmosmith/templates/adapters/copilot/copilot-instructions.md` 为 `.github/copilot-instructions.md`。

Copilot instructions 应保持简短，并指向 `AGENTS.md`。

## OpenCode 使用

兼容 OpenCode 的环境可以使用项目规则和可移植 skill 文件夹：

1. 复制 `plugins/cosmosmith/templates/generated-project/AGENTS.md` 到项目根目录。
2. 如果你的 OpenCode 环境支持 skill folders，把 `plugins/cosmosmith/skills/` 复制到对应位置。
3. 在提示词中使用 skill 名，例如 `cosmosmith-spec-governor`。

如果你的环境不直接支持 portable skills，可以把 `SKILL.md` 当作工作流参考。

## Trae 使用

Trae 用户可以通过项目规则使用 Cosmosmith：

1. 复制 `plugins/cosmosmith/templates/generated-project/AGENTS.md` 到项目。
2. 如果 Trae 工作区使用不同的规则文件格式，把相关章节转换为 Trae 项目规则。
3. 尽量保持 `AGENTS.md` 为 canonical source。

## 典型流程

1. 用 `cosmosmith-product-discovery` 澄清粗略想法。
2. 用 `cosmosmith-market-research` 调研竞品和当前约束。
3. 用 `cosmosmith-spec-governor` 创建 `proposal.md`、`design.md` 和 `task.md`。
4. 用 `cosmosmith-architect` 和 `cosmosmith-ui-ux-designer` 审查架构和体验。
5. 前端/后端按小任务切片实现。
6. 用 `cosmosmith-qa-verifier` 做验收验证。
7. 用 `cosmosmith-devops-release` 做发布准备。
8. 完成前用 `cosmosmith-governance-review` 做治理审查。

示例：

```text
Use $cosmosmith-product-discovery to turn this idea into a brief: ...
```

```text
Use $cosmosmith-spec-governor to create proposal.md, design.md, and task.md.
```

```text
Use $cosmosmith-project-rules to create AGENTS.md and CLAUDE.md for this repo.
```

## 仓库结构

```text
.agents/plugins/marketplace.json
plugins/cosmosmith/
  .codex-plugin/plugin.json
  skills/
  templates/
scripts/validate_release.py
```

插件位于 `plugins/cosmosmith/`，所以这个仓库可以作为 Codex marketplace。

## 开发验证

验证发布包：

```bash
python scripts/validate_release.py
```

验证 Codex plugin：

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

## 许可证

MIT
