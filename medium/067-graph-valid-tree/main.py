from graph_valid_tree import Solution

solution = Solution()

print(solution.valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(solution.valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(solution.valid_tree(5, [[0, 1], [1, 2], [3, 4]]))
