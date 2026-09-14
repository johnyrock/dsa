from task_scheduler import Solution

solution = Solution()

print(solution.least_interval(["A", "A", "A", "B", "B", "B"], 2))       # 8
print(solution.least_interval(["A", "C", "A", "B", "D", "B"], 1))       # 6
print(solution.least_interval(["A", "A", "A", "B", "B", "B"], 3))       # 10
