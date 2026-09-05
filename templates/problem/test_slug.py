from slug import solve


def test_solve():
    cases = [
        # (input, expected)
    ]

    failures = 0
    for args, expected in cases:
        result = solve(args)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  input={args} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_solve()
