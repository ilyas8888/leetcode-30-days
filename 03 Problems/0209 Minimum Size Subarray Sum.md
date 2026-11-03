---
type: problem
number: 209
title: Minimum Size Subarray Sum
url: https://leetcode.com/problems/minimum-size-subarray-sum/
card: "[[Card 08 Variable window]]"
day: 8
role: solo
status: learning
attempts: 2
last_result: hints
familiarity: 4
last_attempt: 2026-10-29
next_review: 2026-10-30
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
- Day 9 version: check `sum(nums) < target` once, before the loop, and return 0 right away. One `sum()` outside the loop is a single pass; inside the loop it would be a hidden loop.

## Solution

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        length = float("inf")
        total = 0
        if sum(nums) < target:
            return 0
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                length = min(length, r - l + 1)
                total -= nums[l]
                l += 1
        return length
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
- Day 9 re-solve, the same traps again:
  - shrink before grow, and `length` measured on every turn, valid or not, so it returned 1 whenever an answer existed (`target = 3`, `[1, 2]`);
  - `>` instead of `>=`;
  - a list as the window with `sum(array)` in the `while`: correct, but Time Limit Exceeded (about 6 billion additions for 100,000 ones);
  - space answered O(k), which was right for the list version; with the running total it's O(1).
- Fixed in two steps: the order (grow; while valid: measure, then shrink), then the list → one number (`total += nums[r]`, `total -= nums[l]`).
- `return total` returned 0 there, but reads as "return the sum". Say what you mean: `return 0`.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-23 | 8 | hints | — | 4 | Solo: hint 1 (what does the window remember?) and hint 2 (the approach in words); "understood finally" |
| 2026-10-29 | 9 | hints | — | 4 | Re-solve: the order rule in words, then hint 1 on the hidden `sum()` and the list → total table |
