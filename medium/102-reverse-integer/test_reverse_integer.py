import unittest
from reverse_integer import Solution


class TestReverseInteger(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_reverse(self):
        cases = [
            # (x, expected)
            (-123, -321),             # the running example: the sign stays at the front
            (123, 321),
            (120, 21),                # a trailing zero disappears
            (0, 0),
            (5, 5),                   # single digit
            (1000000000, 1),          # many trailing zeros collapse
            (1534236469, 0),          # reverses to 9646324351, over INT_MAX
            (-1534236469, 0),
            (1463847412, 2147483641), # reverses to just under INT_MAX
            (2147483647, 0),          # INT_MAX itself reverses to 7463847412
            (-2147483648, 0),         # INT_MIN reverses to -8463847412
            (1056389759, 0),          # 9579836501 is over the limit
        ]
        for x, expected in cases:
            with self.subTest(x=x):
                self.assertEqual(self.solution.reverse(x), expected)


if __name__ == '__main__':
    unittest.main()
