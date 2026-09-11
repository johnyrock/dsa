import unittest
from serialize_and_deserialize_binary_tree import Codec, TreeNode


def build_tree(values):
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root


def tree_to_list(root):
    if root is None:
        return []
    values = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values


class TestSerializeAndDeserializeBinaryTree(unittest.TestCase):
    def setUp(self):
        self.codec = Codec()

    def test_round_trip(self):
        cases = [
            [1, 2, 3, None, None, 4, 5],
            [],
            [1],
            [1, 2],
            [1, None, 2, None, 3, None, 4],   # right-skewed chain
            [5, 4, 7, 3, None, 2, None, -1, None, 9],
        ]

        for values in cases:
            with self.subTest(values=values):
                original = build_tree(values)
                data = self.codec.serialize(original)
                restored = self.codec.deserialize(data)
                self.assertEqual(tree_to_list(restored), tree_to_list(original))


if __name__ == '__main__':
    unittest.main()
