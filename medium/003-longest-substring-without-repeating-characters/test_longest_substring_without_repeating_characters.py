from longest_substring_without_repeating_characters import length_of_longest_substring


def test_length_of_longest_substring():
    cases = [
        # (s, expected)
        ("abcabcbb", 3),
        ("bbbbb", 1),              # all the same character
        ("pwwkew", 3),             # "wke"
        ("", 0),                   # empty string
        (" ", 1),                  # a single space is a character
        ("au", 2),                 # two distinct, whole string
        ("dvdf", 3),               # the stale-occurrence trap: left must not move backwards
        ("abba", 2),               # second trap: the 'a' at index 0 is outside the window when the last 'a' arrives
        ("tmmzuxt", 5),            # "mzuxt"
        ("abcdefg", 7),            # no repeats at all
        ("aab", 2),
        ("a1!a1!", 3),             # digits and symbols count as characters
    ]

    failures = 0
    for s, expected in cases:
        result = length_of_longest_substring(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  s={s!r} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_length_of_longest_substring()
