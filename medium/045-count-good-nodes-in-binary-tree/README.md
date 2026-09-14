# 045. Count Good Nodes in Binary Tree

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #1448

## Problem

Given the root of a binary tree, a node `X` is *good* if on the path from the root down to `X` there is no node with a value greater than `X.val`. The root is always good, because there is nothing above it.

Return the number of good nodes in the tree.

## Examples

```
Input:  root = [3,1,4,3,null,1,5]
Output: 4             # root 3 is good; 4 (path 3,4); the deeper 3 (path 3,1,3, equal counts); 5 (path 3,4,5)
                      # the 1 under the root and the 1 under 4 are not: 3 and 4 sit above them

Input:  root = [3,3,null,4,2]
Output: 3             # root 3, the child 3 (equal is fine), and 4; the 2 is blocked by 3 and 4

Input:  root = [1]
Output: 1             # a single node has no ancestors, so it is good
```

## Constraints

- the number of nodes is in `[1, 10^5]`
- `-10^4 <= Node.val <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from re-walking every root-to-node path to a single DFS that carries the path maximum downward, with complexity.

## Follow-up

- Count the nodes that are *strictly* greater than every ancestor. Which single character changes, and which answer in the examples changes with it?
- Return the good nodes' values in the order they are found rather than a count. Does the traversal order (pre-order vs. post-order) matter for the count? For the list?
- Solve it iteratively with an explicit stack of `(node, max_so_far)` pairs so a 10^5-node chain does not blow the recursion limit.
