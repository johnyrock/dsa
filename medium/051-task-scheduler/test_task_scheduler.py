import unittest
from task_scheduler import Solution


class TestTaskScheduler(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_least_interval(self):
        cases = [
            # (tasks, n, expected)
            (["A", "A", "A", "B", "B", "B"], 2, 8),                 # the running example: A B _ A B _ A B
            (["A", "C", "A", "B", "D", "B"], 1, 6),                 # enough distinct letters, no idle at all
            (["A", "A", "A", "B", "B", "B"], 3, 10),                # two idles per gap
            (["A", "A", "A", "B", "B", "B"], 0, 6),                 # n = 0 means just run them all
            (["A"], 5, 1),                                          # a single task never waits
            (["A", "A"], 2, 4),                                     # A _ _ A: the last cooldown is fully paid
            (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),  # one dominant letter, A x x A x x ... A
            (["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], 2, 12),  # closed form gives 7 + ..., but len(tasks) = 12 wins
            (["A", "B", "C", "D", "E", "F"], 100, 6),               # all distinct, huge n irrelevant
        ]

        for tasks, n, expected in cases:
            with self.subTest(tasks=tasks, n=n):
                result = self.solution.least_interval(tasks, n)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
