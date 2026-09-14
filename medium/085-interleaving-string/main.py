from interleaving_string import Solution

solution = Solution()

print(solution.is_interleave("aabcc", "dbbca", "aadbbcbcac"))
print(solution.is_interleave("aabcc", "dbbca", "aadbbbaccc"))
print(solution.is_interleave("", "", ""))
