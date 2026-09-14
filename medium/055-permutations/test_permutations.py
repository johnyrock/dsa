import unittest
from itertools import permutations
from permutations import Solution


class TestPermutations(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_permute(self):
        cases = [
            # (nums, expected set of orderings)
            ([1, 2, 3], {(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)}),   # the running example in the walkthrough
            ([0, 1], {(0, 1), (1, 0)}),
            ([1], {(1,)}),                                                                      # a single element has one ordering
            ([-1, 0, 5, 9], set(permutations([-1, 0, 5, 9]))),                                  # 4! = 24, negatives are ordinary values
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.permute(nums)
                self.assertEqual(len(result), len(expected))                                    # no duplicates
                self.assertEqual({tuple(p) for p in result}, expected)

    def test_count_is_factorial(self):
        # forgetting `used[i] = False` on the way back up leaves far fewer than n! results
        result = self.solution.permute(list(range(6)))
        self.assertEqual(len(result), 720)
        self.assertEqual(len({tuple(p) for p in result}), 720)

    def test_copies_are_independent(self):
        # a missing path[:] copy makes every entry the same (finally empty) list
        result = self.solution.permute([1, 2])
        self.assertIn([1, 2], result)
        self.assertIn([2, 1], result)


if __name__ == '__main__':
    unittest.main()
