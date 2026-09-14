# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `max_area_of_island.py`, keep the tests, write it again.

## Key insight

This is Number of Islands with one extra counter. Scan every cell; the first time the scan touches unvisited land, flood-fill from it with an explicit stack, sinking each cell to `0` as it is pushed so it is never pushed twice, and count one for every pop. When the stack empties, `area` is the size of that island, and `best = max(best, area)` keeps the record. Sinking in place is the visited set, so the outer scan skips the rest of an island it has already measured.

## Complexity

- Time: O(m × n). Every cell is scanned once by the outer loop, and every land cell is pushed and popped at most once by the flood fill.
- Space: O(m × n) worst case for the stack, when the whole grid is one island. Nothing else beyond the grid, which doubles as the visited set.

## Mistakes to watch for

- Counting on push instead of on pop, i.e. `area += 1` only inside the neighbour loop. The seed cell is never counted, so every island comes out one short: the running example returns `3` instead of `4`.
- Declaring `area = 0` once before the scan instead of once per island. It then accumulates across islands and the function returns the total land, `8` on the running example, instead of the largest island.
- Sinking a cell when it is popped instead of when it is pushed. The same cell can be pushed from two neighbours before either pop happens, so it is popped twice and counted twice; a 2 × 2 block reports area 5 or 6 instead of 4.
- Writing `nr < rows` without `0 <= nr`. Negative indices wrap around silently in Python, so a flood fill on row 0 reads row `rows - 1` and can leak into an unrelated island.
- Returning `area` instead of `best`, which gives the size of the *last* island scanned (1 on the running example).

## Related

- [medium/010-number-of-islands](../010-number-of-islands) is the same scan-and-sink flood fill, counting islands instead of measuring them.
- [medium/063-rotting-oranges](../063-rotting-oranges) is the same grid graph traversed breadth-first, where the queue order carries time.
- [medium/058-word-search](../058-word-search) is a grid DFS where the visited mark must be undone on backtrack, which this problem never needs.
- Review the [graph pattern](../../patterns/graph.md) and its concept page.
