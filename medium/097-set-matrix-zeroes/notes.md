# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `set_matrix_zeroes.py`, keep the tests, write it again.

## Key insight

The obvious approach records which rows and columns need zeroing in two boolean lists. The O(1)-space version stores those flags *inside the matrix*: `matrix[r][0]` is the flag for row `r` and `matrix[0][c]` is the flag for column `c`. Because row 0 and column 0 are doing double duty, whether *they* need zeroing is saved in two ordinary booleans first. Pass 1 sets flags from the interior zeros, pass 2 zeroes interior cells whose row or column flag is set, and only then are row 0 and column 0 zeroed from the saved booleans.

## Complexity

- Time: O(m × n). Two full scans of the interior plus one scan each of row 0 and column 0.
- Space: O(1). Two booleans; the flags live in the matrix.

## Mistakes to watch for

- Zeroing a row and column as soon as a 0 is seen. The written zeros are then discovered later in the same scan and cascade. On the running example `[[1,1,1],[1,0,1],[1,1,1]]` this gives `[[1,0,0],[0,0,0],[0,0,0]]` instead of `[[1,0,1],[0,0,0],[1,0,1]]`.
- Using `matrix[0][0]` as the single flag for both row 0 and column 0. On `[[1,2],[0,4]]` the zero at (1,0) sets `matrix[0][0]`, and a shared flag then zeroes row 0 as well, returning `[[0,0],[0,0]]` instead of `[[0,2],[0,0]]`. Row 0 and column 0 need separate booleans read *before* any marking.
- Zeroing row 0 or column 0 before pass 2 runs. That wipes the flags, so every interior cell reads a zero flag and the whole matrix becomes 0.
- Starting the pass-2 loops at index 0 instead of 1. Row 0 then gets zeroed wherever `matrix[0][0]` happens to be 0, regardless of the saved boolean.

## Related

- [medium/095-rotate-image](../095-rotate-image/) — another in-place matrix transform with no extra allocation.
- [medium/096-spiral-matrix](../096-spiral-matrix/) — index bookkeeping on a matrix without a visited set.
- [medium/010-number-of-islands](../010-number-of-islands/) — also reuses the grid itself as the "visited" marker by overwriting cells.
- Pattern doc: [patterns/matrix.md](../../patterns/matrix.md)
