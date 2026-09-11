import unittest
from valid_anagram import Solution


class TestValidAnagram(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_anagram(self):
        cases = [
            # (s, t, expected)
            ("anagram", "nagaram", True),
            ("rat", "car", False),
            ("aa", "a", False),                 # different lengths, must exit early
            ("a", "aa", False),                 # same mismatch the other way round
            ("a", "a", True),                   # single character
            ("aacc", "ccac", False),            # same letter set, wrong counts
            ("ab", "ba", True),                 # simple swap
            ("abc", "abd", False),              # same length, one letter differs
        ]

        for s, t, expected in cases:
            with self.subTest(s=s, t=t):
                result = self.solution.is_anagram(s, t)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
