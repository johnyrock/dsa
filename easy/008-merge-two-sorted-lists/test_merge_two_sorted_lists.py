import unittest
from merge_two_sorted_lists import ListNode, Solution


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


class TestMergeTwoSortedLists(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_two_lists(self):
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

        for l1, l2, expected in cases:
            with self.subTest(list1=l1, list2=l2):
                result = to_list(self.solution.merge_two_lists(from_list(l1), from_list(l2)))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
