import unittest
from merge_triplets_to_form_target_triplet import Solution


class TestMergeTripletsToFormTargetTriplet(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_merge_triplets(self):
        cases = [
            # (triplets, target, expected)
            ([[2, 5, 3], [1, 8, 4], [1, 7, 5]], [2, 7, 5], True),      # the running example: [1,8,4] is skipped, the other two cover all three positions
            ([[3, 4, 5], [4, 5, 6]], [3, 2, 5], False),               # every triplet exceeds target[1] = 2, so nothing is usable
            ([[2, 5, 3], [2, 3, 4], [1, 2, 5], [5, 2, 3]], [5, 5, 5], True),
            ([[1, 3, 4], [2, 5, 8]], [2, 5, 8], True),                # target is present verbatim
            ([[1, 2, 3]], [1, 2, 4], False),                          # position 2 can never reach 4
            ([[3, 3, 3], [1, 1, 1]], [1, 1, 1], True),                # the oversized triplet is ignored, not fatal
            ([[2, 2, 2], [2, 2, 2]], [3, 3, 3], False),               # all safe but none reaches the target values
        ]

        for triplets, target, expected in cases:
            with self.subTest(triplets=triplets, target=target):
                result = self.solution.merge_triplets(triplets, target)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
