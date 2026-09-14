class Solution:
    # Return the length of the longest strictly increasing subsequence (elements need not be adjacent).
    def length_of_lis(self, nums: list[int]) -> int:
        # dp[i] is the length of the longest increasing subsequence that ENDS at index i. Every element alone is a subsequence of length 1, so seed with 1, never 0.
        dp = [1] * len(nums)
        # Fill left to right: by the time we reach i, every dp[j] for j < i is final.
        for i in range(len(nums)):
            # Try every earlier index j as the element that comes right before nums[i] in the subsequence.
            for j in range(i):
                # Only a strictly smaller earlier value can precede nums[i]; equal values do not count as increasing.
                if nums[j] < nums[i]:
                    # Extending the best subsequence ending at j by nums[i] gives length dp[j] + 1; keep the best over all j.
                    dp[i] = max(dp[i], dp[j] + 1)
        # The overall LIS can end anywhere, not necessarily at the last index, so take the max of the whole table.
        return max(dp)
