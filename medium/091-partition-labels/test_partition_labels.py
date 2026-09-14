import unittest
from partition_labels import Solution


class TestPartitionLabels(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition_labels(self):
        cases = [
            # (s, expected)
            ("ababcbacadefegdehijhklij", [9, 7, 8]),  # the running example
            ("eccbbbbdec", [10]),                     # the first letter's last occurrence is the final index
            ("a", [1]),
            ("abc", [1, 1, 1]),                       # no repeats, every letter is its own part
            ("abca", [4]),                            # a repeat at the far end swallows everything
            ("abcab", [5]),                           # b reappears at the very end, so a's last index (3) cannot close a part
            ("aabb", [2, 2]),
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                result = self.solution.partition_labels(s)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
