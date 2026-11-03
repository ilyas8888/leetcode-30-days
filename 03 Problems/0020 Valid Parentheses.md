---
type: problem
number: 20
title: Valid Parentheses
url: https://leetcode.com/problems/valid-parentheses/
card: "[[Card 09 Stack]]"
day: 9
role: guided
status: learning
attempts: 1
last_result: solution
familiarity: 2
last_attempt: 2026-10-30
next_review: 2026-10-31
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/valid-parentheses/) · Card: [[Card 09 Stack]] · Day: [[Day 09]] · Role: guided

## Trigger

- "Brackets must be closed by the **same type**, in the **right order**" → a stack: each closing bracket must match the most recent opening bracket that's still open.

## Approach

- Opening bracket: push it on the stack.
- Closing bracket: the top of the stack must be its partner, `couples[c]` (the value stored under the closing bracket). If it is, pop it: that pair is closed. If the stack is empty or the top is wrong, return False.
- At the end, the stack must be empty: `return not stack`.
- In `if stack and stack[-1] == ...`, the `and` stops before `stack[-1]` when the stack is empty.
- Say it: "Push every opener; each closer must match the top, which I pop; at the end nothing may be left open."
- Video: [Valid Parentheses - Stack - Leetcode 20 - Python (NeetCode)](https://www.youtube.com/watch?v=WTzjTskDFMg)

## Solution

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        couples = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in couples:
                if stack and stack[-1] == couples[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return not stack
```

## Complexity

- Time: O(n). One pass; push and pop are O(1).
- Space: O(n). The stack can hold every character, as in `"(((((("`.

## Mistakes and blank moments

- Wrote it while watching the video's coding part, then typed the card from memory, correct.
- The first version ended with `if not stack: return True` / `else: return False`, which is just `return not stack`.
- In the explanation: `if stack` only checks that the stack isn't empty (a closer with nothing open → False); `couples[c]` is the **value** for the key `c`, the matching opener; and the pop, which closes the pair, was left out.
- The RESET comments had no trigger line: "pairs that must close in the right order → stack".

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-30 | 9 | solution | — | 2 | Guided: written alongside the video's coding part; then the card typed from memory, correct |
