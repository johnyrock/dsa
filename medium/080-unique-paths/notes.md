# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `unique_paths.py`, keep the tests, write it again.

## Key insight

The robot enters any cell from exactly one of two neighbours: the cell above (its last move was down) or the cell to the left (its last move was right). So `paths(r, c) = paths(r - 1, c) + paths(r, c - 1)`, with every cell in the first row and first column equal to 1 because only one straight-line route reaches them. Filling rows top to bottom, only the previous row is ever read, so a single row updated in place (`row[c] += row[c - 1]`) is the whole table.

## Complexity

- Time: O(m × n), one addition per cell.
- Space: O(n) for the single rolling row.

## Mistakes to watch for

- Seeding the row with zeros (`row = [0] * n`). The first row and column must be 1, or every sum stays 0 and `unique_paths(3, 7)` returns 0.
- Iterating rows `for _ in range(m)` instead of `range(1, m)`. The seed row already *is* row 0, so this computes one row too many: `(3, 7)` returns 84 (the answer for a 4 × 7 grid) instead of 28.
- Starting the column loop at 0: `row[0] += row[-1]` reads the last cell in Python and corrupts column 0, which must stay 1.
- Using a 2-D table but initialising only `dp[0][0] = 1` and then reading `dp[r - 1][c]` / `dp[r][c - 1]` without bounds guards at the edges — either an `IndexError` or a wrap to index `-1`.

## Related

- [easy/010-climbing-stairs](../../easy/010-climbing-stairs/) is the 1-D version of "count ways by summing the ways into each predecessor".
- [easy/020-min-cost-climbing-stairs](../../easy/020-min-cost-climbing-stairs/) is what this becomes when `+` turns into `min` plus a cost.
- [medium/010-number-of-islands](../010-number-of-islands/) uses the same grid-of-cells layout for a graph problem instead of a table.
- [patterns/dynamic-programming.md](../../patterns/dynamic-programming.md)
