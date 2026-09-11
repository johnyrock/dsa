import unittest
from linked_list_cycle import ListNode, Solution


def build(values, pos):
    # pos = index the tail's next should point back to, or -1 for no cycle.
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]


class TestLinkedListCycle(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_has_cycle(self):
        cases = [
            # (values, pos, expected)
            ([3, 2, 0, -4], 1, True),     # tail points back into the middle
            ([1, 2], 0, True),            # tail points back to head
            ([1], -1, False),             # single node, no cycle
            ([1], 0, True),               # single node pointing to itself
            ([], -1, False),              # empty list
            ([1, 2, 3, 4, 5], -1, False), # straight list
        ]

        for values, pos, expected in cases:
            with self.subTest(values=values, pos=pos):
                result = self.solution.has_cycle(build(values, pos))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
