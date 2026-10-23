---
type: problem
number: 209
title: Minimum Size Subarray Sum
url: https://leetcode.com/problems/minimum-size-subarray-sum/
card: "[[Card 08 Variable window]]"
day: 8
role: solo
status: learning
attempts: 1
last_result: hints
familiarity: 4
last_attempt: 2026-10-23
next_review: 2026-10-24
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/minimum-size-subarray-sum/) · Card: [[Card 08 Variable window]] · Day: [[Day 08]] · Role: solo

## Trigger

- "The **minimal length** of a subarray whose sum is **greater than or equal to** target" → a variable window, shortest form.

## Approach

- The window only needs its **total**: one number, not a set. Add `nums[r]` when a number enters, subtract `nums[l]` when one leaves.
- Every turn: **grow** first (`total += x`). Then, **while** `total >= target`, the window is valid: **measure** `best = min(best, r - l + 1)`, **then shrink**.
- Shortest vs longest: here you shrink while the window is still **valid** and measure each time; in #3 you shrink while it's **broken** and measure after.
- If `best` is still infinity at the end, no window reached the target: return 0.

## Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        best = float("inf")
        total = 0
        for r, x in enumerate(nums):
            total += x
            while total >= target:
                best = min(best, r - l + 1)
                total -= nums[l]
                l += 1
        if best == float("inf"):
            return 0
        return best
```

## Complexity

- Time: O(n). Each number enters once and leaves at most once.
- Space: O(1). Only `l`, `total` and `best`.

## Mistakes and blank moments

- First version used a set as the window:
  - a set keeps only one copy of repeated numbers (nums had two 2s and two 3s);
  - `sum(seen)` inside the `while` adds everything again on every check.
- The other slips in that version:
  - `> target` where the problem says "greater than or equal to";
  - shrinking before adding the new number;
  - measuring after shrinking;
  - checking `sum(seen) < target` at the end instead of `best == inf`.
- Wrote space as O(n); the running total makes it O(1).

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-23 | 8 | hints | — | 4 | Solo: hint 1 (what does the window remember?) and hint 2 (the approach in words); "understood finally" |
