# 015. Validate Binary Search Tree

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #98

## Problem

Given the root of a binary tree, determine if it is a valid binary search tree: every node's value is strictly greater than all values in its left subtree and strictly less than all values in its right subtree.

## Examples

```
Input:  root = [2,1,3]
Output: true

Input:  root = [5,1,4,null,null,3,6]
Output: false     # 4's left child 3 is less than root 5, but the right subtree of 5 must be > 5
```

## Constraints

- the number of nodes is in `[1, 10^4]`
- `-2^31 <= Node.val <= 2^31 - 1`

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of the inherited-bounds recursion.

## Follow-up

- Why does comparing each node only to its immediate parent fail?
- Solve it with an in-order traversal instead, checking the sequence is strictly increasing.
