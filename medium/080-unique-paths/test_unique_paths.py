import unittest
from unique_paths import Solution


class TestUniquePaths(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_unique_paths(self):
        cases = [
            # (m, n, expected)
            (3, 7, 28),            # the running example in the walkthrough
            (3, 2, 3),             # right-down-down, down-right-down, down-down-right
            (1, 1, 1),             # single cell, the empty path
            (1, 10, 1),            # one row: only "right" moves
            (10, 1, 1),            # one column: only "down" moves
            (2, 2, 2),
            (3, 3, 6),             # C(4, 2)
            (7, 3, 28),            # symmetric with (3, 7)
            (4, 4, 20),            # an extra row iteration would give 35 here
            (10, 10, 48620),       # C(18, 9)
            (100, 100, 22750883079422934966181954039568885395604168260154104734000),  # the value must not overflow
        ]

        for m, n, expected in cases:
            with self.subTest(m=m, n=n):
                result = self.solution.unique_paths(m, n)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
