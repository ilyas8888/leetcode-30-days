---
type: problem
number: 383
title: Ransom Note
url: https://leetcode.com/problems/ransom-note/
card: "[[Card 03 Counting and grouping]]"
day: 2
role: solo
status: learning
attempts: 2
last_result: hints
familiarity: 2
last_attempt: 2026-10-17
next_review: 2026-10-18
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/ransom-note/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 02]] · Role: solo

## Trigger

- Each magazine letter can be used once: "aa" can't come from "ab" because there is only one a → counting.

## Approach

- Way 1 (Day 2): count the magazine's letters, then use them up one by one while walking the note. A count of 0 means False.
- Way 2 (Day 3): count both strings. For each letter of the note, the magazine must have at least as many.

## Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_m = Counter(magazine)
        count_n = Counter(ransomNote)
        for ch in ransomNote:
            if count_m[ch] < count_n[ch]:
                return False
        return True
```

## Complexity

- Time: O(m + n). One pass to count each string.
- Space: O(1). Each counter holds at most 26 letters.

## Mistakes and blank moments

- Slow solution "for each note letter, search the magazine" was labelled O(n log n). A loop inside a loop is O(n × m).
- Trigger step chose sorting, so that `in` would work. `in` looks for letters side by side: note "ac", magazine "abc" gives False, but the answer is True.
- Day 2: wrote the code after getting the approach in words; used Counter's "missing letter counts as 0". The second `if count_magazine[ch] > 0` wasn't needed.
- Day 3: forgot the approach. Hint 1 (walk the note through the magazine's counts) led to Way 2, a new solution.
- Optional polish for Way 2: loop over `count_n` so each different letter is checked once.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-16 | 2 | hints | — | — | Solo: RESET comments up to the trigger, then the approach in words |
| 2026-10-17 | 3 | hints | — | 2 | Re-solve: forgot the approach; hint 1, then a new solution |
