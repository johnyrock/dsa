import unittest
from longest_palindromic_substring import Solution


class TestLongestPalindromicSubstring(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_palindrome(self):
        cases = [
            # (s, set of accepted answers)
            ("babad", {"bab", "aba"}),
            ("cbbd", {"bb"}),                          # even length
            ("a", {"a"}),                              # single character
            ("ac", {"a", "c"}),                        # no repeat, any single character
            ("aaaa", {"aaaa"}),                        # whole string, even
            ("racecar", {"racecar"}),                  # whole string, odd
            ("abacdfgdcaba", {"aba"}),                 # two equal candidates that are the same text
            ("forgeeksskeegfor", {"geeksskeeg"}),      # long even palindrome in the middle
            ("bananas", {"anana"}),
            ("noonabbad", {"noon", "abba"}),           # two ties of length 4
            ("abcda", {"a", "b", "c", "d"}),           # nothing longer than 1
            ("xabbay", {"abba"}),                      # even palindrome not at an edge
            ("12321abc", {"12321"}),                   # digits count as characters
        ]

        for s, accepted in cases:
            with self.subTest(s=s):
                result = self.solution.longest_palindrome(s)
                self.assertIn(result, accepted)


if __name__ == '__main__':
    unittest.main()
