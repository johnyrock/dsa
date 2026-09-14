# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `copy_list_with_random_pointer.py`, and rebuild the two-pass map approach.

## Key insight

A `random` pointer can target a node that has not been copied yet (it may point forward), so the pointers cannot be wired in the same pass that creates the nodes. Split the work: pass 1 creates one new node per original and records `old_to_new[original] = copy`; pass 2 walks the originals again and sets `copy.next = old_to_new[node.next]` and `copy.random = old_to_new[node.random]`. Seeding the map with `None: None` makes null pointers translate for free. The map is keyed by node *object*, so two nodes with the same `val` stay distinct.

## Complexity

- Time: O(n), two passes over the list with O(1) dict work per node.
- Space: O(n) for the map (plus the O(n) output, which is required). The interleaving trick (`A → A' → B → B'`) gets the extra space to O(1).

## Mistakes to watch for

- Forgetting to seed `{None: None}`. The first node whose `random` is `null` (node 7 in the example) does `old_to_new[None]` and raises `KeyError: None`; the same happens at the tail for `node.next`.
- Setting `copy.random = node.random` instead of `old_to_new[node.random]`. Serialising the copy by value looks right, but the copied nodes point *into the original list*, so it is not a deep copy — the test's identity check catches it.
- Keying the map by `node.val`. With `[[3,null],[3,0],[3,null]]` all three nodes collide on the key `3`, so only one copy is created (the last one written wins) and the result is a one-node list `[[3,null]]`.
- Wiring `next` and `random` in the first pass. `node.random` may point to a node later in the list that has no copy yet, so the lookup fails (or, with `dict.get`, silently becomes `None`): the example's 13 → 0 works but 11 → 4 does not.

## Related

- [medium/019-clone-graph](../019-clone-graph) is the same old-to-new map applied to a graph with arbitrary neighbours.
- [medium/011-lru-cache](../011-lru-cache) also keys a dict by node to reach linked-list nodes in O(1).
- [medium/006-add-two-numbers](../006-add-two-numbers) builds a new list node by node with a dummy head.
- Review the [Hash Map pattern](../../patterns/hash-map.md) and its concept page.
