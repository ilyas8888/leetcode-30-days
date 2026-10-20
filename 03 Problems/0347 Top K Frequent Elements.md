---
type: problem
number: 347
title: Top K Frequent Elements
url: https://leetcode.com/problems/top-k-frequent-elements/
card: "[[Card 03 Counting and grouping]]"
day: 3
role: solo
status: learning
attempts: 3
last_result: hints
familiarity: 2
last_attempt: 2026-10-20
next_review: 2026-10-21
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/top-k-frequent-elements/) · Card: [[Card 03 Counting and grouping]] · Day: [[Day 03]] · Role: solo

## Trigger

- "The k most frequent" → count, then take the top k.

## Approach

- `Counter(nums).most_common(k)` gives (number, count) pairs, most frequent first. Keep only the numbers.

## Solution

```python
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        pairs = count.most_common(k)
        result = []
        for num, time in pairs:
            result.append(num)
        return result
```

## Complexity

- Time: O(n log n). Counting is one pass, and `most_common` sorts the counts.
- Space: O(n). The counter can hold every distinct number.

## Mistakes and blank moments

- First try reused #49's `groups` and wrote `pairs[count]`: a count used as a position, so "index out of range".
- Names: these are the k most frequent numbers, not duplicates. `top_pairs` and `result` read better; the `defaultdict` import isn't needed.
- Caught the hidden sort in `most_common` for time. Said O(k) space; the counter makes it O(n).
- Day 4: read it as "the first k elements that have duplicates" and wrote the trigger as "seen". Hint 1's example, `[1,2,2,3,3,3]` with k = 1, gives [3]: it's about the biggest counts. Read the output line twice.
- Day 4: reached for #49's `groups` and imported `defaultdict` again, as on Day 3. Top k isn't grouping.
- Day 4: collected the numbers in a set. Counter keys are already unique, so a list does it and keeps the most-frequent-first order.
- Day 4: `for i, x in` names (number, count) as if `i` were a position; `for num, times in` says what each one is.
- Day 4: said O(k) space again. It's O(n): the Counter holds every different number, and numbers aren't capped like letters.
- Day 5: read the problem right this time, with `Counter` and `most_common(k)` alone. Then:
  - `defaultdict` came back a third day;
  - the loop stored whole pairs and called `most_common` inside the loop (a sort every turn);
  - `freq.append(count.most_common(k))` nested the list (to name a result, use `=`);
  - `enumerate` was mixed up with pair unpacking.
- Day 5, their own diagnosis: "I forgot that we can do `for i, x in pairs:`". Name them `num, times`, so they don't look like `enumerate`'s position and value. Typed the full solution once more from memory, correct.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | 3 | hints | — | 3 | Solo: asked why the index was out of range, then fixed it alone |
| 2026-10-19 | 4 | hints | — | 3 | Re-solve: hint 1 fixed the reading; Counter, most_common and the pair loop alone; set changed to a list |
| 2026-10-20 | 5 | hints | — | 2 | Re-solve: needed hints up to rung 4 (the skeleton) for the pair loop; then typed it again from memory |
