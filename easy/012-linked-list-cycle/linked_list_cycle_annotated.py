from __future__ import annotations


class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    def has_cycle(self, head: ListNode | None) -> bool:
        # Two pointers start together at the head.
        slow = fast = head
        # Stop if fast (or its next) falls off the end — that means no cycle.
        while fast is not None and fast.next is not None:
            # Slow moves one node per step, fast moves two.
            slow = slow.next
            fast = fast.next.next
            # If there is a cycle, fast eventually laps slow and they land on the
            # same node. If there is no cycle, fast reaches None first and the
            # loop condition above stops us before this line is even reached again.
            if slow is fast:
                return True
        return False
