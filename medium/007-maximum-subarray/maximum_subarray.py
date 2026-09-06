def max_sub_array(nums):
    best = nums[0]
    current = nums[0]  # best sum of a subarray ending at the current index
    for x in nums[1:]:
        current = max(x, current + x)  # extend the run, or restart at x
        best = max(best, current)
    return best
