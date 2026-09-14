# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `spiral_matrix.py`, keep the tests, write it again.

## Key insight

Keep four inclusive bounds, `top`, `bottom`, `left`, `right`, that describe the rectangle not yet emitted. One loop iteration walks the top row, the right column, the bottom row, and the left column of that rectangle, shrinking the corresponding bound after each walk. The bottom and left walks are guarded by `if top <= bottom` and `if left <= right` because after the first two shrinks the rectangle may have collapsed to a single row or column that has already been read.

## Complexity

- Time: O(m × n). Every cell is appended exactly once; the bound arithmetic is O(1) per walk.
- Space: O(1) beyond the output list. Four integers of state, no visited set.

## Mistakes to watch for

- Dropping the `if top <= bottom` guard before the bottom walk. On the running example the inner layer is one row (`6, 7`); after the top walk reads it, `top` is 2 and `bottom` is 1, and an unguarded bottom walk reads `matrix[1][1..]` again, giving `[..., 5, 6, 7, 6]` (13 values for 12 cells). On a single-row matrix `[[1,2,3]]` it returns `[1, 2, 3, 2, 1]`.
- Dropping the `if left <= right` guard has the same effect on a single-column matrix `[[1],[2],[3]]`: the left walk re-reads the column upward.
- Off-by-one on the ranges: the bottom walk must run `range(right, left - 1, -1)` to include `left`, and the left walk `range(bottom, top - 1, -1)` to include `top`. Stopping at `left` or `top` skips a corner cell.
- Shrinking the wrong bound after a walk (`bottom -= 1` after the top walk) makes the rectangle collapse from the wrong side and skips whole rows.

## Related

- [medium/095-rotate-image](../095-rotate-image/) — layer-by-layer thinking on a square matrix.
- [medium/036-search-a-2d-matrix](../036-search-a-2d-matrix/) — flattening 2D indices to 1D, another way to walk a matrix without a visited set.
- [medium/010-number-of-islands](../010-number-of-islands/) — grid traversal where a visited marker *is* needed because the walk is not a fixed pattern.
- Pattern doc: [patterns/matrix.md](../../patterns/matrix.md)
