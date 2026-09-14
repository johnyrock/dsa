import unittest
from jump_game import Solution


class TestJumpGame(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_jump(self):
        cases = [
            # (nums, expected)
            ([2, 3, 1, 1, 4], True),        # the running example in the walkthrough
            ([3, 2, 1, 0, 4], False),       # every path lands on the 0 at index 3
            ([0], True),                    # single element: already standing on the last index
            ([1, 0], True),                 # a 0 on the last index is fine
            ([0, 1], False),                # stuck on index 0
            ([2, 0, 0], True),              # reach without max() would drop to 1 here and fail
            ([2, 5, 0, 0], True),           # a big jump early makes the zeros irrelevant
            ([1, 1, 1, 1, 0], True),        # exact steps all the way, last index reached
            ([1, 1, 1, 0, 1], False),
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.can_jump(nums), expected)


if __name__ == '__main__':
    unittest.main()
