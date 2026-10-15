---
type: card
card: 20
name: Dynamic programming
days: [25, 26]
tags: [card]
---

> [!tip] Use when
> Number of ways, minimum or maximum cost, choices that repeat. Solves #70, #53 and #322.

## Card

```python
# Five questions: 1) what does dp[i] mean? 2) how does it use smaller i?
# 3) base case? 4) loop order? 5) where is the answer?

def climb_stairs(n):
    prev, cur = 1, 1                   # ways to reach step 0 and step 1
    for _ in range(n - 1):
        prev, cur = cur, prev + cur
    return cur

def max_sub_array(nums):               # Kadane's algorithm
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)          # extend the run, or restart here
        best = max(best, cur)
    return best

def coin_change(coins, amount):
    dp = [0] + [float("inf")] * amount    # dp[a] = fewest coins to make a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0070 Climbing Stairs]]
- [[0746 Min Cost Climbing Stairs]]
- [[0509 Fibonacci Number]]
- [[0053 Maximum Subarray]]
- [[0198 House Robber]]
- [[0322 Coin Change]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
