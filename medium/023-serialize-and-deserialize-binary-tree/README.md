# 023. Serialize and Deserialize Binary Tree

**Difficulty:** Medium | **Pattern:** [tree](../../patterns/tree.md) ([explained](../../concepts/tree-traversal.html)) | **Source:** LeetCode #297

## Problem

Design an algorithm to serialize a binary tree to a string and deserialize that string back to the original tree structure (any encoding is fine, as long as it round-trips).

## Examples

```
Input:  root = [1,2,3,null,null,4,5]
serialize -> some string
deserialize(serialize(root)) -> a tree with the same structure and values
```

## Constraints

- the number of nodes is in `[0, 10^4]`
- `-1000 <= Node.val <= 1000`

## Walkthrough

Open [walkthrough.html](walkthrough.html) for a scroll-driven narration of pre-order encoding with null markers, and why that's enough to rebuild the exact shape.

## Follow-up

- Could you serialize more compactly, e.g. binary-encoding instead of comma-separated text?
