class Solution:
    def climb_stairs(self, n: int) -> int:
        if n <= 2:
            return n
        two_back, one_back = 1, 2  # ways to reach step 1 and step 2
        for _ in range(3, n + 1):
            two_back, one_back = one_back, two_back + one_back
        return one_back
