---
type: card
card: 18
name: Graph breadth-first search
days: [23]
tags: [card]
---

> [!tip] Use when
> Can I reach it, and in how few steps? Build an adjacency list, then run BFS. Solves #1971.

## Card

```python
from collections import defaultdict, deque

def valid_path(n, edges, source, destination):
    graph = defaultdict(list)          # node -> its neighbours
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen, q = {source}, deque([source])
    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)          # mark when you add, not when you pop
                q.append(nxt)
    return False
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[1971 Find if Path Exists in Graph]]
- [[0994 Rotting Oranges]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
