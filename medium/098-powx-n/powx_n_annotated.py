class Solution:
    # Compute x raised to the integer power n in O(log n) multiplications.
    def my_pow(self, x: float, n: int) -> float:
        # A negative exponent is the same as a positive exponent of the reciprocal: x^-n = (1/x)^n. Flip both so the loop only ever sees n >= 0.
        if n < 0:
            x = 1 / x
            n = -n
        # The running product. Starts at 1 so that n = 0 returns 1 without any special case.
        result = 1.0
        # base holds x^(2^k) for the bit currently being examined: x, x^2, x^4, x^8, ...
        base = x
        # Consume n one bit at a time from the low end; the loop runs once per bit, so about log2(n) times.
        while n:
            # If the current lowest bit of n is 1, this power of two is part of the exponent, so fold the matching base into the result.
            if n & 1:
                result *= base
            # Square base so it becomes x^(2^(k+1)), ready for the next bit up. Done every iteration, whether or not the bit was set.
            base *= base
            # Drop the bit just examined.
            n >>= 1
        # Every set bit of n has contributed its power of x, so result is x^n.
        return result
