from palindrome import is_palindrome

cases = [
    # s, expected
    ('T"AC OCA T', True),
    ('CA R"AT', False),
    ('R" ACE C AR', True),
    ('"', False),
    ('', False),
]

def test_palindrome(cases):
    for s, expected in cases:
        result = is_palindrome(s)
        assert result == expected, f'{s!r} -> FAIL'
        print(f'{s!r} -> PASS')

test_palindrome(cases)