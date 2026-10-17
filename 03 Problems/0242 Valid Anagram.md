---
type: problem
number: 242
title: Valid Anagram
url: https://leetcode.com/problems/valid-anagram/
card: "[[Card 03 Counting and grouping]]"
day: 2
role: guided
status: learning
attempts: 2
last_result: alone
familiarity: 4
last_attempt: 2026-10-17
next_review: 2026-10-20
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/valid-anagram/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 02]] · Role: guided

## Trigger

- "The same count of each letter" → counting.

## Approach

- Build a letter → count dict for each string. They're anagrams if the two dicts are equal.

## Solution

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        if count_s == count_t:
            return True
        return False
```

## Complexity

- Time: O(n). Two separate passes, and O(2n) is O(n).
- Space: O(1). Each dict holds at most 26 keys, because the input is only lowercase letters.

## Mistakes and blank moments

- Slow solution: sort both strings and compare, O(n log n). Counting is O(n).
- The trigger step first listed properties of a hash map. Triggers come from the problem: "same count of each letter" → counting.
- Shorter ending: `return count_s == count_t` replaces the `if` and both returns.
- Card version: `return Counter(s) == Counter(t)`. Use the loop version if the interviewer says "no Counter".
- Said space is O(n); with only 26 lowercase letters, it's O(1).

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-16 | 2 | hints | — | — | Guided: RESET one step at a time with Claude; built from own counting loop |
| 2026-10-17 | 3 | alone | — | 4 | Re-solve in the warm-up: `return Counter(s) == Counter(t)` from memory |
