import unittest
from course_schedule import Solution


class TestCourseSchedule(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_finish(self):
        cases = [
            # (num_courses, prerequisites, expected)
            (2, [[1, 0]], True),                          # 0 -> 1, fine
            (2, [[1, 0], [0, 1]], False),                  # direct cycle
            (1, [], True),                                 # no prerequisites at all
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]], True),   # diamond dependency, no cycle
            (3, [[0, 1], [1, 2], [2, 0]], False),          # 3-cycle
            (5, [[1, 0], [2, 1], [3, 2], [4, 3]], True),   # long chain
        ]

        for num_courses, prerequisites, expected in cases:
            with self.subTest(num_courses=num_courses, prerequisites=prerequisites):
                result = self.solution.can_finish(num_courses, prerequisites)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
