import unittest
from add_two_numbers import ListNode, Solution


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


class TestAddTwoNumbers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_add_two_numbers(self):
        cases = [
            # (l1, l2, expected)
            ([2, 4, 3], [5, 6, 4], [7, 0, 8]),                        # 342 + 465 = 807
            ([0], [0], [0]),                                          # zero plus zero
            ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),  # different lengths, carry chain
            ([5], [5], [0, 1]),                                       # single digits producing a new digit
            ([1], [9, 9, 9], [0, 0, 0, 1]),                           # carry ripples through the longer list
            ([9, 9], [1], [0, 0, 1]),                                 # same, longer list first
            ([1, 8], [0], [1, 8]),                                    # adding zero changes nothing
            ([2, 4, 3], [5, 6], [7, 0, 4]),                           # 342 + 65 = 407
            ([0, 1], [0, 1], [0, 2]),                                 # 10 + 10 = 20, zero in the ones place
            ([9] * 100, [1], [0] * 100 + [1]),                        # upper bound length with a full carry chain
        ]

        for a, b, expected in cases:
            with self.subTest(l1=a, l2=b):
                result = to_list(self.solution.add_two_numbers(from_list(a), from_list(b)))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
