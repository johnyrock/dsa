s = "([]{})"

# ( ]
def is_valid_parenthesis(s):
    check = [] # (,
    pairs = {")":"(","]":"[","}":"{"}
    for ch in s:
        if ch in pairs:
            if not check or check.pop() != pairs.get(ch):
                return False
        else:
            check.append(ch)
    return not check