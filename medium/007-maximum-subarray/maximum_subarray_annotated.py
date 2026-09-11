class Solution:
    # Define the function that takes the array and returns the largest sum of any non-empty contiguous subarray.
    def max_sub_array(self, nums: list[int]) -> int:
        # Seed both trackers with the first element. Starting at 0 would be wrong for all-negative arrays, where the answer is negative.
        best = nums[0]
        # current is the best sum of a subarray that ENDS exactly here. That is the subproblem: "best ending at i", not "best so far".
        current = nums[0]  # best sum of a subarray ending at the current index
        # One forward pass over the remaining elements.
        for x in nums[1:]:
            # Either extend the run that ended at the previous index by adding x, or abandon it and start fresh at x. If the previous run's sum was negative it can only drag x down, so max() picks the restart.
            current = max(x, current + x)  # extend the run, or restart at x
            # The overall answer is the best "ending here" value seen at any index.
            best = max(best, current)
        # best is the maximum subarray sum; the subarray itself is never stored because only its sum was asked for.
        return best
