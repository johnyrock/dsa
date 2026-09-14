import unittest
from gas_station import Solution


class TestGasStation(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_can_complete_circuit(self):
        cases = [
            # (gas, cost, expected)
            ([1, 2, 3, 4, 5], [3, 4, 5, 1, 2], 3),      # the running example
            ([2, 3, 4], [3, 4, 3], -1),                 # total gas 9 < total cost 10
            ([5, 1, 2, 3, 4], [4, 4, 1, 5, 1], 4),      # index 0 survives three legs before dying at station 3
            ([4], [3], 0),                              # single station, trivially completes
            ([3], [4], -1),
            ([2, 2, 2], [2, 2, 2], 0),                  # exactly break-even, the first index wins
            ([1, 2, 3], [2, 3, 1], 2),                  # only the last station can start; start = i + 1 lands exactly on it
            ([5, 8, 2, 8], [6, 5, 6, 6], 3),
        ]

        for gas, cost, expected in cases:
            with self.subTest(gas=gas, cost=cost):
                self.assertEqual(self.solution.can_complete_circuit(gas, cost), expected)


if __name__ == '__main__':
    unittest.main()
