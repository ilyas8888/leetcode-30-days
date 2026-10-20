---
type: review
tags: [review]
---

> [!tip] Learned so far
> Everything from Days 1–5 on one page. Read it before each warm-up. Claude adds to it after every session.

## Patterns

| Pattern | Trigger in the problem | Key line | Card |
| --- | --- | --- | --- |
| Hash map lookup | "Have I seen this value before?", a pair that adds up to a target | `if target - x in seen:` | [[Card 02 Hash map lookup]] |
| Counting | "How many times", "the same count of each letter" | `count[ch] = count.get(ch, 0) + 1` | [[Card 03 Counting and grouping]] |
| Grouping | Group the items that share something, like the same letters | `groups["".join(sorted(w))].append(w)` | [[Card 03 Counting and grouping]] |
| Top k | "The k most frequent" | `Counter(nums).most_common(k)` | [[Card 03 Counting and grouping]] |
| Running total | Each item becomes itself plus everything before it | `nums[i] += nums[i - 1]` | [[Card 11 Prefix sums]] |
| Two pointers from both ends | "Palindrome", "reverse", or a sorted array and a pair | `while l < r:` … `l += 1` and `r -= 1` | [[Card 04 Two pointers from both ends]] |
| Read/write pointer | "In place" + move, remove or keep some items | `if nums[r] != 0:` then swap `nums[w], nums[r]` and `w += 1` | [[Card 05 Read-write pointer]] |

Videos: card 5, [Move Zeroes - Leetcode 283 - Python (NeetCode)](https://www.youtube.com/watch?v=aayNRwUN3Do).

> [!warning] Four rules that prevent most bugs
> 1. **Inside the brackets is the key; after `=` is the stored value.** `seen[x] = i` stores position `i` under the number `x`.
> 2. **`=` replaces, `.append` adds.** `groups[label] = w` loses the earlier words; `groups[label].append(w)` keeps them all.
> 3. **Parentheses build, brackets read.** `Counter(s)` builds a counter; `count[ch]` reads from one. Parentheses also run a method: `s[l].lower()` gives the letter, `s[l].lower` only names the method.
> 4. **A position isn't a value or a key.** `i` from `enumerate` is a position; a count is how many times. Ask which one you have before indexing.

## Python tools

| Tool | What it gives you | Example |
| --- | --- | --- |
| `enumerate(nums)` | (position, value) pairs | `for i, x in enumerate(nums):` |
| `set()` | "seen or not" | `if x in seen:` then `seen.add(x)` |
| `d.get(key, 0)` | the stored value, or 0 if the key is missing | `count.get(ch, 0)` |
| `Counter(s)` | item → count in one line; a missing key counts as 0 | `Counter("banana")["a"]` gives 3 |
| `Counter(s).most_common(k)` | the k most frequent (item, count) pairs, most frequent first | `Counter("banana").most_common(2)` gives `[('a', 3), ('n', 2)]` |
| `sorted("tea")` | a **list** of the letters, in order | `['a', 'e', 't']` |
| `"".join(letters)` | one string glued from a list of letters | `"".join(['a', 'e', 't'])` gives `'aet'` |
| `defaultdict(list)` | a dict whose new keys start with an empty list | `groups[label].append(w)` never crashes |
| `d.values()` | the stored values, without their keys | `list(groups.values())` |
| `for a, b in pairs:` | each pair unpacked into two names | `for num, count in pairs:` |
| `l, r = 0, len(s) - 1` | two names set at once; the last position is `len(s) - 1` | positions start at 0 |
| `while l < r:` | repeats while the condition holds; you move the pointers yourself | forget `l += 1` and it never ends |
| `ch.isalnum()` | True for a letter or a digit | `",".isalnum()` gives False |
| `ch.lower()` | the lowercase letter | `"E".lower()` gives `'e'` |
| `a, b = b, a` | a swap: both old values are read first, then written | `s[l], s[r] = s[r], s[l]` |
| `s[::-1]` | a reversed **copy**, n extra slots | `[1, 2, 3][::-1]` gives `[3, 2, 1]` |
| `n // 2` | division that drops the remainder | `5 // 2` gives `2` |
| `for r in range(len(nums)):` | positions 0 to n − 1; the loop moves `r` by itself | an `r += 1` inside does nothing |
| `-> None` / `-> int` | what the function must give back | `-> None`: change in place, return nothing |

Outside LeetCode, add `from collections import Counter, defaultdict` at the top.

## Big-O

| Cost | Means | Example | Steps for 1,000,000 items |
| --- | --- | --- | --- |
| O(1) | the same work for any size | one dict or set lookup | 1 |
| O(n) | one pass | counting the letters | ~1,000,000 |
| O(n log n) | sorting | sort both words, then compare | ~20,000,000 |
| O(n²) | a loop inside a loop | for each item, scan the others | ~1,000,000,000,000 |

- Drop constants: two separate passes are O(2n), which is O(n).
- Keep different sizes apart: a note and a magazine give O(m + n); n words of k letters give O(n · k).
- **Count the loops you can't see:** `Counter(s)` is a full pass, `sorted(w)` costs k log k for a word of k letters, and `most_common` sorts the counts.
- Space is the number of different keys: letters are capped at 26, so O(1); numbers aren't, so O(n). Returning only k of them doesn't change that: the Counter still holds them all.
- Two pointers: O(n) time, because every turn moves a pointer inward; O(1) space, just two positions. Cleaning and reversing is also O(n) time but O(n) space, so two pointers save space, not time.
- Swapping inside the input is O(1) space; building a copy like `s[::-1]` is O(n).
- Big-O is the worst case: in #1 the pair can be the last two numbers, so `seen` can hold almost all n of them → O(n) space.
- `Counter(s) == Counter(t)` is O(n), not O(log n): each `Counter` reads every letter once.

## RESET

**R** read it out loud · **E** a tiny example · **S** a slow solution · **E** examine the triggers · **T** template, then trace. Full version: [[RESET]].

In every session: type **blank** for the next RESET step, **hint** for the next hint, **stop** to end. When your mind goes blank at T, the skeleton with blanks gets you moving.

For solos and re-solves, start the editor with these comments:

```python
# input / output:
# example:
# slow solution:
# trigger:
# say it:
```

The slow solution: if each position has exactly one partner (its mirror, `len(s) - 1 - i`), it's one loop, not a loop inside a loop.

## Stuck at T: say it, name it, check it

1. **Say it** in one sentence, from the table below.
2. **Name it:** give each thing in the sentence its own variable (`label`, `seen`, `count`, `l`, `r`), then turn the sentence into code piece by piece.
3. **Check it:** brackets hold what you look things up by; `=` replaces, `.append` adds; trace one tiny example.

| Pattern | Say it |
| --- | --- |
| Seen before (#217) | "Return True the moment a number is already in my seen set." |
| Hash map lookup (#1) | "For each number, check whether target minus it is already in seen; if not, store it with its index." |
| Counting (#242, #383, #387) | "Count everything first, then read the counts." |
| Grouping (#49) | "Put each word in the box for its label: its letters, sorted." |
| Top k (#347) | "Count everything, take the k biggest counts, keep only the numbers." |
| Running total (#1480) | "Each item becomes itself plus the total before it." |
| Two pointers from both ends (#125, #344) | "Compare or swap the two ends, then walk inward until they meet." |
| Read/write pointer (#283, #26) | "Read every item. When you keep one, write it into the next slot and move the write slot forward." |

## Problems so far

| Problem | Pattern | The idea in one line |
| --- | --- | --- |
| [[0001 Two Sum]] | Hash map lookup | For each x, check whether `target - x` is already in `seen` (value → index) |
| [[0217 Contains Duplicate]] | Hash map lookup | A set: return True the moment x is already in it |
| [[0242 Valid Anagram]] | Counting | Count both strings' letters and compare the counts |
| [[0383 Ransom Note]] | Counting | For each note letter, the magazine needs at least as many |
| [[0387 First Unique Character in a String]] | Counting | Count first, then return the first index whose count is 1 |
| [[0049 Group Anagrams]] | Grouping | Label each word with its sorted letters; same label, same box |
| [[0347 Top K Frequent Elements]] | Top k | `most_common(k)`, then keep only the numbers from the pairs |
| [[0205 Isomorphic Strings]] | Pairing (unfinished) | Each letter of s always pairs with one letter of t, and no two share a partner: two dicts |
| [[1480 Running Sum of 1d Array]] | Running total | Add the previous item, which already holds the total so far |
| [[0125 Valid Palindrome]] | Two pointers | Skip anything that isn't a letter or digit, compare the two ends ignoring case, walk inward |
| [[0344 Reverse String]] | Two pointers | Swap the two ends and walk inward; stop at the middle |
| [[0283 Move Zeroes]] | Read/write pointer | Keep every non-zero: swap it into slot `w`, then `w += 1` |
| [[0026 Remove Duplicates from Sorted Array]] | Read/write pointer | Keep a number when it differs from the last kept one; return the count |

Live status, with Dataview on:

```dataview
TABLE WITHOUT ID file.link AS Problem, last_result AS Result, familiarity AS Familiar, next_review AS "Next review"
FROM "03 Problems"
WHERE attempts > 0
SORT next_review ASC
```

## Mistakes to avoid

**Dicts and counters**
- Swapping key and value: rule 1.
- `count(ch, 0)` needs `.get`: `count.get(ch, 0)`. Without it, Python tries to call the dict and crashes.
- `Counter[s]` should be `Counter(s)`: rule 3.
- Looping over a Counter gives its keys (the letters), not counts or positions. Loop over the string with `enumerate(s)`, then read `count[ch]`.
- `Counter(s)[i]` with a position `i` always gives 0: a position isn't a key.
- `groups[label] = w` loses words: rule 2.
- `groups[s]` uses the word as the key. The key is the label: `"".join(sorted(s))` (#49).
- "Seen or not" calls for a set, not a dict with `count[x] = x` (#217).
- Counter keys are already unique: collect them in a list, which also keeps the order, not a set (#347).
- `groups` and `defaultdict` don't belong in top k. That's #49's tool (#347).
- Grouping needs no `if` and no seen set: `defaultdict(list)` makes the first box itself. Checking "seen before" loses the first word of every group (#49).
- `most_common(k)` gives (number, count) pairs. Name the result with `=` (`pairs = …`, not `.append`), then unpack each pair on its own: `for num, times in pairs:`, with no `enumerate` (#347).

**Lists and loops**
- `pairs[count]` uses a count as a position, so Python says "index out of range".
- `List` with a capital L isn't defined: use `list`.
- `reverse=True` belongs to `sorted`, not to `join`.
- `in` on strings looks for letters side by side: `"ac" in "abc"` is False.
- "Appears only once" means a count of 1. A letter taken from the string never has a count of 0.
- A loop inside a loop when each position has one partner: the partner of `i` is `len(s) - 1 - i`, so it's one loop (#125, #344).
- `s[i] = s[j]` overwrites the letter at `i` before you need it. Swap instead: `s[i], s[j] = s[j], s[i]` (#344).
- A loop that runs past the middle swaps every pair twice and undoes the work. Stop at `len(s) // 2`, or use `while l < r` (#344).
- "In place with O(1) extra memory" rules out `s[::-1]`, which builds a copy (#344).
- A `while` branch that moves no pointer can loop forever: swapping two zeros changed nothing (#283). Every turn must move something.
- In a `for` loop, `r += 1` does nothing: the loop sets `r` again at the next turn (#283).
- Know what your pointer means at the end: if `w` sits on the last kept item, the count is `w + 1` (#26).

**Code style**
- `def f(string = str)` sets a default value. A type hint uses a colon: `def f(string: str)`.
- `if a == b: return True` followed by `return False` is just `return a == b`.
- Name things for what they hold: `top_pairs`, not `duplicates`; `for num, times in pairs:`, not `for i, x in pairs:` (`i` reads as a position).
- `.lower` without `()` is the method itself, never equal to a letter, so every comparison fails. Write `.lower()` (#125).

**Big-O**
- A loop inside a loop is O(n²), not O(n log n).
- Hidden loops cost time: `Counter`, `sorted` and `most_common`.
- Letter counts take O(1) space; number counts take O(n), even when you return only k of them (#347).
- Two inputs of different sizes: O(m + n), not O(n) (#383).

**Habits**
- Triggers come from the problem, and your own examples often show them: "only one a" → counting.
- Trace before trusting an example: the running sum of [1, 2, 3] is [1, 3, 6], not [1, 3, 5].
- The trigger is a word in the problem ("palindrome", "reverse", "most frequent"), not how the solution moves ("parallelism").
- Read the output line twice: #347 asks for "the k most frequent", not "the elements that repeat". If your example fits both readings, make one that doesn't: `[1,2,2,3,3,3]`, k = 1 → [3].
- In a trace, pick the branch by reading the `if/elif` lines from the top: the first true one runs.
- Read `->` in the signature before coding: `-> None` means change in place and return nothing (#283, #344); `-> int` means return a number too (#26).
- "Sorted" is a trigger word on its own: a sorted array and a pair → two pointers (#167).
- Draw the steps (Excalidraw) before coding: it found the right loop for #26.
