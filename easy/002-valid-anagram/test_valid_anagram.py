from valid_anagram import is_anagram


def test_is_anagram():
    cases = [
        # (s, t, expected)
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aa", "a", False),                 # different lengths, must exit early
        ("a", "aa", False),                 # same mismatch the other way round
        ("a", "a", True),                   # single character
        ("aacc", "ccac", False),            # same letter set, wrong counts
        ("ab", "ba", True),                 # simple swap
        ("abc", "abd", False),              # same length, one letter differs
    ]

    failures = 0
    for s, t, expected in cases:
        result = is_anagram(s, t)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  s={s!r} t={t!r} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_is_anagram()
