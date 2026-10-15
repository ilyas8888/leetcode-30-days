---
type: plan
title: Pattern Triggers
tags: [plan]
---

> [!info] What you notice in a problem, turned into the pattern to try first.

Memorize this table: each row turns something you notice in a problem into the pattern to try first.

| You notice | Try first | Card |
| --- | --- | --- |
| "Have I seen this before?", pairs, counting | Hash map or set | [[Card 02 Hash map lookup\|2]], [[Card 03 Counting and grouping\|3]] |
| Sorted array, a pair, a palindrome | Two pointers | [[Card 04 Two pointers from both ends\|4]], [[Card 05 Read-write pointer\|5]] |
| Contiguous subarray or substring, "longest", "shortest", "at most k" | Sliding window | [[Card 06 Running best and fixed windows\|6]], [[Card 08 Variable window\|8]] |
| Sum of a range, "subarray sum equals k" | Prefix sums | [[Card 11 Prefix sums\|11]] |
| Brackets, nesting, undo, "most recent first" | Stack | [[Card 09 Stack\|9]] |
| Sorted input plus "find", or "smallest value that works" | Binary search | [[Card 10 Binary search\|10]] |
| Linked list: cycle, middle, n-th from the end | Fast and slow pointers | [[Card 12 Linked lists\|12]] |
| Linked list: reverse or merge | Pointer moves plus a dummy node | [[Card 12 Linked lists\|12]] |
| Tree: depth, path, compare two trees | Depth-first search (recursion) | [[Card 13 Tree depth-first search\|13]] |
| "Level by level", "fewest steps" | Breadth-first search (queue) | [[Card 14 Tree breadth-first search\|14]], [[Card 18 Graph breadth-first search\|18]] |
| Binary search tree: search, validate, k-th smallest | Use the order: left < node < right | [[Card 15 Binary search tree\|15]] |
| Grid of cells, "connected", islands | Grid DFS or BFS | [[Card 17 Grid depth-first search\|17]], [[Card 18 Graph breadth-first search\|18]] |
| "Top k", "k-th largest", take the min or max again and again | Heap | [[Card 16 Heap\|16]] |
| "All subsets", "all combinations", "all permutations" | Backtracking | [[Card 19 Backtracking\|19]] |
| "Number of ways", "min or max cost", choices that repeat | Dynamic programming | [[Card 20 Dynamic programming\|20]] |
| Overlapping ranges, meetings | Sort by start, then merge | [[Card 21 Intervals\|21]] |

The size limit is a trigger too: n ≤ 20 means backtracking is fine, n ≤ 1,000 allows O(n²), and n up to 100,000 needs O(n log n) or O(n).
