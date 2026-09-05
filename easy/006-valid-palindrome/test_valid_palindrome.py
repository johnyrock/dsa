from valid_palindrome import is_palindrome


def test_is_palindrome():
    cases = [
        # (s, expected)
        ("A man, a plan, a canal: Panama", True),
        ("No 'x' in Nixon", True),           # mixed case plus apostrophes
        ("race a car", False),               # "raceacar" is not a palindrome
        ("", True),                          # empty string
        (" ", True),                         # only whitespace, nothing to compare
        (".,;'", True),                      # only punctuation, nothing to compare
        ("12321", True),                     # digits count as alphanumeric
        ("0P", False),                       # '0' and 'P' are not equal after lowering
    ]

    failures = 0
    for s, expected in cases:
        result = is_palindrome(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  s={s!r} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_is_palindrome()
