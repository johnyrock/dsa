# 015. Balanced Binary Tree

**Difficulty:** Easy | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #110

## Problem

Given the `root` of a binary tree, determine whether it is height-balanced: for every node, the heights of its left and right subtrees differ by at most 1.

Return `true` if the whole tree satisfies that, `false` otherwise. An empty tree is balanced.

## Examples

```
Input:  root = [3,9,20,null,null,15,7]
Output: true          # root: left height 1, right height 2, differ by 1

Input:  root = [1,2,2,3,3,null,null,4,4]
Output: false         # the left 2 has heights 2 and 0 under it

Input:  root = []
Output: true          # nothing to be unbalanced
```

## Constraints

- the number of nodes is in `[0, 5000]`
- `-10^4 <= Node.val <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- The top-down version (`abs(height(l) - height(r)) <= 1 and balanced(l) and balanced(r)`) recomputes heights. What is its worst-case time, and on which tree shape?
- Can you write it without the -1 sentinel, returning a `(balanced, height)` tuple instead? Which reads better?
- What if the condition were "every node's subtree sizes differ by at most 1" (weight-balanced)? What does `height` become?
