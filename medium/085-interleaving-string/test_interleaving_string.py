import unittest
from interleaving_string import Solution


class TestInterleavingString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_interleave(self):
        cases = [
            # (s1, s2, s3, expected)
            ("aabcc", "dbbca", "aadbbcbcac", True),   # the running example: aa + d + bb + c + bc + a + c
            ("aabcc", "dbbca", "aadbbbaccc", False),  # same letters, wrong order
            ("", "", "", True),                       # three empty strings
            ("", "b", "b", True),                     # one string empty
            ("a", "", "a", True),
            ("a", "b", "ab", True),
            ("a", "b", "ba", True),                   # either may go first
            ("a", "b", "aa", False),                  # right length, wrong letters
            ("abc", "def", "abcde", False),           # lengths do not add up
            ("ab", "ab", "abab", True),               # equal strings
            ("aa", "ab", "abaa", True),               # a(s1) b(s2) a(s1) a(s2): which string each a comes from matters
            ("a", "aa", "aaa", True),
            ("aab", "aac", "aaaabc", True),           # a(s1) a(s1) a(s2) a(s2) b(s1) c(s2); a greedy "prefer s1" scan wrongly says False
            ("aab", "aac", "aabaac", True),           # take s1 whole, then s2 whole
            ("abc", "abd", "abcdab", False),          # same letters, but c and d each need their own "ab" first and s3 has only one "ab" before them
        ]

        for s1, s2, s3, expected in cases:
            with self.subTest(s1=s1, s2=s2, s3=s3):
                result = self.solution.is_interleave(s1, s2, s3)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
