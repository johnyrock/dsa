# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `clone_graph.py`, keep the tests, write it again.

## Key insight

A hash map from original node to its clone does two jobs at once: it prevents infinite recursion on a cycle (the graph is undirected, so every edge is itself a 2-cycle), and it guarantees each original node is cloned exactly once even when reached via multiple paths. The map entry must be written *before* recursing into neighbors, so a path that loops back finds the in-progress clone instead of recursing again.

## Complexity

- Time: O(V + E), every node and edge visited once.
- Space: O(V) for the map plus O(V) recursion depth in the worst case.

## Mistakes to watch for

- Registering the clone in the map *after* recursing into neighbors instead of before — on any cycle this recurses forever.
- Cloning `val` but sharing the original `neighbors` list reference instead of building a fresh list of cloned neighbors.
- Assuming the graph is directed — it's undirected, so `[[2,4],[1,3],...]` means 1-2 is a two-way edge, not one-way.

## Related

- Course Schedule (medium) traverses a similar adjacency structure but as a directed graph with dependency ordering.
- Number of Islands (medium) is DFS/BFS over an implicit grid graph instead of an explicit adjacency list.
