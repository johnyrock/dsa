# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete the solution, and rebuild the invariant.

## Key insight

Walk `root` and, at every node, ask the Same Tree question against `sub_root`. `is_subtree` is the outer walk (`_same_tree(here) or is_subtree(left) or is_subtree(right)`) and `_same_tree` is the exact-match check from problem 016. An empty `sub_root` is trivially a subtree, and once `root` runs out with no match the answer is `False`.

## Complexity

- Time: O(n * m) worst case, where n and m are the sizes of `root` and `sub_root`; a full `_same_tree` check can start at every node of `root`.
- Space: O(h) for the recursion stack, where h is the height of `root`.

## Mistakes to watch for

- Checking only values along the way down and stopping at the first value match. `_same_tree` must compare the *whole* subtree; the second README example fails at a grandchild after the roots agree.
- Getting the two base cases backwards: `sub_root is None` returns `True` (the empty tree is everywhere), `root is None` returns `False` (nothing left to search). Swapping them breaks the single-node case.
- Letting `_same_tree` treat a missing child as a wildcard (`if second is None: return True`). That answers "does `sub_root` match the top of some subtree", not "is it an entire subtree".
- Trying to prune with `root.val == sub_root.val` before recursing into the children — fine as an optimisation, but the recursion into `root.left` and `root.right` must still happen when the values match and the structures differ.

## Related

- [easy/016-same-tree](../016-same-tree) is the inner check, reused verbatim as `_same_tree`.
- [easy/013-maximum-depth-of-binary-tree](../013-maximum-depth-of-binary-tree) is the plain "visit every node" recursion the outer walk is built on.
- [medium/023-serialize-and-deserialize-binary-tree](../../medium/023-serialize-and-deserialize-binary-tree) is the tool the O(n + m) follow-up needs.
- Review the [Tree pattern](../../patterns/tree.md) and its concept page.
