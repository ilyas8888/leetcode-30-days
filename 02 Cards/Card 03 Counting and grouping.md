---
type: card
card: 3
name: Counting and grouping
days: [2, 3]
tags: [card]
---

> [!tip] Use when
> Compare letter counts, or group items that share a key. Solves #242 and #49.

## Card

```python
from collections import Counter, defaultdict

def is_anagram(s, t):
    return Counter(s) == Counter(t)

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))       # same letters -> same key
        groups[key].append(w)
    return list(groups.values())
```

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0242 Valid Anagram]]
- [[0383 Ransom Note]]
- [[0387 First Unique Character in a String]]
- [[0049 Group Anagrams]]
- [[0347 Top K Frequent Elements]]
- [[0997 Find the Town Judge]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
