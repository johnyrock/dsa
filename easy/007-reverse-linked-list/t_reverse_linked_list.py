from reverse_linked_list import ListNode, reverse_list


def from_list(values):
    # Build the chain front to back. `dummy` is a throwaway node so there is
    # always something to hang the first real node off, and `tail` is the last
    # node added, so the next value goes straight into tail.next.
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next   # dummy is scaffolding, the real head is the node after it


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
