# Session summaries

Newest first. One line each, format: `Day NN — focus — what clicked / what to revisit`.

<!-- Example: Day 01 — hash map lookup — solved Two Sum alone; revisit when to store index vs value -->

Day 08 — variable sliding window — #125, #344 (now done), #26 and #643 all alone; #3 from the video's theory + a drawing, fixed after hint 1 (missing add, `s[0]` vs `s[l]`); #209 solo after hints 1–2 (set → running total, measure before shrink); #1004 bonus needed the full solution (shrink checked the incoming number → infinite loop) / revisit: what the window remembers, longest vs shortest, the shrink loop moving l every turn

Day 07 — review week 1 — cards 2–6 from memory (only #643's `best = nums[0]` wrong); #121, #387, #383 alone (#387 and #383 now done), #26's return after a guided hint; pattern sprint 4/10 plus 2 half right (counting and set problems missed); card 7 with Sales by Match (own sort-and-pair design, then counting); think-aloud on #389 with good edge cases but a Counter inside the loop / revisit: counting and set triggers, Counter once before the loop, brute force and trace in the think-aloud

Day 06 — running best and fixed windows — #283 and #347 from memory (#347 alone at last), #49 alone, #26 counted but forgot to write into nums; #121 tried alone with separate min/max (null = −inf), then the card; window positions fixed with a drawing (start at k, drop r − k, carry the total); #643 `best = 0.00` patched with special cases, fixed to `best = avg`; #219 alone / revisit: running best's start value, trace before adding special cases, window positions

Day 05 — read/write pointer — #125 (card 4) from memory, #344 the card's way, #1/#1480/#242 alone (now done); #49 and #347 needed hints again (#347: forgot pair unpacking, third day); #283 tried alone in Excalidraw → time limit, fixed with the card's for/w shape; #26 own design, return fixed to w + 1; asked for a video and a step visual for each new card / revisit: read `->` for the return, what a pointer means at the end, "sorted" as a trigger

Day 04 — two pointers from both ends — re-solves first: #387 and #383 alone (familiarity 2 → 4), #217 alone (done), #49 regressed (word as the key); card 4 typed 3 times; #125 guided with a 6-turn trace; #344 after hint 1 (mirror swap, stop at the middle); #347 misread as "has duplicates", fixed after hint 1 / revisit: triggers come from the problem's words, one partner per position = one loop, a Counter of numbers = O(n) space

Day 03 — grouping and frequency — anagram one-liner from memory; #387 re-solve needed hint 1 and the skeleton after a blank; built #49 in one line; #347 with most_common after an index error; #383 re-solved a new way after hint 1; #205 bonus unfinished / revisit: hidden loops in Big-O, positions vs values vs keys, multi-step solutions fade after a day

Day 02 — counting — #1 from memory (~6 min); built #242 from own counting loop; #383 after the approach in words; #1480 re-solved with every RESET step alone; #387 stopped at T, saw solution / revisit: loop in a loop = O(n²), letter counts = O(1) space, triggers come from the problem

Day 01 — hash map lookup — learned card 2 (fixed a swapped `seen[x] = i`), wrote #1 from memory, solved #217 alone in ~6 min then switched to a set, learned #1480 from a video; familiarity 2/5/3 / revisit: RESET step by step, re-solve #1 and #1480
