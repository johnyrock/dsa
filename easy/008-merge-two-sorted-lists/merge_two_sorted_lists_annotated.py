# Define the node type for a singly linked list. On LeetCode this class is given to you in the editor.
class ListNode:
    # Build a node from a value and a pointer to the next node. Both default so ListNode() alone makes a placeholder.
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        # Store the value carried by this node.
        self.val = val
        # Store the link to the following node, or None if this is the last one.
        self.next = next


class Solution:
    # Define the function that takes the heads of two already-sorted lists and returns the head of the merged list.
    def merge_two_lists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # Create a throwaway node that sits in front of the real result. It means we never need a special case for attaching the very first node.
        dummy = ListNode()
        # Keep a pointer to the last node of the merged list so far. It starts at the dummy, since nothing is attached yet.
        tail = dummy
        # Keep going while both lists still have nodes. The moment either runs out, the rest of the other one is already sorted and can be attached wholesale.
        while list1 and list2:
            # Both lists are sorted, so the smallest node not yet merged is whichever head is smaller. Using <= keeps equal values in their original order, which makes the merge stable.
            if list1.val <= list2.val:
                # Splice list1's head onto the end of the merged list. No new node is allocated, we just relink the existing one.
                tail.next = list1
                # Step list1 forward to its next node, since its head has now been consumed.
                list1 = list1.next
            # Otherwise list2's head is strictly smaller, so it is the one that goes next.
            else:
                # Splice list2's head onto the end of the merged list.
                tail.next = list2
                # Step list2 forward past the node we just consumed.
                list2 = list2.next
            # Whichever node we just attached is now the last one, so move the tail pointer onto it.
            tail = tail.next
        # One list is now empty and the other may still have nodes. Those are all larger than everything merged so far and already sorted, so a single link attaches them all. If both are empty this harmlessly sets None.
        tail.next = list1 or list2
        # The dummy was only ever a handle, so the real head of the merged list is the node after it.
        return dummy.next
