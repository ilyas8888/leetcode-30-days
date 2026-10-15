---
type: card
card: 11
name: Prefix sums
days: [12]
tags: [card]
---

> [!tip] Use when
> Sums of ranges, or counting subarrays with a given sum. Solves #724 and #560.

## Card

```python
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
# sum of nums[i..j] = prefix[j + 1] - prefix[i]

def pivot_index(nums):
    total, left = sum(nums), 0
    for i, x in enumerate(nums):
        if left == total - left - x:   # left side == right side
            return i
        left += x
    return -1

def subarray_sum(nums, k):
    seen = {0: 1}                      # prefix sum -> times seen
    total = count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)   # earlier prefixes that leave k
        seen[total] = seen.get(total, 0) + 1
    return count
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[1480 Running Sum of 1d Array]]
- [[0724 Find Pivot Index]]
- [[0303 Range Sum Query - Immutable]]
- [[0560 Subarray Sum Equals K]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
