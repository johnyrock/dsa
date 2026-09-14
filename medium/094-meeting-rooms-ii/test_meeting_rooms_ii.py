import unittest
from meeting_rooms_ii import Solution


class TestMeetingRoomsII(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_min_meeting_rooms(self):
        cases = [
            # (intervals, expected)
            ([[0, 30], [5, 10], [15, 20]], 2),        # the running example: [5,10] and [15,20] reuse one room
            ([[7, 10], [2, 4]], 1),                   # unsorted input, no overlap
            ([[1, 5], [2, 6], [3, 7], [4, 8]], 4),    # all four overlap at t = 4
            ([[1, 2], [2, 3]], 1),                    # touching endpoints share a room
            ([[1, 3], [2, 3]], 2),
            ([[5, 8], [6, 8]], 2),
            ([[1, 10], [2, 3], [4, 5], [6, 7]], 2),   # one long meeting, three short ones reuse the second room
            ([[2, 15], [36, 45], [9, 29], [16, 23], [4, 9]], 2),
            ([[1, 2]], 1),                            # a single meeting needs one room
            ([], 0),                                  # no meetings, no rooms
        ]
        for intervals, expected in cases:
            with self.subTest(intervals=intervals):
                self.assertEqual(self.solution.min_meeting_rooms(intervals), expected)


if __name__ == '__main__':
    unittest.main()
