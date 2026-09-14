from combination_sum import Solution

solution = Solution()

for candidates, target in (([2, 3, 6, 7], 7), ([2, 3, 5], 8), ([2], 1)):
    print(candidates, target, solution.combination_sum(candidates, target))
