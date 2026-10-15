---
type: card
card: 2
name: Hash map lookup
days: [1]
tags: [card]
---

> [!tip] Use when
> Know instantly whether you have seen a value before. Solves #1 Two Sum.

## Card

```python
def two_sum(nums, target):
    seen = {}                          # value -> its index
    for i, x in enumerate(nums):
        if target - x in seen:         # is my partner already here?
            return [seen[target - x], i]
        seen[x] = i
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0001 Two Sum]]
- [[0217 Contains Duplicate]]
- [[0205 Isomorphic Strings]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
