import unittest
from group_anagrams import Solution


def normalize(groups):
    # Group order and order within a group are both unspecified, so canonicalise both.
    return sorted(sorted(g) for g in groups)


class TestGroupAnagrams(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_group_anagrams(self):
        cases = [
            # (strs, expected)
            (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
            ([""], [[""]]),                                     # single empty string is its own group
            (["a"], [["a"]]),                                   # single word
            (["", ""], [["", ""]]),                             # two empty strings are anagrams of each other
            (["abc", "bca", "cab", "cba"], [["abc", "bca", "cab", "cba"]]),
            (["ab", "ba", "abc"], [["ab", "ba"], ["abc"]]),     # prefix is not an anagram
            (["aab", "abb"], [["aab"], ["abb"]]),               # same letters, different counts
            (["bdddddddddd", "bbbbbbbbbbc"], [["bdddddddddd"], ["bbbbbbbbbbc"]]),  # sums of letters match, counts do not
            (["x", "y", "z"], [["x"], ["y"], ["z"]]),           # all singletons
        ]

        for strs, expected in cases:
            with self.subTest(strs=strs):
                result = self.solution.group_anagrams(list(strs))
                self.assertEqual(normalize(result), normalize(expected))


if __name__ == '__main__':
    unittest.main()
