from subsets import Solution

solution = Solution()

for nums in ([1, 2, 3], [0], [4, 7]):
    print(nums, solution.subsets(nums))
