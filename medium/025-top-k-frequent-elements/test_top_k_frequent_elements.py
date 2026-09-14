import unittest
from top_k_frequent_elements import Solution


class TestTopKFrequentElements(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_top_k_frequent(self):
        cases = [
            # (nums, k, expected as a set; the problem accepts any order)
            ([1, 1, 1, 2, 2, 3], 2, {1, 2}),           # the running example in the walkthrough
            ([1], 1, {1}),                              # single element, k = 1
            ([4, 4, 4, 5, 5, 6, 6, 7], 3, {4, 5, 6}),  # 7 is the only value that must be evicted
            ([3, 3, 2, 2, 1, 1], 3, {1, 2, 3}),         # k equals the number of distinct values, nothing is evicted
            ([-1, -1, 2, 2, 2, 5], 1, {2}),             # negative values are fine as heap payloads
            ([5, 5, 5, 5, 1, 2, 3, 4], 1, {5}),         # k = 1 keeps only the root's rival
        ]

        for nums, k, expected in cases:
            with self.subTest(nums=nums, k=k):
                result = self.solution.top_k_frequent(nums, k)
                self.assertEqual(len(result), k)
                self.assertEqual(set(result), expected)


if __name__ == '__main__':
    unittest.main()
