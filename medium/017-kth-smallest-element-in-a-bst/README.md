# 017. Kth Smallest Element in a BST

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #230

## Problem

Given the root of a binary search tree and an integer `k`, return the `k`-th smallest value in the tree (1-indexed).

## Examples

```
Input:  root = [3,1,4,null,2], k = 1
Output: 1

Input:  root = [5,3,6,2,4,null,null,1], k = 3
Output: 3
```

## Constraints

- the number of nodes is in `[1, 10^4]`
- `0 <= Node.val <= 10^4`
- `1 <= k <= number of nodes`

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of the iterative in-order traversal, stopping early at the k-th visit.

## Follow-up

- If the BST is modified often and `kth_smallest` is called repeatedly, how would you speed it up (augment each node with subtree size)?
