#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __filename = fileURLToPath(import.meta.url);
const ROOT = path.resolve(path.dirname(__filename), "..");
const PLUGIN = path.join(ROOT, "plugins", "cosmosmith");

const args = process.argv.slice(2);
const command = args[0];

function usage() {
  console.log(`Cosmosmith

Usage:
  cosmosmith init [options]

Options:
  --dir <path>       Target project directory (default: current directory)
  --all              Generate all supported adapters
  --claude           Generate CLAUDE.md
  --cursor           Generate .cursor/rules/cosmosmith.mdc
  --copilot          Generate .github/copilot-instructions.md
  --opencode         Generate .opencode/AGENTS.md adapter
  --trae             Generate .trae/rules/cosmosmith.md adapter
  --force            Overwrite existing generated files
  --dry-run          Print planned writes without changing files
  -h, --help         Show help

Examples:
  npx cosmosmith init
  npx cosmosmith init --all
  npx cosmosmith init --claude --cursor
`);
}

function parseOptions(raw) {
  const opts = {
    dir: process.cwd(),
    all: false,
    claude: false,
    cursor: false,
    copilot: false,
    opencode: false,
    trae: false,
    force: false,
    dryRun: false,
  };

  for (let i = 0; i < raw.length; i += 1) {
    const arg = raw[i];
    if (arg === "--dir") {
      const value = raw[i + 1];
      if (!value) throw new Error("--dir requires a path");
      opts.dir = path.resolve(value);
      i += 1;
    } else if (arg === "--all") {
      opts.all = true;
    } else if (arg === "--claude") {
      opts.claude = true;
    } else if (arg === "--cursor") {
      opts.cursor = true;
    } else if (arg === "--copilot") {
      opts.copilot = true;
    } else if (arg === "--opencode") {
      opts.opencode = true;
    } else if (arg === "--trae") {
      opts.trae = true;
    } else if (arg === "--force") {
      opts.force = true;
    } else if (arg === "--dry-run") {
      opts.dryRun = true;
    } else if (arg === "-h" || arg === "--help") {
      opts.help = true;
    } else {
      throw new Error(`Unknown option: ${arg}`);
    }
  }

  if (opts.all) {
    opts.claude = true;
    opts.cursor = true;
    opts.copilot = true;
    opts.opencode = true;
    opts.trae = true;
  }

  return opts;
}

function readTemplate(...segments) {
  return fs.readFileSync(path.join(PLUGIN, ...segments), "utf8");
}

function writeFile(targetRoot, relativePath, content, opts) {
  const destination = path.join(targetRoot, relativePath);
  const exists = fs.existsSync(destination);
  if (exists && !opts.force) {
    console.log(`skip  ${relativePath} (exists; use --force to overwrite)`);
    return;
  }
  if (opts.dryRun) {
    console.log(`${exists ? "would overwrite" : "would create"}  ${relativePath}`);
    return;
  }
  fs.mkdirSync(path.dirname(destination), { recursive: true });
  fs.writeFileSync(destination, content, "utf8");
  console.log(`${exists ? "write" : "create"} ${relativePath}`);
}

function adapter(content) {
  return `${content.trim()}\n`;
}

function init(opts) {
  const targetRoot = opts.dir;
  if (!opts.dryRun) fs.mkdirSync(targetRoot, { recursive: true });

  const generatedAgents = readTemplate("templates", "generated-project", "AGENTS.md");
  const taskLedger = readTemplate("templates", "artifacts", "task-ledger.md");
  const ideaBrief = readTemplate("templates", "artifacts", "idea-brief.md");
  const researchBrief = readTemplate("templates", "artifacts", "research-brief.md");
  const proposal = readTemplate("templates", "artifacts", "proposal.md");
  const design = readTemplate("templates", "artifacts", "design.md");

  const writes = [
    ["AGENTS.md", generatedAgents],
    ["task.md", taskLedger],
    ["docs/cosmosmith/idea-brief.md", ideaBrief],
    ["docs/cosmosmith/research-brief.md", researchBrief],
    ["proposal.md", proposal],
    ["design.md", design],
  ];

  if (opts.claude) {
    writes.push(["CLAUDE.md", readTemplate("templates", "generated-project", "CLAUDE.md")]);
  }
  if (opts.cursor) {
    writes.push([
      ".cursor/rules/cosmosmith.mdc",
      readTemplate("templates", "adapters", "cursor", "cosmosmith.mdc"),
    ]);
  }
  if (opts.copilot) {
    writes.push([
      ".github/copilot-instructions.md",
      readTemplate("templates", "adapters", "copilot", "copilot-instructions.md"),
    ]);
  }
  if (opts.opencode) {
    writes.push([
      ".opencode/AGENTS.md",
      adapter(`# OpenCode Cosmosmith Adapter

Follow ../AGENTS.md as the canonical Cosmosmith project constitution.

Use task.md for claimable work and verification evidence.`),
    ]);
  }
  if (opts.trae) {
    writes.push([
      ".trae/rules/cosmosmith.md",
      adapter(`# Trae Cosmosmith Rules

Follow AGENTS.md as the canonical Cosmosmith project constitution.

Use task.md for claimable work, role handoffs, and verification evidence.`),
    ]);
  }

  for (const [relativePath, content] of writes) {
    writeFile(targetRoot, relativePath, content, opts);
  }

  console.log("\nCosmosmith init complete.");
  console.log("Next: start with `cosmosmith-product-discovery`, then run `cosmosmith-spec-governor`.");
}

try {
  if (!command || command === "-h" || command === "--help") {
    usage();
  } else if (command === "init") {
    const opts = parseOptions(args.slice(1));
    if (opts.help) usage();
    else init(opts);
  } else {
    throw new Error(`Unknown command: ${command}`);
  }
} catch (error) {
  console.error(`cosmosmith: ${error.message}`);
  process.exit(1);
}

