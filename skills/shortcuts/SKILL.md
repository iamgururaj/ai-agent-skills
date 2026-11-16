---
name: shortcuts
description: Apply predefined prompt shortcuts to control how tasks are handled.
---

# Shortcuts

| Prefix | Behaviour |
|---|---|
| `ans:` | Answer only. No code changes. |
| `rev:` | Review code. No changes. |
| `plan:` | Create an implementation plan. No changes. |
| `web:` | Research latest information with sources. |
| `uli:` | Research latest ULI information and recommendations. |
| `gcsm:` | Inspect git diff and generate a short commit message. Never commit. |

## Rules
- Match prefixes at the start, case-insensitive.
- Apply the matching behaviour to the remaining prompt.
- `ans`, `rev`, `plan` and `gcsm` are read-only.
- Never invent findings or commit messages.
- `web` and `uli` require current information.
- No prefix: follow normal instructions.
- Unknown prefixes: treat as normal text.
- Never exceed the requested scope.