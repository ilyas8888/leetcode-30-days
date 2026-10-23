---
type: session
day: 8
week: 2
kind: learn
focus: Variable sliding window
cards: ["[[Card 08 Variable window]]"]
status: done
date: 2026-10-23
tags: [session]
---

> [!todo] Day 08 · Variable sliding window
> Cards: [[Card 08 Variable window]] · Problems: [[0003 Longest Substring Without Repeating Characters]], [[0209 Minimum Size Subarray Sum]], [[1004 Max Consecutive Ones III]]

## Plan

- Guided: [[0003 Longest Substring Without Repeating Characters]]
- Solo: [[0209 Minimum Size Subarray Sum]]
- Bonus: [[1004 Max Consecutive Ones III]]
- Re-solve:
  - In the warm-up: card 4 from memory covers [[0125 Valid Palindrome]], plus [[0344 Reverse String]] the card's way.
  - First, before the new card: [[0026 Remove Duplicates from Sorted Array]] and [[0643 Maximum Average Subarray I]].
  - [[0205 Isomorphic Strings]] if time is left.

## Routine

- [x] Warm-up · 10 min — rewrite 2 cards from memory, then name the pattern for 5 titles
- [x] Learn · 20 min — type today's card three times: copy it, fill the gaps, from memory
- [x] Reset · 5 min — stand up, drink water, look at something far away
- [x] Guided problem · 25 min — solve it with Claude using RESET, thinking out loud
- [x] Reset · 5 min — stand up, drink water, look at something far away
- [x] Solo problem · 25 min — 20-minute timer, alone, hints only if you ask, then review
- [x] Reset · 5 min — stand up, drink water, look at something far away
- [x] Re-solve · 20 min — 1–2 earlier problems from memory, then the bonus if time is left
- [x] Close · 5 min — write 3 sentences, log the attempts
- [x] Commit and push

How the session ran:
1. Warm-up: card 4 (#125) and #344 from memory, both alone and now done.
2. Re-solves of #26 and #643, both alone.
3. Card 8 with the NeetCode video and a step visual. #3 was tried from memory with a drawing, fixed after hint 1, then the card was typed from memory.
4. #209 solo, after hints 1–2.
5. #1004 bonus, after hints up to the full solution.

## Recap

- When the pattern applies: when we need the longest (or shortest) sublist or substring that follows a rule.
- Its key line: `best = max(best, r - l + 1)`, with the `while` inside the `for`.
- What I did when I got stuck: drew it, then asked for a hint.

## Blank moments

- What happened: went blank on the bonus (#1004) at the end of the session, and needed hints all the way to the full solution.
- RESET step that got me moving: T. The skeleton with blanks, then the full solution traced step by step in the visual.

## Next time

- Every window problem: ask "what does the window need to remember?" A set of letters (#3), a total (#209), a count of zeros (#1004).
- Longest: shrink while broken, measure after. Shortest: shrink while valid, measure before each shrink.
- In the shrink, look at the number leaving, `nums[l]`, and move `l` on every turn.
- The bonus is optional: if there's something waiting after the session, it's fine to close after the solo.

← [[Day 07]] · [[Day 09]] →
