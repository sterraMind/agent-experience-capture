[![skills.sh](https://skills.sh/b/sterraMind/agent-experience-capture)](https://skills.sh/sterraMind/agent-experience-capture)

# Agent Experience Capture

**Your agent's memory, codified.** Every session produces hard-won knowledge — API quirks, non-obvious bugs, design decisions, patterns that emerged. This skill ensures that knowledge outlives the session: captured, structured, and reusable.

```
One-shot session insight → codemem entries → SOP updates → (optionally) a brand new agent skill
```

## The Problem

Coding agents are **stateless by default**. Every session starts fresh. The bugs you fixed last week, the tool behavior you discovered yesterday, the architectural decision you debated — all gone when the conversation ends.

Without structured capture:

- **The same bug gets fixed twice** — root cause wasn't recorded
- **Onboarding new agents means repeating discoveries** — no institutional memory
- **Wins are fragile** — a clever workaround disappears when the session closes

## What This Skill Does

This skill activates **automatically** at session end when there's knowledge worth preserving. It guides the agent through a 7-step process:

| Step | What Happens | Output |
|------|-------------|--------|
| **1. Evaluate** | Is this worth keeping? (cross-session relevance, non-obvious, actionable, durable) | Pass/fail gate |
| **2. Categorize** | Rule? Decision? Discovery? Pattern? Pitfall? | One label |
| **3. Codemem** | Write to durable memory with TRIGGER + RULE + WHY + VIOLATION | `codemem_memory_remember()` |
| **4. SOP update** | Update QUICK-START / FULL-SOP / PITFALLS docs | File changes |
| **5. AGENTS.md** | Register new trigger categories | Updated triggers |
| **6. Handoff** | Log to handoff record | `.agents/handoff.md` |
| **7. Create Skill** | (Conditional) Package repeatable processes as new skills | `scripts/scaffold-skill.py` |

## Quickstart

```bash
# Install the skill
npx skills@latest add sterraMind/agent-experience-capture

# The skill activates automatically at session end.
# No manual invocation needed.
```

## How It Works

### Automatic Triggering

The skill fires when a session completes with any of:

- A bug was found and fixed (especially non-obvious root cause)
- An API/tool behavior differs from documentation
- A design decision that affects future work
- A pattern worth codifying
- A "by design" assumption was proven wrong

It **does not** fire for trivial one-offs, routine operations, or temporary context.

### Structured Output

Every captured lesson follows a strict format — no prose, no ambiguity:

```yaml
TRIGGER:  "When an API returns 202 but the resource isn't ready yet"
RULE:     "Always poll GET /resources/{id}/status after POST, don't assume 202 = done"
WHY:      "The API is eventually-consistent; 202 only means 'accepted'"
VIOLATION: "We called GET /resources/{id} immediately and got 404"
TAGS:     "api, polling, eventual-consistency"
```

### Skill Creation (Step 7)

When a captured experience represents a **repeatable, cross-session process**, the skill can scaffold and validate a new agent skill from it:

```bash
uv run python scripts/scaffold-skill.py \
  --name "my-process" \
  --description "Runs [task] using [tools]. Use when [trigger]. Don't use for [boundary]." \
  --category "technical" \
  --output "../skills/"
```

The scaffold script enforces name and description format constraints from the [agentskills.io](https://agentskills.io) spec. For full spec compliance, run the checklist in `references/validation-checklist.md`.

## Who This Is For

- **Teams using coding agents** — preserve institutional knowledge across sessions
- **Platform operators** — capture deployment quirks and environment-specific behaviors
- **Solo developers** — never re-discover the same fix twice
- **Skill authors** — use the conditional Step 7 to bootstrap new skills from real experience

## Project Structure

```
experience-capture/
├── SKILL.md                    # Core instructions: 7-step capture + creation flow
├── TEMPLATE.md                 # Quick-reference output templates
├── README.md                   # This file
├── LICENSE                     # Apache 2.0
├── scripts/
│   └── scaffold-skill.py       # Scaffold new skills from captured experiences
└── references/
    ├── skill-templates.md      # Templates for technical, design, and workflow skills
    └── validation-checklist.md # agentskills.io spec compliance checklist
```

## Prerequisites

| Tool | Required? | Notes |
|------|-----------|-------|
| `npx skills` | Yes | For SkillsMP installation |
| `uv` | For Step 7 | Python project manager for `scaffold-skill.py` |
| `codemem` | For Steps 3-4 | Built into OpenCode/Claude Code |
| SOP files | For Step 4 | QUICK-START.md, FULL-SOP.md, PITFALLS.md per service under `.agents/[service]/` |

> **Note:** Step 4 (SOP update) requires that your project already maintains SOP document structure under `.agents/[service]/`. If you don't have this structure, Steps 1-3, 5-7 still work independently.

## Validating the Skill

Each capture goes through a quality gate before completion:

- [x] TRIGGER, RULE, WHY, VIOLATION, TAGS — 5 fields, none missing
- [x] No duplicate entries (checked against existing codemem)
- [x] Tags consistent with existing entries
- [x] SOP versions updated
- [x] No sensitive data in output
- [x] Each entry ≤ 100 words, one concept per entry

## License

Apache 2.0 — see [LICENSE](./LICENSE).
