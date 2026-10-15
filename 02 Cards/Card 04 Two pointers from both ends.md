---
type: card
card: 4
name: Two pointers from both ends
days: [4]
tags: [card]
---

> [!tip] Use when
> Sorted array or palindrome: start at both ends and move inward. Solves #125.

## Card

```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1                     # skip a non-letter on the left
        elif not s[r].isalnum():
            r -= 1                     # skip a non-letter on the right
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1                     # both match: move inward
            r -= 1
    return True
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0125 Valid Palindrome]]
- [[0344 Reverse String]]
- [[0167 Two Sum II - Input Array Is Sorted]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
