from parenthesis import is_valid_parenthesis

cases = [
    # s, expected
    ("({}[])", True),
    ("){}", False),
    ("", True),
    ("([]}{)", False),
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("(", False),
    (")", False),
    ("((", False),
    ("(()", False),
    ("())", False),
]

def test_parenthesis(cases):
    for s, expected in cases:
        result = is_valid_parenthesis(s)
        assert result==expected, f'{s!r} -> FAIL, expected {expected}'
        print(f'{s!r} -> PASS')

# def test_parenthesis(cases):
#     for s, expected in cases:
#         result = is_valid_parenthesis(s)
#         assert result == expected, f'{s!r} -> FAIL (got {result}, expected {expected})'
#         print(f'{s!r} -> PASS')

test_parenthesis(cases)
