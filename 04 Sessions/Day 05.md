---
type: session
day: 5
week: 1
kind: learn
focus: Read/write pointer
cards: ["[[Card 05 Read-write pointer]]"]
status: done
date: 2026-10-20
tags: [session]
---

> [!todo] Day 05 · Read/write pointer
> Cards: [[Card 05 Read-write pointer]] · Problems: [[0283 Move Zeroes]], [[0026 Remove Duplicates from Sorted Array]], [[0088 Merge Sorted Array]]

## Plan

- Guided: [[0283 Move Zeroes]]
- Solo: [[0026 Remove Duplicates from Sorted Array]]
- Bonus: [[0088 Merge Sorted Array]]
- Re-solve: [[0344 Reverse String]] (the card's way), [[0347 Top K Frequent Elements]] and [[0049 Group Anagrams]] first, before the new card. Card 4 from memory in the warm-up covers [[0125 Valid Palindrome]]. [[0001 Two Sum]], [[1480 Running Sum of 1d Array]] and [[0242 Valid Anagram]] if time is left

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

How the session actually ran:
1. Warm-up: card 4 from memory (#125) and #49, then 5 titles to name.
2. Re-solves before the new card: #344 (the card's way) and #347.
3. Learn: the card, plus the [NeetCode video](https://www.youtube.com/watch?v=aayNRwUN3Do).
4. #283, tried alone in Excalidraw first, then reviewed.
5. #26 solo.
6. #1, #1480 and #242 at the end.

Typing card 5 with blanks and from memory moved to Day 06's warm-up.

## Recap

- When the pattern applies: when we have to move elements to the far right (zeros to the end, duplicates out of the way), in place.
- Its key line: `if nums[r] != 0:` (for duplicates, `if nums[r] != nums[w]:`).
- What I did when I got stuck: asked for a hint, then designed the algorithm in Excalidraw.

## Blank moments

- What happened: no blank. Got stuck on:
  - #49: a seen set crept into grouping;
  - #347: forgot that a pair unpacks itself, `for num, times in pairs:`;
  - #26: the return value.
- RESET step that got me moving: T. Drawing the steps in Excalidraw, then the skeleton with blanks (#347), and tracing a tiny example to count (#26).

## Next time

- Warm-up from memory: card 5 (that's #283) and #347's lines, typed like a card. #347 has slipped three days running.
- Re-solves first: [[0026 Remove Duplicates from Sorted Array]] (what does `w` mean at the end?) and [[0049 Group Anagrams]] (no `if`, no set).
- Read `->` in the signature before coding: `-> None` means change in place and return nothing; `-> int` means return a number too.
- "Sorted" is a trigger word on its own.

← [[Day 04]] · [[Day 06]] →
