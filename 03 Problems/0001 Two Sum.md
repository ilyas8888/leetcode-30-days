---
type: problem
number: 1
title: Two Sum
url: https://leetcode.com/problems/two-sum/
card: "[[Card 02 Hash map lookup]]"
day: 1
role: guided
status: done
attempts: 3
last_result: alone
familiarity: 4
last_attempt: 2026-10-20
next_review: 2026-10-27
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/two-sum/) · Card: [[Card 02 Hash map lookup]] · Day: [[Day 01]] · Role: guided

## Trigger

- "Two numbers that add up to target", in an unsorted array → for each x, look for its partner `target - x` among the numbers seen so far: a hash map.

## Approach

- One pass. For each x, check whether `target - x` is already in `seen` (value → index). If it is, return both positions; if not, store x with its index.

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
- Day 5: wrote the space as "O(index when target - x in seen)". Big-O is the worst case: the pair can be the last two numbers, so `seen` can hold almost all n numbers → O(n).

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-15 | 1 | hints | 6 | 2 | Guided: card taught first, then written from memory |
| 2026-10-16 | 2 | alone | 6 | — | Re-solve from memory; `seen[x] = i` right this time |
| 2026-10-20 | 5 | alone | — | 4.5 | Re-solve at the end of the session; space fixed to O(n) |
