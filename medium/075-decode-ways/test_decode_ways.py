import unittest
from decode_ways import Solution


class TestDecodeWays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_num_decodings(self):
        cases = [
            # (s, expected)
            ("226", 3),      # the running example: 2|26, 22|6, 2|2|6
            ("12", 2),       # 1|2 or 12
            ("06", 0),       # a leading zero cannot start a code
            ("0", 0),
            ("1", 1),        # single digit, the loop never runs
            ("10", 1),       # the 0 must pair with the 1; "1|0" is illegal
            ("27", 1),       # 27 > 26, so only 2|7
            ("2101", 1),     # 2|10|1 only; 21|0|1 is illegal
            ("100", 0),      # the second 0 has no partner
            ("11106", 2),    # 1|1|10|6 and 11|10|6; "06" is never a code
            ("1111111111", 89),  # every split is legal, so it is Fibonacci
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                self.assertEqual(self.solution.num_decodings(s), expected)


if __name__ == '__main__':
    unittest.main()
