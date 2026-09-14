from evaluate_reverse_polish_notation import Solution

solution = Solution()

print(solution.eval_rpn(["4", "13", "5", "/", "+"]))   # 6
print(solution.eval_rpn(["2", "1", "+", "3", "*"]))    # 9
print(solution.eval_rpn(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))   # 22
