import unittest
from letter_combinations_of_a_phone_number import Solution


class TestLetterCombinationsOfAPhoneNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_letter_combinations(self):
        cases = [
            # (digits, expected)
            ("23", ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]),   # the running example, 3 × 3
            ("", []),                                                         # must be [] and not [""]
            ("2", ["a", "b", "c"]),                                           # single key
            ("7", ["p", "q", "r", "s"]),                                      # a four-letter key
            ("79", ["pw", "px", "py", "pz", "qw", "qx", "qy", "qz",
                    "rw", "rx", "ry", "rz", "sw", "sx", "sy", "sz"]),         # 4 × 4 = 16
        ]

        for digits, expected in cases:
            with self.subTest(digits=digits):
                result = self.solution.letter_combinations(digits)
                self.assertEqual(sorted(result), sorted(expected))
                self.assertEqual(len(result), len(set(result)))   # no duplicates

    def test_count_at_upper_constraint(self):
        # four digits of 4 letters each: 4^4 = 256 strings, every one of length 4
        result = self.solution.letter_combinations("7979")
        self.assertEqual(len(result), 256)
        self.assertTrue(all(len(s) == 4 for s in result))
        self.assertEqual(len(self.solution.letter_combinations("2222")), 81)


if __name__ == '__main__':
    unittest.main()
