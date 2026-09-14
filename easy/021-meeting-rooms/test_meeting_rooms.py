import unittest
from meeting_rooms import Solution


class TestMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_meeting_rooms(self):
        cases = [
            ([[0, 30], [5, 10], [15, 20]], False),
            ([[7, 10], [2, 4]], True),
            ([], True),                         # no meetings cannot conflict
            ([[1, 2], [2, 3]], True),           # touching endpoints do not overlap
            ([[1, 4], [2, 3]], False),
        ]
        for intervals, expected in cases:
            with self.subTest(intervals=intervals):
                self.assertEqual(self.solution.can_attend_meetings(intervals), expected)


if __name__ == '__main__':
    unittest.main()
