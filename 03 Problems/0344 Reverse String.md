---
type: problem
number: 344
title: Reverse String
url: https://leetcode.com/problems/reverse-string/
card: "[[Card 04 Two pointers from both ends]]"
day: 4
role: solo
status: learning
attempts: 2
last_result: alone
familiarity: 4
last_attempt: 2026-10-20
next_review: 2026-10-23
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/reverse-string/) · Card: [[Card 04 Two pointers from both ends]] · Day: [[Day 04]] · Role: solo

## Trigger

- "Reverse", in place with O(1) extra memory → swap the two ends → two pointers.

## Approach

- Swap the two ends and walk inward until they meet: `l` and `r` with `while l < r`.
- Day 4's index version does the same: `for i in range(len(s) // 2)`, swapping `s[i]` with its mirror `s[len(s) - 1 - i]`. It has to stop at the middle, or it swaps every pair back.
- No copy allowed: `s[::-1]` builds a new list (O(n) memory), and the problem allows O(1).
- Say it: "Swap the two ends and walk inward until they meet."
- Index math works here because both ends always move together. In #167 they move one at a time, so you need two variables.

## Solution

```python
class Solution:
    def reverseString(self, s: list[str]) -> None:
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
```

## Complexity

- Time: O(n). n/2 swaps, and the ½ is dropped.
- Space: O(1). The swaps happen inside `s`.

## Mistakes and blank moments

- Slow solution was a nested loop again, as in #125. Each position has exactly one partner, so it's one loop.
- The first idea used `s[::-1]`: a copy, which breaks the O(1) memory rule.
- `s[i] = s[(len(s)-1)-i]` overwrote "h" before it was needed (`=` replaces). A swap, `a, b = b, a`, reads both old values first.
- The loop ran past the middle, so each pair was swapped twice: "oellh". Stop at `len(s) // 2`, or use `while l < r`.
- Found the mirror index after hint 1 and diagnosed the overwrite from the output alone.
- Day 5: ended with `return s`. The signature says `-> None` and the change is in place, so there's nothing to return.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-19 | 4 | hints | — | 3 | Solo: hint 1 (which positions swap first?), then the mirror index and the swap; fixed the loop's end |
| 2026-10-20 | 5 | alone | — | 4 | Re-solve the card's way (`l`, `r`, `while l < r`); index version kept as a comment |
