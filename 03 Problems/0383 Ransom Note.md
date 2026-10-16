---
type: problem
number: 383
title: Ransom Note
url: https://leetcode.com/problems/ransom-note/
card: "[[Card 03 Counting and grouping]]"
day: 2
role: solo
status: learning
attempts: 1
last_result: hints
familiarity:
last_attempt: 2026-10-16
next_review: 2026-10-17
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/ransom-note/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 02]] · Role: solo

## Trigger

- Each magazine letter can be used once: "aa" can't come from "ab" because there is only one a → counting.

## Approach

- Count the magazine's letters. For each letter of the note: if its count is 0, return False; otherwise use it up (subtract 1). If the whole note is covered, return True.

## Solution

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_magazine = Counter(magazine)
        for ch in ransomNote:
            if count_magazine[ch] == 0:
                return False
            if count_magazine[ch] > 0:
                count_magazine[ch] -= 1
        return True
```

## Complexity

- Time: O(m + n). One pass to count the magazine (Counter loops inside), one pass over the note.
- Space: O(1). The counter holds at most 26 letters.

## Mistakes and blank moments

- Slow solution "for each note letter, search the magazine" was labelled O(n log n). A loop inside a loop is O(n × m).
- Trigger step chose sorting, so that `in` would work. `in` looks for letters side by side: note "ac", magazine "abc" gives False, but the answer is True.
- Wrote the code after getting the approach in words; used Counter's "missing letter counts as 0".
- The second `if count_magazine[ch] > 0` can go: past the first `if`, the count is already above 0.
- Said O(n) time and O(n) space; it's O(m + n) and O(1).

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-16 | 2 | hints | — | — | Solo: RESET comments up to the trigger, then the approach in words |
