---
type: card
card: 9
name: Stack
days: [9]
tags: [card]
---

> [!tip] Use when
> Matching pairs, nesting, the most recent item first. Solves #20.

Video: [Valid Parentheses - Stack - Leetcode 20 - Python (NeetCode)](https://www.youtube.com/watch?v=WTzjTskDFMg)

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

Min stack (#155): a second stack remembers the min at every level, so `getMin` is just `self.mins[-1]`.

```python
def push(self, value):
    self.stack.append(value)
    if self.mins:                      # guard [-1] with the list it reads
        self.mins.append(min(value, self.mins[-1]))
    else:                              # first push: the value is the min
        self.mins.append(value)
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
