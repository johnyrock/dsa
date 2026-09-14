from reorder_list import ListNode, Solution


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

for values in ([1, 2, 3, 4, 5], [1, 2, 3, 4], [1]):
    head = from_list(values)
    solution.reorder_list(head)
    print(values, "->", to_list(head))
