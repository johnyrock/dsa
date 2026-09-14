import heapq


class Solution:
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda interval: interval[0])
        end_times = []
        for start, end in intervals:
            if end_times and end_times[0] <= start:
                heapq.heapreplace(end_times, end)
            else:
                heapq.heappush(end_times, end)
        return len(end_times)
