import unittest
from climbing_stairs import Solution


class TestClimbingStairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_climb_stairs(self):
        cases = [
            # (n, expected)
            (1, 1),                 # base case, only one move fits
            (2, 2),                 # base case, 1+1 or 2
            (3, 3),                 # first case the loop actually runs
            (4, 5),
            (5, 8),                 # the running example in the walkthrough
            (6, 13),                # off-by-one in the loop would give 21 here
            (10, 89),
            (45, 1836311903),       # upper constraint, must stay fast
        ]

        for n, expected in cases:
            with self.subTest(n=n):
                result = self.solution.climb_stairs(n)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
