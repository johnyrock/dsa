# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `construct_binary_tree_from_preorder_and_inorder_traversal.py`, keep the tests, write it again.

## Key insight

The first preorder value is the root. Finding that value in inorder splits inorder into the left subtree's values (everything before it) and the right subtree's (everything after). Because preorder lists the entire left subtree before the right one, a single cursor `next_pre` marching through `preorder` hands out the correct root for every recursive call as long as the left subtree is built before the right. A dict `index_of` makes the inorder split O(1), so each call is O(1) and the whole build is O(n) with no array copying.

## Complexity

- Time: O(n). Building `index_of` is one pass; each of the n nodes is created by one `build` call doing O(1) work.
- Space: O(n) for the map plus O(h) recursion stack (h up to n on a chain).

## Mistakes to watch for

- Building the right subtree before the left, `node.right = build(mid + 1, hi)` first. The cursor then hands the left subtree's preorder values to the right window; on the running example 9 is consumed as the root of the window `[15,20,7]` and the cursor runs off the end with `IndexError: list index out of range`.
- Passing `mid` instead of `mid - 1` as the left window's upper bound, `build(lo, mid)`. The root's own value stays in the left window, so the call consumes one preorder value too many at every level and again runs off the end of `preorder`.
- Forgetting `nonlocal next_pre`. The `+= 1` then makes `next_pre` a local of `build` and Python raises `UnboundLocalError` on the first read.
- Using `inorder.index(val)` instead of the precomputed `index_of` map. Correct, but each call scans the list, making the build O(n²) on a chain of 3000 nodes.
- Slicing both arrays at each call (`preorder[1:mid+1]`, `inorder[:mid]`). Also correct, but every level copies the arrays, which is O(n²) time and space in the worst case, and it is easy to get the preorder slice bounds wrong.

## Related

- [medium/023-serialize-and-deserialize-binary-tree](../023-serialize-and-deserialize-binary-tree/) — rebuilds a tree from a single preorder list by recording the null slots instead of using a second traversal.
- [medium/017-kth-smallest-element-in-a-bst](../017-kth-smallest-element-in-a-bst/) — leans on the same fact that inorder of a tree is "left, node, right".
- [medium/014-binary-tree-level-order-traversal](../014-binary-tree-level-order-traversal/) — a third traversal order, the one the tests use to compare the rebuilt tree.
- [patterns/tree.md](../../patterns/tree.md)
