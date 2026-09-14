class Solution:
    def can_attend_meetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort(key=lambda interval: interval[0])
        for index in range(1, len(intervals)):
            if intervals[index][0] < intervals[index - 1][1]:
                return False
        return True
