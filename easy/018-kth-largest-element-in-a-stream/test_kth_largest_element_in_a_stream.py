import unittest
from kth_largest_element_in_a_stream import KthLargest


class TestKthLargestElementInAStream(unittest.TestCase):
    def test_kth_largest_element_in_a_stream(self):
        stream = KthLargest(3, [4, 5, 8, 2])
        cases = [
            (3, 4),
            (5, 5),
            (10, 5),
            (9, 8),
            (4, 8),                         # smaller values do not displace the top k
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(stream.add(value), expected)

    def test_k_one(self):
        stream = KthLargest(1, [])
        self.assertEqual(stream.add(-3), -3)
        self.assertEqual(stream.add(2), 2)


if __name__ == '__main__':
    unittest.main()
