# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `lowest_common_ancestor_of_a_bst.py`, keep the tests, write it again.

## Key insight

BST ordering means you never have to search both subtrees. Starting at the root, if both `p` and `q` are smaller, the LCA can only be in the left subtree; if both are larger, only the right. The moment they're no longer both on the same side — one is less-or-equal, the other greater-or-equal — the current node is exactly where their paths split, which is the LCA by definition.

## Complexity

- Time: O(h), h being the tree's height — O(log n) balanced, O(n) worst case.
- Space: O(1) with the iterative version; O(h) if written recursively.

## Mistakes to watch for

- Solving it like the general binary-tree LCA problem (search both subtrees, no ordering) — correct but throws away the BST structure and is more code than needed.
- Off-by-one on the branching condition: use strict `<`/`>` for "both smaller" / "both larger", and let anything else (including equality) fall into the "found it" branch.
- Forgetting that either `p` or `q` can be an ancestor of the other, and that's still a valid split point.

## Related

- Validate Binary Search Tree (medium) is the same "carry bounds down the tree" instinct, applied to check ordering instead of finding a split.
- Lowest Common Ancestor of a Binary Tree (LeetCode #236) is the general version without a BST's ordering guarantee.
