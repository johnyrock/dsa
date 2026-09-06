from product_of_array_except_self import product_except_self


def test_product_except_self():
    cases = [
        # (nums, expected)
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),       # one zero: only its own slot is non-zero
        ([2, 3], [3, 2]),                             # minimum length
        ([0, 0], [0, 0]),                             # two zeros: everything is zero
        ([0, 4, 5], [20, 0, 0]),                      # zero at the front
        ([4, 5, 0], [0, 0, 20]),                      # zero at the back
        ([1, 1, 1, 1], [1, 1, 1, 1]),                 # all ones
        ([-2, -3, 4], [-12, -8, 6]),                  # negatives, sign flips
        ([5, 1, 2], [2, 10, 5]),
        ([30, 30, 30, 30], [27000, 27000, 27000, 27000]),  # upper bound values
    ]

    failures = 0
    for nums, expected in cases:
        result = product_except_self(list(nums))
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  nums={nums} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_product_except_self()
