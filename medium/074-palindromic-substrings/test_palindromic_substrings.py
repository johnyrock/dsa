import unittest
from palindromic_substrings import Solution


class TestPalindromicSubstrings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_count_substrings(self):
        cases = [
            # (s, expected)
            ("aaa", 6),          # the running example: "a" x3, "aa" x2, "aaa"
            ("abc", 3),          # only the single characters
            ("a", 1),            # smallest input
            ("aa", 3),           # "a", "a", "aa": needs the even expansion
            ("abba", 6),         # "a", "b", "b", "a", "bb", "abba"; skipping even centres gives 4
            ("abab", 6),         # "a", "b", "a", "b", "aba", "bab"
            ("racecar", 10),     # 7 singles + "cec", "aceca", "racecar"
            ("aaaa", 10),        # n(n+1)/2 for a uniform string
            ("abcd", 4),
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                self.assertEqual(self.solution.count_substrings(s), expected)


if __name__ == '__main__':
    unittest.main()
