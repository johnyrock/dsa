class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None) -> None:
        self.val = val
        self.next = next


class Solution:
    # Define the function that takes two reversed-digit lists and returns their sum as a reversed-digit list.
    def add_two_numbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        # A dummy node in front of the result means the first digit is appended exactly like every other one.
        dummy = ListNode()
        tail = dummy
        # The carry from the previous column, 0 or 1. Starts at 0 because there is nothing to the right of the ones digit.
        carry = 0
        # Keep going while either list has digits left OR a carry is pending. The carry clause is what produces the extra leading digit in 999 + 1 = 1000.
        while l1 or l2 or carry:
            # Start the column with the carry, then add whichever digits exist. A list that has run out contributes nothing, which is the same as padding it with zeros.
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            # Split the column sum into the digit that stays and the carry that moves left. total is at most 9 + 9 + 1 = 19, so carry is 0 or 1.
            carry, digit = divmod(total, 10)
            # Append the digit. Because the lists are least-significant first, appending in order builds the answer least-significant first too.
            tail.next = ListNode(digit)
            tail = tail.next
        # Skip the dummy and hand back the real head.
        return dummy.next
