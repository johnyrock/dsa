# 063. Rotting Oranges

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #994

## Problem

You are given an `m × n` grid where each cell is `0` (empty), `1` (a fresh orange) or `2` (a rotten orange). Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes until no fresh orange remains. If that is impossible because some fresh orange can never be reached, return `-1`.

## Examples

```
Input:  grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1],
]
Output: 4             # rot spreads (1,0),(0,1) → (1,1),(0,2) → (2,1) → (2,2): four waves

Input:  grid = [
  [2, 1, 1],
  [0, 1, 1],
  [1, 0, 1],
]
Output: -1            # the orange at (2, 0) is walled off by empty cells and never rots

Input:  grid = [[0, 2]]
Output: 0             # nothing fresh to begin with, so no time passes
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 10`
- `grid[i][j]` is `0`, `1`, or `2`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from simulating the grid minute by minute to a breadth-first search seeded with every rotten orange, where each queue level is one minute, with complexity.

## Follow-up

- Rot now takes 2 minutes to cross a cell horizontally but 1 vertically. Why does the level-by-level queue stop working, and what replaces it?
- Return the coordinates of the last orange to rot, not just the time. Where in the loop is that known?
- If you may place one extra rotten orange anywhere before the clock starts, how would you pick the cell that minimises the total time?
