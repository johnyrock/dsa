import unittest
from hand_of_straights import Solution


class TestHandOfStraights(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_n_straight_hand(self):
        cases = [
            # (hand, group_size, expected)
            ([1, 2, 3, 6, 2, 3, 4, 7, 8], 3, True),     # the running example: [1,2,3] [2,3,4] [6,7,8]
            ([1, 2, 3, 4, 5], 4, False),                # 5 cards cannot split into groups of 4
            ([1, 1, 2, 2, 3, 3], 3, True),              # two groups opened at once from the two 1s
            ([1, 1, 2, 3, 3, 4], 3, False),             # both 1s need a 2, only one exists
            ([1, 2, 3], 1, True),                       # groups of one always work
            ([3, 2, 1, 2, 3, 4, 3, 4, 5, 9, 10, 11], 3, True),
            ([8, 10, 12], 3, False),                    # gaps between cards
            ([1, 2, 4, 5], 2, True),                    # [1,2] [4,5]; gap between groups is fine
            ([1, 2, 4, 5], 3, False),
        ]

        for hand, group_size, expected in cases:
            with self.subTest(hand=hand, group_size=group_size):
                self.assertEqual(self.solution.is_n_straight_hand(hand, group_size), expected)


if __name__ == '__main__':
    unittest.main()
