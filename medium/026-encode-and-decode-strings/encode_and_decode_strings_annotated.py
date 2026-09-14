class Solution:
    # Turn a list of strings into one string that can be split back exactly, whatever characters the strings contain.
    def encode(self, strs: list[str]) -> str:
        # Prefix each string with its length and a '#' terminator: "abc" becomes "3#abc". The length, not the '#', is what delimits, so a '#' inside a string is harmless. An empty list encodes to "" and an empty string to "0#".
        return "".join(f"{len(s)}#{s}" for s in strs)

    # Read the encoded string chunk by chunk, using each length header to know exactly how many characters to take.
    def decode(self, s: str) -> list[str]:
        # The strings recovered so far, in their original order.
        result = []
        # i is the start of the next length header. It only ever moves forward.
        i = 0
        # Stop when i has walked off the end; each iteration consumes exactly one "<len>#<chars>" chunk.
        while i < len(s):
            # Find the '#' that ends this header. Searching from i means a '#' inside an earlier payload is never seen, because i has already jumped past it.
            j = s.index("#", i)
            # The digits between i and the '#' are the payload length (possibly several digits, possibly 0).
            length = int(s[i:j])
            # The payload starts right after the '#' and is exactly `length` characters. Slicing never inspects the content, so any character is safe.
            result.append(s[j + 1:j + 1 + length])
            # Jump i to the character after the payload, which is the start of the next header.
            i = j + 1 + length
        # All chunks consumed; this is the original list.
        return result
