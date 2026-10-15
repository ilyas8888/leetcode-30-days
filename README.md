# leetcode-30-days

A 30-day, pattern-first LeetCode practice plan in Python, built as an Obsidian vault.
It doubles as Claude's memory: each session you send "Day N" to Claude in the claude.ai app, and it reads this repo from GitHub to pick up exactly where you stopped.
The goal is familiarity, not mastery — recognizing a problem's shape and knowing your first moves.

## Folders

| Folder | What's inside |
| --- | --- |
| `00 Home.md` | Dashboard: next session, due re-solves, progress, links to everything |
| `01 Plan/` | The plan, session routine, rules, RESET, pattern triggers, phrases, roadmap |
| `02 Cards/` | 21 pattern template cards |
| `03 Problems/` | 72 problem notes |
| `04 Sessions/` | 30 day notes |
| `05 Mocks/` | 4 mock-interview notes |
| `06 Cheat Sheet/` | One-page summary, filled in on day 30 |
| `90 Claude/` | Claude's memory between sessions |
| `99 Templates/` | Note skeletons |
| `scripts/` | `check_vault.py` and `new_problem.py` |

## How a session works

1. Send **Day N** to Claude in the claude.ai app.
2. Solve the problems on LeetCode in its editor, without AI autocomplete.
3. Log each attempt in the matching Obsidian note.
4. Commit and push.

Run `python scripts/check_vault.py` (on Windows, `py scripts/check_vault.py`) to check for broken links and print your progress: sessions done, the next planned day, problems by status and last result, and re-solves due today.
