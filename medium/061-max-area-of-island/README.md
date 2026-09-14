# 061. Max Area of Island

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #695

## Problem

You are given an `m × n` binary matrix `grid` where `1` is land and `0` is water. An island is a group of `1` cells connected horizontally or vertically (not diagonally), and the four edges of the grid are surrounded by water.

The area of an island is the number of cells it contains. Return the maximum area of any island in `grid`, or `0` if there is no island.

## Examples

```
Input:  grid = [
  [0, 0, 1, 0, 0],
  [0, 1, 1, 0, 0],
  [0, 0, 0, 1, 0],
  [1, 0, 1, 1, 1],
]
Output: 4             # three islands of area 3, 4 and 1; the L-shape bottom-right is the largest

Input:  grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
Output: 0             # no land at all

Input:  grid = [
  [1, 1, 0],
  [1, 1, 0],
  [0, 0, 1],
]
Output: 4             # the 2 × 2 block; the corner cell (2, 2) only touches it diagonally
```

## Constraints

- `m == grid.length`
- `n == grid[i].length`
- `1 <= m, n <= 50`
- `grid[i][j]` is either `0` or `1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from counting land cells to a flood fill that measures each island the first time it is touched, with complexity.

## Follow-up

- Return the coordinates of the largest island's cells, not just its area. What extra bookkeeping does the flood fill need?
- Suppose you may flip one `0` to `1` (LeetCode #827, Making A Large Island). Why does labelling each island with an id during the flood fill make that a second O(m × n) pass?
- If the grid must not be mutated, what replaces `grid[r][c] = 0` and what does it cost?
