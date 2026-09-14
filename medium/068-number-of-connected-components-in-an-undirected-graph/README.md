# 068. Number of Connected Components in an Undirected Graph

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #323

## Problem

You are given `n` nodes labelled `0` to `n - 1` and a list of undirected `edges`, each a pair `[a, b]`. Two nodes are in the same connected component if there is a path of edges between them.

Return the number of connected components in the graph. A node with no edges at all is a component of its own.

## Examples

```
Input:  n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2             # {0, 1, 2} and {3, 4}

Input:  n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1             # one chain touches every node

Input:  n = 4, edges = []
Output: 4             # no edges: each node is its own component
```

## Constraints

- `1 <= n <= 2000`
- `1 <= edges.length <= 5000`
- `edges[i].length == 2`
- `0 <= ai <= bi < n`
- `ai != bi`
- there are no repeated edges

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from running a fresh traversal out of every unvisited node, to union-find that starts the count at `n` and subtracts one every time an edge merges two different sets, with complexity.

## Follow-up

- Solve it with DFS over an adjacency list instead: count how many times the outer loop finds an unvisited node. Which version is shorter, and which one handles a stream of edges arriving over time?
- Return the *size of the largest* component instead of the count. What one extra array does union-find need, and where is it updated?
- Given a sequence of edge additions, report the component count after each one (dynamic connectivity, additions only). Why does this solution already answer that in amortised near-constant time per edge, and what breaks if edges can also be removed?
