from jump_game_ii import Solution

solution = Solution()

for nums in ([2, 3, 1, 1, 4], [2, 3, 0, 1, 4], [0], [1, 1, 1, 1]):
    print(nums, solution.jump(nums))
