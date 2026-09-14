from subsets_ii import Solution

solution = Solution()

for nums in ([1, 2, 2], [0], [4, 4, 4, 1]):
    print(nums, solution.subsets_with_dup(nums))
