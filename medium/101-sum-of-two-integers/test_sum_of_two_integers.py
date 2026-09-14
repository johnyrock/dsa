import unittest
from sum_of_two_integers import Solution


class TestSumOfTwoIntegers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_get_sum(self):
        cases = [
            # (a, b, expected)
            (5, 3, 8),              # the running example in the walkthrough: four carry rounds
            (2, 3, 5),
            (1, 2, 3),              # no carry at all, a single XOR
            (0, 0, 0),
            (7, 0, 7),              # b = 0 means the loop never runs
            (0, 7, 7),
            (-2, 3, 1),             # negative operand: without the mask the carry loop never terminates
            (3, -2, 1),
            (-3, 1, -2),            # negative result: bit 31 set after masking, must be unmasked
            (-1, -1, -2),
            (-1, 1, 0),             # carry ripples off the top of the register and is discarded
            (1000, 1000, 2000),     # constraint maxima
            (-1000, -1000, -2000),
            (-1000, 1000, 0),
        ]

        for a, b, expected in cases:
            with self.subTest(a=a, b=b):
                result = self.solution.get_sum(a, b)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
