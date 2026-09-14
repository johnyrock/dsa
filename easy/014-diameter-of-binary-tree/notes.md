# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

The longest path that *bends at* a node is `height(left) + height(right)`, where height counts edges below the node. Every node computes that sum as a side effect of a normal height recursion and updates a `nonlocal diameter`, while returning `1 + max(left, right)` upward as its own height. The answer is the largest sum seen anywhere, not the value returned at the root.

## Complexity

- Time: O(n), a single post-order traversal.
- Space: O(h) for the recursion stack, where h is the tree height.

## Mistakes to watch for

- Returning `left + right` from `height` instead of `1 + max(left, right)`. The parent then reads a path length as a height and the answer inflates.
- Forgetting `nonlocal diameter`. Python creates a fresh local on assignment inside the nested function and the outer `diameter` stays 0.
- Returning the root's `left + right` as the answer. The longest path may live entirely in one subtree (the third README example never touches the root's right side).
- Off-by-one on the base case: `height(None)` must be 0 so a leaf has height 1 and the edge count between two leaves under one parent is 2.

## Related

- [easy/013-maximum-depth-of-binary-tree](../013-maximum-depth-of-binary-tree) is the height recursion this problem wraps.
- [easy/015-balanced-binary-tree](../015-balanced-binary-tree) uses the same "compute height, check something about `left` vs `right` on the way up" shape.
- [medium/016-lowest-common-ancestor-of-a-bst](../../medium/016-lowest-common-ancestor-of-a-bst) is the same idea of "the answer lives at the node where the path bends".
- Review the [Tree pattern](../../patterns/tree.md) and its concept page.
