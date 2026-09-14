class TimeMap:
    # Two parallel lists per key: the timestamps and the values written at them. Kept separate so the binary search reads a plain list of ints.
    def __init__(self) -> None:
        self.times: dict[str, list[int]] = {}
        self.values: dict[str, list[str]] = {}

    # Timestamps arrive strictly increasing per key (guaranteed by the problem), so appending keeps each list sorted without any searching or shifting.
    def set(self, key: str, value: str, timestamp: int) -> None:
        # setdefault creates the empty list on the first write to this key and returns the existing one afterwards.
        self.times.setdefault(key, []).append(timestamp)
        self.values.setdefault(key, []).append(value)

    # Return the value whose timestamp is the largest one <= the requested timestamp, or "" if nothing that old exists.
    def get(self, key: str, timestamp: int) -> str:
        # A key that was never set has no history at all.
        if key not in self.times:
            return ""
        times = self.times[key]
        # Search for the insertion point just past every timestamp <= the target: hi is exclusive, so the range is [0, len(times)] and lo can end at len(times) when everything qualifies.
        lo, hi = 0, len(times)
        while lo < hi:
            mid = (lo + hi) // 2
            # <= rather than <: an exact timestamp match must count as "old enough", so the search moves past it rather than stopping on it.
            if times[mid] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        # lo is now the count of timestamps <= the target. Zero means every write is newer than what was asked for.
        if lo == 0:
            return ""
        # The last qualifying write sits one slot before the insertion point.
        return self.values[key][lo - 1]
