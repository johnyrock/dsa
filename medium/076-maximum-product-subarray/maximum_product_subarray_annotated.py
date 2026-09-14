class Solution:
    # Largest product of any contiguous, non-empty subarray. Negatives can flip sign, so the smallest product matters too.
    def max_product(self, nums: list[int]) -> int:
        # cur_max / cur_min = the largest and smallest product of a subarray that ENDS at the current index. best = the largest seen anywhere. All three start as the first element, the only subarray ending there.
        best = cur_max = cur_min = nums[0]
        for x in nums[1:]:
            # A subarray ending at x either starts fresh at x, or extends the best or worst product ending just before it. A negative x turns the worst into the best, which is why cur_min is carried along.
            candidates = (x, x * cur_max, x * cur_min)
            # Take both extremes from the same three candidates. The tuple assignment reads the old cur_max / cur_min before rebinding either.
            cur_max, cur_min = max(candidates), min(candidates)
            # The answer is the best product ending at any index, so update it after each one.
            best = max(best, cur_max)
        # best covers every non-empty subarray.
        return best
