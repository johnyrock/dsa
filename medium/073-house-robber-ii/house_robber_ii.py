class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob_line(nums[1:]), self._rob_line(nums[:-1]))

    def _rob_line(self, houses: list[int]) -> int:
        skip, take = 0, 0
        for money in houses:
            skip, take = take, max(take, skip + money)
        return take
