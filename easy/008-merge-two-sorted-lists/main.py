from merge_two_sorted_lists import ListNode, Solution


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

merged = solution.merge_two_lists(from_list([1, 2, 4]), from_list([1, 3, 4]))
print(to_list(merged))
