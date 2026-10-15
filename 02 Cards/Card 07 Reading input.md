---
type: card
card: 7
name: Reading input
days: [7]
tags: [card]
---

> [!tip] Use when
> For HackerRank-style tests, where you read the input yourself and print the answer.

## Card

```python
import sys

data = sys.stdin.read().split()        # every value, whatever the layout
n = int(data[0])
nums = list(map(int, data[1:1 + n]))
print(sum(nums))                       # print only the answer

# Line by line instead:
# n = int(input())
# nums = list(map(int, input().split()))
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- None yet — this card supports the others.

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
