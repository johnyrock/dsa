import unittest
from combination_sum import Solution


class TestCombinationSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_combination_sum(self):
        cases = [
            # (candidates, target, expected set of combinations as sorted tuples)
            ([2, 3, 6, 7], 7, {(2, 2, 3), (7,)}),                              # the running example in the walkthrough
            ([2, 3, 5], 8, {(2, 2, 2, 2), (2, 3, 3), (3, 5)}),                 # one candidate reused four times
            ([2], 1, set()),                                                   # nothing fits: empty answer
            ([1], 2, {(1, 1)}),                                                # reuse is required, not optional
            ([7, 3, 2], 7, {(2, 2, 3), (7,)}),                                 # unsorted input must give the same answer
            ([3, 5], 4, set()),                                                # overshoots every way
        ]

        for candidates, target, expected in cases:
            with self.subTest(candidates=candidates, target=target):
                result = self.solution.combination_sum(candidates, target)
                self.assertEqual(len(result), len(expected))                   # no duplicates such as [2,3] and [3,2]
                self.assertEqual({tuple(sorted(c)) for c in result}, expected)
                for combo in result:
                    self.assertEqual(sum(combo), target)

    def test_does_not_mutate_input(self):
        candidates = [7, 3, 2]
        self.solution.combination_sum(candidates, 7)
        self.assertEqual(candidates, [7, 3, 2])


if __name__ == '__main__':
    unittest.main()
