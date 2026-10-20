---
type: problem
number: 26
title: Remove Duplicates from Sorted Array
url: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
card: "[[Card 05 Read-write pointer]]"
day: 5
role: solo
status: learning
attempts: 1
last_result: hints
familiarity: 4
last_attempt: 2026-10-20
next_review: 2026-10-21
tags: [problem]
---

> [!info] Problem
> [Open on LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) · Card: [[Card 05 Read-write pointer]] · Day: [[Day 05]] · Role: solo

## Trigger

- "Remove the duplicates in place" from a **sorted** array, so equal numbers sit next to each other → read/write pointer.

## Approach

- Keep a number when it differs from the last kept one. The array is sorted, so one comparison is enough.
- Return k, the number of unique values. LeetCode also checks that the first k slots hold them, in order.
- In the solution below, `w` sits on the last kept number and you write at `w + 1`, so the count is `w + 1`.
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
        w = 0
        for r in range(len(nums)):
            if nums[w] != nums[r]:
                nums[r], nums[w+1] = nums[w+1], nums[r]
                w += 1
        return w + 1
```

## Complexity

- Time: O(n). One pass.
- Space: O(1). Everything happens inside `nums`.

## Mistakes and blank moments

- Hint 1 mapped it onto card 5: in #283 you keep a number when it isn't 0; here, when it differs from the last kept one.
- Designed the loop alone in Excalidraw ([1,1,2,2,3] → [1,2,1,2,3] → [1,2,3,2,1]), and the loop was right.
- The return was wrong: on [1,1,2], LeetCode showed [1,2,1], so the function returned 3. `w` ends on the last unique number, and positions start at 0, so the count is `w + 1`.
- Expected to return nothing, because #283 and #344 don't. Read `->` in the signature: `-> int` means return a number, even when the list is also changed in place.

## Attempts

| Date | Day | Result | Minutes | Familiar (1–5) | Note |
| --- | --- | --- | --- | --- | --- |
| 2026-10-20 | 5 | hints | — | 4 | Solo: hint 1, then own design in Excalidraw; return fixed to `w + 1` |
