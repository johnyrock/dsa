import unittest
from remove_nth_node_from_end_of_list import ListNode, Solution


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head, limit=10000):
    values = []
    while head is not None and len(values) < limit:
        values.append(head.val)
        head = head.next
    return values


class TestRemoveNthNodeFromEndOfList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_remove_nth_from_end(self):
        cases = [
            # (values, n, expected)
            ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),   # the running example in the walkthrough
            ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),   # remove the tail
            ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),   # remove the head; only the dummy makes this uniform
            ([1], 1, []),                         # single node, list becomes empty
            ([1, 2], 2, [2]),                     # remove head of a two-node list
            ([1, 2], 1, [1]),                     # remove tail of a two-node list
            ([7, 7, 7], 2, [7, 7]),               # duplicate values, position not value decides
        ]

        for values, n, expected in cases:
            with self.subTest(values=values, n=n):
                result = self.solution.remove_nth_from_end(from_list(values), n)
                self.assertEqual(to_list(result), expected)


if __name__ == '__main__':
    unittest.main()
