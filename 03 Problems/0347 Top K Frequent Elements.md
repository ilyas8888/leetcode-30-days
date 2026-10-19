---
type: problem
number: 347
title: Top K Frequent Elements
url: https://leetcode.com/problems/top-k-frequent-elements/
card: "[[Card 03 Counting and grouping]]"
day: 3
role: solo
status: learning
attempts: 2
last_result: hints
familiarity: 3
last_attempt: 2026-10-19
next_review: 2026-10-20
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
        freq = []
        for i, x in count.most_common(k):
            freq.append(i)
        return freq
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

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-17 | 3 | hints | — | 3 | Solo: asked why the index was out of range, then fixed it alone |
| 2026-10-19 | 4 | hints | — | 3 | Re-solve: hint 1 fixed the reading; Counter, most_common and the pair loop alone; set changed to a list |
