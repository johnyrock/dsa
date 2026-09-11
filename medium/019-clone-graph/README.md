# 019. Clone Graph

**Difficulty:** Medium | **Pattern:** [graph](../../patterns/graph.md) ([explained](../../concepts/graph-traversal.html)) | **Source:** LeetCode #133

## Problem

Given a reference node in a connected undirected graph, return a deep copy (clone) of the graph.

## Examples

```
Input:  adjList = [[2,4],[1,3],[2,4],[1,3]]
Output: a cloned graph with the same structure, all new node objects

Input:  adjList = [[]]
Output: a single cloned node with no neighbors
```

## Constraints

- the number of nodes is in `[0, 100]`
- the graph is connected, no repeated edges or self-loops

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of DFS with a visited-to-clone map, and why it handles cycles safely.

## Follow-up

- Rewrite it iteratively with BFS and an explicit queue instead of recursion.
