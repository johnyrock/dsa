class Solution:
    def longest_consecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        best = 0
        for num in seen:
            if num - 1 in seen:
                continue
            length = 1
            while num + length in seen:
                length += 1
            best = max(best, length)
        return best
