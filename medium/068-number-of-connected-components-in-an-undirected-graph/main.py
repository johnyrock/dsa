from number_of_connected_components_in_an_undirected_graph import Solution

solution = Solution()

print(solution.count_components(5, [[0, 1], [1, 2], [3, 4]]))
print(solution.count_components(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))
print(solution.count_components(4, []))
