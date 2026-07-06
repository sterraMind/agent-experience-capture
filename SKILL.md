# Experience Capture Skill

## Purpose

When a session produces knowledge worth preserving across future sessions, this skill defines exactly how to capture it.

## Trigger

Activate when a session completes with any of these signals:
- A bug was found and fixed (especially if root cause was non-obvious)
- An API/tool behavior was discovered that differs from docs
- A decision was made that will affect future work
- A pattern emerged that's worth codifying
- A "by design" assumption was proven wrong

**Don't activate for:** trivial one-offs, routine operations following existing SOPs, temporary context expiring with the session.

## Input: Session Data

The AI has access to the full session context (messages, files modified, errors encountered). Extract from it:
- What was attempted
- What succeeded
- What failed (and why)
- What decisions were made
- What was surprising

## Process (Execute in Order)

### Step 1: Evaluate Value (Must Pass)

Check all 4 criteria. If 2+ pass, proceed:

| Criterion | Question | Example Pass |
|-----------|----------|-------------|
| Cross-session relevance | Will a future agent benefit? | "API flow is non-obvious" |
| Non-obvious | Not in official docs? | "Endpoint doesn't auto-queue" |
| Actionable | Changes future behavior? | "Must call start after create" |
| Durable | True for 3+ months? | "Tool design won't change soon" |

If 2+ pass → continue. If <2 → skip, no action needed.

### Step 2: Categorize

Classify each lesson into exactly ONE category:

| Category | When to use |
|----------|------------|
| **Rule** | A behavior to always follow or avoid |
| **Decision** | A choice made with a reason |
| **Discovery** | A fact about the environment/tool |
| **Pattern** | A repeated approach worth noting |
| **Pitfall** | Something that broke or caused wasted time |

### Step 3: Write Codemem Entry (Mandatory)

For each lesson, create ONE codemem entry using this EXACT format:

**Step 2 category → codemem `kind` mapping:**

| Step 2 Category | → codemem kind |
|----------------|----------------|
| Rule | `decision` |
| Decision | `decision` |
| Discovery | `discovery` |
| Pattern | `discovery` |
| Pitfall | `bugfix` |

```
codemem_memory_remember(
  kind="decision" | "discovery" | "feature" | "bugfix" | "refactor" | "exploration",
  title="[Global/Project]: [Category] — [one-line rule]",
  body="TRIGGER: [when to recall this]\nRULE: [what to do]\nWHY: [why it matters]\nVIOLATION: [what went wrong this time]\nTAGS: [comma-separated keywords]",
  confidence=1.0,  # 1.0 for verified, 0.5 for hypothesis
  #  project="project-name"  # set for project-scoped memory
)
```

**Rules for codemem entries:**
- One concept per entry
- Body must be under 100 words
- MUST include a specific VIOLATION example from this session
- MUST include TRIGGER that describes when to recall
- Use tags consistent with existing entries (check codemem_recent first)

**Before writing, check for duplicates:**
```
codemem_memory_search_index(query="[keyword from lesson]", limit=5)
```
If a similar entry exists → update it instead of creating a new one.

### Step 4: Update SOP Documents (Conditional)

Only if the lesson relates to an existing documented process:

**4a. QUICK-START.md** — Add to "关键规则" section if it's a must-follow rule:
```markdown
### [Section Title]
- **Rule:** [one-line rule]
- **Wrong:** [common mistake]
- **Right:** [correct approach]
```

**4b. FULL-SOP.md** — Add to relevant step or create new section:
- Insert after the most relevant existing section
- Use `### [Number]. [Title]` heading format
- Include the API endpoint, file path, or command that demonstrates the rule

**4c. PITFALLS.md** — Add with this EXACT format:
```markdown
### [N]. [Short title]
**症状：** [what you see / error message]
**原因：** [why it happens]
**解决：** [what to do instead]
**验证：** [how to confirm it's fixed]
```
- Increment N to the next available number
- Place in alphabetical order by title

**4d. Update metadata:**
- Update `last_verified` to today's date
- Update `stale_after` to 3 months from today

### Step 5: Update AGENTS.md Trigger (Conditional)

Only if this is a NEW category of experience not yet covered:

Add to root `AGENTS.md` under the relevant project section:
```markdown
## [Service Name] 镜像构建

当任务涉及 **[keywords]** 时：
1. 先读 `.agents/[service]/QUICK-START.md` 了解关键规则
2. 完整步骤读 `.agents/[service]/FULL-SOP.md`
3. 踩坑记录 `.agents/[service]/PITFALLS.md`
4. 关键规则：[3-5 bullet points of must-follow rules]
```

Keep the trigger under 5 lines. If it's longer, move details to QUICK-START.md.

### Step 6: Record to Handoff (Mandatory)

Append to `.agents/handoff.md`:
```markdown
## YYYY-MM-DD
- learned: [one-line summary of what was learned]
- codemem: [IDs of entries created, comma-separated]
- updated: [file paths modified]
```

## Quality Gate (Must Pass All)

Before declaring capture complete, verify ALL:

- [ ] Each codemem entry has TRIGGER, RULE, WHY, VIOLATION, TAGS (5 fields, no missing)
- [ ] No duplicate entries (checked via codemem_memory_search_index)
- [ ] Tags are consistent (checked via codemem_memory_recent)
- [ ] SOP documents updated with correct version numbers
- [ ] Handoff record includes file paths changed
- [ ] No sensitive data (passwords, API keys, personal info) in any output
- [ ] Body of each codemem entry under 100 words
- [ ] One concept per codemem entry

If ANY check fails → fix it before proceeding.

## Anti-Patterns (BLOCKING)

| Anti-pattern | Why | Correct approach |
|-------------|-----|-----------------|
| Dump raw logs | Too much noise, no signal | Extract the insight, not the transcript |
| Write for obvious things | Wastes codemem capacity | Only capture non-obvious knowledge |
| Overwrite existing entries | Loses history | Append or create new ones |
| Skip violation example | No learning signal | Always include "what went wrong" |
| Entries over 100 words | Too verbose for codemem | Move details to SOP, keep codemem concise |
| Forget to update trigger | Nobody knows to read it | Always update AGENTS.md trigger |

## Full End-to-End Example

Here is a generic example showing the complete flow from session to final output. Replace bracketed values with actual session content.

### Session Context
- Task: [brief description of what was attempted]
- What happened: [what actually occurred]
- What we did wrong: [the mistake or wrong assumption]
- What we discovered: [the real root cause or behavior]
- Verification: [how it was confirmed]

### Step 3 Output (Codemem Entry)
```
Title: [Global/Project]: [Category] — [one-line rule]
Kind: [decision | discovery | bugfix | etc.]
Body: TRIGGER: [when to recall]\nRULE: [what to do]\nWHY: [why matters]\nVIOLATION: [what went wrong]\nTAGS: [keywords]
Confidence: 1.0
Project: [omit for global]
```

### Step 4 Output (PITFALLS.md Addition)
```markdown
### [N]. [Short title]
**症状：** [error / behavior]
**原因：** [root cause]
**解决：** [what to do]
**验证：** [how to confirm]
```

### Step 6 Output (Handoff)
```markdown
## YYYY-MM-DD
- learned: [one-line summary]
- codemem: [IDs created]
- updated: [file paths modified]
```

## Maintenance

- **Quarterly review:** Check codemem entries for duplicates or stale rules
- **When SOP becomes outdated:** Update `stale_after` date and note what changed
- **When a rule is proven wrong:** Don't delete — add a "superseded by" note with date
- **Consolidation:** Every 3 months, merge related entries and remove low-confidence ones
