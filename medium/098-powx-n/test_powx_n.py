import unittest
from powx_n import Solution


class TestPowxN(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_my_pow(self):
        cases = [
            # (x, n, expected)
            (2.0, 10, 1024.0),              # the running example: 1010 in binary
            (2.1, 3, 9.261),
            (2.0, -2, 0.25),                # negative exponent: reciprocal
            (2.0, 0, 1.0),                  # n = 0 must give 1, not x
            (0.0, 5, 0.0),
            (1.0, 2147483647, 1.0),         # upper constraint, must stay fast
            (2.0, -2147483648, 0.0),        # lower constraint: -n must not overflow (Python ints do not)
            (-2.0, 3, -8.0),                # odd power keeps the sign
            (-2.0, 2, 4.0),                 # even power drops the sign
            (0.5, 2, 0.25),
        ]
        for x, n, expected in cases:
            with self.subTest(x=x, n=n):
                self.assertAlmostEqual(self.solution.my_pow(x, n), expected, places=5)


if __name__ == '__main__':
    unittest.main()
