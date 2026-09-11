import unittest
from word_container import Solver, WordList


def solve(words):
    return Solver(WordList(words)).find_words_containing_other_words()


class TestWordContainer(unittest.TestCase):
    def test_find_words_containing_other_words(self):
        cases = [
            # (words, expected)
            (["apple", "app", "banana", "nana"], ["apple", "banana"]),  # the running example
            (["a", "b", "c"], []),                                      # no word contains another
            (["abc", "ab", "a"], ["abc", "ab"]),                        # chained containment
            (["cat", "cats"], ["cats"]),
            (["same", "same"], []),                                    # identical strings: not "another" word
            (["xy", "xyz", "wxyz"], ["xyz", "wxyz"]),                   # containment can be more than one level deep
            ([], []),                                                  # empty list
            (["onlyone"], []),                                         # nothing else to contain
            (["ab", "ba"], []),                                        # same letters, not a substring of each other
            (["prefix", "pre"], ["prefix"]),                           # match at the start of the word
            (["suffix", "fix"], ["suffix"]),                           # match at the end of the word
        ]

        for words, expected in cases:
            with self.subTest(words=words):
                result = solve(list(words))
                self.assertEqual(sorted(result), sorted(expected))


if __name__ == '__main__':
    unittest.main()
