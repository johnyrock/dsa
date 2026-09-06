# Define the function that takes a list of [start, end] pairs and returns them with all overlaps merged.
def merge(intervals):
    # Sort by start. After this, any interval that overlaps the one we are building must come next in line, so one forward pass is enough.
    intervals.sort(key=lambda iv: iv[0])
    # The output list. Its last element is the interval currently being built; earlier elements are finished and can never grow again.
    merged = []
    for start, end in intervals:
        # Overlap test: because of the sort, this interval starts at or after the last merged one, so they overlap exactly when it starts before (or at) that one's end.
        if merged and start <= merged[-1][1]:
            # Extend the last merged interval. max() matters: the new interval might end earlier, as in [1, 4] swallowing [2, 3].
            merged[-1][1] = max(merged[-1][1], end)  # overlap: extend the last one
        else:
            # A gap, or the very first interval. Start a fresh one. A new list is created here so we never alias the caller's data.
            merged.append([start, end])              # gap: start a new interval
    return merged
