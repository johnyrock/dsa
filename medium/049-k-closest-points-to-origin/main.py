from k_closest_points_to_origin import Solution

solution = Solution()

print(solution.k_closest([[3, 3], [5, -1], [-2, 4]], 2))   # [[-2, 4], [3, 3]] in some order
print(solution.k_closest([[1, 3], [-2, 2]], 1))            # [[-2, 2]]
print(solution.k_closest([[0, 1], [1, 0]], 2))             # both points
