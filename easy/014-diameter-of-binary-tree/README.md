# 014. Diameter of Binary Tree

**Difficulty:** Easy | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #543

## Problem

Given the `root` of a binary tree, return the length of its diameter: the longest path between any two nodes, measured in edges. The path does not have to pass through the root.

## Examples

```
Input:  root = [1,2,3,4,5]
Output: 3             # 4 -> 2 -> 1 -> 3 (or 5 -> 2 -> 1 -> 3), three edges

Input:  root = [1,2]
Output: 1             # one edge, 2 -> 1

Input:  root = [1,2,null,3,null,4]
Output: 3             # a left-skewed chain 4 -> 3 -> 2 -> 1; the "path" never bends
```

## Constraints

- the number of nodes is in `[1, 10^4]`
- `-100 <= Node.val <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- The naive approach calls `height` from every node and is O(n^2). Why does one post-order pass suffice?
- What if each node carried a value and the "diameter" were the maximum path *sum* instead of edge count (LeetCode #124)? Which line changes, and why do negative values complicate the recursion?
- Can you return the two endpoint nodes of the longest path, not just its length?
