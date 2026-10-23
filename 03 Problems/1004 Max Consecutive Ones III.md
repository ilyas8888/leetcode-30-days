---
type: problem
number: 1004
title: Max Consecutive Ones III
url: https://leetcode.com/problems/max-consecutive-ones-iii/
card: "[[Card 08 Variable window]]"
day: 8
role: bonus
status: learning
attempts: 1
last_result: solution
familiarity: 3
last_attempt: 2026-10-23
next_review: 2026-10-24
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/max-consecutive-ones-iii/) · Card: [[Card 08 Variable window]] · Day: [[Day 08]] · Role: bonus

## Trigger

- "The **maximum** number of consecutive 1s if you can flip **at most k** 0s" → a variable window (longest form) that may hold at most k zeros.

## Approach

- The window only needs one number: `zeros`, how many 0s are inside. It's broken when `zeros > k`.
- It's #3 line for line:
  - `seen.add(ch)` becomes "if `nums[r]` is 0, `zeros += 1`";
  - `while ch in seen` becomes `while zeros > k`;
  - `seen.remove(s[l])` becomes "if `nums[l]` is 0, `zeros -= 1`".
- Inside the shrink, look at the number **leaving** (`nums[l]`), and move `l` on **every** turn.

## Solution

```python
class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l = best = 0
        zeroes = 0
        for r, x in enumerate(nums):
            if x == 0:
                zeroes += 1
            while zeroes > k:
                if nums[l] == 0:
                    zeroes -= 1
                l += 1
            best = max(best, r - l + 1)
        return best
```

## Complexity

- Time: O(n). Each number enters once and leaves at most once.
- Space: O(1).

## Mistakes and blank moments

- Went blank on this bonus at the end of the session and needed the hints all the way to the full solution.
- Tries along the way:
  - a dict `seen[x] = x`;
  - a `while` ending with `break`, which is just an `if`;
  - `r - l - 1` instead of `r - l + 1`;
  - measuring before the shrink.
- Last try looped forever: the shrink checked `x`, the number coming **in**, and moved `l` only inside the `if`. When the number was a 1, nothing changed. Every turn of a `while` must move something.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-23 | 8 | solution | — | 3 | Bonus: hints 1–3, then the full solution explained with a step visual; retyped it |
