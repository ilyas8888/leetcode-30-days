---
type: card
card: 14
name: Tree breadth-first search
days: [18]
tags: [card]
---

> [!tip] Use when
> Anything level by level. Solves #102.

## Card

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):        # exactly one level
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0102 Binary Tree Level Order Traversal]]
- [[0637 Average of Levels in Binary Tree]]
- [[0111 Minimum Depth of Binary Tree]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
