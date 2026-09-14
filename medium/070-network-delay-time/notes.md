# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `network_delay_time.py`, keep the tests, write it again.

## Key insight

The signal reaches each node along its shortest path from `k`, and the whole network is done when the slowest of those shortest paths finishes. That is single-source shortest paths with non-negative weights, so Dijkstra: keep a min-heap of `(time, node)`, pop the smallest, and the first time a node is popped its time is final. Relax its outgoing edges by pushing `(time + w, neighbour)`; stale entries for already-settled nodes are skipped on pop. The answer is `max(dist.values())` if all `n` nodes were settled, otherwise `-1`.

## Complexity

- Time: O(E log E), each edge pushes at most one heap entry and each push or pop is logarithmic. With E <= V² this is the same as O(E log V).
- Space: O(V + E) for the adjacency list, the heap, and `dist`.

## Mistakes to watch for

- Building the edge backwards, `graph[v].append((u, w))`. From `k = 2` in the running example nothing is reachable, `dist = {2: 0}`, and the function returns `-1` instead of `2`.
- Returning `max(dist.values())` without the `len(dist) == n` guard. For `times = [[1,2,1]], n = 2, k = 2` the only settled node is the source, and the answer becomes `0` instead of `-1`.
- Returning `sum(dist.values())` instead of `max`. Signals travel in parallel, so the delay is the slowest arrival, `2`, not the total `0 + 1 + 1 + 2 = 4`.
- Dropping the `if node in dist: continue` check. A node popped a second time with a larger `d` overwrites its correct time, which the case `[[1,2,5],[1,3,1],[3,2,1]]` catches: node 2 must keep `2`, not `5`.

## Related

- `medium/018-course-schedule` — the same adjacency-list build over a directed graph, with a queue instead of a heap.
- `medium/071-min-cost-to-connect-all-points` — Prim's algorithm, the same heap loop keyed on edge weight instead of path length.
- `easy/019-last-stone-weight` — `heapq` basics: the smallest entry is always at index 0.
- `patterns/graph.md` — the pattern doc.
