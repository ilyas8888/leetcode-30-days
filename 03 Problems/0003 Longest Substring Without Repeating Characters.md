---
type: problem
number: 3
title: Longest Substring Without Repeating Characters
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
card: "[[Card 08 Variable window]]"
day: 8
role: guided
status: learning
attempts: 1
last_result: hints
familiarity: 4
last_attempt: 2026-10-23
next_review: 2026-10-24
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/) · Card: [[Card 08 Variable window]] · Day: [[Day 08]] · Role: guided

## Trigger

- "The **longest** substring **without repeating** characters" → a variable window (longest form), with a set of what's inside.

## Approach

- Three moves every turn:
  1. **Grow:** `r` brings in the next letter.
  2. **Shrink:** while that letter is already inside, remove `s[l]` and move `l`.
  3. **Measure:** `r - l + 1`, once the window is valid again.
- Say it: "Grow on the right; while it's broken, shrink from the left; then measure."
- Video: [Longest Substring Without Repeating Characters - Leetcode 3 - Python (NeetCode)](https://www.youtube.com/watch?v=wiGpQwVHdE0)

## Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = best = 0
        seen = set()
        for r, ch in enumerate(s):
            while ch in seen:
                seen.remove(s[l])
                l += 1
            seen.add(ch)
            best = max(best, r - l + 1)
        return best
```

## Complexity

- Time: O(n). The `while` can run several times in one turn, but each letter enters once and leaves at most once over the whole string.
- Space: O(min(n, m)), where m is the number of different characters (at most 128 here). The set never holds a repeat.

## Mistakes and blank moments

- Tried it from memory after the video's theory part, drawing it in Excalidraw.
- Forgot `seen.add(ch)`: the set stayed empty, so the window never shrank and "abcabcbb" returned 8.
- Wrote `seen.remove(s[0])`, the string's first letter, instead of `s[l]`, the window's first letter. That gives `KeyError: 'a'`.
- Big-O reasoning: "the while runs only once" isn't the reason; each letter leaves the window at most once overall.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-23 | 8 | hints | — | 4 | Guided: built from the video's theory and a drawing; hint 1 found the missing add and `s[l]`; card typed from memory after |
