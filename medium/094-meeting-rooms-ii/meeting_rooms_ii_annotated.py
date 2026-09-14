import heapq


class Solution:
    # Return the minimum number of rooms so that no two meetings share a room while both are running.
    def min_meeting_rooms(self, intervals: list[list[int]]) -> int:
        # Process meetings in start order, so when one starts, every meeting that started earlier has already been assigned a room.
        intervals.sort(key=lambda interval: interval[0])
        # One entry per room in use: the time that room becomes free. A min-heap keeps the earliest-freeing room at index 0.
        end_times = []
        for start, end in intervals:
            # The room that frees up soonest is the only one worth checking: if it is still busy at `start`, every room is. `<=` because a meeting may start exactly when another ends.
            if end_times and end_times[0] <= start:
                # That room is free: reuse it. heapreplace pops the old end time and pushes the new one in a single sift, so the room count does not change.
                heapq.heapreplace(end_times, end)
            else:
                # No room is free yet: open a new one. The heap only ever grows here, so its size is the peak number of simultaneous meetings.
                heapq.heappush(end_times, end)
        # Every push that was not a reuse opened a room, and rooms are never closed, so the heap size is the answer.
        return len(end_times)
