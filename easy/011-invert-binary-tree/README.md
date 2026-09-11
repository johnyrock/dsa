# 011. Invert Binary Tree

**Difficulty:** Easy | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #226

## Problem

Given the root of a binary tree, mirror it: every node's left and right subtrees are swapped, all the way down. Return the new root.

## Examples

```
Input:  root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Input:  root = [2,1,3]
Output: [2,3,1]

Input:  root = []
Output: []
```

## Constraints

- the number of nodes is in `[0, 100]`
- `-100 <= Node.val <= 100`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the recursive mirror, traced level by level.

## Follow-up

- Rewrite it iteratively with an explicit stack or queue instead of recursion.
- What is the recursion depth on a skewed tree of `n` nodes, and does it matter here?
