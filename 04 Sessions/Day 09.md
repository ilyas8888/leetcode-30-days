---
type: session
day: 9
week: 2
kind: learn
focus: Stack
cards: ["[[Card 09 Stack]]"]
status: done
date: 2026-11-03
tags: [session]
---

> [!todo] Day 09 · Stack
> Cards: [[Card 09 Stack]] · Problems: [[0020 Valid Parentheses]], [[0155 Min Stack]], [[0150 Evaluate Reverse Polish Notation]]

## Plan

- Guided: [[0020 Valid Parentheses]]
- Solo: [[0155 Min Stack]]
- Bonus: [[0150 Evaluate Reverse Polish Notation]]
- Re-solve:
  - In the warm-up: card 8 from memory covers [[0003 Longest Substring Without Repeating Characters]], and card 5 covers [[0283 Move Zeroes]].
  - First, before the new card: [[0209 Minimum Size Subarray Sum]] and [[1004 Max Consecutive Ones III]].
  - If time is left: [[0347 Top K Frequent Elements]], [[0049 Group Anagrams]] and [[0219 Contains Duplicate II]] (each solved alone last time), then [[0205 Isomorphic Strings]].

## Routine

- [x] Warm-up · 10 min — rewrite 2 cards from memory, then name the pattern for 5 titles
- [x] Learn · 20 min — type today's card three times: copy it, fill the gaps, from memory
- [ ] Reset · 5 min — stand up, drink water, look at something far away
- [x] Guided problem · 25 min — solve it with Claude using RESET, thinking out loud
- [x] Reset · 5 min — stand up, drink water, look at something far away
- [x] Solo problem · 25 min — 20-minute timer, alone, hints only if you ask, then review
- [ ] Reset · 5 min — stand up, drink water, look at something far away
- [x] Re-solve · 20 min — 1–2 earlier problems from memory, then the bonus if time is left
- [x] Close · 5 min — write 3 sentences, log the attempts
- [x] Commit and push

How the session ran:
1. Spread over four sittings: 2026-10-25, 10-29, 10-30 and 11-03.
2. Warm-up: card 8 (#3) fixed after hint 1 (remove `s[l]`, then move `l`; a set, not a list). Card 5 (#283) after hint 1: card 8's `while` and `l += 1` had leaked in. Titles: 3 right (Majority Element, Remove Element, Longest Repeating Character Replacement) and 2 half right (Squares of a Sorted Array → two pointers from both ends; Intersection of Two Arrays → a set).
3. Re-solves: #209 (the order for "shortest", then a running total instead of `sum()` of a list) and #1004 (count the new zero first, no flipping in `nums`, a shrink that walks one step, `count > k`), both after several hints.
4. Card 9 with the NeetCode video and a step visual. #20 guided, written alongside the video's coding part, then the card typed from memory, correct.
5. #155 solo: the slow version first, then hints up to the full solution with a side-by-side visual. Typed from memory, correct, four days later.
6. Skipped: the #150 bonus and the "if time" re-solves.

## Recap

- When the pattern applies: when we want to insert and remove from the end in instant time.
- Its key line: — (skipped at the close)
- What I did when I got stuck: — (skipped at the close)

## Blank moments

- What happened: got confused on #155 after several one-line fixes, each of which changed a line that already worked.
- RESET step that got me moving: T. The whole solution at once with a side-by-side visual of the two stacks, then typing it from memory.

## Next time

- The stack trigger comes from the problem's words: matching pairs, nesting, "the most recent one first". The close sentence described how a stack works, not when to use it.
- A stack's space is O(n): it can hold every item (#20), and #155 keeps two lists that grow with each push.
- Guard `[-1]` with the list it reads: `if self.mins:` before `self.mins[-1]`, like `if stack and stack[-1] == ...` in #20.
- When fixing one line, leave the lines that already work alone.
- Read/write pointer vs window: one `if` per number and `w`; a `while` that shrinks and `l`.
- Windows: the shrink walks one step at a time (check `nums[l]`, then `l += 1`); broken means more than k.

← [[Day 08]] · [[Day 10]] →
