class Solution:
    # Houses form a circle: the first and last are neighbours, so they can never both be robbed.
    def rob(self, nums: list[int]) -> int:
        # A single house has no neighbour to conflict with. Both slices below would be empty and return 0, which is wrong, so handle it first.
        if len(nums) == 1:
            return nums[0]
        # Either the first house is out (rob among nums[1:]) or the last house is out (rob among nums[:-1]). Each slice is a straight line, which the ordinary House Robber solves. The true answer is the better of the two.
        return max(self._rob_line(nums[1:]), self._rob_line(nums[:-1]))

    # The linear House Robber: best loot from a row of houses where adjacent ones cannot both be taken.
    def _rob_line(self, houses: list[int]) -> int:
        # skip = best loot with the previous house NOT robbed, take = best loot up to and including the previous house (robbed or not). Both start at 0 before any house.
        skip, take = 0, 0
        for money in houses:
            # Robbing this house forces the previous one to be skipped: skip + money. Not robbing it keeps take. The old take becomes the new skip. The tuple assignment reads both old values before rebinding.
            skip, take = take, max(take, skip + money)
        # take is the best over the whole row.
        return take
