# Validation Checklist — agentskills.io Spec Compliance

Use this checklist to verify a skill before registering it. Every check must pass.

## Frontmatter Validation

- [ ] `name` field present, ≤ 64 characters
- [ ] `name` is lowercase with hyphens only (no consecutive hyphens/underscores)
- [ ] `name` matches the parent directory name exactly
- [ ] `description` field present, ≤ 1024 characters
- [ ] `description` includes **capability** (what it does)
- [ ] `description` includes **trigger context** (when to use it)
- [ ] `description` includes **negative boundary** (when NOT to use it)
- [ ] `description` uses third-person imperative tone
- [ ] `license` field present (Apache-2.0 or Proprietary)
- [ ] `metadata.version` present
- [ ] `metadata.last_updated` in YYYY-MM-DD format

## SKILL.md Body Validation

- [ ] Total lines ≤ 500 (if over, move details to `references/`)
- [ ] Has an **Overview** section (2-3 sentences)
- [ ] Has a **Quick Reference** table mapping scenarios to approaches
- [ ] Has **Step-by-Step Procedures** with numbered steps
- [ ] Has a **Critical Rules** section with **CRITICAL:** prefix warnings
- [ ] Has an **Error Handling** section
- [ ] Has at least 2 **Examples** (good and bad patterns)
- [ ] Uses forward slashes in file references (e.g., `references/foo.md`)
- [ ] All file references are **one level deep** (no nested paths like `references/a/b.md`)
- [ ] No XML tags in content
- [ ] No reserved words in content

## Directory Structure Validation

- [ ] Root contains only: `SKILL.md`, `scripts/`, `references/`, `assets/`
- [ ] **No** `README.md` in skill root
- [ ] **No** `CHANGELOG.md` in skill root
- [ ] **No** `INSTALLATION.md` in skill root
- [ ] **No** documentation files that should be in `references/`
- [ ] `scripts/` contains only tiny CLIs (not library code)
- [ ] `scripts/` has no `.py` files named `utils.py`, `helpers.py`, `api_client.py`
- [ ] `references/` files are focused (one topic per file)
- [ ] `assets/` contains templates or static resources (not source code)

## Script Validation (if scripts/ exists)

- [ ] Each script exits 0 on success, non-zero on failure
- [ ] Each script writes errors to stderr, results to stdout
- [ ] Each script handles edge cases gracefully (no unhandled exceptions)
- [ ] Scripts accept arguments via `sys.argv` or `argparse`
- [ ] No scripts exceed 200 lines (split into smaller utilities if over)

## Triggering Accuracy Validation

- [ ] Skill triggers on ≥ 3 distinct user prompt patterns
- [ ] Skill does NOT trigger on simple one-step queries
- [ ] Description is "pushy" enough to combat Claude's undertriggering tendency
- [ ] Negative boundaries prevent overtriggering on adjacent domains

## Quality Score (from SkillsBench)

Rate the skill on a 1-12 scale. Top-quartile skills score 9+.

| Dimension | Score (1-4) | Notes |
|-----------|-------------|-------|
| **Specificity** — Does the skill mention exact tools, versions, edge cases? | | |
| **Testability** — Can you verify the output is correct? | | |
| **Decision Logic** — Does it include branching/conditionals, not just flat rules? | | |
| **Error Handling** — Does it cover failure modes with recovery steps? | | |
| **Examples** — Are there concrete good/bad examples? | | |
| **Scope Fit** — Is it narrowly focused (single responsibility)? | | |

**Total:** ___ / 24 (aim for ≥ 18 = top quartile)

## Registration Checklist

- [ ] Validation checklist passed (all items checked)
- [ ] Quality score ≥ 9/12
- [ ] Skill copied to target directory (`~/.config/opencode/skills/` or project `.agents/skills/`)
- [ ] Registered in `opencode.json` or equivalent config
- [ ] Handoff record appended to `.agents/handoff.md`
- [ ] Codemem entry created linking experience source → new skill
