from binary_search import search


def test_search():
    cases = [
        # (nums, target, expected)
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),      # absent, lo crosses hi
        ([1, 2, 3, 4, 5], 5, 4),            # last element, the case `while lo < hi` misses
        ([1, 2, 3, 4, 5], 1, 0),            # first element
        ([5], 5, 0),                        # single element, found
        ([5], -5, -1),                      # single element, absent
        ([], 1, -1),                        # empty array, loop body never runs
        ([2, 4, 6, 8], 5, -1),              # even length, target falls between two values
    ]

    failures = 0
    for nums, target, expected in cases:
        result = search(nums, target)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  nums={nums} target={target} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_search()
