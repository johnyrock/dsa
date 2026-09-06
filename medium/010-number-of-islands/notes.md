# Notes

## Attempts

- 2026-09-06: Folder generated as reference material rather than solved independently, so there is no real attempt behind it yet. The first review should be a from-scratch re-solve: delete `number_of_islands.py`, keep the tests, write it again.

## Key insight

The grid is a graph: each land cell is a node, and orthogonal land neighbours are edges. Counting islands is counting connected components. Scan every cell; the first time you touch unvisited land, that is a new island, so count it and flood-fill (DFS or BFS) from it, marking every reachable land cell visited so the scan never counts that island again. Sinking cells in place (`'1'` to `'0'`) is the cheapest visited set.

## Complexity

- Time: O(m × n). Every cell is scanned once by the outer loop and pushed at most once by the flood fill.
- Space: O(m × n) worst case for the stack or queue, when the whole grid is one island. O(1) beyond that because the grid itself records visits.

## Mistakes to watch for

- Recursive DFS on the full 300 × 300 grid. One giant island recurses 90,000 deep and blows Python's default recursion limit. Use an explicit stack or a queue.
- Marking a cell visited when it is *popped* instead of when it is *pushed*. It still terminates, but the same cell can sit on the stack many times, wasting memory.
- Counting diagonal neighbours. Only the four orthogonal directions connect land.
- Forgetting the bounds check before indexing, or writing `nr < rows` without `0 <= nr`. Negative indices wrap around silently in Python.
- Comparing to the integer `1` when the grid holds the string `'1'`.
- Mutating the caller's grid without saying so. If the grid must be preserved, keep a `visited` set of `(r, c)` instead, at O(m × n) extra space.

## Related

- Max Area of Island (LeetCode #695) is the same flood fill returning the size of each component instead of counting them.
- Rotting Oranges (LeetCode #994) is BFS on the same grid graph, where the queue order carries time.
- Clone Graph (LeetCode #133) and Course Schedule (LeetCode #207) are the same traversal on explicit adjacency lists.
