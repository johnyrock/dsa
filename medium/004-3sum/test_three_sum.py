import unittest
from three_sum import Solution


def normalize(triplets):
    # Triplet order and order within a triplet are unspecified, so canonicalise both.
    return sorted(sorted(t) for t in triplets)


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_three_sum(self):
        cases = [
            # (nums, expected)
            ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
            ([0, 1, 1], []),                                  # no zero-sum triplet
            ([0, 0, 0], [[0, 0, 0]]),                         # one triplet from three zeros
            ([0, 0, 0, 0], [[0, 0, 0]]),                      # still one triplet, not four
            ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),     # duplicate 1s form a valid pair once
            ([1, 2, 3], []),                                  # all positive, early break
            ([-3, -2, -1], []),                               # all negative
            ([-1, -1, -1, 2], [[-1, -1, 2]]),                 # three copies of the first value
            ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
            ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
             [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.three_sum(list(nums))
                self.assertEqual(normalize(result), normalize(expected))


if __name__ == '__main__':
    unittest.main()
