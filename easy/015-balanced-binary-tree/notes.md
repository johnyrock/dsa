# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Compute heights bottom-up and overload the return value: a real height means "this subtree is balanced", and -1 means "something below here is already broken". A node returns -1 if either child returned -1 or if `abs(left - right) > 1`; otherwise it returns `1 + max(left, right)`. Checking the left child's -1 before recursing into the right skips work once the answer is known. The tree is balanced iff the root does not return -1.

## Complexity

- Time: O(n), each node's height is computed once.
- Space: O(h) for the recursion stack, where h is the tree height.

## Mistakes to watch for

- Only checking the balance condition at the root. `[1,2,2,3,3,null,null,4,4]` is balanced at the root (heights 3 and 2) but not at the left `2`.
- Computing `abs(left - right) > 1` before checking that neither side is -1. A -1 next to a height of 0 passes the difference test and the failure is silently lost.
- Using 0 as the sentinel. A `None` child already has height 0, so "unbalanced" and "empty" become indistinguishable; -1 is the only value a real height can never take.
- Comparing `height(root) == -1` and returning that. The function must return `True` for balanced, so the test is `!= -1`.

## Related

- [easy/013-maximum-depth-of-binary-tree](../013-maximum-depth-of-binary-tree) is the plain height recursion this problem decorates.
- [easy/014-diameter-of-binary-tree](../014-diameter-of-binary-tree) is the same shape with a `nonlocal` max instead of a sentinel.
- [medium/015-validate-binary-search-tree](../../medium/015-validate-binary-search-tree) is another "every node must satisfy a local condition" recursion where checking only the root is the classic bug.
- Review the [Tree pattern](../../patterns/tree.md) and its concept page.
