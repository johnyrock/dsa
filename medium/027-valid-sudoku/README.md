# 027. Valid Sudoku

**Difficulty:** Medium | **Pattern:** [hash-set](../../patterns/hash-set.md) ([explained](../../concepts/hash-map.html)) | **Source:** LeetCode #36

## Problem

You are given a 9x9 sudoku `board` where each cell holds a digit `'1'`–`'9'` or `'.'` for empty. Decide whether the filled cells are valid: no digit repeats within a row, within a column, or within any of the nine 3x3 boxes.

Only the filled cells are checked. The board does not need to be solvable, and an empty board is valid.

## Examples

```
Input:  board =
        5 3 . | . 7 . | . . .
        6 . . | 1 9 5 | . . .
        . 9 8 | . . . | . 6 .
        ------+-------+------
        8 . . | . 6 . | . . 3
        4 . . | 8 . 3 | . . 1
        7 . . | . 2 . | . . 6
        ------+-------+------
        . 6 . | . . . | 2 8 .
        . . . | 4 1 9 | . . 5
        . . . | . 8 . | . 7 9
Output: true          # every filled digit is unique in its row, its column, and its box

Input:  the same board with the top-left 5 replaced by 8
Output: false         # the 8 at (0,0) repeats the 8 at (2,2): different row and column, same top-left box

Input:  board = all '.'
Output: true          # nothing filled, nothing to conflict
```

## Constraints

- `board.length == 9`
- `board[i].length == 9`
- `board[i][j]` is a digit `'1'`–`'9'` or `'.'`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from re-scanning rows, columns, and boxes per cell to one pass with 27 hash sets, with complexity.

## Follow-up

- The three groups can be collapsed into one set of tuples such as `(value, "r", r)`, `(value, "c", c)`, `(value, "b", box)`. What does that buy, and what does it cost in readability?
- Since the digits are `'1'`–`'9'`, each set can be a 9-bit integer with `1 << (int(value) - 1)`. Rewrite the check and the insert as bit operations; what is the space now?
- Sudoku Solver (LeetCode #37) needs this same membership test on every placement attempt. How would you keep the 27 sets updated as digits are placed and removed during backtracking?
