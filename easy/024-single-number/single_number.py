class Solution:
    def single_number(self, nums: list[int]) -> int:
        unique = 0
        for number in nums:
            unique ^= number
        return unique
