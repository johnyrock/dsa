# 013. Maximum Depth of Binary Tree

**Difficulty:** Easy | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #104

## Problem

Given the `root` of a binary tree, return its maximum depth: the number of nodes on the longest path from the root down to a leaf.

An empty tree has depth 0; a single node has depth 1.

## Examples

```
Input:  root = [3,9,20,null,null,15,7]
Output: 3             # 3 -> 20 -> 15 (or 3 -> 20 -> 7)

Input:  root = [1,null,2]
Output: 2             # 1 -> 2, the left side is empty

Input:  root = []
Output: 0             # no nodes, no path
```

## Constraints

- the number of nodes is in `[0, 10^4]`
- `-100 <= Node.val <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- The recursion uses O(h) stack. Can you compute the depth iteratively with a queue, level by level (BFS)?
- What changes if you need the *minimum* depth instead (LeetCode #111)? Why does `min` over the children break on a node with only one child?
- A skewed tree of 10^4 nodes has 10^4 stack frames. Does that blow Python's default recursion limit?
