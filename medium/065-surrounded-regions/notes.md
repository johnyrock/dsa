# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `surrounded_regions.py`, keep the tests, write it again.

## Key insight

Deciding whether a region is surrounded means checking whether any of its cells touches the border, and that is awkward to do while flood-filling from the inside because you only know the answer once the whole region is explored. Invert the question: flood-fill from every `'O'` on the border and relabel everything reached as `'T'`. Those are exactly the regions that cannot be captured. A final pass then flips every remaining `'O'` to `'X'` (surrounded) and every `'T'` back to `'O'` (safe).

## Complexity

- Time: O(m × n). Every cell is scanned a constant number of times, and every `'O'` is pushed onto the stack at most once because it is relabelled to `'T'` before being pushed.
- Space: O(m × n) worst case for the explicit stack (a board that is all `'O'` is one region). No visited set: the board itself records what has been reached.

## Mistakes to watch for

- Seeding only the top row and left column (`for c in range(cols): if board[0][c] == "O"` and the matching left-column loop) misses `'O'` cells on the bottom and right edges. On the running example (3,1), (1,4) and (2,4) are never marked safe and get flipped, so the whole board comes out `'X'`.
- Flood-filling from interior cells and flipping them to `'X'` as you go, then trying to undo when the fill hits a border. By the time you learn the region is safe you have already destroyed part of it; the undo needs a second list of every cell touched. The border-first approach never needs an undo.
- Relabelling reached cells as `'O'` instead of a distinct `'T'`. The fill then re-pushes cells it has already visited (they still look like unvisited `'O'`) and loops forever on any region of two or more cells.
- Checking `nr < rows` but not `0 <= nr`. Python's `board[-1]` is the last row, so a fill starting on row 0 silently connects to row `rows - 1` and marks bottom-row interior regions safe when they are not.

## Related

- [medium/010-number-of-islands](../010-number-of-islands/) is the same flood fill with the same "sink cells as you push them" trick, counting components instead of capturing them.
- [medium/058-word-search](../058-word-search/) walks the same 4-neighbour grid but backtracks, un-marking cells on the way out.
- [medium/019-clone-graph](../019-clone-graph/) is the same BFS/DFS over an explicit adjacency list rather than a grid.
- Pattern doc: [patterns/graph.md](../../patterns/graph.md)
