# Notes

## Attempts

- 2026-09-12: Folder generated as reference material, not solved independently. First review should be a from-scratch re-solve: delete `linked_list_cycle.py`, keep the tests, write it again.

## Key insight

Two pointers move through the list at different speeds: slow steps one node at a time, fast steps two. If there is no cycle, fast reaches the end first and the loop stops. If there is a cycle, fast is effectively lapping slow inside a loop of fixed length — the gap between them shrinks by one each step, so fast must eventually land exactly on slow.

## Complexity

- Time: O(n). In the worst case fast laps the cycle length once before catching slow.
- Space: O(1) — only two pointers, no visited set.

## Mistakes to watch for

- Checking `fast is not None` but not `fast.next is not None` before advancing `fast.next.next` — crashes with an `AttributeError` on a list of even length with no cycle.
- Using `==` instead of `is` to compare nodes. `ListNode.__eq__` isn't defined here, so `==` falls back to identity anyway, but relying on that is fragile if `__eq__` is ever added.
- Starting `fast` one step ahead of `slow` "to be safe" — unnecessary, and makes the self-loop case (`pos = 0`, a single node pointing to itself) easy to get wrong.

## Related

- Linked List Cycle II (medium, LeetCode #142) finds the start of the cycle using the same two pointers plus a second phase.
- Middle of the Linked List (easy, LeetCode #876) is the same slow/fast skeleton used to find a midpoint instead of a cycle.
- Happy Number (easy, LeetCode #202) applies the identical cycle-detection idea to a sequence of digit-square sums instead of a linked list.
