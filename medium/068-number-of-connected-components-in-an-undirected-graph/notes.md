# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `number_of_connected_components_in_an_undirected_graph.py`, keep the tests, write it again.

## Key insight

With no edges there are `n` components. Each edge either joins two nodes that are already in the same component (changes nothing) or joins two different components into one (the count drops by exactly one). Union-find answers "same component?" with `find(a) == find(b)`, so the whole algorithm is: start `count = n`, and for every edge whose endpoints have different roots, union them and do `count -= 1`. No adjacency list, no visited set, no traversal.

## Complexity

- Time: O(n + E × α(n)), effectively linear. Each edge does two `find` calls and at most one union; with path halving and union by rank a `find` is amortised inverse-Ackermann.
- Space: O(n) for `parent` and `rank`.

## Mistakes to watch for

- Decrementing `count` for every edge (equivalently returning `n - len(edges)`). A redundant edge inside an existing component must not lower the count. On `n = 5, edges = [[0,1],[1,2],[3,4],[0,2]]` the answer is 2 but the unconditional version returns `5 - 4 = 1`.
- Counting components at the end as `len(set(parent))`. After unions the parent array is not flat: on `n = 4, edges = [[0,1],[2,3],[1,3]]` the final `parent` is `[0, 0, 0, 2]`, whose set has 2 elements, but there is 1 component. Either count `i` with `parent[i] == i`, or, simpler, count merges as you go.
- Writing `find` as `return parent[x]` without the loop. It returns the immediate parent, not the root, so two nodes in the same component can look different and a redundant edge gets counted as a merge.
- Assigning `parent[b] = a` instead of `parent[rb] = ra`. That re-points node `b` itself and orphans whatever was attached to it, splitting a component the count will never see.

## Related

- [medium/067-graph-valid-tree](../067-graph-valid-tree/) is the same union-find, returning `False` on the first repeated root instead of skipping it.
- [medium/010-number-of-islands](../010-number-of-islands/) is the same component count on a grid, done with flood fill.
- [medium/028-longest-consecutive-sequence](../028-longest-consecutive-sequence/) is another "group things into runs" problem where union-find is an alternative to the hash-set scan.
- Pattern doc: [patterns/graph.md](../../patterns/graph.md)
