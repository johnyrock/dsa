import unittest
from target_sum import Solution


class TestTargetSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_target_sum_ways(self):
        cases = [
            # (nums, target, expected)
            ([1, 1, 1, 1, 1], 3, 5),         # choose which one of the five gets the minus: C(5,1) = 5
            ([1], 1, 1),                     # +1
            ([1], 2, 0),                     # target beyond the total
            ([1], -1, 1),                    # -1; negative targets are fine
            ([1, 2, 3], 7, 0),               # total is 6, unreachable
            ([1, 2, 3], 6, 1),               # all plus
            ([1, 2, 3], 0, 2),               # +1+2-3 and -1-2+3
            ([1, 2, 3], 1, 0),               # total + target is odd, no subset can be 3.5
            ([0, 0, 0, 0, 0, 0, 0, 0, 1], 1, 256),  # zeros can take either sign: 2^8
            ([100], -200, 0),                # single number, target twice its size
            ([1, 1, 1, 1, 1], 5, 1),         # all plus is the only way
            ([1, 1, 1, 1, 1], -3, 5),        # mirror of the running example
            ([2, 1, 1, 2], 2, 3),            # plus-side sum 4: {2,2}, {2,1,1} twice; an upward inner loop over-counts
        ]

        for nums, target, expected in cases:
            with self.subTest(nums=nums, target=target):
                result = self.solution.find_target_sum_ways(list(nums), target)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
