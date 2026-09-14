# Notes

## Attempts

- 2026-09-13: Folder generated as reference material, not solved independently. The first review should be a from-scratch re-solve: keep the tests, delete `remove_nth_node_from_end_of_list.py`, and rebuild the two-pointer walk.

## Key insight

Two pointers that start together and are separated by exactly `n` steps stay `n` apart no matter how far they walk. When the leading pointer reaches the last node, the trailing pointer is `n + 1` from the end, which is the node *before* the one to delete. Starting both on a dummy node in front of `head` (rather than on `head`) is what makes the trailing pointer land on the predecessor, and it also means deleting the head is not a special case: `dummy.next` is returned either way.

## Complexity

- Time: O(sz), one walk over the list (the gap loop and the main loop together touch each node at most once with `fast`).
- Space: O(1), two pointers and one dummy node.

## Mistakes to watch for

- Looping `while fast is not None` instead of `while fast.next is not None`. Both pointers go one step too far, `slow` lands *on* the target instead of before it, and `slow.next = slow.next.next` deletes the node after it: `[1,2,3,4,5], n = 2` returns `[1,2,3,4]` instead of `[1,2,3,5]`.
- Starting `fast` and `slow` on `head` instead of the dummy. Then with `n == sz` the gap loop pushes `fast` to `None` and the main loop's `fast.next` crashes with `AttributeError`; and even when it does not crash, there is no predecessor for the head, so `[1,2], n = 2` needs a separate `return head.next` branch.
- Advancing `fast` `n + 1` times from the dummy *and* looping on `fast.next`. The gap becomes `n + 1`, so `slow` stops two nodes before the target: `[1,2,3,4,5], n = 2` returns `[1,2,4,5]`.
- Returning `head` instead of `dummy.next`. Works for every case except removing the head, where the old head is still returned with its `next` intact: `[1,2], n = 2` returns `[1,2]`.

## Related

- [easy/007-reverse-linked-list](../../easy/007-reverse-linked-list) is the basic pointer-rewiring drill.
- [easy/012-linked-list-cycle](../../easy/012-linked-list-cycle) uses two pointers at different *speeds* rather than a fixed gap.
- [medium/006-add-two-numbers](../006-add-two-numbers) uses the same dummy-head trick to avoid a special case for the first node.
- Review the [Two Pointers pattern](../../patterns/two-pointers.md) and its concept page.
