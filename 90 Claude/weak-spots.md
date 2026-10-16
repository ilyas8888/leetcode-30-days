# Weak spots

| Card | What goes wrong | Fix that works | Last seen |
| --- | --- | --- | --- |
| [[Card 02 Hash map lookup]] | Swaps key and value: `seen[i] = x` on Day 1; a comment calling the letter the value on Day 2 | Rule: inside the brackets is the key, after `=` is the stored value. The code was right on Day 2 | 2026-10-16 |
| [[RESET]] (every problem) | Day 1: skipped RESET and looked up a video when stuck | Claude leads RESET one step at a time on the guided problem; the five-line comment template on solos. Day 2: wrote R, E, S and the trigger alone three times, and typed "stuck" instead of opening a video | 2026-10-16 |
| Big-O time | Labels a loop inside a loop O(n log n) (#383, #1480) | A loop inside a loop over the same list is O(n²); O(n log n) is the cost of sorting | 2026-10-16 |
| Big-O space | Says O(n) space for letter counts (#242, #383) | Space is the number of different keys: at most 26 lowercase letters, so O(1) | 2026-10-16 |
| Trigger step | Names a technique or a data-structure property ("sorting", "a hash map is sorted") instead of something in the problem | Read the trigger off the E-step examples: "only one a" → counting | 2026-10-16 |
