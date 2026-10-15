---
type: card
card: 9
name: Stack
days: [9]
tags: [card]
---

> [!tip] Use when
> Matching pairs, nesting, the most recent item first. Solves #20.

## Card

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:                # closing bracket
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:                          # opening bracket
            stack.append(ch)
    return not stack                   # True only if nothing is left open
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0020 Valid Parentheses]]
- [[0155 Min Stack]]
- [[0150 Evaluate Reverse Polish Notation]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
