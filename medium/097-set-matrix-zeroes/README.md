# 097. Set Matrix Zeroes

**Difficulty:** Medium | **Pattern:** [matrix](../../patterns/matrix.md) ([explained](../../concepts/matrix.html)) | **Source:** LeetCode #73

## Problem

Given an `m x n` integer matrix, if any element is `0`, set its entire row and entire column to `0`. Do this **in place**: the function mutates the input and returns nothing.

Zeros written during the process must not trigger further zeroing; only the zeros in the original matrix count.

## Examples

```
Input:  matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]          # the single 0 at (1,1) clears row 1 and column 1

Input:  matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]    # zeros at (0,0) and (0,3) clear row 0, column 0, column 3

Input:  matrix = [[1,2],[0,4]]
Output: [[0,2],[0,0]]                      # the 0 in column 0 clears row 1 and column 0, but not row 0
```

## Constraints

- `m == matrix.length`, `n == matrix[0].length`
- `1 <= m, n <= 200`
- `-2^31 <= matrix[i][j] <= 2^31 - 1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from an O(m × n) copy through O(m + n) flag sets to the O(1) trick of storing the flags in the first row and column, with complexity.

## Follow-up

- The O(m + n) version keeps two boolean lists. Why does moving those flags into row 0 and column 0 need *two extra* booleans, and why not one?
- Suppose zeros written during the process *should* cascade (a newly zeroed row keeps triggering). What does the output become for any matrix with at least one zero?
- Generalise: set the row and column to `0` only for cells equal to a given target `t`. Does anything in the marker approach change?
