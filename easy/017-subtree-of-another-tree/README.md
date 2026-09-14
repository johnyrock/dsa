# 017. Subtree of Another Tree

**Difficulty:** Easy | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #572

## Problem

Given the roots of two binary trees, `root` and `subRoot`, determine whether `subRoot` appears inside `root` as a complete subtree: some node of `root`, together with *all* of its descendants, has exactly the same shape and values as `subRoot`.

Return `true` if such a node exists, `false` otherwise. A tree counts as a subtree of itself.

## Examples

```
Input:  root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true          # the node 4 in root has children 1 and 2 and nothing else

Input:  root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false         # the 4 in root matches at the top, but its 2 has an extra child 0

Input:  root = [1], subRoot = [1]
Output: true          # a tree is a subtree of itself
```

## Constraints

- the number of nodes in `root` is in `[1, 2000]`
- the number of nodes in `subRoot` is in `[1, 1000]`
- `-10^4 <= root.val, subRoot.val <= 10^4`

## Walkthrough

Open [walkthrough.html](walkthrough.html) in a browser for a scroll-driven narration of the brute-force idea, invariant, trace, pitfalls, and complexity.

## Follow-up

- The solution is O(n * m) in the worst case. Which pair of trees actually hits that bound?
- Can you get to O(n + m) by serializing both trees (with explicit `null` markers) and running a substring search? Why are the markers essential, and why is a `#1` vs `#12` prefix a trap?
- What if `subRoot` may appear as a *partial* subtree, matching only the top of some node's descendants? Which base case changes?
