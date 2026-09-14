class Solution:
    # Return True if nums can be split into two groups with the same sum.
    def can_partition(self, nums: list[int]) -> bool:
        # Two equal halves must each sum to exactly half the total.
        total = sum(nums)
        # An odd total cannot be halved into integers, so no partition exists. This check also keeps target an int below.
        if total % 2:
            return False
        # The question becomes: is there a subset whose sum is exactly target? The other elements then form the second half automatically.
        target = total // 2
        # dp[s] means "some subset of the numbers seen so far sums to exactly s". One slot per sum from 0 to target.
        dp = [False] * (target + 1)
        # The empty subset sums to 0. This seed is where every other True is grown from.
        dp[0] = True
        # Take the numbers one at a time; each is either put in the subset or left out.
        for num in nums:
            # Walk the sums from high to low so dp[s - num] still refers to the table BEFORE this num was added. Ascending would let the same num be counted twice.
            for s in range(target, num - 1, -1):
                # If s - num was reachable without this num, then s is reachable by adding it.
                if dp[s - num]:
                    dp[s] = True
        # Reachable exactly at half the total means the other half is the complement.
        return dp[target]
