import unittest
from reorder_list import ListNode, Solution


def from_list(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head, limit=100):
    # limit guards against an accidental cycle turning a failing test into an infinite loop
    values = []
    while head is not None and len(values) < limit:
        values.append(head.val)
        head = head.next
    return values


class TestReorderList(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reorder_list(self):
        cases = [
            # (values, expected)
            ([1, 2, 3, 4, 5], [1, 5, 2, 4, 3]),     # the running example in the walkthrough
            ([1, 2, 3, 4], [1, 4, 2, 3]),           # even length: halves are [1,2] and [3,4]
            ([1], [1]),                             # single node, early return
            ([1, 2], [1, 2]),                       # two nodes: already in order
            ([1, 2, 3], [1, 3, 2]),                 # smallest case where a real swap happens
            ([1, 2, 3, 4, 5, 6], [1, 6, 2, 5, 3, 4]),
            ([7, 7, 7, 7, 7], [7, 7, 7, 7, 7]),     # duplicates: values identical, structure still rewired
            (list(range(1, 11)), [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]),
        ]

        for values, expected in cases:
            with self.subTest(values=values):
                head = from_list(values)
                self.solution.reorder_list(head)
                self.assertEqual(to_list(head), expected)

    def test_empty_list(self):
        self.assertIsNone(self.solution.reorder_list(None))


if __name__ == '__main__':
    unittest.main()
