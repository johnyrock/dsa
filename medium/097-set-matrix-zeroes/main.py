from set_matrix_zeroes import Solution

solution = Solution()

matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.set_zeroes(matrix)
for row in matrix:
    print(row)
