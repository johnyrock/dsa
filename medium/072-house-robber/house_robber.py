class Solution:
    def rob(self, nums: list[int]) -> int:
        skip, take = 0, 0
        for money in nums:
            skip, take = take, max(take, skip + money)
        return take
