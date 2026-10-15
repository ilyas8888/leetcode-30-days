---
type: card
card: 1
name: Python toolkit
days: [1]
tags: [card]
---

> [!tip] Use when
> The built-ins every card below relies on.

## Card

```python
from collections import Counter, defaultdict, deque
import heapq

seen = set()                 # x in seen -> instant lookup
pos = {}                     # pos.get(x, -1) -> -1 if x is missing
count = Counter("banana")    # Counter({'a': 3, 'n': 2, 'b': 1})
groups = defaultdict(list)   # groups[key].append(x), no KeyError
q = deque([1, 2])            # q.append(3), then q.popleft() -> 1
stack = [1, 2]               # stack.append(3), then stack.pop() -> 3

for i, x in enumerate(["a", "b"]):   # i = 0, 1 and x = "a", "b"
    pass

sorted([("ana", 30), ("bo", 25)], key=lambda p: p[1])  # sort by 2nd item
float("inf")                 # start value when looking for a minimum
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
