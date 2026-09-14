# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned. First review should be a from-scratch re-solve: delete `pacific_atlantic_water_flow.py`, keep the tests, write it again.

## Key insight

Tracing water downhill from every cell repeats the same paths thousands of times. Reverse the flow: start at the ocean and walk *uphill*. A cell is reachable from the Pacific's edge by moving only to neighbours with `heights[nr][nc] >= heights[r][c]` exactly when water from that cell could flow downhill to the Pacific. Run that traversal once seeded with the whole top row and left column, once seeded with the bottom row and right column, and intersect the two visited sets. The visited set *is* the answer for each ocean, so nothing else is stored.

## Complexity

- Time: O(m × n). Each of the two traversals marks a cell on push, so every cell is pushed at most once per ocean and checks four neighbours. The final scan is another O(m × n).
- Space: O(m × n) for the two `seen` sets and the stack.

## Mistakes to watch for

- Flipping the comparison to `heights[nr][nc] <= heights[r][c]`. That walks *downhill* from the ocean, which is the wrong direction; on the running example it returns 15 cells instead of 7, including `(0, 0)` at height 1, which cannot reach the Atlantic at all.
- Using a strict `>` instead of `>=`. Water flows between equal heights, so `[[1, 1], [1, 1]]` must return all four cells; with `>` the traversal never leaves the edge cells and the answer is wrong for any plateau.
- Seeding only the corners, or only one edge per ocean. The Pacific is the *entire* top row plus the *entire* left column; miss the left column and `(3, 0)` (height 6) is dropped from the running example.
- Marking `seen` on pop instead of on push. On a 200 × 200 plateau every cell is pushed from up to four neighbours before it is popped, so the stack grows to four times the grid and the traversal does four times the work.
- Recursive DFS without raising the recursion limit. The 200 × 200 all-equal grid recurses 40,000 deep and crashes.

## Related

- [medium/010-number-of-islands](../010-number-of-islands) is the same iterative DFS on a grid; here the edge condition is a height comparison instead of "is land".
- [medium/062-walls-and-gates](../062-walls-and-gates) is the same "search from the destination instead of the source" reversal, done breadth-first because distances matter there.
- [medium/061-max-area-of-island](../061-max-area-of-island) is another flood fill whose visited set is the thing being measured.
- Review the [graph pattern](../../patterns/graph.md) and its concept page.
