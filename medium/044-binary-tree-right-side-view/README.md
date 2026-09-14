# 044. Binary Tree Right Side View

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #199

## Problem

Given the `root` of a binary tree, imagine standing to its right and looking across: at each depth you see only the rightmost node. Return the values of those nodes ordered from top (the root) to bottom.

Note that the rightmost node at a level is not always reached by always going right; a left child can be the only node at its depth.

## Examples

```
Input:  root = [1,2,3,null,5,null,4]
Output: [1,3,4]       # levels: [1], [2,3], [5,4]; last of each

Input:  root = [1,2,3,4,null,null,null,5]
Output: [1,3,4,5]     # 4 and 5 hang off the LEFT subtree but are the only nodes at depths 2 and 3

Input:  root = []
Output: []            # empty tree, nothing to see
```

## Constraints

- the number of nodes in the tree is in the range `[0, 100]`
- `-100 <= Node.val <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of why "always go right" fails, level-order traversal with the last node of each level, pitfalls, and complexity.

## Follow-up

- Return the *left* side view instead. Which single character in the solution changes?
- Do it with DFS instead of BFS: visit right child before left, and record a value the first time each depth is reached. Why does the visit order make that correct?
- What if you must return the *leftmost and rightmost* node of every level as pairs?
