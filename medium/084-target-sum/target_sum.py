class Solution:
    def find_target_sum_ways(self, nums: list[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total or (total + target) % 2:
            return 0
        goal = (total + target) // 2  # sum of the numbers that get a plus sign
        dp = [0] * (goal + 1)  # dp[s]: subsets of the numbers seen so far that sum to s
        dp[0] = 1
        for num in nums:
            for s in range(goal, num - 1, -1):
                dp[s] += dp[s - num]
        return dp[goal]
