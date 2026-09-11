import unittest
from insert_interval import Solution


class TestInsertInterval(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_insert(self):
        cases = [
            # (intervals, new_interval, expected)
            ([[1, 3], [6, 9]], [2, 5], [[1, 5], [6, 9]]),
            ([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8], [[1, 2], [3, 10], [12, 16]]),
            ([], [5, 7], [[5, 7]]),                            # empty list
            ([[1, 5]], [2, 3], [[1, 5]]),                      # fully contained
            ([[1, 5]], [6, 8], [[1, 5], [6, 8]]),              # no overlap, after
            ([[1, 5]], [-2, 0], [[-2, 0], [1, 5]]),            # no overlap, before
            ([[1, 5]], [0, 6], [[0, 6]]),                      # new interval swallows the old one
        ]

        for intervals, new_interval, expected in cases:
            with self.subTest(intervals=intervals, new_interval=new_interval):
                result = self.solution.insert(intervals, new_interval)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
