---
type: review
tags: [review]
---

> [!tip] Learned so far
> Everything from the sessions on one page, Days 1–2 for now. Read it before each warm-up. Claude adds to it after every session.

## Patterns

| Pattern | Trigger in the problem | Key line | Card |
| --- | --- | --- | --- |
| Hash map lookup | "Have I seen this value before?", a pair that adds up to a target | `if target - x in seen:` | [[Card 02 Hash map lookup]] |
| Counting | "How many times", "the same count of each letter" | `count[ch] = count.get(ch, 0) + 1` | [[Card 03 Counting and grouping]] |
| Running total | Each item becomes itself plus everything before it | `nums[i] += nums[i - 1]` | [[Card 11 Prefix sums]] |

> [!warning] The dict rule
> Inside the brackets is the **key**; after the `=` is the **stored value**.
> `seen[x] = i` stores position `i` under the number `x`. `count[ch] = ...` stores a count under the letter `ch`.

## Python tools

| Tool | What it gives you | Example |
| --- | --- | --- |
| `enumerate(nums)` | (index, value) pairs | `for i, x in enumerate(nums):` |
| `set()` | "seen or not" | `if x in seen:` then `seen.add(x)` |
| `d.get(key, 0)` | the stored value, or 0 if the key is missing | `count.get(ch, 0)` |
| `Counter(s)` | letter → count in one line; a missing letter counts as 0 | `Counter("banana")["a"]` gives 3 |
| `+=` with the previous item | a running total, in place | `nums[i] += nums[i - 1]` |

LeetCode imports `Counter` for you. Anywhere else, add `from collections import Counter` at the top.

## Big-O

| Cost | Means | Example | Steps for 1,000,000 items |
| --- | --- | --- | --- |
| O(1) | the same work for any size | one dict or set lookup | 1 |
| O(n) | one pass | counting the letters | ~1,000,000 |
| O(n log n) | sorting | sort both words, then compare | ~20,000,000 |
| O(n²) | a loop inside a loop | for each item, scan the others | ~1,000,000,000,000 |

- Drop constants: two separate passes are O(2n), which is O(n).
- Keep different lengths apart: a note and a magazine give O(m + n).
- Space is the number of different keys: only 26 lowercase letters means O(1).
- One-liners still loop inside: `Counter(s)` is a full pass over `s`.

## RESET

**R** read it out loud · **E** a tiny example · **S** a slow solution · **E** examine the triggers · **T** template, then trace. Full version: [[RESET]].

In every session: type **blank** for the next RESET step, **hint** for the next hint, **stop** to end.

## Problems so far

| Problem | Pattern | The idea in one line |
| --- | --- | --- |
| [[0001 Two Sum]] | Hash map lookup | For each x, check whether `target - x` is already in `seen` (value → index) |
| [[0217 Contains Duplicate]] | Hash map lookup | A set: return True the moment x is already in it |
| [[0242 Valid Anagram]] | Counting | Count both strings' letters and compare the counts |
| [[0383 Ransom Note]] | Counting | Count the magazine, use each letter up; a count of 0 means False |
| [[0387 First Unique Character in a String]] | Counting | Count first, then return the first index whose count is 1 |
| [[1480 Running Sum of 1d Array]] | Running total | Add the previous item, which already holds the total so far |

Live status, with Dataview on:

```dataview
TABLE WITHOUT ID file.link AS Problem, last_result AS Result, familiarity AS Familiar, next_review AS "Next review"
FROM "03 Problems"
WHERE attempts > 0
SORT next_review ASC
```

## Mistakes to avoid

- Swapping key and value in a dict: see the dict rule above.
- `def f(string = str)` sets a default value. A type hint uses a colon: `def f(string: str)`.
- `if a == b: return True` followed by `return False` is just `return a == b`.
- Calling a loop inside a loop O(n log n): it's O(n²).
- Saying O(n) space for letter counts: it's O(1), at most 26 keys.
- Naming a technique as the trigger. Triggers come from the problem, and your own examples often show them: "only one a" → counting.
- `in` on strings looks for letters side by side: `"ac" in "abc"` is False.
- Trusting an example without tracing it: the running sum of [1, 2, 3] is [1, 3, 6], not [1, 3, 5].
