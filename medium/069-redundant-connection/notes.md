# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `redundant_connection.py`, keep the tests, write it again.

## Key insight

Add the edges one at a time while tracking connected components with union-find. Before adding `[a, b]`, ask `find(a) == find(b)`: if both endpoints already share a root, earlier edges already connect them and this edge creates a cycle, so it is the answer. Because edges are processed in input order, the first edge that closes a cycle is automatically the last edge of that cycle in the input, which is exactly the tie-break the problem asks for. Otherwise merge the two roots with `parent[root_b] = root_a`.

## Complexity

- Time: O(n α(n)), effectively O(n). Each edge does two `find` calls, and path halving keeps every chain nearly flat.
- Space: O(n) for the `parent` array.

## Mistakes to watch for

- Merging before checking: `parent[find(b)] = find(a)` followed by `if find(a) == find(b)` is always true, so the function returns the very first edge, `[1, 2]`, instead of `[1, 4]`.
- Sizing the array as `list(range(len(edges)))`. Nodes are 1-indexed and node `n` exists, so the last edge `[1, 5]` in the example raises `IndexError` on `parent[5]`.
- Linking the endpoints instead of the roots, `parent[b] = a`. It happens to pass the running example, but it detaches nodes already in `b`'s tree from their old root, so later `find` calls disagree and a cycle can go undetected.
- Comparing `parent[a] == parent[b]` directly instead of calling `find`. Only the roots are meaningful; two nodes in one component can have different direct parents.

## Related

- `medium/018-course-schedule` — cycle detection on a directed graph, where indegrees replace union-find.
- `medium/019-clone-graph` — the same node/edge adjacency shape, traversed with a visited map.
- `patterns/graph.md` — the pattern doc.
