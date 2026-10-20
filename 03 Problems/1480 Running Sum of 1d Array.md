---
type: problem
number: 1480
title: Running Sum of 1d Array
url: https://leetcode.com/problems/running-sum-of-1d-array/
card: "[[Card 11 Prefix sums]]"
day: 1
role: bonus
status: done
attempts: 3
last_result: alone
familiarity: 5
last_attempt: 2026-10-20
next_review: 2026-10-27
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) · Card: [[Card 11 Prefix sums]] · Day: [[Day 01]] · Role: bonus

## Trigger

- Each item becomes itself plus everything before it → a running total (prefix sums, [[Card 11 Prefix sums]]).

## Approach

- Walk from index 1 and add the previous value. By the time the loop reaches i, `nums[i - 1]` has already been updated, so it holds the total of everything before i.

## Solution

```python
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
```

## Complexity

- Time: O(n). One pass.
- Space: O(1) extra. It overwrites `nums` in place; say so in an interview, or build a new list if the input must stay unchanged.

## Mistakes and blank moments

- Got stuck and watched a video instead of starting with RESET or asking for a hint.
- Re-solve example said [1, 2, 3] → [1, 3, 5]; it's [1, 3, 6]. A hand trace showed why: at i = 2, `nums[1]` is already 3, not 2. The list keeps its 3 items; the code changes values in place.
- Slow solution "for each i, add up everything before it" was labelled O(n log n). A loop inside a loop is O(n²).

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | 1 | solution | — | 3 | Bonus; learned from a video |
| 2026-10-16 | 2 | alone | — | — | Re-solve: all RESET steps written alone; code right, the trace fixed the example |
| 2026-10-20 | 5 | alone | — | 5 | Re-solve at the end of the session; time and space right |
