class Solution:
    # Define the function that takes a rotated sorted array of distinct values and returns its smallest element.
    def find_min(self, nums: list[int]) -> int:
        # Search the whole index range. hi is inclusive because nums[hi] is used as the anchor for every comparison.
        lo, hi = 0, len(nums) - 1
        # Stop when one index is left. lo < hi (not <=) because hi is never moved past a candidate, so lo and hi meet on the answer.
        while lo < hi:
            # Probe the middle. Rounding down means mid < hi whenever lo < hi, so lo = mid + 1 always makes progress.
            mid = (lo + hi) // 2
            # Compare against the right end, not the left. A sorted run never has a bigger value on its left than its right, so nums[mid] > nums[hi] proves the rotation point (the minimum) sits strictly to the right of mid.
            if nums[mid] > nums[hi]:
                # Everything from lo through mid belongs to the larger, left-hand run. Skip mid too: it is bigger than nums[hi], so it cannot be the minimum.
                lo = mid + 1
            # Otherwise nums[mid] <= nums[hi], so mid through hi is a sorted run whose smallest value is nums[mid]. The minimum is mid or something to its left.
            else:
                # Keep mid in the range because it might be the minimum itself.
                hi = mid
        # lo == hi here, and it is the index the search never ruled out: the rotation point.
        return nums[lo]
