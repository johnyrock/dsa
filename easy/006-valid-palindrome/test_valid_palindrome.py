import unittest
from valid_palindrome import Solution


class TestValidPalindrome(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_palindrome(self):
        cases = [
            # (s, expected)
            ("A man, a plan, a canal: Panama", True),
            ("No 'x' in Nixon", True),           # mixed case plus apostrophes
            ("race a car", False),               # "raceacar" is not a palindrome
            ("", True),                          # empty string
            (" ", True),                         # only whitespace, nothing to compare
            (".,;'", True),                      # only punctuation, nothing to compare
            ("12321", True),                     # digits count as alphanumeric
            ("0P", False),                       # '0' and 'P' are not equal after lowering
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                result = self.solution.is_palindrome(s)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
