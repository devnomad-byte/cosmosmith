# Cosmosmith（造界匠）

**一条命令，给你的 AI 编程 Agent 配上产品团队、架构台、任务板和发布门禁。**

Cosmosmith 帮你把一个粗略产品想法变成可治理的多 Agent 工作流。它会初始化项目规则、规格模板、任务账本、编辑器适配文件和 Codex 角色 skills，让 Agent 从产品发现走到开发验证，而不是在一堆 prompt 里漂移。

[English README](README.md) | [npm](https://www.npmjs.com/package/cosmosmith) | [GitHub](https://github.com/devnomad-byte/cosmosmith)

## 10 秒开始

```bash
npx cosmosmith@latest init --all
```

你会得到一个适合 AI 协作开发的项目工作区：

```text
AGENTS.md                         Agent 项目宪法
task.md                           带证据字段的任务账本
proposal.md                       产品提案模板
design.md                         技术与 UX 设计模板
docs/cosmosmith/idea-brief.md      产品发现记录
docs/cosmosmith/research-brief.md  调研记录
CLAUDE.md                         Claude Code 适配
.cursor/rules/cosmosmith.mdc       Cursor 适配
.github/copilot-instructions.md    GitHub Copilot 适配
.opencode/AGENTS.md                OpenCode 适配
.trae/rules/cosmosmith.md          Trae 适配
```

## 为什么开发者会需要它

AI Agent 写代码很快，但快不等于产品完成。Cosmosmith 给工作流一根主线：

- **先澄清想法**，再开始实现。
- **拆分角色职责**：产品、调研、架构、UX、前端、后端、QA、DevOps、治理。
- **把任务发布到 `task.md`**，让 Agent 领取小切片，而不是到处游走。
- **要求验证证据**，没有证据就不能标记完成。
- **用一个主规则源** 适配 Codex、Claude Code、Cursor、Copilot、OpenCode 和 Trae。

核心模型是：

```text
Prompt -> Context -> Harness -> Loop
```

- Prompt：当前要让 Agent 做什么。
- Context：本次任务真正相关的文件、调研、约束和决策。
- Harness：测试、脚本、检查项和发布门禁。
- Loop：评审、验证、反馈和规则更新。

## CLI 和 Plugin 的区别

Cosmosmith 有两层能力。

| 层 | 作用 | 什么时候用 |
| --- | --- | --- |
| CLI 初始化器 | 生成 `AGENTS.md`、`task.md`、规格模板和编辑器适配。 | 任何项目都可以用。 |
| Codex 插件 | 把 `$cosmosmith-*` 角色 skills 加载进 Codex。 | 当你希望 Codex 直接调用这些角色工作流时使用。 |

CLI 适用于任何仓库：

```bash
npx cosmosmith init
npx cosmosmith@latest init
npx cosmosmith@latest init --all
npx cosmosmith@latest init --dir ./my-project --all
```

常用选项：

```bash
npx cosmosmith@latest init --claude --cursor --copilot
npx cosmosmith@latest init --opencode --trae
npx cosmosmith@latest init --all --dry-run
npx cosmosmith@latest init --all --force
```

默认不会覆盖已有文件。只有你明确想替换生成文件时，才使用 `--force`。

## Codex 插件安装

Codex 用户可以把角色 skills 安装为原生插件：

```bash
codex plugin marketplace add devnomad-byte/cosmosmith
codex plugin add cosmosmith@cosmosmith
```

安装后开启一个新的 Codex 线程，让新 skills 被加载。

## 角色网格

Cosmosmith 不是一个 prompt，而是一组能交接产物的角色工作流。

| Skill | 帮 Agent 做什么 |
| --- | --- |
| `cosmosmith-product-discovery` | 把模糊想法转成用户、任务、第一切片和验收标准。 |
| `cosmosmith-market-research` | 调研竞品、同类产品、标准、风险和当前外部事实。 |
| `cosmosmith-spec-governor` | 把发现结果转成 `proposal.md`、`design.md` 和可领取任务。 |
| `cosmosmith-architect` | 定义边界、数据流、可靠性、安全和集成方式。 |
| `cosmosmith-ui-ux-designer` | 设计流程、页面、交互状态、可访问性和视觉方向。 |
| `cosmosmith-frontend-engineer` | 实现前端任务切片，并记录验证证据。 |
| `cosmosmith-backend-engineer` | 实现 API、领域逻辑、持久化、权限和契约。 |
| `cosmosmith-qa-verifier` | 把验收标准转成可复现测试和 QA 证据。 |
| `cosmosmith-devops-release` | 检查构建、CI、部署、监控、回滚和发布准备。 |
| `cosmosmith-governance-review` | 找出规则漂移、证据缺失、交接薄弱和任务不完整。 |
| `cosmosmith-project-rules` | 生成或更新项目规则文件和编辑器适配。 |

## 典型工作流

```text
粗略想法
  -> 产品发现
  -> 在事实可能变化时进行市场调研
  -> 提案和设计
  -> task.md
  -> 前端/后端实现切片
  -> QA 证据
  -> 发布准备
  -> 治理评审
```

你可以这样告诉 Agent：

```text
使用 Cosmosmith。我想做一个给独立顾问用的安静型个人 CRM。
先做产品发现，然后发布第一版 task.md。
```

## 验证安装

创建一个临时工作区：

```bash
npx cosmosmith@latest init --all --dir .tmp/cosmosmith-check
```

检查输出：

```bash
ls .tmp/cosmosmith-check
```

你应该能看到 `AGENTS.md`、`task.md`、`proposal.md`、`design.md`、`CLAUDE.md` 和 `docs/cosmosmith/`。

## 开发验证

```bash
npm run validate
npm run smoke:init
```

验证 Codex 插件 manifest：

```bash
python path/to/plugin-creator/scripts/validate_plugin.py plugins/cosmosmith
```

预览 npm 包：

```bash
npm pack --dry-run
```

## 路线图

- `cosmosmith init --sample`：生成一个很小但可验证的演示工作流。
- task ledger 一致性校验器。
- 更清楚地区分 CLI 初始化和运行时 skills。
- 随着 Agent 规则约定稳定，增加更多编辑器适配。

## 许可证

MIT
