---
type: home
tags: [home]
---

> [!todo] Next session
> [[Day 09]] · Stack (card 9) · warm-up: cards 8 and 5 from memory · re-solve first: [[0209 Minimum Size Subarray Sum]], [[1004 Max Consecutive Ones III]]. Claude updates this line after each session.

```dataview
TABLE focus, kind
FROM "04 Sessions"
WHERE status = "planned"
SORT day
LIMIT 1
```

## Start here

- [[Learned So Far]]
- [[30-Day Plan]]
- [[Session Routine]]
- [[Rules]]
- [[RESET]]
- [[Pattern Triggers]]
- [[Interview Phrases]]
- [[After Day 30]]
- [[Roadmap.canvas]]

## Due for re-solve

```dataview
TABLE card, last_result, familiarity, next_review
FROM "03 Problems"
WHERE next_review AND next_review <= date(today)
SORT next_review
```

## Progress

Sessions done:
```dataview
TABLE WITHOUT ID length(rows) AS "Done out of 30"
FROM "04 Sessions"
WHERE status = "done"
```

Problems by last result:
```dataview
TABLE WITHOUT ID last_result AS Result, length(rows) AS Count
FROM "03 Problems"
GROUP BY last_result
```

Average familiarity per card:
```dataview
TABLE WITHOUT ID card AS Card, round(average(rows.familiarity), 1) AS "Avg familiar"
FROM "03 Problems"
WHERE familiarity
GROUP BY card
```

## Cards

- [[Card 01 Python toolkit]]
- [[Card 02 Hash map lookup]]
- [[Card 03 Counting and grouping]]
- [[Card 04 Two pointers from both ends]]
- [[Card 05 Read-write pointer]]
- [[Card 06 Running best and fixed windows]]
- [[Card 07 Reading input]]
- [[Card 08 Variable window]]
- [[Card 09 Stack]]
- [[Card 10 Binary search]]
- [[Card 11 Prefix sums]]
- [[Card 12 Linked lists]]
- [[Card 13 Tree depth-first search]]
- [[Card 14 Tree breadth-first search]]
- [[Card 15 Binary search tree]]
- [[Card 16 Heap]]
- [[Card 17 Grid depth-first search]]
- [[Card 18 Graph breadth-first search]]
- [[Card 19 Backtracking]]
- [[Card 20 Dynamic programming]]
- [[Card 21 Intervals]]

## Weeks

- **Week 1:** [[Day 01]] · [[Day 02]] · [[Day 03]] · [[Day 04]] · [[Day 05]] · [[Day 06]] · [[Day 07]]
- **Week 2:** [[Day 08]] · [[Day 09]] · [[Day 10]] · [[Day 11]] · [[Day 12]] · [[Day 13]] · [[Day 14]]
- **Week 3:** [[Day 15]] · [[Day 16]] · [[Day 17]] · [[Day 18]] · [[Day 19]] · [[Day 20]] · [[Day 21]]
- **Week 4:** [[Day 22]] · [[Day 23]] · [[Day 24]] · [[Day 25]] · [[Day 26]] · [[Day 27]] · [[Day 28]]
- **Final days:** [[Day 29]] · [[Day 30]]

> [!info]- First-time setup
> 1. In Obsidian, open this folder as a vault.
> 2. Settings → Core plugins: turn on Templates (folder `99 Templates`) and Canvas.
> 3. Optional community plugins: Dataview (live tables) and Obsidian Git (commit and push from inside Obsidian).
