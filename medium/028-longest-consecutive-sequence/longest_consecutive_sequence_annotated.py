class Solution:
    # Return the length of the longest run of consecutive integers present in nums, regardless of their order in the array.
    def longest_consecutive(self, nums: list[int]) -> int:
        # A set gives O(1) "is this value present?" and collapses duplicates, which would otherwise be counted or walked twice.
        seen = set(nums)
        # The longest run found so far. 0 is right for an empty input.
        best = 0
        # Iterate the set, not the list, so duplicates are visited once.
        for num in seen:
            # If num - 1 is present, num is in the middle of a run that will be walked from its true start; skip it so each run is walked exactly once.
            if num - 1 in seen:
                continue
            # num is the smallest value of its run. Count it, then step upward while the next integer exists.
            length = 1
            while num + length in seen:
                length += 1
            # This run is fully measured; keep it if it beats the best.
            best = max(best, length)
        # Every run was walked once from its start, so best is the answer.
        return best
