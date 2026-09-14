from encode_and_decode_strings import Solution

solution = Solution()

strs = ["neet", "code", "love", "you"]
encoded = solution.encode(strs)
print(encoded)
print(solution.decode(encoded))
print(solution.decode(solution.encode(["we", "say", ":", "yes", "#", ""])))
