---
type: card
card: 16
name: Heap
days: [20]
tags: [card]
---

> [!tip] Use when
> Top k, k-th largest, or taking the biggest or smallest again and again. Solves #1046 and #215.

## Card

```python
import heapq

def last_stone_weight(stones):
    heap = [-s for s in stones]        # negate: heapq is a min-heap
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)       # heaviest
        b = -heapq.heappop(heap)       # second heaviest
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0

def find_kth_largest(nums, k):
    heap = []                          # the k largest so far
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # drop the smallest
    return heap[0]
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[1046 Last Stone Weight]]
- [[0703 Kth Largest Element in a Stream]]
- [[0215 Kth Largest Element in an Array]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
