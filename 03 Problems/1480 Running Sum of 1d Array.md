---
type: problem
number: 1480
title: Running Sum of 1d Array
url: https://leetcode.com/problems/running-sum-of-1d-array/
card: "[[Card 11 Prefix sums]]"
day: 1
role: bonus
status: learning
attempts: 1
last_result: solution
familiarity: 3
last_attempt: 2026-10-15
next_review: 2026-10-16
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) · Card: [[Card 11 Prefix sums]] · Day: [[Day 01]] · Role: bonus

## Trigger

## Approach

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

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | 1 | solution | — | 3 | Bonus; learned from a video |
