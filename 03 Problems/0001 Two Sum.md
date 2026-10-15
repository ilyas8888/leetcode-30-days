---
type: problem
number: 1
title: Two Sum
url: https://leetcode.com/problems/two-sum/
card: "[[Card 02 Hash map lookup]]"
day: 1
role: guided
status: learning
attempts: 1
last_result: hints
familiarity: 2
last_attempt: 2026-10-15
next_review: 2026-10-16
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/two-sum/) · Card: [[Card 02 Hash map lookup]] · Day: [[Day 01]] · Role: guided

## Trigger

## Approach

## Solution

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
```

## Complexity

- Time: O(n). One pass over the list, and each dict lookup is instant (O(1)).
- Space: O(n). The dict can hold up to n values.

## Mistakes and blank moments

- While learning the card, wrote `seen[i] = x`. The dict must map value → index, because `in seen` only checks keys. Read `seen[x] = i` as "value x was seen at position i."
- The LeetCode editor was on Python (Python 2); switched to Python3.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | 1 | hints | 6 | 2 | Guided: card taught first, then written from memory |
