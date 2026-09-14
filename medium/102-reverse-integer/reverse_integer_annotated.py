class Solution:
    # Reverse the decimal digits of a signed 32-bit integer, returning 0 if the reversed value would not fit.
    def reverse(self, x: int) -> int:
        # 2147483647. The overflow test below compares against INT_MAX // 10 = 214748364 and its last digit 7.
        INT_MAX = 2**31 - 1
        # Remember the sign and work on the magnitude, so % and // behave like plain digit extraction. (Python's -123 % 10 is 7, not 3.)
        sign = -1 if x < 0 else 1
        x = abs(x)
        # The reversed number, built one digit at a time from the low end of x.
        result = 0
        while x:
            # Peel the lowest digit off x ...
            digit = x % 10
            x //= 10
            # ... and before appending it, check that result * 10 + digit would still fit. If result is already past 214748364, any digit overflows; if it is exactly that, only digits up to 7 fit. The negative limit (…648) is never reached, since its reversal would need an input outside the 32-bit range.
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > 7):
                return 0
            # Shift the digits built so far one place left and drop the new one in the ones column.
            result = result * 10 + digit
        # Restore the sign; the magnitude was verified to fit.
        return sign * result
