import unittest
from valid_parentheses import Solution


class TestValidParentheses(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_valid(self):
        cases = [
            # (s, expected)
            ("()", True),
            ("()[]{}", True),
            ("([]{})", True),                   # nested and sequential mixed
            ("([)]", False),                    # counts balance but the order crosses
            ("((", False),                      # leftover openers, stack not empty at the end
            (")", False),                       # closer with nothing open
            ("]", False),                       # single closer, minimum length
            ("{[()]}", True),                   # fully nested, three levels deep
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                result = self.solution.is_valid(s)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
