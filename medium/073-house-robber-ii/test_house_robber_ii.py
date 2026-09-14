import unittest
from house_robber_ii import Solution


class TestHouseRobberII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rob(self):
        cases = [
            # (nums, expected)
            ([2, 3, 2], 3),               # the running example: 2 + 2 is illegal on the circle, so 3
            ([1, 2, 3, 1], 4),            # 1 + 3, same as the linear answer
            ([1, 2, 3], 3),               # only one house can be taken among three in a ring
            ([1], 1),                     # single house: both slices are empty, must not return 0
            ([1, 2], 2),                  # two houses are neighbours both ways
            ([0, 0], 0),
            ([200, 3, 140, 20, 10], 340), # 200 + 140, first house in, last house out
            ([1, 3, 1, 3, 100], 103),     # 3 + 100, first house out
            ([5, 1, 1, 5], 6),            # linear robber says 10 (5 + 5), but houses 0 and 3 touch on the ring
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.rob(nums), expected)


if __name__ == '__main__':
    unittest.main()
