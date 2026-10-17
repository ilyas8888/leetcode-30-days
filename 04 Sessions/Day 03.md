---
type: session
day: 3
week: 1
kind: learn
focus: Grouping and frequency
cards: ["[[Card 03 Counting and grouping]]"]
status: done
date: 2026-10-17
tags: [session]
---

> [!todo] Day 03 · Grouping and frequency
> Cards: [[Card 03 Counting and grouping]] · Problems: [[0049 Group Anagrams]], [[0347 Top K Frequent Elements]], [[0205 Isomorphic Strings]]

## Plan

- Guided: [[0049 Group Anagrams]]
- Solo: [[0347 Top K Frequent Elements]]
- Bonus: [[0205 Isomorphic Strings]]
- Re-solve: [[0387 First Unique Character in a String]], [[0383 Ransom Note]] ([[0242 Valid Anagram]] in the warm-up)

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

- When the pattern applies: grouping when items share something, like the same letters; top k when the problem says "the k most frequent".
- Its key line: `groups["".join(sorted(s))].append(s)`, and `Counter(nums).most_common(k)`.
- What I did when I got stuck: typed **blank** on #387 and got the skeleton with blanks; asked "why" when my code failed.

## Blank moments

- What happened: went blank at T on the #387 re-solve, writing the loop.
- RESET step that got me moving: T, the skeleton with blanks to fill in.

## Next time

- Re-solves first: [[0387 First Unique Character in a String]] and [[0383 Ransom Note]], both rated 2.
- Warm-up from memory: #49's grouping line and #217's set loop.
- Count the loops you can't see: `Counter`, `sorted` and `most_common` all cost time.
- `=` replaces, `.append` adds. Parentheses build, brackets read.

← [[Day 02]] · [[Day 04]] →
