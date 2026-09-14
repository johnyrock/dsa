import unittest
from course_schedule_ii import Solution


def is_valid_order(num_courses: int, prerequisites: list[list[int]], order: list[int]) -> bool:
    if sorted(order) != list(range(num_courses)):
        return False
    position = {course: i for i, course in enumerate(order)}
    return all(position[pre] < position[course] for course, pre in prerequisites)


class TestCourseScheduleII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_find_order_exact(self):
        cases = [
            # (num_courses, prerequisites, expected) — cases whose BFS order is fully determined
            (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [0, 1, 2, 3]),   # the running example: diamond, FIFO takes 1 before 2
            (2, [[1, 0]], [0, 1]),
            (1, [], [0]),                                          # single course, no prerequisites
            (2, [[1, 0], [0, 1]], []),                             # direct cycle, no order exists
            (3, [[1, 0], [2, 1], [1, 2]], []),                     # 0 can be taken but 1 and 2 need each other: still []
            (5, [[1, 0], [2, 1], [3, 2], [4, 3]], [0, 1, 2, 3, 4]),   # long chain
            (3, [[0, 1], [0, 2], [1, 2]], [2, 1, 0]),              # pairs are [course, pre]: 2 first, not 0
        ]

        for num_courses, prerequisites, expected in cases:
            with self.subTest(num_courses=num_courses, prerequisites=prerequisites):
                result = self.solution.find_order(num_courses, prerequisites)
                self.assertEqual(result, expected)

    def test_find_order_any_valid(self):
        cases = [
            # (num_courses, prerequisites) — several valid orders exist; check validity, not a specific one
            (3, []),                                       # no prerequisites at all: any permutation is fine
            (6, [[5, 2], [5, 0], [4, 0], [4, 1], [2, 3], [3, 1]]),
            (4, [[3, 0], [3, 1], [3, 2]]),                 # three independent prerequisites for one course
        ]

        for num_courses, prerequisites in cases:
            with self.subTest(num_courses=num_courses, prerequisites=prerequisites):
                result = self.solution.find_order(num_courses, prerequisites)
                self.assertTrue(is_valid_order(num_courses, prerequisites, result), result)


if __name__ == '__main__':
    unittest.main()
