# 016. Lowest Common Ancestor of a BST

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #235

## Problem

Given a binary search tree and two of its nodes `p` and `q`, find their lowest common ancestor: the deepest node that has both `p` and `q` as descendants (a node can be a descendant of itself).

## Examples

```
Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6

Input:  root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2      # p is itself an ancestor of q
```

## Constraints

- `2 <= number of nodes <= 10^5`
- all node values are unique
- `p != q`, both exist in the tree

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of walking down using BST ordering instead of searching.

## Follow-up

- Solve the general Lowest Common Ancestor of a Binary Tree (no BST ordering, LeetCode #236) — it needs a different approach.
