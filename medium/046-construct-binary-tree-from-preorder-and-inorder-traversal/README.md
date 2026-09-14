# 046. Construct Binary Tree from Preorder and Inorder Traversal

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #105

## Problem

Given two integer arrays `preorder` and `inorder`, the preorder and inorder traversals of the same binary tree with distinct values, rebuild that tree and return its root.

Preorder lists each node before its subtrees (root, left, right); inorder lists the left subtree, then the node, then the right subtree. Together they pin down exactly one tree.

## Examples

```
Input:  preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]   # preorder[0] = 3 is the root; in inorder, [9] is left of 3 and [15,20,7] is right of it
                                  # the right window's root is the next preorder value, 20, with 15 left of it and 7 right of it

Input:  preorder = [-1], inorder = [-1]
Output: [-1]                      # a single node is its own tree

Input:  preorder = [1,2,3], inorder = [3,2,1]
Output: [1,2,null,3]              # inorder is preorder reversed, so every node is a left child: a left-leaning chain
```

## Constraints

- `1 <= preorder.length <= 3000`
- `inorder.length == preorder.length`
- `-3000 <= preorder[i], inorder[i] <= 3000`
- `preorder` and `inorder` consist of unique values
- each value of `inorder` also appears in `preorder`
- `preorder` is guaranteed to be the preorder traversal of the tree and `inorder` its inorder traversal

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the solution, from slicing both arrays at every call to a single preorder cursor plus a value-to-index map over inorder, with complexity.

## Follow-up

- Do the same from `inorder` and `postorder` (LeetCode #106). Which end of `postorder` holds the root, and in which order must the two subtrees now be built?
- Why can `preorder` and `postorder` alone *not* always determine the tree? Give the smallest pair of trees that share both traversals.
- Drop the "distinct values" guarantee. What breaks in the `index_of` map, and is the tree still unique?
