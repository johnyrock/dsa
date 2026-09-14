from remove_nth_node_from_end_of_list import ListNode, Solution

solution = Solution()


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


print(to_list(solution.remove_nth_from_end(from_list([1, 2, 3, 4, 5]), 2)))
print(to_list(solution.remove_nth_from_end(from_list([1]), 1)))
print(to_list(solution.remove_nth_from_end(from_list([1, 2]), 2)))
