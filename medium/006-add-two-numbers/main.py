from add_two_numbers import ListNode, Solution


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

total = solution.add_two_numbers(from_list([2, 4, 3]), from_list([5, 6, 4]))
print(to_list(total))  # 342 + 465 = 807, stored least significant digit first
