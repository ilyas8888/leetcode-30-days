---
type: card
card: 5
name: Read-write pointer
days: [5]
tags: [card]
---

> [!tip] Use when
> Keep, remove or move items in place, without a second array. Solves #283.

Video: [Move Zeroes - Leetcode 283 - Python (NeetCode)](https://www.youtube.com/watch?v=aayNRwUN3Do)

## Card

```python
def move_zeroes(nums):
    w = 0                              # next slot to write into
    for r in range(len(nums)):         # r reads every item
        if nums[r] != 0:               # keep this one
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0283 Move Zeroes]]
- [[0026 Remove Duplicates from Sorted Array]]
- [[0088 Merge Sorted Array]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
