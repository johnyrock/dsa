import unittest
from longest_repeating_character_replacement import Solution


class TestLongestRepeatingCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_character_replacement(self):
        cases = [
            # (s, k, expected)
            ("ABAB", 2, 4),               # replace both odd letters out
            ("AABABBA", 1, 4),            # AABA or ABBB, one swap
            ("", 0, 0),                   # empty string
            ("A", 0, 1),                  # single character, no swaps needed
            ("AAAA", 2, 4),               # already uniform
            ("ABCDE", 1, 2),              # all distinct, best window is 2
            ("ABBB", 2, 4),               # k covers the rest of the string
        ]

        for s, k, expected in cases:
            with self.subTest(s=s, k=k):
                result = self.solution.character_replacement(s, k)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
