# 095. Rotate Image

**Difficulty:** Medium | **Pattern:** [matrix](../../patterns/matrix.md) ([explained](../../concepts/matrix.html)) | **Source:** LeetCode #48

## Problem

You are given an `n x n` matrix of integers representing an image. Rotate the image by 90 degrees clockwise.

The rotation must be done **in place**: modify the input matrix directly and do not allocate a second matrix. The function returns nothing.

## Examples

```
Input:  matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]   # the first column 1,4,7 read bottom-up becomes the first row 7,4,1

Input:  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]   # the last row becomes the last column, top-down

Input:  matrix = [[1]]
Output: [[1]]                      # a single cell rotates onto itself
```

## Constraints

- `n == matrix.length == matrix[i].length`
- `1 <= n <= 20`
- `-1000 <= matrix[i][j] <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from copying into a second matrix to the transpose-then-reverse trick that rotates in place, with complexity.

## Follow-up

- Rotate counter-clockwise instead. Which of the two phases changes, and to what?
- Rotate by 180 degrees in place. Can you do it with one pass over half the cells rather than two 90-degree rotations?
- The matrix is `m x n` instead of square. Why does in-place rotation become impossible, and what is the best you can do?
