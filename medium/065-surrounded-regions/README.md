# 065. Surrounded Regions

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #130

## Problem

You are given an `m × n` board of characters where each cell is `'X'` or `'O'`. A region is a group of `'O'` cells connected horizontally or vertically. A region is *surrounded* if it is completely enclosed by `'X'` cells, which is the same as saying none of its cells lies on the border of the board.

Capture every surrounded region by flipping all of its `'O'` cells to `'X'`, in place. Regions that touch the border are left alone.

## Examples

```
Input:  board = [
  ["X", "X", "X", "X", "X"],
  ["X", "O", "O", "X", "O"],
  ["X", "X", "O", "X", "O"],
  ["X", "O", "X", "X", "X"],
]
Output: [
  ["X", "X", "X", "X", "X"],
  ["X", "X", "X", "X", "O"],   # the (1,1)-(1,2)-(2,2) blob touches no edge: captured
  ["X", "X", "X", "X", "O"],   # (1,4) and (2,4) sit on the right edge: kept
  ["X", "O", "X", "X", "X"],   # (3,1) sits on the bottom edge: kept
]

Input:  board = [
  ["X", "X", "X", "X"],
  ["X", "O", "O", "X"],
  ["X", "X", "O", "X"],
  ["X", "O", "X", "X"],
]
Output: [
  ["X", "X", "X", "X"],
  ["X", "X", "X", "X"],
  ["X", "X", "X", "X"],
  ["X", "O", "X", "X"],        # only the bottom-row O survives
]

Input:  board = [["X"]]
Output: [["X"]]
```

## Constraints

- `m == board.length`, `n == board[i].length`
- `1 <= m, n <= 200`
- `board[i][j]` is `'X'` or `'O'`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from flood-filling every region and asking "did I touch the edge?" to the inverted approach that flood-fills only from the border and captures whatever is left, with complexity.

## Follow-up

- The solution overwrites the board with a third symbol `'T'`. How would you do it without a third symbol, using only a visited set, and what does that cost?
- Instead of capturing regions, return the *number* of surrounded regions. What is the smallest change to the traversal?
- If the board were 10,000 × 10,000 and would not fit in memory as a whole, could you still decide which `'O'` cells touch the border in a streaming pass over rows?
