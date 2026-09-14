class Solution:
    # Count the ways to put a + or - in front of every number so that the expression equals target.
    def find_target_sum_ways(self, nums: list[int], target: int) -> int:
        # Let P be the sum of the numbers given a plus and N the sum of those given a minus. P - N = target and P + N = total, so P = (total + target) / 2. The problem is now: count subsets whose sum is P.
        total = sum(nums)
        # No assignment can reach a target outside [-total, total], and P must be a whole number, so an odd total + target has no solutions. Both checks also keep goal from going negative or fractional below.
        if abs(target) > total or (total + target) % 2:
            return 0
        # The subset-sum target: how much has to be on the plus side.
        goal = (total + target) // 2  # sum of the numbers that get a plus sign
        # dp[s] counts subsets of the numbers processed so far that add up to exactly s.
        dp = [0] * (goal + 1)  # dp[s]: subsets of the numbers seen so far that sum to s
        # The empty subset sums to 0. Every other count grows from this seed.
        dp[0] = 1
        # Add the numbers one at a time; each is either in the subset or not.
        for num in nums:
            # Walk the sums downward so that dp[s - num] is still the count from before this number was added. That is what makes each number usable at most once. Stop at num because smaller sums cannot include it.
            for s in range(goal, num - 1, -1):
                # Every subset summing to s - num becomes a subset summing to s by adding num.
                dp[s] += dp[s - num]
        # Subsets with sum goal correspond one-to-one with sign assignments that hit target.
        return dp[goal]
