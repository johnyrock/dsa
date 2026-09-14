# 096. Spiral Matrix

**Difficulty:** Medium | **Pattern:** [matrix](../../patterns/matrix.md) ([explained](../../concepts/matrix.html)) | **Source:** LeetCode #54

## Problem

Given an `m x n` matrix of integers, return a list of all its elements in **spiral order**: start at the top-left corner, walk right along the top row, down the right column, left along the bottom row, up the left column, and then repeat one layer inward until every cell has been visited.

## Examples

```
Input:  matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]   # outer ring clockwise, then the single inner row 6,7 left to right

Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]            # outer ring, then the lone centre cell 5

Input:  matrix = [[1,2,3]]
Output: [1,2,3]                        # one row: the "bottom" walk must not re-read it backwards
```

## Constraints

- `m == matrix.length`, `n == matrix[i].length`
- `1 <= m, n <= 10`
- `-100 <= matrix[i][j] <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from a visited-set simulation to four shrinking bounds, with complexity.

## Follow-up

- Spiral Matrix II (LeetCode #59) asks for the reverse: fill an empty `n x n` matrix with `1..n²` in spiral order. Does the same four-bounds loop work with `append` replaced by an assignment?
- Produce the spiral counter-clockwise, starting at the top-left and going down first. Which of the four walks change order?
- Generate the spiral lazily as an iterator so a huge matrix does not need the whole output list in memory at once.
