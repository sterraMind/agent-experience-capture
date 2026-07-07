# Experience Capture Templates

Quick reference for output formats. Full process is in SKILL.md.

## Codemem Entry

```
codemem_memory_remember(
  kind="decision" | "discovery" | "feature" | "bugfix" | "refactor" | "exploration",
  title="[Global/Project]: [Category] — [one-line rule]",
  body="TRIGGER: [when to recall]\nRULE: [what to do]\nWHY: [why matters]\nVIOLATION: [what went wrong]\nTAGS: [keywords]",
  confidence=1.0,
  project="my-project"  # omit for global
)
```

## PITFALLS.md Entry

```markdown
### [N]. [Short title]
**症状：** [error / behavior]
**原因：** [root cause]
**解决：** [what to do]
**验证：** [how to confirm]
```

## QUICK-START.md Entry

```markdown
### [Section Title]
- **Rule:** [one-line rule]
- **Wrong:** [common mistake]
- **Right:** [correct approach]
```

## Handoff Entry

```markdown
## YYYY-MM-DD
- learned: [one-line summary]
- codemem: [IDs created]
- updated: [file paths]
```

## New Skill Entry (Step 7)

When a captured experience qualifies as a repeatable process worth packaging as a skill:

```bash
# 1. Scaffold
uv run python scripts/scaffold-skill.py --name "process-name" \
  --description "Description with capability + triggers + negatives" \
  --category "technical" \
  --output "../skills/"

# 2. Fill SKILL.md from codemem entry fields
#    TRIGGER → description, RULE → procedures, VIOLATION → examples

# 3. Validate
#    Run references/validation-checklist.md

# 4. Register
#    Copy to skills/ dir, update opencode.json, append handoff record
```

See `references/skill-templates.md` for full SKILL.md templates.
