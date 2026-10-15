---
type: card
card: 13
name: Tree depth-first search
days: [16, 17]
tags: [card]
---

> [!tip] Use when
> Depth, paths, or comparing subtrees: ask the children, then combine. Solves #104 and #543.

## Card

```python
def max_depth(root):
    if not root:                       # 1. base case
        return 0
    left = max_depth(root.left)        # 2. ask both children
    right = max_depth(root.right)
    return 1 + max(left, right)        # 3. combine

def diameter_of_binary_tree(root):
    best = 0
    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)        # longest path through this node
        return 1 + max(l, r)
    height(root)
    return best
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0104 Maximum Depth of Binary Tree]]
- [[0226 Invert Binary Tree]]
- [[0100 Same Tree]]
- [[0543 Diameter of Binary Tree]]
- [[0112 Path Sum]]
- [[0110 Balanced Binary Tree]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
