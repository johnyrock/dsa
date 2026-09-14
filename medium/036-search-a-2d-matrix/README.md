# 036. Search a 2D Matrix

**Difficulty:** Medium | **Pattern:** [binary-search](../../patterns/binary-search.md) ([explained](../../concepts/binary-search.html)) | **Source:** LeetCode #74

## Problem

You are given an `m x n` integer matrix with two properties: each row is sorted in non-decreasing order, and the first integer of each row is greater than the last integer of the row before it. Given an integer `target`, return `true` if `target` is in the matrix and `false` otherwise.

The solution must run in `O(log(m * n))` time.

## Examples

```
Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true          # flat index 1 -> row 1 // 4 = 0, col 1 % 4 = 1

Input:  matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false         # 13 would sit between 11 and 16, and no cell holds it

Input:  matrix = [[1]], target = 2
Output: false
```

## Constraints

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from scanning every cell to one binary search over the flattened index with `divmod` to map back to a cell, with complexity.

## Follow-up

- Search a 2D Matrix II (LeetCode #240) drops the "each row starts after the previous row ends" property; rows and columns are each sorted but the matrix does not flatten into one sorted list. Why does this binary search break, and what is the O(m + n) staircase walk that replaces it?
- Do two binary searches instead: one down the first column to pick the row, then one across that row. Is it the same complexity, and which version has more edge cases?
- Return the cell coordinates `(row, col)` instead of a boolean, or `(-1, -1)` if absent. Which line changes?
