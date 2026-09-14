import unittest
from longest_common_subsequence import Solution


class TestLongestCommonSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_longest_common_subsequence(self):
        cases = [
            # (text1, text2, expected)
            ("abcde", "ace", 3),          # the running example: a, c, e
            ("abc", "abc", 3),            # identical strings
            ("abc", "def", 0),            # nothing in common
            ("a", "a", 1),                # single matching character
            ("a", "b", 0),                # single mismatching character
            ("abcba", "abcbcba", 5),      # the whole shorter string is a subsequence of the longer
            ("bl", "yby", 1),             # only the b matches, and it is not at the same index
            ("ezupkr", "ubmrapg", 2),     # u, r in that order; a diagonal-only bug returns 1
            ("oxcpqrsvwf", "shmtulqrypy", 2),  # q, r
            ("abcdef", "acf", 3),         # match then skip then match then skip
            ("a" * 1000, "a" * 1000, 1000),    # upper constraint, must stay fast
        ]

        for text1, text2, expected in cases:
            with self.subTest(text1=text1, text2=text2):
                result = self.solution.longest_common_subsequence(text1, text2)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
