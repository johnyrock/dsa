import unittest
from valid_parenthesis_string import Solution


class TestValidParenthesisString(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_check_valid_string(self):
        cases = [
            # (s, expected)
            ("()", True),
            ("(*)", True),
            ("(*))", True),           # the running example: the star must become '('
            ("(((*)", False),         # one star cannot close three opens
            (")(", False),            # hi drops below 0 on the first character
            (")**", False),           # a leading ')' cannot be fixed by later stars
            ("*(", False),            # a star before the '(' cannot close it
            ("(**", True),            # one star closes the "(", the other vanishes
            ("**", True),             # both stars vanish
            ("", True),               # LeetCode's minimum length is 1, but the empty string is trivially valid
            ("(*()", True),           # the star closes the first '('
        ]

        for s, expected in cases:
            with self.subTest(s=s):
                result = self.solution.check_valid_string(s)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
