from combination_sum_ii import Solution

solution = Solution()

for candidates, target in [([10, 1, 2, 7, 6, 1, 5], 8), ([2, 5, 2, 1, 2], 5), ([3], 8)]:
    print(candidates, target, solution.combination_sum2(list(candidates), target))
