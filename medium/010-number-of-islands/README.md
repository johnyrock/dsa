# 010. Number of Islands

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) | **Source:** LeetCode #200

## Problem

Given an `m × n` grid of characters where `'1'` is land and `'0'` is water, return the number of islands.

An island is a group of land cells connected horizontally or vertically. Diagonal neighbours do not count. Assume the grid is surrounded by water on all sides.

## Examples

```
Input:  grid = [
  ["1", "1", "0", "0", "0"],
  ["1", "1", "0", "0", "0"],
  ["0", "0", "1", "0", "0"],
  ["0", "0", "0", "1", "1"],
]
Output: 3             # top-left block, the lone 1 in the middle, the pair bottom-right

Input:  grid = [
  ["1", "1", "1"],
  ["0", "1", "0"],
  ["1", "1", "1"],
]
Output: 1             # everything connects through the centre column

Input:  grid = [["0"]]
Output: 0
```

## Constraints

- `1 <= m, n <= 300`
- `grid[i][j]` is `'0'` or `'1'`
- the grid may be mutated, or use a separate visited set if it must not be

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from counting land cells to a flood fill that sinks each island the first time it is touched, with complexity.

## Follow-up

- The recursive flood fill is shortest to write. Why can it fail on a 300 × 300 grid, and what does the iterative version change?
- How would you count islands if the grid must not be modified? What does that cost in space?
