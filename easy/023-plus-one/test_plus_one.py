import unittest
from plus_one import Solution


class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_plus_one(self):
        cases = [
            ([1, 2, 3], [1, 2, 4]),
            ([4, 3, 2, 1], [4, 3, 2, 2]),
            ([9], [1, 0]),
            ([9, 9], [1, 0, 0]),              # carry creates a new digit
            ([1, 2, 9], [1, 3, 0]),
        ]
        for digits, expected in cases:
            with self.subTest(digits=digits):
                self.assertEqual(self.solution.plus_one(digits), expected)


if __name__ == '__main__':
    unittest.main()
