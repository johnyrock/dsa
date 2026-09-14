from jump_game import Solution

solution = Solution()

for nums in ([2, 3, 1, 1, 4], [3, 2, 1, 0, 4], [0], [2, 0, 0]):
    print(nums, solution.can_jump(nums))
