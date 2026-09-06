from three_sum import three_sum


def normalize(triplets):
    # Triplet order and order within a triplet are unspecified, so canonicalise both.
    return sorted(sorted(t) for t in triplets)


def test_three_sum():
    cases = [
        # (nums, expected)
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),                                  # no zero-sum triplet
        ([0, 0, 0], [[0, 0, 0]]),                         # one triplet from three zeros
        ([0, 0, 0, 0], [[0, 0, 0]]),                      # still one triplet, not four
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),     # duplicate 1s form a valid pair once
        ([1, 2, 3], []),                                  # all positive, early break
        ([-3, -2, -1], []),                               # all negative
        ([-1, -1, -1, 2], [[-1, -1, 2]]),                 # three copies of the first value
        ([3, 0, -2, -1, 1, 2], [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
         [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ]

    failures = 0
    for nums, expected in cases:
        result = three_sum(list(nums))
        status = "PASS" if normalize(result) == normalize(expected) else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  nums={nums} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_three_sum()
