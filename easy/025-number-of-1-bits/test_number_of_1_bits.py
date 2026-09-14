import unittest
from number_of_1_bits import Solution


class TestNumberOf1Bits(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_number_of_1_bits(self):
        cases = [
            (11, 3),
            (128, 1),
            (0, 0),                            # no set bits
            (2**31 - 1, 31),
        ]
        for value, expected in cases:
            with self.subTest(value=value):
                self.assertEqual(self.solution.hamming_weight(value), expected)


if __name__ == '__main__':
    unittest.main()
