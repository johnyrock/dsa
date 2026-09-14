import unittest
from happy_number import Solution


class TestHappyNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_happy_number(self):
        cases = [
            (19, True),
            (2, False),
            (1, True),                         # already at the success state
            (7, True),
            (4, False),                        # a member of the non-happy cycle
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(self.solution.is_happy(value), expected)


if __name__ == '__main__':
    unittest.main()
