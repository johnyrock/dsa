import unittest
from copy_list_with_random_pointer import Node, Solution


def build(pairs):
    # pairs = [[val, random_index or None], ...] in list order.
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, rnd) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[rnd] if rnd is not None else None
    return nodes[0] if nodes else None


def serialize(head):
    nodes, index, node = [], {}, head
    while node is not None:
        index[node] = len(nodes)
        nodes.append(node)
        node = node.next
    return [[n.val, index[n.random] if n.random is not None else None] for n in nodes]


def all_nodes(head):
    out = []
    while head is not None:
        out.append(head)
        head = head.next
    return out


class TestCopyListWithRandomPointer(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_copy_random_list(self):
        cases = [
            # (pairs,)
            ([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],),   # the running example in the walkthrough
            ([[1, 1], [2, 1]],),                                  # both randoms hit the same node
            ([[3, None], [3, 0], [3, None]],),                    # equal values; copy must key on identity, not val
            ([[5, 0]],),                                          # single node pointing at itself
            ([[1, None]],),                                       # single node, random null
            ([],),                                                # empty list -> None
            ([[1, 2], [2, 0], [3, 1]],),                          # every random points somewhere else
        ]

        for (pairs,) in cases:
            with self.subTest(pairs=pairs):
                original = build(pairs)
                copy = self.solution.copy_random_list(original)
                self.assertEqual(serialize(copy), pairs)
                # deep copy: no node object may be shared between the two lists
                originals = set(map(id, all_nodes(original)))
                for node in all_nodes(copy):
                    self.assertNotIn(id(node), originals)
                    if node.random is not None:
                        self.assertNotIn(id(node.random), originals)
                # the original must be untouched
                self.assertEqual(serialize(original), pairs)


if __name__ == '__main__':
    unittest.main()
