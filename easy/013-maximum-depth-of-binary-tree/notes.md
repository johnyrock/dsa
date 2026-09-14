# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

The depth of a tree is one (for the root) plus the depth of its taller subtree. `max_depth(None)` is 0, and every other node returns `1 + max(max_depth(left), max_depth(right))`. The recursion is post-order: both children answer before the parent can, and the final answer bubbles up from the leaves.

## Complexity

- Time: O(n), every node is visited exactly once.
- Space: O(h) for the recursion stack, where h is the tree height; O(n) on a skewed tree.

## Mistakes to watch for

- Returning 1 for `None` instead of 0. Every leaf then counts as depth 2 and the whole answer is off by one.
- Counting edges instead of nodes. LeetCode #104 wants nodes, so a single node is depth 1, not 0.
- Forgetting the `None` guard entirely and touching `root.left` on an empty tree, which raises `AttributeError` for `root = []`.
- Using `+` instead of `max` on the two children's depths. That sums the subtrees and only happens to match when one side is empty.

## Related

- [easy/014-diameter-of-binary-tree](../014-diameter-of-binary-tree) is the same height recursion with a running max of `left + right` kept on the side.
- [easy/015-balanced-binary-tree](../015-balanced-binary-tree) is the same height recursion with an early -1 exit when the two sides differ by more than 1.
- [medium/014-binary-tree-level-order-traversal](../../medium/014-binary-tree-level-order-traversal) is the BFS version: the number of levels emitted is the depth.
- Review the [Tree pattern](../../patterns/tree.md) and its concept page.
