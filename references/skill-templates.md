# Skill Templates Reference

Templates for different skill types. Use these as starting points when creating new skills from captured experience.

## Template 1: Technical Process Skill

For skills that encode a repeatable technical procedure (e.g., "deploy ComfyUI", "fix image settings").

```markdown
---
name: skill-name
description: "Perform [specific technical task] using [tools/frameworks]. Use when the user wants to [trigger context 1], [trigger context 2], or [trigger context 3]. Don't use for [negative boundary 1] or [negative boundary 2]."
license: Apache-2.0
metadata:
  author: kpy-team
  version: "1.0"
  last_updated: "YYYY-MM-DD"
  category: technical
---

# [Skill Name] Skill

## Overview

[2-3 sentences: what this skill does, who benefits, and the core problem it solves.]

## Quick Reference

| Scenario | Command/Approach |
|----------|-----------------|
| [Scenario 1] | `[command or reference]` |
| [Scenario 2] | `[command or reference]` |
| [Scenario 3] | `[command or reference]` |

## Prerequisites

- [Tool] ≥ [version]
- [Permission/Access]
- [Environment variable]

## Procedure

### Step 1: [Setup]

1. [Action]
2. [Action]

### Step 2: [Core Work]

1. [Action with code example]
2. [Action with code example]

### Step 3: [Verification]

1. [How to verify success]
2. [How to verify failure]

## Critical Rules

**CRITICAL**: [Rule that prevents the most common failure mode.]

**CRITICAL**: [Rule that prevents data loss or security issues.]

## Error Handling

| Error | Cause | Fix |
|-------|-------|-----|
| `[error message]` | `[cause]` | `[fix]` |

See `references/common-errors.md` for full error mapping.

## Dependencies

Requires: [list]
Optional: [list]
```

---

## Template 2: Design/UX Skill

For skills that encode design principles, visual standards, or UX patterns.

```markdown
---
name: skill-name
description: "Create [type] designs using [framework/style]. Use when the user wants to [trigger: build UI, redesign page, polish interface]. Don't use for backend logic, data modeling, or non-visual tasks."
license: Apache-2.0
metadata:
  author: kpy-team
  version: "1.0"
  last_updated: "YYYY-MM-DD"
  category: design
---

# [Skill Name] Skill

## Overview

[What design problems this skill solves, what aesthetic/quality bar it targets.]

## Design Principles

1. **[Principle 1]** — [Explanation + example]
2. **[Principle 2]** — [Explanation + example]
3. **[Principle 3]** — [Explanation + example]

## Quick Reference

| Design Goal | Pattern |
|-------------|---------|
| [Goal 1] | [Pattern/approach] |
| [Goal 2] | [Pattern/approach] |

## Components

### [Component Category 1]

- **Purpose:** [When to use]
- **Structure:** [Code/template example]
- **Styling:** [Key CSS/design tokens]

### [Component Category 2]

[same structure]

## Critical Rules

**CRITICAL**: [Design rule that, if violated, produces visibly poor results.]

## Visual QA Checklist

- [ ] Typography scale consistent
- [ ] Color palette matches brand
- [ ] Spacing follows 4px/8px grid
- [ ] Responsive breakpoints tested
- [ ] Accessibility contrast ratios pass

## Examples

### Good
```
[code/design example]
```

### Bad (and why)
```
[broken example]
Reason: [explanation]
```
```

---

## Template 3: Workflow/Process Skill

For skills that encode a multi-step process or decision tree (e.g., "review code", "plan architecture").

```markdown
---
name: skill-name
description: "Guide through [type of process] using [framework/methodology]. Use when the user wants to [trigger 1], [trigger 2], or [trigger 3]. Don't use for [non-applicable scenarios]."
license: Apache-2.0
metadata:
  author: kpy-team
  version: "1.0"
  last_updated: "YYYY-MM-DD"
  category: workflow
---

# [Skill Name] Skill

## Overview

[What process this skill encodes, when it should be applied, what outcomes it produces.]

## Decision Tree

```
Start
  │
  ├─ Is [condition A]? → Yes → [Path A]
  │                        No  → [Path B]
  │
  └─ Is [condition B]? → Yes → [Path C]
                         No  → [Path D]
```

## Procedure

### Phase 1: [Phase Name]

1. [Action]
2. [Action]
3. **Checkpoint:** [How to verify this phase is done]

### Phase 2: [Phase Name]

1. [Action]
2. [Action]

### Phase 3: [Phase Name]

1. [Action]
2. [Action]
3. **Final verification:** [Complete checklist]

## Critical Rules

**CRITICAL**: [Process rule that prevents skipping essential steps.]

## Anti-Patterns

| Anti-pattern | Why it fails | Correct approach |
|--------------|-------------|-----------------|
| [Bad behavior] | [Consequence] | [Better alternative] |

## Outputs

This skill produces:
- [Artifact 1] — [Description]
- [Artifact 2] — [Description]

See `scripts/[generator].py` for automated output generation.
```

---

## Mapping Codemem Entries to Skill Sections

When converting a codemem entry into a skill, use this mapping:

| Codemem Field | → Skill Section |
|---------------|----------------|
| `TRIGGER` | `description` (frontmatter) + Quick Reference table |
| `RULE` | Step-by-step Procedures |
| `WHY` | Overview paragraph |
| `VIOLATION` | Examples (Wrong/Right) + Anti-Patterns table |
| `TAGS` | Quick Reference scenarios + metadata category |

## Tips for Effective Skill Descriptions

From research findings:

1. **Include capability + trigger + negative boundary** in one sentence
2. **Be pushy** — Claude undertriggers skills; make the description slightly aggressive
3. **Use domain-native terminology** — match the words users actually type
4. **List specific triggers** — not "when needed" but "when the user mentions X, Y, Z"

### Good Description Formula

```
description: "[Verb] [object] using [tool/framework]. Use when the user [trigger 1], [trigger 2], or [trigger 3]. Don't use for [negative 1] or [negative 2]."
```

### Example: Good vs Bad

**❌ Bad:** "Helps with testing."
- No capability, no trigger, no boundary

**✅ Good:** "Sets up and runs test suites for React applications using Vitest and Testing Library. Use when the user wants to add tests, fix failing tests, or improve test coverage for a React component. Don't use for Vue, Angular, or backend API testing."
- Clear capability + specific triggers + explicit negative boundary
