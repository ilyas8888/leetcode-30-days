---
type: session
day: 6
week: 1
kind: learn
focus: Running best and fixed windows
cards: ["[[Card 06 Running best and fixed windows]]"]
status: done
date: 2026-10-21
tags: [session]
---

> [!todo] Day 06 · Running best and fixed windows
> Cards: [[Card 06 Running best and fixed windows]] · Problems: [[0121 Best Time to Buy and Sell Stock]], [[0643 Maximum Average Subarray I]], [[0219 Contains Duplicate II]]

## Plan

- Guided: [[0121 Best Time to Buy and Sell Stock]]
- Solo: [[0643 Maximum Average Subarray I]]
- Bonus: [[0219 Contains Duplicate II]]
- Re-solve:
  - In the warm-up: card 5 from memory covers [[0283 Move Zeroes]], and [[0347 Top K Frequent Elements]] gets typed from memory like a card.
  - First, before the new card: [[0026 Remove Duplicates from Sorted Array]] and [[0049 Group Anagrams]].
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
1. Warm-up: card 5 (#283) and #347 from memory, then 5 titles to name.
2. Re-solves of #26 and #49.
3. The card with two videos and a step visual. #121 was tried alone after the video, then the card's version.
4. Typings 2 and 3, and the window drawn in Excalidraw.
5. #643 solo.
6. #219 bonus, solved alone.

## Recap

- When the pattern applies: when we're looking for the biggest sum or average of k items in a row (and the best profit in one pass).
- Its key line: `window += nums[r] - nums[r - k]`.
- What I did when I got stuck: drew it in Excalidraw; if it was still wrong, I wrote conditions for the special cases; then asked for a hint.

## Blank moments

- What happened: no blank. Stuck on:
  - #121's first try: separate min and max;
  - the window's positions: where it starts, which number leaves, carrying the total;
  - #643's `best = 0.00`.
- RESET step that got me moving: T, drawing the steps in Excalidraw and checking them against the visual, then tracing a failing input.

## Next time

- Before adding special-case conditions, trace the failing input. On #643 the special cases were patching `best = 0.00`, and one of them was wrong.
- A running best starts from the first real value when results can be negative (#643). 0 only works when the answer can't go below 0 (#121).
- Don't name variables `max`, `min` or `sum`: they hide Python's functions.
- [[Day 07]] is a review day: cards 2–6 from memory, a 10-title pattern sprint, re-solves of about 12 minutes each, one stdin-style problem, and think-aloud practice.

← [[Day 05]] · [[Day 07]] →
