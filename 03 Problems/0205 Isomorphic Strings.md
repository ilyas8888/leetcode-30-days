---
type: problem
number: 205
title: Isomorphic Strings
url: https://leetcode.com/problems/isomorphic-strings/
card: "[[Card 02 Hash map lookup]]"
day: 3
role: bonus
status: learning
attempts: 1
last_result: hints
familiarity:
last_attempt: 2026-10-17
next_review: 2026-10-20
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/isomorphic-strings/) · Card: [[Card 02 Hash map lookup]] · Day: [[Day 03]] · Role: bonus

## Trigger

- Each letter of s must always pair with the same letter of t → a pairing dict.

## Approach

- Two dicts: s-letter → t-letter, and t-letter → s-letter.
- At each position, if a letter already has a partner, it must be the letter on the other side at this position. Otherwise, record the pair in both dicts.

## Solution

```python
```

## Complexity

- Time:
- Space:

## Mistakes and blank moments

- `Counter(s)[i]` used a position as a key. The keys are letters, so both sides were always 0 and the code never returned False ("foo" / "bar" gave True).
- Counts can't decide this problem: "aabb" and "abab" have the same counts at every position but aren't isomorphic.
- Not solved yet: stopped after the approach in words. It comes back after the core re-solves.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | 3 | hints | — | — | Bonus: counting attempt, then the approach in words; unfinished |
