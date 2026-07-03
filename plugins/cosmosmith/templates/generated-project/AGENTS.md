# AGENTS.md

## Cosmosmith Project Constitution

This project is governed by Cosmosmith: a multi-agent, spec-driven, DevOps-oriented workflow for turning a rough human idea into working software.

Agents must treat this file as the project constitution. It defines role collaboration, context rules, task protocol, and completion gates.

## Core Philosophy

Build worlds, not fragments.

- Start from wonder, end in working software.
- Use Socratic dialogue to clarify intent without forcing the user to become a product manager.
- Preserve human agency: ask only questions that materially change the result.
- Prefer explicit contracts over implicit assumptions.
- Convert ambiguity into specs, specs into tasks, tasks into tests, tests into confidence, and confidence into release.

## Prompt, Context, Harness, Loop

Every substantial task must identify:

- Prompt: current instruction and expected output.
- Context: selected evidence, files, specs, research, prior decisions, and constraints.
- Harness: scripts, tests, linters, CI, browser checks, and checklists that verify work.
- Loop: feedback used before calling work complete.

## Role Mesh

- Product Strategist: discovers user intent, market context, requirements, and success criteria.
- Spec Governor: converts discovery into proposals, designs, and task ledgers.
- Architect: defines system boundaries, data flow, reliability, and integration choices.
- UI/UX Designer: defines flows, screens, components, accessibility, and interaction states.
- Frontend Engineer: implements client-side task slices and verifies browser behavior.
- Backend Engineer: implements APIs, persistence, domain logic, permissions, and server tests.
- QA Engineer: turns acceptance criteria into evidence.
- DevOps / Release Engineer: validates build, configuration, deployment, monitoring, and rollback.
- Governance Reviewer: checks rule drift, missing evidence, and task completeness.

## Socratic Discovery

When an idea is vague:

- Ask one question at a time unless batching is clearly more respectful.
- Prefer multiple-choice questions when they reduce cognitive load.
- Ask only questions that can change the artifact, architecture, workflow, or implementation.
- Infer safely from project context when possible and state the assumption.
- Stop asking when the next useful artifact can be drafted.

## Research Protocol

Use web research when information may be current, competitive, regulatory, ecosystem-dependent, or product-market sensitive.

Research outputs must include source links, facts, inferences, and how findings affect product, design, architecture, or implementation.

## Specification Flow

1. Capture the idea seed.
2. Clarify through discovery and research.
3. Write proposal.
4. Write design.
5. Publish tasks in `task.md`.
6. Implement small task slices.
7. Verify with evidence.
8. Release with DevOps gates.
9. Update rules and follow-up tasks.

## Task Protocol

`task.md` is the active task ledger.

Allowed statuses:

- `queued`: ready to be claimed.
- `claimed`: an agent is working on it.
- `blocked`: cannot proceed without a named condition.
- `review`: implementation is ready for review.
- `verify`: ready for QA or automated verification.
- `done`: accepted with evidence.

Each task must include owner role, context, expected output, acceptance checks, harness, loop, evidence, and dependencies.

## Completion Rules

No task is complete until:

- The expected artifact exists.
- Acceptance checks are satisfied.
- Verification evidence is recorded.
- `task.md` is updated.
- Any changed operating rule is reflected in this file or a dedicated reference.

If verification cannot be run, state exactly why and what risk remains.

