---
type: problem
number: 283
title: Move Zeroes
url: https://leetcode.com/problems/move-zeroes/
card: "[[Card 05 Read-write pointer]]"
day: 5
role: guided
status: learning
attempts: 2
last_result: alone
familiarity: 5
last_attempt: 2026-10-21
next_review: 2026-10-24
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/move-zeroes/) · Card: [[Card 05 Read-write pointer]] · Day: [[Day 05]] · Role: guided

## Trigger

- "Move all 0s to the end", "in place", "keep the relative order" → read/write pointer.

## Approach

- `r` reads every item; `w` is the next slot to write into. When `nums[r]` isn't 0, swap it into slot `w` and move `w` forward. Everything left of `w` is kept, in the original order, and the swaps push the zeros back.
- Say it: "Read every item. When you keep one, swap it into the write slot and move the write slot forward."
- Video: [Move Zeroes - Leetcode 283 - Python (NeetCode)](https://www.youtube.com/watch?v=aayNRwUN3Do)

## Solution

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        w = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[w], nums[r] = nums[r], nums[w]
                w += 1
```

## Complexity

- Time: O(n). One pass.
- Space: O(1). The swaps happen inside `nums`.

## Mistakes and blank moments

- Tried it alone first, after the theory part of the video, drawing it in Excalidraw: `w, r = 0, 1`, a `while` loop and three branches.
- The swap branch moved neither pointer. On `[0, 0, 1]` it swapped two zeros forever: Time Limit Exceeded. "Run" only used the visible examples; "Submit" ran the hidden ones.
- When both numbers were non-zero, only `w` moved, so on `[1, 2, 3]` it passed `r` and ran off the end (IndexError).
- Fix: the card's shape. `for r in range(len(nums))` moves `r` every turn by itself, and `w` moves only when you keep a number, so `w` never passes `r`.
- The retyped version kept `else: r += 1`. In a `for` loop that does nothing: the loop sets `r` again at the next turn.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-20 | 5 | hints | — | 4 | Tried alone with a drawing first; time limit, then the card's version |
| 2026-10-21 | 6 | alone | — | 5 | Warm-up: card 5 from memory, drawn in Excalidraw first |
