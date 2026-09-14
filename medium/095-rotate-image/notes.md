# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `rotate_image.py`, keep the tests, write it again.

## Key insight

A clockwise 90-degree rotation sends cell `(r, c)` to `(c, n - 1 - r)`. That map factors into two simple in-place moves: a **transpose** (swap `(r, c)` with `(c, r)`, which turns every column into a row read top-to-bottom) followed by **reversing each row** (which flips that read to bottom-to-top). Each phase is a plain swap loop, so no second matrix is ever allocated.

## Complexity

- Time: O(n²). The transpose touches each cell above the diagonal once; the reverse touches every cell once.
- Space: O(1). Every move is a swap inside the input.

## Mistakes to watch for

- Transposing with `for c in range(n)` instead of `range(r + 1, n)` swaps every pair twice, which undoes the transpose. The rows then just get reversed, giving `[[3,2,1],[6,5,4],[9,8,7]]` for the running example instead of `[[7,4,1],[8,5,2],[9,6,3]]`.
- Reversing rows *before* transposing rotates counter-clockwise: `[[3,6,9],[2,5,8],[1,4,7]]`. Transpose first, then reverse rows, for clockwise.
- Reversing columns instead of rows after the transpose is also counter-clockwise. The row reversal is `row.reverse()` on each `row in matrix`.
- Returning a new matrix (`return [list(col)[::-1] for col in zip(*matrix)]`) gives the right numbers but the caller's list is unchanged, so the in-place requirement fails and the test that inspects the original list sees the old values.

## Related

- [medium/096-spiral-matrix](../096-spiral-matrix/) — the other classic index-gymnastics matrix problem, walking layers instead of rotating them.
- [medium/097-set-matrix-zeroes](../097-set-matrix-zeroes/) — another in-place matrix transform that reuses the matrix itself as its scratch space.
- [medium/036-search-a-2d-matrix](../036-search-a-2d-matrix/) — treats the 2D indices as a flattened 1D range.
- Pattern doc: [patterns/matrix.md](../../patterns/matrix.md)
