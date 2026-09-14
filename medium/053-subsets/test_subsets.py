import unittest
from subsets import Solution


class TestSubsets(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsets(self):
        cases = [
            # (nums, expected set of subsets as sorted tuples)
            ([1, 2, 3], {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}),   # the running example in the walkthrough
            ([0], {(), (0,)}),                                                       # single element: empty set and itself
            ([], {()}),                                                              # no elements: only the empty subset
            ([4, 7], {(), (4,), (7,), (4, 7)}),
            ([-1, 5], {(), (-1,), (5,), (-1, 5)}),                                   # negatives are ordinary values
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.subsets(nums)
                self.assertEqual(len(result), len(expected))                         # no duplicates
                self.assertEqual({tuple(sorted(s)) for s in result}, expected)

    def test_count_is_power_of_two(self):
        # a missing `start` argument would produce permutations of every size instead
        for n in (4, 6, 10):
            with self.subTest(n=n):
                result = self.solution.subsets(list(range(n)))
                self.assertEqual(len(result), 2 ** n)
                self.assertEqual(len({tuple(s) for s in result}), 2 ** n)

    def test_copies_are_independent(self):
        # a missing path[:] copy makes every entry the same (finally empty) list
        result = self.solution.subsets([1, 2])
        self.assertIn([1, 2], result)
        self.assertIn([], result)


if __name__ == '__main__':
    unittest.main()
