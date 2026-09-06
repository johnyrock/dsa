from merge_intervals import merge


def test_merge():
    cases = [
        # (intervals, expected)
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),                       # touching endpoints merge
        ([[1, 4], [2, 3]], [[1, 4]]),                       # one interval inside another
        ([[1, 4]], [[1, 4]]),                               # single interval
        ([[4, 7], [1, 4]], [[1, 7]]),                       # unsorted input
        ([[1, 4], [0, 4]], [[0, 4]]),                       # unsorted, same end
        ([[1, 4], [0, 0]], [[0, 0], [1, 4]]),               # unsorted, no overlap
        ([[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]),  # one big interval swallows everything
        ([[1, 2], [3, 4], [5, 6]], [[1, 2], [3, 4], [5, 6]]),    # nothing overlaps
        ([[1, 1], [1, 1], [1, 1]], [[1, 1]]),               # duplicate points
        ([[1, 3], [2, 4], [3, 5], [4, 6]], [[1, 6]]),       # chain of overlaps
    ]

    failures = 0
    for intervals, expected in cases:
        result = merge([list(iv) for iv in intervals])
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  intervals={intervals} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_merge()
