class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # value -> index
        for i, n in enumerate(nums):
            complement = target - n
            if complement in seen:
                return [seen[complement], i]
            seen[n] = i
        return []
