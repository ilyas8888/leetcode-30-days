---
type: problem
number: 26
title: Remove Duplicates from Sorted Array
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
card: "[[Card 05 Read-write pointer]]"
day: 5
role: solo
status: learning
attempts: 4
last_result: alone
familiarity: 5
last_attempt: 2026-10-23
next_review: 2026-10-26
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · Card: [[Card 05 Read-write pointer]] · Day: [[Day 05]] · Role: solo

## Trigger

- "Remove the duplicates in place" from a **sorted** array, so equal numbers sit next to each other → read/write pointer.

## Approach

- Keep a number when it differs from the last kept one. The array is sorted, so one comparison is enough.
- Return k, the number of unique values. LeetCode also checks that the first k slots hold them, in order.
- In the solution below, `l` sits on the last kept number. When `nums[r]` differs from it, swap it into slot `l + 1` and move `l` forward. The answer is `l + 1`, because positions start at 0.
- Day 6's version wrote instead of swapping, with the same idea: `if nums[i] < nums[i + 1]: count += 1; nums[count] = nums[i + 1]`, then `return count + 1`.
- The card's way: `w` is the next empty slot, so the count is `w` itself.

```python
w = 1
for r in range(1, len(nums)):
    if nums[r] != nums[w - 1]:
        nums[w] = nums[r]
        w += 1
return w
```

- Say it: "Read every number; when it differs from the last kept one, write it into the next slot."

## Solution

```python
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        l = 0
        for r in range(len(nums)):
            if nums[l] != nums[r]:
                nums[r], nums[l + 1] = nums[l + 1], nums[r]
                l += 1
        return l + 1
```

## Complexity

- Time: O(n). One pass.
- Space: O(1). Everything happens inside `nums`.

## Mistakes and blank moments

- Hint 1 mapped it onto card 5: in #283 you keep a number when it isn't 0; here, when it differs from the last kept one.
- Designed the loop alone in Excalidraw ([1,1,2,2,3] → [1,2,1,2,3] → [1,2,3,2,1]), and the loop was right.
- The return was wrong: on [1,1,2], LeetCode showed [1,2,1], so the function returned 3. `w` ends on the last unique number, and positions start at 0, so the count is `w + 1`.
- Expected to return nothing, because #283 and #344 don't. Read `->` in the signature: `-> int` means return a number, even when the list is also changed in place.
- Day 6: a sharp trigger ("sorted, so a number bigger than the one before it is new"), and the count was right. But the code only counted and never wrote into `nums`, so on [1, 1, 2] the first two slots stayed 1, 1. LeetCode checks the k you return **and** the first k slots. Fix: `nums[count] = nums[i + 1]`.
- Day 7: wrote the loop alone but ended with a bare `return` (None). After a guided hint ("what does `l` mean at the end?"), found `return l + 1` and the reason: positions start at 0. Also left an `r += 1` inside the `for`, which does nothing.
- Day 8: alone, with no `r += 1`, and said it right: "`l` ends on the biggest number of the unique part; positions start at 0, so return `l + 1`."

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-20 | 5 | hints | — | 4 | Solo: hint 1, then own design in Excalidraw; return fixed to `w + 1` |
| 2026-10-21 | 6 | hints | — | 4 | Re-solve: counted the new numbers but didn't write them; one line added |
| 2026-10-22 | 7 | hints | — | 4 | Review day: the loop alone; the return value after a guided hint |
| 2026-10-23 | 8 | alone | — | 5 | Re-solve: alone, return explained in their own words |
