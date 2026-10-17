---
type: problem
number: 387
title: First Unique Character in a String
url: https://leetcode.com/problems/first-unique-character-in-a-string/
card: "[[Card 03 Counting and grouping]]"
day: 2
role: bonus
status: learning
attempts: 2
last_result: hints
familiarity: 2
last_attempt: 2026-10-17
next_review: 2026-10-18
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/first-unique-character-in-a-string/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 02]] · Role: bonus

## Trigger

- "The first letter that appears only once" → counting.

## Approach

- Two passes. Count every letter first, then walk the string in order and return the first index whose count is 1. Return -1 if there is none.
- One pass isn't enough: when you meet a letter, you can't know yet whether it appears again later.

## Solution

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)                 # pass 1: count every letter
        for i, ch in enumerate(s):         # pass 2: walk the string in order
            if count[ch] == 1:
                return i
        return -1
```

## Complexity

- Time: O(n). Two passes.
- Space: O(1). At most 26 letters in the counter.

## Mistakes and blank moments

- The slow solution checked only to the right of each letter. It must check the whole string: in "aab", the a at index 1 has no a on its right, but it isn't unique.
- Day 2: stuck at T after naming the counting trigger; typed "stuck" instead of looking it up. Stopped there and read the solution.
- Day 3: the slow solution was labelled O(n²) correctly. Wrote `Counter[s]` (brackets read, parentheses build) and looped over the Counter, which gives letters, not counts or positions.
- Day 3: went blank at T; the skeleton with blanks got things moving. Tested `== 0` first and fixed it to `== 1` alone: a letter from the string always appears at least once.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-16 | 2 | solution | — | — | Bonus: RESET up to the trigger, hint 1, then saw the solution |
| 2026-10-17 | 3 | hints | — | 2 | Re-solve: RESET alone; hint 1, then the skeleton after a blank |
