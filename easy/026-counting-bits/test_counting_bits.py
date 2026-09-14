import unittest
from counting_bits import Solution


class TestCountingBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_counting_bits(self):
        cases = [
            (0, [0]),
            (2, [0, 1, 1]),
            (5, [0, 1, 1, 2, 1, 2]),
            (8, [0, 1, 1, 2, 1, 2, 2, 3, 1]),  # power of two resets to one bit
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(self.solution.count_bits(value), expected)


if __name__ == '__main__':
    unittest.main()
