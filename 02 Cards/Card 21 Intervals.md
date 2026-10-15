---
type: card
card: 21
name: Intervals
days: [27]
tags: [card]
---

> [!tip] Use when
> Overlapping ranges: sort by start, then merge into the last one. Solves #56.

## Card

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])     # sort by start
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:         # overlaps the last one
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0056 Merge Intervals]]
- [[0228 Summary Ranges]]
- [[0057 Insert Interval]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
