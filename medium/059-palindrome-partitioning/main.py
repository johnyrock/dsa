from palindrome_partitioning import Solution

solution = Solution()

for s in ["aab", "a", "aba"]:
    print(s, solution.partition(s))
