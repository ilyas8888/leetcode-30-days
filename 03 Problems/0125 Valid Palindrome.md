---
type: problem
number: 125
title: Valid Palindrome
url: https://leetcode.com/problems/valid-palindrome/
card: "[[Card 04 Two pointers from both ends]]"
day: 4
role: guided
status: done
attempts: 3
last_result: alone
familiarity: 5
last_attempt: 2026-10-23
next_review: 2026-10-30
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/valid-palindrome/) · Card: [[Card 04 Two pointers from both ends]] · Day: [[Day 04]] · Role: guided

## Trigger

- "Palindrome" → compare the two ends → two pointers. The trigger is the word in the problem, not how the solution moves ("parallelism").

## Approach

- Slow: keep the letters and digits, lowercased, in a list, then compare it with its reverse: `chars == chars[::-1]`. O(n) time, but O(n) space for the copy.
- Two pointers: `l` starts at the first position, `r` at the last. Skip anything that isn't a letter or a digit, compare the two characters ignoring case, and move both inward when they match. Same O(n) time, O(1) space: two pointers save space, not time.
- Say it: "Compare the two ends and walk inward; any mismatch is False."

## Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l += 1
                r -= 1
        return True
```

## Complexity

- Time: O(n). Every turn moves at least one pointer inward, so the loop runs at most n times.
- Space: O(1). Only two positions are stored.

## Mistakes and blank moments

- Slow solution was a nested loop. In a palindrome each position has one partner, its mirror, so the loop isn't nested: a nested version fails on "abba" at i = 0, j = 2.
- Trigger: said "parallelism" (how the solution moves) instead of the word in the problem, "palindrome".
- Typing the card: `s[l].lower` without `()` is the method itself, never equal to a letter, so every palindrome returned False.
- Trace on "it's an Exam, maxe nasti ": the l, r and letter columns were right on every turn, but the branch column copied the example's "skip right". Pick the branch by reading the `if/elif` lines from the top: the first true one runs.
- The one-sentence idea said "the indexes aren't the same"; it's the characters at the indexes. `l` and `r` are positions, `s[l]` and `s[r]` are letters.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-19 | 4 | hints | — | 4 | Guided: card written from memory first, then the slow way, the trigger and a 6-turn trace with Claude |
| 2026-10-20 | 5 | alone | — | 4 | Warm-up: card 4 from memory in LeetCode format, all correct, `()` on `.lower()` included |
| 2026-10-23 | 8 | alone | — | 5 | Warm-up: card 4 from memory, correct |
