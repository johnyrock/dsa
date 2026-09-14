# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `min_cost_to_connect_all_points.py`, keep the tests, write it again.

## Key insight

Every pair of points is a potential edge, so this is a minimum spanning tree on a complete graph. Prim's algorithm grows the tree one point at a time: keep a min-heap of `(cost, point)` edges leaving the tree, pop the cheapest, and if that point is still outside the tree, absorb it, add the cost, and push an edge from it to every point still outside. A point may sit in the heap several times with different costs; only its first pop counts and `visited` filters the rest. Stop when `connected == n`.

## Complexity

- Time: O(n² log n). Each absorbed point pushes up to n entries, so the heap sees O(n²) pushes and pops at O(log n) each.
- Space: O(n²) for the heap in the worst case, plus O(n) for `visited`.

## Mistakes to watch for

- Dropping the `if visited[i]: continue` guard. Point 3 is popped a second time as `(7, 3)` and counted again: `connected` hits 5 before point 2 ever joins, and the function returns `18` instead of `20`.
- Using Euclidean distance, `math.hypot(dx, dy)`, instead of Manhattan. The running example then returns roughly `16.72`, a float, instead of `20`.
- Looping `while heap` instead of `while connected < n`. The result is still correct because the guard skips stale entries, but it needlessly drains up to n² leftover entries after the tree is complete.
- Seeding with `heap = [(0, 0)]` but forgetting that `total += cost` adds 0 for the seed; seeding with a real distance instead (e.g. to point 1) double counts that edge.

## Related

- `medium/070-network-delay-time` — Dijkstra, the same pop/skip/push heap loop keyed on path length instead of edge weight.
- `medium/069-redundant-connection` — union-find, which is what Kruskal's alternative to this solution would use.
- `easy/019-last-stone-weight` — `heapq` basics.
- `patterns/graph.md` — the pattern doc.
