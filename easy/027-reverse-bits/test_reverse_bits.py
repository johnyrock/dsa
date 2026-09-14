import unittest
from reverse_bits import Solution


class TestReverseBits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse_bits(self):
        cases = [
            (0b00000010100101000001111010011100, 964176192),
            (0b11111111111111111111111111111101, 3221225471),
            (0, 0),
            (1, 2147483648),                  # the low bit becomes the high bit
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(self.solution.reverse_bits(value), expected)


if __name__ == '__main__':
    unittest.main()
