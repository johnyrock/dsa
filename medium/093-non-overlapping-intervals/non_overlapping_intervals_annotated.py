class Solution:
    # Return the minimum number of intervals to remove so that the rest do not overlap.
    def erase_overlap_intervals(self, intervals: list[list[int]]) -> int:
        # Sort by END, not start. The interval that ends earliest leaves the most room for everything after it, so it is always safe to keep.
        intervals.sort(key=lambda interval: interval[1])
        # Count removals; the kept intervals are never materialised.
        removed = 0
        # The first interval in end order is always kept; prev_end is the right edge of the last kept interval.
        prev_end = intervals[0][1]
        # Sweep the rest in end order.
        for start, end in intervals[1:]:
            # Touching is not overlapping: a start equal to the previous end is fine, so >= keeps it.
            if start >= prev_end:
                # No conflict with anything kept so far, so keep it; it now has the latest end among kept intervals.
                prev_end = end
            else:
                # It starts before the last kept one ends. Since it also ends no earlier (end order), dropping it is the choice that frees the most room.
                removed += 1
        return removed
