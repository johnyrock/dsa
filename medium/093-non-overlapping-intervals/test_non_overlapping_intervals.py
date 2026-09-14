import unittest
from non_overlapping_intervals import Solution


class TestNonOverlappingIntervals(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_erase_overlap_intervals(self):
        cases = [
            # (intervals, expected)
            ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),   # the running example: drop [1,3]
            ([[1, 2], [1, 2], [1, 2]], 2),           # identical intervals, keep one
            ([[1, 2], [2, 3]], 0),                   # touching endpoints do not overlap
            ([[1, 100], [2, 3], [4, 5]], 1),         # sort-by-start would drop two; sort-by-end drops the long one
            ([[1, 5], [2, 3], [4, 6]], 1),
            ([[1, 2]], 0),                           # a single interval needs no removal
            ([[-5, -1], [-2, 0], [1, 3]], 1),        # negative coordinates
        ]

        for intervals, expected in cases:
            with self.subTest(intervals=intervals):
                result = self.solution.erase_overlap_intervals(intervals)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
