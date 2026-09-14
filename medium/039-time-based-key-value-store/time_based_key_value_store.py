class TimeMap:
    def __init__(self) -> None:
        self.times: dict[str, list[int]] = {}
        self.values: dict[str, list[str]] = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.times.setdefault(key, []).append(timestamp)
        self.values.setdefault(key, []).append(value)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.times:
            return ""
        times = self.times[key]
        lo, hi = 0, len(times)
        while lo < hi:
            mid = (lo + hi) // 2
            if times[mid] <= timestamp:
                lo = mid + 1
            else:
                hi = mid
        if lo == 0:
            return ""
        return self.values[key][lo - 1]
