from climbing_stairs import climb_stairs


def test_climb_stairs():
    cases = [
        # (n, expected)
        (1, 1),                 # base case, only one move fits
        (2, 2),                 # base case, 1+1 or 2
        (3, 3),                 # first case the loop actually runs
        (4, 5),
        (5, 8),                 # the running example in the walkthrough
        (6, 13),                # off-by-one in the loop would give 21 here
        (10, 89),
        (45, 1836311903),       # upper constraint, must stay fast
    ]

    failures = 0
    for n, expected in cases:
        result = climb_stairs(n)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  n={n} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_climb_stairs()
