# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The solution, annotated version, and walkthrough were written up front rather than earned, so the confidence score means nothing yet. First review should be a from-scratch re-solve: delete `count_good_nodes_in_binary_tree.py`, keep the tests, write it again.

## Key insight

A node is good exactly when `node.val >= max(values on the path above it)`, so the only thing a node needs from its ancestors is one number: the largest value seen so far. Carry that number down as a parameter of the DFS. Each call adds 1 if the node clears the bar, raises the bar with `max(max_so_far, node.val)`, and adds whatever its two children report with the raised bar. Seeding with `-inf` makes the root good for free, even when every value is negative.

## Complexity

- Time: O(n), every node is visited once and does a comparison and a `max`.
- Space: O(h) for the call stack, h being the tree's height (up to n for a chain).

## Mistakes to watch for

- Using `>` instead of `>=`. A node equal to the path max is good (the 3 under the 1 in `[3,1,4,3,null,1,5]`), so `>` returns 3 instead of 4 there, and 2 instead of 3 on `[3,3,null,4,2]`.
- Seeding the maximum with `0` or `root.val - 1` instead of `-inf`. With `0`, the tree `[-1,-2,-3]` reports 0 good nodes because the root `-1 >= 0` fails; the answer is 1.
- Comparing against the parent's value instead of the path maximum, i.e. passing `node.val` to the children rather than `max(max_so_far, node.val)`. On `[3,1,4,3,null,1,5]` the 1 under 4 would be compared to 4 (fine), but on `[5,3,7,2,4,6,8]` the 4 under 3 would count because `4 >= 3`, giving 4 instead of 3.
- Keeping the maximum in one shared variable (`nonlocal best`) instead of passing it down. The bar never comes back down when the recursion backtracks, so on `[1,10,2]` the 2 is compared against the 10 from the *other* subtree and the answer is 2 instead of 3.

## Related

- [easy/015-balanced-binary-tree](../../easy/015-balanced-binary-tree/) — the same post-order shape, but information flows *up* (heights) instead of down.
- [medium/015-validate-binary-search-tree](../015-validate-binary-search-tree/) — carries bounds down the recursion the same way this carries a maximum.
- [easy/013-maximum-depth-of-binary-tree](../../easy/013-maximum-depth-of-binary-tree/) — the simplest "visit every node once" recursion.
- [patterns/tree.md](../../patterns/tree.md)
