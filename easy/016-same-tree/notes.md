# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Two trees are the same when their roots agree and, recursively, their left subtrees are the same and their right subtrees are the same. The base case collapses to one line: if either node is `None`, they match only if both are (`p is q`). The `and` chain short-circuits, so the first mismatch anywhere stops the traversal.

## Complexity

- Time: O(min(n, m)); the walk stops at the first mismatch and never visits more nodes than the smaller tree has.
- Space: O(h) for the recursion stack, where h is the height of the smaller tree.

## Mistakes to watch for

- Writing the base case as `if p is None and q is None: return True` and then reading `p.val` when only one is `None`. That is an `AttributeError` on `[1,2]` vs `[1,null,2]`.
- Comparing `p == q` on nodes. `TreeNode` has no `__eq__`, so that is identity, and two distinct-but-equal trees return `False`.
- Comparing values only and never recursing into structure, so `[1,2]` and `[1,null,2]` come back equal.
- Recursing `(p.left, q.right)` on one side. That is the Symmetric Tree recursion, not this one.

## Related

- [easy/017-subtree-of-another-tree](../017-subtree-of-another-tree) calls this exact function at every node of the larger tree.
- [easy/011-invert-binary-tree](../011-invert-binary-tree) is the same two-branch recursion with a swap instead of a comparison.
- [medium/023-serialize-and-deserialize-binary-tree](../../medium/023-serialize-and-deserialize-binary-tree) gives another way to test tree equality: compare the serialized strings, including the `null` markers.
- Review the [Tree pattern](../../patterns/tree.md) and its concept page.
