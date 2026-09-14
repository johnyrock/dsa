from valid_parenthesis_string import Solution

solution = Solution()

for s in ["()", "(*)", "(*))", "(((*)"]:
    print(s, solution.check_valid_string(s))
