class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            # Even after rotation, at least one half of [left, mid, right] is
            # a contiguous sorted run. Figure out which half that is first.
            if nums[left] <= nums[mid]:
                # Left half [left..mid] is sorted normally.
                if nums[left] <= target < nums[mid]:
                    # target sits inside the sorted left half.
                    right = mid - 1
                else:
                    # target must be in the other (rotated) half.
                    left = mid + 1
            else:
                # Right half [mid..right] is sorted normally instead.
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
