from longest_palindromic_substring import longest_palindrome


def test_longest_palindrome():
    cases = [
        # (s, set of accepted answers)
        ("babad", {"bab", "aba"}),
        ("cbbd", {"bb"}),                          # even length
        ("a", {"a"}),                              # single character
        ("ac", {"a", "c"}),                        # no repeat, any single character
        ("aaaa", {"aaaa"}),                        # whole string, even
        ("racecar", {"racecar"}),                  # whole string, odd
        ("abacdfgdcaba", {"aba"}),                 # two equal candidates that are the same text
        ("forgeeksskeegfor", {"geeksskeeg"}),      # long even palindrome in the middle
        ("bananas", {"anana"}),
        ("noonabbad", {"noon", "abba"}),           # two ties of length 4
        ("abcda", {"a", "b", "c", "d"}),           # nothing longer than 1
        ("xabbay", {"abba"}),                      # even palindrome not at an edge
        ("12321abc", {"12321"}),                   # digits count as characters
    ]

    failures = 0
    for s, accepted in cases:
        result = longest_palindrome(s)
        status = "PASS" if result in accepted else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  s={s!r} -> {result!r} (expected one of {sorted(accepted)})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_longest_palindrome()
