import unittest
from two_sum_ii_input_array_is_sorted import Solution


class TestTwoSumIiInputArrayIsSorted(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        cases = [
            # (numbers, target, expected 1-based indices)
            ([2, 7, 11, 15], 9, [1, 2]),          # the running example in the walkthrough
            ([2, 3, 4], 6, [1, 3]),               # must not use index 2 twice (3 + 3)
            ([-1, 0], -1, [1, 2]),                # negative values, two elements
            ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),   # duplicates: the answer is the adjacent pair
            ([5, 25, 75], 100, [2, 3]),           # answer is the last two
            ([1, 2, 3, 4, 5], 9, [4, 5]),         # left never moves
            ([1, 2, 3, 4, 5], 3, [1, 2]),         # right walks all the way down
            ([-3, -1, 0, 2, 4], 2, [3, 4]),       # mixed signs
            ([0, 0, 3, 4], 0, [1, 2]),            # target 0 with two zeros
        ]

        for numbers, target, expected in cases:
            with self.subTest(numbers=numbers, target=target):
                result = self.solution.two_sum(numbers, target)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
