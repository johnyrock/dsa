from generate_parentheses import Solution

solution = Solution()

for n in range(1, 4):
    print(n, solution.generate_parenthesis(n))
