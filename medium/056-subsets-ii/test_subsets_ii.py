import unittest
from subsets_ii import Solution


class TestSubsetsII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subsets_with_dup(self):
        cases = [
            # (nums, expected set of subsets as sorted tuples)
            ([1, 2, 2], {(), (1,), (2,), (1, 2), (2, 2), (1, 2, 2)}),          # the running example: 6, not 8
            ([0], {(), (0,)}),
            ([2, 2, 2], {(), (2,), (2, 2), (2, 2, 2)}),                        # all equal: one subset per count
            ([4, 4, 4, 1], {(), (1,), (4,), (1, 4), (4, 4), (1, 4, 4), (4, 4, 4), (1, 4, 4, 4)}),   # unsorted input must be sorted first
            ([1, 2, 3], {(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)}),                  # no duplicates: plain power set
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.subsets_with_dup(nums)
                self.assertEqual(len(result), len(expected))                   # the whole point: no repeated subsets
                self.assertEqual({tuple(sorted(s)) for s in result}, expected)

    def test_second_copy_is_still_allowed(self):
        # skipping every repeated value (dropping the i > start condition) would lose [2, 2]
        result = self.solution.subsets_with_dup([2, 1, 2])
        self.assertIn([2, 2], result)
        self.assertIn([1, 2, 2], result)


if __name__ == '__main__':
    unittest.main()
