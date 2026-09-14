import unittest
from jump_game_ii import Solution


class TestJumpGameII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_jump(self):
        cases = [
            # (nums, expected)
            ([2, 3, 1, 1, 4], 2),           # the running example: 0 -> 1 -> 4
            ([2, 3, 0, 1, 4], 2),
            ([0], 0),                       # already on the last index, no jump
            ([1, 2], 1),                    # one jump; looping to len(nums) would give 2
            ([1, 1, 1, 1], 3),              # forced single steps
            ([5, 1, 1, 1, 1, 1], 1),        # one big jump covers everything
            ([1, 2, 1, 1, 1], 3),           # 0 -> 1 -> 3 -> 4
            ([3, 2, 1, 1, 4], 2),           # jumping to the farthest index first is not always best but the count is
        ]

        for nums, expected in cases:
            with self.subTest(nums=nums):
                self.assertEqual(self.solution.jump(nums), expected)


if __name__ == '__main__':
    unittest.main()
