class Solution:
    def insert(self, intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
        result = []
        i, n = 0, len(intervals)
        start, end = new_interval

        while i < n and intervals[i][1] < start:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        result.append([start, end])

        while i < n:
            result.append(intervals[i])
            i += 1

        return result
