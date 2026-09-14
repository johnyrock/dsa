from max_area_of_island import Solution

solution = Solution()

grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 0, 1, 1, 1],
]
print(solution.max_area_of_island(grid))
