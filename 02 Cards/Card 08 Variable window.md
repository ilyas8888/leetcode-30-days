---
type: card
card: 8
name: Variable window
days: [8]
tags: [card]
---

> [!tip] Use when
> The longest or shortest contiguous part that follows a rule. Solves #3.

Video: [Longest Substring Without Repeating Characters - Leetcode 3 - Python (NeetCode)](https://www.youtube.com/watch?v=wiGpQwVHdE0)

## Card

```python
def length_of_longest_substring(s):
    seen = set()                       # what is inside the window
    l = best = 0
    for r, ch in enumerate(s):         # 1. grow on the right
        while ch in seen:              # 2. broken? shrink from the left
            seen.remove(s[l])
            l += 1
        seen.add(ch)
        best = max(best, r - l + 1)    # 3. valid again: measure it
    return best

# "Shortest" problems: update best inside the while loop instead.
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0003 Longest Substring Without Repeating Characters]]
- [[0209 Minimum Size Subarray Sum]]
- [[1004 Max Consecutive Ones III]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
