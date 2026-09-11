class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = new_interval

        # Phase 1: intervals entirely before the new one (no overlap) go
        # straight to the output untouched.
        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        # Phase 2: every interval that overlaps the new one gets merged into
        # it. Overlap means `intervals[i][0] <= end` — its start is no later
        # than the merged interval's current end.
        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        # Phase 3: everything left starts after the merged interval ends, so
        # it goes straight to the output too.
        while i < n:
            result.append(intervals[i])
            i += 1

        return result
