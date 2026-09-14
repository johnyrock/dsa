import unittest
from implement_trie_prefix_tree import Trie


class TestImplementTriePrefixTree(unittest.TestCase):
    def test_leetcode_example(self):
        trie = Trie()
        ops = [
            # (operation, argument, expected)
            ("insert", "apple", None),
            ("search", "apple", True),
            ("search", "app", False),          # prefix of an inserted word, but not inserted itself
            ("starts_with", "app", True),
            ("insert", "app", None),
            ("search", "app", True),           # now it is both a prefix and a word
        ]
        for op, arg, expected in ops:
            with self.subTest(op=op, arg=arg):
                result = getattr(trie, op)(arg)
                self.assertEqual(result, expected)

    def test_search_cases(self):
        trie = Trie()
        for word in ["car", "card", "care", "cat", "dog"]:
            trie.insert(word)
        cases = [
            # (method, argument, expected)
            ("search", "car", True),
            ("search", "ca", False),           # interior node, not a word end
            ("search", "cards", False),        # walks past the end of "card"
            ("search", "cab", False),          # branch missing at the last letter
            ("search", "bird", False),         # branch missing at the first letter
            ("starts_with", "ca", True),
            ("starts_with", "card", True),     # a full word is also a prefix of itself
            ("starts_with", "cards", False),
            ("starts_with", "d", True),
            ("starts_with", "e", False),
        ]
        for method, arg, expected in cases:
            with self.subTest(method=method, arg=arg):
                self.assertEqual(getattr(trie, method)(arg), expected)

    def test_empty_trie(self):
        trie = Trie()
        self.assertFalse(trie.search("a"))
        self.assertFalse(trie.starts_with("a"))
        self.assertTrue(trie.starts_with(""))  # the empty prefix always matches the root

    def test_insert_twice_is_idempotent(self):
        trie = Trie()
        trie.insert("hello")
        trie.insert("hello")
        self.assertTrue(trie.search("hello"))
        self.assertEqual(len(trie.root.children), 1)


if __name__ == '__main__':
    unittest.main()
