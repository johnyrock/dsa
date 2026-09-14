from surrounded_regions import Solution

solution = Solution()

board = [
    ["X", "X", "X", "X", "X"],
    ["X", "O", "O", "X", "O"],
    ["X", "X", "O", "X", "O"],
    ["X", "O", "X", "X", "X"],
]
solution.solve(board)
for row in board:
    print(" ".join(row))
