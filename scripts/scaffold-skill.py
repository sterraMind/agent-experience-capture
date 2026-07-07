#!/usr/bin/env python3
"""
Scaffold a new skill directory structure following agentskills.io spec.

Usage:
    uv run python scripts/scaffold-skill.py --name "process-name" --category "category" --output "../skills/"

Creates:
    process-name/
    ├── SKILL.md              # Skeleton with frontmatter + section placeholders
    ├── scripts/              # Empty dir for executable helpers
    ├── references/           # Empty dir for supplementary docs
    └── assets/               # Empty dir for templates/static files

Exit 0 = success, non-zero = failure with descriptive stderr.
"""

import argparse
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path


def validate_name(name: str) -> tuple[bool, str]:
    """Validate skill name against agentskills.io spec constraints."""
    if len(name) > 64:
        return False, f"name too long: {len(name)} chars (max 64)"
    if not name.islower() and not all(c.islower() or c in '-_' for c in name):
        return False, "name must be lowercase with hyphens only"
    if '--' in name or '__' in name:
        return False, "no consecutive hyphens or underscores"
    if not name[0].isalpha():
        return False, "name must start with a letter"
    return True, ""


def validate_description(desc: str) -> tuple[bool, str]:
    """Validate description length and content."""
    if len(desc) > 1024:
        return False, f"description too long: {len(desc)} chars (max 1024)"
    if len(desc) < 10:
        return False, "description too short (min 10 chars)"
    # Check for capability + trigger context
    has_capability = any(w in desc.lower() for w in ['create', 'build', 'help', 'use', 'manage', 'implement'])
    has_trigger = any(w in desc.lower() for w in ['use when', 'trigger', 'don\'t use', 'do not use', 'avoid'])
    if not has_capability:
        return False, "description must include capability verbs"
    if not has_trigger:
        return False, "description must include trigger context (e.g., 'Use when...')"
    return True, ""


def create_skill_md(name: str, description: str, category: str) -> str:
    """Generate skeleton SKILL.md content."""
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    return textwrap.dedent(f"""\
---
name: {name}
description: "{description}"
license: Apache-2.0
metadata:
  author: kpy-team
  version: "1.0"
  last_updated: "{today}"
  category: {category}
---

# {name.replace("-", " ").title()} Skill

## Overview

[High-level purpose: what this skill does and who it helps. 2-3 sentences.]

## Quick Reference

| Scenario | Approach |
|----------|----------|
| [Common task 1] | See `references/[topic].md` |
| [Common task 2] | See `scripts/[tool].py` |
| [Common task 3] | [Direct instruction] |

## Step-by-Step Procedures

### Step 1: [First major step]

1. [Action 1]
2. [Action 2]
3. [Action 3]

### Step 2: [Second major step]

1. [Action 1]
2. [Action 2]

## Critical Rules

**CRITICAL**: [Most important rule that, if violated, causes the biggest problems.]

**CRITICAL**: [Second most important rule.]

## Error Handling

If [common failure], do [recovery action]:
1. [Step 1 of recovery]
2. [Step 2 of recovery]

See `references/common-errors.md` for complete error mapping.

## Dependencies

Requires: [List external tools, libraries, or services]
Optional: [List optional dependencies]

## Examples

### Example 1: [Typical use case]

**Input:** [What the agent receives]
**Output:** [What the agent produces]

```
[Code or file content example]
```

### Example 2: [Edge case or anti-pattern]

**Wrong:**
```
[Incorrect approach]
```

**Right:**
```
[Correct approach]
```

See `references/[topic].md` for complete fix.
""")


def scaffold_skill(name: str, description: str, category: str, output_dir: str) -> Path:
    """Create the skill directory structure."""
    # Validate
    valid, msg = validate_name(name)
    if not valid:
        print(f"ERROR: Invalid name: {msg}", file=sys.stderr)
        sys.exit(1)

    valid, msg = validate_description(description)
    if not valid:
        print(f"ERROR: Invalid description: {msg}", file=sys.stderr)
        sys.exit(1)

    # Resolve output directory
    out = Path(output_dir)
    skill_dir = out / name

    if skill_dir.exists():
        print(f"ERROR: Skill directory already exists: {skill_dir}", file=sys.stderr)
        sys.exit(1)

    # Create directory structure
    skill_dir.mkdir(parents=True, exist_ok=False)
    (skill_dir / "scripts").mkdir()
    (skill_dir / "references").mkdir()
    (skill_dir / "assets").mkdir()

    # Write SKILL.md
    skill_md = skill_dir / "SKILL.md"
    skill_md.write_text(create_skill_md(name, description, category), encoding="utf-8")

    return skill_dir


def main():
    parser = argparse.ArgumentParser(
        description="Scaffold a new agent skill directory structure.",
        epilog="Example: uv run python scripts/scaffold-skill.py --name my-process --category technical --output ../skills/",
    )
    parser.add_argument("--name", required=True, help="Skill name (lowercase, hyphens, max 64 chars)")
    parser.add_argument("--description", required=True, help="Skill description (max 1024 chars, must include capability + triggers)")
    parser.add_argument("--category", required=True, help="Skill category (e.g., technical, design, workflow)")
    parser.add_argument("--output", default="./", help="Output directory (default: current directory)")

    args = parser.parse_args()
    skill_dir = scaffold_skill(args.name, args.description, args.category, args.output)

    print(f"Created skill: {skill_dir}")
    print(f"  SKILL.md:     {skill_dir / 'SKILL.md'}")
    print(f"  scripts/:     {skill_dir / 'scripts'}")
    print(f"  references/:  {skill_dir / 'references'}")
    print(f"  assets/:      {skill_dir / 'assets'}")
    sys.exit(0)


if __name__ == "__main__":
    main()
