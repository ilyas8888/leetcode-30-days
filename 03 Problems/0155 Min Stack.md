---
type: problem
number: 155
title: Min Stack
url: https://leetcode.com/problems/min-stack/
card: "[[Card 09 Stack]]"
day: 9
role: solo
status: learning
attempts: 1
last_result: solution
familiarity: 3
last_attempt: 2026-11-03
next_review: 2026-11-04
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/min-stack/) · Card: [[Card 09 Stack]] · Day: [[Day 09]] · Role: solo

## Trigger

- "Design a stack that supports push, pop, top, and retrieving the **minimum** element in **constant time**" → a stack plus a second stack that remembers the min at every level.

## Approach

- A design problem: LeetCode gives a class. `__init__` runs once when the object is created; anything you keep goes on `self` (`self.stack = []`), so every method can reach it.
- Two lists, always the same length: `self.stack` holds the values, and `self.mins[i]` holds the smallest value from the bottom up to level `i`.
- push: append the value; append to `mins` the smaller of the value and the current min (`self.mins[-1]`), or the value itself on the first push.
- pop: pop both lists. The min goes back to what it was before, with no search.
- top: `self.stack[-1]`. getMin: `self.mins[-1]`.
- Say it: "Keep a second stack with the min at every level: push adds one, pop removes one, getMin reads its top."

## Solution

```python
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if self.mins:
            self.mins.append(min(value, self.mins[-1]))
        else:
            self.mins.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]
```

## Complexity

- Time: O(1) for every method.
- Space: O(n). Both lists grow by one with each push. (Answered O(1) on Day 9.)

## Mistakes and blank moments

- Didn't know how to start a class: `__init__` and `self` were new (format help, not a hint).
- First version, the slow solution: `getMin` was `min(self.stack)`, a hidden O(n) loop, and `pop` was `self.stack.remove(self.stack[-1])`, which removes the **first** copy of that value: push 1, 2, 1, then pop gave `[2, 1]` instead of `[1, 2]`. Use `self.stack.pop()`.
- Filled in the min column right (−2, −2, −3, then −2 after the pop), but "what does that column behave like?" was too abstract. The table with the two real lists worked.
- Then, fixing one line at a time, lines that already worked got changed:
  - `min(self.stack)` moved into `push`, still O(n);
  - `getMin` changed to return the top;
  - `self.stack.append(value)` disappeared;
  - `self.mins[-1]` was read on the first push, while `mins` was empty (IndexError);
  - the guard from #20 was copied as `self.stack[-1] == self.mins`, a number compared with a list, always False.
- Got confused, so the whole solution came at once with a side-by-side visual (hint 5). Four days later, typed the whole class from memory, correct.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-11-03 | 9 | solution | — | 3 | Solo (10-30): slow version, hints, then the full solution with a visual; typed from memory, correct, on 11-03 |
