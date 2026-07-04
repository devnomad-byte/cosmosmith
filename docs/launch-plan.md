# Cosmosmith Exposure Plan

This document is the launch playbook for exposing Cosmosmith to developer communities. It is written as an execution checklist: what to prepare, where to post, what URL to use, what to say, and what outcome to look for.

## Positioning

One-line positioning:

> Cosmosmith is a universal initializer and Codex plugin that turns rough ideas into multi-agent product, spec, implementation, QA, and release workflows.

Short Chinese positioning:

> Cosmosmith（造界匠）是一条命令初始化多 Agent 工程工作流的开源工具：从粗略想法到产品、架构、设计、开发、测试、发布和治理。

Core demo command:

```bash
npx cosmosmith@latest init --all
```

Primary links:

- GitHub: https://github.com/devnomad-byte/cosmosmith
- npm: https://www.npmjs.com/package/cosmosmith

## Launch Goals

- Get the first real users to run `npx cosmosmith@latest init --all`.
- Collect feedback from developers who use Codex, Claude Code, Cursor, OpenCode, Trae, or Copilot.
- Validate the message: "agents need product, spec, task, test, and release discipline, not just prompts."
- Convert feedback into issues, examples, and a `0.2.0` roadmap.

## Phase 0 - Prepare Before Posting

Do these before any public launch.

### Product Readiness

- [ ] Publish `0.1.1` so npm displays the polished README.
- [ ] Add GitHub topics:
  - `ai-agents`
  - `agent-skills`
  - `codex`
  - `claude-code`
  - `cursor`
  - `devtools`
  - `devops`
  - `spec-driven-development`
- [ ] Add GitHub repository description:
  - `Universal initializer and Codex plugin for multi-agent product, spec, implementation, QA, and release workflows.`
- [ ] Add one example directory:
  - `examples/world-seed-compass`
- [ ] Record a short terminal GIF or video:
  - run `npx cosmosmith@latest init --all`
  - show generated `AGENTS.md`, `task.md`, `proposal.md`, and editor adapters
- [ ] Create 3 GitHub issues for visible roadmap:
  - `Add --sample verified example workflow`
  - `Improve post-init guidance for CLI vs plugin`
  - `Add task ledger consistency validator`

### Message To Repeat Everywhere

Use this as the spine of every post:

> AI agents can write code, but projects still fail when roles, context, tasks, tests, and release gates are implicit. Cosmosmith adds a project constitution, task ledger, spec templates, editor adapters, and Codex role skills so an idea can become verified work.

## Phase 1 - Soft Launch

Goal: get feedback without creating a big traffic spike.

### GitHub

URL:

- Repository: https://github.com/devnomad-byte/cosmosmith
- Topics docs: https://docs.github.com/articles/classifying-your-repository-with-topics

Actions:

- Add topics and description.
- Pin the repo on the GitHub profile.
- Add a release `v0.1.1` after publishing npm.
- Open the roadmap issues listed above.

Success signal:

- Repo page explains the project within 10 seconds.
- A new visitor can copy one command and run it.

### npm

URL:

- Package page: https://www.npmjs.com/package/cosmosmith

Actions:

- Publish `0.1.1` after README polish.
- Verify:

```bash
npm view cosmosmith version
npx cosmosmith@latest init --all --dir .tmp/cosmosmith-check
```

Success signal:

- npm page shows the polished README.
- `npx cosmosmith@latest init --all` works from a clean folder.

### V2EX

URL:

- 分享创造: https://www.v2ex.com/go/create
- 程序员: https://www.v2ex.com/go/programmer

Recommended first post:

- Use `分享创造`, not `程序员`, for the first post.

Title:

```text
[开源] 我做了一个把粗略想法变成多 Agent 工程流的工具：Cosmosmith
```

Post shape:

```markdown
大家好，我做了一个小工具 Cosmosmith（造界匠）。

它解决的问题是：现在 Agent 很会写代码，但很多项目缺少产品、架构、任务、测试、发布这些工程纪律。

一条命令：

```bash
npx cosmosmith@latest init --all
```

会生成：
- AGENTS.md：项目规则
- task.md：任务账本
- proposal.md / design.md：规格模板
- Claude / Cursor / Copilot / OpenCode / Trae 适配文件

GitHub: https://github.com/devnomad-byte/cosmosmith
npm: https://www.npmjs.com/package/cosmosmith

我想听听大家两个反馈：
1. 这种多 Agent 工作流有没有真实使用场景？
2. 默认生成的 AGENTS.md / task.md 还缺什么？
```

Tone:

- Be direct and humble.
- Ask for feedback, not stars.
- Reply to every serious comment with specifics.

Success signal:

- 5+ useful comments.
- At least one user runs the command and reports friction.

## Phase 2 - Public Developer Launch

Do this after Phase 1 feedback has been handled.

### Hacker News

URLs:

- Submit: https://news.ycombinator.com/submit
- Show HN guidelines: https://news.ycombinator.com/showhn.html
- Show page: https://news.ycombinator.com/show

Recommended title:

```text
Show HN: Cosmosmith - Turn rough ideas into multi-agent software workflows
```

URL to submit:

```text
https://github.com/devnomad-byte/cosmosmith
```

First comment:

```text
Hi HN, I built Cosmosmith because most AI coding workflows I tried were missing the boring but important parts: product discovery, specs, task ledgers, verification evidence, and release gates.

It is a zero-dependency npm initializer:

  npx cosmosmith@latest init --all

It creates AGENTS.md, task.md, proposal/design templates, and adapters for Claude Code, Cursor, Copilot, OpenCode, and Trae. For Codex, it also includes role skills for product, market research, architecture, UI/UX, frontend, backend, QA, DevOps, and governance.

I would love feedback on whether the generated project rules are useful, too heavy, or missing something important.
```

Rules to respect:

- Do not ask friends to upvote.
- Stay in the comments and answer technical questions.
- Be transparent that this is your own work.

Success signal:

- Technical comments about workflow design, not just traffic.
- Issues opened from HN feedback.

### Product Hunt

URLs:

- Launch guide: https://www.producthunt.com/launch
- Prepare for launch: https://www.producthunt.com/launch/preparing-for-launch

Use Product Hunt after Hacker News or V2EX feedback, not as the first launch.

Product name:

```text
Cosmosmith
```

Tagline:

```text
Turn rough ideas into multi-agent software workflows
```

Short description:

```text
Cosmosmith initializes AGENTS.md, task.md, spec templates, editor adapters, and Codex role skills so AI agents can move from product discovery to implementation, QA, DevOps, and governance with evidence.
```

Assets needed:

- Logo or simple wordmark.
- 3 screenshots:
  - terminal running `npx cosmosmith@latest init --all`
  - generated `AGENTS.md`
  - generated `task.md`
- 1 GIF or short video.

Success signal:

- Developer comments asking about supported editors, Codex plugin installation, or examples.

## Phase 3 - Content Marketing

Goal: make the idea understandable beyond launch-day traffic.

### Juejin

URLs:

- Homepage: https://juejin.cn/
- New draft, login required: https://juejin.cn/editor/drafts/new

Article title:

```text
我做了一个把想法变成多 Agent 工程流的开源工具：Cosmosmith
```

Article outline:

1. 为什么现在 Agent 工作流容易失控。
2. Prompt / Context / Harness / Loop 是什么。
3. 一条命令初始化项目。
4. 支持哪些编辑器和 Agent。
5. 真实 e2e 验证：从任务发布到 `npm test` 通过。
6. 下一步路线图。

Success signal:

- Saves and comments from developers using AI coding tools.

### Zhihu

URLs:

- Zhihu: https://www.zhihu.com/
- Write article: https://zhuanlan.zhihu.com/write

Article title:

```text
AI Agent 会写代码之后，为什么还需要 AGENTS.md、task.md 和工程治理？
```

Angle:

- Do not write it like a product ad.
- Write it like an explanation of the problem.
- Mention Cosmosmith as the implementation at the end.

Success signal:

- Comments debating workflow design.
- People asking for examples.

### DEV Community

URLs:

- DEV: https://dev.to/
- New post: https://dev.to/new
- Writing help: https://dev.to/help/writing-editing-scheduling

Post title:

```text
I built a universal initializer for multi-agent software workflows
```

Post structure:

1. The problem with prompt-only coding agents.
2. What Cosmosmith generates.
3. How to try it.
4. What role skills exist.
5. What feedback is needed.

Success signal:

- International feedback from developers using Cursor, Claude Code, Copilot, or Codex.

### X

URLs:

- X: https://x.com/
- Compose: https://x.com/compose/post

Thread outline:

```text
1/ I built Cosmosmith: a tiny open-source initializer for multi-agent software workflows.

2/ The problem: AI agents can write code, but projects still need product discovery, specs, task ledgers, tests, release gates, and governance.

3/ Try it:
npx cosmosmith@latest init --all

4/ It generates AGENTS.md, task.md, proposal.md, design.md, and adapters for Claude Code, Cursor, Copilot, OpenCode, and Trae.

5/ Codex plugin skills include product, market research, architect, UI/UX, frontend, backend, QA, DevOps, and governance.

6/ Repo:
https://github.com/devnomad-byte/cosmosmith
```

Success signal:

- Reposts by developers using AI coding tools.
- People asking for a demo GIF.

### Reddit

URLs:

- Self-promotion guide: https://www.reddit.com/r/reddit.com/wiki/selfpromotion/
- r/opensource: https://www.reddit.com/r/opensource/
- r/SideProject: https://www.reddit.com/r/SideProject/
- r/programming: https://www.reddit.com/r/programming/

Use Reddit carefully. Read each subreddit rule before posting. Do not post the same text everywhere.

Recommended first subreddit:

- `r/SideProject` if you want maker feedback.
- `r/opensource` if you want open-source feedback.

Post angle:

```text
I built an open-source npm initializer for multi-agent coding workflows. Looking for feedback on the generated AGENTS.md/task.md structure.
```

Success signal:

- Feedback about install friction or generated rule quality.

## Recommended Posting Order

Use this order to reduce risk and improve the message.

1. GitHub cleanup and `0.1.1` npm publish.
2. V2EX `分享创造`.
3. Juejin article.
4. X thread with demo GIF.
5. Hacker News `Show HN`.
6. DEV Community article.
7. Product Hunt launch.
8. Reddit, only after reading each subreddit rule.

## Day-By-Day Plan

### Day 0

- Publish `0.1.1`.
- Add GitHub topics.
- Add example project.
- Record terminal demo.

### Day 1

- Post on V2EX.
- Collect feedback.
- Open GitHub issues for repeated comments.

### Day 2

- Publish Juejin article.
- Share short X thread.

### Day 3

- Fix the top 1-3 issues found from Chinese developer feedback.

### Day 4

- Submit Show HN.
- Stay available for comments for at least 6 hours.

### Day 5-6

- Write DEV article.
- Prepare Product Hunt assets.

### Day 7

- Product Hunt launch if the repo, demo, and examples look polished.

## Copy Blocks

### Short Description

```text
Cosmosmith is a universal initializer and Codex plugin that turns rough ideas into multi-agent product, spec, implementation, QA, and release workflows.
```

### Chinese Short Description

```text
Cosmosmith（造界匠）是一套开源多 Agent 工程工作流：一条命令生成 AGENTS.md、task.md、规格模板和多编辑器适配，让粗略想法进入产品、架构、开发、测试和发布闭环。
```

### Demo Command

```bash
npx cosmosmith@latest init --all
```

### Feedback Questions

- Does the generated `AGENTS.md` feel useful or too heavy?
- Is `task.md` enough for task claiming and evidence tracking?
- Which editor or agent adapter should be improved first?
- Should `cosmosmith init --sample` generate a verified demo task?

## Metrics To Track

Track these manually in the first week:

| Metric | Source | Target |
| --- | --- | --- |
| GitHub stars | GitHub | 50+ after launch week |
| npm weekly downloads | npm | 100+ after launch week |
| Useful comments | V2EX / HN / DEV | 20+ |
| GitHub issues from feedback | GitHub | 5+ |
| Confirmed successful installs | replies / issues | 5+ |

## Follow-Up After Launch

Turn feedback into visible progress:

- Publish `0.2.0` with the top requested feature.
- Add `examples/world-seed-compass`.
- Add `cosmosmith init --sample`.
- Add a task ledger validator.
- Add a short demo video to README.

## Sources Checked

- Hacker News Show HN guidelines: https://news.ycombinator.com/showhn.html
- Product Hunt launch guide: https://www.producthunt.com/launch
- Product Hunt launch preparation: https://www.producthunt.com/launch/preparing-for-launch
- GitHub repository topics docs: https://docs.github.com/articles/classifying-your-repository-with-topics
- V2EX 分享创造: https://www.v2ex.com/go/create
- DEV writing help: https://dev.to/help/writing-editing-scheduling
- Reddit self-promotion guide: https://www.reddit.com/r/reddit.com/wiki/selfpromotion/
