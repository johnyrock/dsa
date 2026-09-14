import unittest
from generate_parentheses import Solution


class TestGenerateParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_generate_parenthesis(self):
        cases = [
            # (n, expected set of strings)
            (1, {"()"}),                                                   # smallest input
            (2, {"(())", "()()"}),
            (3, {"((()))", "(()())", "(())()", "()(())", "()()()"}),       # the running example in the walkthrough
        ]

        for n, expected in cases:
            with self.subTest(n=n):
                result = self.solution.generate_parenthesis(n)
                self.assertEqual(len(result), len(expected))                # no duplicates
                self.assertEqual(set(result), expected)

    def test_counts_are_catalan(self):
        # C(4) = 14, C(5) = 42, C(8) = 1430; a missing prune would give C(2n, n) instead
        for n, count in [(4, 14), (5, 42), (8, 1430)]:
            with self.subTest(n=n):
                result = self.solution.generate_parenthesis(n)
                self.assertEqual(len(result), count)
                self.assertEqual(len(set(result)), count)
                for s in result:
                    depth = 0
                    for ch in s:
                        depth += 1 if ch == "(" else -1
                        self.assertGreaterEqual(depth, 0)
                    self.assertEqual(depth, 0)


if __name__ == '__main__':
    unittest.main()
