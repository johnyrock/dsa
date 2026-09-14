import unittest
from car_fleet import Solution


class TestCarFleet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_car_fleet(self):
        cases = [
            # (target, position, speed, expected)
            (12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 3),   # the running example in the walkthrough
            (10, [3], [3], 1),                            # a single car is a fleet
            (100, [0, 2, 4], [4, 2, 1], 1),               # everyone catches the slow leader
            (10, [6, 8], [3, 2], 2),                      # 6 arrives at 1.33 > 8's 1.0: never catches up
            (10, [0, 4, 2], [2, 1, 3], 1),                # leader (pos 4) takes 6; the others would take 2.67 and 5, so both merge
            (10, [8, 3, 7], [2, 1, 1], 3),                # decreasing speeds ahead, nobody merges
            (10, [0, 5], [1, 1], 2),                      # equal speeds never meet
            (12, [4, 2, 0], [2, 2, 2], 3),
        ]

        for target, position, speed, expected in cases:
            with self.subTest(target=target, position=position, speed=speed):
                result = self.solution.car_fleet(target, position, speed)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
