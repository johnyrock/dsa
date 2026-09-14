from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    # Remove the n-th node from the end in a single pass using two pointers kept exactly n apart.
    def remove_nth_from_end(self, head: ListNode | None, n: int) -> ListNode | None:
        # A throwaway node in front of head means "the node before the one to delete" always exists, even when the head itself is deleted.
        dummy = ListNode(0, head)
        # Both pointers start on the dummy, not on head, so slow will stop one node BEFORE the target.
        fast = slow = dummy
        # Open a gap of n nodes between fast and slow. n <= length, so fast never runs off the list here.
        for _ in range(n):
            fast = fast.next
        # Walk both pointers until fast is on the last node. The gap is preserved, so slow is then n + 1 from the end: the predecessor of the target.
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        # Splice the target out by pointing its predecessor at its successor.
        slow.next = slow.next.next
        # dummy.next is the real head, which may be a different node than the one passed in if n == length.
        return dummy.next
