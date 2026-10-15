---
type: card
card: 6
name: Running best and fixed windows
days: [6]
tags: [card]
---

> [!tip] Use when
> Track the best value so far in one pass, or slide a window of fixed size k. Solves #121; the window is the core of #643.

## Card

```python
def max_profit(prices):
    lowest, best = float("inf"), 0
    for p in prices:
        lowest = min(lowest, p)        # cheapest day to buy so far
        best = max(best, p - lowest)   # what if I sell today?
    return best

# Fixed window of size k: add the new right item, drop the old left one
window = sum(nums[:k])
for r in range(k, len(nums)):
    window += nums[r] - nums[r - k]
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0121 Best Time to Buy and Sell Stock]]
- [[0643 Maximum Average Subarray I]]
- [[0219 Contains Duplicate II]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
