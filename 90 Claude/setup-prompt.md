# Claude Code task: build my LeetCode practice repo and Obsidian vault

This folder becomes three things at once:

1. **A Git repository** that I push to GitHub after every practice session.
2. **An Obsidian vault** that I open every day. Every note must be clear at a glance.
3. **Claude's memory between sessions.** I study 2 hours a day with Claude in the claude.ai app, and that Claude reads this repo from GitHub. `CLAUDE.md` and the `90 Claude/` folder let it pick up exactly where we stopped.

About me: I'm a junior developer on a 30-day plan to make LeetCode-style problems feel familiar, so I don't freeze in front of a problem in an interview. The goal is familiarity, not mastery. Language: Python.

All the content is in the appendices at the end of this file: the plan text (A), the 30 days (B), the 72 problems (C) and 21 template cards whose code is already tested (D). Use them exactly as given. Don't add, drop or rename problems, and copy card code byte for byte.

## Ground rules

- Work in the current folder. It contains only this file, and it becomes both the repo root and the vault root.
- Everything must work on Windows, macOS and Linux. Scripts use Python 3 and the standard library only.
- Ask me before creating the GitHub repository and before any push.
- One level of folders only: no subfolders inside the numbered folders.
- Never write health, personal or other sensitive information about me anywhere in the repo.
- Work through the sections below in order, and tell me in one line when each section is done.

## 1. Folder structure

Create exactly this layout:

```
.
├── 00 Home.md                 dashboard: next session, due re-solves, progress, links to everything
├── README.md                  GitHub front page
├── CLAUDE.md                  instructions Claude reads first, every session
├── 01 Plan/
│   ├── 30-Day Plan.md         all 30 days as a checklist, linked to the day notes
│   ├── Session Routine.md
│   ├── Rules.md
│   ├── RESET.md               the routine for blank moments
│   ├── Pattern Triggers.md
│   ├── Interview Phrases.md
│   ├── After Day 30.md
│   └── Roadmap.canvas         visual map of the 30 days
├── 02 Cards/                  21 notes: "Card 01 Python toolkit.md" … "Card 21 Intervals.md"
├── 03 Problems/               72 notes: "0001 Two Sum.md" … (number zero-padded to 4 digits)
├── 04 Sessions/               30 notes: "Day 01.md" … "Day 30.md"
├── 05 Mocks/                  "Mock 1.md" … "Mock 4.md" (days 14, 21, 28 and 30)
├── 06 Cheat Sheet/
│   └── Cheat Sheet.md         a skeleton I fill in on day 30
├── 90 Claude/                 Claude's memory
│   ├── STATUS.md              where we are and what comes next
│   ├── profile.md             how I learn and how to help me
│   ├── weak-spots.md
│   ├── session-summaries.md
│   └── setup-prompt.md        this file, moved here at the end
├── 99 Templates/
│   ├── Problem.md
│   ├── Session.md
│   ├── Card.md
│   └── Mock.md
├── assets/                    attachments (keep it with a .gitkeep)
├── scripts/
│   ├── check_vault.py
│   └── new_problem.py
├── .obsidian/                 minimal settings (section 7)
├── .gitignore
└── .gitattributes
```

Note names come from the appendices. A card or problem title with a character that isn't allowed in file names gets the note name given in the appendix.

## 2. Note design rules

Every note must make sense in 10 seconds.

- **Same skeleton for each note type**, with sections in the same order every time (section 4). I learn the layout once.
- **The body starts with a callout** that says what the note is and what to do with it, in one or two lines.
- **Callouts carry the key information**: `[!tip]` for the line to remember, `[!info]` for links and triggers, `[!warning]` for mistakes to avoid, `[!todo]` for what to do next. At most one callout of each kind per note.
- **Properties (YAML frontmatter) hold everything that is tracked**: status, dates, results. The body holds explanations. Use exactly the schemas in section 3, with lowercase values.
- **Short sections**: H2 headings only below the title, sentences under 25 words, no walls of text.
- **Everything is linked**: each problem links to its card and its day, each day links to its problems and cards, each card lists its problems, and Home links to every hub. No orphan notes.
- **Wikilinks between notes** (`[[0001 Two Sum]]`); normal markdown links only for external pages such as LeetCode.
- **Readable on a phone**: tables of at most 6 columns.
- **Works without plugins.** Dataview queries are welcome for live tables, but every note must still make sense without Dataview: keep a static list of links next to each query.

## 3. Properties

Problem notes:

```yaml
type: problem
number: 1
title: Two Sum
url: https://leetcode.com/problems/two-sum/
card: "[[Card 02 Hash map lookup]]"
day: 1
role: guided        # guided | solo | bonus
status: todo        # todo | learning | done
attempts: 0
last_result:        # alone | hints | solution
familiarity:        # 1-5, from the latest attempt
last_attempt:       # YYYY-MM-DD
next_review:        # YYYY-MM-DD
tags: [problem]
```

Session notes:

```yaml
type: session
day: 1
week: 1
kind: learn         # learn | review | mixed | final
focus: Hash map lookup
cards: ["[[Card 01 Python toolkit]]", "[[Card 02 Hash map lookup]]"]
status: planned     # planned | done | minimum
date:               # YYYY-MM-DD, filled in when done
tags: [session]
```

Card notes:

```yaml
type: card
card: 2
name: Hash map lookup
days: [1]
tags: [card]
```

Mock notes:

```yaml
type: mock
mock: 1
day: 14
status: planned     # planned | done
date:
tags: [mock]
```

## 4. Note skeletons

**Problem note** (`03 Problems/0001 Two Sum.md`)
1. `[!info]` callout: LeetCode link, card link, `[[Day NN]]` link, role.
2. `## Trigger`: what in the statement points to the pattern (an empty line for me to fill).
3. `## Approach`: 1 to 3 sentences in my own words.
4. `## Solution`: an empty `python` code block; my latest working version goes here.
5. `## Complexity`: `Time:` and `Space:` lines.
6. `## Mistakes and blank moments`: bullets.
7. `## Attempts`: table with Date | Day | Result | Minutes | Familiar (1–5) | Note.

**Session note** (`04 Sessions/Day 01.md`)
1. `[!todo]` callout: the day's focus, cards and problems as links. On review, mixed and final days, the day's activities instead.
2. `## Plan`: guided, solo, bonus and re-solve problems as labelled links, or the activities from appendix B on review, mixed and final days.
3. `## Routine`: the blocks of the Session Routine as `- [ ]` checkboxes on learn days, and the day's own activities as checkboxes on other days. The last box is always "Commit and push".
4. `## Recap`: three prompts: when the pattern applies, its key line, what I did when I got stuck.
5. `## Blank moments`: what happened, and which RESET step got me moving again.
6. `## Next time`.
7. Navigation at the bottom: `← [[Day 01]] · [[Day 03]] →` (skip the missing end on days 1 and 30).

**Card note** (`02 Cards/Card 02 Hash map lookup.md`)
1. `[!tip]` callout: the "Use when" line from appendix D.
2. `## Card`: the code from appendix D, byte for byte, then one quiet line: "On LeetCode, put the function inside `class Solution` and add `self` as the first parameter."
3. `## Key line`: empty, for the one line I want to remember.
4. `## Problems`: a static list of links to the problems that use this card (appendix C), then a Dataview table of the same problems with status, last result and familiarity.
5. `## My notes`.

**Mock note** (`05 Mocks/Mock 1.md`): `[!info]` callout with the day and format from appendix B, then `## Problems`, `## What went well`, `## What to fix`, `## Feedback from Claude`.

**Templates** in `99 Templates/` are these same skeletons with empty values, using `{{title}}` and `{{date}}` where they help.

## 5. Content to pre-fill

- `01 Plan/`: one note per section of appendix A. In `Pattern Triggers.md`, turn each card number into a link to its card note. `30-Day Plan.md` lists all 30 days as `- [ ]` items, one line per day, linking `[[Day NN]]` and that day's problems.
- `04 Sessions/`: all 30 day notes from appendix B, with `status: planned`.
- `03 Problems/`: all 72 problem notes from appendix C, with `status: todo`.
- `02 Cards/`: all 21 card notes from appendix D.
- `05 Mocks/`: 4 mock notes for days 14, 21, 28 and 30, with `status: planned`.
- `06 Cheat Sheet/Cheat Sheet.md`: three sections, each with a one-line prompt: "Patterns and their triggers", "Lines I always forget", "My usual mistakes".
- `00 Home.md`, in this order:
    1. `[!todo]` callout "Next session": a static line (Claude updates it after each session; start with `[[Day 01]]`) plus a Dataview query for the first day note with `status: planned`.
    2. `## Start here`: links to every note in `01 Plan/`.
    3. `## Due for re-solve`: Dataview table of problem notes whose `next_review` is today or earlier.
    4. `## Progress`: sessions done out of 30, problems by `last_result`, average familiarity per card (Dataview).
    5. `## Cards`: the 21 card notes as links.
    6. `## Weeks`: the day notes as links, one line per week.
    7. A collapsed callout `> [!info]- First-time setup` with the manual steps from section 7.
- `README.md`: what the repo is (2–3 lines), a table of the folders, how a session works (send "Day N" to Claude in claude.ai, solve on LeetCode, log the attempt in Obsidian, commit and push), and that `scripts/check_vault.py` prints progress.
- `01 Plan/Roadmap.canvas` (JSON Canvas format, jsoncanvas.org): one group per week and one for days 29–30, each holding file nodes for its day notes in a row; the review, mock and final days (7, 14, 21, 28, 30) in a different color; an edge from each group to the next. Validate the JSON. Do this last; if it fails, skip it and tell me.

## 6. Claude's memory: CLAUDE.md and 90 Claude/

`CLAUDE.md` contains:
- One paragraph on what this repo is.
- **At the start of a session, read in this order**: `90 Claude/STATUS.md`, `90 Claude/profile.md`, `90 Claude/weak-spots.md`, then the day's note in `04 Sessions/`.
- A map of the folders, one line each.
- **How to help me**: follow `01 Plan/Session Routine.md` and `01 Plan/Rules.md`. Start every problem with RESET. Give hints only when I type "hint", one rung of the hint ladder at a time. When reviewing my code, name the exact line, explain why, give only the fix, one change at a time, and let me retype it. Python unless I ask otherwise.
- **At the end of a session, update in this order**: the problem notes (new Attempts row, properties, my final solution under `## Solution`), the day note (checkboxes, recap, blank moments, `status`, `date`), `90 Claude/STATUS.md`, `90 Claude/session-summaries.md` (3 lines at most, newest first), `90 Claude/weak-spots.md`, and the "Next session" line in `00 Home.md`. Then commit with the message `day NN: <focus> (#n, #n)` and push.
- **Re-solve rule for `next_review`**: saw the solution or needed hints → the next day; solved alone → 3 days later; solved alone twice in a row → 7 days later and `status: done`.
- The property schemas from section 3.
- **Privacy**: never write health, personal or sensitive details in this repo.

`90 Claude/STATUS.md`, initial content:
- Current day: not started. Next: Day 1, hash map lookup (cards 1–2).
- Due re-solves: none. Mock interviews done: 0 of 4.
- Last updated: today's date, by Claude Code during setup.

`90 Claude/profile.md`, initial content, in the first person:
- My goal: problems feel familiar so I never freeze. Not mastery.
- Python. 2-hour sessions with Claude in claude.ai. I code on a laptop in LeetCode's editor.
- I learn well by memorizing template lines, even before I fully understand them.
- My main obstacle is going blank at the start of a problem or under pressure. RESET is the fix.
- Code reviews: exact line, why, only the fix, one change at a time, and I retype it.

`90 Claude/weak-spots.md`: a table with Card | What goes wrong | Fix that works | Last seen, and no rows yet.

`90 Claude/session-summaries.md`: a heading and a one-line example of the format, no entries yet.

## 7. Obsidian settings

Only write `.obsidian` files whose format you are sure of:
- `templates.json`: template folder `99 Templates`.
- `app.json`: attachments go to `assets`, and internal links update automatically when a note is renamed.

Don't write `core-plugins.json` or `community-plugins.json`. Put these manual steps in Home's first-time setup callout instead:
1. In Obsidian, open this folder as a vault.
2. Settings → Core plugins: turn on Templates (folder `99 Templates`) and Canvas.
3. Optional community plugins: Dataview (live tables) and Obsidian Git (commit and push from inside Obsidian).

## 8. Scripts (standard library only)

`scripts/check_vault.py`
- Reads frontmatter with a small parser (simple `key: value` lines and inline lists, no PyYAML).
- Lists every problem if a `[[link]]` points to a missing note, a required property is missing, or a value is outside its allowed set (section 3). Exit code 1 if anything is wrong, 0 if clean.
- Prints a short status: sessions done out of 30, the next planned day, problems by status and by last result, and re-solves due today or earlier.

`scripts/new_problem.py NUMBER "Title" CARD [--slug SLUG] [--day N] [--role bonus]`
- Creates `03 Problems/NNNN Title.md` from the problem skeleton, builds the LeetCode URL from the slug (derived from the title if not given), and adds the problem to its card note's static Problems list. It's for problems I add after day 30.

## 9. Git and GitHub

- `git init` with `main` as the default branch.
- `.gitignore`: `.obsidian/workspace.json`, `.obsidian/workspace-mobile.json`, `.obsidian/cache`, `.obsidian/plugins/`, `.trash/`, `.DS_Store`, `__pycache__/`, `*.pyc`, `.venv/`.
- `.gitattributes`: `* text=auto eol=lf`.
- First commit: `Set up 30-day LeetCode practice vault`.
- Then ask me for the repository name (suggest `leetcode-30-days`) and visibility (suggest private). If the GitHub CLI `gh` is installed and logged in, create the repository and push once I confirm. Otherwise, give me the exact commands to run.

## 10. Before you finish

1. Run `python scripts/check_vault.py` (or `python3`). It must pass with 0 broken links and report 72 problem notes, 30 session notes, 21 card notes and 4 mock notes.
2. Check programmatically that the code block in every card note is identical to appendix D.
3. Move this file to `90 Claude/setup-prompt.md`.
4. Show me the folder tree (top two levels) and five short lines on what I do next.

---

# Appendices

## Appendix A: plan text

Turn each section into its note in `01 Plan/`. Keep the wording.

### A1. 30-Day Plan (intro for `30-Day Plan.md`)

In 30 days you learn 16 patterns that cover most junior-level interview problems, and repeat them until starting a problem feels routine. The goal is familiarity, not mastery: you read a problem, recognize its shape, and know your first moves.

- **Patterns, not volume.** 48 core problems plus 24 optional bonus ones, grouped by pattern. Each pattern has a short Python template card you memorize line by line.
- **Repeats over new problems.** Problems come back in later sessions, and the key ones come back twice. Seeing a problem the third time is what makes it feel familiar.
- **A routine for blank moments.** RESET is how you start every problem, so it runs on autopilot under pressure.
- **Checkpoints.** Days 7, 14, 21 and 28 are review days. Days 14, 21, 28 and 30 include a mock interview with Claude as the interviewer.

**Language: Python.** It needs the fewest lines to memorize, and Counter, deque and heapq do the heavy lifting. If a company requires Java, the patterns stay the same; only the syntax changes.

### A2. Session Routine (`Session Routine.md`)

Every session runs the same nine blocks, so you never decide what to do next; you only start the next block. Send **Day N** to Claude in claude.ai to begin. Code on a laptop in LeetCode's editor, without AI autocomplete, and paste your code in the chat.

| Starts at | Block | What you do |
| --- | --- | --- |
| 0:00 | Warm-up · 10 min | Rewrite 2 template cards from memory, then name the pattern for 5 problem titles |
| 0:10 | Learn · 20 min | Claude explains today's pattern. You type its card 3 times: copy it, fill in the gaps, then from memory |
| 0:30 | Reset · 5 min | Stand up, drink water, look at something far away |
| 0:35 | Guided problem · 25 min | You solve it together with Claude using RESET, saying or typing your thinking as you go |
| 1:00 | Reset · 5 min | Same as above |
| 1:05 | Solo problem · 25 min | 20-minute timer, you solve it alone, hints only if you ask. Then Claude reviews your code |
| 1:30 | Reset · 5 min | Same as above |
| 1:35 | Re-solve · 20 min | 1–2 earlier problems from memory, then the bonus problem if time is left |
| 1:55 | Close · 5 min | Write 3 sentences: when the pattern applies, its key line, what you did when stuck. Log the attempts, then commit and push |

Review days (7, 14, 21, 28) swap the blocks for review and mock work, but keep the 2 hours and the resets.

### A3. Rules (`Rules.md`)

Seven rules keep you moving instead of stuck. Read them at the start of each session in week 1.

1. **Timer on, phone in another room.**
2. **20 minutes max on a new problem.** No progress after 10 minutes: ask for hint 1. At 20 minutes, read the solution, close it, and retype it from memory. That is part of the method, not a failure.
3. **Hint ladder.** Type **hint** for the next step: 1 a guiding question · 2 the pattern's name · 3 the approach in words · 4 a code skeleton with blanks · 5 the full solution, explained.
4. **Trace once, then run.** Walk through your code once with your small example, then press Run. Let the tests do the checking.
5. **Retype, don't paste.** When Claude reviews your code, you get the exact line and only the fix, and you retype it yourself.
6. **Everything comes back.** A problem solved with hints or the solution returns the next day. Each day note lists re-solves, and Claude adjusts them from the problem notes.
7. **Low-energy day: 30-minute minimum.** Do the warm-up and one re-solve; it counts as a full day. Missed a day? Continue with the next day number, never restart.

### A4. RESET (`RESET.md`)

RESET is five moves you make at the start of every problem, so when your mind goes blank, your hands already know what comes next.

1. **R: Reset and read.** One slow breath out, feet flat on the floor. Read the problem out loud and say: "Let me take a moment to think."
2. **E: Example.** Write one tiny input and its output by hand, like `[2,7,11,15], 9 -> [0,1]`.
3. **S: Slow solution.** Say or write the brute force, even if it is O(n²). The page is no longer blank.
4. **E: Examine the triggers.** Sorted? Pairs? Contiguous? Counting? Tree or grid? All combinations? Number of ways? Match your answer in Pattern Triggers.
5. **T: Template, then trace.** Write the pattern's card skeleton, fill in the blanks, and trace it once with your example.

In an online test with no one watching, run the same five steps as comments at the top of the editor.

### A5. Pattern Triggers (`Pattern Triggers.md`)

Memorize this table: each row turns something you notice in a problem into the pattern to try first.

| You notice | Try first | Card |
| --- | --- | --- |
| "Have I seen this before?", pairs, counting | Hash map or set | 2, 3 |
| Sorted array, a pair, a palindrome | Two pointers | 4, 5 |
| Contiguous subarray or substring, "longest", "shortest", "at most k" | Sliding window | 6, 8 |
| Sum of a range, "subarray sum equals k" | Prefix sums | 11 |
| Brackets, nesting, undo, "most recent first" | Stack | 9 |
| Sorted input plus "find", or "smallest value that works" | Binary search | 10 |
| Linked list: cycle, middle, n-th from the end | Fast and slow pointers | 12 |
| Linked list: reverse or merge | Pointer moves plus a dummy node | 12 |
| Tree: depth, path, compare two trees | Depth-first search (recursion) | 13 |
| "Level by level", "fewest steps" | Breadth-first search (queue) | 14, 18 |
| Binary search tree: search, validate, k-th smallest | Use the order: left < node < right | 15 |
| Grid of cells, "connected", islands | Grid DFS or BFS | 17, 18 |
| "Top k", "k-th largest", take the min or max again and again | Heap | 16 |
| "All subsets", "all combinations", "all permutations" | Backtracking | 19 |
| "Number of ways", "min or max cost", choices that repeat | Dynamic programming | 20 |
| Overlapping ranges, meetings | Sort by start, then merge | 21 |

The size limit is a trigger too: n ≤ 20 means backtracking is fine, n ≤ 1,000 allows O(n²), and n up to 100,000 needs O(n log n) or O(n).

### A6. Interview Phrases (`Interview Phrases.md`)

Learn these lines word for word. They fill silence, show the interviewer how you think, and buy you time when you go blank.

| Moment | Say |
| --- | --- |
| Start | "So the input is X and I need to return Y. Is that right?" |
| Clarify | "Can the input be empty? Can there be duplicates or negative numbers?" |
| Mind goes blank | "Let me take a moment and write out a small example." |
| Brute force | "The simple approach is X. That's O(n²), so let me look for something faster." |
| Pattern | "Because X, I think a hash map fits here." (or two pointers, a stack…) |
| Before coding | "My plan: first X, then Y. I'll code it now." |
| Testing | "Let me trace through it with my example." |
| Complexity | "Time is O(n) because X. Space is O(n) because Y." |
| Stuck | "I'm stuck on X. Could you give me a hint on that part?" |

Edge cases to check out loud: empty input, one element, duplicates, negative numbers, all values equal, already sorted.

### A7. After Day 30 (`After Day 30.md`)

Familiarity fades without practice, so keep three short sessions a week after day 30: one re-solve day, one new-problem day, one mock.

- **New problems:** continue pattern by pattern through a public list such as NeetCode 150 or Blind 75. Add each one with `scripts/new_problem.py`.
- **Two days before an interview:** re-solve five problems you know well, then reread your cheat sheet and Interview Phrases.
- **On the day:** solve one easy warm-up problem in the morning. If the problem is only read aloud, ask to see it written in the shared editor.


## Appendix B: the 30 days

Problems are LeetCode numbers; appendix C gives their note names. On review, mixed and final days, use the Activities column for the day note's plan and checklist. Days 29 and 30 have `week: 5` and appear as "Final days" on Home.

| Day | Week | Kind | Focus | Cards | Guided | Solo | Bonus | Re-solve | Activities |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 1 | learn | Hash map lookup | 1, 2 | #1 | #217 | #1480 |  | Also: learn RESET and Big-O basics |
| 2 | 1 | learn | Counting | 3 | #242 | #383 | #387 | #1 |  |
| 3 | 1 | learn | Grouping and frequency | 3 | #49 | #347 | #205 | #217, #242 |  |
| 4 | 1 | learn | Two pointers from both ends | 4 | #125 | #344 | #167 | #1, #49 |  |
| 5 | 1 | learn | Read/write pointer | 5 | #283 | #26 | #88 | #125, #383 |  |
| 6 | 1 | learn | Running best and fixed windows | 6 | #121 | #643 | #219 | #283, #347 |  |
| 7 | 1 | review | Review week 1 | 2, 3, 4, 5, 6, 7 |  |  |  | #242, #49, #125, #121 | Rewrite cards 2–6 from memory · pattern sprint: name the pattern for 10 problem titles · re-solves, about 12 minutes each · one stdin-style problem (card 7) · 20-minute think-aloud practice |
| 8 | 2 | learn | Variable sliding window | 8 | #3 | #209 | #1004 | #121, #26 |  |
| 9 | 2 | learn | Stack | 9 | #20 | #155 | #150 | #3, #643 |  |
| 10 | 2 | learn | Binary search | 10 | #704 | #35 | #278 | #20, #209 |  |
| 11 | 2 | learn | Binary search on the answer | 10 | #69 | #74 | #33 | #704, #155 |  |
| 12 | 2 | learn | Prefix sums | 11 | #724 | #303 | #560 | #69, #35 |  |
| 13 | 2 | learn | Linked lists: reverse and merge | 12 | #206 | #21 | #83 | #724, #283 |  |
| 14 | 2 | review | Review week 2 + mock interview 1 | 8, 9, 10, 11, 12 |  |  |  | #3, #20, #704, #206 | Rewrite cards 8–12 from memory · pattern sprint: 10 titles from weeks 1–2 · re-solves · mock interview 1 (see the mocks table) |
| 15 | 3 | learn | Linked lists: fast and slow pointers | 12 | #141 | #876 | #19 | #206, #74 |  |
| 16 | 3 | learn | Tree depth-first search | 13 | #104 | #226 | #100 | #141, #21 |  |
| 17 | 3 | learn | Trees: return a value, track a best | 13 | #543 | #112 | #110 | #104, #303 |  |
| 18 | 3 | learn | Tree breadth-first search | 14 | #102 | #637 | #111 | #543, #876 |  |
| 19 | 3 | learn | Binary search trees | 15 | #235 | #700 | #98 | #102, #226 |  |
| 20 | 3 | learn | Heaps and top k | 16 | #1046 | #703 | #215 | #235, #347 | Re-solve #347 again, this time with a heap |
| 21 | 3 | review | Review week 3 + mock interview 2 | 12, 13, 14, 15, 16 |  |  |  | #141, #104, #543, #102 | Rewrite cards 12–16 from memory · pattern sprint: 10 titles from weeks 1–3 · re-solves · mock interview 2 (see the mocks table) |
| 22 | 4 | learn | Grids: depth-first search | 17 | #200 | #733 | #695 | #1046, #112 |  |
| 23 | 4 | learn | Graphs: breadth-first search | 18 | #1971 | #994 | #997 | #200, #703 |  |
| 24 | 4 | learn | Backtracking | 19 | #78 | #46 | #17 | #1971, #235 |  |
| 25 | 4 | learn | Dynamic programming 1 | 20 | #70 | #746 | #509 | #78, #733 |  |
| 26 | 4 | learn | Dynamic programming 2 | 20 | #53 | #198 | #322 | #70, #994 |  |
| 27 | 4 | learn | Intervals | 21 | #56 | #228 | #57 | #53, #46 |  |
| 28 | 4 | review | Review week 4 + mock interview 3 | 17, 18, 19, 20, 21 |  |  |  | #200, #78, #198, #56 | Rewrite cards 17–21 from memory · pattern sprint: 15 titles from all weeks · re-solves · mock interview 3 (see the mocks table) |
| 29 | 5 | mixed | Mixed day |  |  |  |  |  | Four problems from the whole plan, picked by Claude without naming the pattern, 20 minutes each · one stdin-style problem · re-solve the two weakest problems in the problem notes |
| 30 | 5 | final | Final mock and cheat sheet |  |  |  |  |  | Mock interview 4 (see the mocks table) · write the one-page cheat sheet in your own words: patterns, triggers, and the lines you still forget |

Mock interviews (one note each in `05 Mocks/`):

| Mock | Day | Format |
| --- | --- | --- |
| 1 | 14 | One easy problem in 30 minutes, then feedback. |
| 2 | 21 | One easy and one easy-to-medium problem in 35 minutes, then feedback. |
| 3 | 28 | Two problems in 45 minutes, then feedback. |
| 4 | 30 | A full mock interview, 45 to 60 minutes, run like the real thing. |

## Appendix C: the 72 problems

URL = `https://leetcode.com/problems/<slug>/`. Use the note name exactly as written.

| # | Note name | Slug | Card | Day | Role |
| --- | --- | --- | --- | --- | --- |
| 1 | 0001 Two Sum | two-sum | 2 | 1 | guided |
| 217 | 0217 Contains Duplicate | contains-duplicate | 2 | 1 | solo |
| 1480 | 1480 Running Sum of 1d Array | running-sum-of-1d-array | 11 | 1 | bonus |
| 242 | 0242 Valid Anagram | valid-anagram | 3 | 2 | guided |
| 383 | 0383 Ransom Note | ransom-note | 3 | 2 | solo |
| 387 | 0387 First Unique Character in a String | first-unique-character-in-a-string | 3 | 2 | bonus |
| 49 | 0049 Group Anagrams | group-anagrams | 3 | 3 | guided |
| 347 | 0347 Top K Frequent Elements | top-k-frequent-elements | 3 | 3 | solo |
| 205 | 0205 Isomorphic Strings | isomorphic-strings | 2 | 3 | bonus |
| 125 | 0125 Valid Palindrome | valid-palindrome | 4 | 4 | guided |
| 344 | 0344 Reverse String | reverse-string | 4 | 4 | solo |
| 167 | 0167 Two Sum II - Input Array Is Sorted | two-sum-ii-input-array-is-sorted | 4 | 4 | bonus |
| 283 | 0283 Move Zeroes | move-zeroes | 5 | 5 | guided |
| 26 | 0026 Remove Duplicates from Sorted Array | remove-duplicates-from-sorted-array | 5 | 5 | solo |
| 88 | 0088 Merge Sorted Array | merge-sorted-array | 5 | 5 | bonus |
| 121 | 0121 Best Time to Buy and Sell Stock | best-time-to-buy-and-sell-stock | 6 | 6 | guided |
| 643 | 0643 Maximum Average Subarray I | maximum-average-subarray-i | 6 | 6 | solo |
| 219 | 0219 Contains Duplicate II | contains-duplicate-ii | 6 | 6 | bonus |
| 3 | 0003 Longest Substring Without Repeating Characters | longest-substring-without-repeating-characters | 8 | 8 | guided |
| 209 | 0209 Minimum Size Subarray Sum | minimum-size-subarray-sum | 8 | 8 | solo |
| 1004 | 1004 Max Consecutive Ones III | max-consecutive-ones-iii | 8 | 8 | bonus |
| 20 | 0020 Valid Parentheses | valid-parentheses | 9 | 9 | guided |
| 155 | 0155 Min Stack | min-stack | 9 | 9 | solo |
| 150 | 0150 Evaluate Reverse Polish Notation | evaluate-reverse-polish-notation | 9 | 9 | bonus |
| 704 | 0704 Binary Search | binary-search | 10 | 10 | guided |
| 35 | 0035 Search Insert Position | search-insert-position | 10 | 10 | solo |
| 278 | 0278 First Bad Version | first-bad-version | 10 | 10 | bonus |
| 69 | 0069 Sqrt(x) | sqrtx | 10 | 11 | guided |
| 74 | 0074 Search a 2D Matrix | search-a-2d-matrix | 10 | 11 | solo |
| 33 | 0033 Search in Rotated Sorted Array | search-in-rotated-sorted-array | 10 | 11 | bonus |
| 724 | 0724 Find Pivot Index | find-pivot-index | 11 | 12 | guided |
| 303 | 0303 Range Sum Query - Immutable | range-sum-query-immutable | 11 | 12 | solo |
| 560 | 0560 Subarray Sum Equals K | subarray-sum-equals-k | 11 | 12 | bonus |
| 206 | 0206 Reverse Linked List | reverse-linked-list | 12 | 13 | guided |
| 21 | 0021 Merge Two Sorted Lists | merge-two-sorted-lists | 12 | 13 | solo |
| 83 | 0083 Remove Duplicates from Sorted List | remove-duplicates-from-sorted-list | 12 | 13 | bonus |
| 141 | 0141 Linked List Cycle | linked-list-cycle | 12 | 15 | guided |
| 876 | 0876 Middle of the Linked List | middle-of-the-linked-list | 12 | 15 | solo |
| 19 | 0019 Remove Nth Node From End of List | remove-nth-node-from-end-of-list | 12 | 15 | bonus |
| 104 | 0104 Maximum Depth of Binary Tree | maximum-depth-of-binary-tree | 13 | 16 | guided |
| 226 | 0226 Invert Binary Tree | invert-binary-tree | 13 | 16 | solo |
| 100 | 0100 Same Tree | same-tree | 13 | 16 | bonus |
| 543 | 0543 Diameter of Binary Tree | diameter-of-binary-tree | 13 | 17 | guided |
| 112 | 0112 Path Sum | path-sum | 13 | 17 | solo |
| 110 | 0110 Balanced Binary Tree | balanced-binary-tree | 13 | 17 | bonus |
| 102 | 0102 Binary Tree Level Order Traversal | binary-tree-level-order-traversal | 14 | 18 | guided |
| 637 | 0637 Average of Levels in Binary Tree | average-of-levels-in-binary-tree | 14 | 18 | solo |
| 111 | 0111 Minimum Depth of Binary Tree | minimum-depth-of-binary-tree | 14 | 18 | bonus |
| 235 | 0235 Lowest Common Ancestor of a Binary Search Tree | lowest-common-ancestor-of-a-binary-search-tree | 15 | 19 | guided |
| 700 | 0700 Search in a Binary Search Tree | search-in-a-binary-search-tree | 15 | 19 | solo |
| 98 | 0098 Validate Binary Search Tree | validate-binary-search-tree | 15 | 19 | bonus |
| 1046 | 1046 Last Stone Weight | last-stone-weight | 16 | 20 | guided |
| 703 | 0703 Kth Largest Element in a Stream | kth-largest-element-in-a-stream | 16 | 20 | solo |
| 215 | 0215 Kth Largest Element in an Array | kth-largest-element-in-an-array | 16 | 20 | bonus |
| 200 | 0200 Number of Islands | number-of-islands | 17 | 22 | guided |
| 733 | 0733 Flood Fill | flood-fill | 17 | 22 | solo |
| 695 | 0695 Max Area of Island | max-area-of-island | 17 | 22 | bonus |
| 1971 | 1971 Find if Path Exists in Graph | find-if-path-exists-in-graph | 18 | 23 | guided |
| 994 | 0994 Rotting Oranges | rotting-oranges | 18 | 23 | solo |
| 997 | 0997 Find the Town Judge | find-the-town-judge | 3 | 23 | bonus |
| 78 | 0078 Subsets | subsets | 19 | 24 | guided |
| 46 | 0046 Permutations | permutations | 19 | 24 | solo |
| 17 | 0017 Letter Combinations of a Phone Number | letter-combinations-of-a-phone-number | 19 | 24 | bonus |
| 70 | 0070 Climbing Stairs | climbing-stairs | 20 | 25 | guided |
| 746 | 0746 Min Cost Climbing Stairs | min-cost-climbing-stairs | 20 | 25 | solo |
| 509 | 0509 Fibonacci Number | fibonacci-number | 20 | 25 | bonus |
| 53 | 0053 Maximum Subarray | maximum-subarray | 20 | 26 | guided |
| 198 | 0198 House Robber | house-robber | 20 | 26 | solo |
| 322 | 0322 Coin Change | coin-change | 20 | 26 | bonus |
| 56 | 0056 Merge Intervals | merge-intervals | 21 | 27 | guided |
| 228 | 0228 Summary Ranges | summary-ranges | 21 | 27 | solo |
| 57 | 0057 Insert Interval | insert-interval | 21 | 27 | bonus |

## Appendix D: the 21 template cards

Each card was run against LeetCode's own examples and passed. Copy each code block into its card note byte for byte.

### D1. Python toolkit

- Note name: `Card 01 Python toolkit`
- Days: 1
- Use when: The built-ins every card below relies on.

```python
from collections import Counter, defaultdict, deque
import heapq

seen = set()                 # x in seen -> instant lookup
pos = {}                     # pos.get(x, -1) -> -1 if x is missing
count = Counter("banana")    # Counter({'a': 3, 'n': 2, 'b': 1})
groups = defaultdict(list)   # groups[key].append(x), no KeyError
q = deque([1, 2])            # q.append(3), then q.popleft() -> 1
stack = [1, 2]               # stack.append(3), then stack.pop() -> 3

for i, x in enumerate(["a", "b"]):   # i = 0, 1 and x = "a", "b"
    pass

sorted([("ana", 30), ("bo", 25)], key=lambda p: p[1])  # sort by 2nd item
float("inf")                 # start value when looking for a minimum
```

### D2. Hash map lookup

- Note name: `Card 02 Hash map lookup`
- Days: 1
- Use when: Know instantly whether you have seen a value before. Solves #1 Two Sum.

```python
def two_sum(nums, target):
    seen = {}                          # value -> its index
    for i, x in enumerate(nums):
        if target - x in seen:         # is my partner already here?
            return [seen[target - x], i]
        seen[x] = i
```

### D3. Counting and grouping

- Note name: `Card 03 Counting and grouping`
- Days: 2, 3
- Use when: Compare letter counts, or group items that share a key. Solves #242 and #49.

```python
from collections import Counter, defaultdict

def is_anagram(s, t):
    return Counter(s) == Counter(t)

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = "".join(sorted(w))       # same letters -> same key
        groups[key].append(w)
    return list(groups.values())
```

### D4. Two pointers from both ends

- Note name: `Card 04 Two pointers from both ends`
- Days: 4
- Use when: Sorted array or palindrome: start at both ends and move inward. Solves #125.

```python
def is_palindrome(s):
    l, r = 0, len(s) - 1
    while l < r:
        if not s[l].isalnum():
            l += 1                     # skip a non-letter on the left
        elif not s[r].isalnum():
            r -= 1                     # skip a non-letter on the right
        elif s[l].lower() != s[r].lower():
            return False
        else:
            l += 1                     # both match: move inward
            r -= 1
    return True
```

### D5. Read/write pointer

- Note name: `Card 05 Read-write pointer`
- Days: 5
- Use when: Keep, remove or move items in place, without a second array. Solves #283.

```python
def move_zeroes(nums):
    w = 0                              # next slot to write into
    for r in range(len(nums)):         # r reads every item
        if nums[r] != 0:               # keep this one
            nums[w], nums[r] = nums[r], nums[w]
            w += 1
```

### D6. Running best and fixed windows

- Note name: `Card 06 Running best and fixed windows`
- Days: 6
- Use when: Track the best value so far in one pass, or slide a window of fixed size k. Solves #121; the window is the core of #643.

```python
def max_profit(prices):
    lowest, best = float("inf"), 0
    for p in prices:
        lowest = min(lowest, p)        # cheapest day to buy so far
        best = max(best, p - lowest)   # what if I sell today?
    return best

# Fixed window of size k: add the new right item, drop the old left one
window = sum(nums[:k])
for r in range(k, len(nums)):
    window += nums[r] - nums[r - k]
```

### D7. Reading input

- Note name: `Card 07 Reading input`
- Days: 7
- Use when: For HackerRank-style tests, where you read the input yourself and print the answer.

```python
import sys

data = sys.stdin.read().split()        # every value, whatever the layout
n = int(data[0])
nums = list(map(int, data[1:1 + n]))
print(sum(nums))                       # print only the answer

# Line by line instead:
# n = int(input())
# nums = list(map(int, input().split()))
```

### D8. Variable window

- Note name: `Card 08 Variable window`
- Days: 8
- Use when: The longest or shortest contiguous part that follows a rule. Solves #3.

```python
def length_of_longest_substring(s):
    seen = set()                       # what is inside the window
    l = best = 0
    for r, ch in enumerate(s):         # 1. grow on the right
        while ch in seen:              # 2. broken? shrink from the left
            seen.remove(s[l])
            l += 1
        seen.add(ch)
        best = max(best, r - l + 1)    # 3. valid again: measure it
    return best

# "Shortest" problems: update best inside the while loop instead.
```

### D9. Stack

- Note name: `Card 09 Stack`
- Days: 9
- Use when: Matching pairs, nesting, the most recent item first. Solves #20.

```python
def is_valid(s):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for ch in s:
        if ch in pairs:                # closing bracket
            if not stack or stack.pop() != pairs[ch]:
                return False
        else:                          # opening bracket
            stack.append(ch)
    return not stack                   # True only if nothing is left open
```

### D10. Binary search

- Note name: `Card 10 Binary search`
- Days: 10, 11
- Use when: Sorted input, or the smallest or largest value that works. Solves #704 and #69.

```python
def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[m] < target:
            l = m + 1                  # answer is on the right
        else:
            r = m - 1                  # answer is on the left
    return -1                          # here, l = where target would go

def my_sqrt(x):                        # binary search on the answer
    l, r = 0, x
    while l <= r:
        m = (l + r) // 2
        if m * m <= x:
            l = m + 1                  # m works: try bigger
        else:
            r = m - 1                  # m too big: go smaller
    return r                           # the last value that worked
```

### D11. Prefix sums

- Note name: `Card 11 Prefix sums`
- Days: 12
- Use when: Sums of ranges, or counting subarrays with a given sum. Solves #724 and #560.

```python
prefix = [0]
for x in nums:
    prefix.append(prefix[-1] + x)
# sum of nums[i..j] = prefix[j + 1] - prefix[i]

def pivot_index(nums):
    total, left = sum(nums), 0
    for i, x in enumerate(nums):
        if left == total - left - x:   # left side == right side
            return i
        left += x
    return -1

def subarray_sum(nums, k):
    seen = {0: 1}                      # prefix sum -> times seen
    total = count = 0
    for x in nums:
        total += x
        count += seen.get(total - k, 0)   # earlier prefixes that leave k
        seen[total] = seen.get(total, 0) + 1
    return count
```

### D12. Linked lists

- Note name: `Card 12 Linked lists`
- Days: 13, 15
- Use when: Reverse a list, build one behind a dummy head, detect a cycle. Solves #206 and #141.

```python
def reverse_list(head):
    prev, cur = None, head
    while cur:
        nxt = cur.next                 # 1. save
        cur.next = prev                # 2. flip
        prev = cur                     # 3. move prev
        cur = nxt                      # 4. move cur
    return prev

# Dummy node: a fake head, so the first real node is not a special case
dummy = tail = ListNode()
# ...each time: tail.next = node, then tail = tail.next
# at the end: return dummy.next

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:          # slow moves 1, fast moves 2
        slow, fast = slow.next, fast.next.next
        if slow is fast:
            return True
    return False
```

### D13. Tree depth-first search

- Note name: `Card 13 Tree depth-first search`
- Days: 16, 17
- Use when: Depth, paths, or comparing subtrees: ask the children, then combine. Solves #104 and #543.

```python
def max_depth(root):
    if not root:                       # 1. base case
        return 0
    left = max_depth(root.left)        # 2. ask both children
    right = max_depth(root.right)
    return 1 + max(left, right)        # 3. combine

def diameter_of_binary_tree(root):
    best = 0
    def height(node):
        nonlocal best
        if not node:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)        # longest path through this node
        return 1 + max(l, r)
    height(root)
    return best
```

### D14. Tree breadth-first search

- Note name: `Card 14 Tree breadth-first search`
- Days: 18
- Use when: Anything level by level. Solves #102.

```python
from collections import deque

def level_order(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        level = []
        for _ in range(len(q)):        # exactly one level
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```

### D15. Binary search tree

- Note name: `Card 15 Binary search tree`
- Days: 19
- Use when: Use the order left < node < right to skip half the tree. Solves #235 and #98.

```python
def lowest_common_ancestor(root, p, q):
    node = root
    while node:
        if p.val < node.val and q.val < node.val:
            node = node.left           # both are on the left
        elif p.val > node.val and q.val > node.val:
            node = node.right          # both are on the right
        else:
            return node                # they split here

def is_valid_bst(root):
    def check(node, low, high):
        if not node:
            return True
        if not (low < node.val < high):
            return False
        return (check(node.left, low, node.val) and
                check(node.right, node.val, high))
    return check(root, float("-inf"), float("inf"))
```

### D16. Heap

- Note name: `Card 16 Heap`
- Days: 20
- Use when: Top k, k-th largest, or taking the biggest or smallest again and again. Solves #1046 and #215.

```python
import heapq

def last_stone_weight(stones):
    heap = [-s for s in stones]        # negate: heapq is a min-heap
    heapq.heapify(heap)
    while len(heap) > 1:
        a = -heapq.heappop(heap)       # heaviest
        b = -heapq.heappop(heap)       # second heaviest
        if a != b:
            heapq.heappush(heap, -(a - b))
    return -heap[0] if heap else 0

def find_kth_largest(nums, k):
    heap = []                          # the k largest so far
    for x in nums:
        heapq.heappush(heap, x)
        if len(heap) > k:
            heapq.heappop(heap)        # drop the smallest
    return heap[0]
```

### D17. Grid depth-first search

- Note name: `Card 17 Grid depth-first search`
- Days: 22
- Use when: Connected regions in a grid: visit, mark, spread in four directions. Solves #200.

```python
def num_islands(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(r, c):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != "1":
            return                     # off the grid, water, or seen
        grid[r][c] = "0"               # mark as seen
        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    islands = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands += 1
                dfs(r, c)              # sink the whole island
    return islands
```

### D18. Graph breadth-first search

- Note name: `Card 18 Graph breadth-first search`
- Days: 23
- Use when: Can I reach it, and in how few steps? Build an adjacency list, then run BFS. Solves #1971.

```python
from collections import defaultdict, deque

def valid_path(n, edges, source, destination):
    graph = defaultdict(list)          # node -> its neighbours
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen, q = {source}, deque([source])
    while q:
        node = q.popleft()
        if node == destination:
            return True
        for nxt in graph[node]:
            if nxt not in seen:
                seen.add(nxt)          # mark when you add, not when you pop
                q.append(nxt)
    return False
```

### D19. Backtracking

- Note name: `Card 19 Backtracking`
- Days: 24
- Use when: Generate every subset, combination or permutation. Solves #78.

```python
def subsets(nums):
    res, path = [], []
    def backtrack(start):
        res.append(path[:])            # save a COPY of the current choice
        for i in range(start, len(nums)):
            path.append(nums[i])       # 1. choose
            backtrack(i + 1)           # 2. explore
            path.pop()                 # 3. undo
    backtrack(0)
    return res

# Every backtracking problem: choose, explore, undo. Only the rules change.
```

### D20. Dynamic programming

- Note name: `Card 20 Dynamic programming`
- Days: 25, 26
- Use when: Number of ways, minimum or maximum cost, choices that repeat. Solves #70, #53 and #322.

```python
# Five questions: 1) what does dp[i] mean? 2) how does it use smaller i?
# 3) base case? 4) loop order? 5) where is the answer?

def climb_stairs(n):
    prev, cur = 1, 1                   # ways to reach step 0 and step 1
    for _ in range(n - 1):
        prev, cur = cur, prev + cur
    return cur

def max_sub_array(nums):               # Kadane's algorithm
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)          # extend the run, or restart here
        best = max(best, cur)
    return best

def coin_change(coins, amount):
    dp = [0] + [float("inf")] * amount    # dp[a] = fewest coins to make a
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a:
                dp[a] = min(dp[a], dp[a - c] + 1)
    return dp[amount] if dp[amount] != float("inf") else -1
```

### D21. Intervals

- Note name: `Card 21 Intervals`
- Days: 27
- Use when: Overlapping ranges: sort by start, then merge into the last one. Solves #56.

```python
def merge(intervals):
    intervals.sort(key=lambda x: x[0])     # sort by start
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        if start <= merged[-1][1]:         # overlaps the last one
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged
```
