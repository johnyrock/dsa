from letter_combinations_of_a_phone_number import Solution

solution = Solution()

for digits in ["23", "", "2", "79"]:
    print(repr(digits), solution.letter_combinations(digits))
