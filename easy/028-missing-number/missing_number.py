class Solution:
    def missing_number(self, nums: list[int]) -> int:
        missing = len(nums)
        for index, number in enumerate(nums):
            missing ^= index ^ number
        return missing
