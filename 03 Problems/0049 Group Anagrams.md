---
type: problem
number: 49
title: Group Anagrams
url: https://leetcode.com/problems/group-anagrams/
card: "[[Card 03 Counting and grouping]]"
day: 3
role: guided
status: learning
attempts: 2
last_result: hints
familiarity: 2
last_attempt: 2026-10-18
next_review: 2026-10-19
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/group-anagrams/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 03]] · Role: guided

## Trigger

- "Group the words that use the same letters" → one shared label per group.

## Approach

- Label each word with its letters sorted and glued back together: "eat", "tea" and "ate" all get "aet".
- Put each word in the box for its label (a `defaultdict(list)`), then return the boxes.

## Solution

```python
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            label = "".join(sorted(s))   # the thing you look up by
            groups[label].append(s)      # the thing you store
        return list(groups.values())
```

## Complexity

- Time: O(n · k log k). One pass over the n words, and sorting each word of up to k letters costs k log k.
- Space: O(n · k). The dict stores every word, plus a label for each group.

## Mistakes and blank moments

- Went straight to the fast solution at step S, with the dict rule the right way round.
- Said time is O(n): missed the hidden sort inside the loop. Count the loops you can't see.
- In the Learn block before it: swapped key and value (`groups["eat"].append("aet")`), used `=` where `.append` was needed, and wrote `List` with a capital L.
- Day 4 warm-up: used the word itself as the key (`groups[s]`) with an if/else and `=`. Fix: name the label first, `label = "".join(sorted(s))`, then `groups[label].append(s)`. The Say it → Name it → Check it method came out of this mistake.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | 3 | hints | — | 4 | Guided: RESET one step at a time; wrote it in one line inside the loop |
| 2026-10-18 | 4 | hints | — | 2 | Warm-up re-solve: the word as the key and `=` instead of append; fixed with the label line |
