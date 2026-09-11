# Define the node type the list is built from. A singly linked list is just a chain of these, each one holding a value and a reference to the next node.
class ListNode:
    # The constructor takes the value stored in this node and the node that follows it. Both have defaults so a lone node can be made with ListNode() or ListNode(5).
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        # Store the payload of this node.
        self.val = val
        # Store the link to the next node, or None if this node is the tail.
        self.next = next


class Solution:
    # Define the function that takes the head of a singly linked list and returns the head of the reversed list.
    def reverse_list(self, head: ListNode | None) -> ListNode | None:
        # Track the node we have already reversed, which becomes the node the current one should point back to. It starts as None because the old head must end up pointing at nothing.
        prev = None
        # Track the node we are working on right now, starting at the head of the list.
        curr = head
        # Keep going while there is still a node to rewire. When curr falls off the end this is False and the loop stops.
        while curr:
            # Save the rest of the list before we touch curr.next. The very next line overwrites that link, so without this line the tail would be unreachable.
            next_node = curr.next
            # Flip this node's arrow so it points backwards at the part of the list we have already reversed.
            curr.next = prev
            # The node we just flipped is now the front of the reversed part, so it becomes prev for the next iteration.
            prev = curr
            # Step forward using the pointer we saved, since curr.next no longer leads that way.
            curr = next_node
        # When the loop ends curr is None and prev is the last node we flipped, which is the new head.
        return prev
