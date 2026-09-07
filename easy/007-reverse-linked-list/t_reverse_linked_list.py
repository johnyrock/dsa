from reverse_linked_list import ListNode, reverse_list


def from_list(values):
    head = None
    for v in reversed(values):
        head = ListNode(v, head)
    return head


def to_list(head):
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


cases = [
    # values, expected
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([1], [1]),
    ([], []),
]

def test_reverse_list(cases):
    for values, expected in cases:
        result = to_list(reverse_list(from_list(values)))
        assert result == expected, f'{values!r} -> FAIL'
        print(f'{values!r} -> PASS')

test_reverse_list(cases)
