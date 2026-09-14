class Solution:
    # Multiply two non-negative integers given as decimal strings, without converting either whole string to an int.
    def multiply(self, num1: str, num2: str) -> str:
        # A zero factor gives "0". Handling it up front avoids returning a string of zeros like "000".
        if num1 == "0" or num2 == "0":
            return "0"
        # A product of an m-digit and an n-digit number has at most m + n digits, so one cell per possible digit is enough.
        result = [0] * (len(num1) + len(num2))
        # Walk num1 from its least significant digit (the rightmost) to its most significant.
        for i in range(len(num1) - 1, -1, -1):
            # For each digit of num1, walk num2 the same way, so every pair of digits is multiplied exactly once.
            for j in range(len(num2) - 1, -1, -1):
                # The product of digit i and digit j lands at position i + j + 1 (its ones place) and i + j (its tens place). Add whatever is already sitting in the ones cell.
                total = int(num1[i]) * int(num2[j]) + result[i + j + 1]
                # Keep only the ones digit in its cell.
                result[i + j + 1] = total % 10
                # Carry the tens digit into the next cell to the left. It may exceed 9 for now; a later iteration normalises it when that cell becomes an i + j + 1 position.
                result[i + j] += total // 10
        # The leading cells may be 0 when the product is shorter than m + n digits. Skip them, but always keep at least one digit.
        start = 0
        while start < len(result) - 1 and result[start] == 0:
            start += 1
        # Glue the remaining digits into a string.
        return "".join(str(d) for d in result[start:])
