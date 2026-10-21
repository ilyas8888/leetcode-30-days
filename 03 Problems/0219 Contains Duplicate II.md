---
type: problem
number: 219
title: Contains Duplicate II
url: https://leetcode.com/problems/contains-duplicate-ii/
card: "[[Card 06 Running best and fixed windows]]"
day: 6
role: bonus
status: learning
attempts: 1
last_result: alone
familiarity: 4
last_attempt: 2026-10-21
next_review: 2026-10-24
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/contains-duplicate-ii/) · Card: [[Card 06 Running best and fixed windows]] · Day: [[Day 06]] · Role: bonus

## Trigger

- "Two equal values at most k positions apart" → remember where each value was last seen (hash map), or keep a window of the last k numbers in a set.

## Approach

- Hash map, value → last index: if `x` was seen within k positions, return True; then store the new index. O(n) space.
- Window, today's card: a set of the last k numbers. Check, add, and drop `nums[i - k]` when the set holds more than k. O(k) space.

```python
window = set()
for i, x in enumerate(nums):
    if x in window:
        return True
    window.add(x)
    if len(window) > k:
        window.remove(nums[i - k])   # the number that fell out
return False
```

## Solution

```python
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, x in enumerate(nums):
            if x in seen and i - seen[x] <= k:
                return True
            seen[x] = i
        return False
```

## Complexity

- Time: O(n). One pass.
- Space: O(n) for the dict (the window version is O(k)).

## Mistakes and blank moments

- Solved alone. Two cleanups: `x in seen` instead of `nums[i] in seen`, and no `abs`, since `i` always comes after `seen[x]`.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-21 | 6 | alone | — | 4 | Bonus: hash map of last positions, first try |
