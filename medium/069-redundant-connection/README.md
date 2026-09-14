# 069. Redundant Connection

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #684

## Problem

You are given a graph that started as a tree with `n` nodes labeled `1` to `n`, plus exactly one extra edge that was added afterwards. `edges[i] = [a, b]` is an undirected edge between `a` and `b`, and there are exactly `n` edges.

Return the edge that can be removed so the remaining graph is a tree. If several edges qualify, return the one that appears last in the input.

## Examples

```
Input:  edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]         # 1-2-3-4 already connects 1 and 4; [1,4] closes the cycle

Input:  edges = [[1,2],[1,3],[2,3]]
Output: [2,3]         # 1-2 and 1-3 connect 2 and 3 already

Input:  edges = [[1,2],[2,3],[1,3],[3,4]]
Output: [1,3]         # [3,4] comes later but is not part of the cycle
```

## Constraints

- `n == edges.length`
- `3 <= n <= 1000`
- `edges[i].length == 2`
- `1 <= a < b <= n`, no repeated edges
- the input is always a tree plus one edge

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from rerunning a DFS per edge to union-find with path compression, with complexity.

## Follow-up

- LeetCode #685 asks the same question for a *directed* graph. Which extra cases appear (a node with two parents, a cycle, or both)?
- Adding union by rank keeps the trees flat without relying on path compression. Where would the `rank` array change the union step?
- If the extra edge were duplicated (`[a, b]` appearing twice), does the current code still return the right answer?
