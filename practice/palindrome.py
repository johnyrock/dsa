def is_palindrome(s):

    if not any(c.isalnum() for c in s):
        return False

    # T'AC OCAT
    left_index = 0
    right_index = len(s) - 1

    while left_index < right_index:
        while left_index < right_index and not s[left_index].isalnum():
            left_index += 1
        while left_index < right_index and not s[right_index].isalnum():
            right_index -= 1

        if s[left_index].lower() !=  s[right_index].lower():
            return False

        left_index += 1
        right_index -= 1

    return True