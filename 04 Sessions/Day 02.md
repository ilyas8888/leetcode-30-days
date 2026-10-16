---
type: session
day: 2
week: 1
kind: learn
focus: Counting
cards: ["[[Card 03 Counting and grouping]]"]
status: done
date: 2026-10-16
tags: [session]
---

> [!todo] Day 02 · Counting
> Cards: [[Card 03 Counting and grouping]] · Problems: [[0242 Valid Anagram]], [[0383 Ransom Note]], [[0387 First Unique Character in a String]]

## Plan

- Guided: [[0242 Valid Anagram]]
- Solo: [[0383 Ransom Note]]
- Bonus: [[0387 First Unique Character in a String]]
- Re-solve: [[0001 Two Sum]], [[1480 Running Sum of 1d Array]]

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

## Recap

- When the pattern applies: when the problem is about how many times each letter appears ("the same count of each character").
- Its key line: `count[ch] = count.get(ch, 0) + 1`, or `Counter(s)`.
- What I did when I got stuck: typed "stuck" and got a hint instead of looking for a video.

## Blank moments

- What happened: not recalled at the close.
- RESET step that got me moving: wrote R, E, S and the trigger alone for #383, #1480 and #387.

## Next time

- Re-solve [[0387 First Unique Character in a String]] and [[0383 Ransom Note]] first. Card 3's `is_anagram` goes in the warm-up, which covers [[0242 Valid Anagram]].
- A loop inside a loop is O(n²); O(n log n) is the cost of sorting.
- Space for letter counts is O(1): at most 26 keys.
- Triggers come from the problem; my E-step examples often show them.

← [[Day 01]] · [[Day 03]] →
