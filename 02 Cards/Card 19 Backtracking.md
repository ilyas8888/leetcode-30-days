---
type: card
card: 19
name: Backtracking
days: [24]
tags: [card]
---

> [!tip] Use when
> Generate every subset, combination or permutation. Solves #78.

## Card

```python
def subsets(nums):
    res, path = [], []
    def backtrack(start):
        res.append(path[:])            # save a COPY of the current choice
        for i in range(start, len(nums)):
            path.append(nums[i])       # 1. choose
            backtrack(i + 1)           # 2. explore
            path.pop()                 # 3. undo
    backtrack(0)
    return res

# Every backtracking problem: choose, explore, undo. Only the rules change.
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0078 Subsets]]
- [[0046 Permutations]]
- [[0017 Letter Combinations of a Phone Number]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
