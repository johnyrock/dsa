from anagram import is_anagram

cases = [
    # s, t, expected
    ("anagram", "nagaram", True),
    ("ab", "ba", True),
    ("abca", "acba", True),
    ("aa", "a", False),
    ("aa", "aaa", False),
    ("", "", True),
    ("rat", "car", False)
]

def test_anagram(cases):
    for s, t, expected in cases:
        if is_anagram(s, t) == expected:
            print(f'{s} | {t} -> PASS')
        else:
            print(f'{s} | {t} -> FAIL (expected = {expected})')

test_anagram(cases)