from permutations import Solution

solution = Solution()

for nums in ([1, 2, 3], [0, 1], [1]):
    print(nums, solution.permute(nums))
