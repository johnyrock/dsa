import unittest
import bisect
from random_pick_with_weight import Solution


class TestRandomPickWithWeight(unittest.TestCase):
    def test_prefix_sums(self):
        # The randomness itself isn't worth testing; the prefix-sum
        # construction and the boundary behaviour of bisect_left are.
        cases = [
            ([1], [1]),
            ([1, 3], [1, 4]),
            ([1, 3, 2], [1, 4, 6]),
            ([5, 5, 5, 5], [5, 10, 15, 20]),
        ]

        for w, expected_prefix in cases:
            with self.subTest(w=w):
                solution = Solution(w)
                self.assertEqual(solution.prefix, expected_prefix)
                self.assertEqual(solution.total, expected_prefix[-1])

    def test_boundaries_map_to_expected_index(self):
        # w = [1, 3] -> prefix = [1, 4]. target=1 must land on index 0
        # (the only point owned by weight 1); targets 2..4 must land on index 1.
        solution = Solution([1, 3])
        self.assertEqual(bisect.bisect_left(solution.prefix, 1), 0)
        for target in (2, 3, 4):
            with self.subTest(target=target):
                self.assertEqual(bisect.bisect_left(solution.prefix, target), 1)

    def test_pick_index_stays_in_range(self):
        solution = Solution([3, 1, 2, 4])
        for _ in range(200):
            index = solution.pick_index()
            self.assertGreaterEqual(index, 0)
            self.assertLess(index, 4)


if __name__ == '__main__':
    unittest.main()
