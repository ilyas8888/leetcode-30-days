---
type: problem
number: 643
title: Maximum Average Subarray I
url: https://leetcode.com/problems/maximum-average-subarray-i/
card: "[[Card 06 Running best and fixed windows]]"
day: 6
role: solo
status: learning
attempts: 2
last_result: hints
familiarity: 4
last_attempt: 2026-10-22
next_review: 2026-10-23
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/maximum-average-subarray-i/) · Card: [[Card 06 Running best and fixed windows]] · Day: [[Day 06]] · Role: solo

## Trigger

- "Contiguous subarray of length k" + "maximum average" → a fixed window, plus a running best.

## Approach

- Sum the first window, then slide: add the new number at `r`, drop the one at `r - k`. After every slide, keep the best so far.
- `best` starts as the **first window**, not 0: averages can be negative, and the first window has to be compared too.
- Polish: keep the window as a sum of whole numbers and divide by k once at the end, `return best / k`.
- Say it: "Slide a window of k numbers, and keep the best window you've seen."
- Video: [Maximum Sum Subarray of Size K - Sliding Window Pattern Explained (CodeLucky)](https://www.youtube.com/watch?v=-cLczYQt48A)

## Solution

```python
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best = window
        for r in range(k, len(nums)):
            window += nums[r] - nums[r - k]
            best = max(window, best)
        return best / k
```

## Complexity

- Time: O(n). One pass; each slide costs O(1).
- Space: O(1).

## Mistakes and blank moments

- In the Learn block, typed the window as `range(1, …)` and `nums[k] - nums[r]`. `r` is the new number on the right, and the one that leaves is at `r - k`.
- The drawing first started at the 5 (already in the window), dropped one position too far right, and restarted from 8 on every line. Fixed: 8 → 7 → 9 → 6.
- Wrote `window = nums[:k]` without `sum(...)`: that's a list, not a total.
- Solo: `best = 0.00`. The first window was never compared ([9, 1, 1], k = 2 gave 1 instead of 5), and negative averages lost to 0 ([-1, -2, -3], k = 2 gave 0 instead of −1.5).
- Added special cases (`k >= len(nums)`, `k == 1: return nums[1]`) that only patched that bug, and `nums[1]` was wrong for k = 1. With `best = avg`, the loop handles every case.
- Day 7, with the window kept as a sum: `best = nums[0]`, a single number instead of the first window's sum.
  - When `k == len(nums)`, the loop never runs: [1, 2], k = 2 gave 0.5 instead of 1.5.
  - A big first number beat every window: [10, -5, -5, 1], k = 2 gave 5.0 instead of 2.5.
  - Fix: `best = window`.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-21 | 6 | hints | — | 4 | Solo: window + running best alone; fixed `best = 0.00` to `best = avg` after asking why |
| 2026-10-22 | 7 | hints | — | 4 | Review day, as card 6's window: `best = nums[0]` fixed to `best = window` after asking why |
