import unittest
from permutation_in_string import Solution


class TestPermutationInString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_check_inclusion(self):
        cases = [
            # (s1, s2, expected)
            ("ab", "eidbaooo", True),      # the running example in the walkthrough, matches at "ba"
            ("ab", "eidboaoo", False),     # the letters are present but never adjacent
            ("adc", "dcda", True),         # matches at "cda", i.e. after the window has started sliding
            ("a", "a", True),              # window is the whole text
            ("a", "b", False),
            ("abc", "ab", False),          # s1 longer than s2, guard must fire before the loop
            ("ab", "ab", True),            # match on the very first full window (i == k - 1)
            ("ab", "ba", True),            # match with reversed order
            ("aab", "baa", True),          # repeated letters, counts must reach 2
            ("aab", "abb", False),         # same letter set but different multiplicity
            ("hello", "ooollehoooleh", True),  # match "olleh" only after several slides
            ("abc", "ccccbbbbaaaa", False),    # every letter present, never within one window
            ("ab", "xxxxab", True),        # match at the very end of s2
        ]

        for s1, s2, expected in cases:
            with self.subTest(s1=s1, s2=s2):
                result = self.solution.check_inclusion(s1, s2)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
