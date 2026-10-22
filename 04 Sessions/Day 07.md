---
type: session
day: 7
week: 1
kind: review
focus: Review week 1
cards: ["[[Card 02 Hash map lookup]]", "[[Card 03 Counting and grouping]]", "[[Card 04 Two pointers from both ends]]", "[[Card 05 Read-write pointer]]", "[[Card 06 Running best and fixed windows]]", "[[Card 07 Reading input]]"]
status: done
date: 2026-10-22
tags: [session]
---

> [!todo] Day 07 · Review week 1
> Rewrite cards 2–6 from memory; pattern sprint: name the pattern for 10 problem titles; re-solves, about 12 minutes each; one stdin-style problem (card 7); 20-minute think-aloud practice

## Plan

- Rewrite cards 2–6 from memory (card 6 covers [[0121 Best Time to Buy and Sell Stock]])
- pattern sprint: name the pattern for 10 problem titles
- re-solves, about 12 minutes each: [[0026 Remove Duplicates from Sorted Array]], [[0643 Maximum Average Subarray I]], [[0387 First Unique Character in a String]], [[0383 Ransom Note]]; [[0205 Isomorphic Strings]] if time is left
- one stdin-style problem (card 7)
- 20-minute think-aloud practice

## Routine

- [x] Rewrite cards 2–6 from memory
- [x] pattern sprint: name the pattern for 10 problem titles
- [x] re-solves, about 12 minutes each
- [x] one stdin-style problem (card 7)
- [x] 20-minute think-aloud practice
- [x] Commit and push

How the review went:
- **Cards 2–6 from memory:** all correct, except card 6's window used on #643 (`best = nums[0]`, fixed to `best = window`). Card 6's running best counted as the #121 re-solve: alone, 5.
- **Pattern sprint:** right on 2, 3, 6 and 8, with 1 (seen instead of two pointers) and 7 (window instead of running best) half right. Missed 4, 5, 9 and 10: the counting and set problems.
- **Re-solves:**
  - #26: the return value after a guided hint.
  - #387 and #383: alone, now done.
- **Card 7:** watched the Neso Academy video and tried `input().split()` in the Python shell.
- **Stdin problem:** Sales by Match. Own sort-and-pair design (three code fixes), then the counting version alone.
- **Think-aloud:** #389 Find the Difference, with start, example, edge cases and pattern all said. The `Counter` was rebuilt inside the loop, which makes it O(n²).

## Recap

- When the pattern applies (card 7): when you read the input yourself, split it and turn it into a list of numbers.
- Its key line: `nums = list(map(int, input().split()))`. In a test, use no message inside `input()`.
- What I did when I got stuck: drew it in Excalidraw, then asked for a hint if I was still stuck.

## Blank moments

- What happened: no blank.
- RESET step that got me moving: T, drawing the steps in Excalidraw (Sales by Match), then a trace of a failing input (#643's `k == len(nums)`).

## Next time

- Counting and set problems need another round: Find the Difference, Jewels and Stones, Word Pattern and Sort Characters By Frequency all slipped in the sprint.
- Build a `Counter` once, before the loop. Inside the loop it's a full pass every turn.
- Think-aloud: also say the brute force, and trace your example before giving the complexity.
- In a test, call `input()` with no message, and import `Counter` outside LeetCode.

← [[Day 06]] · [[Day 08]] →
