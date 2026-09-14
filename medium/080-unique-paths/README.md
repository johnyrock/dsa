# 080. Unique Paths

**Difficulty:** Medium | **Pattern:** [dynamic-programming](../../patterns/dynamic-programming.md) ([explained](../../concepts/dynamic-programming.html)) | **Source:** LeetCode #62

## Problem

A robot starts in the top-left corner of an `m x n` grid and wants to reach the bottom-right corner. At each step it can move only right or only down.

Return the number of distinct paths from the start to the finish. The answer is guaranteed to fit in a 32-bit integer.

## Examples

```
Input:  m = 3, n = 7
Output: 28            # each cell's count is the sum of the cell above and the cell to its left

Input:  m = 3, n = 2
Output: 3             # RDD, DRD, DDR

Input:  m = 1, n = 1
Output: 1             # already there: the empty path
```

## Constraints

- `1 <= m, n <= 100`
- the answer is at most `2 * 10^9`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from enumerating every right/down sequence to the 2-D table and the single rolling row, with complexity.

## Follow-up

- Some cells are obstacles the robot cannot enter (LeetCode #63). Which single line of the table update changes?
- Every path is `m - 1` downs and `n - 1` rights in some order. Can you compute the answer as `C(m + n - 2, m - 1)` in O(min(m, n)) time without any table?
- Each cell holds a cost and you want the cheapest path instead of the count (LeetCode #64). What replaces the `+` in the recurrence?
