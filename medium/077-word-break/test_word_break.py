import unittest
from word_break import Solution


class TestWordBreak(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_word_break(self):
        cases = [
            # (s, word_dict, expected)
            ("leetcode", ["leet", "code"], True),                        # the running example in the walkthrough
            ("applepenapple", ["apple", "pen"], True),                   # a word is reused
            ("catsandog", ["cats", "dog", "sand", "and", "cat"], False), # "cats and og" / "cat sand og" both leave "og"
            ("a", ["a"], True),                                          # single character
            ("a", ["b"], False),
            ("aaaaaaa", ["aaaa", "aaa"], True),                          # 4 + 3, needs the cut-point search
            ("aaaaaaab", ["aaaa", "aaa"], False),                        # last char never matches
            ("cars", ["car", "ca", "rs"], True),                         # greedy "car" fails; "ca" + "rs" works
            ("abcd", ["a", "abc", "b", "cd"], True),
            ("ab", ["ab", "a", "b"], True),                              # whole string is itself a word
        ]

        for s, word_dict, expected in cases:
            with self.subTest(s=s, word_dict=word_dict):
                result = self.solution.word_break(s, list(word_dict))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
