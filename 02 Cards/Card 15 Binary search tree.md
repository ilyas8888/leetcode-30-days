---
type: card
card: 15
name: Binary search tree
days: [19]
tags: [card]
---

> [!tip] Use when
> Use the order left < node < right to skip half the tree. Solves #235 and #98.

## Card

```python
def lowest_common_ancestor(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left           # both are on the left
        elif p.val > node.val and q.val > node.val:
            node = node.right          # both are on the right
        else:
            return node                # they split here

def is_valid_bst(root):
    def check(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (check(node.left, low, node.val) and
                check(node.right, node.val, high))
    return check(root, float("-inf"), float("inf"))
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0235 Lowest Common Ancestor of a Binary Search Tree]]
- [[0700 Search in a Binary Search Tree]]
- [[0098 Validate Binary Search Tree]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
