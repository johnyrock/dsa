# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `valid_sudoku.py`, and write it again.

## Key insight

Every filled cell belongs to exactly three groups: its row, its column, and its 3x3 box. Keep a set of seen digits for each of the 27 groups, and visit the cells once. For each digit, ask all three sets whether it has been seen; if any says yes, the board is invalid, otherwise record it in all three. The one non-obvious line is the box index, `(r // 3) * 3 + c // 3`, which numbers the nine boxes 0–8 in reading order.

## Complexity

- Time: O(81) = O(1) for a fixed 9x9 board; in general O(n²) for an n x n board, one constant-time check and insert per cell.
- Space: O(1) here (27 sets of at most 9 digits); O(n²) in general.

## Mistakes to watch for

- Box index `r // 3 + c // 3` instead of `(r // 3) * 3 + c // 3`. It gives only values 0–4 and merges boxes that share a diagonal; on the valid running example it reports `False`, flagging the `6` at `(3, 4)` as a repeat of the `6` at `(2, 7)`.
- Not skipping `'.'`. The second empty cell in any row is then reported as a duplicate `'.'`, and every real board comes back `False`.
- Recording the digit before checking it, i.e. `add` first then `in`. Every digit is then found "already present" the moment it is checked, so the first filled cell returns `False`.
- Checking only rows and columns. LeetCode example 2 (the `8` at `(0, 0)` and the `8` at `(2, 2)`) is invalid purely because of the box, and passes a row/column-only check.

## Related

- [easy/003-contains-duplicate](../../easy/003-contains-duplicate) is the one-set version of this check: "have I seen this value before?"
- [easy/002-valid-anagram](../../easy/002-valid-anagram) is another fixed-alphabet counting problem where O(1) space is really 26 slots.
- [medium/010-number-of-islands](../../medium/010-number-of-islands) is the other grid-walk problem in the repo, where the neighbourhood matters instead of the row/column/box.
- Review the [Hash Set pattern](../../patterns/hash-set.md) and its concept page.
