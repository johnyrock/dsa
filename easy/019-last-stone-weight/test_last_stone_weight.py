import unittest
from last_stone_weight import Solution


class TestLastStoneWeight(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_last_stone_weight(self):
        cases = [
            ([2, 7, 4, 1, 8, 1], 1),
            ([1], 1),
            ([2, 2], 0),                     # equal stones both vanish
            ([10, 4, 2, 10], 2),
            ([], 0),                         # defensive empty input
        ]
        for stones, expected in cases:
            with self.subTest(stones=stones):
                self.assertEqual(self.solution.last_stone_weight(stones), expected)


if __name__ == '__main__':
    unittest.main()
