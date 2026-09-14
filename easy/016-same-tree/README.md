# 016. Same Tree

**Difficulty:** Easy | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #100

## Problem

Given the roots `p` and `q` of two binary trees, determine whether they are the same tree: identical in shape, with equal values at every corresponding node.

Return `true` if they match, `false` otherwise. Two empty trees are the same.

## Examples

```
Input:  p = [1,2,3], q = [1,2,3]
Output: true          # same shape, same values

Input:  p = [1,2], q = [1,null,2]
Output: false         # same values, but 2 is a left child in p and a right child in q

Input:  p = [1,2,1], q = [1,1,2]
Output: false         # same shape, children swapped
```

## Constraints

- the number of nodes in each tree is in `[0, 100]`
- `-10^4 <= Node.val <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- Can you do it iteratively with a stack of `(p_node, q_node)` pairs? What goes on the stack when one side is `None`?
- Why is comparing the two trees' in-order traversals not enough? Which pair of trees fools it?
- Symmetric Tree (LeetCode #101) is this function applied to `root.left` and a *mirrored* `root.right`. Which two lines change?
