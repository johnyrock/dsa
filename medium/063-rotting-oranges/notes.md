# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `rotting_oranges.py`, keep the tests, write it again.

## Key insight

Rot spreads one cell per minute in every direction from every rotten orange at once, which is exactly what a breadth-first search does if all the rotten oranges start in the queue together. Each BFS level is one minute: read `len(queue)` once, pop that many oranges, rot their fresh neighbours and append them, then `minutes += 1`. Counting `fresh` up front lets the loop stop the moment the last orange rots (`while queue and fresh`) and lets the end detect an orange nothing could reach (`return -1 if fresh else minutes`).

## Complexity

- Time: O(m × n). One scan to seed the queue, then every cell is appended at most once (only while fresh) and checks four neighbours.
- Space: O(m × n) for the queue in the worst case, when almost every cell is rotten at the start. The grid records rot in place.

## Mistakes to watch for

- `while queue:` without `and fresh`. After the last fresh orange rots at minute 4, the queue still holds it, so one more level runs, rots nothing, and returns `5` instead of `4` on the running example. The alternative fix, `minutes - 1` at the end, then breaks the `[[0, 2]]` case, which must return 0, not -1.
- Incrementing `minutes` inside the inner loop, once per pop, instead of once per level. The running example returns 6 (one per orange popped while anything was still fresh) rather than 4.
- Writing `for _ in range(len(queue))` as `while queue` inside the level. The appends made during the level are then processed in the same minute, and the whole grid rots in "1 minute".
- Not marking `grid[nr][nc] = 2` at append time. An orange with two rotten neighbours in the same wave is appended twice and `fresh` is decremented twice, which can go negative and hide an unreachable orange.
- Returning `minutes` when `fresh` is still positive. Example 2 would return 2 instead of -1.

## Related

- [medium/062-walls-and-gates](../062-walls-and-gates) is the same multi-source BFS, but each cell records its own arrival time instead of the grid reporting the last one.
- [medium/010-number-of-islands](../010-number-of-islands) is the same grid graph traversed depth-first, where the order of visits does not matter.
- [medium/061-max-area-of-island](../061-max-area-of-island) is the same scan-and-flood structure measuring components instead of timing a spread.
- Review the [graph pattern](../../patterns/graph.md) and its concept page.
