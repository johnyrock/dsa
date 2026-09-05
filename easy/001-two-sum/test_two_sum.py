from two_sum import two_sum


def test_two_sum():
    cases = [
        # (nums, target, expected)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),                # duplicate values, must use both indices
        ([-1, -2, -3, -4], -6, [1, 3]),     # negatives
        ([0, 4, 3, 0], 0, [0, 3]),          # zero target
        ([1, 5], 6, [0, 1]),                # minimum length
        ([4, 1, 7], 8, [1, 2]),             # 4 + 4 = 8 but only one 4, so [0, 0] is wrong
        ([1, 2, 3], 100, []),               # no answer
    ]

    failures = 0
    for nums, target, expected in cases:
        result = two_sum(nums, target)
        status = "PASS" if sorted(result) == sorted(expected) else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  nums={nums} target={target} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_two_sum()
