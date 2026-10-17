# Weak spots

| Card | What goes wrong | Fix that works | Last seen |
| --- | --- | --- | --- |
| [[Card 02 Hash map lookup]] | Swaps key and value: `seen[i] = x` (Day 1), a comment calling the letter the value (Day 2), `groups["eat"].append("aet")` in a drill (Day 3) | Rule: inside the brackets is the key, after `=` is the stored value. The real solutions were right on Days 2 and 3 | 2026-10-17 |
| Positions, values and keys | Uses one where another belongs: `pairs[count]` (a count as a position), `Counter(s)[i]` (a position as a key), looping over a Counter instead of the string | Ask "is this a position, a value or a key?" before indexing | 2026-10-17 |
| Python syntax | `Counter[s]`, `count(ch, 0)` without `.get`, `List` with a capital L, `=` where `.append` was needed | Parentheses build, brackets read; `.get` reads with a fallback; `=` replaces, `.append` adds | 2026-10-17 |
| [[RESET]] (every problem) | Day 1: skipped RESET and looked up a video when stuck | Days 2–3: writes R, E and S alone on every problem. When blank at T, the skeleton with blanks gets them moving | 2026-10-17 |
| Recall | Multi-step solutions (#383, #387) fade after a day; one-liners (#242, #49) stick | Re-solves first in the session, again the next day; skeletons with blanks | 2026-10-17 |
| Big-O time | Labelled a loop inside a loop O(n log n) (#383, #1480); missed the hidden sort in #49 | Got O(n²) right on Day 3 (#387) and caught the sort in #347. Rule: count the loops you can't see (`Counter`, `sorted`, `most_common`) | 2026-10-17 |
| Big-O space | O(n) for letter counts (#242, #383); O(k) for #347's counter | Space is the number of different keys: letters are capped at 26, so O(1); numbers aren't, so O(n) | 2026-10-17 |
| Trigger step | Day 2: named a technique or a data-structure property ("sorting", "a hash map is sorted") instead of something in the problem | Day 3: named "count" correctly and went straight to labels on #49. Read the trigger off the E-step examples | 2026-10-17 |
