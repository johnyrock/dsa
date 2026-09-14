class Solution:
    def max_product(self, nums: list[int]) -> int:
        best = cur_max = cur_min = nums[0]
        for x in nums[1:]:
            candidates = (x, x * cur_max, x * cur_min)
            cur_max, cur_min = max(candidates), min(candidates)
            best = max(best, cur_max)
        return best
