def merge(intervals):
    intervals.sort(key=lambda iv: iv[0])
    merged = []
    for start, end in intervals:
        if merged and start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)  # overlap: extend the last one
        else:
            merged.append([start, end])              # gap: start a new interval
    return merged
