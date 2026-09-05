from merge_two_sorted_lists import ListNode, merge_two_lists


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


def test_merge_two_lists():
    cases = [
        # (list1, list2, expected)
        ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
        ([], [], []),                                       # both empty
        ([], [0], [0]),                                     # first list empty
        ([-9, 3], [], [-9, 3]),                             # second list empty
        ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),         # disjoint, whole tail attached at the end
        ([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6]),         # disjoint the other way round
        ([5, 5, 5], [5, 5], [5, 5, 5, 5, 5]),               # all values equal
        ([-3, -1, 0], [-2, 4], [-3, -2, -1, 0, 4]),         # negatives, interleaved
    ]

    failures = 0
    for l1, l2, expected in cases:
        result = to_list(merge_two_lists(from_list(l1), from_list(l2)))
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  list1={l1} list2={l2} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_merge_two_lists()
