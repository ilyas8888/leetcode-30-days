# Weak spots

| Card | What goes wrong | Fix that works | Last seen |
| --- | --- | --- | --- |
| [[Card 02 Hash map lookup]] | Swapped key and value: wrote `seen[i] = x` | Read `seen[x] = i` as "value x was seen at position i" | 2026-10-15 |
| [[RESET]] (every problem) | Skips RESET; when stuck, looks up a video | To try: Claude prompts each RESET step; type **hint** before any video | 2026-10-15 |
