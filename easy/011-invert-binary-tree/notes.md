# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `invert_binary_tree.py`, keep the tests, write it again.

## Key insight

Inverting a tree means every node's left and right children are swapped, recursively. If you already have the inverted left subtree and the inverted right subtree, the whole tree is inverted by swapping those two results into the opposite slots on the current node. Base case: an empty subtree inverts to itself.

## Complexity

- Time: O(n), every node is visited exactly once.
- Space: O(h) for the call stack, where h is the tree's height — O(log n) balanced, O(n) worst case (a skewed chain).

## Mistakes to watch for

- Swapping `root.left` and `root.right` directly (`root.left, root.right = root.right, root.left`) without recursing first only swaps the top level; the subtrees underneath are untouched.
- Recursing on the already-swapped attributes instead of the original ones — assign the recursive calls' results in one tuple statement so the right-hand side reads the pre-swap values.
- Forgetting the `None` base case causes an `AttributeError` on leaf nodes.

## Related

- Binary Tree Level Order Traversal (medium) traverses the same shape breadth-first instead of recursively.
- Symmetric Tree (easy, LeetCode #101) compares a tree against its own mirror instead of building one.
