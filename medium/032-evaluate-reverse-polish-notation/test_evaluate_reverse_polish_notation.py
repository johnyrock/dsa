import unittest
from evaluate_reverse_polish_notation import Solution


class TestEvaluateReversePolishNotation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_eval_rpn(self):
        cases = [
            # (tokens, expected)
            (["4", "13", "5", "/", "+"], 6),                 # the running example in the walkthrough: 4 + (13 / 5)
            (["2", "1", "+", "3", "*"], 9),                  # (2 + 1) * 3
            (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),   # 6 / -132 must truncate to 0, not floor to -1
            (["3"], 3),                                      # a single operand is a complete expression
            (["-7"], -7),                                    # negative literal, not the minus operator
            (["5", "3", "-"], 2),                            # operand order: 5 - 3, not 3 - 5
            (["3", "5", "-"], -2),
            (["7", "2", "/"], 3),                            # truncates 3.5 toward zero
            (["-7", "2", "/"], -3),                          # truncates -3.5 toward zero; floor division would give -4
            (["7", "-2", "/"], -3),
            (["1", "2", "3", "*", "+"], 7),                  # operator applies to the two most recent values
            (["2", "3", "4", "+", "*"], 14),                 # (3 + 4) * 2
            (["0", "3", "-"], -3),
            (["1000000000", "1000000000", "*"], 10**18),     # Python ints do not overflow
        ]

        for tokens, expected in cases:
            with self.subTest(tokens=tokens):
                result = self.solution.eval_rpn(tokens)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
