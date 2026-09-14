import unittest
from network_delay_time import Solution


class TestNetworkDelayTime(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_network_delay_time(self):
        cases = [
            # (times, n, k, expected)
            ([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2, 2),           # the running example: slowest arrival is node 4 at time 2
            ([[1, 2, 1]], 2, 1, 1),                                  # single edge
            ([[1, 2, 1]], 2, 2, -1),                                 # edge points the wrong way, node 1 unreachable
            ([[1, 2, 1], [2, 3, 2], [1, 3, 4]], 3, 1, 3),            # direct edge 1->3 costs 4 but 1->2->3 costs 3
            ([[1, 2, 1], [2, 1, 3]], 2, 1, 1),                       # cycle, the stale heap entry must be skipped
            ([[1, 2, 5], [1, 3, 1], [3, 2, 1]], 3, 1, 2),            # node 2 pushed twice: (5, 2) then (2, 2); the smaller wins
            ([], 1, 1, 0),                                           # only the source exists, nothing to wait for
            ([[1, 2, 0]], 2, 1, 0),                                  # zero-weight edge is allowed by the constraints
        ]

        for times, n, k, expected in cases:
            with self.subTest(times=times, n=n, k=k):
                result = self.solution.network_delay_time(times, n, k)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
