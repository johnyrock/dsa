import unittest
from daily_temperatures import Solution


class TestDailyTemperatures(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_daily_temperatures(self):
        cases = [
            # (temperatures, expected)
            ([73, 74, 75, 71, 69, 72, 76, 73], [1, 1, 4, 2, 1, 1, 0, 0]),  # the running example in the walkthrough
            ([30, 40, 50, 60], [1, 1, 1, 0]),                              # strictly rising: every day resolves next day
            ([30, 60, 90], [1, 1, 0]),
            ([90, 60, 30], [0, 0, 0]),                                     # strictly falling: nothing ever resolves
            ([70, 70, 70], [0, 0, 0]),                                     # equal is not warmer; `<=` would give [1, 1, 0]
            ([50], [0]),                                                   # single day
            ([60, 50, 40, 70], [3, 2, 1, 0]),                              # one warm day resolves a whole run at once
            ([30, 100, 30, 100], [1, 0, 1, 0]),
        ]

        for temperatures, expected in cases:
            with self.subTest(temperatures=temperatures):
                result = self.solution.daily_temperatures(list(temperatures))
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
