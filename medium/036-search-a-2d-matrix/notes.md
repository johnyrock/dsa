# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `search_a_2d_matrix.py`, keep the tests, write it again.

## Key insight

Because every row is sorted and each row starts after the previous one ends, reading the matrix row by row is one sorted list of `rows * cols` values. Run an ordinary binary search on flat indices `0 .. rows * cols - 1` and translate each `mid` back to a cell with `matrix[mid // cols][mid % cols]`. Nothing is copied; the flat array exists only as an index formula.

## Complexity

- Time: O(log(m · n)); each iteration halves the flat window.
- Space: O(1); two indices and a mid.

## Mistakes to watch for

- `while lo < hi` instead of `while lo <= hi`. The window is inclusive on both ends, so a one-element window `lo == hi` is a real candidate. With `<` the running example (`target = 3`) shrinks to `lo = hi = 1` and exits without checking cell 1, returning `False`; `target = 60` (the last cell) fails the same way.
- Dividing by `rows` instead of `cols`: `matrix[mid // rows][mid % rows]`. For a 3 x 4 matrix flat index 5 lands on `matrix[1][2] = 16` instead of `matrix[1][1] = 11`; for a 1 x 6 matrix it raises `IndexError`. The row length is what you divide by.
- Setting `hi = rows * cols` (exclusive) while keeping `<=`. Searching for a value above everything, like `61`, walks `lo` up until `mid` is `rows * cols = 12`, and `matrix[12 // 4]` raises `IndexError`. The inclusive window ends at `rows * cols - 1`.
- Moving the wrong bound: `lo = mid` / `hi = mid` instead of `mid + 1` / `mid - 1`. The window can stop shrinking (`lo = 0, hi = 1` gives `mid = 0` forever) and the loop never ends.

## Related

- [easy/009-binary-search](../../easy/009-binary-search) is the same loop on a plain array; this problem only adds the index translation.
- [medium/021-search-in-rotated-sorted-array](../021-search-in-rotated-sorted-array) is binary search where the "sorted" property needs an extra check each iteration.
- [medium/010-number-of-islands](../010-number-of-islands) is the other grid problem here, where the grid is a graph rather than a sorted list.
- Review the [Binary Search pattern](../../patterns/binary-search.md) and its concept page.
