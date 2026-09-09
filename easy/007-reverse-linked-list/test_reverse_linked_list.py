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


def to_list(head, limit=10000):
    values = []
    while head is not None and len(values) < limit:
        values.append(head.val)
        head = head.next
    return values


def test_reverse_list():
    cases = [
        # (values, expected)
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),                                   # empty list, head is None
        ([7], [7]),                                 # single node, unchanged
        ([1, 1, 2, 2], [2, 2, 1, 1]),               # duplicate values
        ([-5000, 0, 5000], [5000, 0, -5000]),       # negatives and bounds
        (list(range(10)), list(range(9, -1, -1))),  # longer list
    ]

    failures = 0
    for values, expected in cases:
        result = to_list(reverse_list(from_list(values)))
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  values={values} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_reverse_list()
