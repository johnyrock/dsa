import unittest
from longest_substring_without_repeating_characters import Solution


class TestLongestSubstringWithoutRepeatingCharacters(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_length_of_longest_substring(self):
        cases = [
            # (s, expected)
            ("abcabcbb", 3),
            ("bbbbb", 1),              # all the same character
            ("pwwkew", 3),             # "wke"
            ("", 0),                   # empty string
            (" ", 1),                  # a single space is a character
            ("au", 2),                 # two distinct, whole string
            ("dvdf", 3),               # the stale-occurrence trap: left must not move backwards
            ("abba", 2),               # second trap: the 'a' at index 0 is outside the window when the last 'a' arrives
            ("tmmzuxt", 5),            # "mzuxt"
            ("abcdefg", 7),            # no repeats at all
            ("aab", 2),
            ("a1!a1!", 3),             # digits and symbols count as characters
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                result = self.solution.length_of_longest_substring(s)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
