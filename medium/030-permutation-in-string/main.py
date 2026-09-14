from permutation_in_string import Solution

solution = Solution()

print(solution.check_inclusion("ab", "eidbaooo"))   # True, "ba" is a permutation of "ab"
print(solution.check_inclusion("ab", "eidboaoo"))   # False
print(solution.check_inclusion("adc", "dcda"))      # True, "cda"
