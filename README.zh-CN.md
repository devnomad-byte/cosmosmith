# Cosmosmith（造界匠）

**把一个粗略想法，变成一套可协作、可验证、可发布的多 Agent 软件工作流。**

Cosmosmith 是一个通用项目初始化器，同时也是 Codex 插件。它面向希望用 AI Agent 做产品、架构、设计、开发、测试和发布的人：你给出一个还不完整的想法，Cosmosmith 帮项目生成规则、任务账本、规格模板、编辑器适配文件，并提供一组角色 skills，让 Agent 按工程化流程协作。

[English README](README.md) | [npm 包](https://www.npmjs.com/package/cosmosmith) | [GitHub](https://github.com/devnomad-byte/cosmosmith)

## 为什么需要 Cosmosmith

很多 Agent 工作流失败在同一个地方：用户的想法一开始很模糊，角色职责没有写清，上下文会漂移，最后又容易在没有证据的情况下说“完成了”。

Cosmosmith 把这个过程变成一个可执行的循环：

- **Prompt**：当前要解决什么问题，哪个角色在行动，预期输出是什么。
- **Context**：本次行动真正需要的文件、调研、约束、决策和任务状态。
- **Harness**：测试、脚本、检查项、评审门禁和发布标准。
- **Loop**：从发现、提案、设计、实现、验证、发布到复盘的反馈循环。

它的核心哲学是：**创造世界，而不是堆碎片**。允许用户从一个不完整的念头开始，然后让 Agent 把它转成文档、任务、实现切片和验证证据。

## 在任意项目里安装

通过 npm 直接初始化：

```bash
npx cosmosmith@latest init
```

默认会生成这些项目治理文件：

```text
AGENTS.md
task.md
proposal.md
design.md
docs/cosmosmith/idea-brief.md
docs/cosmosmith/research-brief.md
```

一次生成所有支持的编辑器 / Agent 适配文件：

```bash
npx cosmosmith@latest init --all
```

只生成你需要的适配：

```bash
npx cosmosmith@latest init --claude --cursor --copilot
npx cosmosmith@latest init --opencode --trae
```

指定目标目录：

```bash
npx cosmosmith@latest init --dir ./my-project --all
```

预览或覆盖：

```bash
npx cosmosmith@latest init --all --dry-run
npx cosmosmith@latest init --all --force
```

默认不会覆盖已有文件。只有在你明确想替换生成文件时，才使用 `--force`。

## 它会生成什么

Cosmosmith 把 `AGENTS.md` 作为项目的主宪法。其他工具文件只是适配层，负责告诉不同编辑器或 Agent 回到同一个主规则。

| 使用场景 | 生成文件 | 命令 |
| --- | --- | --- |
| 通用 Agent / Codex 项目规则 | `AGENTS.md` | `npx cosmosmith init` |
| 任务账本 | `task.md` | `npx cosmosmith init` |
| 提案模板 | `proposal.md` | `npx cosmosmith init` |
| 设计模板 | `design.md` | `npx cosmosmith init` |
| 想法澄清记录 | `docs/cosmosmith/idea-brief.md` | `npx cosmosmith init` |
| 调研记录 | `docs/cosmosmith/research-brief.md` | `npx cosmosmith init` |
| Claude Code | `CLAUDE.md` | `npx cosmosmith init --claude` |
| Cursor | `.cursor/rules/cosmosmith.mdc` | `npx cosmosmith init --cursor` |
| GitHub Copilot | `.github/copilot-instructions.md` | `npx cosmosmith init --copilot` |
| OpenCode | `.opencode/AGENTS.md` | `npx cosmosmith init --opencode` |
| Trae | `.trae/rules/cosmosmith.md` | `npx cosmosmith init --trae` |

## CLI 和 Plugin 的区别

Cosmosmith 有两层：

- **CLI 初始化器**：`npx cosmosmith init` 给项目生成规则、模板和编辑器适配文件。这个能力适用于任何仓库。
- **Codex 插件**：把真正的 `$cosmosmith-*` 角色 skills 安装进 Codex，让 Agent 可以把它们作为可复用工作流加载。

如果你只想给项目加规则和模板，用 CLI 就够了。  
如果你希望 Codex 里能直接调用 Cosmosmith 的角色 skills，就再安装 Codex 插件。

## Codex 插件安装

Codex 用户可以把 Cosmosmith 作为原生插件安装：

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
codex plugin add cosmosmith@cosmosmith
```

安装后开启一个新的 Codex 线程，让新 skills 被加载。

## 角色 Skills

Codex 插件提供一组角色网格。每个 skill 都有自己的职责、交接产物、网络调研触发条件和验证要求。

| Skill | 角色职责 |
| --- | --- |
| `cosmosmith-product-discovery` | 通过苏格拉底式对话澄清粗略想法，并写出 idea brief。 |
| `cosmosmith-market-research` | 检索当前竞品、同类产品、价格、标准、风险和外部证据。 |
| `cosmosmith-spec-governor` | 把 brief 转成 `proposal.md`、`design.md` 和可领取的 `task.md`。 |
| `cosmosmith-architect` | 定义系统边界、数据流、可靠性、安全、集成方式和取舍。 |
| `cosmosmith-ui-ux-designer` | 设计流程、页面、状态、可访问性和符合领域的交互模式。 |
| `cosmosmith-frontend-engineer` | 领取前端任务，完成实现切片，验证浏览器行为并记录证据。 |
| `cosmosmith-backend-engineer` | 领取后端任务，实现 API、领域逻辑、持久化和契约验证。 |
| `cosmosmith-qa-verifier` | 把验收标准转成可复现的 QA 证据，失败时重新打开任务。 |
| `cosmosmith-devops-release` | 检查构建、CI、环境、部署、监控、回滚和发布准备。 |
| `cosmosmith-governance-review` | 检查规则漂移、证据缺失、任务完整性和角色交接健康度。 |
| `cosmosmith-project-rules` | 创建或更新 `AGENTS.md` 和各编辑器规则适配文件。 |

## 典型工作流

1. **种子**：用户给出一个粗略想法。
2. **发现**：`cosmosmith-product-discovery` 提出少量关键问题，并写入 `docs/cosmosmith/idea-brief.md`。
3. **调研**：当竞品、标准、法律、库版本或产品预期可能变化时，`cosmosmith-market-research` 进行网络检索。
4. **规格**：`cosmosmith-spec-governor` 写出 `proposal.md`、`design.md`，并把任务发布到 `task.md`。
5. **评审**：架构和 UX 角色在实现变大之前挑战方案。
6. **开发**：前端和后端角色领取小任务，边做边更新状态。
7. **验证**：QA 把验收标准映射到测试、手工检查、截图或 API 证据。
8. **发布**：DevOps 检查构建、配置、部署、监控和回滚。
9. **治理**：Governance Review 检查规则、任务、产物和证据是否仍然一致。

## 示例

```bash
mkdir my-world
cd my-world
npx cosmosmith@latest init --all
```

然后对你的 Agent 说：

```text
使用 Cosmosmith。我想做一个给独立顾问用的安静型个人 CRM。
先做产品发现，然后发布第一版 task.md。
```

期望产物大致是：

```text
docs/cosmosmith/idea-brief.md      -> 澄清后的意图
docs/cosmosmith/research-brief.md  -> 来源、事实、推断
proposal.md                        -> 要创造的世界和第一切片
design.md                          -> 可实现、可测试的方案
task.md                            -> 带 harness 和证据要求的可领取任务
```

## 验证安装

你可以把 Cosmosmith 初始化到一个临时目录：

```bash
npx cosmosmith@latest init --all --dir .tmp/cosmosmith-check
```

检查生成文件：

```bash
ls .tmp/cosmosmith-check
```

你应该能看到 `AGENTS.md`、`task.md`、`proposal.md`、`design.md`、`CLAUDE.md` 和 `docs/cosmosmith/`。

## 开发与发布验证

克隆仓库后运行：

```bash
npm run validate
npm run smoke:init
```

验证 Codex 插件 manifest：

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

预览 npm 包内容：

```bash
npm pack --dry-run
```

## 仓库结构

```text
bin/cosmosmith.mjs                 # 零依赖 CLI
plugins/cosmosmith/.codex-plugin/  # Codex 插件 manifest
plugins/cosmosmith/skills/         # 角色 skills
plugins/cosmosmith/templates/      # 项目模板和编辑器适配
plugins/cosmosmith/references/     # 共享标准
scripts/validate_release.py        # 发布验证 harness
```

## 路线图

- `--sample`：初始化后生成一个很小但可验证的示例任务。
- 更清楚的 post-init 提示，区分“项目规则初始化”和“运行时 plugin skills 安装”。
- 随着各编辑器 Agent 规则约定稳定，增加更多适配。
- 增加可选的 task ledger 一致性校验和文档新鲜度校验。

## 许可证

MIT
