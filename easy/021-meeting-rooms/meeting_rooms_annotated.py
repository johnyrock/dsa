class Solution:
    # Decide whether any pair of meetings overlaps.
    def can_attend_meetings(self, intervals: list[list[int]]) -> bool:
        # After sorting, only neighboring meetings can create a new conflict.
        intervals.sort(key=lambda interval: interval[0])
        # Compare each meeting to the one that ends immediately before it in sorted order.
        for index in range(1, len(intervals)):
            # A start before the previous end is an overlap.
            if intervals[index][0] < intervals[index - 1][1]:
                return False
        # No neighboring pair overlapped.
        return True
