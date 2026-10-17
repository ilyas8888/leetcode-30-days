---
type: problem
number: 347
title: Top K Frequent Elements
url: https://leetcode.com/problems/top-k-frequent-elements/
card: "[[Card 03 Counting and grouping]]"
day: 3
role: solo
status: learning
attempts: 1
last_result: hints
familiarity: 3
last_attempt: 2026-10-17
next_review: 2026-10-18
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 03]] · Role: solo

## Trigger

- "The k most frequent" → count, then take the top k.

## Approach

- `Counter(nums).most_common(k)` gives (number, count) pairs, most frequent first. Keep only the numbers.

## Solution

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        nums_duplicates = []
        duplicates = Counter(nums).most_common(k)
        for num, count in duplicates:
            nums_duplicates.append(num)
        return nums_duplicates
```

## Complexity

- Time: O(n log n). Counting is one pass, and `most_common` sorts the counts.
- Space: O(n). The counter can hold every distinct number.

## Mistakes and blank moments

- First try reused #49's `groups` and wrote `pairs[count]`: a count used as a position, so "index out of range".
- Names: these are the k most frequent numbers, not duplicates. `top_pairs` and `result` read better; the `defaultdict` import isn't needed.
- Caught the hidden sort in `most_common` for time. Said O(k) space; the counter makes it O(n).

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | 3 | hints | — | 3 | Solo: asked why the index was out of range, then fixed it alone |
