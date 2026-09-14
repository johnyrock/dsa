import unittest
from combination_sum_ii import Solution


class TestCombinationSumII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combination_sum2(self):
        cases = [
            # (candidates, target, expected as a set of sorted tuples)
            ([10, 1, 2, 7, 6, 1, 5], 8, {(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)}),   # the running example; [1,7] must appear once
            ([2, 5, 2, 1, 2], 5, {(1, 2, 2), (5,)}),                             # three 2s available, two used
            ([3], 8, set()),                                                     # no reuse, so nothing reaches 8
            ([1], 1, {(1,)}),                                                    # smallest input
            ([1, 1, 1, 1], 2, {(1, 1)}),                                         # four equal values, one combination
            ([4, 4, 2, 1, 4, 2, 2, 1, 3], 6, {(1, 1, 2, 2), (1, 1, 4), (1, 2, 3), (2, 2, 2), (2, 4)}),
        ]

        for candidates, target, expected in cases:
            with self.subTest(candidates=candidates, target=target):
                result = self.solution.combination_sum2(candidates, target)
                as_tuples = [tuple(sorted(c)) for c in result]
                self.assertEqual(len(as_tuples), len(set(as_tuples)))   # no duplicate combinations
                self.assertEqual(set(as_tuples), expected)
                for combo in result:
                    self.assertEqual(sum(combo), target)

    def test_does_not_reuse_an_index(self):
        # with backtrack(i) instead of backtrack(i + 1), [2, 2, 2, 2] would appear
        result = self.solution.combination_sum2([2, 3, 6, 7], 8)
        self.assertNotIn([2, 2, 2, 2], result)
        self.assertEqual(sorted(result), [[2, 6]])


if __name__ == '__main__':
    unittest.main()
