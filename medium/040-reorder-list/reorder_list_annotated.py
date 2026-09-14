from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    # Rewire the list in place from L0 -> L1 -> ... -> Ln into L0 -> Ln -> L1 -> Ln-1 -> ... Nothing is returned; the caller's head still points at the first node.
    def reorder_list(self, head: ListNode | None) -> None:
        # Zero or one node is already in the required order, and the middle-finding loop below would dereference None on an empty list.
        if head is None or head.next is None:
            return
        # Phase 1: find the end of the first half. fast moves two hops per slow hop, so when fast runs out slow is at the middle.
        slow = fast = head
        # Checking fast.next.next (not fast.next) stops slow on the LAST node of the first half for even lengths: [1,2,3,4] leaves slow at 2, so the halves are [1,2] and [3,4].
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Phase 2: cut the list after slow. The first half must end in None, or the merge step will walk past it into nodes that have already been rewired.
        second = slow.next
        slow.next = None
        # Reverse the second half in place with the usual three-pointer loop; prev ends up as the new head of the reversed half.
        prev = None
        while second is not None:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        # Phase 3: weave the two halves together, alternating one node from each. The first half is never shorter than the second, so looping on second is enough.
        first, second = head, prev
        while second is not None:
            # Save both successors before touching any pointer: the two assignments below overwrite them.
            first_next, second_next = first.next, second.next
            # Splice the second-half node right after the first-half node.
            first.next = second
            second.next = first_next
            # Advance both cursors to the nodes that have not been woven yet.
            first, second = first_next, second_next
