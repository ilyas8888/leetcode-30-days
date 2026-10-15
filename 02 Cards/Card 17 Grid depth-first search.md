---
type: card
card: 17
name: Grid depth-first search
days: [22]
tags: [card]
---

> [!tip] Use when
> Connected regions in a grid: visit, mark, spread in four directions. Solves #200.

## Card

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

On LeetCode, put the function inside `class Solution` and add `self` as the first parameter.

## Key line

## Problems

- [[0200 Number of Islands]]
- [[0733 Flood Fill]]
- [[0695 Max Area of Island]]

```dataview
TABLE status, last_result, familiarity
FROM "03 Problems"
WHERE contains(card, this.file.link)
SORT number
```

## My notes
