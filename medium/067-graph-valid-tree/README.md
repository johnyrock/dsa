# 067. Graph Valid Tree

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #261

## Problem

You are given `n` nodes labelled `0` to `n - 1` and a list of undirected `edges`, each a pair `[a, b]`. Return `true` if these edges form a valid tree: the graph must be connected (every node reachable from every other) and must contain no cycle. Otherwise return `false`.

## Examples

```
Input:  n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true          # 4 edges on 5 nodes, all connected through 0, no cycle

Input:  n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false         # 1-2-3-1 is a cycle; also 5 edges on 5 nodes is one too many

Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: false         # no cycle, but {0,1,2} and {3,4} are two separate pieces
```

## Constraints

- `1 <= n <= 2000`
- `0 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai, bi < n`
- `ai != bi`
- there are no duplicate edges (and no self-loops)

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from removing edges one at a time to see whether they were redundant, to the two-part test — exactly `n - 1` edges and no edge that joins two nodes already in the same union-find set — with complexity.

## Follow-up

- Solve it with a single DFS from node 0 instead of union-find: what do you have to track to distinguish "I came from my parent" from a genuine cycle in an undirected graph?
- If the edges were *directed* and you were asked whether they form a rooted tree, which of the two checks changes, and what new check appears?
- The edges arrive one at a time as a stream and after each edge you must say whether the graph is still a forest. Which part of this solution already answers that in amortised near-constant time?
