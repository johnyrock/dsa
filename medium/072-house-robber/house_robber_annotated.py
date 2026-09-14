class Solution:
    # Return the most money obtainable from a row of houses when no two adjacent houses may both be robbed.
    def rob(self, nums: list[int]) -> int:
        # skip = best total for the houses before the previous one (i.e. ending two back).
        # take = best total for all houses up to and including the previous one.
        # Both start at 0: with no houses considered, the best haul is nothing.
        skip, take = 0, 0
        for money in nums:
            # Two options for this house: leave it, keeping the best so far (take), or rob it, which forbids the previous house, so add money to skip.
            # The tuple assignment reads both right-hand values before rebinding, so the old take becomes the new skip without a temporary.
            skip, take = take, max(take, skip + money)
        # After the last house, take is the best total over the whole street.
        return take
