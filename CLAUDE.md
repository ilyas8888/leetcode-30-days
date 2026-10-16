# CLAUDE.md

This repository is a 30-day LeetCode practice vault for a junior developer working in Python. It is three things at once: a Git repo pushed to GitHub after every session, an Obsidian vault opened daily, and your memory between sessions. The goal is familiarity, not mastery — reading a problem, recognizing its shape, and knowing the first moves.

## At the start of a session, read in this order

1. `90 Claude/STATUS.md` — where we are and what comes next.
2. `90 Claude/profile.md` — how they learn and how to help them.
3. `90 Claude/weak-spots.md` — recurring trouble and the fixes that work.
4. The day's note in `04 Sessions/` (for example `Day 07.md`).

## Folders

- `00 Home.md` — dashboard: next session, due re-solves, progress, links to everything.
- `01 Plan/` — the plan, session routine, rules, RESET, pattern triggers, interview phrases, roadmap.
- `02 Cards/` — 21 pattern template cards.
- `03 Problems/` — 72 problem notes.
- `04 Sessions/` — 30 day notes.
- `05 Mocks/` — 4 mock-interview notes.
- `06 Cheat Sheet/` — `Learned So Far.md` (everything learned so far, updated after each session) and the one-page cheat sheet, filled in on day 30.
- `90 Claude/` — your memory (this folder).
- `99 Templates/` — the note skeletons.
- `scripts/` — `check_vault.py` (progress + broken-link check) and `new_problem.py`.

## How to help me

- Follow `01 Plan/Session Routine.md` and `01 Plan/Rules.md`.
- Start every problem with RESET (`01 Plan/RESET.md`).
- Give hints only when they type **hint**, one rung of the hint ladder at a time.
- When reviewing their code, name the exact line, explain why, give only the fix, one change at a time, and let them retype it.
- Python unless they ask otherwise.

## At the end of a session, update in this order

1. The problem notes: a new Attempts row, the properties, and the final working solution under `## Solution`.
2. The day note: checkboxes, recap, blank moments, `status`, `date`.
3. `90 Claude/STATUS.md`.
4. `90 Claude/session-summaries.md` (3 lines at most, newest first).
5. `90 Claude/weak-spots.md`.
6. The "Next session" line in `00 Home.md`.
7. `06 Cheat Sheet/Learned So Far.md`: add the session's new patterns, tools, problems and mistakes.

Then commit with the message `day NN: <focus> (#n, #n)` and push.

## Re-solve rule for `next_review`

- Saw the solution, or needed hints → the next day.
- Solved alone → 3 days later.
- Solved alone twice in a row → 7 days later, and set `status: done`.

## Property schemas

Problem notes:

```yaml
type: problem
number: 1
title: Two Sum
url: https://leetcode.com/problems/two-sum/
card: "[[Card 02 Hash map lookup]]"
day: 1
role: guided        # guided | solo | bonus
status: todo        # todo | learning | done
attempts: 0
last_result:        # alone | hints | solution
familiarity:        # 1-5, from the latest attempt
last_attempt:       # YYYY-MM-DD
next_review:        # YYYY-MM-DD
tags: [problem]
```

Session notes:

```yaml
type: session
day: 1
week: 1
kind: learn         # learn | review | mixed | final
focus: Hash map lookup
cards: ["[[Card 01 Python toolkit]]", "[[Card 02 Hash map lookup]]"]
status: planned     # planned | done | minimum
date:               # YYYY-MM-DD, filled in when done
tags: [session]
```

Card notes:

```yaml
type: card
card: 2
name: Hash map lookup
days: [1]
tags: [card]
```

Mock notes:

```yaml
type: mock
mock: 1
day: 14
status: planned     # planned | done
date:
tags: [mock]
```

## Privacy

Never write health, personal or other sensitive details about them anywhere in this repo.
