---
type: problem
number: 217
title: Contains Duplicate
url: https://leetcode.com/problems/contains-duplicate/
card: "[[Card 02 Hash map lookup]]"
day: 1
role: solo
status: learning
attempts: 1
last_result: alone
familiarity: 5
last_attempt: 2026-10-15
next_review: 2026-10-18
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/contains-duplicate/) · Card: [[Card 02 Hash map lookup]] · Day: [[Day 01]] · Role: solo

## Trigger

- "Have I seen this value before?" → a hash set.

## Approach

## Solution

```python
class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
```

## Complexity

- Time: O(n). One pass, and each set lookup is O(1).
- Space: O(n). The set can hold up to n values.

## Mistakes and blank moments

- The first version used a dict and stored an index it never read. When you only need "seen or not", use a set.
- Used `i` for values. `i` usually means an index, so `x` or `num` reads better.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | 1 | alone | 6 | 5 | Solo; rewrote it with a set afterwards |
