# Cosmosmith

Cosmosmith（造界匠）是一套通用初始化器和 Codex 插件，用来把粗略想法变成经过调研的规格、任务板、实现切片、验证证据和发布准备。

它面向 Codex、Claude Code、Cursor、GitHub Copilot、OpenCode、Trae 以及类似的 AI 编程工具。

English documentation: [README.md](README.md)

## 快速开始

在任意项目里运行：

```bash
npx cosmosmith init
```

它会生成：

- `AGENTS.md`
- `task.md`
- `proposal.md`
- `design.md`
- `docs/cosmosmith/idea-brief.md`
- `docs/cosmosmith/research-brief.md`

一次生成所有工具适配文件：

```bash
npx cosmosmith init --all
```

或者只选择部分适配：

```bash
npx cosmosmith init --claude --cursor --copilot
```

常用选项：

```bash
npx cosmosmith init --dir ./my-project
npx cosmosmith init --all --force
npx cosmosmith init --all --dry-run
```

## 编辑器 / Agent 支持

| 工具 | 命令 |
| --- | --- |
| 通用 Agent | `npx cosmosmith init` |
| Claude Code | `npx cosmosmith init --claude` |
| Cursor | `npx cosmosmith init --cursor` |
| GitHub Copilot | `npx cosmosmith init --copilot` |
| OpenCode | `npx cosmosmith init --opencode` |
| Trae | `npx cosmosmith init --trae` |
| 全部适配 | `npx cosmosmith init --all` |

Cosmosmith 把 `AGENTS.md` 作为项目的主规则文件。其他工具文件只是适配层。

## Codex 插件安装

Codex 用户也可以安装原生插件：

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
codex plugin add cosmosmith@cosmosmith
```

安装后开启一个新的 Codex 线程，让新 skills 被加载。

## Skills

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
- `cosmosmith-project-rules`：生成项目规则适配文件。

## 典型流程

1. 用 `cosmosmith-product-discovery` 澄清粗略想法。
2. 用 `cosmosmith-market-research` 调研竞品和当前约束。
3. 用 `cosmosmith-spec-governor` 创建 `proposal.md`、`design.md` 和 `task.md`。
4. 用 `cosmosmith-architect` 和 `cosmosmith-ui-ux-designer` 审查架构和体验。
5. 前端/后端按小任务切片实现。
6. 用 `cosmosmith-qa-verifier` 做验收验证。
7. 用 `cosmosmith-devops-release` 做发布准备。
8. 完成前用 `cosmosmith-governance-review` 做治理审查。

## `init` 会写入什么

默认：

```text
AGENTS.md
task.md
proposal.md
design.md
docs/cosmosmith/idea-brief.md
docs/cosmosmith/research-brief.md
```

使用 `--all`：

```text
CLAUDE.md
.cursor/rules/cosmosmith.mdc
.github/copilot-instructions.md
.opencode/AGENTS.md
.trae/rules/cosmosmith.md
```

默认不会覆盖已有文件。需要覆盖时使用 `--force`。

## 仓库结构

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

## 开发验证

验证发布包：

```bash
npm run validate
```

冒烟测试初始化器：

```bash
npm run smoke:init
```

验证 Codex plugin：

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

## 许可证

MIT

