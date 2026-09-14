import unittest
from palindrome_partitioning import Solution


class TestPalindromePartitioning(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_partition(self):
        cases = [
            # (s, expected as a set of tuples)
            ("aab", {("a", "a", "b"), ("aa", "b")}),                              # the running example
            ("a", {("a",)}),                                                       # single character
            ("aba", {("a", "b", "a"), ("aba",)}),                                  # whole string is a palindrome
            ("abc", {("a", "b", "c")}),                                            # no multi-character palindromes at all
            ("aaa", {("a", "a", "a"), ("a", "aa"), ("aa", "a"), ("aaa",)}),        # every cut set works: 2^(n-1) partitions
            ("abba", {("a", "b", "b", "a"), ("a", "bb", "a"), ("abba",)}),         # "ab", "abb", "bba", "ba" are rejected
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                result = self.solution.partition(s)
                as_tuples = [tuple(p) for p in result]
                self.assertEqual(len(as_tuples), len(set(as_tuples)))   # no duplicates
                self.assertEqual(set(as_tuples), expected)
                for pieces in result:
                    self.assertEqual("".join(pieces), s)                # pieces cover s exactly, in order

    def test_all_same_letter_count(self):
        # every one of the 2^(n-1) cut sets is valid when all characters match
        self.assertEqual(len(self.solution.partition("a" * 10)), 2 ** 9)


if __name__ == '__main__':
    unittest.main()
