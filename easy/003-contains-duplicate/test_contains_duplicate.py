from contains_duplicate import contains_duplicate


def test_contains_duplicate():
    cases = [
        # (nums, expected)
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),                          # single element, nothing to repeat
        ([2, 2], True),                        # shortest possible duplicate
        ([-1, -2, -3, -1], True),              # negatives
        ([0, 4, 3, 0], True),                  # zero counts like any other value
        ([5, -5, 10, -10], False),             # same magnitudes, different signs, all distinct
    ]

    failures = 0
    for nums, expected in cases:
        result = contains_duplicate(nums)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  nums={nums} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_contains_duplicate()
