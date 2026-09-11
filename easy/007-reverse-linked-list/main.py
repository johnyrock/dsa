from reverse_linked_list import ListNode, Solution


def from_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head: ListNode | None) -> list[int]:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


solution = Solution()

head = from_list([1, 2, 3, 4, 5])
print(to_list(solution.reverse_list(head)))
