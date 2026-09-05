from valid_parentheses import is_valid


def test_is_valid():
    cases = [
        # (s, expected)
        ("()", True),
        ("()[]{}", True),
        ("([]{})", True),                   # nested and sequential mixed
        ("([)]", False),                    # counts balance but the order crosses
        ("((", False),                      # leftover openers, stack not empty at the end
        (")", False),                       # closer with nothing open
        ("]", False),                       # single closer, minimum length
        ("{[()]}", True),                   # fully nested, three levels deep
    ]

    failures = 0
    for s, expected in cases:
        result = is_valid(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  s={s!r} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_is_valid()
