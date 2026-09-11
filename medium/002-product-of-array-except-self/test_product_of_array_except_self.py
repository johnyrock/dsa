import unittest
from product_of_array_except_self import Solution


class TestProductOfArrayExceptSelf(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_product_except_self(self):
        cases = [
            # (nums, expected)
            ([1, 2, 3, 4], [24, 12, 8, 6]),
            ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),       # one zero: only its own slot is non-zero
            ([2, 3], [3, 2]),                             # minimum length
            ([0, 0], [0, 0]),                             # two zeros: everything is zero
            ([0, 4, 5], [20, 0, 0]),                      # zero at the front
            ([4, 5, 0], [0, 0, 20]),                      # zero at the back
            ([1, 1, 1, 1], [1, 1, 1, 1]),                 # all ones
            ([-2, -3, 4], [-12, -8, 6]),                  # negatives, sign flips
            ([5, 1, 2], [2, 10, 5]),
            ([30, 30, 30, 30], [27000, 27000, 27000, 27000]),  # upper bound values
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                result = self.solution.product_except_self(list(nums))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
