from container_with_most_water import max_area


def test_max_area():
    cases = [
        # (height, expected)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),                          # minimum length
        ([4, 3, 2, 1, 4], 16),                # the two ends win
        ([1, 2, 1], 2),                       # width 2, height 1
        ([2, 3, 4, 5, 18, 17, 6], 17),        # two tall neighbours beat every wider pair
        ([0, 0, 0], 0),                       # all zero, no water
        ([5, 0, 5], 10),                      # zero in the middle does not matter
        ([1, 3, 2, 5, 25, 24, 5], 24),        # the tall pair in the middle, width 1
        ([10000] * 5, 40000),                 # upper bound heights, widest pair
        (list(range(1, 11)), 25),             # strictly increasing: index 4 (5) to index 9 (10)
    ]

    failures = 0
    for height, expected in cases:
        result = max_area(list(height))
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  height={height} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_max_area()
