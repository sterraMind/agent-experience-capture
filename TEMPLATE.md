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
