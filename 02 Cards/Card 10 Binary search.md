---
type: card
card: 10
name: Binary search
days: [10, 11]
tags: [card]
---

> [!tip] Use when
> Sorted input, or the smallest or largest value that works. Solves #704 and #69.

## Card

```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1                  # answer is on the right
        else:
            r = m - 1                  # answer is on the left
    return -1                          # here, l = where target would go

def my_sqrt(x):                        # binary search on the answer
    l, r = 0, x
    while l <= r:
        m = (l + r) // 2
        if m * m <= x:
            l = m + 1                  # m works: try bigger
        else:
            r = m - 1                  # m too big: go smaller
    return r                           # the last value that worked
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0704 Binary Search]]
- [[0035 Search Insert Position]]
- [[0278 First Bad Version]]
- [[0069 Sqrt(x)]]
- [[0074 Search a 2D Matrix]]
- [[0033 Search in Rotated Sorted Array]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
