# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `graph_valid_tree.py`, keep the tests, write it again.

## Key insight

A tree on `n` nodes is exactly a connected graph with `n - 1` edges, and a graph with `n - 1` edges is connected if and only if it has no cycle (every edge must join two previously separate pieces). So check `len(edges) == n - 1` up front, then run union-find over the edges: `find(a) == find(b)` before the union means the edge closes a cycle, so return `False`. If every edge merges two different sets, `n` components collapsed to one, and the answer is `True`.

## Complexity

- Time: O(n + E × α(n)), effectively linear. Each edge does two `find` calls and one union; with path halving and union by rank a `find` is amortised inverse-Ackermann.
- Space: O(n) for `parent` and `rank`.

## Mistakes to watch for

- Dropping the `len(edges) != n - 1` guard. Union-find only detects cycles; on `n = 5, edges = [[0,1],[1,2],[3,4]]` no edge closes a cycle, so the loop finishes and returns `True` for a graph that is two separate pieces.
- Writing `find` as `return parent[x]` with no loop. It returns the immediate parent, not the root. On `n = 5, edges = [[0,1],[2,3],[1,3],[0,3]]` the third union sets `parent[2] = 0`, so node 3's root is 0 but its parent is still 2; the cycle-closing edge `[0, 3]` compares 0 with 2, sees them as different, and the function returns `True` instead of `False`.
- Assigning `parent[b] = a` instead of `parent[rb] = ra`. This re-points node `b` itself (not its root), silently detaching `b` from its old component. On `n = 4, edges = [[0,1],[2,1],[0,2]]` the second edge re-points node 1 under 2 and orphans node 0, so the cycle-closing edge `[0, 2]` looks like a fresh merge and the function returns `True` instead of `False`.
- Checking `len(edges) < n - 1` only. Too many edges also fails the tree test; with `n = 3` and `[[0,1],[1,2],[0,2]]` the cycle check catches it anyway, but relying on that means one more `find` pass for nothing.

## Related

- [medium/068-number-of-connected-components-in-an-undirected-graph](../068-number-of-connected-components-in-an-undirected-graph/) is the same union-find, counting successful unions instead of failing on the first cycle.
- [medium/018-course-schedule](../018-course-schedule/) detects a cycle in a *directed* graph, which needs Kahn's algorithm or DFS colouring rather than union-find.
- [medium/010-number-of-islands](../010-number-of-islands/) counts connected components on a grid with flood fill.
- Pattern doc: [patterns/graph.md](../../patterns/graph.md)
