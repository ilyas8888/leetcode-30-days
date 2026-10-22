---
type: problem
number: 121
title: Best Time to Buy and Sell Stock
url: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
card: "[[Card 06 Running best and fixed windows]]"
day: 6
role: guided
status: learning
attempts: 2
last_result: alone
familiarity: 5
last_attempt: 2026-10-22
next_review: 2026-10-25
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) · Card: [[Card 06 Running best and fixed windows]] · Day: [[Day 06]] · Role: guided

## Trigger

- "Maximum profit", buy on one day and sell on a **later** day → running best in one pass.

## Approach

- Treat every day as a possible day to sell. Keep `lowest`, the cheapest price up to today, and `best`, the best profit so far. Each day, update `lowest`, then ask "what if I sell today?": `p - lowest`.
- `lowest` only holds prices from today or earlier, so you never sell before you buy. `best` starts at 0 and only goes up, so prices that only fall return 0.
- Say it: "Walk once, remember the cheapest so far, and ask every day what selling today would earn."
- Video: [Sliding Window: Best Time to Buy and Sell Stock - Leetcode 121 - Python (NeetCode)](https://www.youtube.com/watch?v=1pkOgXD63yU). His `l` is our `lowest`.

## Solution

```python
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        lowest, best = float("inf"), 0
        for p in prices:
            lowest = min(lowest, p)        # cheapest day to buy so far
            best = max(best, p - lowest)   # what if I sell today?
        return best
```

## Complexity

- Time: O(n). One pass.
- Space: O(1). Two numbers.

## Mistakes and blank moments

- Tried it alone after the theory part of the video. Tracked the lowest and the highest price separately and returned `max - min`, but the highest has to come after the lowest. On [2, 9, 1], 9 − 1 = 8 would sell before buying; the answer is 7.
- On [7, 6, 4, 3, 1], `min` stayed at infinity, and `0 − infinity` is minus infinity, which LeetCode shows as "null".
- The `elif` chain let only one update happen per turn, and `l += 1; r += 1` inside a `for` loop did nothing.
- Named the variables `max` and `min`, which hides Python's `max()` and `min()`: the very functions this card needs.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-21 | 6 | hints | — | 3 | Tried alone first (min and max tracked separately), then the card's version |
| 2026-10-22 | 7 | alone | — | 5 | Review day: card 6's running best from memory, correct |
