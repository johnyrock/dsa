# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `walls_and_gates.py`, keep the tests, write it again.

## Key insight

Searching from each room toward the gates repeats work; searching from the gates toward the rooms shares it. Put *every* gate in the queue at once, all at distance 0, and run one breadth-first search. BFS visits cells in non-decreasing distance order, so the first time a room is dequeued-into is via a shortest path from the closest gate, and `rooms[nr][nc] = rooms[r][c] + 1` is final. Because only cells still equal to `INF` are written, writing the distance is also the visited mark, and walls, gates, and filled rooms are all skipped by the same `== INF` test.

## Complexity

- Time: O(m × n). Each cell enters the queue at most once (only while it is `INF`) and does four constant-time neighbour checks.
- Space: O(m × n) for the queue in the worst case, when almost every cell is a gate or one BFS layer is a whole diagonal. Distances are stored in the input grid.

## Mistakes to watch for

- Running a separate BFS from each gate and skipping cells that are no longer `INF`. The first gate claims every reachable room with *its* distance, and later, closer gates cannot overwrite. On the running example `(2, 0)` becomes 4 (from the gate at `(0, 2)`) instead of 1 (from the gate at `(3, 0)`), and `(0, 0)` becomes 4 instead of 3.
- Testing `rooms[nr][nc] != -1` instead of `== INF`. Gates and already-filled rooms then get overwritten with a larger distance and re-queued, and the loop never terminates.
- Running a BFS from each *room* toward the nearest gate: correct, but O((m × n)²) on a 250 × 250 grid.
- Using DFS from the gates. A depth-first path reaches a room by whatever route it stumbled on first, not the shortest, so distances come out too large unless you allow rewrites, which reintroduces the quadratic cost.
- Forgetting the empty-grid guard: `len(rooms[0])` raises `IndexError` on `[]`.

## Related

- [medium/063-rotting-oranges](../063-rotting-oranges) is the same multi-source BFS where the layer number is the answer instead of a per-cell fill.
- [medium/010-number-of-islands](../010-number-of-islands) is the same grid graph traversed depth-first, where order does not matter.
- [medium/036-search-a-2d-matrix](../036-search-a-2d-matrix) is another matrix problem, but one where the structure lets you skip the traversal entirely.
- Review the [graph pattern](../../patterns/graph.md) and its concept page.
