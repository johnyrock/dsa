# Define the function that takes the original string s and the candidate anagram t.
def is_anagram(s, t):
    # If the two strings have different lengths they cannot use the same letters the same number of times. This is also what makes the single `return True` at the end safe.
    if len(s) != len(t):
        # Bail out immediately, before doing any counting work.
        return False
    # Create an empty dictionary that will map each character of s to the number of times it appears.
    counts = {}
    # Walk through s one character at a time to build the tally.
    for ch in s:
        # Add one to this character's running count. `get(ch, 0)` treats a character we have not seen yet as a count of zero.
        counts[ch] = counts.get(ch, 0) + 1
    # Now walk through t and try to cancel one copy of each character against the tally.
    for ch in t:
        # If t needs a character that s never had, or has already used up every copy of it, the strings cannot match.
        if counts.get(ch, 0) == 0:
            # t contains a character s cannot supply, so this is not an anagram.
            return False
        # Consume one copy of this character from the tally.
        counts[ch] -= 1
    # Every character of t was cancelled and the lengths matched, so every count landed back on zero. It is an anagram.
    return True
