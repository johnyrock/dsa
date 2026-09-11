# 014. Binary Tree Level Order Traversal

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #102

## Problem

Given the root of a binary tree, return the values grouped level by level, left to right.

## Examples

```
Input:  root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Input:  root = [1]
Output: [[1]]

Input:  root = []
Output: []
```

## Constraints

- the number of nodes is in `[0, 2000]`
- `-1000 <= Node.val <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of the BFS queue, level by level.

## Follow-up

- Adapt it to return levels bottom-up, or in a zig-zag (alternating) order.
