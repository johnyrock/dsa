import unittest
from design_add_and_search_words_data_structure import WordDictionary


class TestDesignAddAndSearchWordsDataStructure(unittest.TestCase):
    def test_leetcode_example(self):
        wd = WordDictionary()
        ops = [
            # (operation, argument, expected)
            ("add_word", "bad", None),
            ("add_word", "dad", None),
            ("add_word", "mad", None),
            ("search", "pad", False),          # no branch for p under the root
            ("search", "bad", True),
            ("search", ".ad", True),           # the dot tries b, d, m; b-a-d succeeds
            ("search", "b..", True),           # two dots, one path each
        ]
        for op, arg, expected in ops:
            with self.subTest(op=op, arg=arg):
                self.assertEqual(getattr(wd, op)(arg), expected)

    def test_search_cases(self):
        wd = WordDictionary()
        for word in ["bad", "dad", "mad", "badge"]:
            wd.add_word(word)
        cases = [
            # (pattern, expected)
            ("ba", False),                     # prefix only, not a word end
            ("b.", False),                     # dot reaches "ba", which is not a word
            ("..d", True),
            ("...", True),
            ("....", False),                   # "badg" is not a word
            (".....", True),                   # "badge"
            ("......", False),                 # longer than every word
            ("ma.", True),
            (".a.g.", True),                   # mixed literals and dots
            ("z..", False),                    # dead at the first literal
            ("b.dge", True),
            ("b.dgf", False),                  # dead at the last literal
        ]
        for pattern, expected in cases:
            with self.subTest(pattern=pattern):
                self.assertEqual(wd.search(pattern), expected)

    def test_empty_dictionary(self):
        wd = WordDictionary()
        self.assertFalse(wd.search("a"))
        self.assertFalse(wd.search("."))       # a dot with no children to try

    def test_dot_must_consume_exactly_one_letter(self):
        wd = WordDictionary()
        wd.add_word("a")
        wd.add_word("ab")
        self.assertTrue(wd.search("."))
        self.assertTrue(wd.search(".."))
        self.assertFalse(wd.search("..."))


if __name__ == '__main__':
    unittest.main()
