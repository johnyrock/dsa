class Solution:
    # Decide whether s can be a valid parenthesis string once every '*' is chosen to be '(', ')', or nothing.
    def check_valid_string(self, s: str) -> bool:
        # Track the range of possible "open count" values: lo assumes every '*' so far closed (or vanished), hi assumes every '*' opened.
        lo = hi = 0
        # One left-to-right pass; each character shifts the whole range.
        for ch in s:
            if ch == '(':
                # A real open bracket raises both bounds.
                lo += 1
                hi += 1
            elif ch == ')':
                # A real close bracket lowers both bounds.
                lo -= 1
                hi -= 1
            else:
                # A star widens the range: it could close (lo - 1) or open (hi + 1); the "empty" choice sits in between.
                lo -= 1
                hi += 1
            # If even the most generous reading has more ')' than '(' at this point, no choice of stars can rescue it.
            if hi < 0:
                return False
            # An open count cannot be negative, so clamp lo: the readings that would go below 0 are invalid and must be discarded, not carried forward.
            lo = max(lo, 0)
        # At the end, valid means an open count of exactly 0 is reachable; 0 is in [lo, hi] exactly when lo is 0, since hi is never negative here.
        return lo == 0
