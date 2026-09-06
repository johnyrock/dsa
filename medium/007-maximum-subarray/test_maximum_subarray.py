from maximum_subarray import max_sub_array


def test_max_sub_array():
    cases = [
        # (nums, expected)
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),                            # single element
        ([5, 4, -1, 7, 8], 23),              # whole array
        ([-3, -1, -2], -1),                  # all negative, pick the largest single element
        ([-1], -1),                          # single negative element
        ([0, 0, 0], 0),                      # all zeros
        ([2, -1, 2, -1, 2], 4),              # small dips are worth absorbing
        ([-2, -1], -1),
        ([1, -2, 3, -2, 5], 6),              # 3 + (-2) + 5 beats 5 alone
        ([8, -19, 5, -4, 20], 21),           # restart after a big negative, then absorb a small one
        ([-10000, 10000, -10000, 10000], 10000),
    ]

    failures = 0
    for nums, expected in cases:
        result = max_sub_array(list(nums))
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  nums={nums} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_max_sub_array()
