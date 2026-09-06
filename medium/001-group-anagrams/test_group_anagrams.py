from group_anagrams import group_anagrams


def normalize(groups):
    # Group order and order within a group are both unspecified, so canonicalise both.
    return sorted(sorted(g) for g in groups)


def test_group_anagrams():
    cases = [
        # (strs, expected)
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        ([""], [[""]]),                                     # single empty string is its own group
        (["a"], [["a"]]),                                   # single word
        (["", ""], [["", ""]]),                             # two empty strings are anagrams of each other
        (["abc", "bca", "cab", "cba"], [["abc", "bca", "cab", "cba"]]),
        (["ab", "ba", "abc"], [["ab", "ba"], ["abc"]]),     # prefix is not an anagram
        (["aab", "abb"], [["aab"], ["abb"]]),               # same letters, different counts
        (["bdddddddddd", "bbbbbbbbbbc"], [["bdddddddddd"], ["bbbbbbbbbbc"]]),  # sums of letters match, counts do not
        (["x", "y", "z"], [["x"], ["y"], ["z"]]),           # all singletons
    ]

    failures = 0
    for strs, expected in cases:
        result = group_anagrams(list(strs))
        status = "PASS" if normalize(result) == normalize(expected) else "FAIL"
        if status == "FAIL":
            failures += 1
        print(f"{status}  strs={strs} -> {result} (expected {expected})")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")


test_group_anagrams()
